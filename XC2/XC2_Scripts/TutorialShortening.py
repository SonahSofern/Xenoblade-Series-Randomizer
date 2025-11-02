import json, copy, os
from XC2.XC2_Scripts.Unused import EnemyRandoLogic
from scripts import Helper, JSONParser
from XC2.XC2_Scripts import Options, IDs, QOL

def ShortenedTutorial():
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
    CoreCrystalTutorials()
    MeloloWaypoint()
    SpraineTalk()
    Tutorials()
    QOL.BaseGameStorySkip([7,9,10,11,13,15]) #10 # Can just skip some story quests by tying them to an early event
    FieldTutorials()                
    BattleTutorials()
    TornaQuestTutorials(["aoc_tut04", "aoc_tut25", "aoc_tut14", "aoc_tut21", "aoc_tut06", "aoc_tut07", "aoc_tut09", "aoc_tut08"])
    BFTutorials()
    AreaReloadSkip()
    MinimizeTutorialBoxes()

def RaceModeTutorialShortening(): # we need to call this from the race mode function
    SpraineTalk()
    Tutorials()
    FieldTutorials()                
    BattleTutorials()
    BFTutorials()
    MinimizeTutorialBoxes()
    Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "")
    NextQuestSkipper({7:9, 10:12, 13:15})

def UMHuntShortenedTutorial():
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
    CoreCrystalTutorials()
    NextQuestSkipper({7:9, 10:12, 13:15, 15:17})
    MeloloWaypoint()
    SpraineTalk()
    Tutorials()
    FieldTutorials()
    BattleTutorials()
    BFTutorials()
    MinimizeTutorialBoxes()

def NextQuestSkipper(questDict:dict):
    with open("./XC2/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as qstFile: # shortens opening section
        qstData = json.load(qstFile)
        for qst in qstData["rows"]:
            if qst["$id"] in questDict:
                qst["NextQuestA"] = questDict[qst["$id"]]
        JSONParser.CloseFile(qstData, qstFile)

def RemoveBanaCutscene():
    with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: # shortens opening section
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2006:
                row["ScenarioFlagMin"] = row["ScenarioFlagMax"] = 10049
            if row["$id"] == 2008:
                row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def MeloloWaypoint():
    with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: #allows waypoints to work, and us to skip Melolo
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] <= 2005:
                row["ScenarioFlagMin"] = 1003
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PinkArrowFix():
    # the way ben did it breaks the pink arrow and leaves some cutscenes unstarted, this function fixes the pink arrow that tells you where to go and also stops those cutscenes from playing since they're out of order story-wise
    with open("./XC2/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: # shortens opening section
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 7: #if we go to argentum
                row["NextQuestA"] = 9 # then go explore argentum
            if row["$id"] == 10: #if we go to bana's room
                row["NextQuestA"] = 12 # then complete the big prep quest
            if row["$id"] == 13: # if we rest at lemour inn (this seems to make the flags go away that were keeping you from shopping and going further upstairs in argentum)
                row["NextQuestA"] = 15 # then talk to spraine
            if row["$id"] == 15: #talk to spraine
                row["NextQuestA"] = 17 #sets next quest to be to go to the top of the Maelstrom
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)


def MinimizeTutorialBoxes():
    with open("XC2/JsonOutputs/common/MNU_Tutorial_Tips.json", 'r+', encoding='utf-8') as tipFile: # Minimizing the number of boxes a tutorial has
        tipData = json.load(tipFile)
        for tip in tipData["rows"]:
            for i in range(1,4):
                tip[f"window_y{i}"] = 0
                tip[f"message{i}"] = 0
        JSONParser.CloseFile(tipData, tipFile)

