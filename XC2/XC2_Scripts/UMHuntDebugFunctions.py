import json, random, IDs, EnemyRandoLogic, RaceMode, math, Options, time, FieldSkillAdjustments
from Enhancements import *
from BladeRandomization import Replacement2Original
from scripts import Helper
from UMHuntMain import *

def DebugEnemyLevels(ChosenAreaOrder):
    AllAreasEnemies = []
    TotalAreasEnemies = []
    for k in range(0, len(ChosenAreaOrder)):
        CurrentAreasEnemies = []
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[k]][2] + "_FLD_EnemyPop.json"
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for k in range(1, 5):
                    if row[f"ene{k}ID"] == 0:
                        break
                    elif row[f"ene{k}num"] != 0:
                        CurrentAreasEnemies.append(row[f"ene{k}ID"])
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        AllAreasEnemies.append(CurrentAreasEnemies)
        TotalAreasEnemies.extend(list(set(CurrentAreasEnemies)))
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(ChosenAreaOrder)):
            for row in data["rows"]:
                if (row["$id"] in AllAreasEnemies[i]) & (row["Lv"] not in [5+12*i, 115, 125, 135, 145, 155]): #if the enemy level doesnt match what it should
                    print(f"{row['$id']} is not the correct level for {ChosenAreaOrder[i]}! It should be level {5+12*i}.")
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(len(TotalAreasEnemies)):
        numofenemy = TotalAreasEnemies.count(TotalAreasEnemies[i])
        if numofenemy > 1:
            print(f"{TotalAreasEnemies[i]} appears {numofenemy} times!")

def DebugFindMonsters(ChosenAreaOrder): # was used to debug and find enemies that spawned in too often. If the objective pointer points towards defeating an enemy of which there are 16 or more on the map you're on, the game will freeze upon loading.
    enemycountholder = Helper.ExtendListtoLength([0], len(AllQuestDefaultEnemyIDs),"0")
    for i in range(0, len(ChosenAreaOrder)):
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_EnemyPop.json"
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for k in range(1, 5):
                    if row[f"ene{k}ID"] == 0:
                            break
                    else:
                        for j in range(0, len(AllQuestDefaultEnemyIDs)):
                            if row[f"ene{k}ID"] == AllQuestDefaultEnemyIDs[j]:
                                enemycountholder[j] += row[f"ene{k}num"]
                                break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    toolargepool = {
        "IDs": [],
        "Counts": []
    }
    for i in range(0, len(enemycountholder)):
        if enemycountholder[i] >= 10: # I chose 10 as an arbitrary number under 16. 
            toolargepool["IDs"].append(AllQuestDefaultEnemyIDs[i])
            toolargepool["Counts"].append(enemycountholder[i])
    print(toolargepool)

