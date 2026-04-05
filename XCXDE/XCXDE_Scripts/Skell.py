from XCXDE.XCXDE_Scripts import IDs, Options

from scripts import JSONParser, Helper

# Make a class that can randomize stats in a balanced way given an intensity and min and max val
# Art Unlock Order
# Class Weapon (What weapons a class uses)

# Skills (Make enhance file and option to add new skills)

# Overdrive Route Rando (Can't because theres no way to see what changed)

# Skell (Stats)
# Skell Weapons and Armor (Their stats and gem effects basically)

# Soul Voices https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_SoulArts.html

class NumberRando():
    def __init__(self, maxChangePercent, neutralChangePercent = 100):
        self.maxChangePercent = maxChangePercent
        self.neutralChangePercenet = neutralChangePercent

    def GetBalancedRandomMult(self, intensity, reverseChance = 50):
        '''Generally gets multipliers according to intensity, eg. intensity 90 with max at 300% gets you 90% towards the max so up to 270% variance'''
        percVariance = intensity * .01
        maxWithIntensity = percVariance * self.maxChangePercent

        chosenMult = Helper.random.randrange(self.neutralChangePercenet, maxWithIntensity) # Choose a mult between neutral and max*intensity
        
        if Helper.OddsCheck(reverseChance):
            return 100/chosenMult
        else:
            return chosenMult


def SkellBaseStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    
    
    for skell in statsFile.rows:
        if skell["$id"] not in IDs.SkellFrameIDs:
            continue
        for stat in ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "Def", "FuelMax"]:
            skell[stat] = NumberRando(200).GetBalancedRandomMult(intensity) # Pass the skell[stat] into the function and rename it the name blows
            
        
    statsFile.Close()