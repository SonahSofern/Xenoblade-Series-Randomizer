import Helper
import json
import EnemyRandoLogic
import random

def RaceModeChanging(CheckboxList, CheckboxStates): 
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Race Mode Box":
            RaceModeBox = j
            break
    if CheckboxStates[RaceModeBox].get() == True:    
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
        
        AreaList1 = [41] # readd 68
        AreaList2 = [90, 152]
        AreaList3 = [125, 133, 168]
        AreaList4 = [175, 187]

        AreaList = [41, 68, 90, 152, 125, 133, 168, 175, 187]

        MSGIDList = [63, 141, 205, 367, 299, 314, 396, 413, 445] #list of MSGIDs for each of the landmarks in Area List (276 for Temperantia) (427 for Land of Morytha) 

        RaceModeDungeons = []
        RaceModeDungeons.append(random.choice(AreaList1))
        RaceModeDungeons.append(random.choice(AreaList2))
        RaceModeDungeons.append(random.choice(AreaList3))
        RaceModeDungeons.append(random.choice(AreaList4))
        RaceModeDungeons.append(200)

        # Default Level-Based Modifiers for EXP, Damage Taken/Given, Accuracy, and Odds of getting a reaction (on an enemy?) (break/topple/launch/smash)
        ExpRevHigh = [105, 110, 117, 124, 134, 145, 157, 170, 184, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
        ExpRevLow = [95, 86, 77, 69, 62, 56, 50, 45, 41, 37, 33, 30, 27, 24, 22, 20, 18, 16, 14, 13]
        ExpRevLow2 = [100, 95, 88, 81, 75, 69, 64, 56, 49, 43, 38, 33, 29, 25, 22, 20, 18, 16, 14, 13]
        DamageRevHigh = [100, 100, 100, 105, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
        DamageRevLow = [100, 100, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66]
        HitRevLow = [110, 115, 122, 129, 138, 147, 158, 169, 182, 195, 210, 225, 242, 259, 278, 297, 318, 339, 362, 385]
        ReactRevHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 100, 100, 100, 100, 100, 100]

        # Race Mode Stuff

        AllMapIDs = [["Gormott", "ma05a"], ["Uraya", "ma07a"], ["Mor Ardain","ma08a"], ["Leftherian Archipelago", "ma15a"], ["Indoline Praetorium", "ma11a"], ["Tantal", "ma13a"], ["Spirit Crucible Elpys", "ma16a"], ["Cliffs of Morytha", "ma17a"], ["World Tree", "ma20a"], ["Final Stretch", "ma21a"]] #that we care about lol

        # common/FLD_QuestList
        # [Gormott, Uraya, Mor Ardain, Leftherian Archipelago, Temperantia + Indoline Praetorium, Tantal, Spirit Crucible Elpys, Cliffs of Morytha + Land of Morytha, World Tree, Final Stretch]

        ContinentWarpCutscenes = [10034, 10088, 10156, 10197, 10213, 10270, 10325, 10350, 10399, 10476] # We want to call these after the boss fight cutscenes
        ScenarioFlagLists = [2001, 3005]
        NextQuestAList = [26, 56, 100, 128, 136, 163, 183, 194, 214, 238]
        LastQuestAList = [50, 81, 125, 135, 161, 177, 191, 211, 227, 270]
        LevelAtStartofArea = [5, 20, 29, 35, 38, 42, 46, 51, 59, 68] #Level going to: # Level(ish) of the first boss of the current area (so you want to be around this level after warping)
        LevelAtEndofArea = [15, 26, 34, 35, 42, 46, 46, 59, 68, 70]  #Level going from: # Level the last boss of the previous area was (so you should be around the same level before warping to new area)

        # The Save File is set up in a way that it has 56 bonus exp already, and is at level 2, so that value (totals to 76 xp gained) gets subtracted from the total xp needed
        # XP needed to reach a given level, formatted in [Given Level, Total XP Needed] 
        XPNeededToReachLv = [[5, 360], [15, 9060], [20, 21360], [26, 44520], [29, 59820], [34, 91320], [35, 98580], [38, 122520], [42, 160080], [46, 205140], [51, 274640], [59, 428120], [68, 682040], [70, 789920]]

        ChosenIndices = []

        RaceModeMapJumpIDs = [41, 68, 90, 152, 125, 133, 168, 175, 187, 200]

        for i in range(0, len(RaceModeDungeons)): # Defines the chosen indices that we're using from the list of race-mode locations
            for j in range(0, len(RaceModeMapJumpIDs)):
                if RaceModeDungeons[i] == RaceModeMapJumpIDs[j]:
                    ChosenIndices.append(j)

        ExpBefore = [0] * 5
        ExpAfter = [0] * 5
        ExpDiff = [0] * 5

        #exp before[0] should always be 76
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

        MapSpecificIDs = [501, 701, 801, 1501, 1101, 1301, 1601, 1701, 2001, 2103]
        FileStart = "./_internal/JsonOutputs/common_gmk/"
        FileEnd = "_FLD_LandmarkPop.json"
        LandmarkFilestoTarget = [] 
        LandmarkMapSpecificIDstoTarget = []

        for i in range(0, len(ChosenIndices)): # Defines what files we want to target and what map ids in that file we want to target  
            LandmarkFilestoTarget.append(FileStart + AllMapIDs[ChosenIndices[i]][1] + FileEnd)
            LandmarkMapSpecificIDstoTarget.append(MapSpecificIDs[ChosenIndices[i]])
            
        for i in range(0, len(LandmarkFilestoTarget)):  # Adjusts the EXP gained from the first landmark in each race-mode location
            with open(LandmarkFilestoTarget[i], 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    if row["$id"] == LandmarkMapSpecificIDstoTarget[i]:
                        row["getEXP"] = ExpDiff[i]
                        row["getSP"] = 5000 * ChosenIndices[i]
                        break
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)
        
        with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
            data = json.load(file)
            for row in data["rows"]:
                if (row["PRTQuestID"] != 0) and (row["$id"] >= 25):
                    row["PRTQuestID"] = 6
                if row["$id"] == 15: # Talking to Spraine
                    row["NextQuestA"] = NextQuestAList[ChosenIndices[0]]
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

        with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 10013:
                    if ChosenIndices[0] == 0:
                        # Gormott
                        row["nextID"] = 10034
                        row["scenarioFlag"] = 2001
                        row["nextIDtheater"] = 10034
                    if ChosenIndices[0] == 1:
                        # Uraya
                        row["nextID"] = 10088
                        row["scenarioFlag"] = 3005
                        row["nextIDtheater"] = 10088
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

        with open("./_internal/JsonOutputs/common_gmk/ma05a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 5001:
                    row["ScenarioFlagMin"] = 0
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)
