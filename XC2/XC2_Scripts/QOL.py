import json
from XC2.XC2_Scripts import Options
from XC2.XC2_Scripts.Unused import EnemyRandoLogic
from scripts import Helper, JSONParser
FreeDLCFlags = Helper.InclRange(65000, 65534)

def CreateDLCtoSetFlag(ItemName: list[str], Flag: list[int], Category: list[int] = [2], ItemID: list[int] = [0], Quantity: list[int] = [1], Condition: list[int] = [1]):
    MaxRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/MNU_DlcGift.json", "$id") + 1
    CurrentNameID = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    
    with open("./XC2/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        
        with open("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as namefile:
            
            data = json.load(file)
            namedata = json.load(namefile)
            
            for item in range(len(ItemName)):
                data["rows"].append({"$id": MaxRow, "releasecount": 1, "title": CurrentNameID, "condition": Condition[item], "category": Category[item], "item_id": ItemID[item], "value": Quantity[item], "disp_item_info": 0, "getflag": Flag[item]})
                namedata["rows"].append({"$id": CurrentNameID, "style": 162, "name": ItemName[item]})
                MaxRow += 1
                CurrentNameID += 1
            
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)
        
        JSONParser.CloseFile(data, file)

def AddMovespeedDeed():
    # Torna Exclusive debug
    #JSONParser.ChangeJSONLine(["common/FLD_OwnerBonus.json"],[49],["Value"], 500)
    #JSONParser.ChangeJSONLine(["common/FLD_OwnerBonusParam.json"],[1],["Max"], 1000)
    #Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/ma40a_FLD_TboxPop.json", ["FSID", "FSID2"], 0)
    # Torna Exclusive debug
    # CurrentNameID = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    # JSONParser.ChangeJSONLine(["common/ITM_PreciousList.json"], [25249], ["Name"], CurrentNameID)
    # JSONParser.ChangeJSONLine(["common/ITM_PreciousList.json"], [25249], ["Caption"], CurrentNameID + 1)
    # JSONParser.ChangeJSONLine(["common/FLD_OwnerBonus.json"], [1], ["Value"], BonusMovespeed)
    # JSONParser.ChangeJSONLine(["common/FLD_OwnerBonus.json"], [1], ["Type"], 1)
    # JSONParser.ChangeJSONLine(["common/FLD_OwnerBonusParam.json"], [1], ["Max"], 750)
    # with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
    #     data = json.load(file)
    #     data["rows"].append({"$id": CurrentNameID, "style": 36, "name": "Movespeed Deed"})
    #     data["rows"].append({"$id": CurrentNameID + 1, "style": 61, "name": f"Increases running speed by {BonusMovespeed}%."})
    #     file.seek(0)
    #     file.truncate()
    #     json.dump(data, file, indent=2, ensure_ascii=False)
    # CreateDLCtoSetFlag(["Movespeed Deed"], [65000], [1], [25249], [1])
    
    # First enemy drops movespeed deed
    BonusMovespeed = Options.StartwithIncreasedMovespeedOption.GetSpinbox() * 10
    JSONParser.ChangeJSONLine(["common/FLD_OwnerBonus.json"], [9], ["Value"], BonusMovespeed)
    JSONParser.ChangeJSONLine(["common/CHR_EnArrange.json"], [1430 , 179], ["PreciousID"], 25257)

def FixIssuesCausedByNGPlusFlag():
    CreateDLCtoSetFlag(["Driver Skill Tree Key"], [48589], Condition = [1853]) # 1853 is a pre-existing flag that requires the Scenario to be 2001 or higher (when you get pyra)
    # if not Options.EnemiesOption.GetState(): # we need to force the enemies to drop their item, if enemy randomization is off
    #     EnemyRandoLogic.KeyItemsReAdd()
    # if Options.TreasureChestOption.GetState(): #if treasure chests are randomized loot, we need to force the ladder key in mor ardain to drop, allowing us to unlock the factory
    #     JSONParser.ChangeJSONLine(["common_gmk/ma08a_FLD_TboxPop.json"], [870], ["itm1ID"], 25409)