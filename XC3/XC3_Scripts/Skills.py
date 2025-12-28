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
        

def SkillRandoMain():
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/battle/msg_btl_skill_name.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                skillData = json.load(skillFile)
                nameData = json.load(nameFile)
            
                skillFiles = SkillRandoFiles(skillData, nameData, enhanceData, Options.MajorSkillOption.GetSpinbox())
                
                # Vanilla replacements used by all
                replacementIDs =  IDs.BaseGameClassSkills + IDs.InoSkillTree + IDs.SoulhackerSkills + IDs.UroSkills + IDs.DLC4Skills + IDs.PairSkills
                
                # Vanilla skills that should stay in their respective game
                baseGameOnlyIDs = [116, 223, 224, 225]
                dlc4OnlyIDs = [330, 340, 404]
                
                if Options.MajorSkillOption_ClassSkills.GetState():
                    skillFiles.SkillRando(IDs.BaseGameClassSkills, replacementIDs, dlc4OnlyIDs, True, [(0,20),(21,40),(41,60),(61,80),(81,100)])
                if Options.MajorSkillOption_InoSkills.GetState():
                    skillFiles.SkillRando(IDs.InoSkillTree, replacementIDs, dlc4OnlyIDs, True, [(20,30),(40,50),(60,100)])
                if Options.MajorSkillOption_HackerSkills.GetState():
                    skillFiles.SkillRando(IDs.SoulhackerSkills, replacementIDs, dlc4OnlyIDs, True, [(20,40), (60,90)])
                if Options.MajorSkillOption_OuroSkills.GetState():
                    skillFiles.SkillRando(IDs.UroSkills, replacementIDs, dlc4OnlyIDs, True, [(20,50), (70,80)])            
                if Options.MajorSkillOption_AffinityGrowthSkills.GetState():
                    skillFiles.SkillRando(IDs.DLC4Skills, replacementIDs, baseGameOnlyIDs, False, [(20,40),(50,70),(80,100)])
                if Options.MajorSkillOption_UnitySkills.GetState():
                    skillFiles.SkillRando(IDs.PairSkills, replacementIDs, baseGameOnlyIDs, False, [(30,60),(70,100)])
        
                JSONParser.CloseFile(skillData, skillFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

class SkillRandoFiles():
    def __init__(self, skillData, nameData, enhanceData, odds):
        self.originalSkillData = skillData
        self.skillData = skillData
        self.nameData = nameData
        self.enhanceData = enhanceData
        self.odds = odds
        
    def SkillRando(self, targetSkillIDs, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly, customSkillEnhancementRanges):
        
        skillList:Helper.RandomGroup = self.CreateSkillList(replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
        
        for skill in self.skillData["rows"]: # Replace the list
            copyKeys = ["Enhance1", "Enhance2", "Enhance3", "Enhance4", "Enhance5", "Icon"]
            if not Helper.OddsCheck(self.odds):
                continue
            if skill["$id"] not in targetSkillIDs:
                continue
            
            chosenSkill = skillList.SelectRandomMember()
    
            if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                self.DetermineName(chosenSkill, skill)
                chosenSkill = self.DefineNewSkill(chosenSkill, customSkillEnhancementRanges)
            else:
                copyKeys.append("Name") # Names should be copied if they are vanilla skills
                self.ExtendSkillLength(chosenSkill)
            
            Helper.CopyKeys(skill, chosenSkill, copyKeys, isGoodKeys=True)

    def CreateSkillList(self, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly):
        skillList = Helper.RandomGroup()
        
        if Options.MajorSkillOption_VanillaSkills.GetState(): # Generate Vanilla Replacement Skill List
            for skill in self.originalSkillData["rows"]:
                if skill["$id"] in invalidReplacementIDs:
                    continue
                if skill["$id"] not in replacementSkillIDs:
                    continue
                skillList.AddNewData(copy.copy(skill))
        
        if Options.MajorSkillOption_CustomSkills.GetState(): # Generate Custom Replacement Skill List
            copyListCurrentGroup:list[Enhancements.Enhancement] = Enhancements.EnhancementsList.currentGroup
            for enh in copyListCurrentGroup:            
                if isCustomReplacementBaseGameOnly:
                    if enh.isFutureRedeemedOnly: # Dont add FR only enhancement to the pool 
                            continue
                    elif enh.isBaseGameOnly:  # Dont add Base Game only enhancement to the pool 
                        continue
                if enh.skillIcon == Enhancements.invalidSkillIcon:
                    continue
                skillList.AddNewData(copy.copy(enh))
                    
        if skillList.isEmpty():
            raise Exception("Empty pool of choices, choose Vanilla, Custom or Both")
        
        return skillList

    def ExtendSkillLength(self, chosenSkill):
        '''Some vanilla skills only power up twice, in this case we will extend the higher level through all 5 possible slots, this means if you get a skill that has 2 levels in a skill spot that has 5, you will only ever be able to get level 2 of that skill'''
        for i in range(1,6):
            if chosenSkill[f"Enhance{i}"] != 0:
                maxLv = i
            else:
                break
        
        for f in range(maxLv+1,6):
            chosenSkill[f"Enhance{f}"] = chosenSkill[f"Enhance{maxLv}"]

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
 
