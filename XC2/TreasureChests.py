import Options, IDs, json, random
from scripts import Helper
def RandoTreasureBoxes():
    ValidReplacements = []
    if Options.TreasureChestOption_Accessories.GetState():
        ValidReplacements.append(IDs.Accessories)
    if Options.TreasureChestOption_TornaAccessories.GetState():
        ValidReplacements.append(IDs.TornaAccessories)
    if Options.TreasureChestOption_WeaponChips.GetState():
        ValidReplacements.append(IDs.WeaponChips)
    if Options.TreasureChestOption_AuxCores.GetState():
        ValidReplacements.append(IDs.AuxCores)
    if Options.TreasureChestOption_RefinedAuxCores.GetState():
        ValidReplacements.append(IDs.RefinedAuxCores)
    if Options.TreasureChestOption_CoreCrystals.GetState():
        ValidReplacements.append(IDs.CoreCrystals)
    if Options.TreasureChestOption_Deeds.GetState():
        ValidReplacements.append(IDs.Deeds)
    if Options.TreasureChestOption_CollectionPointMaterials.GetState():
        ValidReplacements.append(IDs.CollectionPointMaterials)
    odds = Options.TreasureChestOption.GetOdds()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    for area in IDs.MajorAreaIds:
        try:
            with open(f"./_internal/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as tboxFile:
                boxData = json.load(tboxFile)
                for box in boxData["rows"]:
                    for i in range(1,9):
                        if not Helper.OddsCheck(odds): # Check spinbox
                            continue
                        if box[f"itm{i}ID"] == 0: # Ignore empty spots in points
                            continue
                        box[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
                tboxFile.seek(0)
                tboxFile.truncate()
                json.dump(boxData, tboxFile, indent=2, ensure_ascii=False)
        except:
            pass # Ignores wrong files
