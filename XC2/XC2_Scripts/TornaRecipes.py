from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from IDs import ValidEnemies, TornaUMIDs

# FLD_CollectionTable $id -> ma40a and ma41a_FLD_CollectionPopList CollectionTable.
# if i implement random crafting recipes, this will be useful

def CreateTornaRecipeList():
    global TornaRecipeIDs
    TornaRecipeIDs = []
    TornaRegularEnemyIDs = []
    TornaMA40AEnemyIDs = []
    TornaMA41AEnemyIDs = []
    class TornaRecipe:
        def __init__(self, id):
            self.id = id
            self.components = list()
            subcomponentid = 0
            for i in range(1, 6):
                subcomponentid = Helper.FindValues("./XC2/_internal/JsonOutputs/common/MNU_ShopChangeTask.json", ["$id"], [self.id], f"SetItem{i}")
                if subcomponentid != [0]:
                    self.components.extend(subcomponentid)
            self.nameid = Helper.FindValues("./XC2/_internal/JsonOutputs/common/MNU_ShopChangeTask.json", ["$id"], [self.id], "Name")[0]
            self.name = Helper.FindValues("./XC2/_internal/JsonOutputs/common_ms/fld_shopchange.json", ["$id"], [self.nameid], "name")[0]
            TornaRecipeIDs.append(self)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["IraCraftIndex"] != 0:
                TornaRecipe(row["$id"])      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
#    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_EnemyPop.json", 'r+', encoding='utf-8') as file:
#        data = json.load(file)
#        for row in data["rows"]:
#            if row["name"][:2] not in ["bo", "cf", "qs", "  "]:
#                for i in range(1, 5):
#                    if row[f"ene{i}ID"] in ValidEnemies and row[f"ene{i}ID"] not in TornaUMIDs:
#                        TornaMA40AEnemyIDs.append(row[f"ene{i}ID"])
#        file.seek(0)
#        file.truncate()
#        json.dump(data, file, indent=2, ensure_ascii=False)
#    with open("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_EnemyPop.json", 'r+', encoding='utf-8') as file:
#        data = json.load(file)
#        for row in data["rows"]:
#            if row["name"][:2] not in ["bo", "cf", "qs", "  "]:
#                for i in range(1, 5):
#                    if row[f"ene{i}ID"] in ValidEnemies and row[f"ene{i}ID"] not in TornaUMIDs:
#                        TornaMA41AEnemyIDs.append(row[f"ene{i}ID"])
#        file.seek(0)
#        file.truncate()
#        json.dump(data, file, indent=2, ensure_ascii=False)
#    TornaMA40AEnemyIDs = list(set(TornaMA40AEnemyIDs))
#    print(len(TornaMA40AEnemyIDs))
#    TornaMA41AEnemyIDs = list(set(TornaMA41AEnemyIDs))
#    print(len(TornaMA41AEnemyIDs))
#    TornaRegularEnemyIDs = TornaMA40AEnemyIDs + TornaMA41AEnemyIDs
#    TornaRegularEnemyIDs = list(set(TornaRegularEnemyIDs))
#    print(TornaRegularEnemyIDs)