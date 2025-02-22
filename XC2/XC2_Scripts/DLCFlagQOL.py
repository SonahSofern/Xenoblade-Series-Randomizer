import json, Options
from scripts import Helper

def CreateDLCtoSetFlag(ItemName: list[str], Flag: list[int]):
    MaxRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", "$id") + 1
    CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    
    with open("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        
        with open("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as namefile:
            
            data = json.load(file)
            namedata = json.load(namefile)
            
            for item in range(len(ItemName)):
                data["rows"].append({"$id": MaxRow, "releasecount": 1, "title": CurrentNameID, "condition": 1, "category": 2, "item_id": 0, "value": 1, "disp_item_info": 0, "getflag": Flag[item]})
                namedata["rows"].append({"$id": CurrentNameID, "style": 162, "name": ItemName[item]})
                MaxRow += 1
                CurrentNameID += 1
            
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)
        
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)