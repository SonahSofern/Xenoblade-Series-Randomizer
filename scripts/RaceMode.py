import Helper as Helper
import json
import EnemyRandoLogic as EnemyRandoLogic
import random
from IDs import AllRaceModeItemTypeIDs, RaceModeAuxCoreIDs, A1RaceModeCoreChipIDs, A2RaceModeCoreChipIDs, A3RaceModeCoreChipIDs, A4RaceModeCoreChipIDs, SeedHashAdj, SeedHashNoun, Accessories, WeaponChips, AuxCores, CoreCrystals, ValidTboxMapNames
import time
import JSONParser
import DebugLog

AllMapIDs = [["Gormott", "ma05a"], ["Uraya", "ma07a"], ["Mor Ardain","ma08a"], ["Leftherian Archipelago", "ma15a"], ["Indoline Praetorium", "ma11a"], ["Tantal", "ma13a"], ["Spirit Crucible Elpys", "ma16a"], ["Cliffs of Morytha", "ma17a"], ["World Tree", "ma20a"], ["Final Stretch", "ma21a"]] #that we care about lol

# Default Level-Based Modifiers for EXP, Damage Taken/Given, Accuracy, and Odds of getting a reaction (on an enemy?) (break/topple/launch/smash)
ExpRevHigh = [105, 110, 117, 124, 134, 145, 157, 170, 184, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
ExpRevLow = [95, 86, 77, 69, 62, 56, 50, 45, 41, 37, 33, 30, 27, 24, 22, 20, 18, 16, 14, 13]
ExpRevLow2 = [100, 95, 88, 81, 75, 69, 64, 56, 49, 43, 38, 33, 29, 25, 22, 20, 18, 16, 14, 13]
DamageRevHigh = [100, 100, 100, 105, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
DamageRevLow = [100, 100, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66]
HitRevLow = [110, 115, 122, 129, 138, 147, 158, 169, 182, 195, 210, 225, 242, 259, 278, 297, 318, 339, 362, 385]
ReactRevHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 100, 100, 100, 100, 100, 100]

def RaceModeChanging(OptionsRunDict): 
    print("Setting Up Race Mode")    
    #EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
    #EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
    
    AreaList1 = [68] #41,
    AreaList2 = [99,152] #99,
    AreaList3 = [125,133,168] #, 125, 133,
    AreaList4 = [175] #187

    AreaList = [41, 68, 99, 152, 125, 133, 168, 175, 187]

    MSGIDList = [63, 141, 205, 367, 299, 314, 396, 413, 445] #list of MSGIDs for each of the landmarks in Area List (276 for Temperantia) (427 for Land of Morytha) 

    RaceModeDungeons = []
    RaceModeDungeons.append(random.choice(AreaList1))
    RaceModeDungeons.append(random.choice(AreaList2))
    RaceModeDungeons.append(random.choice(AreaList3))
    RaceModeDungeons.append(random.choice(AreaList4))
    RaceModeDungeons.append(200)

    # common/FLD_QuestList
    # [Gormott, Uraya, Mor Ardain, Leftherian Archipelago, Temperantia + Indoline Praetorium, Tantal, Spirit Crucible Elpys, Cliffs of Morytha + Land of Morytha, World Tree, Final Stretch]

    ContinentWarpCutscenes = [10034, 10088, 10156, 10197, 10213, 10270, 10325, 10350, 10392, 10476] # We want to call these after the boss fight cutscenes
    FinalContinentCutscenes = [10079, 10130, 10189, 10212, 10266, 10304, 10345, 10392, 10451, 30000]
    ScenarioFlagLists = [2001, 3005, 4025, 5005, 5021, 6028, 7018, 7043, 8024, 10026]
    NextQuestAList = [27, 56, 100, 128, 136, 163, 184, 195, 212, 238]
    LastQuestAList = [50, 81, 125, 135, 161, 177, 191, 211, 227, 270]
    LevelAtStartofArea = [5, 20, 29, 35, 38, 42, 46, 51, 59, 68] #Level going to: # Level(ish) of the first boss of the current area (so you want to be around this level after warping)
    LevelAtEndofArea = [15, 26, 34, 35, 42, 46, 46, 59, 68, 70]  #Level going from: # Level the last boss of the previous area was (so you should be around the same level before warping to new area)

    # The Save File is set up in a way that it has 56 bonus exp already, and is at level 2, so that value (totals to 76 xp gained) gets subtracted from the total xp needed
    # XP needed to reach a given level, formatted in [Given Level, Total XP Needed]
    # Tora ends up like 35 xp off level 20 with the actual xp needed to reach lv 5 at 360, so I give some more exp to compensate. It doesn't push anyone else over.
    XPNeededToReachLv = [[5, 325], [15, 9060], [20, 21360], [26, 44520], [29, 59820], [34, 91320], [35, 98580], [38, 122520], [42, 160080], [46, 205140], [51, 274640], [59, 428120], [68, 682040], [70, 789920]]

    ChosenIndices = []

    RaceModeMapJumpIDs = [41, 68, 99, 152, 125, 133, 168, 175, 187, 200]

    for i in range(0, len(RaceModeDungeons)): # Defines the chosen indices that we're using from the list of race-mode locations
        for j in range(0, len(RaceModeMapJumpIDs)):
            if RaceModeDungeons[i] == RaceModeMapJumpIDs[j]:
                ChosenIndices.append(j)

    ExpBefore = [0] * 5
    ExpAfter = [0] * 5
    ExpDiff = [0] * 5

    for i in range(0, len(ChosenIndices)): # Defines the EXP difference we need to give to the first landmark in a race-mode location    
        for j in range(0, len(XPNeededToReachLv)):
            if i == 0:
                ExpBefore[i] = 76
                if LevelAtStartofArea[ChosenIndices[i]] == XPNeededToReachLv[j][0]:    
                    ExpAfter[i] = XPNeededToReachLv[j][1]
                    break
            if i < 4:
                if LevelAtEndofArea[ChosenIndices[i-1]] == XPNeededToReachLv[j][0]:
                    ExpBefore[i] = XPNeededToReachLv[j][1]
                if LevelAtStartofArea[ChosenIndices[i]] == XPNeededToReachLv[j][0]:
                    ExpAfter[i] = XPNeededToReachLv[j][1]
            if i == 4:
                ExpAfter[i] = 682040
                if LevelAtEndofArea[ChosenIndices[i-1]] == XPNeededToReachLv[j][0]:
                    ExpBefore[i] = XPNeededToReachLv[j][1]
                    break
                
        ExpDiff[i] = ExpAfter[i] - ExpBefore[i]
        if ExpDiff[i] > 65535:
            ExpDiff[i] = 65535

    MapSpecificIDs = [501, 701, 832, 1501, 1101, 1301, 1601, 1701, 2001, 2103]
    FileStart = "./_internal/JsonOutputs/common_gmk/"
    FileEnd = "_FLD_LandmarkPop.json"
    LandmarkFilestoTarget = [] 
    LandmarkMapSpecificIDstoTarget = []
    
    for i in range(0, len(ChosenIndices)): # Defines what files we want to target and what map ids in that file we want to target  
        LandmarkFilestoTarget.append(FileStart + AllMapIDs[ChosenIndices[i]][1] + FileEnd)
        LandmarkMapSpecificIDstoTarget.append(MapSpecificIDs[ChosenIndices[i]])
    
    if ChosenIndices[0] == 0: # Because Gormott warp is broken currently, we 
        LandmarkFilestoTarget[0] = "./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json"
        LandmarkMapSpecificIDstoTarget[0] = 210

    for i in range(0, len(LandmarkFilestoTarget)):  # Adjusts the EXP gained from the first landmark in each race-mode location
        with open(LandmarkFilestoTarget[i], 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == LandmarkMapSpecificIDstoTarget[i]:
                    row["getEXP"] = ExpDiff[i]
                    row["getSP"] = 4500 * ChosenIndices[i]
                    if row["$id"] == 210: # because the Gormott warp is currently broken, we need a skip travel point there in case the player dies before getting a landmark.
                        row["category"] = 0
                        row["MAPJUMPID"] = 41
                        row["menuPriority"] = 1
                        row["MSGID"] = 63
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    
    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
        data = json.load(file)
        for row in data["rows"]:
            if (row["PRTQuestID"] != 0) and (row["$id"] >= 25):
                row["PRTQuestID"] = 6
            if row["$id"] == 15: # Talking to Spraine
                row["NextQuestA"] = NextQuestAList[ChosenIndices[0]]
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == LastQuestAList[ChosenIndices[i]]:
                    row["NextQuestA"] = NextQuestAList[ChosenIndices[i+1]]
                    break
        for row in data["rows"]: # because cliffs and land are together, the chapter cutscene sets the current quest cleared id to something that is not 6, causing issues with the way I did things.
            if row["$id"] == 200:
                row["NextQuestA"] = 202
            if row["$id"] == 261: # same thing for indol and temperantia
                row["NextQuestA"] = 150
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10013:
                if ChosenIndices[0] == 0:
                    # Gormott
                    row["nextID"] = 10035
                    row["scenarioFlag"] = 2002
                    row["nextIDtheater"] = 10035
                if ChosenIndices[0] == 1:
                    # Uraya
                    row["nextID"] = 10088
                    row["scenarioFlag"] = 3005
                    row["nextIDtheater"] = 10088
            if row["$id"] == 10189:
                row["linkID"] = 0
                row["envSeam"] = 0
            if row["$id"] == 10094: # script that causes Vandham to join is name chapt03 startid 5
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10096: #
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10107: # script for the second time Vandham joins
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10211: # script that removes morag
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10213: # script that readds morag
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10239: # need to hard code the chapter transition for indol and temperantia section because I break some stuff to make warping between continents work.
                row["scenarioFlag"] = 6001
                row["nextID"] = 10244
                row["nextIDtheater"] = 10244
            if row["$id"] == 10304:
                row["linkID"] = 0
            if row["$id"] == 10366: # need to hard code the leap between cliffs and land of morytha because I break some stuff to make warping between continents work.
                row["scenarioFlag"] = 8001
                row["nextID"] = 10369
                row["nextIDtheater"] = 10369
            if row["$id"] == 10369: # script that removes all party members except rex
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] == 10369: # script that adds Jin to the party (there would be 6 chars, breaking the menus, also possibly causing SP dupe bug)
                row["scriptName"] = ""
                row["scriptStartId"] = 0
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == FinalContinentCutscenes[ChosenIndices[i]]:
                    row["nextID"] = ContinentWarpCutscenes[ChosenIndices[i+1]]
                    row["nextIDtheater"] = ContinentWarpCutscenes[ChosenIndices[i+1]]
                    row["scenarioFlag"] = ScenarioFlagLists[ChosenIndices[i+1]]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    NGPlusBladeCrystalIDs = DetermineNGPlusBladeCrystalIDs(OptionsRunDict)
    DifficultyChanges()
    DriverLvandSPFix()
    print(OptionsRunDict["Race Mode"]["subOptionObjects"]["Custom Loot"]["subOptionTypeVal"].get())
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Custom Loot"]["subOptionTypeVal"].get():
        print("Filling Chests with Custom Loot")
        RaceModeLootChanges(ChosenIndices, NGPlusBladeCrystalIDs, OptionsRunDict)
        StackableCoreCrystalsandKeyItems()
        #RenameCoreCrystals(OptionsRunDict)
        FindtheBladeNames(OptionsRunDict)
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Less Grinding"]["subOptionTypeVal"].get():
        print("Reducing amount of grinding")
        LessGrinding()
        ChangeBladeLevelUnlockReqs(ChosenIndices, NGPlusBladeCrystalIDs)
        ReduceBladeReqTrustVals()
        SecondSkillTreeCostReduc()
        DriverArtUpgradeCostChange()
        BladeTreeMaxRewardChange()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Shop Changes"]["subOptionTypeVal"].get():    
        print("Changing Shops")
        ShyniniSaveUs()
        ShopRemovals()
        MovespeedDeedChanges()
        PouchItemCarryCapacityIncrease()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Enemy Drop Changes"]["subOptionTypeVal"].get():
        print("Removing enemy drops")
        EnemyDropRemoval()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["DLC Item Removal"]["subOptionTypeVal"].get():
        print("Nerfing Corvin and Crossette")
        DLCItemChanges()

def LessGrinding(): #adjusting level based exp gains, and debuffs while underleveled to make it less grindy
    with open("./_internal/JsonOutputs/common/BTL_Lv_Rev.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            row["ExpRevHigh"] = 210 + 20 * row["$id"]
            row["ExpRevLow"] = 100
            if row["$id"] >= 10:
                row["DamageRevHigh"] = 250
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DetermineNGPlusBladeCrystalIDs(OptionsRunDict):
    NGPlusBladeIDs = [1043, 1044, 1045, 1046, 1047, 1048, 1049]
    NGPlusBladeCrystalIDs = []
    if OptionsRunDict["Core Crystal Changes"]["optionTypeVal"].get():
        with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for i in range(0, len(NGPlusBladeIDs)):
                for row in data["rows"]:
                    if row["BladeID"] == NGPlusBladeIDs[i]:
                        NGPlusBladeCrystalIDs.append(row["$id"])
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        return NGPlusBladeCrystalIDs

def ChangeBladeLevelUnlockReqs(ChosenIndices, NGPlusBladeCrystalIDs): # changes the blade unlock requirements to the same condition as the final quest in a race-mode continent
    KeyAchievementIDs = [15, 25, 0, 35, 45, 55, 65, 75, 85, 95, 105, 0, 0, 115, 125, 135, 145, 375, 385, 155, 185, 165, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 195, 355, 365, 395, 0, 415, 425, 465, 455, 445, 435, 405, 175, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 95, 405, 455, 455, 445, 435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 365, 85, 1668, 1678, 1648, 1658, 1739, 1749, 0, 1759, 1739, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 325, 325, 325, 1679, 1689, 1699, 1709, 1719, 1729]
    KeyAchievementIDs = list(set([x for x in KeyAchievementIDs if x != 0]))
    RelevantChosenIndices = [x for x in ChosenIndices if x != 9]
    RelevantLocation = [501, 701, 832, 1501, 1101, 1301, 1601, 1701, 2001]
    MapIDs = [6, 9, 10, 14, 12, 13, 15, 16, 20]
    TaskIDs = [143, 309, 147, 285]
    TaskLogIDs = [659, 660, 661, 662]
    LocationNames = ["Gormott", "Uraya", "Mor Ardain", "Leftheria", "Indol", "Tantal", "Spirit Crucible Elpys", "the Cliffs of Morytha", "the World Tree"]

    StarterBladeTrustSetAppearance = [16, 11, 12, 13, 14]
    A1TrustSetAppearance = [16, 16, 12, 13, 14]
    A2TrustSetAppearance = [16, 16, 16, 13, 14]
    A3TrustSetAppearance = [16, 16, 16, 16, 14]
    A4TrustSetAppearance = [16, 16, 16, 16, 16]

    AllTrustSetAppearances = [StarterBladeTrustSetAppearance, A1TrustSetAppearance, A2TrustSetAppearance, A3TrustSetAppearance, A4TrustSetAppearance]

    StarterBladeIDs = [1001, 1002, 1004, 1005, 1009, 1010]
    A1BladeIDs = []
    A2BladeIDs = [1006]
    A3BladeIDs = [1011]
    A4BladeIDs = [1043, 1044, 1045, 1046, 1047, 1048, 1049]

    ValidCrystalListIDs = set(Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45010) + [45016] + Helper.InclRange(45017,45048) + [45056, 45057])
    ValidCrystalListIDs -= set(NGPlusBladeCrystalIDs)
    ValidCrystalListIDs = list(ValidCrystalListIDs)
    CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/ITM_CrystalList.json",["$id"], ValidCrystalListIDs, "BladeID")
    
    for i in range(0, len(ValidCrystalListIDs)):
        if i <= 11:
            A1BladeIDs.append(CorrespondingBladeIDs[i])
        if (i > 11) & (i <= 23):
            A2BladeIDs.append(CorrespondingBladeIDs[i])
        if (i > 22):
            A3BladeIDs.append(CorrespondingBladeIDs[i])

    AllBladeIDs = [StarterBladeIDs, A1BladeIDs, A2BladeIDs, A3BladeIDs, A4BladeIDs]

    ArtandSkillCols = ["ArtsAchievement1", "ArtsAchievement2", "ArtsAchievement3", "SkillAchievement1", "SkillAchievement2", "SkillAchievement3"]
    TrustCol = "KeyAchievement"

    ArtandSkillIDs = [[0], [0], [0], [0], [0]]
    TrustIDs = [[0], [0], [0], [0], [0]]

    for g in range(0, 5): # need to find the area each id belongs to
        for i in range(0, len(ArtandSkillCols)):
            ArtandSkillIDs[g] = ArtandSkillIDs[g] + Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], AllBladeIDs[g], ArtandSkillCols[i])
            ArtandSkillIDs[g] = list(set(ArtandSkillIDs[g])- set([0]))
        TrustIDs[g] = TrustIDs[g] + Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], AllBladeIDs[g], TrustCol)
        TrustIDs[g] = list(set(TrustIDs[g]) - set([0]))

    with open("./_internal/JsonOutputs/common/FLD_AchievementSet.json", 'r+', encoding='utf-8') as file: # now we need to modify corresponding set ids
        data = json.load(file)
        for i in range(0, len(ArtandSkillIDs)):
            for row in data["rows"]:
                if row["$id"] in ArtandSkillIDs[i]:
                    for j in range(1, 6):
                        if (row[f"AchievementID{j}"] != 0):
                            row[f"AchievementID{j}"] = 16
                if row["$id"] in TrustIDs[i]: 
                    for j in range(1,6):
                        row[f"AchievementID{j}"] = AllTrustSetAppearances[i][j-1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #we need to change FLD_Achievement ID 1 to walk 1 step total
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                    row["StatsID"] = 60
                    row["Count"] = 1
                    row["DebugName"] = "WALK_TOTAL"
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_QuestTaskAchievement.json", 'r+', encoding='utf-8') as file: #now we need to modify the FLD_QuestTaskAchievement
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] <= 7004:
                    row["TaskType1"] = 5
                    row["TaskID1"] = TaskIDs[row["$id"]-7001]
                    row["TaskCondition1"] = 0
                if row["$id"] == 7005:
                    row["TaskType1"] = 12
                    row["TaskID1"] = 1
                    row["TaskCondition1"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_QuestReach.json", 'r+', encoding='utf-8') as file:  #modifying the tasks where you need to reach a certain location
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] == TaskIDs[i]:
                    row["Category"] = 2
                    row["MapID"] = MapIDs[RelevantChosenIndices[i]]
                    row["PlaceID"] = RelevantLocation[RelevantChosenIndices[i]]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common_ms/fld_quest_achievement.json", 'r+', encoding='utf-8') as file: #modifying the text files that describe what you need to do to unlock the node
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] == TaskLogIDs[i]:
                    row["name"] = f"Reach {LocationNames[RelevantChosenIndices[i]]}"
                    break
            for row in data["rows"]:
                if row["$id"] == 663:
                    row["name"] = "Unlocked once you unlock the \n corresponding Trust Level."
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RaceModeLootChanges(ChosenIndices, NGPlusBladeCrystalIDs, OptionsRunDict):
    NonNGPlusCoreCrystalIDs = set(Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45010) + [45016] + Helper.InclRange(45017,45048) + [45056, 45057])
    NonNGPlusCoreCrystalIDs -= set(NGPlusBladeCrystalIDs)
    NonNGPlusCoreCrystalIDs = list(NonNGPlusCoreCrystalIDs)
    A1CoreCrystalIDs = (NonNGPlusCoreCrystalIDs[:12]) * 2
    del NonNGPlusCoreCrystalIDs[:12]
    A2CoreCrystalIDs = (NonNGPlusCoreCrystalIDs[:12]) * 2
    del NonNGPlusCoreCrystalIDs[:12]
    A3CoreCrystalIDs = (NonNGPlusCoreCrystalIDs) * 2
    A4CoreCrystalIDs = NGPlusBladeCrystalIDs * 2
    A1Equip = []
    A2Equip = []
    A3Equip = []
    A4Equip = []
    for i in range(0, len(AllRaceModeItemTypeIDs)):
        A1Num = random.randint(1,3) - 1
        A2Num = random.randint(4,6) - 1
        A3Num = random.randint(7,9) - 1
        A4Num = random.randint(10,12) - 1
        A1Equip.append(AllRaceModeItemTypeIDs[i][A1Num]) 
        A2Equip.append(AllRaceModeItemTypeIDs[i][A2Num])
        A3Equip.append(AllRaceModeItemTypeIDs[i][A3Num])
        A4Equip.append(AllRaceModeItemTypeIDs[i][A4Num])
    for i in range(0, len(RaceModeAuxCoreIDs)):
        A1Num = random.randint(1,3) - 1
        A2Num = random.randint(4,6) - 1
        A3Num = random.randint(7,9) - 1
        A4Num = random.randint(10,12) - 1
        A1Equip.append(RaceModeAuxCoreIDs[i][A1Num]) 
        A2Equip.append(RaceModeAuxCoreIDs[i][A2Num])
        A3Equip.append(RaceModeAuxCoreIDs[i][A3Num])
        A4Equip.append(RaceModeAuxCoreIDs[i][A4Num])
    Area1LootIDs = A1CoreCrystalIDs + [25305] * 3 + Helper.InclRange(25249, 25264) * 2 + [25450] * 3 + A1Equip * 2 + [25408] * 5 + [25218, 25218, 25218, 25219, 25219, 25219] + A1RaceModeCoreChipIDs * 2 + [25407] * 10
    Area2LootIDs = A2CoreCrystalIDs + [25305] * 3 + Helper.InclRange(25265, 25280) * 2 + [25450] * 3 + A2Equip * 2 + [25408] * 5 + [25220, 25220, 25220] + A2RaceModeCoreChipIDs * 2 + [25407] * 10
    Area3LootIDs = A3CoreCrystalIDs + [25305] * 3 + Helper.InclRange(25281, 25291) * 2 + [25450] * 3 + A3Equip * 2 + [25408] * 5 + [25221, 25221, 25221] + A3RaceModeCoreChipIDs * 2 + [25407] * 10
    Area4LootIDs = A4CoreCrystalIDs + [25305] * 3 + Helper.InclRange(25292, 25300) * 2 + [25450] * 3 + A4Equip * 2 + [25408] * 5 + [25222, 25222, 25222] + A4RaceModeCoreChipIDs * 2 + [25407] * 10
    random.shuffle(Area1LootIDs)
    random.shuffle(Area2LootIDs)
    random.shuffle(Area3LootIDs)
    random.shuffle(Area4LootIDs)
    AllAreaLootIDs = [Area1LootIDs, Area2LootIDs, Area3LootIDs, Area4LootIDs]
    TBoxFiles = [[0,0], [0,0], [0,0], [0,0]] # this needs to be changed to a for loop if i change the number of race mode dungeons (append [0,0])
    FileStart = "./_internal/JsonOutputs/common_gmk/"
    FileEnd = "_FLD_TboxPop.json"
    StartingPreciousIDs = Helper.InclRange(25001, 25499)
    ExcludePreciousIDs = Helper.InclRange(25218, 25222) + [25305] + [25408] + [25450] + [25405] + [25406] + [25407] + Helper.InclRange(25249, 25300) # We are ok with replacing these, since they're in the pool of items to pull from anyways
    FinalPreciousIDs = [x for x in StartingPreciousIDs if x not in ExcludePreciousIDs] # We do not want to replace these, these are quest/key items
    for i in range(0, len(ChosenIndices) - 1): # Defines what files we want to target and what map ids in that file we want to target  
        if (ChosenIndices[i] != 4) & (ChosenIndices[i] != 7):
            TBoxFiles[i][0] = FileStart + AllMapIDs[ChosenIndices[i]][1] + FileEnd
    BoxestoRandomizePerMap = [0] * (len(ChosenIndices) - 1)
    TBoxName = ""
    for i in range(0, len(ChosenIndices)):
        if ChosenIndices[i] == 4:
            TBoxFiles[i][0] = "./_internal/JsonOutputs/common_gmk/ma10a_FLD_TboxPop.json"
            TBoxFiles[i][1] = "./_internal/JsonOutputs/common_gmk/ma11a_FLD_TboxPop.json"
        if ChosenIndices[i] == 7:
            TBoxFiles[i][0] = "./_internal/JsonOutputs/common_gmk/ma17a_FLD_TboxPop.json"
            TBoxFiles[i][1] = "./_internal/JsonOutputs/common_gmk/ma18a_FLD_TboxPop.json"
    ListTboxFiles = []
    for i in range(0, 4):
        for j in range(0, 2):
            if TBoxFiles[i][j] != 0:
                ListTboxFiles.append(TBoxFiles[i][j])
    AllOtherMapIDs = [x for x in ValidTboxMapNames if x not in ListTboxFiles]
    for i in range(0, len(AllOtherMapIDs)):
        EnemyRandoLogic.ColumnAdjust(AllOtherMapIDs[i], ["Condition","itm1Num", "itm2Num", "itm3Num", "itm4Num", "itm5Num", "itm6Num", "itm7Num", "itm8Num", "itm1ID", "itm2ID", "itm3ID", "itm4ID", "itm5ID", "itm6ID", "itm7ID", "itm8ID"], 0)
    for i in range(0, len(TBoxFiles)):
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        TBoxName = row["name"]
                        if (TBoxName != "tbox_ma08a_f018") & (TBoxName != "tbox_qst1018_001"): # We want to not randomize a broken one inside collision on Mor Ardain, and one in uraya that has a debug item
                            BoxestoRandomizePerMap[i] = BoxestoRandomizePerMap[i] + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)
    ItemsPerBox = []
    for i in range(0, len(AllAreaLootIDs)):
        ItemsPerBox.append(len(AllAreaLootIDs[i])//BoxestoRandomizePerMap[i])
        if ItemsPerBox[i] > 7:
            ItemsPerBox[i] = 7
    k = 0
    for i in range(0, len(TBoxFiles)):
        k = 0
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]: # We want to double the gold per chest to compensate that we're not getting enemy drops
                        row["goldMin"] = 2 * row["goldMin"]
                        row["goldMax"] = 2 * row["goldMax"]
                    for row in data["rows"]:
                        if k > len(AllAreaLootIDs[i]): #If k ever exceeds the size of the loot ids we're shuffling, then we can stop going through the files
                            file.seek(0)
                            file.truncate()
                            json.dump(data, file, indent=2, ensure_ascii=False)
                            break
                        TBoxName = row["name"]
                        if (TBoxName != "tbox_ma08a_f018") & (TBoxName != "tbox_qst1018_001"): # We want to not randomize a box on Mor Ardain stuck in collision
                            for j in range(0, 8):
                                if row[f"itm{j+1}ID"] not in FinalPreciousIDs:
                                    row[f"itm{j+1}ID"] = 0
                                    row[f"itm{j+1}Num"] = 0
                                    row[f"itm{j+1}Per"] = 0 # don't know if this is used at all, but better safe than sorry
                            for h in range(0, ItemsPerBox[i]):
                                if row[f"itm{h+1}ID"] not in FinalPreciousIDs:
                                    row[f"itm{h+1}ID"] = AllAreaLootIDs[i][k]
                                    row[f"itm{h+1}Num"] = 1
                                    k = k + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Xohar Fragment Hunt"]["subOptionTypeVal"].get(): 
        print("Shuffling in Xohar Fragments")
        XoharFragmentHunt(TBoxFiles, BoxestoRandomizePerMap, ChosenIndices)
        
