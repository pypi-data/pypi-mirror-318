#! /usr/bin/env python
"""
Register SE files under specified directory to DFC. Files must be locally readable

Usage:
  ihepdirac_dms_register_dir [option|cfgfile] DFCDir LocalDir SE

Example:
  ihepdirac_dms_register_dir /juno/user/z/zhangxm/9743 /junofs/grid/user/z/zhangxm/9743 IHEP-JUNOEOS

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__RCSID__ = "$Id$"

import os
import sys

from DIRAC.Core.Base.Script import Script
from DIRAC import S_OK, S_ERROR, gLogger, exit

@Script()
def main():

    Script.registerSwitch( 'e', 'existCheck', 'Check if file exists')
    Script.registerSwitch( 'q:', 'querySkip=', 'Skip files in the meta query')
    Script.registerSwitch( 'b:', 'bufferSize=', 'Register buffer size, default to 100')
    Script.parseCommandLine(ignoreErrors = False)

    from DIRAC.Core.Utilities.Adler import fileAdler
    from DIRAC.Core.Utilities.File import makeGuid
    from DIRAC.DataManagementSystem.Client.DataManager import DataManager

    from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
    fcc = FileCatalogClient('DataManagement/FileCatalog')

    args = Script.getPositionalArgs()

    if len(args) != 3:
        Script.showHelp()
        exit(1)

    dfcDir = args[0]
    if (not args[1]) or args[1].endswith(os.sep):
        localDir = args[1]
    else:
        localDir = args[1] + os.sep
    toSE = args[2]

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

    dm = DataManager()
    fileTupleBuffer = []
    for root, dirs, files in os.walk(localDir):
        for f in files:
            counter += 1

            fullFn = os.path.join(root, f)
            if not fullFn.startswith(localDir):
                gLogger.error('%s does not start with %s' % (fullFn, localDir))
                continue
            lastPart = fullFn[len(localDir):]
            lfn = os.path.join(dfcDir, lastPart)

            if lfn in lfnQuery:
                if counter%1000 == 0:
                    gLogger.notice('Skip file in query counter: %s' % counter)
                continue

            if existCheck:
                result = fcc.isFile(lfn)
                if result['OK'] and lfn in result['Value']['Successful'] and result['Value']['Successful'][lfn]:
                    if counter%1000 == 0:
                        gLogger.notice('Skip file existed counter: %s' % counter)
                    continue

            size = os.path.getsize( fullFn )
            adler32 = fileAdler( fullFn )
            guid = makeGuid()
            fileTuple = ( lfn, fullFn, size, toSE, guid, adler32 )
            fileTupleBuffer.append(fileTuple)
            gLogger.debug('Register to lfn: %s' % lfn)
            gLogger.debug('fileTuple: %s' % (fileTuple,))

            if len(fileTupleBuffer) >= bufferSize:
                result = dm.registerFile( fileTupleBuffer )
                if not result['OK']:
                    gLogger.error('Can not register %s' % fullFn)
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
