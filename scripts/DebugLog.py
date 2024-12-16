import random, Helper

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
