from XCXDE.XCXDE_Scripts import IDs, Options
from scripts import JSONParser, Helper, StatRandomizer

# Make a class that can randomize stats in a balanced way given an intensity and min and max val
# Art Unlock Order
# Class Weapon (What weapons a class uses)

# Skills (Make enhance file and option to add new skills)

# Overdrive Route Rando (Can't because theres no way to see what changed)

# Skell Weapons and Armor (Their stats and gem effects basically)

# Soul Voices https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_SoulArts.html

def SkellBaseStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    statRando = StatRandomizer.StatR(2, 16, intensity)
    
    for skell in statsFile.rows:
        if skell["$id"] not in IDs.SkellFrameIDs:
            continue
        for stat in ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "Def", "FuelMax"]:
            statRando.Balanced(skell, stat)
    
    statsFile.Close()