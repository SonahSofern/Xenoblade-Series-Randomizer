import json, random
from Enhancements import *
from scripts import PopupDescriptions
import Options

InvalidSkillEnhancements = [PhyAndEthDefenseUp,ForcedHPPotionOnHit,BlockBoost,FlatBlockBoost,CritBoost, FlatCritBoost, PartyCritMaxAffinity, DamageAndCritUpMaxAffinity,HpPotChanceFor2,EyeOfJustice, BladeSwitchDamageUp, ArtCancel, XStartBattle, YStartBattle, BStartBattle, EvadeDriverArt, EvadeDrainHp,ArtDamageHeal, BladeSwapDamage, FlatAgiBoost,FlatDefBoost,FlatDexBoost, FlatEtherBoost, FlatHPBoost, FlatStrengthBoost, FlatLuckBoost, BladeComboOrbAdder]
ValidSkills:list[Enhancement] = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]

def RandomizeAccessoryEnhancements():



    with open("./XC2/_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as EnhanceFile:
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as NamesFile: # overflows past a certain num so cant make new names
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
        
def AccessoriesDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.DriverAccessoriesOption.name)
    desc.Text("This option randomizes all accessory effects, even to effects that could not be obtained in normal gameplay.")
    desc.Image("accessoryeffects.png", "XC2", 700)
    desc.Text("This also replaces the first word of accessories to fit their new effect.")
    effectDescription:str
    ValidSkills.sort(key=lambda x: x.name) # Alphabetic Sort
    for effect in ValidSkills:
        if effect.Description == "":
            try:
                with open("./XC2/_internal/JsonOutputs/common_ms/btl_enhance_cap.json", 'r+', encoding='utf-8') as descFile:
                    descData = json.load(descFile)
                    for des in descData["rows"]:
                        if des["$id"] == effect.Caption:   
                            effectDescription = des["name"]  
                            break
            except:
                effectDescription = "No files to load descriptions from."
        else:
            effectDescription = effect.Description # keep descriptions that I create for the class
            
        # Replace things we dont want user to see
        effectDescription = effectDescription.replace('\n', " ") # Remove new lines
        effectDescription = effectDescription.replace("[ML:Enhance kind=Param1 ]", f"{effect.Param1[0]}-{effect.Param1[-1]}")
        effectDescription = effectDescription.replace("[ML:Enhance kind=Param1]", f"{effect.Param1[0]}-{effect.Param1[-1]}")
        effectDescription = effectDescription.replace("[ML:Enhance kind=Param2 ]", f"{effect.Param2[0]}-{effect.Param2[-1]}")
        effectDescription = effectDescription.replace("[ML:Enhance kind=Param2]", f"{effect.Param2[0]}-{effect.Param2[-1]}")
        effectDescription = effectDescription.replace("[ML:Enhance ]", f"{effect.max[0]}-{effect.max[-1]}")
        effectDescription = effectDescription.replace("[max: [ML:Enhance kind=Param2", f"max: {effect.Param2[0]}-{effect.Param2[-1]}")

        
        desc.Tag(effect.name, padx=0)
        desc.Text(effectDescription)
    return desc