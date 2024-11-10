import EnemyRandoLogic
import json
import math
import Helper
import time
import random

FLDSkillMaxLv = [3, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 5, 3, 3, 3, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 3, 5, 3, 5, 3, 3, 5, 5, 5, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 3, 5, 5]
# Helper.FindValues("./_internal/JsonOutputs/common/FLD_FieldSkillList.json", ["$id"], Helper.inclRange(2, 7) + Helper.inclRange(9,74), "MaxLevel")
FLDSkillIDs = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# print(Helper.inclRange(2,7) + Helper.inclRange(9,74))

AdjustedFLDSkillSettingID1 = [1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 33, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 2, 2, 3, 2, 2, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 4, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
AdjustedFLDSkillSettingID2 = [0, 1, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 1, 2, 2, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 3, 2, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 2, 2, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 1, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 3, 1, 1, 0, 1, 0, 0, 0, 0, 3, 1, 3, 3, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

BladeIDs = [1008,1016] + Helper.FindValues("./_internal/JsonOutputs/common/BLD_RareList.json", ["$id"], Helper.inclRange(1,37), "Blade")

ValidCrystalListIDs = Helper.inclRange(45002,45010) + [45016] + Helper.inclRange(45017,45043) + [45056, 45057]

def AllRareBlades():
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Condition"] , 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Prob1"] , 1)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Assure1"] , 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Prob2"] , 1)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Assure2"] , 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Prob3"] , 1)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Assure3"] , 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Prob4"] , 1)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Assure4"] , 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Prob5"] , 1)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BLD_RareList.json", ["Assure5"] , 0)

def FieldSkillLevelAdjustment(CheckboxList, CheckboxStates):
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_FieldSkillList.json", ["MaxLevel"] , 1)
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Field Skill QOL Box":
            FieldSkillBox = j
    if CheckboxStates[FieldSkillBox].get() == True:
        FieldAchievementSetFile = "./_internal/JsonOutputs/common/FLD_AchievementSet.json"
        with open(FieldAchievementSetFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
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
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)
        #BladeAdjustmentFile = "./_internal/JsonOutputs/common/CHR_Bl.json"
        """ with open(BladeAdjustmentFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                row["FskillAchivement1"] = 1404
                row["FskillAchivement2"] = 1404
                row["FskillAchivement3"] = 1404
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2) """

def FieldSkillChecksAdjustment(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Field Skill QOL Box":
            FieldSkillBox = j
    if CheckboxStates[FieldSkillBox].get() == True:
        SkillSettingFile = "./_internal/JsonOutputs/common/FLD_FieldSkillSetting.json"
        with open(SkillSettingFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["FieldSkillID1"]:
                    for i in range(0, len(FLDSkillIDs)):
                        if row["FieldSkillID1"] == FLDSkillIDs[i]:
                            row["FieldSkillLevel1"] = math.ceil(row["FieldSkillLevel1"]/FLDSkillMaxLv[i])
                if row["FieldSkillID2"]:    
                    for i in range(0, len(FLDSkillIDs)):
                        if row["FieldSkillID2"] == FLDSkillIDs[i]:
                            row["FieldSkillLevel2"] = math.ceil(row["FieldSkillLevel2"]/FLDSkillMaxLv[i])
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

def AdjustingCrystalList(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Core Crystal Changes Box":
            CoreCrystalChangesBox = j
    if CheckboxStates[CoreCrystalChangesBox].get() == True:
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CrystalList.json", ["BladeID"], 0)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CrystalList.json", ["CommonID"], 0)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CrystalList.json", ["CommonWPN"], 0)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CrystalList.json", ["CommonAtr"], 0)
        ITMCrystalFile = "./_internal/JsonOutputs/common/ITM_CrystalList.json"
        with open(ITMCrystalFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            RandomBlades = BladeIDs.copy()
            random.shuffle(RandomBlades)
            for k in range(0, len(ValidCrystalListIDs)):
                for row in data["rows"]:
                    if row["$id"] == ValidCrystalListIDs[k]:
                        row["NoMultiple"] = k + 1
                        row["ValueMax"] = 1
                        row["BladeID"] = RandomBlades[k]
                        row["Name"] = 12
                        break
            for row in data["rows"]:
                for i in range(45011,45014):
                    if row["$id"] == i:
                        row["RareTableProb"] = 0
                        row["RareBladeRev"] = 0
                        row["CommonPow"] = 0
                        row["AssureP"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)        

def ChangeChestContents(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Core Crystal Changes Box":
            CoreCrystalChangesBox = j
    if CheckboxStates[CoreCrystalChangesBox].get() == True:
        ChestFile = "./_internal/JsonOutputs/common_gmk/ma21a_FLD_TboxPop.json"
        with open(ChestFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 2116:
                    row["itm1ID"] = 45020
                    row["itm2ID"] = 45021
                    row["itm3ID"] = 45022
                    row["itm4ID"] = 45023
                    row["itm5ID"] = 45024
                    row["itm6ID"] = 45025
                    row["itm7ID"] = 45026
                    row["itm8ID"] = 45027                    
                    row["itm2Num"] = 1
                    row["itm3Num"] = 1
                    row["itm4Num"] = 1
                    row["itm5Num"] = 1
                    row["itm6Num"] = 1
                    row["itm7Num"] = 1
                    row["itm8Num"] = 1                    
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

def CoreCrystalChanges(CheckboxList, CheckboxStates):
    AllRareBlades()
    #FieldSkillChecksAdjustment(CheckboxList, CheckboxStates)
    FieldSkillLevelAdjustment(CheckboxList, CheckboxStates)
    #AdjustingCrystalList(CheckboxList, CheckboxStates)
    # ChangeChestContents(CheckboxList, CheckboxStates)