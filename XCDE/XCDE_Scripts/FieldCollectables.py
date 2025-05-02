import json, Options, IDs, random
from scripts import JSONParser, Helper

def FieldItems():
    isCollect = Options.CollectableOptions_Collectables.GetState()
    isMat = Options.CollectableOptions_Materials.GetState()
    isArm = Options.CollectableOptions_Armor.GetState()
    isWep = Options.CollectableOptions_Weapons.GetState()
    isGem = Options.CollectableOptions_Gems.GetState()
    isCry = Options.CollectableOptions_Crystals.GetState()
    isArt = Options.CollectableOptions_ArtBooks.GetState()
    odds = Options.CollectableOptions.GetSpinbox()
    
    itemList = []
    
    if isCollect:
        itemList.append(IDs.CollectableIDs)
    if isMat:
        itemList.append(IDs.MaterialIDs)
    if isArm:
        itemList.append(IDs.ArmorIDs)
    if isWep:
        itemList.append(IDs.WeaponIDs)
    if isGem:
        itemList.append(IDs.GemIDs)
    if isCry:
        itemList.append(IDs.CrystalIDs)
    if isArt:
        itemList.append(IDs.ArtBookIDs)
        
    for area in IDs.areaFileListNumbers:  
        try:
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{area}/Litemlist{area}.json", 'r+', encoding='utf-8') as ItemFile:
                ItemData = json.load(ItemFile)
                for item in ItemData["rows"]:
                    for i in range(1,9):
                        if Helper.OddsCheck(odds):
                            item[f"itm{i}ID"] = random.choice(random.choice(itemList))
            
                JSONParser.CloseFile(ItemData, ItemFile)
        except:
            pass

