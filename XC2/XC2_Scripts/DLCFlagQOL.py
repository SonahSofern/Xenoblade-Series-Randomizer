import json, Options
from scripts import Helper

FreeDLCFlags = Helper.InclRange(65000, 65534)

def CreateDLCtoSetFlag(ItemName: list[str], Flag: list[int], Category: list[int] = [2], ItemID: list[int] = [0], Quantity: list[int] = [1]):
    if not Options.UMHuntOption.GetState():
        MaxRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", "$id") + 1
        CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
        
        with open("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
            
            with open("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as namefile:
                
                data = json.load(file)
                namedata = json.load(namefile)
                
                for item in range(len(ItemName)):
                    data["rows"].append({"$id": MaxRow, "releasecount": 1, "title": CurrentNameID, "condition": 1, "category": Category[item], "item_id": ItemID[item], "value": Quantity[item], "disp_item_info": 0, "getflag": Flag[item]})
                    namedata["rows"].append({"$id": CurrentNameID, "style": 162, "name": ItemName[item]})
                    MaxRow += 1
                    CurrentNameID += 1
                
                namefile.seek(0)
                namefile.truncate()
                json.dump(namedata, namefile, indent=2, ensure_ascii=False)
            
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def AddMovespeedDeed():
    if not Options.UMHuntOption.GetState():
        CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
        BonusMovespeed = Options.StartwithIncreasedMovespeedOption.GetOdds()
        with open("./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 25249:
                    row["Name"] = CurrentNameID
                    row["Caption"] = CurrentNameID + 1 # Increases running speed by X%
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 1:
                    row["Value"] = BonusMovespeed
                    row["Type"] = 1
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 750%
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == 1:
                    row["Max"] = 750
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
            data = json.load(file)
            data["rows"].append({"$id": CurrentNameID, "style": 36, "name": "Movespeed Deed"})
            data["rows"].append({"$id": CurrentNameID + 1, "style": 61, "name": f"Increases running speed by {BonusMovespeed}%."})
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        CreateDLCtoSetFlag(["Movespeed Deed"], [65000], [1], [25249], [1])