def AreaReloadSkip():
    with open("./XC2/JsonOutputs/common_gmk/ma40a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: # skipping an area reload
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [40053, 40054, 40055, 40056]:
                row["ScenarioFlagMin"] = row["ScenarioFlagMax"] = 11130
            #elif row["$id"] == 40001:
            #    row["ScenarioFlagMin"] = row["ScenarioFlagMax"] = 11004
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BFTutorials():
    with open("./XC2/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: # removing more tutorials
        data = json.load(file)
        removables = ["tut_sys26", "tut_sys22", "tut_sys14", "tut_sys02", "tut_btl23", "aoc_tut27"] # "aoc_tut24" plays right at the start but unlocks your current object menu and some other stuff
        for row in data["rows"]:
            if row["scriptName"] in removables:
                row["scriptName"] = ""
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def TornaQuestTutorials(removables):
    with open("./XC2/JsonOutputs/common/EVT_listQst01.json", 'r+', encoding='utf-8') as file: # removing torna tutorials
        data = json.load(file)
        for row in data["rows"]:
            if row["scriptName"] in removables:
                row["scriptName"] = ""
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BattleTutorials():
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["script_file"], "aoc_challenge_tutorial") # Shortens battle tutorials
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["start_id"], 0)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["param1"], 0)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["param1"], 0)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["script_file"], "aoc_challenge_tutorial")
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["start_id"], 0)

def FieldTutorials():
    removables = ["aoc_tut14", "aoc_tut11", "aoc_tut12", "aoc_tut26", "aoc_tut22", "aoc_tut20", "aoc_tut15", "aoc_tut17"]
    with open("./XC2/JsonOutputs/common/EVT_listFev01.json", 'r+', encoding='utf-8') as file: # removing tutorials in field
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 30005:
                row["chgEdID"] = 30007
            if "tut_sys" in row["scriptName"] or row["scriptName"] in removables:
                row["scriptName"] = ""
                row["scriptStartId"] = 0
        JSONParser.CloseFile(data, file)

def Tutorials():
    with open("./XC2/JsonOutputs/common/FLD_QuestListNormal.json", 'r+', encoding='utf-8') as file: #shortens tutorials
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
    with open("./XC2/JsonOutputs/common/FLD_QuestTaskNormal.json", 'r+', encoding='utf-8') as file: #adjusting tutorial quests
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
    with open("./XC2/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #adjusting tutorial quests
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


def SpraineTalk():
    with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: #this makes it so spraine will talk to us no matter how small the flag
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

def CoreCrystalTutorials():
    with open("./XC2/JsonOutputs/common_gmk/FLD_Tutorial.json", 'r+', encoding='utf-8') as file: # part of core crystal tutorial
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
    with open("./XC2/JsonOutputs/common_gmk/RSC_GmkSetList.json", 'r+', encoding='utf-8') as file: # part of core crystal tutorial
        data = json.load(file)
        for row in data["rows"]:
            if row["tutorial"] != "ma05a_tutorial":
                row["tutorial"] = ""
                row["tutorial_bdat"] = ""
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)


def IndolQuizSkip():
    JSONParser.ChangeJSONLine(["common/FLD_QuestList.json"],[156], ["NextQuestA"], 158)
    #JSONParser.ChangeJSONLine(["common/EVT_listBf.json"],[10261], ["nextID", "nextIDtheater"], 10262)
    JSONParser.ChangeJSONLineInMultipleSpots(["common/EVT_chgBf01.json"],[10255], ["chgName", "chgType", "id"], ["bf06_140_130", 1, 6020])
    #JSONParser.ChangeJSONLineInMultipleSpots(["common_gmk/ma11a_FLD_LandmarkPop.json"],[1116], ["category", "MAPJUMPID"], [2, 0])
    #JSONParser.ChangeJSONLineInMultipleSpots(["common_gmk/ma11a_FLD_LandmarkPop.json"],[1117], ["category", "MAPJUMPID"], [0, 132])
    JSONParser.ChangeJSONLineInMultipleSpots(["common/FLD_LODList.json"], [162], ["ScenarioFlagMin1", "ScenarioFlagMax1", "QuestFlag1", "QuestFlagMin1", "QuestFlagMax1"], [6019, 6025, 0, 0, 0])
    
# def TutorialEnemySwaps(): # Swap id in enarrange to an unused enemy so that tutorials no longer activate (Didnt work, the code works but tutorials still show)
