import random, Helper

def CreateDebugLog(OptionsRunDict):
    if OptionsRunDict["Create Debug Log"]["optionTypeVal"].get():
        Range1 = Helper.InclRange(1, 100)
        Range2 = Helper.InclRange(1, 10000)
        rngmuddling1 = random.choice(Range1)
        for i in range(0, rngmuddling1): # this ensures that if this option is on, the seed hash will be different
            rngmuddling2 = random.choice(Range2)

            
        
    