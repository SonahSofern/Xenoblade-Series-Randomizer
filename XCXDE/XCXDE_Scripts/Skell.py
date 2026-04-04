from XCXDE.XCXDE_Scripts import IDs, Options

from scripts import JSONParser, Helper

# Make a class that can randomize stats in a balanced way given an intensity and min and max val

# Chosen on an individual basis not by users
minVal = .1
maxVal = 3

intensity = 10 # Chosen by users from 1-10

valuesToGen = 10
mid = 1

mults = []
variance = intensity * 0.1
for i in range(1,valuesToGen):
    # Choose a value based on intensity
    change = round(Helper.random.uniform(0.1, variance), 1)
    firstTest = Helper.random.randrange(1,intensity*100)/100 # This number represents how hard we deviate (Its random but gets higher and lower depending on intensity)
    chosen = Helper.Clamp(firstTest, minVal, maxVal)
    
    # Add the positive and inverse of the number
    mults.append(chosen)
    mults.append(1/chosen)


print(mults)


def SkellBaseStats():
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    validSkellIDs = []
    
    
    for skell in statsFile.rows:
        if skell["$id"] not in validSkellIDs:
            continue
            
        
    statsFile.Close()