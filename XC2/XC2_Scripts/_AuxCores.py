import json, random
from XC2.XC2_Scripts.Enhancements import *


def RandomizeAuxCoreEnhancements():
    InvalidSkillEnhancements = [ForcedHPPotionOnHit,ArtCancel,HpPotChanceFor2, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, EvadeDrainHp, EvadeDriverArt,ArtDamageHeal, BladeSwitchDamageUp]

    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]

    with open("./XC2/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as AuxCoreFile:
        with open("./XC2/JsonOutputs/common_ms/itm_orb.json", 'r+', encoding='utf-8') as auxNamesFile:
            with open("./XC2/JsonOutputs/common/ITM_HanaAssist.json", 'r+', encoding='utf-8') as poppiAuxEnhancementsFile:
                poppiAuxData = json.load(poppiAuxEnhancementsFile)
                enhanceData = json.load(AuxCoreFile)
                auxNameData = json.load(auxNamesFile)
                

                
                for aux in poppiAuxData["rows"]: # Must do poppis first because of overlap name ids then I update them later down below
                    enhancement:Enhancement = random.choice(ValidSkills)
                    enhancement.RollEnhancement()
                    skillNameID = aux["Name"]
                    aux["Enhance"] = enhancement.id
                    cat = enhancement.EnhanceEffect
                    if cat > 255: # not great temp solution cant set category above 255 but you cant equip things of the same category at once
                        cat -= random.randrange(14,256)
                    aux["EnhanceCategory"] = cat
                    for skillName in auxNameData["rows"]:  
                        if skillName["$id"] == skillNameID:    
                            skillName["name"] = f"{enhancement.name} Core"
                            break
                    
                
                for Aux in enhanceData["rows"]:
                    skillNameID = Aux["Name"]
                    enhancement:Enhancement = random.choice(ValidSkills)
                    enhancement.RollEnhancement()
                    # ValidSkills.remove(enhancement) # Need full pool to remove 


                
                    for skillName in auxNameData["rows"]:  
                        if skillName["$id"] == skillNameID:    
                            skillName["name"] = f"{enhancement.name} Core"
                            break
                        
                    for poppiAux in poppiAuxData["rows"]: # Since poppi uses the same names and I cant add more, poppis must match the effects of the rolled name
                        if poppiAux["Name"] == skillNameID:
                            poppiAux["Enhance"] = enhancement.id
                            break
                                            
                    Aux["Enhance"] = enhancement.id
                    Aux["Rarity"] = enhancement.Rarity
                    cat = enhancement.EnhanceEffect
                    if cat > 255: # not great temp solution cant set category above 255 but you cant equip things of the same category at once
                        cat -= random.randrange(14,256)
                    aux["EnhanceCategory"] = cat

                    
                poppiAuxEnhancementsFile.seek(0)
                poppiAuxEnhancementsFile.truncate()
                json.dump(poppiAuxData, poppiAuxEnhancementsFile, indent=2, ensure_ascii=False)
            auxNamesFile.seek(0)
            auxNamesFile.truncate()
            json.dump(auxNameData, auxNamesFile, indent=2, ensure_ascii=False)
        AuxCoreFile.seek(0)
        AuxCoreFile.truncate()
        json.dump(enhanceData, AuxCoreFile, indent=2, ensure_ascii=False)
