from XC3.XC3_Scripts import IDs
from scripts import JSONParser
import json, random
def Shops():
    with open("XC3/JsonOutputs/mnu/MNU_ShopTable.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        group = IDs.DLC4AccessoriesIDs + IDs.AccessoriesIDs + IDs.BaseGamePreciousIDs
        for shop in shopData["rows"]:
            for i in range(1,21):
                newItemId = random.choice(group)
                if (shop[f"ShopItem{i}"] in [1]) and (shop["$id"] in [1,2,3]): # Dont replace bronze temple guard in shop 1 for tutorial
                    continue
                shop[f"ShopItem{i}"] = newItemId
        JSONParser.CloseFile(shopData,shopFile)


def EnemyNormalDrops():
    with open("XC3/JsonOutputs/mnu/MNU_ShopTable.json", 'r+', encoding='utf-8') as eneDropFile:
        eneDropData = json.load(eneDropFile)
        for drop in eneDropData["rows"]:
            drop["ItemID"] = random.choice(IDs.AccessoriesIDs)
        JSONParser.CloseFile(eneDropData, eneDropFile)