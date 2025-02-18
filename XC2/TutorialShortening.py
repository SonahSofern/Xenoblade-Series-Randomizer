import json
from scripts import Helper
import EnemyRandoLogic, Options

def ShortenedTutorial():
    RaceModeBox = Options.RaceModeOption.GetState()
    if not RaceModeBox:
        print("Shortening Tutorials")
        Helper.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
        with open("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", 'r+', encoding='utf-8') as file: # part of core crystal tutorial
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] not in [65, 67, 70]:
                    row["ScenarioFlagMin"] = 10048
                    row["QuestFlag"] = 0
                    row["QuestFlagMin"] = 0
                    row["QuestFlagMax"] = 0
                    row["SysMultiFlag"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", 'r+', encoding='utf-8') as file: # part of core crystal tutorial
            data = json.load(file)
            for row in data["rows"]:
                if row["tutorial"] != "ma05a_tutorial":
                    row["tutorial"] = ""
                    row["tutorial_bdat"] = ""
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        EnemyRandoLogic.KeyItemsReAdd()
    else:
        print("Shortening Tutorials")
        Helper.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0)
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "")
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: #allows waypoints to work, and us to skip Melolo
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] <= 2005:
                row["ScenarioFlagMin"] = 1003
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: #this makes it so spraine will talk to us no matter how small the flag
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2045:
                row["ScenarioFlagMin"] = 10047
                row["ScenarioFlagMax"] = 10048
            if row["$id"] == 2046:
                row["ScenarioFlagMin"] = 1008
                row["ScenarioFlagMax"] = 1012
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: # shortens opening section
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 7: #if we go to argentum
                row["NextQuestA"] = 9 # then go explore argentum
            if row["$id"] == 10: #if we go to bana's room
                row["NextQuestA"] = 12 # then complete the big prep quest
            if row["$id"] == 13: # if we rest at lemour inn (this seems to make the flags go away that were keeping you from shopping and going further upstairs in argentum)
                row["NextQuestA"] = 15 # then talk to spraine
            if row["$id"] == 15: #talk to spraine
                if not RaceModeBox:
                    row["NextQuestA"] = 17 #sets next quest to be to go to the top of the Maelstrom
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_QuestListNormal.json", 'r+', encoding='utf-8') as file: #shortens tutorials
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] >= 2001) and (row["$id"] <= 2008):
                row["PurposeID"] = 2001
            if row["$id"] == 2709:
                row["PurposeID"] = 2001
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_QuestTaskNormal.json", 'r+', encoding='utf-8') as file: #adjusting tutorial quests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2001:
                row["TaskType1"] = 12
                row["TaskID1"] = 1710
                row["TaskLog1"] = 1066 #it calls these ids from common_ms/fld_quest_normal, so I chose a funny one
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #adjusting tutorial quests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1710:
                row["StatsID"] = 60
                row["Count"] = 1
                row["DebugName"] = "WALK_TOTAL" # these change the quest to only have to walk 1 step (after starting quest, since it needs to update for some reason) to complete this
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/EVT_listFev01.json", 'r+', encoding='utf-8') as file: # removing tutorials in tutorial
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 30005:
                row["chgEdID"] = 30007
            if row["scriptName"][:3] == "tut": # if first 3 letters in script name = "tut"
                row["scriptName"] = ""
                row["scriptStartId"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
        
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Tutorial.json", ["script_file"], "aoc_challenge_tutorial") # Shortens battle tutorials
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Tutorial.json", ["start_id"], 0)
    
    
    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: # removing more tutorials
        data = json.load(file)
        removables = ["tut_sys26", "tut_sys22", "tut_sys14", "tut_sys02", "tut_btl23"]
        for row in data["rows"]:
            if row["scriptName"] in removables:
                row["scriptName"] = ""
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)