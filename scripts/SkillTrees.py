import json, random
from Enhancements import *


def RandomizeSkillEnhancements():
    ArtsCancelSlots = [12,55,82,102,131,161]
    ZekeEye = 152
    X_Slots= [13,56,83,103,132,162]
    Y_Slots= [14,57,84,104,133,163]
    B_Slots= [15,58,85,105,134,164] # Randomize After
    InvalidSkillEnhancements = [ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    ForcedSkills = []
    with open("./_internal/JsonOutputs/common/BTL_Skill_Dr.json", 'r+', encoding='utf-8') as file:
        with open("./_internal/JsonOutputs/common_ms/btl_skill_dr_name.json", 'r+', encoding='utf-8') as skillNames:
            enhanceFile = json.load(file)
            skillNameFile = json.load(skillNames)
            for i in range(len(enhanceFile['rows'])):
                if ForcedSkills != []:
                    skill = random.choice(ForcedSkills)
                elif i+1 in ArtsCancelSlots:
                    skill = ArtCancel
                elif i+1 == ZekeEye:
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
            skillNames.seek(0)
            skillNames.truncate()
            json.dump(skillNameFile, skillNames, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(enhanceFile, file, indent=2, ensure_ascii=False)


def ShuffleSkills():
    # Shuffle each file besides arts cancel so you dont get the same tree
    pass