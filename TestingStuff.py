import Helper
import json
import EnemyRandoLogic
import random

AreaList = [41, 68, 90, 125, 133, 152, 168, 175, 187] #list of MapJump IDs for the first landmark in each map (114 is Temperantia (combining with Indol for now)), (180 is Land of Morytha (combining with Cliffs of Morytha for now))

MSGIDList = [63, 141, 205, 299, 314, 367, 396, 413, 445] #list of MSGIDs for each of the landmarks in Area List (276 for Temperantia) (427 for Land of Morytha) 

RaceModeDungeons = random.sample(AreaList, 4) #take our race mode dungeons

RaceModeMSGIDs = [] #take the race mode msg IDs (so you can see what dungeons you have, and where a warp takes you)

TestingMenuPrios = [1, 2, 3, 4, 5] # Controls the Map Priority

TestingXOffsets = [-154, -200, -155, -90, -153] # These two control the positions of the markers on Argentum

TestingYOffsets = [-207, -100, -63, -100, 72]

# Default Level-Based Modifiers for EXP, Damage Taken/Given, Accuracy, and Odds of getting a reaction (on an enemy?) (break/topple/launch/smash)
ExpRevHigh = [105, 110, 117, 124, 134, 145, 157, 170, 184, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
ExpRevLow = [95, 86, 77, 69, 62, 56, 50, 45, 41, 37, 33, 30, 27, 24, 22, 20, 18, 16, 14, 13]
ExpRevLow2 = [100, 95, 88, 81, 75, 69, 64, 56, 49, 43, 38, 33, 29, 25, 22, 20, 18, 16, 14, 13]
DamageRevHigh = [100, 100, 100, 105, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
DamageRevLow = [100, 100, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66]
HitRevLow = [110, 115, 122, 129, 138, 147, 158, 169, 182, 195, 210, 225, 242, 259, 278, 297, 318, 339, 362, 385]
ReactRevHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 100, 100, 100, 100, 100, 100]

def Beta():
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "") #maybe removes tutorials
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0) #maybe removes tutorials
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1) #unlocks the world maps
    # EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma21a_FLD_LandmarkPop.json", ["cndID"], 0) #removes requirement to unlock location

    for i in range(0, len(RaceModeDungeons)):
        for j in range(0, len(AreaList)):
            if RaceModeDungeons[i] == AreaList[j]:
                RaceModeMSGIDs.append(MSGIDList[j])

    RaceModeDungeons.append(200)
    RaceModeMSGIDs.append(470)

    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(207,212):
            for row in data["rows"]:
                if row["$id"] == i:
                    row["MAPJUMPID"] = RaceModeDungeons[i - 207]
                    row["category"] = 0
                    row["menuPriority"] = TestingMenuPrios[i - 207]
                    row["MSGID"] = RaceModeMSGIDs[i - 207]
                    row["menu_transX"] = TestingXOffsets[i - 207]
                    row["menu_transY"] = TestingYOffsets[i - 207]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
        pass

    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10:
                row["NextQuestA"] = 15
                row["FlagCLD"] = 645
                row["CallEventA"] = 10481
            if row["$id"] == 15:
                row["NextQuestA"] = 17
                row["FlagCLD"] = 680
                break           
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/FLD_QuestListNormal.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2001:
                row["NextQuestA"] = 2008
                row["FlagCLD"] = 36075
                break   
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_EventPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2008:
                row["ScenarioFlagMin"] = 1008
                row["ScenarioFlagMax"] = 10048
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2045:
                row["ScenarioFlagMin"] = 10047
                row["ScenarioFlagMax"] = 10048
            if row["$id"] == 2046:
                row["ScenarioFlagMin"] = 1008
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/BTL_Lv_Rev.json", 'r+', encoding='utf-8') as file: #adjusting level based exp gains to make it less grindy
        data = json.load(file)
        for row in data["rows"]:
            row["ExpRevHigh"] = 110 + 20 * row["$id"]
            row["ExpRevLow"] = 100
            if row["$id"] >= 10:
                row["DamageRevHigh"] = 200
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 202:
                row["ScenarioMin"] = 1010
                row["NotScenarioMax"] = 10019
                break   
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10480:
                row["nextID"] = 10483
                row["nextIDtheater"] = 10483
            if row["$id"] == 10482:
                #row["stFormID"] = 1035
                #row["edFormID"] = 1035
                #row["nextID"] = 0
                row["scenarioFlag"] = 10026
                #row["linkID"] = 0
                #row["zoneID"] = 3
                #row["zoneX"] = -30.52
                #row["zoneY"] = -8.5
                #row["zoneZ"] = 58.52
                #row["zoneR"] = 90
                #row["nextIDtheater"] = 0
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/EVT_chgBf01.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10474:
                row["id"] = 10027
                row["value1"] = 1
            if row["$id"] == 10475:
                row["id"] = 10027
                row["value1"] = 0
                #row["id"] = 1011 #doesnt matter too much, needs to be between 1010 and 1012 if I think the flag matters        
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

"""     with open("./_internal/JsonOutputs/common_gmk/ma20a_FLD_EventPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 20001:
                row["ScenarioFlagMin"] = 0
                row["ScenarioFlagMax"] = 0
            if row["$id"] == 20002:
                row["ScenarioFlagMin"] = 1001
                row["ScenarioFlagMax"] = 10048
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2) """

"""         with open("./_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] != 0:
                row["ScenarioMin"] = 1004
                row["ScenarioMax"] = 10048
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2) """

"""     with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10461:
                row["scenarioFlag"] = 1004
            if row["$id"] == 10005:
                row["stFormID"] = 1264
                row["edFormID"] = 1264
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2) """