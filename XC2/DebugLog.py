import random, json
from scripts import Helper
def CreateDebugLog(OptionsRunDict, Version, randoSeedEntry):
    if OptionsRunDict["Create Debug Log"]["optionTypeVal"].get():
        Range1 = Helper.InclRange(1, 100)
        Range2 = Helper.InclRange(1, 10000)
        rngmuddling1 = random.choice(Range1)
        tbd = "To Be Added"
        for i in range(0, rngmuddling1): # this ensures that if this option is on, the seed hash will be different
            rngmuddling2 = random.choice(Range2)
        global debugfilename
        debugfilename = f"D:/XC2 Rando Debug Logs/{randoSeedEntry}.txt"
        debugfile = open(debugfilename, "w", encoding= "utf-8")
        debugfile.write(f"Xenoblade 2 Randomizer Version {Version}\n")
        debugfile.write(f"Permalink {tbd}\n\n")
        debugfile.write(f"Seed Name: {randoSeedEntry}\n\n")
        debugfile.write("Options Selected:\n")
        OptionName = []
        OptionVal = []
        for option in OptionsRunDict.values(): # for each option
            OptionName = option["name"]    
            OptionVal = option["optionTypeVal"].get()
            if (type(OptionVal) != int) & (OptionVal == True): # if the option is a checkbox and checked
                debugfile.write(f" {OptionName};")
            if (type(OptionVal) == int) & (OptionVal != 0): # slider and not 0
                debugfile.write(f" {OptionName}: {OptionVal};")
        debugfile.write("\n\n")
        debugfile.write("Suboptions Selected:\n")
        for option in OptionsRunDict.values():
            optionName = option["name"]
            for subOption in option["subOptionObjects"].values(): # looping through all suboptions
                SubOptionName = subOption["subName"]
                SubOptionVal = subOption["subOptionTypeVal"].get()
                if (type(SubOptionVal) != int) & (SubOptionVal == True): # if the suboption is a checkbox and checked
                    debugfile.write(f" {optionName}: {SubOptionName};")
                if (type(SubOptionVal) == int) & (SubOptionVal != 0): # if the suboption is a slider and not 0
                    debugfile.write(f" {optionName}: {SubOptionName}: {SubOptionVal};")
        debugfile.write("\n")   
        debugfile.close()
        debugfileread = open(debugfilename, "r", encoding= "utf-8")
        alllines = debugfileread.readlines()
        alllines[6] = alllines[6][1:]
        alllines[6] = alllines[6][:-2]
        alllines[6] += "\n"
        alllines[9] = alllines[9][1:]
        alllines[9] = alllines[9][:-2]
        alllines[9] += "\n"
        debugfilewrite = open(debugfilename, "w", encoding= "utf-8")
        debugfilewrite.writelines(alllines)
        debugfilewrite.close()
            
def AppendSeedHash(seedhash):
    debugfileread = open(debugfilename, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines[2] = f"Seed Hash: {seedhash}\n"
    debugfilewrite = open(debugfilename, "w", encoding= "utf-8")
    debugfilewrite.writelines(alllines)
    debugfilewrite.close()

def DebugCoreCrystalAddition(ValidCrystalListIDs, CorrespondingBladeNames):
    TreasureBoxestoCheck = ['./_internal/JsonOutputs/common_gmk/ma05a_FLD_TboxPop.json', "./_internal/JsonOutputs/common_gmk/ma10a_FLD_TboxPop.json", './_internal/JsonOutputs/common_gmk/ma07a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma08a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma15a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma11a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma13a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma16a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma17a_FLD_TboxPop.json', "./_internal/JsonOutputs/common_gmk/ma18a_FLD_TboxPop.json", './_internal/JsonOutputs/common_gmk/ma20a_FLD_TboxPop.json', './_internal/JsonOutputs/common_gmk/ma21a_FLD_TboxPop.json']
    debugfileread = open(debugfilename, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines.append("\n")
    alllines.append("Core Crystal IDs, Blade Names, and Chest Number\n")
    for i in range(0, len(ValidCrystalListIDs)):
        ChestFound = []
        for j in range(0, len(TreasureBoxestoCheck)):
            for k in range(1, 9):
                ChestFound.extend((Helper.FindValues(TreasureBoxestoCheck[j], [f"itm{k}ID"], [ValidCrystalListIDs[i]],"$id")))
        ChestFound.sort()
        alllines.append(f"Crystal ID: {ValidCrystalListIDs[i]}; Name: {CorrespondingBladeNames[i]}; Chests: {', '.join(str(ChestID) for ChestID in ChestFound)}\n")
    alllines.append("\n")
    debugfilewrite = open(debugfilename, "w", encoding= "utf-8")
    debugfilewrite.writelines(alllines)
    debugfilewrite.close()

def DebugZoharLocations(ZoharChestIDs):
    debugfileread = open(debugfilename, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines.append("\n")
    alllines.append("Zohar Chest IDs:\n")
    for i in range(0, len(ZoharChestIDs)):
        alllines.append(f"{ZoharChestIDs[i]}\n")
    debugfilewrite = open(debugfilename, "w", encoding= "utf-8")
    debugfilewrite.writelines(alllines)
    debugfilewrite.close()

def DebugMovespeed():
    DeedTypeIDValues = Helper.InclRange(1, 51)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["Type"] in DeedTypeIDValues:
                row["Caption"] = 603 # Increases running speed by 5%
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in DeedTypeIDValues:
                row["Value"] = 100
                row["Type"] = 1
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 250%
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Max"] = 1000
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes name of deed
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] >= 25249) & (row["$id"] <= 25299):
                row["Caption"] = 603
            if row["$id"] > 25299:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] >= 491) & (row["$id"] < 542):
                row["name"] = "Movespeed Deed"
            if row["$id"] == 542:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 209:
                row["itm1ID"] = 25249
                row["itm1Num"] = 1
                row["itm2ID"] = 25250
                row["itm2Num"] = 1
                row["itm3ID"] = 25251
                row["itm3Num"] = 1
                row["itm4ID"] = 25252
                row["itm4Num"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)