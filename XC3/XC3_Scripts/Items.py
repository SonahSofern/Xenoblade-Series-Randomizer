from XC3.XC3_Scripts import IDs, Options
from scripts import JSONParser, Helper, PopupDescriptions
import json, random

def Shops():
    if Options.ShopOption_IndividualItems.GetState():
        with open("XC3/JsonOutputs/mnu/MNU_ShopTable.json", 'r+', encoding='utf-8') as shopFile:
            shopData = json.load(shopFile)
            chosenGroup = IDs.DLC4AccessoriesIDs + IDs.AccessoriesIDs
            ignoreGroup = [1] + IDs.DLC4PreciousIDs + IDs.BaseGamePreciousIDs
            for shop in shopData["rows"]:
                for i in range(1,21):
                    if (shop[f"ShopItem{i}"] in ignoreGroup) and (shop["$id"] in [1,2,3]):
                        continue
                    newItemId = random.choice(chosenGroup)
                    shop[f"ShopItem{i}"] = newItemId
            JSONParser.CloseFile(shopData,shopFile)
    if Options.ShopOption_ShuffleShops.GetState():
        Helper.FileShuffle("XC3/JsonOutputs/mnu/MNU_ShopTable.json", ["$id"])

def EnemyNormalDrops():
    if Options.EnemyNormalDropOption_IndividualItems.GetState():
        with open("XC3/JsonOutputs/btl/BTL_EnemyDrop_Normal.json", 'r+', encoding='utf-8') as eneDropFile:
            eneDropData = json.load(eneDropFile)
            for drop in eneDropData["rows"]:
                drop["ItemID"] = random.choice(IDs.AccessoriesIDs)
            JSONParser.CloseFile(eneDropData, eneDropFile)
        with open("XC3/JsonOutputs/btl/BTL_EnemyDrop_Normal_dlc04.json", 'r+', encoding='utf-8') as eneDropFile: # FR
            eneDropData = json.load(eneDropFile)
            for drop in eneDropData["rows"]:
                drop["ItemID"] = random.choice(IDs.AccessoriesIDs + IDs.DLC4AccessoriesIDs)
            JSONParser.CloseFile(eneDropData, eneDropFile)
    if Options.EnemyNormalDropOption_ShuffleDrops.GetState():
        Helper.FileShuffle("XC3/JsonOutputs/btl/BTL_EnemyDrop_Normal.json", ["$id", "LvMin", "LvMax", "Param", "<36D6C799>"])
        Helper.FileShuffle("XC3/JsonOutputs/btl/BTL_EnemyDrop_Normal_dlc04.json", ["$id", "LvMin", "LvMax", "Param", "<36D6C799>"]) # FR
        
        
def TreasureBoxes():
    if Options.TreasureBoxOption_IndividualItems.GetState():
        with open("XC3/JsonOutputs/sys/ITM_RewardAssort.json", 'r+', encoding='utf-8') as containerFile:
            containerData = json.load(containerFile)
            for container in containerData["rows"]:
                for i in range(1,20):
                    if container[f"Reward{i}"] in IDs.BaseGamePreciousIDs + IDs.DLC4PreciousIDs: # Dont replace Precious Items
                        continue
                    container[f"Reward{i}"] = random.choice(IDs.AccessoriesIDs)
            JSONParser.CloseFile(containerData, containerFile)
    if Options.TreasureBoxOption_ShuffleBoxes.GetState():
        Helper.FileShuffle("XC3/JsonOutputs/sys/ITM_RewardAssort.json", ["$id"])
        