from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, Helper, StatRand

def SkellBaseStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    statRando = StatRand.Stat(2, intensity)
    
    for skell in statsFile.rows:
        if skell["$id"] not in IDs.SkellFrameIDs:
            continue
        for stat in ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "Def", "FuelMax"]:
            statRando.Balanced(skell, stat, StatRand.b16)
    
    statsFile.Close()
    
def SkellArmorStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/AMR_DlList.json")
    statRando = StatRand.Stat(2, intensity)
    
    for amr in statsFile.rows:
        if amr["$id"] not in IDs.SkellArmorIDs:
            continue
        for stat in ["Hp", "def"]:
            statRando.Balanced(amr, stat, StatRand.b16)
        for stat in ["RstPhysics", "RstBeam", "RstDM", "RstFire", "RstVolt", "RstGravity"]:
            statRando.Balanced(amr, stat, 100, -100)
            
        amr["AffixCount"] = Helper.random.choice(Helper.InclRange(1,8))
        amr["SlotNum"] = Helper.random.choice(Helper.InclRange(1,3))
    
    statsFile.Close()
    
def SkellWepStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/WPN_DlList.json")
    statRando = StatRand.Stat(3, intensity)
    
    for wep in statsFile.rows:
        if wep["$id"] not in IDs.SkellWeaponIDs:
            continue
        for stat in ["Damage", "DMRatio", "Recast"]:
            statRando.Balanced(wep, stat, StatRand.b16, -StatRand.b16)
        for stat in ["Stability", "Magazine"]:
            statRando.Balanced(wep, stat, StatRand.b8)
        wep["AffixCount"] = Helper.random.choice(Helper.InclRange(1,8))
        wep["SlotNum"] = Helper.random.choice(Helper.InclRange(1,3))
    
    statsFile.Close()