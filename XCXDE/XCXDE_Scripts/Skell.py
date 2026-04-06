from XCXDE.XCXDE_Scripts import IDs
from scripts import Fmr, JSONParser, Helper

# Make a class that can randomize stats in a balanced way given an intensity and min and max val
# Art Unlock Order
# Class Weapon (What weapons a class uses)

# Skills (Make enhance file and option to add new skills)

# Overdrive Route Rando (Can't because theres no way to see what changed)

# Skell Weapons and Armor (Their stats and gem effects basically)

# Soul Voices https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_SoulArts.html

def SkellBaseStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    statRando = Fmr.Stat(2, intensity)
    
    for skell in statsFile.rows:
        if skell["$id"] not in IDs.SkellFrameIDs:
            continue
        for stat in ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "Def", "FuelMax"]:
            statRando.Balanced(skell, stat, Fmr.b16)
    
    statsFile.Close()
    
def SkellArmorStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/AMR_DlList.json")
    statRando = Fmr.Stat(2, intensity)
    
    for amr in statsFile.rows:
        if amr["$id"] not in IDs.SkellArmorIDs:
            continue
        for stat in ["Hp", "def", "RstPhysics", "RstBeam", "RstDM", "RstFire", "RstVolt", "RstGravity"]:
            statRando.Balanced(amr, stat, Fmr.b16)
            
        amr["AffixCount"] = Helper.random.choice(Helper.InclRange(1,8))
        amr["SlotNum"] = Helper.random.choice(Helper.InclRange(1,3))
    
    statsFile.Close()
    
def SkellWepStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/WPN_DlList.json")
    statRando = Fmr.Stat(3, intensity)
    
    for wep in statsFile.rows:
        if wep["$id"] not in IDs.SkellWeaponIDs:
            continue
        for stat in ["Damage", "Stability", "Magazine", "DMRatio", "Recast"]:
            statRando.Balanced(wep, stat, Fmr.b16, -Fmr.b16)
        
        wep["AffixCount"] = Helper.random.choice(Helper.InclRange(1,8))
        wep["SlotNum"] = Helper.random.choice(Helper.InclRange(1,3))
    
    statsFile.Close()