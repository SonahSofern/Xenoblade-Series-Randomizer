import json, random
from Enhancements import *


def RandomizeSkillEnhancements():
    ArtsCancelSlots = [12,55,82,102,131,161]
    ZekeEye = [152]
    X_Slots= [1,51,61,91,121,162]
    Y_Slots= [11,31,71,101,141,171]
    B_Slots= [21,52,62,92,122,151] 
    InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, AegisPowerUp, BigBangPowerUp, CatScimPowerUp, VarSaberPowerUp, MechArmsPowerUp, WhipswordPowerUp, DrillShieldPowerUp, DualScythesPowerUp, EvadeDrainHp, EvadeDriverArt, KnuckleClawsPowerUp, BitballPowerUp, GreataxePowerUp, TwinRingPowerUp, MegalancePowerUp,ShieldHammerPowerUp, ChromaKatanaPowerUp, EtherCannonPowerUp, ArtDamageHeal]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    ForcedSkills = []
    with open("./_internal/JsonOutputs/common/BTL_Skill_Dr.json", 'r+', encoding='utf-8') as enhancementFile:
        with open("./_internal/JsonOutputs/common_ms/btl_skill_dr_name.json", 'r+', encoding='utf-8') as nameFile:
            enhanceFile = json.load(enhancementFile)
            skillNameFile = json.load(nameFile)
            for i in range(len(enhanceFile['rows'])):
                if ForcedSkills != []:
                    skill = random.choice(ForcedSkills)
                elif i+1 in ArtsCancelSlots:
                    skill = ArtCancel
                elif i+1 in ZekeEye:
                    skill = EyeOfJustice
                elif i+1 in X_Slots:
                    skill = XStartBattle
                elif i+1 in Y_Slots:
                    skill = YStartBattle
                elif i+1 in B_Slots:
                    skill = BStartBattle
                else:
                    skill = random.choice(ValidSkills)
                    ValidSkills.remove(skill)
                skill.RollEnhancement()
                skillNameFile["rows"][i]["name"] = skill.name
                enhanceFile["rows"][i]["Enhance"] = skill.id
            ArtsCancelCost()
            nameFile.seek(0)
            nameFile.truncate()
            json.dump(skillNameFile, nameFile, indent=2, ensure_ascii=False)
        enhancementFile.seek(0)
        enhancementFile.truncate()
        json.dump(enhanceFile, enhancementFile, indent=2, ensure_ascii=False)
        
def ArtsCancelCost():
    for i in range(1,7):
        with open(f"./_internal/JsonOutputs/common/BTL_Skill_Dr_Table0{i}.json", 'r+', encoding='utf-8') as driverFiles:
            dFile = json.load(driverFiles)
            for item in dFile["rows"]:
                if item["SkillID"] == ArtCancel.id:
                    item["NeedSp"] = 0
            driverFiles.seek(0)
            driverFiles.truncate()
            json.dump(dFile, driverFiles, indent=2, ensure_ascii=False)