from XC2.XC2_Scripts import Options, IDs
import json, random
from scripts import Helper, PopupDescriptions
def RandoPouchShops():
    ValidReplacements = []
    if Options.PouchItemShopOption_Accessories.GetState():
        ValidReplacements.extend(IDs.Accessories)
    if Options.PouchItemShopOption_TornaAccessories.GetState():
        ValidReplacements.extend(IDs.TornaAccessories)
    if Options.PouchItemShopOption_WeaponChips.GetState():
        ValidReplacements.extend(IDs.WeaponChips)
    if Options.PouchItemShopOption_AuxCores.GetState():
        ValidReplacements.extend(IDs.AuxCores)
    if Options.PouchItemShopOption_RefinedAuxCores.GetState():
        ValidReplacements.extend(IDs.RefinedAuxCores)
    if Options.PouchItemShopOption_CoreCrystals.GetState():
        ValidReplacements.extend(IDs.CoreCrystals)
    if Options.PouchItemShopOption_Deeds.GetState():
        ValidReplacements.extend(IDs.Deeds)
    if Options.PouchItemShopOption_PouchItems.GetState():
        ValidReplacements.extend(IDs.PouchItems)
    if Options.PouchItemShopOption_CollectionPointMaterials.GetState():
        ValidReplacements.extend(IDs.CollectionPointMaterials)

    if ValidReplacements == []: # In case they dont select anything
        return
    
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        odds = Options.PouchItemShopOption.GetSpinbox()
        for shop in shopData["rows"]:
            if shop[f"DefItem1"] not in (IDs.PouchItems): # Ensures it is an pouch item shop
                continue
            for i in range(1,11):
                if not Helper.OddsCheck(odds): # Check spinbox
                    continue
                if shop[f"DefItem{i}"] == 0: # Ignore empty spots in shops
                    continue
                shop[f"DefItem{i}"] = random.choice(ValidReplacements) # Make our selection
            
        shopFile.seek(0)
        shopFile.truncate()
        json.dump(shopData, shopFile, indent=2, ensure_ascii=False)


def PouchItemShopDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.PouchItemShopOption.name)
    # Insert image of accessory shop icon
    desc.Text("This option randomizes a % of all items in Pouch Item Shops into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("PouchItemShops.png", "XC2")
    return desc