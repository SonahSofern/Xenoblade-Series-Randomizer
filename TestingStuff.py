import Helper
import json
import EnemyRandoLogic
import random


AreaList1 = [41, 68] #list of MapJump IDs for the first landmark in each map (114 is Temperantia (combining with Indol for now)), (180 is Land of Morytha (combining with Cliffs of Morytha for now))
AreaList2 = [90, 152]
AreaList3 = [125, 133, 168]
AreaList4 = [175, 187]

AreaList = [41, 68, 90, 125, 133, 152, 168, 175, 187]

MSGIDList = [63, 141, 205, 299, 314, 367, 396, 413, 445] #list of MSGIDs for each of the landmarks in Area List (276 for Temperantia) (427 for Land of Morytha) 

RaceModeDungeons = []
RaceModeDungeons.append(random.choice(AreaList1))
RaceModeDungeons.append(random.choice(AreaList2))
RaceModeDungeons.append(random.choice(AreaList3))
RaceModeDungeons.append(random.choice(AreaList4))

""" RaceModeMSGIDs = [] #take the race mode msg IDs (so you can see what areas you have, and where a warp takes you)

TestingMenuPrios = [1, 2, 3, 4, 5] # Controls the Map Priority

TestingXOffsets = [-154, -200, -155, -90, -153] # These two control the positions of the markers on Argentum

TestingYOffsets = [-207, -100, -63, -100, -72] """

# Default Level-Based Modifiers for EXP, Damage Taken/Given, Accuracy, and Odds of getting a reaction (on an enemy?) (break/topple/launch/smash)
ExpRevHigh = [105, 110, 117, 124, 134, 145, 157, 170, 184, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
ExpRevLow = [95, 86, 77, 69, 62, 56, 50, 45, 41, 37, 33, 30, 27, 24, 22, 20, 18, 16, 14, 13]
ExpRevLow2 = [100, 95, 88, 81, 75, 69, 64, 56, 49, 43, 38, 33, 29, 25, 22, 20, 18, 16, 14, 13]
DamageRevHigh = [100, 100, 100, 105, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
DamageRevLow = [100, 100, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66]
HitRevLow = [110, 115, 122, 129, 138, 147, 158, 169, 182, 195, 210, 225, 242, 259, 278, 297, 318, 339, 362, 385]
ReactRevHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 100, 100, 100, 100, 100, 100]

def Beta(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Beta Stuff Box":
            BetaStuffBox = j
            break
    if CheckboxStates[BetaStuffBox].get() == True:    
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/RSC_GmkSetList.json", ["tutorial", "tutorial_bdat"], "") #maybe removes tutorials
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_Tutorial.json", ["ScenarioFlagMin", "QuestFlag", "QuestFlagMin", "QuestFlagMax", "SysMultiFlag"], 0) #maybe removes tutorials
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_Condition.json", ["cond"], 1) #unlocks the world maps
        # EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma21a_FLD_LandmarkPop.json", ["cndID"], 0) #removes requirement to unlock location
        """ 
        for i in range(0, len(RaceModeDungeons)):
            for j in range(0, len(AreaList)):
                if RaceModeDungeons[i] == AreaList[j]:
                    RaceModeMSGIDs.append(MSGIDList[j])

        RaceModeDungeons.append(200)
        RaceModeMSGIDs.append(470) 
        """
        """     with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: #adds landmarks for each race area you need to finish
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
            pass """
        
        with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
            data = json.load(file)
            for row in data["rows"]:
                if (row["$id"] >= 26) and (row["$id"] <= 50):
                    row["PRTQuestID"] = 25
                if row["$id"] == 26:
                    row["NextQuestA"] = 40 # tora + poppy
                    #row["CallEventA"] = 10088 # testing uraya, this should be a choice later
                    #row["FlagCLD"] = 685 # uraya flag
                    #row["NextQuestA"] = 56 #set out for village in uraya 
                if row["$id"] == 40:
                    row["NextQuestA"] = 45
                if row["$id"] == 45: # nia + dromarch quest
                    row["PurposeID"] == 39
                    row["NextQuestA"] = 55 # quest in uraya
                if (row["$id"] >= 52) and (row["$id"] <= 81):
                    row["PRTQuestID"] = 24
                if row["$id"] == 55:
                    row["CallEventA"] = 10088
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

        """         with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: #tora+poppy
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 10033: #after pupunin cutscene to start chapter 2, instantly warp to tora's house and start the tiger!tiger! cutscene
                    row["nextID"] = 10064
                    row["chgEdID"] = 10059 #different than the nextID and nextIDtheater
                    row["scenarioFlag"] = 2032
                    row["nextIDtheater"] = 10064
                if row["$id"] == 10065:
                    row["edFormID"] = 1067
                    row["nextID"] = 10074
                    row["nextIDtheater"] = 10074
                    row["linkID"] = 10074
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2) """

        with open("./_internal/JsonOutputs/common_gmk/ma05a_FLD_EventPop.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 5008: #tora+poppy, plays event 10064, which sets the scenario to 2034 afterwards
                    row["QuestFlag"] = 0
                    row["QuestFlagMin"] = 0
                    row["QuestFlagMax"] = 0
                    row["Condition"] = 0
                    row["ScenarioFlagMin"] = 2032
                    row["ScenarioFlagMax"] = 2032
                    row["EventID"] = 10064
                if row["$id"] == 5009: #nia+dromarch since the scenario flag is 2032, we then play the nia+dromarch cutscene in Tora's house
                    row["EventID"] = 10074 #play the event of nia breaking out of cell
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

        with open("./_internal/JsonOutputs/common/BTL_Lv_Rev.json", 'r+', encoding='utf-8') as file: #adjusting level based exp gains to make it less grindy
            data = json.load(file)
            for row in data["rows"]:
                row["ExpRevHigh"] = 210 + 20 * row["$id"]
                row["ExpRevLow"] = 100
                if row["$id"] >= 10:
                    row["DamageRevHigh"] = 200
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

