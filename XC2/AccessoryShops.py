import Options, IDs, json, random
from scripts import Helper
def RandoAccessoryShops():
    ValidReplacements = []
    if Options.AccessoryShopsOption_Accessories.GetState():
        ValidReplacements.append(IDs.Accessories)
    if Options.AccessoryShopsOption_TornaAccessories.GetState():
        ValidReplacements.append(IDs.TornaAccessories)
    if Options.AccessoryShopsOption_WeaponChips.GetState():
        ValidReplacements.append(IDs.WeaponChips)
    if Options.AccessoryShopsOption_AuxCores.GetState():
        ValidReplacements.append(IDs.AuxCores)
    if Options.AccessoryShopsOption_RefinedAuxCores.GetState():
        ValidReplacements.append(IDs.RefinedAuxCores)
    if Options.AccessoryShopsOption_CoreCrystals.GetState():
        ValidReplacements.append(IDs.CoreCrystals)
    if Options.AccessoryShopsOption_Deeds.GetState():
        ValidReplacements.append(IDs.Deeds)
    if Options.AccessoryShopsOption_PouchItems.GetState():
        ValidReplacements.append(IDs.PouchItems)
    if Options.AccessoryShopsOption_CollectionPointMaterials.GetState():
        ValidReplacements.append(IDs.CollectionPointMaterials)
    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        odds = Options.AccessoryShopsOption.GetOdds()
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