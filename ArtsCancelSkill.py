import JSONParser
from IDs import *

def ArtsCancelBehavior():
    JSONParser.ChangeJSON("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], Helper.inclRange(0,50000),  [0], InvalidTargetIDs=Helper.inclRange(2,30))
    JSONParser.ChangeJSON("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["NeedSp"], DriverSkillTrees,  [14], InvalidTargetIDs=Helper.inclRange(2,30))