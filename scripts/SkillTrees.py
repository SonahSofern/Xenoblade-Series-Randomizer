import json, random
from Enhancements import *


def RandomizeSkillEnhancements():
    ArtsCancelSlots = [12,55,82,102,131,161]
    ZekeEye = [152]
    X_Slots= [1,51,61,91,121,162]
    Y_Slots= [11,31,71,101,141,171]
    B_Slots= [21,52,62,92,122,151] 
    InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, AegisPowerUp, BigBangPowerUp, CatScimPowerUp, VarSaberPowerUp, MechArmsPowerUp, WhipswordPowerUp, DrillShieldPowerUp, DualScythesPowerUp, EvadeDrainHp, EvadeDriverArt, KnuckleClawsPowerUp, BitballPowerUp, GreataxePowerUp, TwinRingPowerUp, MegalancePowerUp,ShieldHammerPowerUp, ChromaKatanaPowerUp, EtherCannonPowerUp, ArtDamageHeal, AegisParty, AegisDriver]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    ForcedSkills = []
    with open("./_internal/JsonOutputs/common/BTL_Skill_Dr.json", 'r+', encoding='utf-8') as enhancementFile:
        with open("./_internal/JsonOutputs/common_ms/btl_skill_dr_name.json", 'r+', encoding='utf-8') as nameFile:
            enhanceFile = json.load(enhancementFile)
            skillNameFile = json.load(nameFile)
            for skillSlot in enhanceFile['rows']:
                if ForcedSkills != []:
                    skill = random.choice(ForcedSkills)
                elif skillSlot["$id"] in ArtsCancelSlots:
                    skill = ArtCancel
                elif skillSlot["$id"] in ZekeEye:
                    skill = EyeOfJustice
                elif skillSlot["$id"] in X_Slots:
                    skill = XStartBattle
                elif skillSlot["$id"] in Y_Slots:
                    skill = YStartBattle
                elif skillSlot["$id"] in B_Slots:
                    skill = BStartBattle
                else:
                    skill = random.choice(ValidSkills)
                    # ValidSkills.remove(skill)
                skill.RollEnhancement()
                skillNameFile["rows"][skillSlot["$id"]-1]["name"] = skill.name
                enhanceFile["rows"][skillSlot["$id"]-1]["Enhance"] = skill.id
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
                if item["Round"] == 1 and item["ColumnNum"] == 1 and item["RowNum"] == 1: 
                    item["NeedSp"] = 0
            driverFiles.seek(0)
            driverFiles.truncate()
            json.dump(dFile, driverFiles, indent=2, ensure_ascii=False)