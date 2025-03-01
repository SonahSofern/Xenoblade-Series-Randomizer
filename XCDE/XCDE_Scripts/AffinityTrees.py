# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_PSVskill.html
import json, random, time


yoinkSkills = [140,138]
MeliaSkills = [152,157,159]
MechonisArmor = [176]
SharlaCoolOff = [110]
ReynTaunts = [32,35,46]
ArmorEquips = [] # So we cant put people with no models with certain types but we can have some fun by limiting. If reyn doesnt roll heavy armor no heavy armor for him

SkillList= []

class Skill:
    def __init__(self, _name, _shape, _target, _skill, _val1, _val2, _time, _point_PP, _point_SP, _flag):
        self.name = _name
        self.shape = _shape
        self.target = _target
        self.skill = _skill
        self.val1 = _val1
        self.val2 = _val2
        self.time = _time
        self.point_PP = _point_PP
        self.point_SP = _point_SP
        self.flag = _flag
        SkillList.append(self)
        
        
def SkillRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_PSVskill.json", 'r+', encoding='utf-8') as skillFile:
        skillData = json.load(skillFile)
        for skill in skillData["rows"]:
            Skill(skill["name"], skill["shape"], skill["target"], skill["skill"], skill["val1"], skill["val2"], skill["time"], skill["point_PP"], skill["point_SP"], skill["flag"])
        
        for skill in skillData["rows"]:
            if skill["$id"] in invalidSkills:
                continue
            chosen:Skill = random.choice(SkillList)
            SkillList.remove(chosen)
            skill["name"] = chosen.name
            skill["shape"] = chosen.shape
            skill["target"] = chosen.target
            skill["skill"] = chosen.skill
            skill["val1"] = chosen.val1
            skill["val2"] = chosen.val2
            skill["time"] = chosen.time
            skill["point_PP"] = chosen.point_PP
            skill["point_SP"] = chosen.point_SP
            skill["flag"] = chosen.flag
            
                        
        # skill["shape"] = random.randrange(1,6)

        skillFile.seek(0)
        skillFile.truncate()
        json.dump(skillData, skillFile, indent=2, ensure_ascii=False)
    
def SkillLinkNodeRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv.json", 'r+', encoding='utf-8') as linkFile: # Randomizes the node shape for skill link trees
        linkData = json.load(linkFile)
        for link in linkData["rows"]:
            for i in range(1,6):
                link[f"rvs_effect0{i}"] = random.randrange(1,5)

        linkFile.seek(0)
        linkFile.truncate()
        json.dump(linkData, linkFile, indent=2, ensure_ascii=False)