import json, random, Helper, IDs, EnemyRandoLogic, RaceMode, math
from Enhancements import *

AllUniqueMonsterDefaultIDs = [611, 612, 705, 706, 707, 708, 709, 710, 711, 712, 713, 715, 736, 738, 808, 809, 810, 811, 812, 814, 815, 816, 817, 819, 890, 891, 892, 893, 894, 895, 896, 898, 899, 926, 929, 953, 954, 955, 957, 958, 1019, 1020, 1023, 1025, 1026, 1101, 1102, 1104, 1106, 1108, 1109, 1111, 1112, 1113, 1114, 1115, 1131, 1132, 1134, 1155, 1156, 1157, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1255, 1256, 1258, 1260, 1261, 1262, 1264, 1265, 1563, 1564, 1566, 1567, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1670, 1774, 1886]

# "Location": [Warp Cutscene, "chgEdID", Map Name, Map ID]
ContinentInfo = {"Gormott": [10043, 10044, "ma05a", 6], "Uraya": [10088, 10079, "ma07a", 9], "Mor Ardain": [10156, 10149, "ma08a", 10], "Leftheria": [10197, 10192, "ma15a", 14], "Temperantia": [10233, 10224, "ma10a", 11], "Tantal": [10272, 10269, "ma13a", 13], "Spirit Crucible": [10325, 10323, "ma16a", 15], "Cliffs of Morytha": [10351, 10345, "ma17a", 16], "Land of Morytha": [10369, 10363, "ma18a", 18], "World Tree": [10399, 10393, "ma20a", 20]}

TotalAreaPool = ["Gormott", "Uraya", "Mor Ardain", "Leftheria", "Temperantia", "Tantal", "Spirit Crucible", "Cliffs of Morytha", "Land of Morytha", "World Tree"]

# "Driver": ["scriptName", "scriptStartID"]
PartyMembersAddScripts = {"Tora": ["chapt02", 7], "Nia": ["chapt02", 9], "Morag": ["chapt05", 7], "Zeke": ["chapt06", 5]}

ProofofPurchaseIDs = Helper.InclRange(25306, 25321)

ValidPouchItems = [x for x in IDs.PouchItems if x not in [40314, 40428]]

# Item ID 25489 is the Doubloon ID!

# TO DO

# Maybe change the blade bundles to be from the same overall class distribution pool, but have them be mixed up, and change the names to "Blade Bundle 1->10", and increase the cost accordingly
# Remove enemy arts that summon enemies that summon more enemies
# Add some secret shops on the map?
# add um sets for superbosses?
# add the names of weapons

# Known Issues: 
# Poppiswap is going to be fucked up with custom enhancements

def UMHunt(OptionDictionary):
    if IDs.CurrentSliderOdds != 0:
        SetCount = IDs.CurrentSliderOdds
        ChosenAreaOrder = []
        if IDs.CurrentSliderOdds > 10: #really need to limit the spinbox instead
            SetCount = 10
        ChosenAreaOrder.extend(random.sample(TotalAreaPool, SetCount))
        PartyMemberstoAdd = PartyMemberAddition(SetCount, ChosenAreaOrder)
        AreaUMs, AllAreaMonsters = CustomEnemyRando(ChosenAreaOrder)
        EnemySets = ChosenEnemySets(SetCount, AreaUMs)
        WarpManagement(SetCount, ChosenAreaOrder, PartyMemberstoAdd, EnemySets)
        CHR_EnArrangeAdjustments(AllAreaMonsters, EnemySets, ChosenAreaOrder)
        LandmarkAdjustments(ChosenAreaOrder)
        NoUnintendedRewards(ChosenAreaOrder)
        SpiritCrucibleEntranceRemoval()
        UMRewardDropChanges()
        CoreCrystalIdentification(OptionDictionary)
        WeaponPowerLevel()
        BladeTrustRequirementChanges()
        PoppiswapCostChanges()
        AddDLCRewards()
        CustomShopSetup()
        MoveSpeedDeedSetup()
        InnShopCosts()
        PneumaNerfs()
        ReplaceBana()
        SecretShopMaker(ChosenAreaOrder)
        RaceMode.SecondSkillTreeCostReduc()
        Cleanup()
        UMHuntMenuTextChanges()
        DebugItemsPlace()

def WarpManagement(SetCount, ChosenAreaOrder, PartyMemberstoAdd, EnemySets): # Main function was getting a bit too cluttered
    EventSetup(SetCount, ChosenAreaOrder, PartyMemberstoAdd)
    EventChangeSetup(SetCount, ChosenAreaOrder)
    QuestListSetup(SetCount, ChosenAreaOrder)
    QuestTaskSetup(SetCount, ChosenAreaOrder, EnemySets)
    FieldQuestBattleSetup(SetCount, ChosenAreaOrder, EnemySets)
    FieldQuestTaskLogSetup(SetCount, ChosenAreaOrder, EnemySets)
    AddQuestConditions(SetCount, ChosenAreaOrder)

def Cleanup():
    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if (row["PRTQuestID"] != 0) and (row["$id"] >= 25):
                row["PRTQuestID"] = 6
            if row["$id"] == 15: # Talking to Spraine
                row["NextQuestA"] = 234
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10013:
                row["nextID"] = 10464
                row["scenarioFlag"] = 10009
                row["nextIDtheater"] = 10464
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/CHR_Dr.json", ["DefAcce", "DefWP", "DefSP"], 0)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/CHR_Dr.json", ["DefLv"], 10)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/CHR_Dr.json", ["DefWPType", "DefSPType", "DefLvType"], 1)

def InnShopCosts(): # Removes cost to stay at inn
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/MNU_ShopInn.json", ["Price"], 0)

