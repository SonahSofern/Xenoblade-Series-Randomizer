import Options, IDs, json, random
from scripts import Helper
def RandoPouchShops():
    ValidReplacements = []
    if Options.PouchItemShopOption_Accessories.GetState():
        ValidReplacements.append(IDs.Accessories)
    if Options.PouchItemShopOption_TornaAccessories.GetState():
        ValidReplacements.append(IDs.TornaAccessories)
    if Options.PouchItemShopOption_WeaponChips.GetState():
        ValidReplacements.append(IDs.WeaponChips)
    if Options.PouchItemShopOption_AuxCores.GetState():
        ValidReplacements.append(IDs.AuxCores)
    if Options.PouchItemShopOption_RefinedAuxCores.GetState():
        ValidReplacements.append(IDs.RefinedAuxCores)
    if Options.PouchItemShopOption_CoreCrystals.GetState():
        ValidReplacements.append(IDs.CoreCrystals)
    if Options.PouchItemShopOption_Deeds.GetState():
        ValidReplacements.append(IDs.Deeds)
    if Options.PouchItemShopOption_PouchItems.GetState():
        ValidReplacements.append(IDs.PouchItems)
    if Options.PouchItemShopOption_CollectionPointMaterials.GetState():
        ValidReplacements.append(IDs.CollectionPointMaterials)
        
    odds = Options.PouchItemShopOption.GetOdds()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    with open("./_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        odds = Options.PouchItemShopOption.GetOdds()
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
