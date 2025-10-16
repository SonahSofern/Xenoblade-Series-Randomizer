import json, copy, os
from scripts import Helper, JSONParser
from XC2.XC2_Scripts import Options, EnemyRandoLogic, IDs

def ShortenedTutorial():
    RaceModeBox = Options.RaceModeOption.GetState()
    if not RaceModeBox:
        print("Shortening Tutorials")
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Condition.json", ["cond"], 1)
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
        EnemyRandoLogic.KeyItemsReAdd()
        with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_EventPop.json", 'r+', encoding='utf-8') as file: #allows waypoints to work, and us to skip Melolo
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] <= 2005:
                    row["ScenarioFlagMin"] = 1003
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
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
        with open("./XC2/JsonOutputs/common/EVT_listFev01.json", 'r+', encoding='utf-8') as file: # removing tutorials in field
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 30005:
                    row["chgEdID"] = 30007
                if "tut_" in row["scriptName"] or "aoc_tut" in row["scriptName"]:
                    row["scriptName"] = ""
                    row["scriptStartId"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
            
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["script_file"], "aoc_challenge_tutorial") # Shortens battle tutorials
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["start_id"], 0)
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial.json", ["param1"], 0)
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["param1"], 0)
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["script_file"], "aoc_challenge_tutorial")
        Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_Tutorial_Ira.json", ["start_id"], 0)
        with open("./XC2/JsonOutputs/common/EVT_listFev01.json", 'r+', encoding='utf-8') as file: # removing torna tutorials
            data = json.load(file)
            removables = ["aoc_tut04", "aoc_tut25", "aoc_tut14", "aoc_tut21", "aoc_tut06", "aoc_tut07", "aoc_tut09", "aoc_tut08"] # "aoc_tut10"
            for row in data["rows"]:
                if row["scriptName"] in removables:
                    row["scriptName"] = ""
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/JsonOutputs/common/EVT_listQst01.json", 'r+', encoding='utf-8') as file: # removing torna tutorials
            data = json.load(file)
            removables = ["aoc_tut14", "aoc_tut11", "aoc_tut12", "aoc_tut26", "aoc_tut22", "aoc_tut20", "aoc_tut15", "aoc_tut17"]
            for row in data["rows"]:
                if row["scriptName"] in removables:
                    row["scriptName"] = ""
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        with open("./XC2/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: # removing more tutorials
            data = json.load(file)
            removables = ["tut_sys26", "tut_sys22", "tut_sys14", "tut_sys02", "tut_btl23", "aoc_tut27"]
            for row in data["rows"]:
                if row["scriptName"] in removables:
                    row["scriptName"] = ""
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

        #with open("./XC2/JsonOutputs/common/EVT_chgBf01.json", 'r+', encoding='utf-8') as file: # skipping an area reload
        #    data = json.load(file)
        #    for row in data["rows"]:
        #        if row["$id"] == 10910:
        #            row["id"] = 11004
        #    file.seek(0)
        #    file.truncate()
        #    json.dump(data, file, indent=2, ensure_ascii=False)

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

def RaceModeTutorialShortening(): # we need to call this from the race mode function
    ShortenedTutorial()
    Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "")
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
                break
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
#     TutorialEnemyIDs = [179, 181, 182, 184, 187, 191, 193, 199, 203, 206, 272, 254, 185, 193, 250]
    
#     def AreaLoop(id, newID):
#         # Swap IDs in the gimmick files
#         for area in IDs.MajorAreaIds:
#             filename = f"XC2/JsonOutputs/common_gmk/ma{area}a_FLD_EnemyPop.json"
#             if not os.path.isfile(filename):
#                 continue
#             with open(filename, 'r+', encoding='utf-8') as popFile:
#                 popData = json.load(popFile)
#                 for en in popData["rows"]:
#                     for i in range(1,5):
#                         if en[f"ene{i}ID"] == id:
#                             en[f"ene{i}ID"] = newID
#                             JSONParser.CloseFile(popData, popFile)
#                             return
    
#     # Swap stats for the IDs in EnArrange
#     def ArrangeSwap(id, newID):
#         with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
#             eneData = json.load(eneFile)
            
#             for en in eneData["rows"]: # Find the new ID
#                 if en["$id"] == newID:
#                     newEn = en
#                     break
            
#             invalidKeys = ["$id"]     
#             for en in eneData["rows"]: # Swap with the old
#                 if en["$id"] == id:
#                     oldEn = copy.deepcopy(en)
#                     for key in newEn:
#                         if key in invalidKeys:
#                             continue
#                         newEn[key] = oldEn[key]
#                     break
#             JSONParser.CloseFile(eneData, eneFile)
        
                   
#     # Swap IDs in the IDs variables
#     newID = 7 # Going to start at 7 since theres a swathe of enemies that arent used from 7-65
#     for id in TutorialEnemyIDs:
#         for bossId in IDs.BossMonsters:
#             if id == bossId:
#                 bossId = newID
#                 newID += 1
#                 break
#         AreaLoop(id, newID)
#         ArrangeSwap(id, newID)