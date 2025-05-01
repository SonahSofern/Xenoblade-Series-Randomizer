import json, Options, IDs
from scripts import JSONParser

def FieldItems():
    for area in IDs.areaFileListNumbers:  
        try:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{area}/Litemlist{area}.json", 'r+', encoding='utf-8') as ItemFile:
                ItemData = json.load(ItemFile)
                for item in ItemData["rows"]:
                    for i in range(1,9):
                        item[f"itm{i}ID"] = 646
            
                JSONParser.CloseFile(ItemData, ItemFile)
        except:
            pass