def PneumaNerfs(): # Mods, break her kneecaps
    with open("./_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 5970:
                row["Damage"] = 1 # Nerfing her base damage to 1 seems good enough, you can still use her for elemental combos, but it wont do much damage. The utility is still nice, but won't let you cheese a fight
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ReplaceBana(): # I want to use Bana as the exchange shop, so I move rumtumtum into Bana's spots on the map
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] != 2079) & (row["NpcID"] == 2002):
                row["NpcID"] = 2233
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def MoveSpeedDeedSetup():
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 25249:
                row["Caption"] = 603 # Increases running speed by 500%
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Value"] = 500
                row["Type"] = 1
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 250%
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Max"] = 750
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 491:
                row["name"] = "Movespeed Deed"
            if row["$id"] == 608:
                row["name"] = "Increases running speed by 500%."
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def QuestListSetup(SetCount, ChosenAreaOrder): # Adjusting the quest list
    with open("./_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            if i != SetCount - 1:
                for row in data["rows"]:
                    if row["$id"] == 235 + i:
                        row["Talker"] = 1001
                        row["FlagCLD"] = 832 + i
                        row["PurposeID"] = 249 + i
                        row["CountCancel"] = 1
                        row["NextQuestA"] = row["$id"] + 1
                        row["CallEventA"] = ContinentInfo[ChosenAreaOrder[i+1]][0]
                        break
            else:
                for row in data["rows"]:
                    if row["$id"] == 235 + i:
                        row["Talker"] = 1001
                        row["FlagCLD"] = 832 + i
                        row["PurposeID"] = 249 + i
                        row["CountCancel"] = 0
                        row["NextQuestA"] = 30000
                        row["CallEventA"] = 10494
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def EventSetup(SetCount, ChosenAreaOrder, PartyMemberstoAdd): # Adjusting the initial area warp events
    with open("./_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10465:
                row["nextID"] = ContinentInfo[ChosenAreaOrder[0]][0]
                row["nextIDtheater"] = row["nextID"]
                break
        for i in range(0, SetCount):
            for row in data["rows"]:
                if row["$id"] == ContinentInfo[ChosenAreaOrder[i]][0]:
                    row["scenarioFlag"] = 10010 + i
                    row["chapID"] = 10
                    row["linkID"] = 0
                    row["nextID"] = 0
                    row["nextIDtheater"] = 0
                    if PartyMemberstoAdd[i] != 0:
                        row["scriptName"] = PartyMembersAddScripts[PartyMemberstoAdd[i]][0]
                        row["scriptStartId"] = PartyMembersAddScripts[PartyMemberstoAdd[i]][1]
                    else:
                        row["scriptName"] = ""
                        row["scriptStartId"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def EventChangeSetup(SetCount, ChosenAreaOrder): # Adjusting the warp event endings that change scenario flags
    with open("./_internal/JsonOutputs/common/EVT_chgBf01.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            for row in data["rows"]:
                if row["$id"] == ContinentInfo[ChosenAreaOrder[i]][1]:
                    row["id"] = 10011 + i
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PartyMemberAddition(SetCount, ChosenAreaOrder): # Adds new party members
    ChosenPartyMemberOrder = []
    FirstPartyMember = []
    ChosenPartyMemberOrder.extend(random.sample(["Tora", "Zeke", "Nia", "Morag"], min(SetCount, 4)))
    FirstPartyMember.append(ChosenPartyMemberOrder[0]) # We want to guarantee getting 1 teammate minimum to start with
    ChosenPartyMemberOrder.pop(0)
    while len(ChosenPartyMemberOrder) < SetCount - 1:
        ChosenPartyMemberOrder.append(0)
    random.shuffle(ChosenPartyMemberOrder)
    FirstPartyMember.extend(ChosenPartyMemberOrder)
    RNGAdjustedChosenPartyMemberOrder = FirstPartyMember
    return RNGAdjustedChosenPartyMemberOrder

def QuestTaskSetup(SetCount, ChosenAreaOrder, EnemySets): # Adds the new quest tasks
    StartingQuestTaskRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_QuestBattle.json", "$id") + 1
    StartingQuestLogRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_quest.json", "$id") + 1
    with open("./_internal/JsonOutputs/common/FLD_QuestTask.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            if len(EnemySets[i]) == 4:
                data["rows"].append({"$id": 249 + i, "PreCondition": 0, "TaskType1": 1, "TaskID1": StartingQuestTaskRow, "Branch1": 0, "TaskLog1": StartingQuestLogRow, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 1, "TaskID2": StartingQuestTaskRow + 1, "Branch2": 0, "TaskLog2": StartingQuestLogRow + 1, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 1, "TaskID3": StartingQuestTaskRow + 2, "Branch3": 0, "TaskLog3": StartingQuestLogRow + 2, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 1, "TaskID4": StartingQuestTaskRow + 3, "Branch4": 0, "TaskLog4": StartingQuestLogRow + 3, "TaskUI4": 0, "TaskCondition4": 0}) 
                StartingQuestTaskRow += 4
                StartingQuestLogRow += 4
            else: # if it's not 4, its 3
                data["rows"].append({"$id": 249 + i, "PreCondition": 0, "TaskType1": 1, "TaskID1": StartingQuestTaskRow, "Branch1": 0, "TaskLog1": StartingQuestLogRow, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 1, "TaskID2": StartingQuestTaskRow + 1, "Branch2": 0, "TaskLog2": StartingQuestLogRow + 1, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 1, "TaskID3": StartingQuestTaskRow + 2, "Branch3": 0, "TaskLog3": StartingQuestLogRow + 2, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 0, "TaskID4": 0, "Branch4": 0, "TaskLog4": 0, "TaskUI4": 0, "TaskCondition4": 0}) 
                StartingQuestTaskRow += 3
                StartingQuestLogRow += 3
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FieldQuestBattleSetup(SetCount, ChosenAreaOrder, EnemySets): # Adds new rows in FLD_QuestBattle accordingly
    with open("./_internal/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as file:
        LastRow = 777
        LastFlag = 795
        data = json.load(file)
        for i in range(0, SetCount):
            for j in range(0, len(EnemySets[i])):
                data["rows"].append({"$id": LastRow, "Refer": 1, "EnemyID": EnemySets[i][j], "EnemyGroupID": 0, "EnemySpeciesID": 0, "EnemyRaceID": 0, "Count": 1, "CountFlag": LastFlag, "DeadAll": 0, "TimeCount": 0, "TimeCountFlag": 0, "ReduceEnemyHP": 0, "ReducePCHP": 0, "TargetOff": 0}) 
                LastRow = LastRow + 1
                LastFlag = LastFlag + 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FieldQuestTaskLogSetup(SetCount, ChosenAreaOrder, EnemySets): # Adds the task logs for the field quests
    AllEnemySetNames = []
    AllEnemySetNameIDs = []
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # add level scaling here
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            CurrEnemySetNameIDs = []
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == EnemySets[i][j]:
                        CurrEnemySetNameIDs.append(row["Name"])
                        row["Lv"] = 5 + 12*i # Sets level of enemy equal to 5 min, then for each set after, the level goes up by 11 more
                        break
            AllEnemySetNameIDs.append(CurrEnemySetNameIDs)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            CurrEnemySetNames = []
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == AllEnemySetNameIDs[i][j]:
                        CurrEnemySetNames.append(row["name"])
                        break
            AllEnemySetNames.append(CurrEnemySetNames)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_quest.json", 'r+', encoding='utf-8') as file:
        StartRow = 278 # makes things easier to get the correct row
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            for j in range(0, len(EnemySets[i])):
                data["rows"].append({"$id": StartRow, "style": 62, "name": f"Defeat [System:Color name=tutorial]{AllEnemySetNames[i][j]}[/System:Color]"})
                StartRow = StartRow + 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ChosenEnemySets(SetCount, AreaUMs): # Figuring out what enemies to turn into a set
    EnemySets = []
    for i in range(0, SetCount):
        if len(AreaUMs[i]) >= 4:
            EnemySets.append(random.sample(AreaUMs[i], 4))
        else:
            EnemySets.append(random.sample(AreaUMs[i], len(AreaUMs[i])))
    return EnemySets

def CustomEnemyRando(ChosenAreaOrder): # Custom shuffling of enemies
    AllAreaUMs = []
    AllAreaMonsters = []
    AllOriginalUMIDs = []
    ShuffledUniqueEnemyIDs = AllUniqueMonsterDefaultIDs.copy()
    random.shuffle(ShuffledUniqueEnemyIDs)
    for k in range(0, len(ChosenAreaOrder)):
        for i in range(0, len(IDs.ValidEnemyPopFileNames)):
            if ContinentInfo[ChosenAreaOrder[k]][2] in IDs.ValidEnemyPopFileNames[i]:
                CurrentAreaUMs = []
                CurrentAreaMonsters = []
                CurrentAreaOriginalUMIDs = []
                enemypopfile = "./_internal/JsonOutputs/common_gmk/" + IDs.ValidEnemyPopFileNames[i]
                with open(enemypopfile, 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        if row["name"][:3] != "bos":
                            for j in range(0, len(ShuffledUniqueEnemyIDs)):
                                if row["ene1ID"] == AllUniqueMonsterDefaultIDs[j]: # only care about the first slot
                                    CurrentAreaOriginalUMIDs.append(row["ene1ID"])
                                    row["ene1ID"] = ShuffledUniqueEnemyIDs[j]
                                    row["Condition"] = row["ScenarioFlagMax"] = row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["muteki_QuestFlag"] = row["muteki_QuestFlagMin"] = row["muteki_QuestFlagMax"] = row["muteki_Condition"] = 0
                                    row["POP_TIME"] = 256
                                    row["popWeather"] = 255
                                    CurrentAreaUMs.append(row["ene1ID"])
                                    break
                        CurrentAreaMonsters.extend([row["ene1ID"], row["ene2ID"], row["ene3ID"], row["ene4ID"]])
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)
                CurrentAreaMonsters = [x for x in CurrentAreaMonsters if x != 0]
                CurrentAreaMonsters = list(set(CurrentAreaMonsters))
                AllOriginalUMIDs.append(CurrentAreaOriginalUMIDs)
                AllAreaUMs.append(CurrentAreaUMs)
                AllAreaMonsters.append(CurrentAreaMonsters)
        EnemyRandoLogic.FlyingEnemyFix(AllOriginalUMIDs[k], AllAreaUMs[k])
        EnemyRandoLogic.SwimmingEnemyFix(AllOriginalUMIDs[k], AllAreaUMs[k])
    EnemyRandoLogic.FishFix()
    EnemyRandoLogic.BigEnemyCollisionFix()

    return AllAreaUMs, AllAreaMonsters
    
def CHR_EnArrangeAdjustments(AllAreaMonsters, EnemySets, ChosenAreaOrder): # adjusts aggro + drops of all enemies
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/CHR_EnArrange.json", ["ExpRev", "GoldRev", "WPRev", "SPRev", "DropTableID", "DropTableID2", "DropTableID3", "PreciousID"], 0)         
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(AllAreaMonsters)):
            for row in data["rows"]:
                if row["$id"] in AllAreaMonsters[i]:
                    row["Lv"] = 5 + 12*i # Sets level of enemy equal to 5 min, then for each set after, the level goes up by 12 more, so eventually the enemies outscale you
        for i in range(0, len(EnemySets)):
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == EnemySets[i][j]:
                        row["ZoneID"] = ContinentInfo[ChosenAreaOrder[i]][3]
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    EnemyRandoLogic.SummonsLevelAdjustment()

def LandmarkAdjustments(ChosenAreaOrder): # removes xp and sp gains from landmarks, except for the first one, adds more safety landmarks to prevent players from getting softlocked
    for i in range(0, len(ChosenAreaOrder)):
        landmarkpopfile = "./_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_LandmarkPop.json"
        with open(landmarkpopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # removes xp gains from argentum landmarks
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma21a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # removes xp gains from elysium landmarks
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma17a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # Adds Cliffs of Morytha Landmark
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 1701:
                    row["menuPriority"] = 10
                if row["$id"] == 1706:
                    row["menuPriority"] = 20
                    row["category"] = 0
                    row["MAPJUMPID"] = 175
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma16a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # Turning Canyon of Husks into a second Landmark that warps you to Spirit Crucible Entrance
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1601:
                row["menuPriority"] = 10
            if row["$id"] == 1609:
                row["category"] = 0
                row["MAPJUMPID"] = 168
                row["menuPriority"] = 20
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma20a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # Turning World Tree Mizar Floor into another landmark
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 2001:
                    row["menuPriority"] = 10
                if row["$id"] == 2012:
                    row["category"] = 0
                    row["MAPJUMPID"] = 187
                    row["menuPriority"] = 20
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def AddQuestConditions(SetCount, ChosenAreaOrder): # Adding conditions for each area's warp to be unlocked + 1 to allow me to disable all other stuff (salvage points are the big one atm)
    # First, need to replace any conditions
    with open("./_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["ScenarioMax"] > 10009:
                row["ScenarioMax"] = 10009
            if row["NotScenarioMin"] < 10009:
                row["NotScenarioMin"] = 10009
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(0, len(ChosenAreaOrder)):
        eventpopfile = "./_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_EventPop.json"
        with open(eventpopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["ScenarioFlagMax"] > 10009:
                    row["ScenarioFlagMax"] = 10009
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    # Condition 3903 Disables Stuff when applied to it.
    with open("./_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": 322, "ScenarioMin": 1001, "ScenarioMax": 1002, "NotScenarioMin": 0, "NotScenarioMax": 0})
        for i in range(0, SetCount):
            data["rows"].append({"$id": 323 + i, "ScenarioMin": 10011 + i, "ScenarioMax": 10048, "NotScenarioMin": 0, "NotScenarioMax": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": 3903, "Premise": 0, "ConditionType1": 1, "Condition1": 322, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        for i in range(0, SetCount):
            data["rows"].append({"$id": 3904 + i, "Premise": 0, "ConditionType1": 1, "Condition1": 323 + i, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    OrderedMapIDs = []
    with open("./_internal/JsonOutputs/common/FLD_maplist.json", 'r+', encoding='utf-8') as file: # pretty sure this is messing up stuff with the maps
        data = json.load(file)
        for i in range(0, len(ChosenAreaOrder)):
            for row in data["rows"]:
                if row["select"] == ContinentInfo[ChosenAreaOrder[i]][2]:
                    OrderedMapIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_WorldMapCond.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] <= len(ChosenAreaOrder):
                row["mapId"] = ContinentInfo[ChosenAreaOrder[row["$id"] - 1]][3] # puts the mapIDs in order, so we can assign conditions in order
                row["cond1"] = 3903 + row["$id"]
            elif row["$id"] == len(ChosenAreaOrder) + 1:
                row["mapId"] = 3
                row["cond1"] = 3904
            else:
                row["mapId"] = 0
                row["cond1"] = 3903
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def NoUnintendedRewards(ChosenAreaOrder): # Removes any cheese you can do by doing sidequests, selling Collection Point items
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/FLD_QuestReward.json", ["Gold", "EXP", "Sp", "Coin", "DevelopZone", "DevelopPoint", "TrustPoint", "MercenariesPoint", "IdeaCategory", "IdeaValue", "ItemID1", "ItemNumber1", "ItemID2", "ItemNumber2", "ItemID3", "ItemNumber3", "ItemID4", "ItemNumber4"], 0) # doing quests don't reward you
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CollectionList.json", ["Price"], 0) # collectables sell for 0
    Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_SalvagePointList.json", ["Condition"], 3903) # salvaging is disabled
    Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2", "EnemyExp"], ['252']) # It costs 252 xp to level up, regardless of level
    Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/FLD_GravePopList.json", ["en_popID"], 0) # Keeps you from respawning a UM.
    Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", ["Condition"], 3903) # removes drops from chests in argentum
    Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", ["QuestID"], 0) # removes talking to NPCs in argentum
    Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/ma21a_FLD_TboxPop.json", ["Condition"], 3903) # removes treasure chests from Elysium
    for area in ChosenAreaOrder:
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_TboxPop.json", ["Condition"], 3903) # removes drops from chests
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_NpcPop.json", ["EventID"], 0) # removes talking to NPCs
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_NpcPop.json", ["QuestID"], 0) # removes talking to NPCs
        Helper.ColumnAdjust("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_NpcPop.json", ["ShopID"], 0) # removes talking to NPCs

def SpiritCrucibleEntranceRemoval(): # Exiting or Entering Spirit Crucible has problems with resetting the quest condition. So we remove that by warping the player back to the original landmark in that area.
    with open("./_internal/JsonOutputs/common_gmk/FLD_MapJump.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 3: # Leftherian Entrance to Spirit Crucible
                row["MapJumpId"] = 166 # get pranked lmao
            if row["$id"] == 4: # Spirit Crucible Entrance to Leftheria
                row["MapJumpId"] = 167 # get pranked lmao
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BladeTrustRequirementChanges(): # changes the blade trust/skill unlock requirements to defeating a specific number of UMs
    NumberofUMstoDefeat = [8, 16, 24, 32]
    KeyAchievementIDs = [15, 25, 0, 35, 45, 55, 65, 75, 85, 95, 105, 0, 0, 115, 125, 135, 145, 375, 385, 155, 185, 165, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 195, 355, 365, 395, 0, 415, 425, 465, 455, 445, 435, 405, 175, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 95, 405, 455, 455, 445, 435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 365, 85, 1668, 1678, 1648, 1658, 1739, 1749, 0, 1759, 1739, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 325, 325, 325, 1679, 1689, 1699, 1709, 1719, 1729]
    KeyAchievementIDs = list(set([x for x in KeyAchievementIDs if x != 0]))
    TaskIDs = Helper.ExtendListtoLength([Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_QuestCondition.json", "$id") + 1], 4, "inputlist[i-1]+1")
    TaskLogIDs = [659, 660, 661, 662]
    ValidBladeIDs = [1001, 1002, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1076, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1111, 1112]
    StarterBladeTrustSetAppearance = [16, 11, 12, 13, 14] #rank 1
    Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1
    ArtandSkillCols = ["ArtsAchievement1", "ArtsAchievement2", "ArtsAchievement3", "SkillAchievement1", "SkillAchievement2", "SkillAchievement3", "FskillAchivement1", "FskillAchivement2", "FskillAchivement3"]
    TrustCol = "KeyAchievement"

    ArtandSkillIDs = []
    TrustIDs = []

    for i in range(0, len(ArtandSkillCols)):
        ArtandSkillIDs += Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], ValidBladeIDs, ArtandSkillCols[i])
        ArtandSkillIDs = [x for x in ArtandSkillIDs if x != 0]

    TrustIDs.extend(Helper.AdjustedFindBadValuesList("./_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], ValidBladeIDs, TrustCol))
    TrustIDs = [x for x in TrustIDs if x != 0]

    with open("./_internal/JsonOutputs/common/FLD_AchievementSet.json", 'r+', encoding='utf-8') as file: # now we need to modify corresponding set ids
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ArtandSkillIDs:
                for j in range(1, 6):
                    if (row[f"AchievementID{j}"] != 0):
                        row[f"AchievementID{j}"] = 16
            if row["$id"] in TrustIDs:
                for j in range(1,6):
                    row[f"AchievementID{j}"] = StarterBladeTrustSetAppearance[j-1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #we need to change FLD_Achievement ID 1 to walk 1 step total
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                    row["StatsID"] = 60
                    row["Count"] = 1
                    row["DebugName"] = "WALK_TOTAL"
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_QuestTaskAchievement.json", 'r+', encoding='utf-8') as file: #now we need to modify the FLD_QuestTaskAchievement
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] <= 7004:
                    row["TaskType1"] = 10
                    row["TaskID1"] = TaskIDs[row["$id"]-7001]
                    row["TaskCondition1"] = 0
                if row["$id"] == 7005:
                    row["TaskType1"] = 12
                    row["TaskID1"] = 1
                    row["TaskCondition1"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_QuestCondition.json", 'r+', encoding='utf-8') as file: # Adding new Quest Conditions
        data = json.load(file)
        ConditionListRows = Helper.ExtendListtoLength([Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1], 4, "inputlist[i-1]+1")
        for i in range(0, 4):
            data["rows"].append({"$id": TaskIDs[i], "ConditionID": ConditionListRows[i], "MapID": 0, "NpcID": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file: # Adding new ConditionIDs for Quest Condition
        data = json.load(file)
        FlagListRows = Helper.ExtendListtoLength([Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionFlag.json", "$id") + 1], 4, "inputlist[i-1]+1")
        for i in range(0, 4):
           data["rows"].append({"$id": ConditionListRows[i], "Premise": 0, "ConditionType1": 4, "Condition1": FlagListRows[i], "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0 , "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    with open("./_internal/JsonOutputs/common/FLD_ConditionFlag.json", 'r+', encoding='utf-8') as file: # Adding new checks for the # of UMs defeated flag
        data = json.load(file)
        for i in range(0, 4):
           data["rows"].append({"$id": FlagListRows[i], "FlagType": 8, "FlagID": 2164, "FlagMin": NumberofUMstoDefeat[i], "FlagMax": 256})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./_internal/JsonOutputs/common_ms/fld_quest_achievement.json", 'r+', encoding='utf-8') as file: #modifying the text files that describe what you need to do to unlock the node
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] == TaskLogIDs[i]:
                    row["name"] = f"Defeat {NumberofUMstoDefeat[i]} total Unique Monsters."
                    break
            for row in data["rows"]:
                if row["$id"] == 663:
                    row["name"] = "Unlocked once you unlock the \n corresponding Trust Level."
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def UMHuntMenuTextChanges():
    seedhashcomplete = random.choice(IDs.SeedHashAdj) + " " + random.choice(IDs.SeedHashNoun) 
    with open("./_internal/JsonOutputs/common_ms/menu_ms.json", 'r+', encoding='utf-8') as file: #puts the seed hash text on the main menu and on the save game screen
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 128:
                row["name"] = f"Seed Hash: [System:Color name=green]{seedhashcomplete}[/System:Color]"
                row["style"] = 166
            if row["$id"] == 129:
                row["name"] = "[System:Color name=tutorial]Unique Monster Hunt[/System:Color]"
            if row["$id"] in [983, 1227]:
                row["name"] = "Bounties"
            if row["$id"] == 1644:
                row["name"] = f"{seedhashcomplete}"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/menu_main_contents_ms.json", 'r+', encoding='utf-8') as file: # Changes the name of "Expansion Pass"
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10:
                row["name"] = "Voucher Rewards"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ReceiptTextChanges(): # Changes the test for the Core Crystal Shop Receipts
    ProofofPurchaseNameIDs = Helper.InclRange(617, 632)
    ProofofPurchaseNameTexts = ["ATK 1 Receipt", "ATK 2 Receipt", "ATK 3 Receipt", "ATK 4 Receipt", "TNK 1 Receipt", "TNK 2 Receipt", "TNK 3 Receipt", "HLR 1 Receipt", "HLR 2 Receipt", "HLR 3 Receipt", "DLC 1 Receipt", "DLC 2 Receipt", "DLC 3 Receipt", "NG+ 1 Receipt", "NG+ 2 Receipt", "NG+ 3 Receipt"]
    ProofofPurchaseDescriptionIDs = Helper.InclRange(718, 733)
    ProofofPurchaseDescriptionText = "Proof you purchased this Blade Bundle."
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ProofofPurchaseIDs: # Proof of Purchases for Core Crystal Bundles
                row["ValueMax"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for i in range(0, len(ProofofPurchaseIDs)):
            for row in data["rows"]:
                if row["$id"] == ProofofPurchaseNameIDs[i]:
                    row["name"] = ProofofPurchaseNameTexts[i]
                if row["$id"] == ProofofPurchaseDescriptionIDs[i]:
                    row["name"] = ProofofPurchaseDescriptionText
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def UMRewardDropChanges(): #Changes text for the UM drops we want
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in Helper.InclRange(25479, 25489): # Custom Shop/UM Drop Token IDs
                row["ValueMax"] = 255
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for i in range(1, 11):
            for row in data["rows"]:
                if row["$id"] == 962 + i:
                    row["name"] = f"[System:Color name=green]Bounty Token Lv {i}[/System:Color]"
                if row["$id"] == 978 + i:
                    row["name"] = "Can be traded at the \nBounty Token Exchange for upgrades."
                    break
        for row in data["rows"]:
            if row["$id"] == 973:
                row["name"] = "[System:Color name=tutorial]Doubloon[/System:Color]"
            if row["$id"] == 989:
                row["name"] = "Can be traded at shops for upgrades."
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def IdentifyDLCBladeCrystals(CrystalList):
    DLCBladeCrystalList = []
    with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: # Adds the exchange tasks
        data = json.load(file)
        for i in range(0, len(CrystalList)):
            for row in data["rows"]:
                if (row["$id"] == CrystalList[i]) and (row["BladeID"] in [1105, 1106, 1107, 1108, 1109, 1111]):
                    DLCBladeCrystalList.append(row["$id"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return DLCBladeCrystalList

def IdentifyClassBladeCrystals(CrystalList): # go from ITM_CrystalList $id->bladeID-> CHR_Bl $id->WeaponType-> ITM_PcWpnType $id->Role
    CrystalBladeIDList = []
    CrystalWeaponTypeIDList = []
    CrystalWeaponRoleList = []
    AttackerList = []
    HealerList = []
    TankList = []
    with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: # Getting BladeIDs for a Crystal $id
        data = json.load(file)
        for i in range(0, len(CrystalList)):
            for row in data["rows"]:
                if row["$id"] == CrystalList[i]:
                    CrystalBladeIDList.append(row["BladeID"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as file: # Getting WeaponType for a Blade $id
        data = json.load(file)
        for i in range(0, len(CrystalBladeIDList)):
            for row in data["rows"]:
                if row["$id"] == CrystalBladeIDList[i]:
                    CrystalWeaponTypeIDList.append(row["WeaponType"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_PcWpnType.json", 'r+', encoding='utf-8') as file: # Getting Role for a WeaponType $id
        data = json.load(file)
        for i in range(0, len(CrystalWeaponTypeIDList)):
            for row in data["rows"]:
                if row["$id"] == CrystalWeaponTypeIDList[i]:
                    CrystalWeaponRoleList.append(row["Role"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(0, len(CrystalList)):
        if CrystalWeaponRoleList[i] == 1: # Tank
            TankList.append(CrystalList[i])
        elif CrystalWeaponRoleList[i] == 2: # Attacker
            AttackerList.append(CrystalList[i])
        else: # Healer
            HealerList.append(CrystalList[i])
    return TankList, AttackerList, HealerList

def CoreCrystalIdentification(OptionsRunDict): # Figuring out the groups that each Core Crystal Belongs to, then picking items from each group for the shop
    ShuffleCoreCrystals()
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    NGPlusBladeCrystalIDs = RaceMode.DetermineNGPlusBladeCrystalIDs(OptionsRunDict)
    RemainingBladeCrystalIDs = [x for x in AllBladeCrystalIDs if x not in NGPlusBladeCrystalIDs]
    DLCBladeCrystalIDs = IdentifyDLCBladeCrystals(RemainingBladeCrystalIDs)
    RemainingBladeCrystalIDs = [x for x in RemainingBladeCrystalIDs if x not in DLCBladeCrystalIDs]
    TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs = IdentifyClassBladeCrystals(RemainingBladeCrystalIDs)
    CoreCrystalGroupCreation(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs)

def ShuffleCoreCrystals(): # first we need to shuffle the blade ids into the core crystal pool
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    BladeIDs = [1008, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1050, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1104, 1108, 1109, 1105, 1106, 1107, 1111]
    with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for i in range(0, len(AllBladeCrystalIDs)):
            for row in data["rows"]:
                if row["$id"] == AllBladeCrystalIDs[i]:
                    row["BladeID"] = RandomBlades[i]
                    row["ValueMax"] = 1
                    row["NoMultiple"] = i + 11
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CoreCrystalGroupCreation(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs):
    Item1IDs, Item2IDs, Item3IDs, Item4IDs = [], [], ProofofPurchaseIDs, Helper.ExtendListtoLength([], 16, "0")
    ChosenAtkBlades, ChosenTnkBlades, ChosenHlrBlades = random.sample(AttackerBladeCrystalIDs, min(8, len(AttackerBladeCrystalIDs))), random.sample(TankBladeCrystalIDs, min(6, len(TankBladeCrystalIDs))), random.sample(HealerBladeCrystalIDs, min(6, len(HealerBladeCrystalIDs)))
    ChosenAtkBlades = Helper.ExtendListtoLength(ChosenAtkBlades, 8 , "0")
    ChosenTnkBlades = Helper.ExtendListtoLength(ChosenTnkBlades, 6 , "0")
    ChosenHlrBlades = Helper.ExtendListtoLength(ChosenHlrBlades, 6 , "0")
    ChosenNGPlusBladeCrystalIDs = random.sample(NGPlusBladeCrystalIDs, min(3, len(NGPlusBladeCrystalIDs)))
    ChosenDLCBladeCrystalIDs = random.sample(DLCBladeCrystalIDs, min(3, len(DLCBladeCrystalIDs)))
    ChosenNGPlusBladeCrystalIDs = Helper.ExtendListtoLength(ChosenNGPlusBladeCrystalIDs, 3, "0")
    ChosenDLCBladeCrystalIDs = Helper.ExtendListtoLength(ChosenDLCBladeCrystalIDs, 3, "0")
    Item1IDs.extend(ChosenAtkBlades[:4])
    Item1IDs.extend(ChosenTnkBlades[:3])
    Item1IDs.extend(ChosenHlrBlades[:3])
    Item1IDs.extend(ChosenDLCBladeCrystalIDs[:3])
    Item1IDs.extend(ChosenNGPlusBladeCrystalIDs[:3])
    Item2IDs.extend(ChosenAtkBlades[-4:])
    Item2IDs.extend(ChosenTnkBlades[-3:])
    Item2IDs.extend(ChosenHlrBlades[-3:])
    Item2IDs = Helper.ExtendListtoLength(Item2IDs, 16, "0")
    global OutputCrystalGroupItemIDs
    OutputCrystalGroupItemIDs = [Item1IDs, Item2IDs, Item3IDs, Item4IDs]
    RenameCrystals(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs)
    # Output should be [16, 16, 16, 16] format, with last 2 entries being 0

def RenameCrystals(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs):    
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/ITM_CrystalList.json", ["Condition", "CommonID", "CommonWPN", "CommonAtr", "Price", "RareTableProb", "RareBladeRev", "AssureP"], 0)
    with open("./_internal/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file: # Now we want to rename crystals according to their category
        IDNumbers = Helper.InclRange(16, 20)
        CrystalCategoryNames = ["NG+ Core Crystal", "DLC Core Crystal", "TNK Core Crystal", "ATK Core Crystal", "HLR Core Crystal"]
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": CrystalCategoryNames[i]})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in NGPlusBladeCrystalIDs:
                row["Name"] = 16
            elif row["$id"] in DLCBladeCrystalIDs:
                row["Name"] = 17
            elif row["$id"] in TankBladeCrystalIDs:
                row["Name"] = 18
            elif row["$id"] in AttackerBladeCrystalIDs:
                row["Name"] = 19
            elif row["$id"] in HealerBladeCrystalIDs:
                row["Name"] = 20
            else:
                row["Name"] = 12
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def WPAdjustments(): # Changes how much a weapon manual gives, and how much is needed to max an art
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP2"], 250) # 250 to upgrade each level
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP3"], 250)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP4"], 250)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP5"], 250)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 25405:
                row["Type"] = 250 # Changed the amount of WP it gives to 250
                continue
            if row["$id"] == 25406:
                row["Type"] = 500
                continue
            if row["$id"] == 25407:
                row["Type"] = 1000
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of WP Boosting Items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 715:
                row["name"] = "250 WP Booster"
                continue
            if row["$id"] == 716:
                row["name"] = "500 WP Booster"
                continue
            if row["$id"] == 717:
                row["name"] = "1000 WP Booster"
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ChipShopRewards():
    ChipStrengthLists = Helper.ExtendListtoLength([], 20, "[]")
    global ChipBundleNames
    Chips1, Chips2, Chips3, Chips4, ChipBundleNames = [], [], [], Helper.ExtendListtoLength([], 16, "0"), []
    with open("./_internal/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            ChipStrengthLists[row["Rank"] - 1].append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(0, 16):
        if i <= 13:
            chosenrewards = random.choices(ChipStrengthLists[i] + ChipStrengthLists[i+1], weights= Helper.ExtendListtoLength([], len(ChipStrengthLists[i]), "2")+ Helper.ExtendListtoLength([], len(ChipStrengthLists[i+1]), "1"), k = 3)
        elif i == 14:
            chosenrewards = random.choices(ChipStrengthLists[15] + ChipStrengthLists[16], weights= Helper.ExtendListtoLength([], len(ChipStrengthLists[15]), "2")+ Helper.ExtendListtoLength([], len(ChipStrengthLists[16]), "1"), k = 3)    
        elif i == 15:
            chosenrewards = random.choices(ChipStrengthLists[17] + ChipStrengthLists[18], weights= Helper.ExtendListtoLength([], len(ChipStrengthLists[17]), "2")+ Helper.ExtendListtoLength([], len(ChipStrengthLists[18]), "1"), k = 3)    
        else:
            chosenrewards = random.choices(ChipStrengthLists[19] + ChipStrengthLists[20], weights= Helper.ExtendListtoLength([], len(ChipStrengthLists[19]), "2")+ Helper.ExtendListtoLength([], len(ChipStrengthLists[20]), "1"), k = 3) 
        Chips1.append(chosenrewards[0])
        Chips2.append(chosenrewards[1])
        Chips3.append(chosenrewards[2])
    global ChipShopRewardDistribution
    ChipShopRewardDistribution = [Chips1, Chips2, Chips3, Chips4]
    for i in range(0, 16):
        ChipBundleNames.append(f"Chip Bundle {i+1}")

def WeaponPowerLevel(): # Assigns appropriately powered enhancement and damage value based on rank of weapon
    WeaponStrengthList = Helper.ExtendListtoLength([], 20, "[]")
    WeaponDamageRanges = [[14, 31], [26, 61], [49, 117], [86, 184], [123, 248], [160, 324], [197, 409], [243, 480], [275, 544], [307, 588], [332, 639], [360, 695], [387, 746], [421, 811], [470, 872], [501, 919], [527, 967], [549, 990], [553, 1037], [592, 1108]]
    InvalidSkillEnhancements = [ArtCancel,EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, BladeSwapDamage, CatScimPowerUp, EvadeDrainHp, EvadeDriverArt, EtherCannonRange,ArtDamageHeal, DreamOfTheFuture, WPEnemiesBoost, ExpEnemiesBoost]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    Common, Rare, Legendary = 0, 1, 2
    with open("./_internal/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            for i in range(1, 37):
                WeaponStrengthList[row["Rank"] - 1].append(row[f"CreateWpn{i}"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(WeaponStrengthList)):
                if row["$id"] in WeaponStrengthList[i]:
                    row["Damage"] = random.randrange(WeaponDamageRanges[i][0], WeaponDamageRanges[i][1])
                    if row["Rank"] <= 7:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Common)
                        row["Enhance1"] = curEnh.id
                    elif row["Rank"] <= 14:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Rare)
                        row["Enhance1"] = curEnh.id
                    else:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Legendary)
                        row["Enhance1"] = curEnh.id
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AuxCoreRewards(): # Makes the Aux Core Bundles
    AuxCoreSkillGroups = {
        "Common": {
            "Damage": [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, BladeComboDamUp, FusionComboDamUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp, LV1Damage, LV2Damage, LV3Damage, LV4Damage],
            "Defensive": [HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, AffinityMaxBarrier, AffinityMaxEvade, LowHPRegen, AllDebuffRes, BladeArtsTriggerUp, BladeArtDuration],
            "Playstyle Defining": [SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat]
        },
        "Rare": {
            "Damage": [IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, PartyDamageMaxAffinity, PartyCritMaxAffinity, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp],
            "Defensive": [HunterChem, ShoulderToShoulder, WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, FlatHPBoost],
            "Playstyle Defining": [CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill]
        },
        "Legendary": {
            "Damage": [KaiserZone, AffinityMaxAttack, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, DamageAndCritUpMaxAffinity, FlatCritBoost],
            "Defensive": [PartyDamageReducMaxAffinity, PhyAndEthDefenseUp, ReduceEnemyChargeMaxAffinity, GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatBlockBoost],
            "Playstyle Defining": [RecoverRechargeCrit, DealMoreTakeLessMaxAffinity, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, HealingUpMaxAffinity, TakeDamageHeal, StopThinking, ChainAttackPower, DamagePerEvadeUp]
        }
    }

    Common, Rare, Legendary = 0, 1, 2

    ChosenAuxCores = {
        Common: {
            "Damage": random.sample(AuxCoreSkillGroups["Common"]["Damage"], 16),
            "Defensive": random.sample(AuxCoreSkillGroups["Common"]["Defensive"], 8),
            "Playstyle Defining": random.sample(AuxCoreSkillGroups["Common"]["Playstyle Defining"], 4)
        },
        Rare: {
            "Damage": random.sample(AuxCoreSkillGroups["Rare"]["Damage"], 8),
            "Defensive": random.sample(AuxCoreSkillGroups["Rare"]["Defensive"], 8),
            "Playstyle Defining": random.sample(AuxCoreSkillGroups["Rare"]["Playstyle Defining"], 4)
        },
        Legendary: {
            "Damage": random.sample(AuxCoreSkillGroups["Legendary"]["Damage"], 4),
            "Defensive": random.sample(AuxCoreSkillGroups["Legendary"]["Defensive"], 4),
            "Playstyle Defining": random.sample(AuxCoreSkillGroups["Legendary"]["Playstyle Defining"], 8)
        }
    }

    with open("./_internal/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./_internal/JsonOutputs/common_ms/itm_orb.json", 'r+', encoding='utf-8') as namefile:
            
            namedata = json.load(namefile) 
            data = json.load(file)

            CurRow = 1
            for rarity in ChosenAuxCores:
                for category in ChosenAuxCores[rarity]:
                    for auxCore in ChosenAuxCores[rarity][category]:
                        for row in data["rows"]:
                            if row["$id"] == CurRow + 17000:
                                curAuxCore:Enhancement = auxCore
                                curAuxCore.RollEnhancement(rarity)
                                row["Enhance"] = curAuxCore.id
                                row["Rarity"] = curAuxCore.Rarity
                                row["EnhanceCategory"] = CurRow
                                CurName = row["Name"]
                                CurRow += 1
                                break
                        for namerow in namedata["rows"]:  
                            if namerow["$id"] == CurName:    
                                namerow["name"] = f"{curAuxCore.name} Core"
                                break
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    global AuxCoreShopRewardDistribution
    AuxCoreShopRewardDistribution = [Helper.ExtendListtoLength([17001], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([17002], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([17003], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([17004], 16, "inputlist[i-1]+4")]

def PouchItemRewards():
    global PouchItemShopRewardDistribution
    PouchItemShopRewardDistribution = [[],[],[],[]]
    with open("./_internal/JsonOutputs/common/ITM_FavoriteList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for i in range(0, 4):
            for j in range(0, 4):
                PouchItemShopRewardDistribution[i].append(random.choice(ValidPouchItems))
        for i in range(12, 24):
            CurrentItemTypeList = []
            for row in data["rows"]:
                if (row["Category"] == i) & (row["$id"] in ValidPouchItems):
                    CurrentItemTypeList.append(row["$id"])
            ChosenItems = random.sample(CurrentItemTypeList, 2)
            PouchItemShopRewardDistribution[0].append(ChosenItems[0])
            PouchItemShopRewardDistribution[1].append(ChosenItems[1])
        PouchItemShopRewardDistribution[2] = Helper.ExtendListtoLength(PouchItemShopRewardDistribution[2], 16, "0")
        PouchItemShopRewardDistribution[3] = Helper.ExtendListtoLength(PouchItemShopRewardDistribution[2], 16, "0")    
        for row in data["rows"]: # Change the duration of all to 60 minutes, and they all give no trust points
            row["Time"] = 60
            row["ValueMax"] = 10
            row["TrustPoint"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AccessoryShopRewards(): # Creates the accessory shop
    AccessorySkillGroups = {
        "Common": {
            "Damage": [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp],
            "Defensive": [HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, LowHPRegen, AllDebuffRes, TastySnack, HPBoost, DoomRes, TauntRes, BladeShackRes, DriverShackRes],
            "Playstyle Defining": [SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat]
        },
        "Rare": {
            "Damage": [IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp, BladeSwitchDamageUp, BreakResDown],
            "Defensive": [WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, FlatHPBoost, ArtUseHeal, AgiBoost, PhysDefBoost, EthDefBoost],
            "Playstyle Defining": [CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill]
        },
        "Legendary": {
            "Damage": [KaiserZone, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, FlatStrengthBoost, FlatEtherBoost],
            "Defensive": [PhyAndEthDefenseUp, GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatAgiBoost, FlatDefBoost, FlatEthDefBoost],
            "Playstyle Defining": [RecoverRechargeCrit, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, TakeDamageHeal, DamagePerEvadeUp, PartyHealBladeSwitch]
        }
    }

    Common, Rare, Legendary = 0, 1, 2

    ChosenAccessories = {
        Common: {
            "Damage": random.sample(AccessorySkillGroups["Common"]["Damage"], 16),
            "Defensive": random.sample(AccessorySkillGroups["Common"]["Defensive"], 8),
            "Playstyle Defining": random.sample(AccessorySkillGroups["Common"]["Playstyle Defining"], 4)
        },
        Rare: {
            "Damage": random.sample(AccessorySkillGroups["Rare"]["Damage"], 8),
            "Defensive": random.sample(AccessorySkillGroups["Rare"]["Defensive"], 8),
            "Playstyle Defining": random.sample(AccessorySkillGroups["Rare"]["Playstyle Defining"], 4)
        },
        Legendary: {
            "Damage": random.sample(AccessorySkillGroups["Legendary"]["Damage"], 4),
            "Defensive": random.sample(AccessorySkillGroups["Legendary"]["Defensive"], 4),
            "Playstyle Defining": random.sample(AccessorySkillGroups["Legendary"]["Playstyle Defining"], 8)
        }
    }

    AccessoryTypesandNames = { # What icon should go with what noun:
        0:["Sandals", "Crocs", "Jordans", "Boots", "Sneakers"], 
        1:["Baseball Cap", "Sweatband", "Beanie", "Earmuffs"], 
        2:["Vest", "Tuxedo", "T-Shirt", "Tank Top", "Jacket"], 
        3:["Choker", "Necklace", "Locket", "Tie"], 
        4:["Belt", "Sash", "Scarf"], 
        5:["Banner", "Loincloth", "Swimsuit", "Thread", "Lamp", "Incense"], 
        6:["Gloves", "Silly Bandz", "Gauntlets", "Bangles", "Watches"],
        7:["Cube", "AirPods", "Headphones", "Hard Drive", "Attachment"],
        8:["Garnet", "Sapphire", "Diamond", "Ruby", "Emerald", "Prismarine"],
        9:["Feather", "Medal", "Bling"]
    }

    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as namefile:
            
            namedata = json.load(namefile) 
            data = json.load(file)
            
            CurRow = 1
            for rarity in ChosenAccessories:
                for category in ChosenAccessories[rarity]:
                    for accessory in ChosenAccessories[rarity][category]:
                        for row in data["rows"]:
                            if row["$id"] == CurRow:
                                curAccessory:Enhancement = accessory
                                curAccessory.RollEnhancement(rarity)
                                row["Enhance1"] = curAccessory.id
                                row["Rarity"] = curAccessory.Rarity
                                ItemType = random.randint(0,9)
                                row["Icon"] = ItemType
                                CurName = row["Name"]
                                CurRow += 1
                                break
                        for namerow in namedata["rows"]:  
                            if namerow["$id"] == CurName:
                                lastWord = random.choice(AccessoryTypesandNames[ItemType])
                                namerow["name"] = f"{curAccessory.name} {lastWord}"
                                break
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    global AccessoryShopRewardDistribution
    AccessoryShopRewardDistribution = [Helper.ExtendListtoLength([1], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([2], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([3], 16, "inputlist[i-1]+4"), Helper.ExtendListtoLength([4], 16, "inputlist[i-1]+4")]

def PoppiswapShopRewards(): # Creates rewards for Poppiswap Shop
    CrystalRows = Helper.InclRange(27, 37)
    StartingCondListRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingItemCondRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionItem.json", "$id") + 1
    StartingDLCItemTextRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    CrystalVoucherNameIDs = Helper.InclRange(633, 643)
    CrystalVoucherCaptionIDs = Helper.InclRange(734, 744)
    with open("./_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 11): # ConditionType of 5 is "Item", meaning you need that item listed in FLD_ConditionItem
            data["rows"].append({"$id": StartingCondListRow + i, "Premise": 0, "ConditionType1": 5, "Condition1": StartingItemCondRow + i, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_ConditionItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 11):
            data["rows"].append({"$id": StartingItemCondRow + i, "ItemCategory": 0, "ItemID": 25322 + i, "Number": 1})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 633:
                for i in range(0, len(CrystalVoucherNameIDs)):
                    if row["$id"] == CrystalVoucherNameIDs[i]:
                        row["name"] = f"Ether Crystal Pack {i+1}"
                    if row["$id"] == CrystalVoucherCaptionIDs[i]:
                        row["name"] = f"Unlocks a DLC {1000*(i+1)} Ether Crystal Reward"
            if row["$id"] >= 745:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in CrystalRows:
                row["releasecount"] = 2
                row["item_id"] = 0
                row["category"] = 3
                row["value"] = 1000*(row["$id"] - 26)
                row["disp_item_info"] = 0
                row["condition"] = StartingCondListRow + (row["$id"] - 27)
                row["title"] = StartingDLCItemTextRow + (row["$id"] - 27)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, 11):
            data["rows"].append({"$id": StartingDLCItemTextRow + i, "style": 162, "name": f"Poppiswap Crafting Materials Rank {i+1}"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PoppiswapCostChanges(): # Reduces cost of poppiswap stuff
    Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/ITM_HanaArtsEnh.json","./_internal/JsonOutputs/common/ITM_HanaAssist.json", "./_internal/JsonOutputs/common/ITM_HanaAtr.json", "./_internal/JsonOutputs/common/ITM_HanaNArtsSet.json", "./_internal/JsonOutputs/common/ITM_HanaRole.json"], ["NeedEther", "DustEther"], ['max(row[key] // 4, 1)'])
    Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_HanaPower.json"], ["EtherNum1", "EtherNum2", "EtherNum3"], ['max(row[key] // 4, 1)'])
    Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_HanaBase.json"], ["Circuit4Num", "Circuit5Num", "Circuit6Num"], ['max(row[key] // 10, 1)'])

def GambaShopRewards(): # Makes the rewards for the gamba shop
    GambaCouponRows = Helper.InclRange(11, 26)
    StartingCondListRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingItemCondRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_ConditionItem.json", "$id") + 1
    StartingDLCItemTextRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    GambaVoucherNameIDs = Helper.InclRange(644, 659)
    GambaVoucherCaptionIDs = Helper.InclRange(745, 760)
    global ShopTokenRewardResults
    ShopTokenRewardResults = random.choices([1, 3, 5, 8, 10, 15, 25], weights=[30, 20, 15, 15, 10, 5, 5], k = 16) # 50% chance to lose tokens, 50% chance to make winnings back + some in theory, but can be better or worse depending on rolled values
    with open("./_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 16): # ConditionType of 5 is "Item", meaning you need that item listed in FLD_ConditionItem
            data["rows"].append({"$id": StartingCondListRow + i, "Premise": 0, "ConditionType1": 5, "Condition1": StartingItemCondRow + i, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_ConditionItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 16):
            data["rows"].append({"$id": StartingItemCondRow + i, "ItemCategory": 0, "ItemID": 25333 + i, "Number": 1})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 644:
                for i in range(0, len(GambaVoucherNameIDs)):
                    if row["$id"] == GambaVoucherNameIDs[i]:
                        row["name"] = f"Mystery Voucher {i+1}"
                    if row["$id"] == GambaVoucherCaptionIDs[i]:
                        row["name"] = f"Unlocks the corresponding\n [System:Color name=tutorial]Doubloon[/System:Color] Booster Pack."
            if row["$id"] >= 761:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, len(GambaCouponRows)):
            for row in data["rows"]:
                if row["$id"] == GambaCouponRows[i]:
                    row["releasecount"] = 3
                    row["item_id"] = 25489
                    row["category"] = 1
                    row["value"] = ShopTokenRewardResults[i]
                    row["disp_item_info"] = 0
                    row["condition"] = StartingCondListRow + i
                    row["title"] = StartingDLCItemTextRow + i
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, 16):
            data["rows"].append({"$id": StartingDLCItemTextRow + i, "style": 162, "name": f"[System:Color name=tutorial]Doubloon[/System:Color] Booster Pack {i+1}"})
        for row in data["rows"]:
            if row["$id"] == 8:
                row["name"] = "[System:Color name=green]Bounty Token[/System:Color] Rewards"
            if row["$id"] == 9:
                row["name"] = "Poppiswap Crafting Materials"
            if row["$id"] == 38:
                row["name"] = "[System:Color name=tutorial]Doubloon[/System:Color] Booster Packs"
            if row["$id"] == 10:
                row["name"] = "Junk"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    global GambaShopRewardList
    GambaShopRewardList = Helper.ExtendListtoLength([25333], 16, "inputlist[i-1] + 1")
    random.shuffle(GambaShopRewardList)

def AddDLCRewards():
    BountyCollectionRewards = Helper.InclRange(1, 10)
    StartingDLCItemTextRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    with open("./_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, len(BountyCollectionRewards)):
            for row in data["rows"]:
                if row["$id"] == BountyCollectionRewards[i]:
                    row["releasecount"] = 1
                    row["item_id"] = 25479 + i
                    row["category"] = 1
                    row["value"] = 4
                    row["disp_item_info"] = 0
                    row["condition"] = 3904 + i
                    row["title"] = StartingDLCItemTextRow + i
                    break
        del data["rows"][37:]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, 10):
            data["rows"].append({"$id": StartingDLCItemTextRow + i, "style": 162, "name": f"[System:Color name=green]Bounty Token[/System:Color] Rewards, Set {i+1}"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AddSPManual(): # Creates 3 SP Manuals, using ID 25015, 25018, 25033
    SPManualIDs = [25349, 25350, 25351]
    SPManualNameIDs = [660, 661, 662]
    SPManualCaptionIDs = [761, 762, 763]
    SPManualValues = [1500, 3000, 6000]
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes max quantity
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in SPManualIDs:
                row["ValueMax"] == 99
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 660:
                for i in range(0, len(SPManualIDs)):
                    if row["$id"] == SPManualNameIDs[i]:
                        row["name"] = f"{SPManualValues[i]} SP Receipt"
                    if row["$id"] == SPManualCaptionIDs[i]:
                        row["name"] = f"Proof that you purchased {SPManualValues[i]} SP\n for the driver skill trees."
            if row["$id"] >= 764:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CustomShopSetup(): # Sets up the custom shops with loot
    
    # Shop Item Setup
    ReceiptTextChanges()
    WPAdjustments()
    ChipShopRewards()
    AuxCoreRewards()
    PouchItemRewards()
    AccessoryShopRewards()
    PoppiswapShopRewards()
    GambaShopRewards()
    AddSPManual()
    
    # Cost Distributions
    CoreCrystalCostDistribution = [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 8, 10, 12, 25, 35, 45]
    ManualCostDistribution = [1, 2, 4, 8, 12, 2, 4, 8]
    ChipShopCostDistribution = Helper.ExtendListtoLength([2],16,"inputlist[i-1]+2")
    
    CommonAuxCoreCosts = [2, 3, 4, 5, 2, 3, 4]
    RareAuxCoreCosts = [4, 6, 4, 6, 8]
    LegendaryAuxCoreCosts = [10, 10, 15, 15]
    AuxCoreShopCostDistribution = CommonAuxCoreCosts + RareAuxCoreCosts + LegendaryAuxCoreCosts

    PouchItemShopCostDistribution = [2,2,2,2,3,2,2,2,4,4,4,3,3,4,3,2]
    
    CommonAccessoryCosts = [3, 4, 5, 6, 3, 4, 5]
    RareAccessoryCosts = [5, 7, 5, 7, 9]
    LegendaryAccessoryCosts = [12, 12, 18, 18]
    AccessoryShopCostDistribution = CommonAccessoryCosts + RareAccessoryCosts + LegendaryAccessoryCosts

    PoppiswapShopCosts = [2, 4, 8, 16, 24, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    GambaShopCosts = Helper.ExtendListtoLength([], 16, "5")

    # Filler Lists
    TokenFillerList = Helper.ExtendListtoLength([], 10, "0") # This gets used so much, I'd rather not screw up typing it out, also by initializing it here, it doesn't calculate the value every time in the dictionary
    EmptyFillerList = Helper.ExtendListtoLength([], 16, "0") # Empty list of full size
    FullFillerList = Helper.ExtendListtoLength([], 16, "1") # Full list of full size
    ManualFillerList = Helper.ExtendListtoLength([], 8, "0") # Empty list for manual shop
    
    # List of Shops
    # Sanity Checks: The number of items in InputTaskIDs should always be less than 16
    # The number of SetItem1IDs, RewardIDs, RewardNames, RewardSP, and RewardXP should all be the same, and also equal to the number of non-zero InputTaskIDs
    # Reward IDs, RewardQtys should have same number of values in each list as SetItem1IDs, however, each list should be made up of 4 lists, 1 for each item slot that a reward can be

    TokenExchangeShop = {
        "NPCModel": 2002, # from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Bana
        "NPCID": 2079, # ma02a_FLD_NpcPop $id
        "ShopIcon": 420, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 18, # MNU_ShopList $id
        "ShopNametoReplace": 9, # fld_shopname $id
        "ShopEventID": 40045, # ma02a_FLD_NpcPop EventID
        "Name": "[System:Color name=green]Bounty Token[/System:Color] Bartering", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(917, 926), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8.
        "AddTaskConditions": [1, 1], # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s,
        "SetItemIDs": [Helper.InclRange(25479, 25488), TokenFillerList, TokenFillerList, TokenFillerList, TokenFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [Helper.ExtendListtoLength([], 10, "1"), TokenFillerList, TokenFillerList, TokenFillerList, TokenFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1282, 1291), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": [Helper.ExtendListtoLength([], 10, "25489"), TokenFillerList, TokenFillerList, TokenFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [[2,3,4,5,6,7,8,9,10,11], TokenFillerList, TokenFillerList, TokenFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["Doubloon (x2)", "Doubloon (x3)", "Doubloon (x4)", "Doubloon (x5)", "Doubloon (x6)", "Doubloon (x7)", "Doubloon (x8)", "Doubloon (x9)", "Doubloon (x10)", "Doubloon (x11)"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": [650, 1250, 1875, 2500, 3125, 3750, 4375, 5000, 5625, 6250], #FLD_QuestReward Sp
        "RewardXP": [0, 630, 630, 630, 630, 630, 630, 630, 630, 630], # FLD_QuestReward EXP
        "HideReward": TokenFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    CoreCrystalShop = {
        "NPCModel": 2008,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Amalthus
        "NPCID": 2080, # ma02a_FLD_NpcPop $id
        "ShopIcon": 427, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 17, # MNU_ShopList $id
        "ShopNametoReplace": 8, # fld_shopname $id
        "ShopEventID": 40054, # ma02a_FLD_NpcPop EventID
        "Name": "Core Crystal Cache", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(927, 942), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [CoreCrystalCostDistribution, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1292, 1307), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": OutputCrystalGroupItemIDs, # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, FullFillerList, FullFillerList, EmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["ATK Blade Bundle 1", "ATK Blade Bundle 2", "ATK Blade Bundle 3", "ATK Blade Bundle 4", "TNK Blade Bundle 1", "TNK Blade Bundle 2", "TNK Blade Bundle 3", "HLR Blade Bundle 1", "HLR Blade Bundle 2", "HLR Blade Bundle 3", "DLC Core Crystal 1", "DLC Core Crystal 2", "DLC Core Crystal 3", "NG+ Core Crystal 1", "NG+ Core Crystal 2", "NG+ Core Crystal 3"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": EmptyFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    WPManualShop = {
        "NPCModel": 2001,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Gramps
        "NPCID": 2086, # ma02a_FLD_NpcPop $id
        "ShopIcon": 442, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 24, # MNU_ShopList $id
        "ShopNametoReplace": 16, # fld_shopname $id
        "ShopEventID": 40051, # ma02a_FLD_NpcPop EventID
        "Name": "Manual Marketplace", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(943, 950), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": [], # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 8, "25489"), ManualFillerList, ManualFillerList, ManualFillerList, ManualFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [ManualCostDistribution, ManualFillerList, ManualFillerList, ManualFillerList, ManualFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1308, 1315), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": [[25405, 25406, 25407, 25305, 25450, 25349, 25350, 25351], ManualFillerList, ManualFillerList, ManualFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [Helper.ExtendListtoLength([], 8, "1"), ManualFillerList, ManualFillerList, ManualFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["250 Art WP", "500 Art WP", "1000 Art WP", "Pouch Expander", "Accessory Expander", "1500 Driver SP", "3000 Driver SP", "6000 Driver SP"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": ManualFillerList, #FLD_QuestReward Sp
        "RewardXP": ManualFillerList, # FLD_QuestReward EXP
        "HideReward": ManualFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    WeaponChipShop = {
        "NPCModel": 3457,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Padraig
        "NPCID": 2087, # ma02a_FLD_NpcPop $id
        "ShopIcon": 430, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 21, # MNU_ShopList $id
        "ShopNametoReplace": 13, # fld_shopname $id
        "ShopEventID": 40048, # ma02a_FLD_NpcPop EventID
        "Name": "Weapon Warehouse", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(951, 966), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [ChipShopCostDistribution, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1316, 1331), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": ChipShopRewardDistribution, # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, FullFillerList, FullFillerList, EmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ChipBundleNames, # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": EmptyFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    AuxCoreShop = {
        "NPCModel": 3106,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Yumyum the Burglar
        "NPCID": 2088, # ma02a_FLD_NpcPop $id
        "ShopIcon": 432, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 26, # MNU_ShopList $id
        "ShopNametoReplace": 17, # fld_shopname $id
        "ShopEventID": 40052, # ma02a_FLD_NpcPop EventID
        "Name": "Aux Core Auction", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(967, 982), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [AuxCoreShopCostDistribution, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1332, 1347), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": AuxCoreShopRewardDistribution, # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, FullFillerList, FullFillerList, FullFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["[System:Color name=blue]Common[/System:Color] Damage 1", "[System:Color name=blue]Common[/System:Color] Damage 2", "[System:Color name=blue]Common[/System:Color] Damage 3", "[System:Color name=blue]Common[/System:Color] Damage 4", "[System:Color name=blue]Common[/System:Color] Defense 1", "[System:Color name=blue]Common[/System:Color] Defense 2", "[System:Color name=blue]Common[/System:Color] Unique", "[System:Color name=red]Rare[/System:Color] Damage 1", "[System:Color name=red]Rare[/System:Color] Damage 2", "[System:Color name=red]Rare[/System:Color] Defense 1", "[System:Color name=red]Rare[/System:Color] Defense 2", "[System:Color name=red]Rare[/System:Color] Unique", "[System:Color name=tutorial]Legendary[/System:Color] Damage", "[System:Color name=tutorial]Legendary[/System:Color] Defense", "[System:Color name=tutorial]Legendary[/System:Color] Unique 1", "[System:Color name=tutorial]Legendary[/System:Color] Unique 2"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": FullFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    PouchItemShop = {
        "NPCModel": 2534,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Head Fire Dragon
        "NPCID": 2092, # ma02a_FLD_NpcPop $id
        "ShopIcon": 426, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 114, # MNU_ShopList $id
        "ShopNametoReplace": 113, # fld_shopname $id
        "ShopEventID": 40731, # ma02a_FLD_NpcPop EventID
        "Name": "Pouch Item Patisserie", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(983, 998), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [PouchItemShopCostDistribution, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1348, 1363), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": PouchItemShopRewardDistribution, # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [Helper.ExtendListtoLength([1,1,1,1], 16, "2"), Helper.ExtendListtoLength([1,1,1,1], 16, "2"), Helper.ExtendListtoLength([1,1,1,1], 16, "0"), Helper.ExtendListtoLength([1,1,1,1], 16, "0")], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["Mystery Set 1", "Mystery Set 2", "Mystery Set 3", "Mystery Set 4", "Staple Foods", "Vegetables", "Meat", "Seafood", "Desserts", "Drinks", "Instruments", "Art", "Literature", "Board Games", "Cosmetics", "Textiles"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": Helper.ExtendListtoLength([1,1,1,1], 16, "0") # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    DriverAccessoryShop = {
        "NPCModel": 2031,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Yew
        "NPCID": 2097, # ma02a_FLD_NpcPop $id
        "ShopIcon": 446, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 23, # MNU_ShopList $id
        "ShopNametoReplace": 15, # fld_shopname $id
        "ShopEventID": 40050, # ma02a_FLD_NpcPop EventID
        "Name": "Excess Accessories", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(999, 1014), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [AccessoryShopCostDistribution, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1364, 1379), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": AccessoryShopRewardDistribution, # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, FullFillerList, FullFillerList, FullFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["[System:Color name=blue]Common[/System:Color] Damage 1", "[System:Color name=blue]Common[/System:Color] Damage 2", "[System:Color name=blue]Common[/System:Color] Damage 3", "[System:Color name=blue]Common[/System:Color] Damage 4", "[System:Color name=blue]Common[/System:Color] Defense 1", "[System:Color name=blue]Common[/System:Color] Defense 2", "[System:Color name=blue]Common[/System:Color] Unique", "[System:Color name=red]Rare[/System:Color] Damage 1", "[System:Color name=red]Rare[/System:Color] Damage 2", "[System:Color name=red]Rare[/System:Color] Defense 1", "[System:Color name=red]Rare[/System:Color] Defense 2", "[System:Color name=red]Rare[/System:Color] Unique", "[System:Color name=tutorial]Legendary[/System:Color] Damage", "[System:Color name=tutorial]Legendary[/System:Color] Defense", "[System:Color name=tutorial]Legendary[/System:Color] Unique 1", "[System:Color name=tutorial]Legendary[/System:Color] Unique 2"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": FullFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    PoppiswapShop = {
        "NPCModel": 3576,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Soosoo
        "NPCID": 2182, # ma02a_FLD_NpcPop $id
        "ShopIcon": 433, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 16, # MNU_ShopList $id
        "ShopNametoReplace": 7, # fld_shopname $id
        "ShopEventID": 40058, # ma02a_FLD_NpcPop EventID
        "Name": "The Poppishop", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(1015, 1030), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [PoppiswapShopCosts, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1380, 1395), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": [Helper.ExtendListtoLength(Helper.ExtendListtoLength([25218], 5, "inputlist[i-1]+1") + [25322], 16, "inputlist[i-1]+1"), EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["Poppiswap Manual 1", "Poppiswap Manual 2", "Poppiswap Manual 3", "Poppiswap Manual 4", "Poppiswap Manual 5", "Ether Crystal Pack 1", "Ether Crystal Pack 2", "Ether Crystal Pack 3", "Ether Crystal Pack 4", "Ether Crystal Pack 5", "Ether Crystal Pack 6", "Ether Crystal Pack 7", "Ether Crystal Pack 8", "Ether Crystal Pack 9", "Ether Crystal Pack 10", "Ether Crystal Pack 11"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": EmptyFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    GambaShop = {
        "NPCModel": 3324,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Generic Mercenary
        "NPCID": 2188, # ma02a_FLD_NpcPop $id
        "ShopIcon": 443, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 27, # MNU_ShopList $id
        "ShopNametoReplace": 18, # fld_shopname $id
        "ShopEventID": 40053, # ma02a_FLD_NpcPop EventID
        "Name": "The [System:Color name=tutorial]Casino[/System:Color]", # fld_shopname name
        "InputTaskIDs": Helper.InclRange(1031, 1046), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
        "AddTaskConditions": Helper.ExtendListtoLength([], 8, "1"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        "SetItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "SetItemQtys": [GambaShopCosts, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardIDs": Helper.InclRange(1396, 1411), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        "RewardItemIDs": [GambaShopRewardList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": Helper.ExtendListtoLength(["Reward Voucher"], 16, "inputlist[0] + ' ' + str(i + 1)"), # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": FullFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    ShopList = [TokenExchangeShop, CoreCrystalShop, WPManualShop, WeaponChipShop, AuxCoreShop, PouchItemShop, DriverAccessoryShop, PoppiswapShop, GambaShop]
    ShopCreator(ShopList, True)

def ShopCreator(ShopList: list, DeleteArgentumShops: bool): # Makes the shops
    with open("./_internal/JsonOutputs/common/MNU_ShopChange.json", 'r+', encoding='utf-8') as file: # Adds the exchange tasks
        data = json.load(file)
        ShopChangeStartRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1 # used in MNU_ShopList for "TableID"
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1
        for shop in ShopList:
            ShopChangeRowToAdd = {"$id": CurrRow, "DefTaskSet1": 0, "DefTaskSet2": 0, "DefTaskSet3": 0, "DefTaskSet4": 0, "DefTaskSet5": 0, "DefTaskSet6": 0, "DefTaskSet7": 0, "DefTaskSet8": 0, "AddTaskSet1": 0, "AddCondition1": 0, "AddTaskSet2": 0, "AddCondition2": 0, "AddTaskSet3": 0, "AddCondition3": 0, "AddTaskSet4": 0, "AddCondition4": 0, "AddTaskSet5": 0, "AddCondition5": 0, "AddTaskSet6": 0, "AddCondition6": 0, "AddTaskSet7": 0, "AddCondition7": 0, "AddTaskSet8": 0, "AddCondition8": 0, "LinkQuestTask": 0, "LinkQuestTaskID": 0, "UnitText": 0}
            for i in range(0, len(shop["InputTaskIDs"])):
                if i <= 7:
                    ShopChangeRowToAdd[f"DefTaskSet{i+1}"] = shop["InputTaskIDs"][i]
                else: # once we get past all the regular tasks, we add new ones to addtaskset instead
                    ShopChangeRowToAdd[f"AddTaskSet{i-7}"] = shop["InputTaskIDs"][i]
                    ShopChangeRowToAdd[f"AddCondition{i-7}"] = shop["AddTaskConditions"][i-8]
            data["rows"].append(ShopChangeRowToAdd)
            CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_shopchange.json", 'r+', encoding='utf-8') as file: # Changes the reward name for the token shop
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1
        StartingShopChangeNameRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1 # Used in MNU_ShopChangeTask for "Name"
        for shop in ShopList:
            for reward in shop["RewardNames"]:
                data["rows"].append({"$id": CurrRow, "style": 36, "name": reward})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file: # Now we define what each task does
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["SetItemIDs"][0])):
                data["rows"].append({"$id": CurrRow, "Name": StartingShopChangeNameRow, "SetItem1": shop["SetItemIDs"][0][i], "SetNumber1": shop["SetItemQtys"][0][i], "SetItem2": shop["SetItemIDs"][1][i], "SetNumber2": shop["SetItemQtys"][1][i], "SetItem3": shop["SetItemIDs"][2][i], "SetNumber3": shop["SetItemQtys"][2][i], "SetItem4": shop["SetItemIDs"][3][i], "SetNumber4": shop["SetItemQtys"][3][i], "SetItem5": shop["SetItemIDs"][4][i], "SetNumber5": shop["SetItemQtys"][4][i], "HideReward": shop["HideReward"][i], "Reward": shop["RewardIDs"][i], "HideRewardFlag": 0, "AddFlagValue": 0, "forcequit": 0, "IraCraftIndex": 0})
                CurrRow += 1
                StartingShopChangeNameRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file: # Sets the reward for each task
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_QuestReward.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["RewardIDs"])):
                data["rows"].append({"$id": CurrRow, "Gold": 0, "EXP": shop["RewardXP"][i], "Sp": shop["RewardSP"][i], "Coin": 0, "DevelopZone": 0, "DevelopPoint": 0, "TrustPoint": 0, "MercenariesPoint": 0, "IdeaCategory": 0, "IdeaValue": 0, "ItemID1": shop["RewardItemIDs"][0][i], "ItemNumber1": shop["RewardQtys"][0][i], "ItemID2": shop["RewardItemIDs"][1][i], "ItemNumber2": shop["RewardQtys"][1][i], "ItemID3": shop["RewardItemIDs"][2][i], "ItemNumber3": shop["RewardQtys"][2][i], "ItemID4": shop["RewardItemIDs"][3][i], "ItemNumber4": shop["RewardQtys"][3][i]})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_shopname.json", 'r+', encoding='utf-8') as file: # Adds new shop name to list 
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1
        ShopNameStartingRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1 # used in MNU_ShopList for "Name"
        for i in range(0, len(ShopList)):
            data["rows"].append({"$id": CurrRow, "style": 70, "name": ShopList[i]["Name"]})
            CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: # Changes existing shop to match what we want
        data = json.load(file)
        for i in range(0, len(ShopList)):
            for row in data["rows"]:
                if row["$id"] == ShopList[i]["ShopIDtoReplace"]:
                    row["Name"] = ShopNameStartingRow
                    row["ShopIcon"] = ShopList[i]["ShopIcon"]
                    row["TableID"] = ShopChangeStartRow
                    row["Discount1"] = row["Discount2"] = row["Discount3"] = row["Discount4"] = row["Discount5"] = 0
                    row["ShopType"] = 1
                    ShopChangeStartRow += 1
                    ShopNameStartingRow += 1
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    if DeleteArgentumShops:
        with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] != 2096: # keeps only the inn as a shop in Argentum
                    row["ShopID"] = 0
                    row["flag"]["Talkable"] = 0
                    row["EventID"] = 0
            for i in range(0, len(ShopList)): # gives a specific npc the shop we want
                for row in data["rows"]:
                    if row["$id"] == ShopList[i]["NPCID"]:
                        row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["TimeRange"] = row["Condition"] = row["Mot"] = row["QuestID"] = 0
                        row["ScenarioFlagMax"] = 10048
                        row["flag"]["Talkable"] = 1
                        row["EventID"] = ShopList[i]["ShopEventID"]
                        row["ShopID"] = ShopList[i]["ShopIDtoReplace"]
                        row["NpcID"] = ShopList[i]["NPCModel"]
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def SecretShopMaker(ChosenAreaOrder): # Adds some secret shops in the areas of interest
    CreateSecretShopReceipts()
    SecretShopRewardGeneration(ChosenAreaOrder)
    UsableShopEventIDs = [40338, 40441, 40339, 40442, 40340, 40443, 40444, 40445, 40446, 41042] # NpcPop EventID
    UsableShopIDs = Helper.InclRange(65, 74) # MNU_ShopList $id, NpcPop ShopID
    UsableShopNames = [66, 51, 72, 52, 68, 53, 54, 55, 56, 57] # MNU_ShopList Name
    SecretEmptyFillerList = Helper.ExtendListtoLength([], 5, "0")
    SecretFullFillerList = Helper.ExtendListtoLength([], 5, "1")
    InputTaskStartingID = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", "$id") + 1
    RewardTaskStartingID = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_QuestReward.json", "$id") + 1
    ShopList = []
    for i in range(0, len(ChosenAreaOrder)):
        MapValidNPCIDs = Helper.FindSubOptionValuesList("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_NpcPop.json", "flag", "Talkable", 1, "$id")
        ChosenSecretNPCID = random.choice(MapValidNPCIDs)
        if i == 0:
            ChosenSecretNPCID = 13024
        with open("./_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == ChosenSecretNPCID:
                    OrigNPCID = row["NpcID"]
                    row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["TimeRange"] = row["Condition"] = row["Mot"] = row["QuestID"] = 0
                    row["ScenarioFlagMax"] = 10048
                    row["EventID"] = UsableShopEventIDs[i]
                    row["ShopID"] = UsableShopIDs[i]
                    row["NpcID"] = 3445 # Traveling Bard from Argentum
                    break
            for row in data["rows"]: # Need to account for more lines where the original NPC speaks, they overlap bodies and it looks weird
                if row["NpcID"] == OrigNPCID:
                    row["NpcID"] = 3445
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        RewardSPList = random.choices([0, 1000, 2000, 3000, 4000], weights = [49, 25, 15, 10, 1], k = 5)
        
        # defining the shop itself

        SecretShop = {
            "NPCModel": 3445,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Soosoo
            "NPCID": ChosenSecretNPCID, # ma02a_FLD_NpcPop $id
            "ShopIcon": 419, # MNU_ShopList ShopIcon
            "ShopIDtoReplace": UsableShopIDs[i], # MNU_ShopList $id
            "ShopNametoReplace": UsableShopNames[i], # fld_shopname $id
            "ShopEventID": UsableShopEventIDs[i], # ma02a_FLD_NpcPop EventID
            "Name": f"[System:Color name=tutorial]Super-Secret Shop {i+1}[/System:Color]", # fld_shopname name
            "InputTaskIDs": Helper.ExtendListtoLength([InputTaskStartingID], 5, "inputlist[i-1]+1"), # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8. Should always have length of 16
            "AddTaskConditions": Helper.ExtendListtoLength([], 8, "0"), # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
            "SetItemIDs": [SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
            "SetItemQtys": [SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
            "RewardIDs": Helper.ExtendListtoLength([RewardTaskStartingID], 5, "inputlist[i-1]+1"), # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
            "RewardItemIDs": [Helper.ExtendListtoLength([SecretReceiptIDs[i]], 5, "inputlist[i-1]"), SecretShopRewardListItem1[i], SecretShopRewardListItem2[i], SecretEmptyFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
            "RewardQtys": [SecretFullFillerList, SecretShopRewardQuantities1[i], SecretShopRewardQuantities2[i], SecretEmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
            "RewardNames": ["Secret Trade 1", "Secret Trade 2", "Secret Trade 3", "Secret Trade 4", "Secret Trade 5"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
            "RewardSP": RewardSPList, #FLD_QuestReward Sp
            "RewardXP": SecretEmptyFillerList, # FLD_QuestReward EXP
            "HideReward": SecretEmptyFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
        }

        print(SecretShop["NPCID"])

        ShopList.append(SecretShop)

        InputTaskStartingID += 5
        RewardTaskStartingID += 5

    ShopCreator(ShopList, False) # run the function on the whole list at once

def CreateSecretShopReceipts(): # Makes receipts for secret shops, limiting the amount of things a player can buy from a shop.
    global SecretReceiptIDs
    SecretReceiptIDs = Helper.ExtendListtoLength([25352], 10, "inputlist[i-1]+1")
    SecretReceiptNameIDs = Helper.ExtendListtoLength([663], 10, "inputlist[i-1]+1")
    SecretReceiptCaptionIDs = Helper.ExtendListtoLength([764], 10, "inputlist[i-1]+1")
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # changes max quantity
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in SecretReceiptIDs:
                row["ValueMax"] = 2
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 663:
                for i in range(0, len(SecretReceiptIDs)):
                    if row["$id"] == SecretReceiptNameIDs[i]:
                        row["name"] = f"Secret Shop Receipt {i+1}"
                    if row["$id"] == SecretReceiptCaptionIDs[i]:
                        row["name"] = f"Proof that you purchased \nan item set from the Secret Shop {i+1}."
            if row["$id"] >= 773:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SecretShopRewardGeneration(ChosenAreaOrder): # Makes the reward sets for the secret shops
    global SecretShopRewardListItem1
    SecretShopRewardListItem1 = []
    global SecretShopRewardListItem2
    SecretShopRewardListItem2 = []
    global SecretShopRewardQuantities1
    SecretShopRewardQuantities1 = [] 
    global SecretShopRewardQuantities2
    SecretShopRewardQuantities2 = []
    
    WeaponRankList = Helper.ExtendListtoLength([], 20, "[]")
    with open("./_internal/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            WeaponRankList[row["Rank"] - 1].append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    RewardTypes = {
        1: "WP Manual", 
        2: "Pouch Item Set",
        3: "Driver Accessory Set",
        4: "Doubloons",
        5: "Weapon Chips",
        6: "Pouch/Accessory Expander",
        7: "Aux Cores"
    }

    # Now assign rewards
    for j in range(0, len(ChosenAreaOrder)):
        SetRewards1 = [0,0,0,0,0]
        SetRewards2 = [0,0,0,0,0]
        SetQuantities1 = [1,1,1,1,1]
        SetQuantities2 = [1,1,1,1,1]
        RewardTypeChoices = random.choices([1, 2, 3, 4, 5, 6, 7], weights = [20, 20, 15, 10, 15, 5, 15], k = 5) # Choose Type of Reward
        for i in range(0, 5): # For each reward,
            if RewardTypeChoices[i] == 1: # WP Manual
                RandomManuals = random.choices([25405, 25406, 25407], weights = [1, 2, 3], k = 2)
                SetRewards1[i] = RandomManuals[0]
                SetRewards2[i] = RandomManuals[1]
            elif RewardTypeChoices[i] == 2: # Pouch Item Set
                RandomPouchItems = random.choices(ValidPouchItems, k = 2)
                SetRewards1[i] = RandomPouchItems[0]
                SetRewards2[i] = RandomPouchItems[1]
            elif RewardTypeChoices[i] == 3: # Driver Accessory Set
                RandomAccessories = random.choices(Helper.InclRange(1, 64), k = 2)
                SetRewards1[i] = RandomAccessories[0]
                SetRewards2[i] = RandomAccessories[1]
            elif RewardTypeChoices[i] == 4: # Doubloons
                SetRewards1[i] = 25489
                SetRewards2[i] = 25489
                DoubloonQuantities = random.choices([1, 3, 5, 8, 10], weights=[30, 25, 20, 15, 10], k = 2)
                SetQuantities1[i] = DoubloonQuantities[0]
                SetQuantities2[i] = DoubloonQuantities[1]
            elif RewardTypeChoices[i] == 5: # Weapon Chips
                RandomWeaponChips = random.choices(WeaponRankList[min((i+1)*2,19)], k = 2)
                SetRewards1[i] = RandomWeaponChips[0]
                SetRewards2[i] = RandomWeaponChips[1]
            elif RewardTypeChoices[i] == 6: # Pouch/Accessory Expander
                RandomPouchorAccessoryExpander = random.choices([25305, 25450], weights = [66, 34], k = 2)
                SetRewards1[i] = RandomPouchorAccessoryExpander[0]
                SetRewards2[i] = RandomPouchorAccessoryExpander[1]
            else: # Aux Cores
                RandomAuxCores = random.choices(Helper.InclRange(17001, 17064), k = 2)
                SetRewards1[i] = RandomAuxCores[0]
                SetRewards2[i] = RandomAuxCores[1]
        SecretShopRewardListItem1.append(SetRewards1)
        SecretShopRewardListItem2.append(SetRewards2)
        SecretShopRewardQuantities1.append(SetQuantities1)
        SecretShopRewardQuantities2.append(SetQuantities2)

def DebugItemsPlace(): #need to place some tokens to play around with them in the shops
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
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