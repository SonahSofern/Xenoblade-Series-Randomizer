import EnemyRandoLogic as EnemyRandoLogic
import json
from scripts import Helper, JSONParser
import random
import Options
import IDs
import RaceMode

FLDSkillMaxLv = [3, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 3, 3, 3, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 5, 3, 3, 5, 5, 5, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 5, 5]
# Helper.FindValues("./XC2/_internal/JsonOutputs/common/FLD_FieldSkillList.json", ["$id"], Helper.inclRange(2, 7) + Helper.inclRange(9,74), "MaxLevel")

BladeFieldSkills = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# print(Helper.inclRange(2,7) + Helper.inclRange(9,74))

AdjustedFLDSkillSettingID1 = [1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 33, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 2, 2, 3, 2, 2, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 4, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
AdjustedFLDSkillSettingID2 = [0, 1, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 1, 2, 2, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 3, 2, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 2, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 1, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 3, 1, 1, 0, 1, 0, 0, 0, 0, 3, 1, 3, 3, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

BladeIDs = [1008, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1050, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1104, 1108, 1109, 1105, 1106, 1107, 1111]

ValidCrystalListIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]

FieldSkillAchievementIDs = Helper.InclRange(1,3824)
ChangeableFieldSkillAchievementIDs = [12, 13, 14, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104, 112, 113, 114, 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164, 172, 173, 174, 182, 183, 184, 192, 193, 194, 202, 203, 204, 212, 213, 214, 222, 223, 224, 232, 233, 234, 242, 243, 244, 252, 253, 254, 262, 263, 264, 272, 273, 274, 282, 283, 284, 292, 293, 294, 302, 303, 304, 312, 313, 314, 322, 323, 324, 332, 333, 334, 342, 343, 344, 352, 353, 354, 362, 363, 364, 372, 373, 374, 382, 383, 384, 392, 393, 394, 402, 403, 404, 412, 413, 414, 422, 423, 424, 432, 433, 434, 442, 443, 444, 452, 453, 454, 462, 463, 464, 1645, 1646, 1647, 1655, 1656, 1657, 1665, 1666, 1667, 1675, 1676, 1677, 1746, 1747, 1748, 1756, 1757, 1758, 1766, 1767, 1768]

def RareBladeProbabilityEqualizer(): # makes it so all blades are equally likely to be pulled
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BLD_RareList.json", ["Condition", "Assure1", "Assure2", "Assure3", "Assure4", "Assure5"] , 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BLD_RareList.json", ["Prob1", "Prob2", "Prob3", "Prob4", "Prob5"] , 1)

def FieldSkillLevelAdjustment():
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_FieldSkillList.json", ["MaxLevel"] , 1)
    FieldAchievementSetFile = "./XC2/_internal/JsonOutputs/common/FLD_AchievementSet.json"
    with open(FieldAchievementSetFile, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(ChangeableFieldSkillAchievementIDs)):
                if row["$id"] == ChangeableFieldSkillAchievementIDs[i]:
                    if row["AchievementID1"] != 0:
                        row["AchievementID1"] = 40
                    if row["AchievementID2"] != 0:
                        row["AchievementID2"] = 40
                    if row["AchievementID3"] != 0:
                        row["AchievementID3"] = 40
                    if row["AchievementID4"] != 0:
                        row["AchievementID4"] = 40
                    if row["AchievementID5"] != 0:
                        row["AchievementID5"] = 40
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    # JSONParser.ChangeJSONFile("common/FLD_AchievementSet.json",Helper.StartsWith("AchievementID",1,5), Helper.InclRange(1,3824), [40], (x for x in FieldSkillAchievementIDs if x in ChangeableFieldSkillAchievementIDs) )

