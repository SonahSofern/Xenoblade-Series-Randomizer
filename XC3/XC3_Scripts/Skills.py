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
        self.originalSkillData = copy.deepcopy(skillData) # A copy of the original data to pull vanilla skills from
        self.skillData = skillData
        self.nameData = nameData
        self.enhanceData = enhanceData
        self.odds = odds
        
    def SkillRando(self, targetSkillIDs, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly, customSkillEnhancementRanges):     
        matchClassType = Options.MajorSkillOption_MatchClassType.GetState()
        
        if matchClassType:
            classTypeWeight = Options.MajorSkillOption_MatchClassType.GetSpinbox()
            AttackerGroup = self.CreateRoleGroup(IDs.AttackerSkillIDs, Enhancements.Atk, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
            DefenderGroup = self.CreateRoleGroup(IDs.DefenderSkillIDs, Enhancements.Def, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
            HealerGroup = self.CreateRoleGroup(IDs.HealerSkillIDs, Enhancements.Hlr, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
            MixedGroup = self.CreateRoleGroup(IDs.MixedSkillIDs, Enhancements.Misc, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
        else:
            skillList:Helper.RandomGroup = self.CreateSkillList(replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly)
            
        for skill in self.skillData["rows"]: # Replace the list
            copyKeys = ["Name", "Enhance1", "Enhance2", "Enhance3", "Enhance4", "Enhance5", "Icon"]
            if not Helper.OddsCheck(self.odds):
                continue
            if skill["$id"] not in targetSkillIDs:
                continue
            
            if matchClassType:
                group:Helper.RandomGroup = random.choices(self.SelectRoleTypedMember(skill, AttackerGroup, DefenderGroup, HealerGroup, MixedGroup), [classTypeWeight, 100-classTypeWeight], k=1)[0]
            else:
                group = skillList
                
            chosenSkill = group.SelectRandomMember()
                
            if isinstance(chosenSkill, Enhancements.Enhancement): # If we get a custom enhancement convert it to workable data
                chosenSkill = self.DefineNewSkill(chosenSkill, customSkillEnhancementRanges)
            else:
                self.ExtendSkillLength(chosenSkill)
            
            Helper.CopyKeys(skill, chosenSkill, copyKeys, isGoodKeys=True)

    def CreateRoleGroup(self, roleSkillIDs, roleType, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly):
        matching = self.CreateSkillList([x for x in roleSkillIDs if x in replacementSkillIDs], invalidReplacementIDs, isCustomReplacementBaseGameOnly, roleType)
        nonMatching = self.CreateSkillList([x for x in replacementSkillIDs if x not in roleSkillIDs], invalidReplacementIDs, isCustomReplacementBaseGameOnly, roleType)
        return [matching, nonMatching]
    
    def SelectRoleTypedMember(self, skill, AttackerGroup, DefenderGroup, HealerGroup, MixedGroup):
        if skill["$id"] in IDs.AttackerSkillIDs:
            return AttackerGroup
        if skill["$id"] in IDs.DefenderSkillIDs:
            return DefenderGroup
        if skill["$id"] in IDs.HealerSkillIDs:
            return HealerGroup
        return MixedGroup

    def CreateSkillList(self, replacementSkillIDs, invalidReplacementIDs, isCustomReplacementBaseGameOnly, customReplacementTargetRole = None):
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
                if customReplacementTargetRole != None and enh.roleType != customReplacementTargetRole:
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
        "Name": self.DetermineName(chosenSkill),
        "Icon": chosenSkill.skillIcon,
        }
        for i in range(1,6):
            if len(ranges) < i:
                newSkill[f"Enhance{i}"] = 0
            else:
                newSkill[f"Enhance{i}"] = chosenSkill.CreateEffect(self.enhanceData, powerPercent=Helper.RandomDecimal(ranges[i-1][0],ranges[i-1][1]))
        return newSkill

    def DetermineName(self, chosenSkill:Enhancements.Enhancement):
        if chosenSkill.roleType == Enhancements.Atk:
            secondWordList = ["Strikes", "Edge", "Blast", "Slashes", "Barrages", "Fists", "Combos"]
        elif chosenSkill.roleType == Enhancements.Hlr:
            secondWordList = ["Support", "Training", "Assist", "Recovery", "Gambit", "Blessing"]
        elif chosenSkill.roleType == Enhancements.Def:
            secondWordList = ["Footwork", "Defenses", "Stance", "Eye", "Sanctuary", "Formation"]
        else:
            secondWordList = ["Aura", "Power", "Boost", "System", "Potential"]
            
        newName = {
            "$id": len(self.nameData["rows"])+1,
            "label": "<D776CC82>",
            "style": 15,
            "name": f"{chosenSkill.name} {random.choice(secondWordList)}"
        }
        
        self.nameData["rows"].append(newName)
        
        return newName["$id"]
            

            
        
 # Used to get IDs
# def GetSkillRoleType(targetRoleType):
#     roleList = []
#     import json
#     with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
#         with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
#             with open(f"XC3/JsonOutputs/btl/BTL_EnhanceEff.json", 'r+', encoding='utf-8') as enhanceEffFile:
#                 skillData = json.load(skillFile)
#                 enhanceData = json.load(enhanceFile)
#                 enhanceEffData = json.load(enhanceEffFile)
#                 replacementIDs =  IDs.BaseGameClassSkills + IDs.InoSkillTree + IDs.SoulhackerSkills + IDs.UroSkills + IDs.DLC4Skills + IDs.PairSkills
#                 for skill in skillData["rows"]:
#                     if skill["$id"] > 96:
#                         if skill["$id"] in replacementIDs:
#                             if skill["$id"] not in AttackerSkillIDs + DefenderSkillIDs + HealerSkillIDs:
#                                 roleList.append(skill["$id"])
#                             # for enh in enhanceData["rows"]:
#                             #     if skill["Enhance1"] == enh["$id"]:
#                             #         for enhEff in EnhancementsList.originalGroup:
#                             #             if enh["EnhanceEffect"] == enhEff.effID:
#                             #                 if enhEff.roleType == targetRoleType:
#                             #                     roleList.append(skill["$id"])
                                        
#                 return roleList

# AttackerSkillIDs = [1, 2, 3, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 41, 42, 43, 44, 53, 54, 55, 56, 69, 70, 71, 72, 73, 74, 75, 76, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 109, 110, 112, 114, 115, 116, 118, 122, 124, 128, 132, 133, 135, 136, 178, 179, 181, 200, 203, 205, 211, 212, 213, 218, 220, 221, 223, 227, 233, 237, 240, 243, 245, 247, 252, 253, 256, 257, 263, 293, 295, 296, 297, 299, 300, 302, 303, 304, 305, 315, 341, 342, 350, 351, 353, 401, 402, 403, 405, 409, 412, 415]
# DefenderSkillIDs = [5, 6, 7, 8, 17, 18, 19, 20, 45, 46, 47, 48, 61, 62, 63, 64, 77, 78, 79, 80, 111, 117, 120, 130, 131, 189, 190, 196, 199, 201, 208, 209, 214, 224, 232, 235, 244, 251, 255, 258, 260, 261, 262, 272, 276, 322, 323, 324, 343, 411]
# HealerSkillIDs = [9, 10, 11, 12, 13, 14, 15, 16, 33, 34, 35, 36, 37, 38, 39, 40, 49, 50, 51, 52, 57, 58, 59, 60, 65, 66, 67, 68, 81, 82, 83, 84, 121, 191, 210, 215, 216, 217, 225, 226, 238, 264, 270, 291, 313, 331, 332, 333, 334]
# MixedSkillIDs = [] + GetSkillRoleType(1)

# print(MixedSkillIDs)
