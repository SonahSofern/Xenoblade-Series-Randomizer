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
    odds = Options.TreasureChestOption.GetOdds()

    
    if ValidReplacements == []: # In case they dont select anything
        return
    
    for area in IDs.MajorAreaIds:
        try:
            with open(f"./_internal/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as collFile:
                collData = json.load(collFile)
                for point in collData["rows"]:
                    for i in range(1,4):
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

#TreasureChestOption = Option("Treasure Chests", General, "Randomizes the contents of Treasure Chests", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID","itm5ID","itm6ID","itm7ID","itm8ID"], Accessories + Boosters + WeaponChips + AuxCores + CoreCrystals + RefinedAuxCores,[])], _hasSpinBox = True)
