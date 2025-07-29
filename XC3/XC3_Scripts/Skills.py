import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options
from XC3.XC3_Scripts import Enhancements

def SkillRando():
    ignoreKeys = ["$id", "UseTalent"]
    ignoreSkillIDs = [100,101,105,106,107] 
    InvalidEnhancements = [Enhancements.AgilityUp]
    skillOdds = XC3.XC3_Scripts.Options.SkillOptions.GetSpinbox()
    unusedSkills = XC3.XC3_Scripts.Options.SkillOptions_Unused.GetState()
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        skillData = json.load(skillFile)

        skillList = Helper.RandomGroup(skillData["rows"])
        for skill in (skillList.originalGroup):
            if not PassSkillCheck(skill, ignoreSkillIDs):
                skillList.FilterMember(skill)
                
        if unusedSkills:
            for enh in Enhancements.EnhancementsList:
                if enh in InvalidEnhancements:
                    continue
                skillList.AddNewData(AddNewSkill(skillList, enh))
        
        for skill in skillData["rows"]: # Replace the list
            if not Helper.OddsCheck(skillOdds):
                continue
            if not PassSkillCheck(skill, ignoreSkillIDs):
                continue
            chosenSkill = skillList.SelectRandomMember()
            skillList.CopyKeys(skill, chosenSkill, ignoreKeys)

        JSONParser.CloseFile(skillData, skillFile)

def PassSkillCheck(skill, ignoreSkills):
    if skill["$id"] in ignoreSkills:
        return False
    for i in range(1,6):
        if skill[f"Enhance{i}"] == 0:
            return False
    return True

def AddNewSkill(skillList:Helper.RandomGroup, e:Enhancements.Enhancement):
      return  {
      "$id": len(skillList.originalGroup) + 1,
      "ID": "<30F895AE>",
      "Name": DetermineName(e),
      "DebugName": "",
      "Caption": 0,
      "Type": 0,
      "UseTalent": 0,
      "UseChr": 0,
      "Enhance1": e.CreateEffect(),
      "Enhance2": e.CreateEffect(),
      "Enhance3": e.CreateEffect(),
      "Enhance4": e.CreateEffect(),
      "Enhance5": e.CreateEffect(),
      "EnSkillAchieve": 0,
      "RoleParam1": 0,
      "RoleParam2": 0,
      "<43BA3C37>": 0,
      "<A6E42F10>": 0,
      "UroProb1": 20,
      "UroProb2": 40,
      "UroProb3": 80,
      "Role": 0,
      "Icon": e.skillIcon,
      "SortNo": 0
    }
      
def DetermineName(enh:Enhancements.Enhancement):
    secondWord = random.choice(["Aura", "Power", "Stance"])
    return f"{enh.name} {secondWord}"
 