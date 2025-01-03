#!/usr/bin/env python
"""
Register files in EOS SE Directory to DFC.

Usage:
  ihepdirac_dms_register_EOS_files [option|cfgfile] DFCDir EosDir SE 

Example:
  $ ihepdirac_dms_register_EOS_files /juno/raw/test_register root://junoeos01.ihep.ac.cn:1094//eos/juno/dirac/juno/raw/test_register IHEP-JUNOEOS
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__RCSID__ = "$Id$"

from DIRAC.Core.Base.Script  import Script
from DIRAC import S_OK, S_ERROR, gLogger, exit

import sys
import os

from XRootD import client
from XRootD.client.flags import QueryCode

from DIRAC.Core.Utilities.Adler import fileAdler
from DIRAC.Core.Utilities.File import makeGuid
from DIRAC.DataManagementSystem.Client.DataManager import DataManager

from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
fcc = FileCatalogClient('DataManagement/FileCatalog')

@Script()
def main():
    Script.parseCommandLine(ignoreErrors = False)
    args = Script.getPositionalArgs()

    if len(args) != 3:
        Script.showHelp()
        exit(1)

    dfcRoot = args[0]
    eosRoot = args[1] 
    toSE = args[2]

    group = eosRoot.split("//")
    eosHead = group[0] + "//" + group[1] + "/" 
    eosPath = "/" + group[2]

    lfnQuery = []
    existCheck = False
    bufferSize = 100
    switches = Script.getUnprocessedSwitches()
    for switch in switches:
        if switch[0] == 'q' or switch[0] == 'querySkip':
            result = fcc.findFilesByMetadata({'juno_transfer': switch[1]}, '/')
            if result['OK']:
                lfnQuery += result['Value']
        if switch[0] == 'e' or switch[0] == 'existCheck':
            existCheck = True
        if switch[0] == 'b' or switch[0] == 'bufferSize':
            bufferSize = int(switch[1])

    lfnQuery = set(lfnQuery)

    counter = 0
    eosclient = client.FileSystem(eosRoot)

    dm = DataManager()
    fileTupleBuffer = []

    cmd = 'xrdfs %s ls %s -R' % (eosHead, eosPath)
    gLogger.debug('Commands to get files:%s' % (cmd))
    file_obj = os.popen(cmd).readlines()
    #gLogger.debug('file lists:%s' % (file_obj))
    for fullFn in file_obj:
        counter += 1
        fullFn=fullFn.strip('\n')
        gLogger.debug('fullFn:%s' % (fullFn))

        if not fullFn.startswith(eosPath):
            gLogger.error('%s does not start with %s' % (fullFn, localDir))
            continue 
        lastPart = fullFn[len(eosPath):]
        pfn = eosHead + fullFn
      
        lfn = dfcRoot + lastPart
        gLogger.debug('lfn, dfcRoot, lastPart:%s, %s, %s' % (lfn, dfcRoot, lastPart))

        if lfn in lfnQuery:
            gLogger.notice('File exists, skip: %s' % lfn)
            counter -= 1
            continue

        if existCheck:
            result = fcc.isFile(lfn)
            if result['OK'] and lfn in result['Value']['Successful'] and result['Value']['Successful'][lfn]:
                gLogger.notice('File exists, skip: %s' % lfn)
                counter -= 1
                continue

        status, response = eosclient.stat(fullFn)
        if status.ok:
            size = response.size
        else:
            gLogger.error('Error in getting size of %s!' % lfn)
            continue
        # 19 is a directory
        if response.flags == 19:
           gLogger.debug('%s is a directory' % lfn)
           counter -= 1
           continue

        status, response = eosclient.query(QueryCode.CHECKSUM, fullFn)
        if status.ok:
            gchecksum = response.split()
        else:
            gLogger.error('%s is not a file, or has problems to get checksum!')% lfn
            continue
        if size != 0:
            #adler32 = gchecksum[1].strip(b'\x00'.decode())
            adler32 = gchecksum[1].strip(b'\x00')
            guid = makeGuid()
            fileTuple = ( lfn, pfn, size, toSE, guid, adler32 )
            gLogger.debug('To be registered: %s %s %s %s %s %s' % (lfn,pfn,size,toSE,guid,adler32))
            fileTupleBuffer.append(fileTuple)
            gLogger.debug('Register lfn: %s' % lfn)
        else:
            counter -=1

        if len(fileTupleBuffer) >= bufferSize:
            result = dm.registerFile( fileTupleBuffer )
            if not result['OK']:
                gLogger.error('Can not register %s' % pfn)
                exit(1)
            del fileTupleBuffer[:]
            gLogger.notice('%s files registered' % counter)

    if fileTupleBuffer:
        result = dm.registerFile( fileTupleBuffer )
        if not result['OK']:
            gLogger.error('Can not register %s' % fullFn)
            exit(1)
        del fileTupleBuffer[:]

    gLogger.notice('Total %s files registered' % counter)

if __name__ == "__main__":
    main()
