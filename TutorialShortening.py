import json
import EnemyRandoLogic

def ShortenedTutorial(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Shorter Tutorial Box":
            ShortTutorialBox = j
        if CheckboxList[j] == "Race Mode Box":
            RaceModeBox = j
    if CheckboxStates[ShortTutorialBox].get() == True:
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "")
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
                    if CheckboxStates[RaceModeBox].get() == False:
                        row["NextQuestA"] = 17 #sets next quest to be to go to the top of the Maelstrom
                        break
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