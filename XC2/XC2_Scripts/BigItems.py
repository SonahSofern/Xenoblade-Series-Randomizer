import json
import random
from scripts import PopupDescriptions, JSONParser
from XC2.XC2_Scripts import Options

def BigItemsRando():
    with open("./XC2/JsonOutputs/common_gmk/RSC_dropitemParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row["endScale"] = random.randint(1, 10)
            row["isSpin"] = random.randint(0,1)
            row["spinSpeed"] = random.randint(60, 1000)
        JSONParser.CloseFile(data,file)

def BigItemsDesc():
    BigItemDesc = PopupDescriptions.Description()
    BigItemDesc.Header(Options.FieldItemOption.name)
    BigItemDesc.Text("When enabled, this option randomizes the size and spinrate of all items dropped from Enemies, Collection Points, and Treasure Chests.")
    BigItemDesc.Image("RandomLootSize.png", "XC2", 700)
    return BigItemDesc