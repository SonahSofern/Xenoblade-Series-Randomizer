import json, random
from Enhancements import *


def RandomizeAccessoryEnhancements():
    InvalidSkillEnhancements = [EyeOfJustice, BladeSwitchDamageUp, ArtCancel, XStartBattle, YStartBattle, BStartBattle, EvadeDriverArt, EvadeDrainHp,ArtDamageHeal, BladeSwapDamage, DreamOfTheFuture, FlatAgiBoost,FlatDefBoost,FlatDexBoost, FlatEtherBoost, FlatHPBoost, FlatStrengthBoost, FlatLuckBoost]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    
    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as EnhanceFile:
        with open("./_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as NamesFile:
            
            
            
            enhanceFile = json.load(EnhanceFile)
            NameFile = json.load(NamesFile)
            for Acc in enhanceFile["rows"]:
                enhancement = random.choice(ValidSkills)
                enhancement.RollEnhancement()
                for skillName in NameFile["rows"]:  
                    if skillName["$id"] == Acc["Name"]:    
                        oldName = skillName["name"]
                        oldNameList = oldName.split()
                        lastWord = oldNameList[-1]
                        skillName["name"] = f"{enhancement.name} {lastWord}" # Solution to naming problem make 
                        break
                Acc["Enhance1"] = enhancement.id
                Acc["Price"] = (enhancement.Rarity+1) * 5000
                Acc["Rarity"] = enhancement.Rarity
                
                
                
            NamesFile.seek(0)
            NamesFile.truncate()
            json.dump(NameFile, NamesFile, indent=2, ensure_ascii=False)
        EnhanceFile.seek(0)
        EnhanceFile.truncate()
        json.dump(enhanceFile, EnhanceFile, indent=2, ensure_ascii=False)

    
        

