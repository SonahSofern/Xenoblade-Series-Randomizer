import Helper
import json
import EnemyRandoLogic
import random

def Beta(CheckboxList, CheckboxStates):
        
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

        """         with open("./_internal/JsonOutputs/common_gmk/ma05a_FLD_EventPop.json", 'r+', encoding='utf-8') as file:
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
            json.dump(data, file, indent=2) """

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

