import Options, IDs, json, random
from scripts import Helper, PopupDescriptions
def RandoTreasureBoxes():
    ValidReplacements = []
    if not Options.RaceModeOption.GetState(): # if race mode is on, we don't want to do any of this
        if Options.TreasureChestOption_Accessories.GetState():
            ValidReplacements.extend(IDs.Accessories)
        if Options.TreasureChestOption_TornaAccessories.GetState():
            ValidReplacements.extend(IDs.TornaAccessories)
        if Options.TreasureChestOption_WeaponChips.GetState():
            ValidReplacements.extend(IDs.WeaponChips)
        if Options.TreasureChestOption_AuxCores.GetState():
            ValidReplacements.extend(IDs.AuxCores)
        if Options.TreasureChestOption_RefinedAuxCores.GetState():
            ValidReplacements.extend(IDs.RefinedAuxCores)
        if Options.TreasureChestOption_CoreCrystals.GetState() and not Options.CustomCoreCrystalOption.GetState():
                ValidReplacements.extend(IDs.CoreCrystals)
        if Options.TreasureChestOption_Deeds.GetState():
            if not Options.StartwithIncreasedMovespeedOption.GetState(): # if we have the bonus movespeed starting deed on, we want to exclude it from the deeds found in chests.
                ValidReplacements.extend(IDs.Deeds)
            else:
                ValidReplacements.extend(Helper.InclRange(25250, 25300))
        if Options.TreasureChestOption_CollectionPointMaterials.GetState():
            ValidReplacements.extend(IDs.CollectionPointMaterials)
    odds = Options.TreasureChestOption.GetSpinbox()

    if ValidReplacements == []: # In case they dont select anything
        return
    
    for area in IDs.MajorAreaIds:
        try:
            with open(f"./XC2/_internal/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as tboxFile:
                boxData = json.load(tboxFile)
                for box in boxData["rows"]:
                    for i in range(1,9):
                        if not Helper.OddsCheck(odds): # Check spinbox
                            continue
                        if box[f"itm{i}ID"] in [0] + IDs.PreciousItems: # Ignore empty spots in points
                            continue
                        box[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
                tboxFile.seek(0)
                tboxFile.truncate()
                json.dump(boxData, tboxFile, indent=2, ensure_ascii=False)
        except:
            pass # Ignores wrong files


def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option randomizes a % of all non-key items in Treasure Chests into the types of items chosen from suboptions.")
    myDesc.Text("If no sub-options are selected this will do nothing.")
    myDesc.Image("TreasureChest.png", "XC2")
    return myDesc