
import json, random, Options, IDs

class Enemy:
    def __init__(self, enelistArea, enelist):
        self.eneListArea = enelistArea
        self.enelist = enelist
        

def Enemies():
    EnemyList = []
    CombinedEnemyData:list[Enemy] = []     
    CopiedStats = ["move_speed", "named", "frame", "size", "scale", "family", "elem_phx", "elem_eth", "Lv_up_hp", "Lv_up_str", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "avoid", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "detects", "assist", "search_range", "search_angle", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_dmg", "spike_state", "spike_state_val", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]
    # "run_speed" Do NOT include run speed idk why the fuck it does this but it lags the game to 1 fps
    CopiedInfo = ["name", "resource", "c_name_id", "mnu_vision_face"]
    # Build our list of enemies
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        BadEnemies = [220]
        
        for enemy in eneData["rows"]: # Build our list of enemy resources and our list of bad enemies that we dont want to touch
            if enemy["name"] == 0:
                BadEnemies.append(enemy["$id"])
                continue
            EnemyList.append(enemy)
            
        # Create our list of enemies from all the area files and Combine the data into the class

        for file in IDs.areaFileListNumbers:
            try:   
                with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                    eneAreaData = json.load(eneAreaFile)
                    for enemy in eneAreaData["rows"]:
                        for en in EnemyList:
                            if en["$id"] == enemy["$id"]:
                                new = Enemy(enemy, en)      
                                CombinedEnemyData.append(new)
                                PrintEnemy(new)
                                break   
                    eneAreaFile.seek(0)
                    eneAreaFile.truncate()
                    json.dump(eneAreaData, eneAreaFile, indent=2, ensure_ascii=False)
            except:
                continue
                        
        for file in IDs.areaFileListNumbers:
            try:   
                with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                    eneAreaData = json.load(eneAreaFile)
                    for enemy in eneAreaData["rows"]:   
                        
                        if enemy["$id"] in [7]:
                            pass                  
                        if enemy["$id"] in BadEnemies:
                            continue
                        
                        chosen = random.choice(CombinedEnemyData)
                        for key in CopiedStats:
                            enemy[key] = chosen.eneListArea[key]
                            
                        for ene in eneData["rows"]:
                            if (ene["$id"] == enemy["$id"]):
                                for key in CopiedInfo:
                                    ene[key] = chosen.enelist[key]
                                break
                    eneAreaFile.seek(0)
                    eneAreaFile.truncate()
                    json.dump(eneAreaData, eneAreaFile, indent=2, ensure_ascii=False)
            except:
                continue
        eneFile.seek(0)
        eneFile.truncate()
        json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
    

def PrintEnemy(enemy:Enemy):
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/BTL_enelist_ms.json", 'r+', encoding='utf-8') as enNamesFile:
        with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/ene_arts_ms.json", 'r+', encoding='utf-8') as enArtNamesFile:
            with open(f"./XCDE/_internal/Enemies.txt", 'a', encoding='utf-8') as enemyTXT:
                enemyNameData = json.load(enNamesFile)
                enemyArtNameData = json.load(enArtNamesFile)
                for name in enemyNameData["rows"]:
                    if enemy.enelist["name"] == name["$id"]:
                        print(f"Name: {name['name']}")
                        enemyTXT.write(f" Name: {name['name']} ")
                        break
                for name in enemyArtNameData["rows"]:
                    for i in range(1,9):
                        if enemy.eneListArea[f"arts{i}"] == name["$id"]:
                            print(f"Art {i}: {name['name']}")
                            enemyTXT.write(f" Art {i}: {name['name']} ")
                            break
                enemyTXT.write("\n")
        #     enArtNamesFile.seek(0)
        #     enArtNamesFile.truncate()
        #     json.dump(enemyArtNameData, enArtNamesFile, indent=2, ensure_ascii=False)
        
        # enNamesFile.seek(0)
        # enNamesFile.truncate()
        # json.dump(enemyNameData, enArtNamesFile, indent=2, ensure_ascii=False)

    
               # for enemy in eneData["rows"]: # Give each enemy a random resource so they turn into that enemy on the field
        #     if enemy["name"] == 0:
        #         continue
        #     chosen = random.choice(res)
        #     enemy["resource"] = chosen
        #     res.remove(chosen) 

        
# def Enemies():
#     BadEnemyIds = [97,98,99,100]

#     # Create Bad Enemy List ID
#     with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
#         eneData = json.load(eneFile)
        
#         for enemy in eneData["rows"]:
#             if enemy["name"] == 0:
#                 BadEnemyIds.append(enemy["$id"])
        
#         eneFile.seek(0)
#         eneFile.truncate()
#         json.dump(eneData, eneFile, indent=2, ensure_ascii=False)

#     # Create our Enemies List
#     EnemyList = []
#     for file in IDs.areaFileListNumbers:
#         try: # Create our list of enemies
#             with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneFile:
#                 eneData = json.load(eneFile)
                
#                 for enemy in eneData["rows"]:
#                     if enemy["$id"] in BadEnemyIds:
#                         continue
#                     EnemyList.append(enemy)
                            
#                 eneFile.seek(0)
#                 eneFile.truncate()
#                 json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
#         except:
#             continue
#     # Randomize the enemy
#     for file in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneFile:
#                 with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/poplist{file}.json", 'r+', encoding='utf-8') as popFile:
#                     eneData = json.load(eneFile)
#                     popData= json.load(popFile)
                    
#                     for enemy in eneData["rows"]:
                        
#                         if enemy["$id"] in BadEnemyIds:
#                             continue
                        
#                         chosen = random.choice(EnemyList)
                        
#                         for popEnemy in popData["rows"]:
#                             for i in range(1,5):
#                                 if popEnemy[f"ene{i}ID"] == enemy["$id"]:
#                                     popEnemy[f"ene{i}ID"] = chosen["$id"]
                                    
#                         # EnemyList.remove(chosen)
#                         CopiedStats = ["$id", "move_speed", "named", "frame", "size", "scale", "family", "elem_phx", "elem_eth", "Lv_up_hp", "Lv_up_str", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "avoid", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "detects", "assist", "search_range", "search_angle", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_dmg", "spike_state", "spike_state_val", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]
#                         for key in ["$id"]:
#                             enemy[key] = chosen[key]

                        
                        
#                     popFile.seek(0)
#                     popFile.truncate()
#                     json.dump(popData, popFile, indent=2, ensure_ascii=False)         
#                 eneFile.seek(0)
#                 eneFile.truncate()
#                 json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
#         except:
#             continue
    