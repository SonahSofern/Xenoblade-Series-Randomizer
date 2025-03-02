# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_PSVskill.html
import json, random, time
import Options

yoinkSkills = [140,138]
MeliaSkills = [152,157,159]
MechonisArmor = [176]
SharlaCoolOff = [110]
ReynTaunts = [32,35,46]
ArmorEquips = [] # So we cant put people with no models with certain types but we can have some fun by limiting. If reyn doesnt roll heavy armor no heavy armor for him



class Skill:
    newId = 0
    def __init__(self, _name, _shape, _target, _skill, _val1, _val2, _time, _point_PP, _point_SP, _flag, _id):
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
        self.id = _id
        
def SkillRando():
    isShape = Options.AffinityTreeOption_Shape.GetState()
    isPower = Options.AffinityTreeOption_Power.GetState()
    isLinkCost = Options.AffinityTreeOption_LinkCost.GetState()
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_PSVskill.json", 'r+', encoding='utf-8') as skillFile:
        with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv/MNU_PSskil.json", 'r+', encoding='utf-8') as skillDescFile:
            skillData = json.load(skillFile)
            descData = json.load(skillDescFile)
            
            SkillList:list[Skill]= []
            invalidSkills = yoinkSkills + MeliaSkills + MechonisArmor + SharlaCoolOff + ReynTaunts
            for skill in skillData["rows"]:
                if skill["$id"] in invalidSkills:
                    continue
                newSkill = Skill(skill["name"], skill["shape"], skill["target"], skill["skill"], skill["val1"], skill["val2"], skill["time"], skill["point_PP"], skill["point_SP"], skill["flag"], skill["$id"])
                SkillList.append(newSkill)
            
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
                # skill["point_PP"] = chosen.point_PP Dont copy because we want to keep the original costs so you dont get stuck with a 3500 cost skill in thge first slot
                skill["point_SP"] = chosen.point_SP
                skill["flag"] = chosen.flag
                
                # Fixing descriptions
                for desc in descData["rows"]:
                    if desc["$id"] == skill["$id"]:
                        desc["help"] = chosen.id
                        break
                
                if isPower:
                    Power(skill)
                
                if isShape:
                    Shape(skill)
                    
                if isLinkCost:
                    LinkCost(skill)
                
            skillDescFile.seek(0)
            skillDescFile.truncate()
            json.dump(descData, skillDescFile, indent=2, ensure_ascii=False)
        skillFile.seek(0)
        skillFile.truncate()
        json.dump(skillData, skillFile, indent=2, ensure_ascii=False)


      
        skillFile.seek(0)
        skillFile.truncate()
        json.dump(skillData, skillFile, indent=2, ensure_ascii=False)    

def Shape(skill):
    Circle = 1
    Square = 2
    Hexagon = 3
    Octagram = 4
    Diamond = 5
    skill["shape"] = random.choice([Circle,Square,Hexagon,Octagram,Diamond])

def Power(skill):
    dist = [.3,.5,.7,.9,1.2,1.5,1.8,2,2.2,2.5,3]
    val1 = random.choice(dist)
    val2 = random.choice(dist)
    time = random.choice(dist)
    skill["val1"] = int(skill["val1"] * val1)
    skill["val2"] = int(skill["val2"] * val2)
    skill["time"] = int(skill["time"] * time)

def LinkCost(skill):
    skillRoll = random.choice([.15,.25,.5,.7,1.2,1.5,2])
    skill["point_SP"] = int(skill["point_SP"] * skillRoll)

def SkillLinkNodeRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv.json", 'r+', encoding='utf-8') as linkFile: # Randomizes the node shape for skill link trees
        linkData = json.load(linkFile)
        for link in linkData["rows"]:
            for i in range(1,6):
                link[f"rvs_effect0{i}"] = random.randrange(1,5)

        linkFile.seek(0)
        linkFile.truncate()
        json.dump(linkData, linkFile, indent=2, ensure_ascii=False)