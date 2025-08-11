from XC3.XC3_Scripts import IDs
from scripts import JSONParser
import json, random
def Shops():
    with open("XC3/JsonOutputs/mnu/MNU_ShopTable.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        group = IDs.DLC4AccessoriesIDs + IDs.AccessoriesIDs
        for shop in shopData["rows"]:
            for i in range(1,21):
                shop[f"ShopItem{i}"] = random.choice(IDs.BaseGamePreciousIDs)
        JSONParser.CloseFile(shopData,shopFile)

# def EnemyNormalDrops():
    