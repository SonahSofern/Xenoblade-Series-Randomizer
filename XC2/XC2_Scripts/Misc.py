import json
import random
from scripts import PopupDescriptions, JSONParser, Helper
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


def BeamRandomizer():
    JSONParser.ChangeJSONFile(["common/EFF_KizunaLink.json"], ["Red1","Red2", "Green1", "Green2", "Blue1", "Blue2"], Helper.InclRange(0,255), Helper.InclRange(0,255))
    JSONParser.ChangeJSONFile(["common/EFF_KizunaLink.json"], ["WavePower"],[100,120,140,200,300,400], Helper.InclRange(0,1000))
    
def SystemBalanceEditor():
    with open("./XC2/JsonOutputs/common/BTL_SystemBalance.json", 'r+', encoding='utf-8') as sysFile:
        sysData = json.load(sysFile)
        for sys in sysData["rows"]:
            UnlockSkillTrees(sys)
        JSONParser.CloseFile(sysData, sysFile)
            
def UnlockSkillTrees(sys):
    if sys["$id"] in [136,137]:
        sys["param"] = 0