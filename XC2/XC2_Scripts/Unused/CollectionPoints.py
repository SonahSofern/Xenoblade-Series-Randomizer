from XC2.XC2_Scripts import Options, IDs
import  json, random
from scripts import Helper, PopupDescriptions
def RandoCollectionPoints():
    ValidReplacements = []
    if Options.CollectionPointsOption_Accessories.GetState():
        ValidReplacements.extend(IDs.AccessoryIDs)
    if Options.CollectionPointsOption_TornaAccessories.GetState():
        ValidReplacements.extend(IDs.TornaAccessories)
    if Options.CollectionPointsOption_WeaponChips.GetState():
        ValidReplacements.extend(IDs.WeaponChipIDs)
    if Options.CollectionPointsOption_AuxCores.GetState():
        ValidReplacements.extend(IDs.AuxCoreIDs)
    if Options.CollectionPointsOption_RefinedAuxCores.GetState():
        ValidReplacements.extend(IDs.RefinedAuxCores)
    if Options.CollectionPointsOption_CoreCrystals.GetState():
        ValidReplacements.extend(IDs.CoreCrystals)
    if Options.CollectionPointsOption_Deeds.GetState():
        ValidReplacements.extend(IDs.Deeds)
    if Options.CollectionPointsOption_CollectionPointMaterials.GetState():
        ValidReplacements.extend(IDs.CollectionPointMaterials)
    odds = Options.CollectionPointsOption.GetSpinbox()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    MajorAreaCopy = IDs.MajorAreaIds
    for area in MajorAreaCopy:
        try:
            with open(f"./XC2/JsonOutputs/common_gmk/ma{area}a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as collFile:
                collData = json.load(collFile)
                for point in collData["rows"]:
                    for i in range(1,5):
                        if not Helper.OddsCheck(odds): # Check spinbox
                            continue
                        if point[f"itm{i}ID"] in [0, 30019]: # Ignore empty spots in points and puzzletree wood
                            continue
                        point[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
                collFile.seek(0)
                collFile.truncate()
                json.dump(collData, collFile, indent=2, ensure_ascii=False)
        except:
            MajorAreaCopy.remove(area)
            pass # Ignores wrong files
    print(MajorAreaCopy)

# CollectionPointsOption = Option("Collection Points", Items, "Randomizes the contents of Collection Points", [lambda: CollectionPoints.RandoCollectionPoints()], hasSpinBox = True, descData=lambda: CollectionPoints.CollectionPointDescriptions())
# CollectionPointsOption_Accessories = SubOption("Accessories", CollectionPointsOption)
# CollectionPointsOption_TornaAccessories = SubOption("Torna Accessories", CollectionPointsOption, defState=False)
# CollectionPointsOption_WeaponChips = SubOption("Weapon Chips", CollectionPointsOption)
# CollectionPointsOption_AuxCores = SubOption("Aux Cores", CollectionPointsOption, defState=False)
# CollectionPointsOption_RefinedAuxCores = SubOption("Refined Aux Cores", CollectionPointsOption)
# CollectionPointsOption_CoreCrystals = SubOption("Core Crystals", CollectionPointsOption)
# CollectionPointsOption_Deeds = SubOption("Shop Deeds", CollectionPointsOption)
# CollectionPointsOption_CollectionPointMaterials = SubOption("Collection Point Materials", CollectionPointsOption)