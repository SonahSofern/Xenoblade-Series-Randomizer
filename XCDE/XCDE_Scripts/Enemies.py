
import json, random, Options, IDs

#Enelist is needed in conjuction with poplist not sure how they are referencing each other yet though

class Enemy:
    def __init__(self, _id, _name, _resource, _c_name_id, _mnu_vision_face):
        self.id = _id
        self.name = _name
        self.resource = _resource
        self.cname = _c_name_id
        self.mnuFace = _mnu_vision_face 


def Enemies():
    BadEnemyIds = []

    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        
        for enemy in eneData["rows"]:
            if enemy["name"] == 0:
                BadEnemyIds.append(enemy["$id"])
                    
        
        eneFile.seek(0)
        eneFile.truncate()
        json.dump(eneData, eneFile, indent=2, ensure_ascii=False)

    
    EnemyList = []
    for file in IDs.areaFileListNumbers:
        try:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/poplist{file}.json", 'r+', encoding='utf-8') as eneFile:
                eneData = json.load(eneFile)
                
                for enemy in eneData["rows"]:
                    for i in range(1,6):
                        if enemy[f"ene{i}ID"] == 0:
                            continue
                        if enemy[f"ene{i}ID"] in BadEnemyIds:
                            continue
                        EnemyList.append(enemy[f"ene{i}ID"])
                            
                
                eneFile.seek(0)
                eneFile.truncate()
                json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
        except:
            continue
    for file in IDs.areaFileListNumbers:
        try:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/poplist{file}.json", 'r+', encoding='utf-8') as eneFile:
                eneData = json.load(eneFile)
                
                for enemy in eneData["rows"]:
                    for i in range(1,6):
                        if enemy[f"ene{i}ID"] == 9:
                            chosen = random.choice(EnemyList)
                            enemy[f"ene{i}ID"] = 62
                            EnemyList.remove(chosen)
                            
                
                eneFile.seek(0)
                eneFile.truncate()
                json.dump(eneData, eneFile, indent=2, ensure_ascii=False)
        except:
            continue
    
    
    # for file in IDs.areaFileListNumbers:
    #     with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneFile:
    #         eneData = json.load(eneFile)
    #         EnemyList:list[Enemy] = []
            
    #         for enemy in eneData["rows"]: # Create our classes of enemies
    #             curEnemy = Enemy(enemy["$id"], enemy["name"], enemy["resource"], enemy["c_name_id"], enemy["mnu_vision_face"])
    #             EnemyList.append(curEnemy)
            
    #         for enemy in eneData["rows"]:
    #             chosen = random.choice(EnemyList)
    #             EnemyList.remove(chosen)
    #             enemy["name"] = chosen.name
    #             enemy["resource"] = chosen.resource
    #             enemy["c_name_id"] = chosen.cname
    #             enemy["mnu_vision_face"] = chosen.mnuFace
            
    #         eneFile.seek(0)
    #         eneFile.truncate()
    #         json.dump(eneData, eneFile, indent=2, ensure_ascii=False)