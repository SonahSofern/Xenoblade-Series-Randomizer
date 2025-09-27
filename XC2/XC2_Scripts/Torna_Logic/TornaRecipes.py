from scripts import Helper, JSONParser, PopupDescriptions
import json, random, time
from XC2.XC2_Scripts.IDs import ValidEnemies, TornaUMIDs

# FLD_CollectionTable $id -> ma40a and ma41a_FLD_CollectionPopList CollectionTable.
# if i implement random crafting recipes, this will be useful

def CreateTornaRecipeList():
    TornaRecipeIDs = []

    class TornaRecipe:
        def __init__(self, id):
            self.shopchangetaskid = id
            self.components = list()
            self.componentqty = list()
            subcomponentid = 0
            for i in range(1, 6):
                subcomponentid = Helper.FindValues("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", ["$id"], [self.shopchangetaskid], f"SetItem{i}")
                subcomponentqty = Helper.FindValues("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", ["$id"], [self.shopchangetaskid], f"SetNumber{i}")
                if subcomponentid != [0]:
                    self.components.extend(subcomponentid)
                    self.componentqty.extend(subcomponentqty)
            self.shopchangenameid = Helper.FindValues("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", ["$id"], [self.shopchangetaskid], "Name")[0]
            self.shopchangenametext = Helper.FindValues("./XC2/JsonOutputs/common_ms/fld_shopchange.json", ["$id"], [self.shopchangenameid], "name")[0]
            self.itmnametext = Helper.FindValues("./XC2/JsonOutputs/common_ms/itm_favorite.json", ["name"], [self.shopchangenametext], "$id")
            if self.itmnametext != []:
                self.itmnametext = self.itmnametext[0]
            self.itmfavlistid = Helper.FindValues("./XC2/JsonOutputs/common/ITM_FavoriteList.json", ["Name"], [self.itmnametext], "$id")
            if self.itmfavlistid != []:
                self.itmfavlistid = self.itmfavlistid[0]
            #print("{'Shop Task ID': " + str(self.shopchangetaskid) + ", 'Ingredients': " + str(self.components) +"}")
            self.id = self.itmfavlistid
            self.name = self.itmnametext
            self.mainreq = 4
            self.itemreqs = self.components
            self.randomizeditems = [self.id]
            self.type = "recipe"
            TornaRecipeIDs.append(self)

    with open("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["IraCraftIndex"] != 0:
                TornaRecipe(row["$id"])      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    return TornaRecipeIDs