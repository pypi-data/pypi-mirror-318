#!/usr/bin/env python
"""
Create JUNO production

Usage:
   ihepdirac-juno-make-reconstruction [option|cfgfile] [process]

Example:
   $ihepdirac-juno-make-reconstruction --example > rec.ini
   $ihepdirac-juno-make-reconstruction --ini myrec.ini
   $ihepdirac-juno-make-reconstruction ChainIBD
   $ihepdirac-juno-make-reconstruction --ini myrec.ini --dryrun
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__RCSID__ = "$Id$"

from DIRAC import S_OK, S_ERROR, gLogger, exit
from DIRAC.Core.Base.Script import Script

import os
import sys
import re
import configparser
import json


from DIRAC.ConfigurationSystem.Client.Helpers import Registry
from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

from DIRAC.TransformationSystem.Client.Transformation import Transformation
from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient

from DIRAC.Core.Workflow.Parameter import Parameter

DEBUG = True

CVMFS_ROOT = '/cvmfs/dcomputing.ihep.ac.cn/frontend/prodsys/scripts'

PROD_EXAMPLE = '''\
; Parameters could be put in the [all] section, or the process specified section
; The parameters in the specified section will overwrite those in the [all] section

; Common parameters
[all]
; Dryrun mode will only test the configuration and do not really submit any jobs
; This can also be passed in the command argument
;dryrun = true

; The process name "Chain" indicates that more parameters are selected from the [Chain] section
; This can also be passed in the command argument
process = Chain

; JUNO software version
softwareVersion = centos7_amd64_gcc1120/Pre-Release/J23.1.0-rc5.dc1

prodName = JUNORecTest

; The prodNameSuffix will be added to the prodName in order to solve the transformation name confliction
;prodNameSuffix = _new

; The transformation group name
transGroup = JUNO_rec_test

; If outputType is "reconstruction", the root directory will be /juno/data/rec
; If outputType is "user" or something else, the root directory will be under your user directory /juno/user/x/xxx
;outputType = reconstruction 

; The sub directory relative to the root directory
outputSubDir = zhangxm/test001

;outputSE = IHEP-STORM

; "closest" means upload the job output data to the closest SE
; If no closest SE is found for this site, then upload to the SE defined by "outputSE"
outputMode = closest

; If no site specified, all available sites will be chosen
;site = GRID.INFN-CNAF.it GRID.IN2P3.fr
;bannedsite = GRID.IHEP.cn

moveFlavor = Replication

; How many files to move in a single request
;moveGroupSize = 10

;moveSourceSE = IHEP-STORM CNAF-STORM JINR-JUNO IN2P3-DCACHE
;moveSourceSE = CNAF-STORM JINR-JUNO IN2P3-DCACHE
;moveTargetSE = IHEP-STORM CNAF-STORM
moveTargetSE = IHEP-STORM
movePlugin = Broadcast
;movePlugin = Standard

; The parameters in this section will overwrite what's in [all]
[Chain]
; maximum event num in a job, default is -1 with full events
evtmax = -1
seed = 1
; How many files to be put in one directory
max2dir = 10000
; How many cores to be used. The default is 1
ncores = 8

; Define metadata for input data
inputQuery = {"Type":"RTRAWtest", "Block":"202310_rc5"}

; The root directory will be /<outputType dir>/<outputSubDir>/<softwareVersion>/<workDir>. default is workDir = Process
; workDir =

; workflow = cal rec rawrec
workflow = rawrec
moveType = rawrec

; Add more parameters except common parameters: 
;rawrec-mode = --output-in-thread
rawrec-mode = --output-in-thread --global-tag J23.1.0-dc1 --pmtcalibsvc-ReadDB 1 --conddb-update-mode event

'''


def _setMetaData(directory, meta):
    fcc = FileCatalogClient()
    res = fcc.createDirectory(directory)
    if not res['OK']:
        raise Exception('DFC createDirectory for "{0}" error: {1}'.format(
            directory, res['Message']))
    res = fcc.setMetadata(directory, meta)
    if not res['OK']:
        raise Exception('DFC setMetadata for "{0}" error: {1}'.format(
            directory, res['Message']))


def _getMetaData(directory):
    fcc = FileCatalogClient()
    res = fcc.getDirectoryUserMetadata(directory)
    if not res['OK']:
        return {}
    return res['Value']

def _checkProxy():
    """checks if the proxy has the ProductionManagement property and belongs to a VO"""
    proxyInfo = getProxyInfo()
    gLogger.debug("DEBUG: the proxyInfo used now: %s\n", proxyInfo)
    if not proxyInfo['OK']:
      gLogger.error("ERROR: No Proxy present")
      return False
    proxyValues = proxyInfo.get('Value', {})
    group = proxyValues.get('group', '')

    groupProperties = proxyValues.get('groupProperties', [])

    if groupProperties:
      if 'ProductionManagement' not in groupProperties:
        gLogger.error("ERROR: Not allowed to create production, you need a ProductionManagement proxy.")
        return False
    else:
      gLogger.error("ERROR: Could not determine Proxy properties, you do not have the right proxy.")
      return False
    return True

class Param(object):
    def __init__(self, configFile='', paramCmd={}):
        self.__configFile = configFile
        self.__paramCmd = paramCmd

        self.__param = {}
        self.__loadParam()
        self.__processParam()

        gLogger.debug('Final param: {0}'.format(self.__param))

    def __loadParam(self):
        if not self.__configFile:
            return
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(self.__configFile)
        self.__param.update(dict(config.items('all')))
        self.__param.update(self.__paramCmd)
        if 'process' in self.__param:
            self.__param.update(dict(config.items(self.__param['process'])))
        self.__param.update(self.__paramCmd)    # Update paramCmd again to overwrite ini

    def __processParam(self):
        def parseList(s):
            return s.strip().split()

        def parseBool(s):
            if s.lower() in ['true', 'yes']:
                return True
            return False

        for key in ['softwareVersion', 'process']:
            if key not in self.__param or not self.__param[key]:
                raise Exception('Param "{0}" must be specified'.format(key))

        self.__param.setdefault('prodName', 'JUNOProd')
        self.__param.setdefault('transGroup', 'JUNO-Prod')
        self.__param.setdefault('outputType', 'user')
        self.__param.setdefault('outputSE', 'IHEP-STORM')
        self.__param.setdefault('outputMode', 'closest')
        self.__param.setdefault('seed', '1')
        self.__param.setdefault('workDir', self.__param['process'])
        self.__param.setdefault('moveFlavor', 'Replication')
        self.__param.setdefault('movePlugin', 'Broadcast')
        self.__param.setdefault('ncores', '1')

        self.__param['numberOfTasks'] = int(self.__param.get('njobs', '1'))
        self.__param['evtmax'] = int(self.__param.get('evtmax', '1'))
        self.__param['ncores'] = int(self.__param.get('ncores', '1'))
        self.__param['max2dir'] = int(self.__param.get('max2dir', '10000'))
        self.__param['userOutput'] = int(self.__param.get('userOutput', '1'))
        self.__param['moveGroupSize'] = int(
            self.__param.get('moveGroupSize', '10'))

        self.__param['site'] = parseList(self.__param.get('site', ''))
        self.__param['bannedsite'] = parseList(self.__param.get('bannedsite', ''))
        self.__param['workflow'] = parseList(self.__param.get('workflow', ''))
        self.__param['moveType'] = parseList(self.__param.get('moveType', ''))
        self.__param['moveSourceSE'] = parseList(
            self.__param.get('moveSourceSE', 'IHEP-STORM'))
        self.__param['moveTargetSE'] = parseList(
            self.__param.get('moveTargetSE', 'IHEP-STORM'))

        self.__param['dryrun'] = parseBool(self.__param.get('dryrun', 'false'))
        
        self.__param['inputQuery'] = self.__param.get('inputQuery', '')
    # TODO: change inputQuery into inputMeta, a dictionary type
    

    @property
    def param(self):
        return self.__param


class ProdMove(object):
    def __init__(self, transType, transGroup, transName='unknown', flavour='Replication', description='Production move',
                 plugin='Broadcast', inputMeta={}, sourceSE=[], targetSE='IHEP-STORM', groupSize=1):
        self.__transType = transType
        self.__transGroup = transGroup
        self.__transName = transName
        self.__flavour = flavour
        self.__description = description
        self.__plugin = plugin
        self.__inputMeta = inputMeta
        self.__sourceSE = sourceSE
        self.__targetSE = targetSE
        self.__groupSize = groupSize

    def createTransformation(self):
        ########################################
        # Transformation definition
        ########################################
        t = Transformation()

        t.setTransformationName(self.__transName)
        t.setType(self.__transType)
        t.setDescription(self.__description)
        t.setLongDescription(self.__description)
        t.setGroupSize(self.__groupSize)
        if self.__transGroup:
            t.setTransformationGroup(self.__transGroup)
        t.setPlugin(self.__plugin)

        t.setTargetSE(self.__targetSE)

        transBody = '' 

        t.setBody(transBody)

        ########################################
        # Transformation submission
        ########################################
        res = t.addTransformation()
        if not res['OK']:
            raise Exception(
                'Add transformation error: {0}'.format(res['Message']))

        t.setStatus("Active")
        t.setAgentType("Automatic")

        currtrans = t.getTransformationID()['Value']

        if self.__inputMeta:
            client = TransformationClient()
            res = client.createTransformationMetaQuery(
                currtrans, self.__inputMeta, 'Input')
            if not res['OK']:
                raise Exception(
                    'Create transformation query error: {0}'.format(res['Message']))

        return str(currtrans)


class ProdStep(object):
    def __init__(self, executable, transType, transGroup, softwareVersion,
                 application, stepName='unknown', description='Reconstruction step',
                 inputMeta={}, extraArgs='', inputData=None,
                 outputPath='/juno/test/prod', outputSE='IHEP-STORM', outputPattern='*.root',
                 site=None, bannedsite=None, outputMode='closest', maxNumberOfTasks=1, ncores=1):
        self.__executable = executable
        self.__transType = transType
        self.__transGroup = transGroup
        self.__softwareVersion = softwareVersion
        self.__application = application
        self.__stepName = stepName
        self.__description = description
        self.__inputMeta = inputMeta
        self.__extraArgs = extraArgs
        self.__inputData = inputData
        self.__outputPath = outputPath
        self.__outputSE = outputSE
        self.__outputPattern = outputPattern
        self.__site = site
        self.__bannedsite = bannedsite
        self.__outputMode = outputMode
        self.__maxNumberOfTasks = maxNumberOfTasks
        self.__ncores=ncores

        self.__job = None

    def createJob(self):
        from DIRAC.Interfaces.API.Job import Job
        job = Job()
        job.setName(self.__stepName)
        job.setOutputSandbox(['*log'])

        arguments = '"{0}" "{1}" "{2}" "{3}" "{4}" "{5}" @{{JOB_ID}}'.format(
            self.__softwareVersion, self.__application, self.__outputPath,
            self.__outputPattern, self.__outputSE, self.__outputMode)
        if self.__extraArgs:
            arguments += ' ' + self.__extraArgs

        # for cvmfs version
        job.setExecutable('"{0}/{1}"'.format(CVMFS_ROOT, self.__executable), arguments=arguments)

        # failover for failed jobs
        #job.setExecutable('/bin/ls -l', modulesList=['Script', 'FailoverRequest'])

        if self.__inputData:
            job.setInputData(self.__inputData)

        if self.__site:
            job.setDestination(self.__site)

        if self.__bannedsite:
            job.setBannedSites(self.__bannedsite)
        
        job.setNumberOfProcessors(self.__ncores)
        job.setOutputSandbox(['app.out','app.err','Script3_CodeOutput.log','Script1_CodeOutput.log','frontier.log'])

        self.__job = job

    def submitJob(self):
        from DIRAC.Interfaces.API.Dirac import Dirac
        dirac = Dirac()
        res = dirac.submitJob(self.__job)
        gLogger.notice('Job submitted: {0}'.format(res["Value"]))
        return res

    def createTransformation(self):
        ########################################
        # Transformation definition
        ########################################
        t = Transformation()

        t.setTransformationName(self.__stepName)
        t.setType(self.__transType)
        t.setDescription(self.__description)
        t.setLongDescription(self.__description)
        t.setGroupSize(1)
        if self.__transGroup:
            t.setTransformationGroup(self.__transGroup)
        # set the job workflow to the transformation
        t.setBody(self.__job.workflow.toXML())

        ########################################
        # Transformation submission
        ########################################
        res = t.addTransformation()
        if not res['OK']:
            raise Exception(
                'Add transformation error: {0}'.format(res['Message']))

        t.setStatus("Active")
        t.setAgentType("Automatic")

        currtrans = t.getTransformationID()['Value']

        if self.__inputMeta:
            client = TransformationClient()
            res = client.createTransformationMetaQuery(
                currtrans, self.__inputMeta, 'Input')
            if not res['OK']:
                raise Exception(
                    'Create transformation query error: {0}'.format(res['Message']))

        return str(currtrans)


class ProdChain(object):
    def __init__(self, param):
        self.__param = param
        self.__transIDs = {}

        self.__prodPrefix = '{0}{1}-{2}-{3}'.format(param['prodName'], param.get(
            'prodNameSuffix', ''), param['softwareVersion'], param['workDir'])

        self.__ownerAndGroup()

        outputSubDir = self.__param['outputSubDir'].strip('/')
        if self.__param['outputType'] == 'reconstruction':
            self.__outputRoot = os.path.join(self.__prodHome, outputSubDir)
        else:
            self.__outputRoot = os.path.join(self.__userHome, outputSubDir)

        self.__prepareDir()

        gLogger.notice('Owner: {0}'.format(self.__owner))
        gLogger.notice('OwnerGroup: {0}'.format(self.__ownerGroup))
        gLogger.notice('VO: {0}'.format(self.__vo))
        gLogger.notice('OutputRoot: {0}'.format(self.__outputRoot))
        gLogger.notice('ProdRoot: {0}'.format(self.__prodRoot))
        gLogger.notice('ProdPrefix: {0}'.format(self.__prodPrefix))

    def __ownerAndGroup(self):
        res = getProxyInfo(False, False)
        if not res['OK']:
            raise Exception('GetProxyInfo error: {0}'.format(res['Message']))
        self.__owner = res['Value']['username']
        self.__ownerGroup = res['Value']['group']
        self.__vo = Registry.getVOMSVOForGroup(self.__ownerGroup)
        self.__voHome = '/{0}'.format(self.__vo)
        self.__prodHome = '/{0}/data/rec'.format(self.__vo)
        self.__userHome = '/{0}/user/{1:.1}/{1}'.format(
            self.__vo, self.__owner)

    def __prepareDir(self):
        outputPath = self.__outputRoot
        for d in ['softwareVersion', 'workDir']:
            if d == 'workDir':
                key = 'process'
            else:
                key = d
            outputPath = os.path.join(outputPath, self.__param[d])
            _setMetaData(outputPath, {key: self.__param[key]})

        self.__prodRoot = outputPath

    def __getOutputPath(self, application):
        #print("application path", os.path.join(self.__prodRoot, application))
        return os.path.join(self.__prodRoot, application)

    def __getTransID(self, application):
        meta = _getMetaData(self.__getOutputPath(application))
        if 'transID' not in meta:
            return ''
        return meta['transID']

    def __getMeta(self, application):
        if not application:
            return {}

        meta = {}
        meta['softwareVersion'] = self.__param['softwareVersion']
        meta['process'] = self.__param['process']
        meta['application'] = application

        transID = self.__getTransID(application)
        if transID:
            meta['transID'] = transID

        return meta

    def __setMeta(self, application):
        outputPath = self.__prodRoot

        meta = {}
        meta['application'] = application
        if application in self.__transIDs:
            meta['transID'] = self.__transIDs[application]
        outputPath = os.path.join(outputPath, application)
        print("set meta data:", outputPath, meta)
        _setMetaData(outputPath, meta)

    def createStep(self, application, transType, prevApp=None, inputMeta={}):
        if prevApp:
            inputMeta = self.__getMeta(prevApp)
            if 'transID' not in inputMeta:
                gLogger.error('{0}: Transformation not found for previous application "{1}"'.format(
                    application, prevApp))
                return
            gLogger.notice('{0}: Input transformation "{1}" from "{2}"'.format(
                application, inputMeta['transID'], prevApp))

        step_mode = self.__param.get(application + '-mode', '')
        step_preScripts = self.__param.get(application + '-preScripts', '')
        if step_mode:
            gLogger.notice('{0}-mode: {1}'.format(application, step_mode))
        if step_preScripts:
            gLogger.notice('{0}-preScripts: {1}'.format(application, step_preScripts))


        extraArgs = '{0} {1} "{2}" {3} {4} "{5}" {6}'.format(
            self.__param['evtmax'], self.__param['seed'], step_mode, self.__param['max2dir'], self.__param['userOutput'], step_preScripts, self.__param['ncores'])
        stepArg = dict(
            executable='bootstrap.sh',
            transType=transType,
            transGroup=self.__param.get('transGroup'),
            softwareVersion=self.__param['softwareVersion'],
            application=application,
            stepName='{0}-{1}'.format(self.__prodPrefix, application),
            description='{0} for {1}'.format(
                application, self.__param['process']),
            extraArgs=extraArgs,
            inputMeta=inputMeta,
            outputPath=self.__getOutputPath(application),
            outputSE=self.__param['outputSE'],
            outputPattern='{0}*-*.root'.format(application),
            site=self.__param.get('site'),
            bannedsite=self.__param.get('bannedsite'),
            outputMode=self.__param['outputMode'],
            maxNumberOfTasks=self.__param['numberOfTasks'],
            ncores=self.__param['ncores']
        )

        print("inputMeta:", inputMeta)

        gLogger.notice('{0}: Create transformation...'.format(application))

        if self.__param['dryrun']:
            transID = 'dryrun'
        else:
            prodStep = ProdStep(**stepArg)
            prodStep.createJob()
            transID = prodStep.createTransformation()

        #self.__transIDs.setdefault({})
        self.__transIDs[application] = transID

        if not self.__param['dryrun']:
            self.__setMeta(application)

    def createMove(self, application, transType):
        inputMeta = self.__getMeta(application)
        if 'transID' not in inputMeta:
            gLogger.error(
                '{0}-move: Transformation not found for application "{0}"'.format(application))
            return
        gLogger.notice(
            '{0}-move: Input transformation "{1}" from "{0}"'.format(application, inputMeta['transID']))

        moveArg = dict(
            transType=transType,
            transGroup=self.__param.get('transGroup'),
            transName='{0}-{1}-{2}'.format(self.__prodPrefix,
                                               application, self.__param.get('moveFlavor')),
            flavour=self.__param.get('moveFlavor'),
            description='Move {0} for {1}'.format(
                application, self.__param['process']),
            plugin=self.__param['movePlugin'],
            inputMeta=inputMeta,
            sourceSE=self.__param['moveSourceSE'],
            targetSE=self.__param['moveTargetSE'],
            groupSize=self.__param['moveGroupSize'],
        )

        gLogger.notice(
            '{0}-move: Create transformation...'.format(application))

        if self.__param['dryrun']:
            transID = 'dryrun'
        else:
            prodMove = ProdMove(**moveArg)
            transID = prodMove.createTransformation()

    def createAllTransformations(self):
  
        inputMeta = json.loads(self.__param['inputQuery'])
        gLogger.notice('\nInput metadata: {0}'.format(inputMeta))

        for step in ['elecsim','calib', 'rec', 'rawrec']:
            if step not in self.__param['workflow']:
                continue

            if step == 'elecsim':
                self.createStep('elecsim','ElecSimulation-JUNO',None, inputMeta)
            if step == 'calib':
                self.createStep('calib','Calibration-JUNO', 'elecsim')
            if step == 'rec':
                self.createStep('rec','DataReconstruction-JUNO', 'calib')
            if step == 'rawrec':
                self.createStep('rawrec', 'DataReconstruction-JUNO', None, inputMeta)
                #self.createStep('rec', 'DataReconstruction-JUNO', 'calib')

        for step in ['elecsim','calib','rec', 'rawrec']:
            if step not in self.__param['moveType']:
                continue
            gLogger.notice('createMove-step:{0}'.format(step))
            self.createMove(step, 'Replication-JUNO')
@Script()
def main():

    if not _checkProxy():
       gLogger.error('ERROR: You don\'t have proper proxy to use prodSys!')
       return 1

    Script.registerSwitch('i:', 'ini=', 'Ini file, default to "prod.ini"')
    Script.registerSwitch(
       'r', 'dryrun', 'Only parse the configuration, do not submit transformation')
    Script.registerSwitch('e', 'example', 'Display prod.ini example')
    Script.parseCommandLine(ignoreErrors=False)

    args = Script.getPositionalArgs()
    switches = Script.getUnprocessedSwitches()

    configFile = 'rec.ini'
    paramCmd = {}
    displayExample = False

    for k, v in switches:
        if k == 'i' or k == 'ini':
            configFile = v
        if k == 'r' or k == 'dryrun':
            paramCmd['dryrun'] = 'true'
        if k == 'e' or k == 'example':
            displayExample = True

    if displayExample:
        sys.stdout.write(PROD_EXAMPLE)
        return 0

    if args:
        paramCmd['process'] = args[0]

    par = Param(configFile, paramCmd)

    chain = ProdChain(par.param)
    chain.createAllTransformations()

    return 0


if __name__ == '__main__':
    try:
        exit(main())
    except Exception as e:
        if DEBUG:
            raise
        gLogger.error('{0}'.format(e))
        exit(1)
