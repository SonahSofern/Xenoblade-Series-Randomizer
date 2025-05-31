import json, Options, IDs, random
from scripts import JSONParser, Helper, PopupDescriptions

class ItemType:
    def __init__(self, ids, obj):
        self.originalIds = ids.copy()
        self.ids = ids.copy()
        self.obj:Options.SubOption = obj
    def RefreshList(self):
        self.ids = self.originalIds
        
def ItemRandomization(itemTypes:list[ItemType] = [], files = [],odds = 0, game = "", keys = []):
    randoList = []
    weights = []
    for item in itemTypes:
        if item.obj.GetState():
            randoList.append(item)
            weights.append(item.obj.GetSpinBox())
        
    for file in files:
        try:
            with open(f"./{game}/_internal/JsonOutputs/{file}.json", 'r+', encoding='utf-8') as ItemFile:
                itemData = json.load(ItemFile)
                for itm in itemData["rows"]:
                    for key in keys:
                        if not Helper.OddsCheck(odds):
                            continue
                        chosenList = random.choices(randoList, weights, k=1)[0]
                        chosen = random.choice(chosenList.ids)
                        chosenList.ids.remove(chosen)
                        if chosenList.ids == []:
                            chosenList.RefreshList()
                        itm[key] = chosen
                JSONParser.CloseFile(itemData, ItemFile)
        except:
            pass



def Collectables():
    col = ItemType(IDs.CollectableIDs, Options.CollectableOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.CollectableOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.CollectableOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.CollectableOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.CollectableOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.CollectableOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.CollectableOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.CollectableOptions_KeyItems)
    odds = Options.CollectableOptions.GetSpinbox()
    areas = []
    keys = []
    for i in range(1,9):
        keys.append(f"itm{i}ID")
    for area in IDs.areaFileListNumbers:  
        areas.append(f"bdat_ma{area}/Litemlist{area}")
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], areas, odds,"XCDE",  keys)

def CollectDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.CollectableOptions.name)
    myDesc.Text("Randomizes collectables in the field. Collectibles have 8 different possible items per orb per location. You can also choose weights for the categories you have chosen.")
    myDesc.Image("orb.png","XCDE", 500)
    return myDesc


def Collectapedia():
    col = ItemType(IDs.CollectableIDs, Options.CollectapediaOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.CollectapediaOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.CollectapediaOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.CollectapediaOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.CollectapediaOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.CollectapediaOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.CollectapediaOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.CollectapediaOptions_KeyItems)
    odds = Options.CollectapediaOptions.GetSpinbox()
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], ["bdat_menu_item/MNU_col"], odds,"XCDE",  ["itemID"])

def CollectapediaDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.CollectapediaOptions.name)
    myDesc.Text("Randomizes rewards from the collectapedia. You can choose the weights for the categories you have chosen.")
    return myDesc


def GiantsChests():
    col = ItemType(IDs.CollectableIDs, Options.GiantsChestOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.GiantsChestOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.GiantsChestOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.GiantsChestOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.GiantsChestOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.GiantsChestOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.GiantsChestOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.GiantsChestOptions_KeyItems)
    odds = Options.GiantsChestOption.GetSpinbox()
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], ["bdat_common/FLD_tboxlist"], odds,"XCDE",  ["itm1ID","itm2ID","itm3ID","itm4ID"])

def GiantsChestsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.GiantsChestOption.name)
    myDesc.Text("Randomizes the contents of giants chests. You can choose the weights for the categories you have chosen.")
    return myDesc