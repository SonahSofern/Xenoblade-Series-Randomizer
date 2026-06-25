from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, Helper, StatRand, PopupDescriptions


def SkellBaseStats(intensity):
    statsFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    statRando = StatRand.Stat(2, intensity)
    
    for skell in statsFile.rows:
        if skell["$id"] not in IDs.SkellFrameIDs:
            continue
        for stat in ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "Def", "FuelMax"]:
            statRando.ApplyMult(skell, stat, statRando.RollBalancedMult(), StatRand.b16)
    
    statsFile.Close()

def ArmorStats(intensity, fileName, statKeys, affixMax, slotMax):
    amrFile = JSONParser.File(f"XCXDE/JsonOutputs/common/{fileName}.json")
    statRando = StatRand.Stat(2, intensity)
    
    for amr in amrFile.rows:
        for stat in statKeys:
            statRando.ApplyMult(amr, stat, statRando.RollBalancedMult(), StatRand.b16)
        for stat in ["RstPhysics", "RstBeam", "RstDM", "RstFire", "RstVolt", "RstGravity"]:
            statRando.ApplyMult(amr, stat, statRando.RollBalancedMult(), 100, -100)
        amr["AffixCount"] = Helper.random.choice(Helper.InclRange(1, affixMax))
        amr["SlotNum"] = Helper.random.choice(Helper.InclRange(1, slotMax))
    
    amrFile.Close()

maxMult = 2

def WeaponStats(intensity, fileName, affixMax, slotMax):
    statsFile = JSONParser.File(f"XCXDE/JsonOutputs/common/{fileName}.json")
    statRando = StatRand.Stat(maxMult, intensity)
    
    for wep in statsFile.rows:
        if wep["$id"] not in IDs.SkellWeaponIDs:
            continue
        for stat in ["Damage", "DMRatio", "Recast"]:
            statRando.ApplyMult(wep, stat, statRando.RollBalancedMult(), StatRand.b16, -StatRand.b16)
        for stat in ["Stability", "Magazine"]:
            statRando.ApplyMult(wep, stat, statRando.RollBalancedMult(), StatRand.b8)
        # for stat in ["EquLv"]:
        #     statRando.ApplyMult(wep, stat, statRando.RollBalancedMult(), 60, 10)
        wep["AffixCount"] = Helper.random.choice(Helper.InclRange(1, affixMax))
        wep["SlotNum"] = Helper.random.choice(Helper.InclRange(1, slotMax))
    
    statsFile.Close()

def SkellArtRando(intensity):
    dlArtsFile = JSONParser.File(f"XCXDE/JsonOutputs/common/BTL_DlArtsList.json")
    statR = StatRand.Stat(maxMult, intensity)
            
    for wpn in dlArtsFile.rows:
        for stat in ["Fuel", "DmgMgn"]:
            statR.ApplyMult(wpn, stat, statR.RollBalancedMult())

    dlArtsFile.Close()
  
def SkellArmorStats(intensity):
    ArmorStats(intensity, "AMR_DlList", ["Hp", "def"], 8, 3)
    
def PlayerArmorStats(intensity):
    ArmorStats(intensity, "AMR_PcList", ["def"], 16, 1)
    
def SkellWepStats(intensity):
    WeaponStats(intensity, "WPN_DlList", 8, 3)
    SkellArtRando(intensity)

def PlayerWepStats(intensity):
    WeaponStats(intensity, "WPN_PcList", 15, 3)
    
def GearDesc(armorName, wepName):
    gearDesc = PopupDescriptions.Description()
    gearDesc.Header(armorName)
    gearDesc.Text("Multiplies the def, resistances and slots of armor by a random multiplier")
    gearDesc.Header(wepName)
    gearDesc.Text("Multiplies the attack, stability, magazine, cooldown and slots of weapons by a random multiplier")
    gearDesc.Header("Intensity")
    gearDesc.Text(StatRand.IntensityDescription)
    return gearDesc