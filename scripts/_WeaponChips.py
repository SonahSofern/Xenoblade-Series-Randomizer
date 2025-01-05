import json, random
from Enhancements import *



def RandomizeWeaponEnhancements():
    InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, BladeSwapDamage, EvadeDrainHp, EvadeDriverArt, EtherCannonRange,ArtDamageHeal]
    
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    InvalidNames = ["Monado", "Well-Used Blades", "Archetype Ralzes", "Halteclere", "Masamune"]
    with open("./_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file:
        with open("./_internal/JsonOutputs/common_ms/itm_pcwpn_ms.json", 'r+', encoding='utf-8') as wepNames:
            
            
            enhanceFile = json.load(file)
            skillNameFile = json.load(wepNames)
            for Wep in enhanceFile["rows"]:
                if Wep["Enhance1"] != 0: # Only replaces already enhanced weps
                    skillNameID = Wep["Name"]
                    enhancement = random.choice(ValidSkills)
                    while enhancement.Caption > 255: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                        enhancement = random.choice(ValidSkills)
                    # ValidSkills.remove(enhancement) # Need full pool
                    for skillName in skillNameFile["rows"]:  
                        if skillName["$id"] == skillNameID:
                            if skillName["name"] not in InvalidNames:      
                                oldName = skillName["name"]
                                oldName = skillName["name"]
                                oldNameList = oldName.split()
                                lastWord = oldNameList[-1]
                                skillName["name"] = f"{enhancement.name} {lastWord}"
                            break
                    Wep["Enhance1"] = enhancement.id
                
                
            wepNames.seek(0)
            wepNames.truncate()
            json.dump(skillNameFile, wepNames, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(enhanceFile, file, indent=2, ensure_ascii=False)
