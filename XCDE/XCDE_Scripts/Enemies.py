
import json, random, Options, IDs, copy, traceback, math
from scripts import Helper, JSONParser, PopupDescriptions
from IDs import *
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

def Enemies(monsterTypeList, normal, unique, boss, superboss):
    MetalFace = ForcedArt(61, 2, 565)
    MysteriousFace = ForcedArt(268,5,611)
    GoldFace = ForcedArt(1622, 1, 740)
    DiscipleDickson = ForcedArt(1316, 8, 942)
    ForcedStoryArts = [MetalFace, MysteriousFace, GoldFace, DiscipleDickson] # (EnemyID, ArtSlots) Needed to make sure when the story requires the enemy to use the ultimate art that ends the fight they actually need an art to use
    isNormal = normal.GetState()
    isUnique = unique.GetState()
    isBoss = boss.GetState()
    isSuper = superboss.GetState()
    ChosenEnemyIds = []
    if isNormal:
        ChosenEnemyIds.extend(NormalEnemies)
    if isUnique:
        ChosenEnemyIds.extend(UniqueEnemies)
    if isBoss:
        ChosenEnemyIds.extend(BossEnemies)
    if isSuper:
        ChosenEnemyIds.extend(SuperbossEnemies)
    # "run_speed" Do NOT include run speed it lags the game to 1 fps "detects", "assist", "search_range", "search_angle", "frame"
    CopiedStats = ["move_speed", "size", "scale", "family","elem_phx", "elem_eth", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "avoid", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_dmg", "spike_state", "spike_state_val", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]
    CopiedStatsWithRatios = ["hp", "str", "eth"] # Not doing agility , "Lv_up_hp", "Lv_up_str", "Lv_up_eth" its too finicky and scales slowly compared to the other stats
    CopiedInfo = ["name", "resource", "c_name_id", "mnu_vision_face"]
    
    # 5001 doesnt have enemies
    enAreaFiles = areaFileListNumbers.copy()
    enAreaFiles.remove("5001")
    
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)    
        
        if OriginalEnemyData == []:
            CreateEnemyDataClass(eneData, enAreaFiles)
            
        filteredEnemyData = OriginalEnemyData.copy() 
        
        # Filter the list so we randomly choose from the enem types we want
        filteredEnemyData = [en for en in filteredEnemyData if en.enelist["$id"] in ChosenEnemyIds]
        
        filteredEnemyDataCopy = filteredEnemyData.copy() # Used to repopulate the list after removing
        
        # Randomly Assign Enemies
        for file in enAreaFiles:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                with open(f"./XCDE/_internal/JsonOutputs/bdat_common/VoEnemy.json", 'r+', encoding='utf-8') as eneVoiceFile:
                    eneVoiceData = json.load(eneVoiceFile)
                    eneAreaData = json.load(eneAreaFile)
                    
                    for enemy in eneAreaData["rows"]:   
                    
                        if enemy["$id"] not in monsterTypeList: # Only want to replace enemies chosen from our groups
                            continue
                                                    
                        chosen = random.choice(filteredEnemyData) # Choose an enemy                
                        
                        TelethiaEarly(enemy, chosen)
                        MechonEarly(enemy, chosen)
                        VoicedEnemiesFix(eneVoiceData, chosen, enemy)                                
                        SpikeBalancer(enemy, chosen.eneListArea)
                        
                        # Copy stats with ratios to original stats
                        replacementTotalStats = TotalStats(chosen.eneListArea, CopiedStatsWithRatios)
                        originalTotalStats = TotalStats(enemy, CopiedStatsWithRatios)
                        
                        # Copy chosen stats over
                        for key in CopiedStats: 
                            enemy[key] = chosen.eneListArea[key]

                        for key in CopiedStatsWithRatios:
                            enemy[key] = KeepStatRatio(enemy, chosen.eneListArea, key, replacementTotalStats, originalTotalStats)
                            
                        for ene in eneData["rows"]:
                            if (ene["$id"] == enemy["$id"]):
                                for key in CopiedInfo:
                                    ene[key] = chosen.enelist[key]
                                break
                        
                        ForcedArts(enemy, ForcedStoryArts)

                        # Allows no dupes if possible if we dont have enough choices it reshuffles the original pool
                        filteredEnemyData.remove(chosen)   
                        if filteredEnemyData == []: # repopulate it if the group is empty
                                filteredEnemyData = filteredEnemyDataCopy.copy()

                    JSONParser.CloseFile(eneVoiceData, eneVoiceFile)
                    JSONParser.CloseFile(eneAreaData, eneAreaFile)  
        JSONParser.CloseFile(eneData, eneFile)
        RingRemoval() 
    
def ForcedArts(enemy, ForcedStoryArts):
    # Fixes boss fights that require the enemy to use an art slot to end the fight 
    for id in ForcedStoryArts:
        if id.id == enemy["$id"]:
            enemy[f"arts{id.artSlot}"] = id.artId  # Change it to their art
            break    

