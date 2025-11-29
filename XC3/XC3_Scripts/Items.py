from XC3.XC3_Scripts import IDs, Options
from scripts import JSONParser, Helper, PopupDescriptions, Values
import json

# Small helpers to generate a standard valtable since they will probably reuse this a lot
def StandardValTable(Accessories = None, Precious = None, Collectables = None):
    valTable = Values.ValueTable(path = "XC3/JsonOutputs/sys")
    if Accessories != None:
        valTable.PopulateValues(Values.ValueFile("ITM_Accessory"), IDs.AccessoriesIDs, Values.WeightOptionMethod(Accessories))
    if Precious != None:
        valTable.PopulateValues(Values.ValueFile("ITM_Precious", key="Price1"), IDs.BaseGamePreciousIDs, Values.WeightOptionMethod(Precious))
    if Collectables != None:
        valTable.PopulateValues(Values.ValueFile("ITM_Collection", key="Price3"), IDs.CollectableIDs, Values.WeightOptionMethod(Collectables))
    return valTable
    
def DLC4StandardValTable(Accessories = None, Precious = None, Collectables = None):
    dlc4ValTable = Values.ValueTable(path = "XC3/JsonOutputs/sys")
    if Accessories != None:
        dlc4ValTable.PopulateValues(Values.ValueFile("ITM_Accessory", key="Price_dlc04"), IDs.AccessoriesIDs + IDs.DLC4AccessoriesIDs, Values.WeightOptionMethod(Accessories))
    if Precious != None:
        dlc4ValTable.PopulateValues(Values.ValueFile("ITM_Precious", key="Price1"), IDs.DLC4PreciousIDs, Values.WeightOptionMethod(Precious))
    if Collectables != None:
        dlc4ValTable.PopulateValues(Values.ValueFile("ITM_Collection", key="Price3_dlc04"), IDs.DLC4CollectableIDs, Values.WeightOptionMethod(Collectables))
    return dlc4ValTable

def Shops():
    valTable:Values.ValueTable = StandardValTable(Options.ShopOption_Accessories, Options.ShopOption_Precious, Options.ShopOption_Collectables)
    dlc4ValTable:Values.ValueTable = DLC4StandardValTable(Options.ShopOption_Accessories, Options.ShopOption_Precious, Options.ShopOption_Collectables)

    DLC4ShopIDs = [54,55,56,57]
    BronzeTempleGuard = [1]
    with open("XC3/JsonOutputs/mnu/MNU_ShopTable.json", 'r+', encoding='utf-8') as shopFile:
            shopData = json.load(shopFile)
            for shop in shopData["rows"]:
                for i in range(1,21):
                    if shop["$id"] in DLC4ShopIDs:
                        dlc4ValTable.SelectValuedMember(shop, f"ShopItem{i}", IDs.DLC4PreciousIDs)
                    else:
                        valTable.SelectValuedMember(shop, f"ShopItem{i}", IDs.BaseGamePreciousIDs + BronzeTempleGuard)
                    
            JSONParser.CloseFile(shopData,shopFile)

def EnemyDrops():
    valTable = StandardValTable(Options.EnemyNormalDrop_Accessories, Options.EnemyNormalDrop_Precious)
    dlc4ValTable = DLC4StandardValTable(Options.EnemyNormalDrop_Accessories, Options.EnemyNormalDrop_Precious)
    
    with open("XC3/JsonOutputs/btl/BTL_EnemyDrop_Normal.json", 'r+', encoding='utf-8') as eneDropFile:
        eneDropData = json.load(eneDropFile)
        for drop in eneDropData["rows"]:
            valTable.SelectValuedMember(drop, ["ItemID"])
        JSONParser.CloseFile(eneDropData, eneDropFile)
        
    with open("XC3/JsonOutputs/dlc/BTL_EnemyDrop_Normal_dlc04.json", 'r+', encoding='utf-8') as eneDropFile: # FR
        eneDropData = json.load(eneDropFile)
        for drop in eneDropData["rows"]:
            dlc4ValTable.SelectValuedMember(drop, ["ItemID"])
        JSONParser.CloseFile(eneDropData, eneDropFile)
        
def TreasureBoxes():
    valTable = StandardValTable(Options.TreasureBoxOption_Accessories, Options.TreasureBoxOption_Precious, Options.TreasureBoxOption_Collectables)
    dlc4ValTable = DLC4StandardValTable(Options.TreasureBoxOption_Accessories, Options.TreasureBoxOption_Precious, Options.TreasureBoxOption_Collectables)
    
    dlc4TboxIDs = Helper.InclRange(429, 501)
    AttackStone = [471] # Tutorials require this
    
    with open("XC3/JsonOutputs/sys/ITM_RewardAssort.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        
        for tbox in tboxData["rows"]:
            for i in range(1,21):
                if tbox["$id"] in dlc4TboxIDs:
                    dlc4ValTable.SelectValuedMember(tbox, [f"Reward{i}"], IDs.DLC4PreciousIDs)
                else:
                    valTable.SelectValuedMember(tbox, [f"Reward{i}"], IDs.BaseGamePreciousIDs + AttackStone)