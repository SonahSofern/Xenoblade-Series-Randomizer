from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, StatRand

def SkillStats(intensity):
    artFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    statRando = StatRand.Stat(1.5, intensity)
    
    # for art in artFile.rows:
    #     for i in range(0,5):
    #         for stat in [f"DmgMgn[{i}]", f"RecastFrm[{i}]"]:
    #             statRando.ApplyMult(art, stat, StatRand.b16)
    
    artFile.Close()