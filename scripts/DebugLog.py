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
        debugfile.write(f"Seed Name: {randoSeedEntry}\n")
        debugfile.write("Options Selected:\n")
        OptionName = []
        OptionVal = []
        SubOptionObjects = []
        for option in OptionsRunDict.values(): # for each option
            OptionName = option["name"]    
            OptionVal = option["optionTypeVal"].get()
            if (type(OptionVal) != int) & (OptionVal == True): # if the option is a checkbox and checked
                debugfile.write(f" {OptionName};")
            if (type(OptionVal) == int) & (OptionVal != 0): # slider and not 0
                debugfile.write(f" {OptionName}: {OptionVal};")
        debugfile.write("\n")
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
        alllines[5] = alllines[5][1:]
        alllines[5] = alllines[5][:-2]
        alllines[5] += "\n"
        alllines[7] = alllines[7][1:]
        alllines[7] = alllines[7][:-2]
        alllines[7] += "\n"
        debugfilewritten = open(debugfilename, "w", encoding= "utf-8")
        debugfilewritten.writelines(alllines)
        debugfilewritten.close()
    return debugfilename
            
def AppendSeedHash():
    debugfileread = open(debugfilename, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines[2] = f"Seed Hash: {debugfilename}\n"
    debugfilewritten = open(debugfilename, "w", encoding= "utf-8")
    debugfilewritten.writelines(alllines)
    debugfilewritten.close()

def DebugCoreCrystalAddition(ValidCrystalListIDs, CorrespondingBladeNames):
    debugfileread = open(debugfilename, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
