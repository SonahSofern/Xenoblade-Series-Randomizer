import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Enhancements, IDs, Options


def SkillRandoMain():
    if Options.SkillOptions_Class:
        SkillRando(IDs.BaseGameClassSkills, [(0,20),(21,40),(41,60),(61,80),(81,100)])
        SkillRando(IDs.InoSkillTree, [(20,30),(40,50),(60,100)])
        SkillRando(IDs.DLC4Skills, [(20,40),(50,70),(80,100)])
        SkillRando(IDs.PairSkills, [(30,60),(70,100)])
    if Options.SkillOptions_SingleNode.GetState():
        SkillRando(IDs.DLC4SingleSkills, [(50,80)])
        SkillRando(IDs.InoTreeNodes, [(10,30)])
        SkillRando(IDs.DLC4SingleSkills, [(30,80)])
        SkillRando(IDs.DLC4TreeNodes, [(20,40)])
    if Options.SkillOptions_Ouroborous.GetState():
        SkillRando(IDs.UroSkills, [(20,50), (70,80)])
    if Options.SkillOptions_Ouroborous.GetState() and Options.SkillOptions_SingleNode.GetState():
        SkillRando(IDs.UroTreeNodes, [(10,30)])
    if Options.SkillOptions_SoulHacker.GetState():
        SkillRando(IDs.SoulhackerSkills, [(20,40), (60,90)])
        
def SkillRando(targetSkillIDs, skillEnhancementRanges):
    ignoreKeys = ["$id", "UseTalent", "Name"]
    skillOdds = Options.SkillOptions.GetSpinbox()
    unusedSkills = Options.SkillOptions_Unused.GetState()
    vanillaSkills = Options.SkillOptions_Vanilla.GetState()
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/battle/msg_btl_skill_name.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                skillData = json.load(skillFile)
                nameData = json.load(nameFile)
                
                skillList = Helper.RandomGroup()

                if vanillaSkills: # Generate Vanilla Skill List
                    skillList.GenData(skillData["rows"])
                    filteringList = copy.deepcopy(skillList.originalGroup) # Make a copy because we cant filter this while looping over it
                    for skill in (filteringList):
                        if not PassSkillCheck(skill, targetSkillIDs):
                            skillList.FilterMember(skill)
                
                if unusedSkills: # Generate Custom Skill List
                    copyList = copy.deepcopy(Enhancements.EnhancementsList)
                    copyListCurrentGroup:list[Enhancements.Enhancement] = copyList.currentGroup
                    for enh in copyListCurrentGroup:
                        if enh.skillIcon != Enhancements.defaultSkillIcon:
                            skillList.AddNewData(enh)
                
                for skill in skillData["rows"]: # Replace the list
                    if not Helper.OddsCheck(skillOdds):
                        continue
                    if not PassSkillCheck(skill, targetSkillIDs):
                        continue
                    
                    chosenSkill = skillList.SelectRandomMember()

                    if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                        DetermineName(chosenSkill, skill, nameData)
                        chosenSkill = DefineNewSkill(chosenSkill, enhanceData, skillEnhancementRanges)
                        
                    Helper.CopyKeys(skill, chosenSkill, ignoreKeys)

                JSONParser.CloseFile(skillData, skillFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

def PassSkillCheck(skill, allowSkills):
    if skill["$id"] in allowSkills:
        return True
    return False

def DefineNewSkill(chosenSkill:Enhancements.Enhancement, enhanceData):
    newSkill = {
      "$id": "null",
      "ID": "null",
      "Name": chosenSkill.name,
      "DebugName": "",
      "Caption": 0,
      "Type": 0,
      "UseTalent": 0,
      "UseChr": 0,
      "Enhance1": chosenSkill.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal(0,20)),
      "Enhance2": chosenSkill.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal(21,40)),
      "Enhance3": chosenSkill.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal(41,60)),
      "Enhance4": chosenSkill.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal(61,80)),
      "Enhance5": chosenSkill.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal(81,100)),
      "EnSkillAchieve": 0,
      "RoleParam1": 0,
      "RoleParam2": 0,
      "<43BA3C37>": 0,
      "<A6E42F10>": 0,
      "UroProb1": 20,
      "UroProb2": 40,
      "UroProb3": 80,
      "Role": 0,
      "Icon": chosenSkill.skillIcon,
      "SortNo": 0
    }
    
    return newSkill

def DetermineName(chosenSkill:Enhancements.Enhancement, skill, nameData):
    if chosenSkill.roleType == Enhancements.Atk:
        secondWordList = ["Strikes", "Hits", "Blast"]
    elif chosenSkill.roleType == Enhancements.Hlr:
        secondWordList = ["Support", "Soothing", "Assist"]
    elif chosenSkill.roleType == Enhancements.Def:
        secondWordList = ["Footwork", "Defenses", "Stance"]
    else:
        secondWordList = ["Aura", "Power"]
        
    for name in nameData["rows"]:
        if name["$id"] == skill["Name"]:
            secondWord = random.choice(secondWordList)
            name["name"] = f"{chosenSkill.name} {secondWord}"
            break
 