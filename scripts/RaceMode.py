import Helper as Helper
import json
import EnemyRandoLogic as EnemyRandoLogic
import random
from IDs import AllRaceModeItemTypeIDs, RaceModeAuxCoreIDs, A1RaceModeCoreChipIDs, A2RaceModeCoreChipIDs, A3RaceModeCoreChipIDs, A4RaceModeCoreChipIDs, SeedHashAdj, SeedHashNoun 

AllMapIDs = [["Gormott", "ma05a"], ["Uraya", "ma07a"], ["Mor Ardain","ma08a"], ["Leftherian Archipelago", "ma15a"], ["Indoline Praetorium", "ma11a"], ["Tantal", "ma13a"], ["Spirit Crucible Elpys", "ma16a"], ["Cliffs of Morytha", "ma17a"], ["World Tree", "ma20a"], ["Final Stretch", "ma21a"]] #that we care about lol

# Default Level-Based Modifiers for EXP, Damage Taken/Given, Accuracy, and Odds of getting a reaction (on an enemy?) (break/topple/launch/smash)
ExpRevHigh = [105, 110, 117, 124, 134, 145, 157, 170, 184, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
ExpRevLow = [95, 86, 77, 69, 62, 56, 50, 45, 41, 37, 33, 30, 27, 24, 22, 20, 18, 16, 14, 13]
ExpRevLow2 = [100, 95, 88, 81, 75, 69, 64, 56, 49, 43, 38, 33, 29, 25, 22, 20, 18, 16, 14, 13]
DamageRevHigh = [100, 100, 100, 105, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
DamageRevLow = [100, 100, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66]
HitRevLow = [110, 115, 122, 129, 138, 147, 158, 169, 182, 195, 210, 225, 242, 259, 278, 297, 318, 339, 362, 385]
ReactRevHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 100, 100, 100, 100, 100, 100]

def RaceModeChanging(OptionsRunDict): 
    print("Setting Up Race Mode")    
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", ["cond1"], 1850) #unlocks the world maps
    EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/FLD_maplist.json", ["mapON_cndID"], 1850) #unlocks the world maps
    
    AreaList1 = [41, 68] # 41
    AreaList2 = [99, 152] #99
    AreaList3 = [125, 133, 168] #133, 168
    AreaList4 = [175, 187]

    AreaList = [41, 68, 99, 152, 125, 133, 168, 175, 187]

    MSGIDList = [63, 141, 205, 367, 299, 314, 396, 413, 445] #list of MSGIDs for each of the landmarks in Area List (276 for Temperantia) (427 for Land of Morytha) 

    RaceModeDungeons = []
    RaceModeDungeons.append(random.choice(AreaList1))
    RaceModeDungeons.append(random.choice(AreaList2))
    RaceModeDungeons.append(random.choice(AreaList3))
    RaceModeDungeons.append(random.choice(AreaList4))
    RaceModeDungeons.append(200)

    # common/FLD_QuestList
    # [Gormott, Uraya, Mor Ardain, Leftherian Archipelago, Temperantia + Indoline Praetorium, Tantal, Spirit Crucible Elpys, Cliffs of Morytha + Land of Morytha, World Tree, Final Stretch]

    ContinentWarpCutscenes = [10034, 10088, 10156, 10197, 10213, 10270, 10325, 10350, 10399, 10476] # We want to call these after the boss fight cutscenes
    FinalContinentCutscenes = [10079, 10130, 10189, 10212, 10266, 10304, 10345, 10392, 10451, 30000]
    ScenarioFlagLists = [2001, 3005, 4025, 5005, 5021, 6028, 7018, 7043, 8031, 10026]
    NextQuestAList = [27, 56, 100, 128, 136, 163, 184, 194, 214, 238]
    LastQuestAList = [50, 81, 125, 135, 161, 177, 191, 211, 227, 270]
    LevelAtStartofArea = [5, 20, 29, 35, 38, 42, 46, 51, 59, 68] #Level going to: # Level(ish) of the first boss of the current area (so you want to be around this level after warping)
    LevelAtEndofArea = [15, 26, 34, 35, 42, 46, 46, 59, 68, 70]  #Level going from: # Level the last boss of the previous area was (so you should be around the same level before warping to new area)

    # The Save File is set up in a way that it has 56 bonus exp already, and is at level 2, so that value (totals to 76 xp gained) gets subtracted from the total xp needed
    # XP needed to reach a given level, formatted in [Given Level, Total XP Needed] 
    XPNeededToReachLv = [[5, 360], [15, 9060], [20, 21360], [26, 44520], [29, 59820], [34, 91320], [35, 98580], [38, 122520], [42, 160080], [46, 205140], [51, 274640], [59, 428120], [68, 682040], [70, 789920]]

    ChosenIndices = []

    RaceModeMapJumpIDs = [41, 68, 99, 152, 125, 133, 168, 175, 187, 200]

    for i in range(0, len(RaceModeDungeons)): # Defines the chosen indices that we're using from the list of race-mode locations
        for j in range(0, len(RaceModeMapJumpIDs)):
            if RaceModeDungeons[i] == RaceModeMapJumpIDs[j]:
                ChosenIndices.append(j)

    ExpBefore = [0] * 5
    ExpAfter = [0] * 5
    ExpDiff = [0] * 5

    for i in range(0, len(ChosenIndices)): # Defines the EXP difference we need to give to the first landmark in a race-mode location    
        for j in range(0, len(XPNeededToReachLv)):
            if i == 0:
                ExpBefore[i] = 76
                if LevelAtStartofArea[ChosenIndices[i]] == XPNeededToReachLv[j][0]:    
                    ExpAfter[i] = XPNeededToReachLv[j][1]
                    break
            if i < 4:
                if LevelAtEndofArea[ChosenIndices[i-1]] == XPNeededToReachLv[j][0]:
                    ExpBefore[i] = XPNeededToReachLv[j][1]
                if LevelAtStartofArea[ChosenIndices[i]] == XPNeededToReachLv[j][0]:
                    ExpAfter[i] = XPNeededToReachLv[j][1]
            if i == 4:
                ExpAfter[i] = 682040
                if LevelAtEndofArea[ChosenIndices[i-1]] == XPNeededToReachLv[j][0]:
                    ExpBefore[i] = XPNeededToReachLv[j][1]
                    break
                
        ExpDiff[i] = ExpAfter[i] - ExpBefore[i]
        if ExpDiff[i] > 65535:
            ExpDiff[i] = 65535

    MapSpecificIDs = [501, 701, 832, 1501, 1101, 1301, 1601, 1701, 2001, 2103]
    FileStart = "./_internal/JsonOutputs/common_gmk/"
    FileEnd = "_FLD_LandmarkPop.json"
    LandmarkFilestoTarget = [] 
    LandmarkMapSpecificIDstoTarget = []
    
    for i in range(0, len(ChosenIndices)): # Defines what files we want to target and what map ids in that file we want to target  
        LandmarkFilestoTarget.append(FileStart + AllMapIDs[ChosenIndices[i]][1] + FileEnd)
        LandmarkMapSpecificIDstoTarget.append(MapSpecificIDs[ChosenIndices[i]])
    
    if ChosenIndices[0] == 0: # Because Gormott warp is broken currently, we 
        LandmarkFilestoTarget[0] = "./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json"
        LandmarkMapSpecificIDstoTarget[0] = 210

    for i in range(0, len(LandmarkFilestoTarget)):  # Adjusts the EXP gained from the first landmark in each race-mode location
        with open(LandmarkFilestoTarget[i], 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == LandmarkMapSpecificIDstoTarget[i]:
                    row["getEXP"] = ExpDiff[i]
                    row["getSP"] = 5000 * ChosenIndices[i]
                    if row["$id"] == 210: # because the Gormott warp is currently broken, we need a skip travel point there in case the player dies before getting a landmark.
                        row["category"] = 0
                        row["MAPJUMPID"] = 41
                        row["menuPriority"] = 1
                        row["MSGID"] = 63
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)
    
    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
        data = json.load(file)
        for row in data["rows"]:
            if (row["PRTQuestID"] != 0) and (row["$id"] >= 25):
                row["PRTQuestID"] = 6
            if row["$id"] == 15: # Talking to Spraine
                row["NextQuestA"] = NextQuestAList[ChosenIndices[0]]
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == LastQuestAList[ChosenIndices[i]]:
                    row["NextQuestA"] = NextQuestAList[ChosenIndices[i+1]]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file: #race mode implementation #these just adjust the quest markers as far as I can tell
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10013:
                if ChosenIndices[0] == 0:
                    # Gormott
                    row["nextID"] = 10035
                    row["scenarioFlag"] = 2002
                    row["nextIDtheater"] = 10035
                if ChosenIndices[0] == 1:
                    # Uraya
                    row["nextID"] = 10088
                    row["scenarioFlag"] = 3005
                    row["nextIDtheater"] = 10088
            if row["$id"] == 10189:
                row["linkID"] = 0
                row["envSeam"] = 0
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == FinalContinentCutscenes[ChosenIndices[i]]:
                    row["nextID"] = ContinentWarpCutscenes[ChosenIndices[i+1]]
                    row["nextIDtheater"] = ContinentWarpCutscenes[ChosenIndices[i+1]]
                    row["scenarioFlag"] = ScenarioFlagLists[ChosenIndices[i+1]]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    NGPlusBladeIDs = DetermineNGPlusBladeCrystalIDs(OptionsRunDict)
    DifficultyChanges()
    MenuChanges()
    print(OptionsRunDict["Race Mode"]["subOptionObjects"]["Custom Loot"]["subOptionTypeVal"].get())
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Custom Loot"]["subOptionTypeVal"].get():
        print("Filling Chests with Custom Loot")
        RaceModeLootChanges(ChosenIndices, NGPlusBladeIDs, OptionsRunDict)
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Less Grinding"]["subOptionTypeVal"].get():
        print("Reducing amount of grinding")
        LessGrinding()
        ReduceBladeReqTrustVals()
        SecondSkillTreeCostReduc()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Shop Changes"]["subOptionTypeVal"].get():    
        print("Changing Shops")
        ShyniniSaveUs()
        ShopRemovals()
        MovespeedDeedChanges()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Enemy Drop Changes"]["subOptionTypeVal"].get():
        print("Removing enemy drops")
        EnemyDropRemoval()
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["DLC Item Removal"]["subOptionTypeVal"].get():
        print("Nerfing Corvin and Crossette")
        DLCItemChanges()

def LessGrinding(): #adjusting level based exp gains, and debuffs while underleveled to make it less grindy
    with open("./_internal/JsonOutputs/common/BTL_Lv_Rev.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            row["ExpRevHigh"] = 210 + 20 * row["$id"]
            row["ExpRevLow"] = 100
            if row["$id"] >= 10:
                row["DamageRevHigh"] = 250
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def DetermineNGPlusBladeCrystalIDs(OptionsRunDict):
    NGPlusBladeIDs = [1043, 1044, 1046, 1047, 1048, 1049]
    NGPlusBladeCrystalIDs = []
    print(OptionsRunDict["Core Crystal Changes"]["optionTypeVal"].get())
    if OptionsRunDict["Core Crystal Changes"]["optionTypeVal"].get():
        print("Figuring out NG+ Blade IDs")
        with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for i in range(0, len(NGPlusBladeIDs)):
                for row in data["rows"]:
                    if row["BladeID"] == NGPlusBladeIDs[i]:
                        NGPlusBladeCrystalIDs.append(row["$id"])
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)
        return NGPlusBladeCrystalIDs

def RaceModeLootChanges(ChosenIndices, NGPlusBladeIDs, OptionsRunDict):
    NonNGPlusCoreCrystalIDs = set(Helper.InclRange(45002, 45010) + Helper.InclRange(45016, 45043) + [45056, 45057])
    NonNGPlusCoreCrystalIDs -= set(NGPlusBladeIDs)
    NonNGPlusCoreCrystalIDs = list(NonNGPlusCoreCrystalIDs)
    A1Num = random.randint(1,3) - 1
    A2Num = random.randint(4,6) - 1
    A3Num = random.randint(7,9) - 1
    A4Num = random.randint(10,12) - 1
    A1Equip = []
    A2Equip = []
    A3Equip = []
    A4Equip = []
    for i in range(0, len(AllRaceModeItemTypeIDs)):
        A1Equip.append(AllRaceModeItemTypeIDs[i][A1Num]) 
        A2Equip.append(AllRaceModeItemTypeIDs[i][A2Num])
        A3Equip.append(AllRaceModeItemTypeIDs[i][A3Num])
        A4Equip.append(AllRaceModeItemTypeIDs[i][A4Num])
    for i in range(0, len(RaceModeAuxCoreIDs)):
        A1Equip.append(RaceModeAuxCoreIDs[i][A1Num]) 
        A2Equip.append(RaceModeAuxCoreIDs[i][A2Num])
        A3Equip.append(RaceModeAuxCoreIDs[i][A3Num])
        A4Equip.append(RaceModeAuxCoreIDs[i][A4Num])
    Area1LootIDs = NonNGPlusCoreCrystalIDs[:11] + [25305] * 3 + Helper.InclRange(25249, 25264) + [25450] * 3 + A1Equip + [25408] * 5 + [25218, 25219] + A1RaceModeCoreChipIDs
    del NonNGPlusCoreCrystalIDs[:11]
    Area2LootIDs = NonNGPlusCoreCrystalIDs[:11] + [25305] * 3 + Helper.InclRange(25265, 25280) + [25450] * 3 + A2Equip + [25408] * 5 + [25220] + A2RaceModeCoreChipIDs
    del NonNGPlusCoreCrystalIDs[:11]
    Area3LootIDs = NonNGPlusCoreCrystalIDs + [25305] * 3 + Helper.InclRange(25281, 25291) + [25450] * 3 + A3Equip + [25408] * 5 + [25221] + A3RaceModeCoreChipIDs
    Area4LootIDs = NGPlusBladeIDs + [25305] * 3 + Helper.InclRange(25292, 25300) + [25450] * 3 + A4Equip + [25408] * 5 + [25222] + A4RaceModeCoreChipIDs
    random.shuffle(Area1LootIDs)
    random.shuffle(Area2LootIDs)
    random.shuffle(Area3LootIDs)
    random.shuffle(Area4LootIDs)
    AllAreaLootIDs = [Area1LootIDs, Area2LootIDs, Area3LootIDs, Area4LootIDs]
    TBoxFiles = [[0,0], [0,0], [0,0], [0,0]] # this needs to be changed to a for loop if i change the number of race mode dungeons (append [0,0])
    FileStart = "./_internal/JsonOutputs/common_gmk/"
    FileEnd = "_FLD_TboxPop.json"
    StartingPreciousIDs = Helper.InclRange(25001, 25499)
    ExcludePreciousIDs = Helper.InclRange(25218, 25222) + [25305] + [25408] + [25450] + [25405] + [25406] + [25407] + Helper.InclRange(25249, 25300) # We are ok with replacing these, since they're in the pool of items to pull from anyways
    FinalPreciousIDs = [x for x in StartingPreciousIDs if x not in ExcludePreciousIDs] # We do not want to replace these, these are quest/key items
    for i in range(0, len(ChosenIndices) - 1): # Defines what files we want to target and what map ids in that file we want to target  
        if (ChosenIndices[i] != 4) & (ChosenIndices[i] != 7):
            TBoxFiles[i][0] = FileStart + AllMapIDs[ChosenIndices[i]][1] + FileEnd
    BoxestoRandomizePerMap = [0] * (len(ChosenIndices) - 1)
    TBoxName = ""
    for i in range(0, len(ChosenIndices)):
        if ChosenIndices[i] == 4:
            TBoxFiles[i][0] = "./_internal/JsonOutputs/common_gmk/ma10a_FLD_TboxPop.json"
            TBoxFiles[i][1] = "./_internal/JsonOutputs/common_gmk/ma11a_FLD_TboxPop.json"
        if ChosenIndices[i] == 7:
            TBoxFiles[i][0] = "./_internal/JsonOutputs/common_gmk/ma17a_FLD_TboxPop.json"
            TBoxFiles[i][1] = "./_internal/JsonOutputs/common_gmk/ma18a_FLD_TboxPop.json"
    for i in range(0, len(TBoxFiles)):
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        TBoxName = row["name"]
                        if (TBoxName[5] != "q") & (TBoxName != "tbox_ma08a_f018"): # We want to not randomize the quest related loot boxes and a broken one inside collision on Mor Ardain
                            BoxestoRandomizePerMap[i] = BoxestoRandomizePerMap[i] + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)
    ItemsPerBox = []
    for i in range(0, len(AllAreaLootIDs)):
        ItemsPerBox.append(len(AllAreaLootIDs[i])//BoxestoRandomizePerMap[i])
        if ItemsPerBox[i] > 7:
            ItemsPerBox[i] = 7
        if ItemsPerBox[i] < 3:
            ItemsPerBox[i] = 3
            ItemtoChestDifference = 3 * BoxestoRandomizePerMap[i] - len(AllAreaLootIDs[i])
            for j in range(0, ItemtoChestDifference):
                AllAreaLootIDs[i].append(random.choice([25405, 25405, 25405, 25406, 25406, 25407])) # fill the rest with WP 
            random.shuffle(AllAreaLootIDs[i])
    k = 0
    for i in range(0, len(TBoxFiles)):
        k = 0
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]: # We want to double the gold per chest to compensate that we're not getting enemy drops
                        row["goldMin"] = 2 * row["goldMin"]
                        row["goldMax"] = 2 * row["goldMax"]
                    for row in data["rows"]:
                        if k > len(AllAreaLootIDs[i]): #If k ever exceeds the size of the loot ids we're shuffling, then we can stop going through the files
                            file.seek(0)
                            file.truncate()
                            json.dump(data, file, indent=2) 
                            break
                        TBoxName = row["name"]
                        if (TBoxName[5] != "q") & (TBoxName != "tbox_ma08a_f018"): # We want to not randomize the quest related loot boxes and a box on Mor Ardain stuck in collision
                            for j in range(0, 8):
                                if row[f"itm{j+1}ID"] not in FinalPreciousIDs:
                                    row[f"itm{j+1}ID"] = 0
                                    row[f"itm{j+1}Num"] = 0
                                    row[f"itm{j+1}Per"] = 0 # don't know if this is used at all, but better safe than sorry
                            for h in range(0, ItemsPerBox[i]):
                                if row[f"itm{h+1}ID"] not in FinalPreciousIDs:
                                    row[f"itm{h+1}ID"] = AllAreaLootIDs[i][k]
                                    row[f"itm{h+1}Num"] = 1
                                    k = k + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)
    print(OptionsRunDict["Race Mode"]["subOptionObjects"]["Mysterious Part Hunt"]["subOptionTypeVal"].get())
    if OptionsRunDict["Race Mode"]["subOptionObjects"]["Mysterious Part Hunt"]["subOptionTypeVal"].get(): 
        print("Shuffling in Mysterious Parts")
        MysteriousPartHunt(TBoxFiles, BoxestoRandomizePerMap, ChosenIndices)

