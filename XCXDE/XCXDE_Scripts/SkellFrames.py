from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, Helper, StatRand, PopupDescriptions

def SkellMovement():
    '''Randomizes skell stats involved with movement'''
    skellFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlActParam.json")
    for skell in skellFile.rows:
        skell["VF_CarDashMaxVelocity"] = 200
        skell["VF_CarDashMinVelocity"] = 50

    skellFile.Close()