def DebugItemsPlace(): #need to place some tokens to play around with them in the shops
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 209:
                row["itm1ID"] = 25488
                row["itm1Num"] = 1
                row["itm2ID"] = 25487
                row["itm2Num"] = 1
                row["itm3ID"] = 25489
                row["itm3Num"] = 1
                row["itm4ID"] = 25485
                row["itm4Num"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DebugEasyMode(): # if this is on, enemies will be lv 1, makes it easier to playtest
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # Adjusted their levels
        data = json.load(file)
        for row in data["rows"]:
            row["Lv"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DebugSpawnCountPrint(EnemySets, ChosenAreaOrder): # Prints how many times an enemy spawns, think it's causing a crash
    debugfilename = "D:/XC2 Rando Debug Logs/EnemyCounting.txt"
    debugfile = open(debugfilename, "w", encoding= "utf-8")
    for k in range(0, len(ChosenAreaOrder)):
        for i in range(0, len(IDs.ValidEnemyPopFileNames)):
            if ContinentInfo[ChosenAreaOrder[k]][2] in IDs.ValidEnemyPopFileNames[i]:
                enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + IDs.ValidEnemyPopFileNames[i]
                AreaUMCount = [0,0,0,0]
                with open(enemypopfile, 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        for j in range(0, len(EnemySets[k])):
                            for l in range(1, 5):
                                if row[f"ene{l}ID"] == EnemySets[k][j]:
                                    AreaUMCount[j] += row[f"ene{l}num"]
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)
                debugfile.write(f"{ChosenAreaOrder[k]}\n\n")
                for j in range(0, 4):
                    debugfile.write(f"ID:{EnemySets[k][j]} Count:{AreaUMCount[j]}\n")  
    debugfile.close()

def DebugGetNPCIDs(): # was used to figure out how many instances of an npc show up in the argentum bazaar. Checked by running around there myself
    TargetedNPCIDs = []
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        CurNPC = 0
        NPCCount = 0
        CurCount = 3 # change this to change what version of an npc shows up (zero-indexed)
        for row in data["rows"]:
            CurNPC = row["NpcID"]
            NPCCount = 0
            for row2 in data["rows"]:
                if row2["NpcID"] == CurNPC:
                    CurNPC2 = row2["$id"]
                    if NPCCount < CurCount:
                        NPCCount += 1
                        row2["ShopID"] = 0
                        row2["flag"]["Talkable"] = 0
                        row2["EventID"] = 0
                        row2["QuestFlag"] = 0
                        row2["ScenarioFlagMin"] = 10047
                        row2["ScenarioFlagMax"] = 10048
                        row2["QuestID"] = 0
                    elif NPCCount == CurCount:
                        row2["flag"]["Talkable"] = 1
                        row2["QuestFlag"] = 0
                        row2["ScenarioFlagMin"] = 1001
                        row2["ScenarioFlagMax"] = 10048
                        row2["Condition"] = 0
                        row2["Mot"] = 0
                        row2["TimeRange"] = 0
                        row2["QuestID"] = 0
                        row2["ShopID"] = 0
                        row2["EventID"] = 41123
                        row2["Visible_XZ"] = 100
                        row2["Visible_Y"] = 10
                        row2["Invisible_XZ"] = 105
                        row2["Invisible_Y"] = 15
                        TargetedNPCIDs.append(row2["$id"])
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
pass

def DebugFindIDForName():
    Instance1NPCNames = ["Shoon", "Hiyaya", "Melolo", "Pupunin", "Lhagen", "Hatatat", "Mitutu", "Motata", "Kynon", "Amumu", "Temimi", "Neyaya", "Pelala", "Mamalu", "Nunana", "Bonbon", "Momoni", "Denden", "Zuzu"]
    Instance2NPCNames = ["Helehele", "Pupunin", "Shynini", "Pelala", "Motata", "Mitutu", "Kynon", "Lutie", "Kux", "Ysolde", "Melolo", "Lhagen", "Hatatat", "Max", "Momoni", "Tonadon", "Garram", "Kokoi", "Pilopilo", "Shoon"]
    Instance3NPCNames = ["Melolo", "Lutie", "Kux", "Garram", "Kokoi", "Pilopilo", "Shoon", "Lhagen", "Kynon", "Helehele", "Pupunin", "Krujah", "Rurui", "Max"]
    Instance4NPCNames = ["Melolo", "Kynon", "Garram", "Pilopilo", "Shoon", "Lhagen", "Rurui", "Max", "Helehele", "Krujah"]

    NPCNames = Instance4NPCNames
    fldnpcnameIDs = []
    RSCNPCIDs = []
    MATWOIDs = []

    with open("./XC2/_internal/JsonOutputs/common_ms/fld_npcname.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(NPCNames)):
            for row in data["rows"]:
                if row["name"] == NPCNames[i]:
                    fldnpcnameIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/RSC_NpcList.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(fldnpcnameIDs)):
            for row in data["rows"]:
                if row["Name"] == fldnpcnameIDs[i]:
                    RSCNPCIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(RSCNPCIDs)):
            FoundInstance = 0
            for row in data["rows"]:
                if row["NpcID"] == RSCNPCIDs[i]:
                    if FoundInstance == 3: # change this to change the instance
                        MATWOIDs.append(row["$id"])
                        break
                    else:
                        FoundInstance += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(MATWOIDs)
    pass