def ShyniniSaveUs(): # Just in case we don't get good blade field skills, we can rely on Shynini to always sell core crystals :D
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 6:
                row["DefItem7"] = 45011
                row["DefItem8"] = 45012
                row["DefItem9"] = 45013
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ShopRemovals(): # Removes the Expensive Core Crystal from the shop, as well as the shop deeds
    ShopDeedIDs = Helper.InclRange(25249, 25300)
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["PrivilegeItem"] in ShopDeedIDs:
                row["PrivilegeItem"] = 0
            if row["$id"] == 33:
                row["Addtem2"] = 0
                row["AddCondition2"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def MovespeedDeedChanges(): #Replaces all other deed effects with movespeed, makes the max movespeed bonus 250% instead of 25%
    DeedTypeIDValues = Helper.InclRange(1, 52)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["Type"] in DeedTypeIDValues:
                row["Caption"] = 603 # Increases running speed by 5%
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in DeedTypeIDValues:
                row["Value"] = 5
                row["Type"] = 1
            if row["$id"] > 52:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 250%
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Max"] = 150
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes name of deed
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] >= 25249) & (row["$id"] <= 25300):
                row["Caption"] = 603
            if row["$id"] > 25300:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] >= 491) & (row["$id"] <= 542):
                row["name"] = "Movespeed Deed"
            if row["$id"] > 542:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DLCItemChanges(): # Changes all DLC gifts to 1 gold except for poppy crystals
    DLCIDRowsWithItems = Helper.InclRange(1,7) + [9, 10] + Helper.InclRange(16, 21) + [23,24] + [30] + [36, 37] + Helper.InclRange(43, 55)
    with open("./_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in DLCIDRowsWithItems:
                row["item_id"] = 0
                row["category"] = 2
                row["value"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DifficultyChanges(): # Makes Easy difficulty the same as Normal
    with open("./_internal/JsonOutputs/common/BTL_DifSetting.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            row["Easy"] = row["Normal"]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SeedHash():
    seedhashcomplete = random.choice(SeedHashAdj) + " " + random.choice(SeedHashNoun) 
    with open("./_internal/JsonOutputs/common_ms/menu_ms.json", 'r+', encoding='utf-8') as file: #puts the seed hash text on the main menu and on the save game screen
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 128:
                row["name"] = f"Seed Hash: {seedhashcomplete}"
                row["style"] = 166
            if row["$id"] == 129:
                row["name"] = "Race Mode Start"
            if row["$id"] == 1644:
                row["name"] = f"{seedhashcomplete}"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    DebugLog.AppendSeedHash()
    
def ReduceBladeReqTrustVals(): # Sets required Trust Values to 0.5x the vanilla values
    with open("./_internal/JsonOutputs/common/FLD_ConditionIdea.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row["TrustPoint"] = int(0.5 * row["TrustPoint"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SecondSkillTreeCostReduc(): # Reduces the cost of the hidden driver skill tree by 80% for race mode
    FilePaths = ["./_internal/JsonOutputs/common/BTL_Skill_Dr_Table01.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table02.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table03.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table04.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table05.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table06.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"]
    for i in range(0, len(FilePaths)):
        with open(FilePaths[i], 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] > 15:
                    row["NeedSp"] = int(row["NeedSp"] / 5)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def EnemyDropRemoval(): # Removes all enemy drops, to avoid getting powerful equipment out of logic.
    for i in range(1, 9):
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BTL_EnDropItem.json", [f"ItemID{i}", f"DropProb{i}", f"NoGetByEnh{i}", f"FirstNamed{i}"] , 0)

def XoharFragmentHunt(TBoxFiles, BoxestoRandomizePerMap, ChosenIndices): # Experimental Mode to make players go out and find chests.
    XoharFragPreciousIDs = [25135, 25136, 25137, 25138] # for now fixed at 4, but if we change # of race mode dungeons or give the player that option, will need to change this
    FragmentNameIDs = [191, 192, 193, 194]
    CaptionIDs = [197, 199, 201, 206]
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # makes them stackable
        data = json.load(file)
        for i in range(0, len(XoharFragPreciousIDs)):
            for row in data["rows"]:
                if row["$id"] == XoharFragPreciousIDs[i]:
                    row["ValueMax"] = 99
                    row["ClearNewGame"] = 0
                    row["Name"] = FragmentNameIDs[i]
                    row["Caption"] = CaptionIDs[i]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    NameTexts = ["Xohar Fragment A", "Xohar Fragment B", "Xohar Fragment C", "Xohar Fragment D"]
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # renaming the fragments in menus
        data = json.load(file)
        for i in range(0, len(XoharFragPreciousIDs)):
            for row in data["rows"]:
                if row["$id"] == FragmentNameIDs[i]:
                    row["name"] = NameTexts[i]
                    break
        for i in range(0, len(XoharFragPreciousIDs)):
            for row in data["rows"]:
                if row["$id"] == CaptionIDs[i]:
                    row["name"] = "3 of these are needed to\nprogress to the next area."
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    QuestCollectIDs = [27, 50, 68, 69]
    with open("./_internal/JsonOutputs/common/FLD_QuestCollect.json", 'r+', encoding='utf-8') as file: # Making Quest Collect Entries for each of them
        data = json.load(file)
        for i in range(0, len(QuestCollectIDs)):
            for row in data["rows"]:
                if row["$id"] == QuestCollectIDs[i]:
                    row["Refer"] = 4
                    row["Count"] = 3
                    row["Deduct"] = 0
                    row["ItemID"] = 25135 + i
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)   
    LastQuestPurposeIDs = [48, 78, 121, 130, 155, 171, 184, 203, 218]
    IDNumbers = Helper.InclRange(278, 281)
    with open("./_internal/JsonOutputs/common/FLD_QuestTask.json", 'r+', encoding='utf-8') as file: # Adding the Quest Requirement to the final quest of the area
        data = json.load(file)
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == LastQuestPurposeIDs[ChosenIndices[i]]:
                    row["TaskType2"] = 3
                    row["TaskID2"] = QuestCollectIDs[i]
                    row["TaskLog2"] = IDNumbers[i]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_quest.json", "r+", encoding='utf-8') as file: # the quest objective now says the name of the custom part
        AreaLetters = ["A", "B", "C", "D"]
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 62, "name": f"Find 3 Xohar Fragment {AreaLetters[i]}."})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    BlankstoShuffle = [0] * (len(ChosenIndices) - 1)
    PartstoShuffle = [0] * (len(ChosenIndices) - 1)
    for i in range(0, len(PartstoShuffle)):
        PartstoShuffle[i] = int(BoxestoRandomizePerMap[i] // 3) # 1/3rd of all chests have a Xohar Fragment
        if PartstoShuffle[i] < 5:
            PartstoShuffle[i] = 5
        BlankstoShuffle[i] = BoxestoRandomizePerMap[i] - PartstoShuffle[i]
    Area1XoharLocations = [0] * BlankstoShuffle[0] + [25135] * PartstoShuffle[0]
    random.shuffle(Area1XoharLocations)
    Area2XoharLocations = [0] * BlankstoShuffle[1] + [25136] * PartstoShuffle[1]
    random.shuffle(Area2XoharLocations)
    Area3XoharLocations = [0] * BlankstoShuffle[2] + [25137] * PartstoShuffle[2]
    random.shuffle(Area3XoharLocations)
    Area4XoharLocations = [0] * BlankstoShuffle[3] + [25138] * PartstoShuffle[3]
    random.shuffle(Area4XoharLocations)
    AllXoharLocations = [Area1XoharLocations, Area2XoharLocations, Area3XoharLocations, Area4XoharLocations]
    ACurBox = 0
    for i in range(0, len(TBoxFiles)): # Shuffling the xohar fragments into the treasure chests
        ACurBox = 0
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        TBoxName = row["name"]
                        if (TBoxName != "tbox_ma08a_f018") & (TBoxName != "tbox_qst1018_001"):
                            if AllXoharLocations[i][ACurBox] != 0:
                                row["itm8ID"] = AllXoharLocations[i][ACurBox]
                                row["itm8Num"] = 1
                                #print(row["name"])
                            ACurBox = ACurBox + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)

def DriverLvandSPFix():
    with open("./_internal/JsonOutputs/common/CHR_Dr.json", 'r+', encoding='utf-8') as file: # Maybe fixing XP dupe
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] <= 6:
                row["DefLv"] = 1
                row["DefLvType"] = 1
                row["DefWPType"] = 1
                row["DefWP"] = 0
                row["DefSPType"] = 0
                row["DefSP"] = 0
                row["DefAcce"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def StackableCoreCrystalsandKeyItems(): # Allows us to shuffle more than 1 copy of a key item or core crystal into the pool
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in Helper.InclRange(25218, 25222):
                row["ValueMax"] = 3
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FindtheBladeNames(OptionsRunDict):
    if OptionsRunDict["Core Crystal Changes"]["optionTypeVal"].get():
        ValidCrystalListIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45010) + [45016] + Helper.InclRange(45017,45048) + [45056, 45057]
        CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/ITM_CrystalList.json",["$id"], ValidCrystalListIDs, "BladeID")
        CorrespondingBladeNameIDs = Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], CorrespondingBladeIDs, "Name")
        CorrespondingBladeNames = Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common_ms/chr_bl_ms.json", ["$id"], CorrespondingBladeNameIDs, "name")
        DebugLog.DebugCoreCrystalAddition(ValidCrystalListIDs, CorrespondingBladeNames)
        ITMCrystalAdditions(CorrespondingBladeNames, CorrespondingBladeIDs)

def ITMCrystalAdditions(BladeNames, CorrespondingBladeIDs):
    with open("./_internal/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file:     
        IDNumbers = Helper.InclRange(16, 58)
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": f"{BladeNames[i]}\'s Core Crystal"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(CorrespondingBladeIDs)):
                if row["BladeID"] == CorrespondingBladeIDs[i]:
                    row["Name"] = IDNumbers[i]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PouchItemCarryCapacityIncrease(): # Set the max carry capacity of pouch items to 10 for all items
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/ITM_FavoriteList.json", ["ValueMax"], 10)

def DriverArtUpgradeCostChange(): # to reduce the amount of time spent menuing, a single manual (5000 WP) should be enough to upgrade an art to level 5
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP2", "NeedWP3", "NeedWP4", "NeedWP5"], 1000)

def BladeTreeMaxRewardChange(): # When a blade skill tree completes, rewards that I already add to the item pool get given to the player, so I just replace the rewards with nothing.
    with open("./_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [927, 928, 929, 930]:
                row["ItemID1"] = 0
                row["ItemNumber1"] = 0
                row["ItemID2"] = 0
                row["ItemNumber2"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)