import json, random, copy
from scripts import JSONParser, Helper
from XC3.XC3_Scripts import Enhancements, IDs, Options

def MinorSkillShuffle(targetSkills): # Seperated to keep balancing intact. We could make these full skills but id rather not.
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        skillData = json.load(skillFile)        
        skillGroup = Helper.RandomGroup()
        
        # Create list
        for skill in skillData["rows"]:
            if skill["$id"] in targetSkills:
                skillGroup.AddNewData(skill)
                
        # Shuffle
        for skill in skillData["rows"]:
            if skill["$id"] in targetSkills:
                newSkill = skillGroup.SelectRandomMember()
                Helper.CopyKeys(skill, newSkill, ["$id", "UseTalent"])
                
        JSONParser.CloseFile(skillData, skillFile)
        

def SkillRandoMain(targetSkills):
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/battle/msg_btl_skill_name.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                skillData = json.load(skillFile)
                nameData = json.load(nameFile)
                
                skillList = Helper.RandomGroup()

                if Options.MajorSkillOption_VanillaSkills.GetState(): # Generate Vanilla Skill List
                    for skill in skillData["rows"]:
                        if skill["$id"] in targetSkills:
                            skillList.AddNewData(skill)
                
                if Options.MajorSkillOption_CustomSkills.GetState(): # Generate Custom Skill List
                    copyListCurrentGroup:list[Enhancements.Enhancement] = Enhancements.EnhancementsList.currentGroup
                    for enh in copyListCurrentGroup:
                        if enh.skillIcon != Enhancements.defaultSkillIcon:
                            skillList.AddNewData(copy.copy(enh))
                            
                if skillList.isEmpty():
                    raise Exception("Empty pool of choices, choose Vanilla, Custom or Both")
                
                skillFiles = SkillRandoFiles(skillList, skillData, nameData, enhanceData, Options.MajorSkillOption.GetSpinbox())
                
                if Options.MajorSkillOption_ClassSkills.GetState():
                    skillFiles.SkillRando(IDs.BaseGameClassSkills, [(0,20),(21,40),(41,60),(61,80),(81,100)])
                if Options.MajorSkillOption_InoSkills.GetState():
                    skillFiles.SkillRando(IDs.InoSkillTree, [(20,30),(40,50),(60,100)])
                if Options.MajorSkillOption_AffinityGrowthSkills.GetState():
                    skillFiles.SkillRando(IDs.DLC4Skills, [(20,40),(50,70),(80,100)])
                if Options.MajorSkillOption_UnitySkills.GetState():
                    skillFiles.SkillRando(IDs.PairSkills, [(30,60),(70,100)])
                if Options.MajorSkillOption_OuroSkills.GetState():
                    skillFiles.SkillRando(IDs.UroSkills, [(20,50), (70,80)])
                if Options.MajorSkillOption_HackerSkills.GetState():
                    skillFiles.SkillRando(IDs.SoulhackerSkills, [(20,40), (60,90)])
        
                JSONParser.CloseFile(skillData, skillFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

class SkillRandoFiles():
    def __init__(self, skillList, skillData, nameData, enhanceData, odds):
        self.skillList:Helper.RandomGroup = skillList
        self.skillData = skillData
        self.nameData = nameData
        self.enhanceData = enhanceData
        self.odds = odds
        
    def SkillRando(self, targetSkillIDs, skillEnhancementRanges):
        for skill in self.skillData["rows"]: # Replace the list
            copyKeys = ["Enhance1", "Enhance2", "Enhance3", "Enhance4", "Enhance5", "Icon"]
            if not Helper.OddsCheck(self.odds):
                continue
            if not self.isValidTargetSkill(skill, targetSkillIDs):
                continue
            
            chosenSkill = self.skillList.SelectRandomMember()
    
            if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                self.DetermineName(chosenSkill, skill)
                chosenSkill = self.DefineNewSkill(chosenSkill, skillEnhancementRanges)
            else:
                copyKeys.append("Name") # Names should be copied if they are vanilla skills
                chosenSkill = self.DefineNewSkill(self.GetEnhancement(skill), self.GetSkillRange(skill))  # Handle Mismatch of Vanilla Skill Lengths
            
            Helper.CopyKeys(skill, chosenSkill, copyKeys, isGoodKeys=True)

        self.skillList.RefreshCurrentGroup()

    def GetEnhancement(self, skill):
        for enh in self.enhanceData["rows"]:
            if skill["Enhance1"] == enh["$id"]:
                for enhEff in Enhancements.EnhancementsList.originalGroup:
                    if enh["EnhanceEffect"] == enhEff.effID:
                        return enhEff
        raise Exception(f"What the fuck")

    def GetSkillRange(self, skill): 
        levels = 5    
        for i in range(1,6):
            if skill[f"Enhance{i}"] == 0:
                levels = i
        
        ranges = [(1,10), (10,20), (20,40), (40,60), (60,100)]
        return ranges[:levels]
        

    def isValidTargetSkill(self, skill, allowSkills):
        if skill["$id"] in allowSkills:
            return True
        return False

    def DefineNewSkill(self, chosenSkill:Enhancements.Enhancement, ranges): 
        newSkill = {
        "Name": chosenSkill.name,
        "Icon": chosenSkill.skillIcon,
        }
        for i in range(1,6):
            if len(ranges) < i:
                newSkill[f"Enhance{i}"] = 0
            else:
                newSkill[f"Enhance{i}"] = chosenSkill.CreateEffect(self.enhanceData, powerPercent=Helper.RandomDecimal(ranges[i-1][0],ranges[i-1][1]))
        return newSkill

    def DetermineName(self,chosenSkill:Enhancements.Enhancement, skill):
        if chosenSkill.roleType == Enhancements.Atk:
            secondWordList = ["Strikes", "Edge", "Blast", "Slashes"]
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
 