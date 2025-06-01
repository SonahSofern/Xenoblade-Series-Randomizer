import json, Options, IDs, random
from scripts import JSONParser, Helper, PopupDescriptions

keepTypeDescriptions = "This will ensure that items replacing an item will be of the same type\n(Weapons replace Weapons, Chestplates replace Chestplates etc.) \nThis will override any of the weight options."

class ItemType:
    def __init__(self, ids, obj =None):
        self.originalIds = ids.copy()
        self.ids = ids.copy()
        self.obj:Options.SubOption = obj
    def RefreshList(self):
        self.ids = self.originalIds.copy()
        
def ItemRandomization(itemTypes:list[ItemType] = [], files = [],odds = 0, game = "", keys = [], dontReplace = [], keepType = False):
    randoLists = []
    weights = []
    for item in itemTypes:
        if item.obj.GetState():
            randoLists.append(item)
            weights.append(item.obj.GetSpinBox())
    
    allItemLists = [ItemType(IDs.ArtBookIDs), ItemType(IDs.CollectableIDs), ItemType(IDs.CrystalIDs), ItemType(IDs.GemIDs), ItemType(IDs.ArmIDs), ItemType(IDs.ChestIDs), ItemType(IDs.LegIDs), ItemType(IDs.WaistIDs), ItemType(IDs.HeadIDs), ItemType(IDs.KeyItemIDs), ItemType(IDs.StoryRequiredKeyItemIDs), ItemType(IDs.MaterialIDs), ItemType(IDs.WeaponIDs)].copy()
    
    for file in files:
        try:
            with open(f"./{game}/_internal/JsonOutputs/{file}.json", 'r+', encoding='utf-8') as ItemFile:
                itemData = json.load(ItemFile)
                for itm in itemData["rows"]:
                    for key in keys:
                        if itm[key] == 0:
                            continue
                        if itm[key] in (IDs.StoryRequiredKeyItemIDs + IDs.KeyItemIDs + dontReplace):
                            continue
                        if not Helper.OddsCheck(odds):
                            continue
                        
                        if keepType:
                            for list in allItemLists:
                                if itm[key] in list.originalIds:
                                    chosenList = list
                                    break
                        else:
                            chosenList = random.choices(randoLists, weights, k=1)[0]
                            
                        if chosenList.ids == []:
                            chosenList.RefreshList()
                            
                        chosen = random.choice(chosenList.ids)

                        chosenList.ids.remove(chosen)
                        itm[key] = chosen
                JSONParser.CloseFile(itemData, ItemFile)
        except Exception as e:
            print(e)
            pass
# Add a keep item type option so the repleacement for x type will always be the same type 


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
    keepType = Options.CollectapediaOptions_KeepType
    
    odds = Options.CollectapediaOptions.GetSpinbox()
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], ["bdat_menu_item/MNU_col"], odds,"XCDE",  ["itemID"], keepType=keepType.GetState())

def CollectapediaDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.CollectapediaOptions.name)
    myDesc.Text("Randomizes rewards from the collectapedia. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
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
    keepType = Options.GiantsChest_KeepType
    
    odds = Options.GiantsChestOption.GetSpinbox()
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], ["bdat_common/FLD_tboxlist"], odds,"XCDE",  ["itm1ID","itm2ID","itm3ID","itm4ID"], keepType=keepType.GetState())

def GiantsChestsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.GiantsChestOption.name)
    myDesc.Text("Randomizes the contents of giants chests. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc

def Shops():
    col = ItemType(IDs.CollectableIDs, Options.ShopOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.ShopOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.ShopOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.ShopOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.ShopOptions_Gems)
    art = ItemType(IDs.ArtBookIDs, Options.ShopOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.ShopOptions_KeyItems)
    keepType = Options.ShopOption_KeepType
    
    odds = Options.ShopOption.GetSpinbox()
    
    keys = []
    preKeys = ["wpn", "head", "body", "arm", "waist", "legg", "arts"]
    for i in range(1,13):
        for pkey in preKeys:
            keys.append(f"{pkey}{i}")
    
    
    ItemRandomization([col, mat, arm, wep, gem, art, key], ["bdat_common/shoplist"], odds,"XCDE",  keys, keepType=keepType.GetState())

def ShopsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.ShopOption.name)
    myDesc.Text("Randomizes the contents of shops. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc

def EnemyDrops():
    col = ItemType(IDs.CollectableIDs, Options.EnemyDropOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.EnemyDropOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.EnemyDropOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.EnemyDropOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.EnemyDropOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.EnemyDropOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.EnemyDropOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.EnemyDropOptions_KeyItems)
    keepType = Options.EnemyDropOption_KeepType
    
    odds = Options.EnemyDropOption.GetSpinbox()
    
    nmlFiles = []
    rarFiles = []
    sprFiles = []
    for file in IDs.areaFileListNumbers:
        nmlFiles.append(f"bdat_ma{file}/drop_nmllist{file}")
        rarFiles.append(f"bdat_ma{file}/drop_rarlist{file}")
        sprFiles.append(f"bdat_ma{file}/drop_sprlist{file}")
        
    sprKeys = ["wpn1", "wpn2", "wpn3", "wpn4"]
    for i in range(1,9):
        sprKeys.append(f"arts{i}")
        sprKeys.append(f"uni_equip{i}")
        sprKeys.append(f"uni_wpn{i}")
    
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], nmlFiles, odds,"XCDE",  ["materia1", "materia2"], keepType=keepType.GetState())
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], rarFiles, odds,"XCDE",  ["crystal1", "crystal2", "wpn1", "wpn2", "wpn3", "wpn4", "equip1", "equip2", "equip3", "equip4"], keepType=keepType.GetState())
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], sprFiles, odds,"XCDE",  sprKeys, keepType=keepType.GetState())

def EnemyDropsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.EnemyDropOption.name)
    myDesc.Text("Randomizes the contents of chests dropped from enemies. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc


def QuestRewards():
    col = ItemType(IDs.CollectableIDs, Options.QuestRewardsOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.QuestRewardsOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.QuestRewardsOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.QuestRewardsOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.QuestRewardsOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.QuestRewardsOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.QuestRewardsOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.QuestRewardsOptions_KeyItems)
    keepType = Options.QuestRewardsOption_KeepType
    
    odds = Options.QuestRewardsOption.GetSpinbox()
    
    areas = []
    for area in IDs.areaFileListNumbers:
        areas.append(f"bdat_common/JNL_quest{area}")
    
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], areas, odds,"XCDE",  ["reward_A1","reward_A2","reward_A3","reward_B1","reward_B2","reward_B3"], keepType=keepType.GetState())

def QuestRewardsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.QuestRewardsOption.name)
    myDesc.Text("Randomizes rewards from quests. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc


def TradeOptions():
    col = ItemType(IDs.CollectableIDs, Options.TradeOptions_Collectables)
    mat = ItemType(IDs.MaterialIDs, Options.TradeOptions_Materials)
    arm = ItemType(IDs.ArmorIDs, Options.TradeOptions_Armor)
    wep = ItemType(IDs.WeaponIDs, Options.TradeOptions_Weapons)
    gem = ItemType(IDs.GemIDs, Options.TradeOptions_Gems)
    cry = ItemType(IDs.CrystalIDs, Options.TradeOptions_Crystals)
    art = ItemType(IDs.ArtBookIDs, Options.TradeOptions_ArtBooks)
    key = ItemType(IDs.KeyItemIDs, Options.TradeOptions_KeyItems)
    keepType = Options.TradeOption_KeepType
    
    odds = Options.TradeOption.GetSpinbox()
    
    areas = []
    for area in IDs.areaFileListNumbers:
        areas.append(f"bdat_ma{area}/exchangelist{area}")
    
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], areas, odds,"XCDE",  ["wpn1", "head1", "body1", "arm1", "waist1", "legg1", "kessyou1", "kessyou2", "collect1", "collect2", "materia1", "materia2"], keepType=keepType.GetState())

def TradeOptionsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TradeOption.name)
    myDesc.Text("Randomizes the trades NPCs make. Only the chosen suboptions will be randomized.\nThe categories will stay the same so helms will always replace helms and so on.")
    myDesc.Image("rondinecap.png", "XCDE", 800)
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc

