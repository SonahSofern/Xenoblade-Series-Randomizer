import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options
from XC3.XC3_Scripts import Enhancements

def SkillRando(): # Match class to skill type probably or at least an option to
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

                if vanillaSkills: # Generate Vanilla Skill List
                    skillList.GenData(skillData["rows"])
                    filteringList = copy.deepcopy(skillList.originalGroup) # Make a copy because we cant filter this while looping over it
                    for skill in (filteringList):
                        if not PassSkillCheck(skill, ignoreSkillIDs):
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
                    if not PassSkillCheck(skill, ignoreSkillIDs):
                        continue
                    
                    chosenSkill = skillList.SelectRandomMember()

                    if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                        DetermineName(chosenSkill, skill, nameData)
                        chosenSkill = DefineNewSkill(chosenSkill, enhanceData)
                        
                    Helper.CopyKeys(skill, chosenSkill, ignoreKeys)

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

def DefineNewSkill(chosenSkill:Enhancements.Enhancement, enhanceData):
    return  {
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
 