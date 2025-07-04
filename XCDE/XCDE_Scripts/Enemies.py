
import json, random, copy, traceback, math
from XCDE.XCDE_Scripts import Options, IDs
from scripts import Helper, JSONParser, PopupDescriptions
from XCDE.XCDE_Scripts.IDs import *

class Enemy:
    def __init__(self, enelistArea, enelist):
        self.eneListArea = enelistArea
        self.enelist = enelist

OriginalEnemyData = []

instantDeathSpikeThreshold = 60

class ForcedArt:
    def __init__(self, id, artSlot, artId):
        self.id = id
        self.artSlot = artSlot
        self.artId = artId
enAreaFiles = areaFileListNumbers.copy()
enAreaFiles.remove("5001")

def Enemies(monsterTypeList, normal, unique, boss, superboss, odds):
    MetalFace = ForcedArt(61, 2, 565)
    MysteriousFace = ForcedArt(268,5,611)
    GoldFace = ForcedArt(1622, 1, 740)
    DiscipleDickson = ForcedArt(1316, 8, 942)
    Yaldabaoth = ForcedArt(2501, 5, 843)
    YaldabaothThree = ForcedArt(2501, 8, 846)
    YaldabaothTwo = ForcedArt(2123, 1, 828)
    SurenyTelethia = ForcedArt(2601, 1, 870)
    # EnergyDevice = ForcedArt(2506, 1, 848) # Not using since the enemies have removed their limits anyway to account for UM who cant be instakilled
    # EnergyDeviceTwo = ForcedArt(2506, 2, 848)
    GroupEnemies = [135,136,137,138,139]
    selfDestructArts = [1005,1015,1017,1009, 1007, 1013, 396, 406, 915, 408, 812, 814, 400, 923, 1053, 398, 899, 404, 410, 1127, 820] + Helper.InclRange(900, 929)
    ForcedStoryArts = [MetalFace, MysteriousFace, GoldFace, DiscipleDickson, Yaldabaoth, YaldabaothTwo, SurenyTelethia, YaldabaothThree] # (EnemyID, ArtSlots) Needed to make sure when the story requires the enemy to use the ultimate art that ends the fight they actually need an art to use
    isNormal = normal.GetState()
    isUnique = unique.GetState()
    isBoss = boss.GetState()
    isSuper = superboss.GetState()
    odds = odds.GetSpinbox()
    ChosenEnemyIds = []
    if isNormal:
        ChosenEnemyIds.extend(NormalEnemies)
    if isUnique:
        ChosenEnemyIds.extend(UniqueEnemies)
    if isBoss:
        ChosenEnemyIds.extend(BossEnemies)
    if isSuper:
        ChosenEnemyIds.extend(SuperbossEnemies)
    # "run_speed" Do NOT include run speed it lags the game to 1 fps "detects", "assist", "search_range", "search_angle", "frame",  "avoid", "spike_dmg", "spike_state_val"
    CopiedStats = ["move_speed", "size", "scale", "family","elem_phx", "elem_eth", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_state", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]
    CopiedStatsWithRatios = ["str", "eth"] # Not doing agility or hp , "Lv_up_hp", "Lv_up_str", "Lv_up_eth" its too finicky and scales slowly compared to the other stats
    CopiedInfo = ["name", "resource", "c_name_id", "mnu_vision_face"]
    
    # 5001 doesnt have enemies
    enAreaFiles = areaFileListNumbers.copy()
    enAreaFiles.remove("5001")
    
    with open(f"./XCDE/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)    
        
        if OriginalEnemyData == []:
            CreateEnemyDataClass(eneData, enAreaFiles)
            
        filteredEnemyData = OriginalEnemyData.copy() 
        
        # Filter the list so we randomly choose from the enem types we want
        filteredEnemyData = [en for en in filteredEnemyData if en.enelist["$id"] in ChosenEnemyIds]
        
        filteredEnemyDataCopy = filteredEnemyData.copy() # Used to repopulate the list after removing
        
        # Randomly Assign Enemies
        for file in enAreaFiles:
            with open(f"./XCDE/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                with open(f"./XCDE/JsonOutputs/bdat_common/VoEnemy.json", 'r+', encoding='utf-8') as eneVoiceFile:
                    eneVoiceData = json.load(eneVoiceFile)
                    eneAreaData = json.load(eneAreaFile)
                    
                    for enemy in eneAreaData["rows"]:   
                        
                        if not Helper.OddsCheck(odds):
                            continue
                        
                        if enemy["$id"] not in monsterTypeList: # Only want to replace enemies chosen from our groups
                            continue
                                                    
                        chosen:Enemy = random.choice(filteredEnemyData) # Choose an enemy                
                        
                        # if Options.FinalBossOption.GetState() and enemy["$id"] in []: # Choose a valid final boss option
                            
                        VoicedEnemiesFix(eneVoiceData, chosen, enemy)                                
                        SpikeBalancer(enemy, chosen.eneListArea)
                        
                        # Copy stats with ratios to original stats
                        replacementTotalStats = TotalStats(chosen.eneListArea, CopiedStatsWithRatios)
                        originalTotalStats = TotalStats(enemy, CopiedStatsWithRatios)
                        
                        # Copy chosen stats over
                        for key in CopiedStats: 
                            enemy[key] = chosen.eneListArea[key]
                        
                        if (not FirstFights(enemy)) and (enemy["$id"] not in GroupEnemies):
                            for key in CopiedStatsWithRatios:
                                enemy[key] = KeepStatRatio(enemy, chosen.eneListArea, key, replacementTotalStats, originalTotalStats)
                            
                        for ene in eneData["rows"]:
                            if (ene["$id"] == enemy["$id"]):
                                for key in CopiedInfo:
                                    ene[key] = chosen.enelist[key]
                                break
                        
                        TelethiaEarly(enemy, chosen)
                        BossSelfDestructs(enemy, chosen, selfDestructArts)
                        MechonEarly(enemy, chosen, [1,2,4], [30, 31, 32,33, 63, 64, 65]) # Mechon before enchant
                        MechonEarly(enemy, chosen, [2], [67, 68, 68, 66, 69, 70, 71, 134, 138, 138, 138, 139, 138, 138, 138, 139, 269, 269, 266, 265, 267, 267, 268, 327, 326, 328, 326, 338, 339, 341, 340, 340, 416, 417, 422, 421, 421, 420, 534, 636, 636, 636, 637, 638, 906, 905, 907, 908, 909, 909, 1039, 1101, 1103, 1103, 1102, 1102]) # Face mechon before monado shackles released
                        SmallAreaFights(enemy)
                        ForcedArts(enemy, ForcedStoryArts)
                        DevicesAttachedToEgilFix(enemy)
                        
                        # Allows no dupes if possible if we dont have enough choices it reshuffles the original pool
                        filteredEnemyData.remove(chosen)   
                        if filteredEnemyData == []: # repopulate it if the group is empty
                                filteredEnemyData = filteredEnemyDataCopy.copy()

                    JSONParser.CloseFile(eneVoiceData, eneVoiceFile)
                    JSONParser.CloseFile(eneAreaData, eneAreaFile)  
        JSONParser.CloseFile(eneData, eneFile)
        RingRemoval()
        NoCooldownFix()

FinalBossOptions = {
    "Zanza" : [2407,2408,2411],
    "Magestic Mordred": [2227],
    "Despotic Arsene": [548],
    "Avalanche Abaasy": [1448],
    "Blizzard Belgazas": [1449],
    "Final Marcus": [1438],
    "Ancient Daedala": [1733],
    "Immovable Gonzales": [284],
    "Territorial Rotbart": [282]
}
def ChallengingFinalBoss():
    pass

def ForcedArts(enemy, ForcedStoryArts):
    # Fixes boss fights that require the enemy to use an art slot to end the fight 
    for id in ForcedStoryArts:
        if id.id == enemy["$id"]:
            enemy[f"arts{id.artSlot}"] = id.artId  # Change it to their art

def HighActIDFix():
    with open(f"./XCDE/JsonOutputs/bdat_common/ene_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            if art["$id"] == 846:
                art["act_idx"] = 0
                break
        JSONParser.CloseFile(artData, artFile)
    

def VoicedEnemiesFix(eneVoiceData, chosen, enemy):
    newVoiceList = []
    for voiceID in eneVoiceData["rows"]:
        if chosen.enelist["$id"] == voiceID["enemy"]: # If the chosen enemy has a voice
            newVoice = voiceID.copy()
            newVoice["enemy"] = enemy["$id"] # Set the ID
            newVoice["$id"] = len(eneVoiceData["rows"]) + len(newVoiceList) + 1
            newVoiceList.append(newVoice)
            break    
    eneVoiceData["rows"].extend(newVoiceList)

# Big enemies in small areas can break the ai and you cant target them if they go into ceilings (Had this in the two ancient machines fight with a big dragon)
def SmallAreaFights(enemy):
    SmallFights = [30,31, 1617]
    if (enemy["$id"] in SmallFights) and (enemy["size"] >= 4):
        enemy["scale"] = max(int(enemy["scale"] /3),1)

# Create our list of enemies from all the area files and Combine the data into the class
def CreateEnemyDataClass(eneData, enAreaFiles):
    for file in enAreaFiles:  
        with open(f"./XCDE/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
            eneAreaData = json.load(eneAreaFile)
            for enemy in eneAreaData["rows"]:
                # if enemy["$id"] not in ChosenEnemyIds: # Ignore non chosen enemies
                #     continue
                for en in eneData["rows"]:
                    enID = en["$id"]
                    if enID == enemy["$id"]:
                        enemyCopy = copy.copy(enemy)
                        enCopy = copy.copy(en)
                        newEnemy = Enemy(enemyCopy, enCopy)
                        OriginalEnemyData.append(newEnemy)
                        # PrintEnemy(newEnemy)
                        break   
            JSONParser.CloseFile(eneAreaData, eneAreaFile)

# There is no fix for topple spikes always being active just nerfed all spikes instead
def SpikeBalancer(enemy, chosen): # spike damage is 10x the spike_dmg value
    if chosen["spike_dmg"] != 0:
        
        # Get current enemy
        if enemy["lv"] < 20:
            spikePerLv = 0.1 # base spike given per level
        elif enemy["lv"] < 40:
            spikePerLv = 0.2
        else:
            spikePerLv = 0.3
        
        # Get chosens 
        if chosen["lv"] < 20:
            chosenSpikePerLv = 0.2 # base spike given per level
        elif chosen["lv"] < 40:
            chosenSpikePerLv = 0.3
        else:
            chosenSpikePerLv = 0.4
        
        # Run some equations to find a good balance for that level and how strong the spike was
        expectedPowerLv = chosen["lv"] * chosenSpikePerLv # The expected power level of the spike before any changes
        actualPowerLv = chosen["spike_dmg"]
        spikeMult = min(actualPowerLv/expectedPowerLv, 2) # If enemy has a stronger/weaker spike than something of its level make the spike stronger/weaker but still balanced
        # print(spikeMult)
        newPowerLv = int(enemy["lv"] * spikePerLv * spikeMult)
        enemy["spike_dmg"] = max(min(newPowerLv, 255), 1) # Set the new amount between 1 and 255
        # print(f"Level: {enemy["lv"]}")
        # print(f"Spike Damage: {enemy["spike_dmg"] * 10}")
        # print(f"Mult: {spikeMult}")
    if (chosen["spike_state_val"] == 220) and (enemy["lv"] <= instantDeathSpikeThreshold): # Removes instant death spikes from all fights below level 60
        enemy["spike_state_val"] = 0
    else:
        enemy["spike_state_val"] = chosen["spike_state_val"]

def BossSelfDestructs(enemy, chosen:Enemy, selfDestructArts):
    if (enemy["limit"] > 0): # If enemy has a health threshold remove the self destruct art
        for i in range(1,9):
            if enemy[f"arts{i}"] in selfDestructArts:
                enemy[f"arts{i}"] = 0 # Remove self destruct arts 

def TelethiaEarly(enemy, chosen:Enemy):
    TelethiaFamily = 9
    BadForTelethia = [30,31,61,62, 134, 265, 266, 268, 416, 417, 534] # Ids for early game so you dont get soul readed
    if (enemy["$id"] in BadForTelethia) and (chosen.eneListArea["family"] == TelethiaFamily):
        for i in range(1,9):
            if enemy[f"arts{i}"] == 666:
                enemy[f"arts{i}"] = 0 # Remove soul read if we get an early telethia

# The first few fights can be really tough before cheering allies or any arts lets leave their stats vanilla
def FirstFights(enemy):
    EarlyFights = [32, 33, 1501, 1502, 1503]
    if enemy["$id"] in EarlyFights:
        return True
    else:
        return False

def MechonEarly(enemy, chosen, BadFamily = [], BadSpots = [], replacementFamily = 3):
    if (enemy["$id"] in BadSpots) and (chosen.eneListArea["family"] in BadFamily):# 4 Seems to share a lot of enemies that are aquatic, but mumkhar is family 4 and we dont want him early so it cuts a few enemies off that we mightve wanted otherwise oh well
        enemy["family"] = replacementFamily

def TotalStats(chosen, keys):
    total = 0
    for key in keys:
        total += chosen[key]
    return total    
    
def KeepStatRatio(enemy, chosen, key, replacementTotal, originalTotal):
    ratio = chosen[key]/replacementTotal
    origStat = enemy[key]
    newStat = min(math.ceil((ratio*originalTotal)), 65535)
    # print(f"{key}: {origStat} - {newStat}")
    return newStat

# dummylist = []
def PrintEnemy(enemy:Enemy):
    with open(f"./XCDE/JsonOutputs/bdat_common_ms/BTL_enelist_ms.json", 'r+', encoding='utf-8') as enNamesFile:
        with open(f"./XCDE/JsonOutputs/bdat_common_ms/ene_arts_ms.json", 'r+', encoding='utf-8') as enArtNamesFile:
            with open(f"./XCDE/Enemies.txt", 'a', encoding='utf-8') as enemyTXT:
                enemyNameData = json.load(enNamesFile)
                enemyArtNameData = json.load(enArtNamesFile)

                for name in enemyNameData["rows"]:
                    if enemy.enelist["name"] == name["$id"]:
                        # if "Dummy" in name["name"]:#  used to weed out dummy enemies
                        #     dummylist.append(enemy.enelist["$id"])
                        # print(f"Name: {name['name']}")
                        enemyTXT.write(f" Name: {name['name']} ")
                        break
                for name in enemyArtNameData["rows"]:
                    for i in range(1,9):
                        if enemy.eneListArea[f"arts{i}"] == name["$id"]:
                            # print(f"Art {i}: {name['name']}")
                            enemyTXT.write(f" Art {i}: {name['name']} ")
                            break
                enemyTXT.write("\n")
        #     enArtNamesFile.seek(0)
        #     enArtNamesFile.truncate()
        #     json.dump(enemyArtNameData, enArtNamesFile, indent=2, ensure_ascii=False)
        # enNamesFile.seek(0)
        # enNamesFile.truncate()
        # json.dump(enemyNameData, enArtNamesFile, indent=2, ensure_ascii=False)
    
    # with open(f"./XCDE/Enemies.txt", 'a', encoding='utf-8') as enemyTXT: # Clear our enemies file
    #     enemyTXT.seek(0)
    #     enemyTXT.truncate()

# Used for starting fight had some weird thing with the enemies
def RingRemoval():
    RemoveLocks = [2]
    with open(f"./XCDE/JsonOutputs/bdat_ma1401/FieldLock1401.json", 'r+', encoding='utf-8') as lockFile:
        lockData = json.load(lockFile)
        for lock in lockData["rows"]:
            if lock["$id"] in RemoveLocks:
                lock["popID1"] = 0
                lock["popID2"] = 0
        JSONParser.CloseFile(lockData, lockFile)

def NoCooldownFix():
    Cooldowns = [10,15,20,25,30]
    with open(f"./XCDE/JsonOutputs/bdat_common/ene_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            if art["tp"] != 0:
                continue
            if art["recast"] == 0:
                art["recast"] = random.choice(Cooldowns)
        JSONParser.CloseFile(artData, artFile)
    

def DevicesAttachedToEgilFix(enemy):
    if enemy["$id"] == 2506: # Remove the limit on these because unique monsters cannot be inflicted with instant death like their art wants to do
        enemy["limit"] = 0


def EgilArenaFix():
    with open(f"./XCDE/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        enData = json.load(eneFile)
        for en in enData["rows"]:
            if en["$id"] == 2501:
                en["resource"] = 486
                break
        JSONParser.CloseFile(enData, eneFile)
    
    # if enemy["$id"] == 2501 and chosen.enelist["$id"] != 2501: # If egil is randomized into not egil we need to move him
    #     with open(f"./XCDE/JsonOutputs/bdat_ma2301/poplist2301.json", 'r+', encoding='utf-8') as enpopFile:
    #         popData = json.load(enpopFile)
    #         for en in popData["rows"]:
    #             if en["$id"] == 2:
    #                 en["posX"] = 5
    #                 en["posY"] = 0
    #         JSONParser.CloseFile(popData, enpopFile)
  
        
def EnemyDesc(categoryName):
    myDesc = PopupDescriptions.Description()
    myDesc.Header(categoryName)
    myDesc.Text(f"Randomizes the chosen categories of enemies onto {categoryName}.")
    myDesc.Text("There is various logic to prevent bad situations:", anchor="w")
    myDesc.Tag("Enemy stats do not scale with level in this game, so instead it takes the original enemies stat total and distributes it in the replacement enemies stat ratios.\nSo, if an enemy has a high attack stat compared to their other stats, they will still have a high attack stat but balanced with the replacement enemies' stats", pady=(5,5))
    myDesc.Tag("Mechon Enemies have their resistances removed for forced fights before you can damage mechon, toppling is not guaranteed with art randomization so this fix is needed.", pady=(5,5))
    myDesc.Tag("Telethia enemies Soul Reads are disabled for boss fights before monado purge is unlocked.", pady=(5,5))
    myDesc.Tag("The Egil fight in Mechonis core is a special case, the enemy will still look like egil but the attacks/stats and everything else will be a random enemy. The mechonis is tied to egils actions there and can easily break without him there.", pady=(5,5))
    myDesc.Tag("Enemy spikes are tuned for their new level", pady=(5,5))
    myDesc.Tag(f"Instant Death Spikes are removed for fights below level {instantDeathSpikeThreshold}", pady=(5,5))
    myDesc.Tag("A few boss fights require certain arts to be used to end. Mysterious Face in spiral valley for example.\nIn this case the enemy that replaces Mysterious Face will have that art added to their list in the slot it requires. (Only affects 4 fights in the game)", pady=(5,5))
    myDesc.Tag("Some fights have small green rings and if you get big enemies there it smashes you up against the wall. These fights will have the ring removed.", pady=(5,5))
    myDesc.Tag("Enemies who self destruct will not be able to if placed in certain boss fights that require arts to end", pady=(5,5))
    myDesc.Tag("The first two required fights in the game (Dunbans Prologue and Shulks Colony 9 introduction scene) are made easier to avoid softlocking.", pady=(5,5))
    return myDesc


# Dummy = [296, 329, 330, 331, 332, 333, 343, 651, 1204, 1206, 1329, 1548, 1625, 1626, 2602, 2603]
# BadEnemies = [220, 1154, 1157, 2403, 2406, 2413, 2750, 2906, 2908, 2909] + Helper.InclRange(370,388) + Helper.InclRange(930,997)+ Helper.InclRange(1131,1195)+ Helper.InclRange(1239, 1300)+ Helper.InclRange(701,778)+ Helper.InclRange(1769,1799)+ Helper.InclRange(1850,1897)

                                    # Grab the first valid enemy art
                                    # validArt = 0
                                    # for i in range(1,9):
                                    #     if enemy[f"arts{i}"] != 0:
                                    #         validArt = enemy[f"arts{i}"]
                                    #         enemy[f"arts{i}"] = 0 # Remove the art from that slot
                                    #         break
                                    
                                    
                                    # If for some reaosn the enemy does not have an art we need to give them one (I randomly chose an unused art rush importantly its act 0 so every enemy should be able to cast it and theres a bug where if enemies have the same art twice they wont use either so it has to be unused)
                                    # if validArts == 0:
                                    #     validArts = 117
                                        
                                    # Ensure that required slot has the art
                                    # if enemy[f"arts{id.artSlot}"] == 0:
                                    
                        # print("\n") 
                        # print(f"ID {enemy["$id"]} Replaced With ID {chosen.eneListArea["$id"]} Stat Total: {originalTotalStats}")
                        
                            #                     if file == "0301" and enemy["$id"] in [261]: # Game doenst like the pods being replaced here
                            # continue # 233 leg lizard [227,241, 233] try 264 this range crashes (260,265)
                        

# Finds locked enemies
# enemiesInLock = []
# for file in enAreaFiles:
#     try:
#         with open(f"./XCDE/JsonOutputs/bdat_ma{file}/FieldLock{file}.json", 'r+', encoding='utf-8') as eneLockFile:
#             with open(f"./XCDE/JsonOutputs/bdat_ma{file}/poplist{file}.json", 'r+', encoding='utf-8') as enePopFile:
#                 enePopData = json.load(enePopFile)
#                 eneLockData = json.load(eneLockFile)
#                 locks = []
#                 for lock in eneLockData["rows"]:
#                     for i in range(1,4):
#                         if lock[f"popID{i}"] != 0:  
#                             locks.append(lock[f"popID{i}"])
#                 for pop in enePopData["rows"]:
#                     if pop["$id"] in locks:
#                         for j in range(1,6):
#                             if pop[f"ene{j}ID"] != 0:
#                                 enemiesInLock.append(pop[f"ene{j}ID"])
#     except:
#         pass
# print(enemiesInLock)