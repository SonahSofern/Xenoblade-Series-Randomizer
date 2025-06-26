
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


def Enemies(monsterTypeList, normal, unique, boss, superboss, odds):

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

                        
                        # Allows no dupes if possible if we dont have enough choices it reshuffles the original pool
                        filteredEnemyData.remove(chosen)   
                        if filteredEnemyData == []: # repopulate it if the group is empty
                                filteredEnemyData = filteredEnemyDataCopy.copy()

                    JSONParser.CloseFile(eneVoiceData, eneVoiceFile)
                    JSONParser.CloseFile(eneAreaData, eneAreaFile)  
        JSONParser.CloseFile(eneData, eneFile)

