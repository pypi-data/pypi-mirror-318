''' SAMTestAgent

  This agent executes SAM tests and evaluates resources and sites SAM status.

'''

import threading
from datetime import datetime
from DIRAC                                             import S_OK, gConfig, gLogger
from DIRAC.Core.Base.AgentModule                       import AgentModule
from DIRAC.Core.DISET.RPCClient                        import RPCClient
from IHEPDIRAC.ResourceStatusSystem.Utilities          import CSHelpers
from DIRAC.DataManagementSystem.Client.DataManager                 import DataManager
from DIRAC.ResourceStatusSystem.Utilities import Utils
from IHEPDIRAC.ResourceStatusSystem.Client.ResourceManagementIHEPClient import ResourceManagementIHEPClient
from IHEPDIRAC.ResourceStatusSystem.SAM.TestExecutor                import TestExecutor
from IHEPDIRAC.ResourceStatusSystem.SAM.StatusEvaluator             import StatusEvaluator
from IHEPDIRAC.ResourceStatusSystem.Utilities import BESUtils
from DIRAC.Interfaces.API.DiracAdmin import DiracAdmin


__RCSID__ = '$Id:  $'
AGENT_NAME = 'ResourceStatus/SAMTestAgent'


class SAMTestAgent(AgentModule):
  """ SAMTestAgent

    The SAMTestAgent is used to execute SAM tests and evaluate SAM status
    periodically. It executes tests with TestExecutor and evaluates status with
    StatusEvaluator.
  """

  def __init__(self, *args, **kwargs):
    AgentModule.__init__(self, *args, **kwargs)

    self.tests = {}
    self.apis = {}


  def initialize(self):
    """
      specify the tests which need to be executed.
    """


    self.apis[ 'DataManager' ] = DataManager()
    self.apis[ 'ResourceManagementIHEPClient' ] = ResourceManagementIHEPClient()

    return S_OK()


  def execute(self):
    """
      The main method of the agent. It get elements which need to be tested and
      evaluated from CS. Then it instantiates TestExecutor and StatusEvaluate and
      calls their main method to finish all the work.
    """

    from IHEPDIRAC.ResourceStatusSystem.SAM.SAMTest import TestConfiguration
    self.tests = TestConfiguration.TESTS
    self.__loadTestObj()

    self.testExecutor = TestExecutor( self.tests, self.apis )
    self.statusEvaluator = StatusEvaluator( self.apis )

    elements = []
    sitesCEs = {}

    # CE tests
    noTestSites = [ site.strip() for site in self.am_getOption( 'noTestSite', '' ).split( ',' ) if site != '' ]
    diracAdmin = DiracAdmin()
    activeSites = diracAdmin.getSiteMask()
