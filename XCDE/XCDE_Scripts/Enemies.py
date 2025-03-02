
import json, random, Options, IDs

        
def Enemies():
    BadEnemyIds = []

    # Create Bad Enemy List ID
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        
        for enemy in eneData["rows"]:
            if enemy["name"] == 0:
                BadEnemyIds.append(enemy["$id"])
                    
        
        eneFile.seek(0)
        eneFile.truncate()
        json.dump(eneData, eneFile, indent=2, ensure_ascii=False)

    # Create our Enemies List
    EnemyList = []
    for file in IDs.areaFileListNumbers:
        try: # Create our list of enemies
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneFile:
                eneData = json.load(eneFile)
                
                for enemy in eneData["rows"]:
                    if enemy["$id"] in BadEnemyIds:
                        continue
                    EnemyList.append(enemy)
                            
                eneFile.seek(0)
                eneFile.truncate()
                json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
        except:
            continue
    # Randomize the enemy
    for file in IDs.areaFileListNumbers:
        try:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneFile:
                with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/poplist{file}.json", 'r+', encoding='utf-8') as popFile:
                    eneData = json.load(eneFile)
                    popData= json.load(popFile)
                    
                    for enemy in eneData["rows"]:
                        
                        if enemy["$id"] in BadEnemyIds:
                            continue
                        
                        chosen = random.choice(EnemyList)
                        
                        for popEnemy in popData["rows"]:
                            for i in range(1,5):
                                if popEnemy[f"ene{i}ID"] == enemy["$id"]:
                                    popEnemy[f"ene{i}ID"] = chosen["$id"]
                                    
                        EnemyList.remove(chosen)
                        for key in ["$id", "move_speed", "run_speed", "named", "frame", "size", "scale", "family", "elem_phx", "elem_eth", "Lv_up_hp", "Lv_up_str", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "avoid", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "detects", "assist", "search_range", "search_angle", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_dmg", "spike_state", "spike_state_val", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]:
                            enemy[key] = chosen[key]

                        
                        
                    popFile.seek(0)
                    popFile.truncate()
                    json.dump(popData, popFile, indent=2, ensure_ascii=False)         
                eneFile.seek(0)
                eneFile.truncate()
                json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
        except:
            continue
    