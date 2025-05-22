# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_PSVskill.html
import json, random, time
import Options, scripts.PopupDescriptions, scripts.JSONParser, scripts.Helper

yoinkSkills = [140,138]
MeliaSkills = [152,157,159]
MechonisArmor = [176]
SharlaCoolOff = [110]
ReynTaunts = [32,35,46]

# Tree focus buffs like dunban gets agility for focusing this tree https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_PSVlink.html#6

class Skill: 
    newId = 0
    def __init__(self, _name, _shape, _target, _skill, _val1, _val2, _time, _point_PP, _point_SP, _flag, _id, type, icon):
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
        self.type = type
        self.icon = icon
        
def SkillRando():
    isShape = Options.AffinityTreeOption_Shape.GetState()
    isPower = Options.AffinityTreeOption_Power.GetState()
    isLinkCost = Options.AffinityTreeOption_LinkCost.GetState()
    isEffect = Options.AffinityTreeOption_Effect.GetState()
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_PSVskill.json", 'r+', encoding='utf-8') as skillFile:
        with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv/MNU_PSskil.json", 'r+', encoding='utf-8') as skillDescFile:
            with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv/MNU_PSskil.json", 'r+', encoding='utf-8') as psFile:
                psData = json.load(psFile)
                skillData = json.load(skillFile)
                descData = json.load(skillDescFile)
                odds = Options.AffinityTreeOption.GetSpinbox()
                
                SkillList:list[Skill]= []
                invalidSkills = yoinkSkills + MeliaSkills + MechonisArmor + SharlaCoolOff + ReynTaunts
                for skill in skillData["rows"]:
                    if skill["$id"] in invalidSkills:
                        continue
                    for ps in psData["rows"]:
                        if ps["$id"] == skill["$id"]:
                            newType = ps["type"]
                            newIcon = ps["icon"]
                            break
                    newSkill = Skill(skill["name"], skill["shape"], skill["target"], skill["skill"], skill["val1"], skill["val2"], skill["time"], skill["point_PP"], skill["point_SP"], skill["flag"], skill["$id"], newType, newIcon)
                    SkillList.append(newSkill)
                
                for skill in skillData["rows"]:
                    if not scripts.Helper.OddsCheck(odds):
                        continue
                    
                    if skill["$id"] in invalidSkills:
                        continue
                    if isEffect:
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
                                desc["type"] = chosen.type
                                desc["icon"] = chosen.icon
                                break
                        
                    if isPower:
                        Power(skill)
                    
                    if isShape:
                        Shape(skill, "shape")
                        SkillLinkNodeRando()
                        
                    if isLinkCost:
                        LinkCost(skill)
                    
                scripts.JSONParser.CloseFile(descData, skillDescFile)
            scripts.JSONParser.CloseFile(skillData, skillFile) 

def Shape(skill, key, excludeShapes = []):
    Circle = 1
    Square = 2
    Hexagon = 3
    Octagram = 4
    Diamond = 5
    shapeChoices = list((x for x in [Circle,Square,Hexagon,Octagram,Diamond] if x not in excludeShapes))
    skill[key] = random.choice(shapeChoices)

def Power(skill):
    dist = [.3,.5,.7,.9,1.2,1.5,1.8,2,2.2,2.5,3]
    val1, val2, time = (random.choices(dist,k=3))
    skill["val1"] = min(int(skill["val1"] * val1),255)
    skill["val2"] = min(int(skill["val2"] * val2),100)
    skill["time"] = min(int(skill["time"] * time),255)

linkCostRange = [.15,.25,.5,.7,1.2,1.5,2]
def LinkCost(skill):
    skillRoll = random.choice(linkCostRange)
    skill["point_SP"] = int(skill["point_SP"] * skillRoll)

def SkillLinkNodeRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_psv/MNU_PSset.json", 'r+', encoding='utf-8') as linkFile: # Randomizes the node shape for skill link trees
        linkData = json.load(linkFile)
        for link in linkData["rows"]:
            for i in range(1,6):
                Shape(link, f"rvs_effect0{i}", [5]) # Want to exlcude diamond shapes to keep vanilla behaviour since that symbolizes a non linkable skill (we could use all if we wanted)
        scripts.JSONParser.CloseFile(linkData, linkFile)
        

def SkillTreeDesc():
    myDesc = scripts.PopupDescriptions.Description()
    myDesc.Header(Options.AffinityTreeOption_Effect.name)
    myDesc.Text("Randomizes the skills in each characters skill tree.\nThis keeps the original cost of the node, regardless of the skill that replaces it.")
    myDesc.Image("Effect.png", "XCDE", 800)
    myDesc.Text("Shulk has Fiora's skill Maiden's Zeal", anchor="center")
    myDesc.Header(Options.AffinityTreeOption_Power.name)
    myDesc.Text("This option affects the power level of skill trees, from 30%-300% of their original strength")
    myDesc.Image("AmazingStars.png", "XCDE")
    myDesc.Text("Amazing Stars normally reduces only 15% of cooldown during night.", anchor="center")
    myDesc.Header(Options.AffinityTreeOption_LinkCost.name)
    myDesc.Text(f"This randomizes the cost when linking skills to your allies between {linkCostRange[0]}x-{linkCostRange[-1]}x")
    myDesc.Header(Options.AffinityTreeOption_Shape.name)
    myDesc.Text("This randomizes all skill node shapes into:\n- Circle\n- Square\n- Hexagon\n- Octagram\n- Diamond")
    myDesc.Image("SkillTreesNodeShape.png", "XCDE", 800)
    myDesc.Text("This also randomizes each character's link skill node shapes into:\n- Circle\n- Square\n- Hexagon\n- Octagram\nDiamond Skills will still not be linkable to keep vanilla behaviour")
    return myDesc