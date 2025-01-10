import json, random
from Enhancements import *


def RandomizeAccessoryEnhancements():
    InvalidSkillEnhancements = [ForcedHPPotionOnHit,EyeOfJustice, BladeSwitchDamageUp, ArtCancel, XStartBattle, YStartBattle, BStartBattle, EvadeDriverArt, EvadeDrainHp,ArtDamageHeal, BladeSwapDamage, DreamOfTheFuture, FlatAgiBoost,FlatDefBoost,FlatDexBoost, FlatEtherBoost, FlatHPBoost, FlatStrengthBoost, FlatLuckBoost, BladeComboOrbAdder]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    
    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as EnhanceFile:
        with open("./_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as NamesFile: # overflows past a certain num so cant make new names
            enhanceFile = json.load(EnhanceFile)
            NameFile = json.load(NamesFile)
            
            
            for Acc in enhanceFile["rows"]:
                enhancement = random.choice(ValidSkills)
                enhancement.RollEnhancement()
                Acc["Enhance1"] = enhancement.id
                Acc["Price"] = (enhancement.Rarity+1) * 5000
                Acc["Rarity"] = enhancement.Rarity      
                
                for skillName in NameFile["rows"]:  # Find old name and make a copy
                    if skillName["$id"] == Acc["Name"]:  
                        nameid = enhancement.id - 3652 
                        oldName = skillName["name"]
                        oldNameList = oldName.split()
                        lastWord = oldNameList[-1]
                        newName = f"{enhancement.name} {lastWord}"
                        
                        customName = {
                        "$id": nameid,
                        "style": 36,
                        "name": newName
                        }
                        Acc["Name"] = nameid + 1
                        NameFile["rows"].append(customName)
                        
                        break

                
            NamesFile.seek(0)
            NamesFile.truncate()
            json.dump(NameFile, NamesFile, indent=2, ensure_ascii=False)
        EnhanceFile.seek(0)
        EnhanceFile.truncate()
        json.dump(enhanceFile, EnhanceFile, indent=2, ensure_ascii=False)

    
        

