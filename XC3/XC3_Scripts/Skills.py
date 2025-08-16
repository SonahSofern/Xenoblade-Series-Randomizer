import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Enhancements, IDs, Options

def SkillRandoMain():
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
                
                if unusedSkills: # Generate Custom Skill List
                    copyList = copy.deepcopy(Enhancements.EnhancementsList)
                    copyListCurrentGroup:list[Enhancements.Enhancement] = copyList.currentGroup
                    for enh in copyListCurrentGroup:
                        if enh.skillIcon != Enhancements.defaultSkillIcon:
                            skillList.AddNewData(enh)
                
                skillFiles = SkillRandoFiles(skillList, skillData, nameData, enhanceData)
                
                if Options.SkillOptions_Class:
                    skillFiles.SkillRando(IDs.BaseGameClassSkills, [(0,20),(21,40),(41,60),(61,80),(81,100)])
                    skillFiles.SkillRando(IDs.InoSkillTree, [(20,30),(40,50),(60,100)])
                    skillFiles.SkillRando(IDs.DLC4Skills, [(20,40),(50,70),(80,100)])
                    skillFiles.SkillRando(IDs.PairSkills, [(30,60),(70,100)])
                if Options.SkillOptions_SingleNode.GetState():
                    skillFiles.SkillRando(IDs.DLC4SingleSkills, [(50,80)])
                    skillFiles.SkillRando(IDs.InoTreeNodes, [(10,30)])
                    skillFiles.SkillRando(IDs.DLC4SingleSkills, [(30,80)])
                    skillFiles.SkillRando(IDs.DLC4TreeNodes, [(20,40)])
                if Options.SkillOptions_Ouroborous.GetState():
                    skillFiles.SkillRando(IDs.UroSkills, [(20,50), (70,80)])
                if Options.SkillOptions_Ouroborous.GetState() and Options.SkillOptions_SingleNode.GetState():
                    skillFiles.SkillRando(IDs.UroTreeNodes, [(10,30)])
                if Options.SkillOptions_SoulHacker.GetState():
                    skillFiles.SkillRando(IDs.SoulhackerSkills, [(20,40), (60,90)])
        
                JSONParser.CloseFile(skillData, skillFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

class SkillRandoFiles():
    def __init__(self, skillList, skillData, nameData, enhanceData):
        self.skillList:Helper.RandomGroup = skillList
        self.skillData = skillData
        self.nameData = nameData
        self.enhanceData = enhanceData
        
    def SkillRando(self,targetSkillIDs, skillEnhancementRanges): # Create the list once  
        ignoreKeys = ["$id", "UseTalent", "Name"]
        skillOdds = Options.SkillOptions.GetSpinbox()
        
        filteringList = copy.deepcopy(self.skillList.originalGroup) # Make a copy because we cant filter this while looping over it
        for skill in (filteringList):
            if isinstance(skill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                continue
            if not self.PassSkillCheck(skill, targetSkillIDs):
                self.skillList.FilterMember(skill)
        
        for skill in self.skillData["rows"]: # Replace the list
            if not Helper.OddsCheck(skillOdds):
                continue
            if not self.PassSkillCheck(skill, targetSkillIDs):
                continue
            if len(self.skillList.originalGroup) < 1:
                continue
            
            chosenSkill = self.skillList.SelectRandomMember()

            if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                self.DetermineName(chosenSkill, skill)
                chosenSkill = self.DefineNewSkill(chosenSkill, skillEnhancementRanges)
                
            Helper.CopyKeys(skill, chosenSkill, ignoreKeys)

        self.skillList.RefreshCurrentGroup()

    def PassSkillCheck(self, skill, allowSkills):
        if skill["$id"] in allowSkills:
            return True
        return False

    def DefineNewSkill(self, chosenSkill:Enhancements.Enhancement, ranges):
        newSkill = {
        "$id": "null",
        "ID": "null",
        "Name": chosenSkill.name,
        "DebugName": "",
        "Caption": 0,
        "Type": 0,
        "UseTalent": 0,
        "UseChr": 0,
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
        for i in range(1,6):
            if len(ranges) < i:
                newSkill[f"Enhance{i}"] = 0
            else:
                newSkill[f"Enhance{i}"] = chosenSkill.CreateEffect(self.enhanceData, powerPercent=Helper.RandomDecimal(ranges[i-1][0],ranges[i-1][1]))
        return newSkill

    def DetermineName(self,chosenSkill:Enhancements.Enhancement, skill):
        if chosenSkill.roleType == Enhancements.Atk:
            secondWordList = ["Strikes", "Edge", "Blast"]
        elif chosenSkill.roleType == Enhancements.Hlr:
            secondWordList = ["Support", "Training", "Assist"]
        elif chosenSkill.roleType == Enhancements.Def:
            secondWordList = ["Footwork", "Defenses", "Stance"]
        else:
            secondWordList = ["Aura", "Power"]
            
        for name in self.nameData["rows"]:
            if name["$id"] == skill["Name"]:
                secondWord = random.choice(secondWordList)
                name["name"] = f"{chosenSkill.name} {secondWord}"
                break
 