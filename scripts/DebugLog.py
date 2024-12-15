import random, Helper

def CreateDebugLog(OptionsRunDict, Version, randoSeedEntry):
    if OptionsRunDict["Create Debug Log"]["optionTypeVal"].get():
        Range1 = Helper.InclRange(1, 100)
        Range2 = Helper.InclRange(1, 10000)
        rngmuddling1 = random.choice(Range1)
        tbd = "To Be Added"
        for i in range(0, rngmuddling1): # this ensures that if this option is on, the seed hash will be different
            rngmuddling2 = random.choice(Range2)
        debugfilename = f"D:/XC2 Rando Debug Logs/{randoSeedEntry}.txt"
        debugfile = open(debugfilename, "w", encoding= "utf-8")
        debugfile.write(f"Xenoblade 2 Randomizer Version {Version}\n")
        debugfile.write(f"Permalink {tbd}\n\n")
        debugfile.write(f"Seed Name: {randoSeedEntry}\n")
        debugfile.write("Options Selected:\n")
        for option in OptionsRunDict.values():
            CurOptionName = option["name"]
            CurOptionVal = option["optionTypeVal"].get()
            OptionOn = 0
            if type(CurOptionVal) != int:
                if CurOptionVal == True:
                    debugfile.write(f"{CurOptionName}; ")
                    OptionOn = 1
            if type(CurOptionVal) == int:
                if CurOptionVal != 0:
                    debugfile.write(f"{CurOptionName}: {CurOptionVal}; ")
                    OptionOn = 1
            if OptionOn == 1:    
                for subOption in option["subOptionObjects"].values():
                    CurSubOptionName = subOption["subName"]
                    CurSubOptionVal = subOption["subOptionTypeVal"].get()
                    if type(CurSubOptionVal) != int:
                        if CurSubOptionVal == True:
                            debugfile.write(f"{CurSubOptionName}, ")
                    if type(CurSubOptionVal) == int:
                        if CurSubOptionVal != 0:
                            debugfile.write(f"{CurSubOptionName}: {CurSubOptionVal}, ")
                debugfile.write("; ")
        debugfile.write("\n")
        debugfile.close()
    return debugfilename
            
def AppendSeedHash(SeedHash, DebugFile):
    debugfileread = open(DebugFile, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines[2] = f"Seed Hash: {SeedHash}\n"
    debugfilewritten = open(DebugFile, "w", encoding= "utf-8")
    debugfilewritten.writelines(alllines)
    debugfilewritten.close()