#    wmsAdmin = RPCClient('WorkloadManagement/WMSAdministrator')
#    activeSites = wmsAdmin.getSiteMask()
    if not activeSites[ 'OK' ]:
      return activeSites
    activeSites = [ site for site in activeSites[ 'Value' ] if site not in noTestSites ]
    gLogger.info('Active sites: %s', activeSites)

    for siteName in activeSites:
      domain = siteName.split('.')[ 0 ]
      vos = BESUtils.getSiteVO( siteName )
      if 'CLOUD' != domain:
        siteCEs = CSHelpers.getSiteComputingElements( siteName )
        sitesCEs[ siteName ] = siteCEs
        for ce in siteCEs:
          elements.append( { 'ElementName' : ce,
                                                  'ElementType' : 'ComputingElement',
                                                  'VO' : vos } )
          gLogger.debug("List of elements: %s" % ce)

      else:
        sitesCEs[ siteName ] = [ siteName ]
        elements.append( { 'ElementName' : siteName,
                                                'ElementType' : 'CLOUD',
                                                'VO' : vos } )

    # SE tests
    ses = gConfig.getValue( 'Resources/StorageElementGroups/SE-USER' )
    for se in ses.split( ', ' ):
      seSites = BESUtils.getSitesForSE( se )
      for seSite in seSites:
        gLogger.debug( 'Site for SE %s: %s' % (se, seSite) )
        if seSite not in activeSites:
          continue
        vos = BESUtils.getSiteVO( seSite )
        gLogger.debug( 'vos for SE %s under site %s: %s' % (se, seSite, vos) )
        if len(vos) == 0:
          continue
        vo = vos[0]
        elements.append( { 'ElementName' : se,
                                              'ElementType' : 'StorageElement',
                                              'VO' : vo } )
        gLogger.info( 'VO for SE %s: %s' % ( se, vo ) )
        break

    lastCheckTime = datetime.utcnow().replace(microsecond = 0)
    self.elementsStatus = {}

    threads = []
    for elementDict in elements:
      gLogger.info( 'Start SAM test for %s with VO %s' % ( elementDict['ElementName'], elementDict.get('VO', []) ) )
      t = threading.Thread( target = self._execute, args = ( elementDict, ) )
      threads.append( t )
      t.start()

    for thread in threads:
      thread.join()

    for siteName in activeSites:
      seList = CSHelpers.getSiteStorageElements( siteName )
      se = ''
      if [] != seList:
        se = seList[ 0 ]
      try:
        seStatus = self.elementsStatus[ se ][ 'all' ]
      except KeyError:
        seStatus = None

      voStatus = { 'all' : [] }
      for ce in sitesCEs[ siteName ]:
        if ce not in self.elementsStatus:
          continue
        for vo, status in self.elementsStatus[ ce ].items():
          if vo not in voStatus:
            voStatus[ vo ] = []
          voStatus[ vo ].append( status )

      for vo, ceStatusList in voStatus.items():
        if ceStatusList == [] and seStatus == None:
          continue
        res = self.statusEvaluator.evaluateSiteStatus( siteName, ceStatusList, seStatus, vo = vo, lastCheckTime = lastCheckTime)
        if not res[ 'OK' ]:
          gLogger.error( 'StatusEvaluator.evaluateSiteStatus: %s' % res[ 'Message' ] )
          break

    return S_OK()


  def _execute( self, elementDict ):
    elementName = elementDict[ 'ElementName' ]
    vos = elementDict.get( 'VO', [] )
    utcNow = datetime.utcnow().replace( microsecond = 0 )

    # Return status of each Testtype
    testRes = self.testExecutor.execute( elementDict, lastCheckTime = utcNow )
    if not testRes[ 'OK' ]:
      gLogger.error( 'TestExecutor.execute error for %s: %s' % ( elementName, testRes[ 'Message' ] ) )
      return
    testsStatus = testRes[ 'Value' ]
    gLogger.info( 'The status of %s is %s' % ( elementName, testsStatus ) )

    defaultTestsStatus = {}
    voTestsStatus = {}
    for vo in vos:
      voTestsStatus[ vo ] = {}
    for testType, status in testsStatus.items():
      vo = self.tests[ testType ][ 'match' ].get( 'VO' )
      if not vo:
        defaultTestsStatus[ testType ] = status
      else:
        voTestsStatus[ vo ][ testType ] = status

    elementStatus = {}
    self.elementsStatus[ elementName ] = elementStatus

    res = self.statusEvaluator.evaluateResourceStatus( elementDict, testsStatus, lastCheckTime = utcNow )
    if not res[ 'OK' ]:
      gLogger.error( 'StatusEvaluator.evaluateResourceStatus: %s' % res[ 'Message' ] )
      return
    elementStatus[ 'all' ] = res[ 'Value' ]

    for vo, statuses in voTestsStatus.items():
      statuses.update( defaultTestsStatus )
      res = self.statusEvaluator.evaluateResourceStatus( elementDict, statuses, vo = vo, lastCheckTime = utcNow )
      if not res[ 'OK' ]:
        gLogger.error( 'StatusEvaluator.evaluateResourceStatus: %s' % res[ 'Message' ] )
        return
      elementStatus[ vo ] = res[ 'Value' ]


  def __loadTestObj(self):
    _module_pre = 'IHEPDIRAC.ResourceStatusSystem.SAM.SAMTest.'

    for testType, testDict in self.tests.items():
      moduleName = testDict[ 'module' ]
      args = testDict.get( 'args', {} )
      args.update( testDict[ 'match' ] )
      args[ 'TestType' ] = testType
      try:
        testModule = Utils.voimport( _module_pre + moduleName )
      except ImportError as e:
        gLogger.error( "Unable to import %s, %s" % ( _module_pre + moduleName, e ) )
        continue
      testClass = getattr( testModule, moduleName )
      obj = testClass(args, self.apis)
      testDict[ 'object' ] = obj
