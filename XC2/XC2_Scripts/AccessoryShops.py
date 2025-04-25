import Options, IDs, json, random
from scripts import Helper, PopupDescriptions
def RandoAccessoryShops():
    ValidReplacements = []
    if Options.AccessoryShopsOption_Accessories.GetState():
        ValidReplacements.extend(IDs.Accessories)
    if Options.AccessoryShopsOption_TornaAccessories.GetState():
        ValidReplacements.extend(IDs.TornaAccessories)
    if Options.AccessoryShopsOption_WeaponChips.GetState():
        ValidReplacements.extend(IDs.WeaponChips)
    if Options.AccessoryShopsOption_AuxCores.GetState():
        ValidReplacements.extend(IDs.AuxCores)
    if Options.AccessoryShopsOption_RefinedAuxCores.GetState():
        ValidReplacements.extend(IDs.RefinedAuxCores)
    if Options.AccessoryShopsOption_CoreCrystals.GetState():
        ValidReplacements.extend(IDs.CoreCrystals)
    if Options.AccessoryShopsOption_Deeds.GetState():
        ValidReplacements.extend(IDs.Deeds)
    if Options.AccessoryShopsOption_PouchItems.GetState():
        ValidReplacements.extend(IDs.PouchItems)
    if Options.AccessoryShopsOption_CollectionPointMaterials.GetState():
        ValidReplacements.extend(IDs.CollectionPointMaterials)
    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        odds = Options.AccessoryShopsOption.GetSpinbox()
        for shop in shopData["rows"]:
            if shop[f"DefItem1"] not in (IDs.Accessories + IDs.TornaAccessories): # Ensures it is an accessory shop
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
        
def AccessoryShopDescription():
    desc = PopupDescriptions.Description()
    desc.Header(Options.AccessoryShopsOption.name)
    desc.Text("This option randomizes a % of all non-key items in Accessory Shops into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("AccessoryShopIcon.png", "XC2")
    return desc