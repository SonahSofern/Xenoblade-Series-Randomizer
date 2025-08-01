import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options
from XC3.XC3_Scripts import Enhancements

def SkillRando():
    ignoreKeys = ["$id", "UseTalent", "Name"]
    ignoreSkillIDs = [100,101,105,106,107] 
    skillOdds = XC3.XC3_Scripts.Options.SkillOptions.GetSpinbox()
    unusedSkills = XC3.XC3_Scripts.Options.SkillOptions_Unused.GetState()
    vanillaSkills = XC3.XC3_Scripts.Options.SkillOptions_Vanilla.GetState()
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/battle/msg_btl_skill_name.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                skillData = json.load(skillFile)
                nameData = json.load(nameFile)
                
                skillList = Helper.RandomGroup()
                originalNames = Helper.RandomGroup()
                originalNames.GenData(nameData["rows"])

                if vanillaSkills: # Generate Vanilla Skill List
                    skillList.GenData(skillData["rows"])
                    for skill in (skillList.originalGroup):
                        if not PassSkillCheck(skill, ignoreSkillIDs):
                            skillList.FilterMember(skill)
                        
                if unusedSkills: # Generate Custom Skill List
                    for enh in Enhancements.SkillEnhancementList.originalGroup:
                        skillList.AddNewData(enh)
                
                for skill in skillData["rows"]: # Replace the list
                    if not Helper.OddsCheck(skillOdds):
                        continue
                    if not PassSkillCheck(skill, ignoreSkillIDs):
                        continue
                    
                    chosenSkill = skillList.SelectRandomMember()
                    
                    if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                        chosenSkill = DefineNewSkill(skillList, enh, enhanceData)
                        DetermineName(enh, skill, nameData)
                    # Apply the original names
                    skillList.CopyKeys(skill, chosenSkill, ignoreKeys)

                JSONParser.CloseFile(skillData, skillFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

def PassSkillCheck(skill, ignoreSkills):
    if skill["$id"] in ignoreSkills:
        return False
    for i in range(1,6):
        if skill[f"Enhance{i}"] == 0:
            return False
    return True

def DefineNewSkill(skillList:Helper.RandomGroup, e:Enhancements.Enhancement, enhanceData):
    newID = len(skillList.originalGroup) + 1
    return  {
      "$id": newID,
      "ID": f"{newID}",
      "Name": e.name,
      "DebugName": "",
      "Caption": 0,
      "Type": 0,
      "UseTalent": 0,
      "UseChr": 0,
      "Enhance1": e.CreateEffect(enhanceData, powerPercent=.2),
      "Enhance2": e.CreateEffect(enhanceData, powerPercent=.4),
      "Enhance3": e.CreateEffect(enhanceData, powerPercent=.6),
      "Enhance4": e.CreateEffect(enhanceData, powerPercent=.8),
      "Enhance5": e.CreateEffect(enhanceData, powerPercent=1),
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
      
def DetermineName(enh:Enhancements.Enhancement, skill, nameData):
    for name in nameData["rows"]:
        if name["$id"] == skill["Name"]:
            secondWord = random.choice(["Aura", "Power", "Stance"])
            name["name"] = f"{enh.name} {secondWord}"
            break
 