import json, random
from Enhancements import *



def RandomizeWeaponEnhancements():
    InvalidSkillEnhancements = [EyeOfJustice]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    
    with open("./_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file:
        with open("./_internal/JsonOutputs/common_ms/itm_pcwpn_ms.json", 'r+', encoding='utf-8') as wepNames:
            enhanceFile = json.load(file)
            skillNameFile = json.load(wepNames)
            for Wep in enhanceFile["rows"]:
                skillNameID = Wep["Name"]
                enhancement = random.choice(ValidSkills)
                # ValidSkills.remove(skill) # Need full pool
                for skillName in skillNameFile["rows"]:  
                    if skillName["$id"] == skillNameID:    
                        oldName = skillName["name"]
                        skillName["name"] = f"{enhancement.name} {oldName}"
                Wep["Enhance1"] = enhancement.id
            wepNames.seek(0)
            wepNames.truncate()
            json.dump(skillNameFile, wepNames, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(enhanceFile, file, indent=2, ensure_ascii=False)
