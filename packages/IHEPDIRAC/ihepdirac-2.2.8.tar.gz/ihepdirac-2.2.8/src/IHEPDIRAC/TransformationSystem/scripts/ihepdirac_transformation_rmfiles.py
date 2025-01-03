#!/bin/env python
"""
Create a production to remove files from all storage elements
"""
from DIRAC.Core.Base.Script import Script
import argparse


@Script()
def main():
    """reads command line parameters, makes check and creates transformation"""
    from DIRAC import gLogger, exit as dexit
    from IHEPDIRAC.TransformationSystem.Utilities.CLIParameters import Params

    clip = Params()
    Script.registerSwitch("G:", "GroupSize=", "Number of Files per transformation task",clip.setGroupSize)
    Script.registerSwitch("R:", "GroupName=", "TransformationGroup Name",clip.setGroupName)
    Script.registerSwitch("N:", "Extraname=", "String to append to transformation name",clip.setExtraname)
    Script.registerSwitch("P:", "Plugin=", "Plugin to use for transformation",clip.setPlugin)
    Script.registerSwitch("x", "Enable", "Enable the transformation creation, otherwise dry-run",clip.setEnable)
    Script.registerSwitch("H","Help","Create one remove files transformation for each MetaValue given.\n\n More on this: Is running in dry-run mode, unless enabled with -x. MetaValue can be comma separated lists.\n \n Usage: ihepdirac_transformation_rmfiles <MetaKey>=<MetaValue> [-G<Files>] [-N<ExtraName>] -x")

    Script.parseCommandLine(ignoreErrors = False)
    args = Script.getPositionalArgs()

    if (args[0] == "help"):
        Script.showHelp()
        exit(1)

    from IHEPDIRAC.TransformationSystem.Utilities.OperationTransformation import createDataTransformation

    if not clip.checkRemoveFileSettings(Script)["OK"]:
        gLogger.error("ERROR: Missing settings")
        dexit(1)

    
    for metaValue in clip.metaValues:
        resCreate = createDataTransformation(
            flavour="RmFile",
            transType="Removal-JUNO",
            targetSE=clip.targetSE,
            sourceSE=clip.sourceSE,
            metaKey=clip.metaKey,
            metaValue=metaValue,
            extraData=clip.extraData,
            extraname=clip.extraname,
            groupSize=clip.groupSize,
            tGroup=clip.groupName,
            plugin=clip.plugin,
            enable=clip.enable,
        )
        if not resCreate["OK"]:
            gLogger.error("Failed to create Transformation", resCreate["Message"])
            dexit(1)

    dexit(0)


if __name__ == "__main__":
    main()
