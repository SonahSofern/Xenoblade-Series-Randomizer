import json, random
from Enhancements import *


def RandomizeSkillEnhancements():
    ArtsCancelSlots = [12,55,82,102,131,161]
    ZekeEye = [152]
    X_Slots= [1,56,83,103,132,162]
    Y_Slots= [11,57,84,104,133,163]
    B_Slots= [21,58,85,105,134,164] 
    InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle]
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
                skillNameFile["rows"][i]["name"] = skill.name
                enhanceFile["rows"][i]["Enhance"] = skill.id
            nameFile.seek(0)
            nameFile.truncate()
            json.dump(skillNameFile, nameFile, indent=2, ensure_ascii=False)
        enhancementFile.seek(0)
        enhancementFile.truncate()
        json.dump(enhanceFile, enhancementFile, indent=2, ensure_ascii=False)
    # ShuffleSkills()

# def ShuffleSkills():
#     NumDrivers = 6
#     for i in range(NumDrivers):
#         S1 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#         S2 = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#         random.shuffle(S1)
#         random.shuffle(S2)
#         with open(f"./_internal/JsonOutputs/common/BTL_Skill_Dr_Table0{i+1}.json", 'r+', encoding='utf-8') as driverSkillFile:
#             skill = json.load(driverSkillFile)
#             for j in range(2,16):
#                 skill["rows"][j-1]["$id"] = S1[j-2]
#             for k in range(16,31):
#                 skill["rows"][k-16]["$id"] = S2[k-17]
#             driverSkillFile.seek(0)
#             driverSkillFile.truncate()
#             json.dump(skill, driverSkillFile, indent=2, ensure_ascii=False)