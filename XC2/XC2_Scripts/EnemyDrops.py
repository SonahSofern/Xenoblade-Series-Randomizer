from XC2.XC2_Scripts import Options, IDs
import json, random
from scripts import Helper
def RandoEnemyDrops():
    ValidReplacements = []
    if Options.EnemyDropOption_Accessories.GetState():
        ValidReplacements.extend(IDs.Accessories)
    if Options.EnemyDropOption_TornaAccessories.GetState():
        ValidReplacements.extend(IDs.TornaAccessories)
    if Options.EnemyDropOption_WeaponChips.GetState():
        ValidReplacements.extend(IDs.WeaponChips)
    if Options.EnemyDropOption_AuxCores.GetState():
        ValidReplacements.extend(IDs.AuxCores)
    if Options.EnemyDropOption_RefinedAuxCores.GetState():
        ValidReplacements.extend(IDs.RefinedAuxCores)
    if Options.EnemyDropOption_CoreCrystals.GetState():
        ValidReplacements.extend(IDs.CoreCrystals)
    if Options.EnemyDropOption_Deeds.GetState():
        ValidReplacements.extend(IDs.Deeds)
    if Options.EnemyDropOption_CollectionPointMaterials.GetState():
        ValidReplacements.extend(IDs.CollectionPointMaterials)
    odds = Options.EnemyDropOption.GetSpinbox()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    


    with open(f"./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as enDropFile:
        enDropData = json.load(enDropFile)
        for drop in enDropData["rows"]:
            for i in range(1,9):
                if not Helper.OddsCheck(odds): # Check spinbox
                    continue
                if drop[f"ItemID{i}"] in [0, 30380] : # Ignore empty spots in points, and Feris Beastmeat for Torna
                    continue
                drop[f"ItemID{i}"] = random.choice(ValidReplacements) # Make our selection
        enDropFile.seek(0)
        enDropFile.truncate()
        json.dump(enDropData, enDropFile, indent=2, ensure_ascii=False)

# EnemyDropOption = Option("Enemy Drops", Enemies, "Randomizes enemy drops/loot", [lambda: JSONParser.ChangeJSONFile(["common/BTL_EnDropItem.json"], Helper.StartsWith("ItemID", 1, 8), AuxCores+ RefinedAuxCores + IDs.Accessories + WeaponChips, [])], _hasSpinBox = True)
