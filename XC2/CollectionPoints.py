import Options, IDs, json, random
from scripts import Helper
def RandoCollectionPoints():
    ValidReplacements = []
    if Options.CollectionPointsOption_Accessories.GetState():
        ValidReplacements.extend(IDs.Accessories)
    if Options.CollectionPointsOption_TornaAccessories.GetState():
        ValidReplacements.extend(IDs.TornaAccessories)
    if Options.CollectionPointsOption_WeaponChips.GetState():
        ValidReplacements.extend(IDs.WeaponChips)
    if Options.CollectionPointsOption_AuxCores.GetState():
        ValidReplacements.extend(IDs.AuxCores)
    if Options.CollectionPointsOption_RefinedAuxCores.GetState():
        ValidReplacements.extend(IDs.RefinedAuxCores)
    if Options.CollectionPointsOption_CoreCrystals.GetState():
        ValidReplacements.extend(IDs.CoreCrystals)
    if Options.CollectionPointsOption_Deeds.GetState():
        ValidReplacements.extend(IDs.Deeds)
    if Options.CollectionPointsOption_CollectionPointMaterials.GetState():
        ValidReplacements.extend(IDs.CollectionPointMaterials)
    odds = Options.CollectionPointsOption.GetOdds()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    for area in IDs.MajorAreaIds:
        try:
            with open(f"./XC2/_internal/JsonOutputs/common_gmk/ma{area}a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as collFile:
                collData = json.load(collFile)
                for point in collData["rows"]:
                    for i in range(1,5):
                        if not Helper.OddsCheck(odds): # Check spinbox
                            continue
                        if point[f"itm{i}ID"] == 0: # Ignore empty spots in points
                            continue
                        point[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
                collFile.seek(0)
                collFile.truncate()
                json.dump(collData, collFile, indent=2, ensure_ascii=False)
        except:
            pass # Ignores wrong files
