import Helper
import json
import EnemyRandoLogic
import random

def Beta():
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "") #maybe removes tutorials
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0) #maybe removes tutorials
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma21a_FLD_LandmarkPop.json", ["cndID"], 0) #removes requirement to unlock location

    AreaList = [41, 68, 90, 114, 125, 133, 152, 168, 175, 180, 187] #list of MapJump IDs for the first landmark in each map

    MSGIDList = [63, 141, 205, 276, 299, 314, 367, 396, 413, 427, 445] #list of MSGIDs for each of the landmarks in Area List

    RaceModeDungeons = random.sample(AreaList, 4) #take our race mode dungeons


    RaceModeMSGIDs = [] #take the race mode msg IDs (so you can see what dungeons you have, and where a warp takes you)

    TestingMenuPrios = [1, 2, 3, 4, 5]

    TestingXOffsets = [-154, -200, -155, -90, -153]

    TestingYOffsets = [-207, -100, -63, -100, 72]

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
                row["ScenarioFlagMax"] = 1012
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