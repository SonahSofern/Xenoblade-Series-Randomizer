import Helper
import json
import EnemyRandoLogic

def Beta():
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "")
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0)
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850)
    with open("./_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] != 0:
                row["ScenarioMin"] = 1004
                row["ScenarioMax"] = 10048
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10461:
                row["scenarioFlag"] = 1004
            if row["$id"] == 10005:
                row["stFormID"] = 1264
                row["edFormID"] = 1264
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma20a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2001:
                row["MAPJUMPID"] = 30
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 202:
                row["MAPJUMPID"] = 187
                row["menuGroup"] = 1
                row["menuMapImage"] = 1
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