def VoicedEnemiesFix(eneVoiceData, chosen, enemy):
    for voiceID in eneVoiceData["rows"]:
        if chosen.enelist["$id"] == voiceID["enemy"]: # If the chosen enemy has a voice
            voiceID["enemy"] = enemy["$id"] # Set the ID
            break    

# Create our list of enemies from all the area files and Combine the data into the class
def CreateEnemyDataClass(eneData, enAreaFiles):
    for file in enAreaFiles:  
        with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
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

def SpikeBalancer(enemy, chosen): # spike damage is 10x the spike_dmg value
    if chosen["spike_dmg"] != 0:
        spikePerLv = 0.5 # base spike given per level
        expectedPowerLv = chosen["lv"] * spikePerLv # The expected power level of the spike before any changes
        actualPowerLv = chosen["spike_dmg"]
        spikeMult = actualPowerLv/expectedPowerLv # If enemy has a stronger/weaker spike than something of its level make the spike stronger/weaker but still balanced
        newPowerLv = int(enemy["lv"] * spikeMult)
        chosen["spike_dmg"] = max(min(newPowerLv, 255), 1) # Set the new amount between 1 and 255
        # print(f"Level: {enemy["lv"]}")
        # print(f"Spike Damage: {chosen["spike_dmg"] * 10}")
    if (chosen["spike_state_val"] == 220) and (enemy["lv"] <= instantDeathSpikeThreshold): # Removes instant death spikes from all fights below level 60
        chosen["spike_state_val"] = 0
        
def TelethiaEarly(enemy, chosen:Enemy):
    TelethiaFamily = 9
    BadForTelethia = [30,31,61,62, 134, 265, 266, 268, 416, 417, 534] # Ids for early game so you dont get soul readed
    if (enemy["$id"] in BadForTelethia) and (chosen.eneListArea["family"] == TelethiaFamily):
        for i in range(1,9):
            if chosen.eneListArea[f"arts{i}"] == 666:
                chosen.eneListArea[f"arts{i}"] = 0 # Remove soul read if we get an early telethia

def MechonEarly(enemy, chosen:Enemy):
    MechonFamily = [1,2,4] # 4 Seems to share a lot of enemies that are aquatic, but mumkhar is family 4 and we dont want him early so it cuts a few enemies off that we mightve wanted otherwise oh well
    BadForMechon = [30, 31, 32,33, 63, 64, 65] # List of ids for the early game to make sure mechon arent placed here
    if (enemy["$id"] in BadForMechon) and (chosen.eneListArea["family"] in MechonFamily):
        chosen.eneListArea["family"] = 0


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
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/BTL_enelist_ms.json", 'r+', encoding='utf-8') as enNamesFile:
        with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/ene_arts_ms.json", 'r+', encoding='utf-8') as enArtNamesFile:
            with open(f"./XCDE/_internal/Enemies.txt", 'a', encoding='utf-8') as enemyTXT:
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
    
    # with open(f"./XCDE/_internal/Enemies.txt", 'a', encoding='utf-8') as enemyTXT: # Clear our enemies file
    #     enemyTXT.seek(0)
    #     enemyTXT.truncate()

# Used for starting fight had some weird thing with the enemies
def RingRemoval():
    RemoveLocks = [2]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_ma1401/FieldLock1401.json", 'r+', encoding='utf-8') as lockFile:
        lockData = json.load(lockFile)
        for lock in lockData["rows"]:
            if lock["$id"] in RemoveLocks:
                lock["popID1"] = 0
                lock["popID2"] = 0
        JSONParser.CloseFile(lockData, lockFile)
        
        
        
def EnemyDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.EnemyOption.name)
    myDesc.Text(f"Randomizes the chosen categories of enemies between their own types.\nThere is various logic to prevent bad situations")
    myDesc.Tag("Enemy stats do not scale with level in this game, so instead it takes the original enemies stat total and distributes it in the replacement enemies stat ratios.\nSo, if an enemy has a high attack stat compared to their other stats, they will still have a high attack stat but balanced with the replacement enemies' stats", pady=(5,5))
    myDesc.Tag(f"Instant Death Spikes are removed for fights below level {instantDeathSpikeThreshold}", pady=(5,5))
    myDesc.Tag("Mechon Enemies are not allowed for fights before you can damage mechon, toppling is not guaranteed with art randomization so this fix is needed", pady=(5,5))
    myDesc.Tag("Telethia enemies are disabled for boss fights before Purge is unlocked\nEnemy spikes are tuned for their new level")
    myDesc.Image("rondinecap.png", "XCDE", 800)
    myDesc.Header(Options.EnemyOption_MixTypes.name)
    myDesc.Header(Options.EnemyOption_Duplicates.name)
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