def ShyniniSaveUs(): # Just in case we don't get good blade field skills, we can rely on Shynini to always sell core crystals :D
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 6:
                row["DefItem7"] = 45011
                row["DefItem8"] = 45012
                row["DefItem9"] = 45013
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def ShopRemovals(): # Removes the Expensive Core Crystal from the shop, as well as the shop deeds
    ShopDeedIDs = Helper.InclRange(25249, 25300)
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["PrivilegeItem"] in ShopDeedIDs:
                row["PrivilegeItem"] = 0
            if row["$id"] == 33:
                row["Addtem2"] = 0
                row["AddCondition2"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def MovespeedDeedChanges(): #Replaces all other deed effects with movespeed, makes the max movespeed bonus 250% instead of 25%
    DeedTypeIDValues = Helper.InclRange(1, 52)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["Type"] in DeedTypeIDValues:
                row["Caption"] = 603 # Increases running speed by 5%
                row["Name"] = 511 # Sprintsy Deeds (hehe)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in DeedTypeIDValues:
                row["Value"] = 5
                row["Type"] = 1
            if row["$id"] > 52:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 250%
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Max"] = 150
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)    

def DLCItemChanges(): # Changes all DLC gifts to 1 gold
    DLCIDRowsWithItems = Helper.InclRange(1,10) + Helper.InclRange(16, 24) + [30] + [36, 37] + Helper.InclRange(43, 55)
    with open("./_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in DLCIDRowsWithItems:
                row["item_id"] = 0
                row["category"] = 2
                row["value"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def DifficultyChanges(): # Makes Easy difficulty the same as Normal
    with open("./_internal/JsonOutputs/common/BTL_DifSetting.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            row["Easy"] = row["Normal"]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def MenuChanges(): # Adjusts the menu text # Ben still needs to push fix
    seedhashcomplete = random.choice(SeedHashNoun) + " " + random.choice(SeedHashAdj)
    with open("./_internal/JsonOutputs/common_ms/menu_ms.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 128:
                row["name"] = f"Seed Hash: {seedhashcomplete}"
                row["style"] = 166
            if row["$id"] == 129:
                row["name"] = "Race Mode Start"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    
def ReduceBladeReqTrustVals(): # Sets required Trust Values to 0.5x the vanilla values
    with open("./_internal/JsonOutputs/common/FLD_ConditionIdea.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row["TrustPoint"] = int(0.5 * row["TrustPoint"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def SecondSkillTreeCostReduc(): # Reduces the cost of the hidden driver skill tree by 80% for race mode
    FilePaths = ["./_internal/JsonOutputs/common/BTL_Skill_Dr_Table01.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table02.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table03.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table04.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table05.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table06.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"]
    for i in range(0, len(FilePaths)):
        with open(FilePaths[i], 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] > 15:
                    row["NeedSp"] = int(row["NeedSp"] / 5)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)

def EnemyDropRemoval(): # Removes all enemy drops, to avoid getting powerful equipment out of logic.
    for i in range(1, 9):
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/BTL_EnDropItem.json", [f"ItemID{i}", f"DropProb{i}", f"NoGetByEnh{i}", f"FirstNamed{i}"] , 0)

def MysteriousPartHunt(TBoxFiles, BoxestoRandomizePerMap, ChosenIndices): # Experimental Mode to make players go out and find chests. This does break the mysterious part quest, but with race mode, it was unlikely to work anyways lmao
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # makes them stackable
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in Helper.InclRange(25034, 25038):
                row["ValueMax"] = 10
                row["ClearNewGame"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma05a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # removing them from chests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 538:
                row["itm1ID"] = 0
                row["itm1Num"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma08a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # removing them from chests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 802:
                row["itm1ID"] = 0
                row["itm1Num"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma13a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # removing them from chests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1305:
                row["itm1ID"] = 0
                row["itm1Num"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common_gmk/ma15a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # removing them from chests
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1502:
                row["itm1ID"] = 0
                row["itm1Num"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file: # removing them from shops
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 345:
                row["SetItem1"] = 25038
                row["SetItem2"] = 0
                row["SetNumber2"] = 0
                row["SetItem3"] = 0
                row["SetNumber3"] = 0
            if row["$id"] == 346:
                row["SetItem1"] = 25084
                row["SetItem2"] = 0
                row["SetNumber2"] = 0
                row["SetItem3"] = 0
                row["SetNumber3"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    BlankstoShuffle = [0] * (len(ChosenIndices) - 1)
    PartstoShuffle = [0] * (len(ChosenIndices) - 1)
    for i in range(0, len(PartstoShuffle)):
        PartstoShuffle[i] = int(BoxestoRandomizePerMap[i] // 3)
        if PartstoShuffle[i] < 5:
            PartstoShuffle[i] = 5
        BlankstoShuffle[i] = BoxestoRandomizePerMap[i] - PartstoShuffle[i]
    Area1MysteriousPartLocations = [0] * BlankstoShuffle[0] + [25034] * PartstoShuffle[0]
    random.shuffle(Area1MysteriousPartLocations)
    Area2MysteriousPartLocations = [0] * BlankstoShuffle[1] + [25035] * PartstoShuffle[1]
    random.shuffle(Area2MysteriousPartLocations)
    Area3MysteriousPartLocations = [0] * BlankstoShuffle[2] + [25036] * PartstoShuffle[2]
    random.shuffle(Area3MysteriousPartLocations)
    Area4MysteriousPartLocations = [0] * BlankstoShuffle[3] + [25037] * PartstoShuffle[3]
    random.shuffle(Area4MysteriousPartLocations)
    AllMysteriousPartLocations = [Area1MysteriousPartLocations, Area2MysteriousPartLocations, Area3MysteriousPartLocations, Area4MysteriousPartLocations]
    ACurBox = 0
    for i in range(0, len(TBoxFiles)): # Shuffling the mysterious parts into the treasure chests
        ACurBox = 0
        for l in range(0, len(TBoxFiles[i])):
            if TBoxFiles[i][l] != 0:
                with open(TBoxFiles[i][l], 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        TBoxName = row["name"]
                        if (TBoxName[5] != "q") & (TBoxName != "tbox_ma08a_f018"):
                            if AllMysteriousPartLocations[i][ACurBox] != 0:
                                row["itm8ID"] = AllMysteriousPartLocations[i][ACurBox]
                                row["itm8Num"] = 1
                                #print(row["name"])
                            ACurBox = ACurBox + 1
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)
    QuestCollectIDs = [27, 50, 68, 69]
    with open("./_internal/JsonOutputs/common/FLD_QuestCollect.json", 'r+', encoding='utf-8') as file: # Making Quest Collect Entries for each of them
        data = json.load(file)
        for i in range(0, len(QuestCollectIDs)):
            for row in data["rows"]:
                if row["$id"] == QuestCollectIDs[i]:
                    row["Refer"] = 4
                    row["Count"] = 3
                    row["Deduct"] = 0
                    row["ItemID"] = 25034 + i
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)    
    LastQuestPurposeIDs = [48, 78, 121, 130, 155, 171, 184, 203, 218]
    with open("./_internal/JsonOutputs/common/FLD_QuestTask.json", 'r+', encoding='utf-8') as file: # Adding the Quest Requirement to the final quest of the area
        data = json.load(file)
        for i in range(0, len(ChosenIndices) - 1):
            for row in data["rows"]:
                if row["$id"] == LastQuestPurposeIDs[ChosenIndices[i]]:
                    row["TaskType2"] = 3
                    row["TaskID2"] = QuestCollectIDs[i]
                    row["TaskLog2"] = 195
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2) 