import json, random, Helper
from Enhancements import *

InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle]

def RandomizeSkillEnhancements():
    
    ArtsCancelSlots = [12,55,82,102,131,161]
    RangeOfSkills = Helper.InclRange(0,270)
    ZekeEye = random.randrange(151,181)
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    
    RunCustomEnhancements()
    with open("./_internal/JsonOutputs/common/BTL_Skill_Dr.json", 'r+', encoding='utf-8') as file:
        with open("./_internal/JsonOutputs/common_ms/btl_skill_dr_name.json", 'r+', encoding='utf-8') as skillNames:
            enhanceFile = json.load(file)
            skillNameFile = json.load(skillNames)
            skill = Enhancement
            for i in range(len(enhanceFile['rows'])):
                if i+1 in ArtsCancelSlots:
                    skill = ArtCancel
                elif i+1 == ZekeEye:
                    skill = EyeOfJustice
                elif i+1 in XStart:
                    skill = XStartBattle
                elif i+1 in YStart:
                    skill = YStartBattle
                elif i+1 in BStart:
                    skill = BStart
                else:
                    skill = random.choice(ValidSkills)
                    ValidSkills.remove(skill) # No dupes but i need a full pool
                skillNameFile["rows"][i]["name"] = skill.name
                enhanceFile["rows"][i]["Enhance"] = skill.id
            skillNames.seek(0)
            skillNames.truncate()
            json.dump(skillNameFile, skillNames, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(enhanceFile, file, indent=2, ensure_ascii=False)
