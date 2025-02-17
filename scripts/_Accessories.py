import json, random
from Enhancements import *


def RandomizeAccessoryEnhancements():
    InvalidSkillEnhancements = [PhyAndEthDefenseUp,ForcedHPPotionOnHit,BlockBoost,FlatBlockBoost,CritBoost, FlatCritBoost, PartyCritMaxAffinity, DamageAndCritUpMaxAffinity,HpPotChanceFor2,EyeOfJustice, BladeSwitchDamageUp, ArtCancel, XStartBattle, YStartBattle, BStartBattle, EvadeDriverArt, EvadeDrainHp,ArtDamageHeal, BladeSwapDamage, FlatAgiBoost,FlatDefBoost,FlatDexBoost, FlatEtherBoost, FlatHPBoost, FlatStrengthBoost, FlatLuckBoost, BladeComboOrbAdder]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]


    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as EnhanceFile:
        with open("./_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as NamesFile: # overflows past a certain num so cant make new names
            enhanceFile = json.load(EnhanceFile)
            NameFile = json.load(NamesFile)
            prevNames = []
            
            for Acc in enhanceFile["rows"]:
                
                enhancement:Enhancement = random.choice(ValidSkills)
                prevNames.append({"myName" :Acc["Name"], "myEnhance": enhancement})
                
                for pair in prevNames: # Ensures the same name has the same enhancement
                    if pair["myName"] == Acc["Name"]:
                        enhancement = pair["myEnhance"]
                        break
                
                enhancement.RollEnhancement()
                
                Acc["Enhance1"] = enhancement.id
                Acc["Price"] = (enhancement.Rarity+1) * 5000
                Acc["Rarity"] = enhancement.Rarity      
                
                for skillName in NameFile["rows"]:  # Changes names
                    if skillName["$id"] == Acc["Name"]:  
                        oldName = skillName["name"]
                        oldNameList = oldName.split()
                        lastWord = oldNameList[-1]
                        skillName["name"] = f"{enhancement.name} {lastWord}"  
                        break

                
            NamesFile.seek(0)
            NamesFile.truncate()
            json.dump(NameFile, NamesFile, indent=2, ensure_ascii=False)
        EnhanceFile.seek(0)
        EnhanceFile.truncate()
        json.dump(enhanceFile, EnhanceFile, indent=2, ensure_ascii=False)