def AdjustingCrystalList():
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/ITM_CrystalList.json", ["Condition", "BladeID", "CommonID", "CommonWPN", "CommonAtr"], 0)
    ITMCrystalFile = "./XC2/_internal/JsonOutputs/common/ITM_CrystalList.json"
    with open(ITMCrystalFile, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for k in range(0, len(ValidCrystalListIDs)):
            for row in data["rows"]:
                if row["$id"] == ValidCrystalListIDs[k]:
                    row["BladeID"] = RandomBlades[k]
                    row["Condition"] = 0
                    row["ValueMax"] = 1
                    row["NoMultiple"] = k + 11
                    break
        for row in data["rows"]:
            for i in range(45011,45014):
                if row["$id"] == i:
                    row["RareTableProb"] = 0
                    row["RareBladeRev"] = 0
                    row["AssureP"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FixingGivenCoreCrystalTutorial():
    with open("./XC2/_internal/JsonOutputs/common/MNU_BladeCreate.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["limited_item"] == 45010:
                row["limited_item"] = 45001
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_AddItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] ==87:
                row["ItemID1"] = 45001
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def LandofChallengeRelease(): #frees shulk, elma, fiora from land of challenge restriction
    Helper.SubColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", "Flag", "OnlyChBtl", 0)

def RegularLootDistribution(): #Adds core crystals to the loot pool if race mode isn't on (Chests Only)
    TotalTBox = 667
    ItemPool = []
    ChestPercent = IDs.CurrentSliderOdds
    AdjustedValidCrystalList = []
    for i in range(0, TotalTBox):
        if AdjustedValidCrystalList == []: #this makes sure all crystals get rotated in evenly, preventing you getting locked out of one crystal permanently if it doesn't get shuffled in.
            AdjustedValidCrystalList.extend(ValidCrystalListIDs)
        if ChestPercent > random.randint(0,100):
            ChosenCrystal = random.choice(AdjustedValidCrystalList)
            ItemPool.append(ChosenCrystal)
            AdjustedValidCrystalList.remove(ChosenCrystal)
        else:
            ItemPool.append(0)
    k = 0
    for TBoxFile in IDs.ValidTboxMapNames:
        with open(TBoxFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] not in IDs.InvalidTreasureBoxIDs:
                    row["itm8ID"] = ItemPool[k]
                    if ItemPool[k] != 0:
                        row["itm8Num"] = 1
                        row["itm8Per"] = 0
                    k = k + 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def FixRoc(): # Fixes Roc softlock
    with open("./XC2/_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for row in data["rows"]:
            if row["BladeID"] == 1008:
                row["Condition"] = 2212
                CrystalID = row["$id"]
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_BladeCreate.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for row in data["rows"]:
            if row["$id"] == 2:
                row["limited_item"] = CrystalID
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FixOpeningSoftlock():
    StartingCondListRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingCondScenarioRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", "$id") + 1
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondListRow, "Premise": 0, "ConditionType1": 1, "Condition1": StartingCondScenarioRow, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondScenarioRow, "ScenarioMin": 2001, "ScenarioMax": 10048, "NotScenarioMin": 0, "NotScenarioMax": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for row in data["rows"]:
            if row["BladeID"] != 1008:
                row["Condition"] = StartingCondListRow
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)    

def FixArtReleaseLevels(): # Fixes issue with NG+ blades having incredibly high level requirements for arts
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for row in data["rows"]:
            if (row["$id"] not in IDs.AutoAttacks) & (row["WpnType"] != 17):
                for i in range(1, 6):
                    row[f"ReleaseLv{i}"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CoreCrystalChanges():
    RareBladeProbabilityEqualizer()
    AdjustingCrystalList()
    LandofChallengeRelease()
    FixingGivenCoreCrystalTutorial()
    if not Options.RaceModeOption.GetState():
        RegularLootDistribution()
        FixRoc()
        FixOpeningSoftlock() # Removes ability to pull before you get Pyra, softlocking if you don't get a blade with arts 
        FixArtReleaseLevels() # Need to just call Hybrid's function MakeAllArtsAccessible() when I merge it with my branch
        RaceMode.FindtheBladeNames()
