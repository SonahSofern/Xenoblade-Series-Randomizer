from scripts import JSONParser, StatRand, Helper
from XCXDE.XCXDE_Scripts import IDs

def ArtStats(intensity):
    artFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    statRando = StatRand.Stat(2, intensity)
    
    for art in artFile.rows:
        for stat in ["DmgMgn", "RecastFrm"]:
            mult = statRando.RollBalancedMult()
            for i in range(0,5):
                    statRando.ApplyMult(art, f"{stat}[{i}]", mult)
    artFile.Close()
    
    ArtEnhancements(intensity)

def ArtEnhancements(intensity):
    '''Art enhancement currently paired with stats, they are unique to arts so can be adjusted without messing with other things'''
    enhFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_Enhance.json")
    statRando = StatRand.Stat(2, intensity)
    
    for enh in enhFile.rows:
        if enh["$id"] in IDs.ArtEnhanceIDs:
            mult = statRando.RollBalancedMult()
            for stat in ["param1", "param2"]:
                statRando.ApplyMult(enh, stat, mult)
    
    enhFile.Close()
    
def ArtOrder():
    class XCXClass():
        def __init__(self, meleeWepIDs, rangedWepIDs, classIndexes):
            self.melee:Helper.RandomGroup = meleeWepIDs
            self.ranged:Helper.RandomGroup = rangedWepIDs
            self.classIndexes = classIndexes # group representing the IDs that use this weapon combo and named this (for things like psycorrupter and psycorrupter+)
            
    # Melee
    KnifeArtsIDs = Helper.RandomGroup([93,94,95,96,97,98,99,100,101,102,103,104,152,153,154])
    LongswordArtIDs = Helper.RandomGroup([55,56,57,58,59,60,61,62,139,140,141,159])
    ShieldArtIDs = Helper.RandomGroup([83,84,85,86,87,88,89,90,91,148,149,150,151])
    DualSwordsArtIDs = Helper.RandomGroup([72,73,74,75,76,77,78,79,80,81,145,146,147])
    JavelinArtIDs = Helper.RandomGroup([64,65,66,67,68,69,70,142,143,144,164])
    PhotonSaberArtIDs = Helper.RandomGroup([107,108,109,110,111,112,113,114,115,116,155,156,157,165])
    # Ranged
    AssaultRifleArtIDs = Helper.RandomGroup([2,3,4,5,6,7,8,9,10,11,12,13,14,122,123,124])
    DualGunsArtIDs = Helper.RandomGroup([25,26,27,28,29,30,31,127,128,129,160])
    GatlingGunArtIDs = Helper.RandomGroup([33,34,35,36,37,38,120,131,132])
    PsychoLauncherArtIDs = Helper.RandomGroup([48,49,50,51,52,53,136,137,138,162,163])
    RaygunArtIDs = Helper.RandomGroup([40,41,42,43,44,45,46,133,134,135,161])
    SniperArtIDs = Helper.RandomGroup([17,18,19,20,21,22,23,125,126,158])
    
    Drifter = XCXClass(KnifeArtsIDs, AssaultRifleArtIDs, [1])
    Striker = XCXClass(LongswordArtIDs, AssaultRifleArtIDs, [2])
    SamuraiGunner = XCXClass(LongswordArtIDs, AssaultRifleArtIDs, [3, 21, 22])
    Duelist = XCXClass(LongswordArtIDs, AssaultRifleArtIDs, [4, 17, 37])
    ShieldTrooper = XCXClass(ShieldArtIDs, GatlingGunArtIDs, [5, 18, 20, 28])
    BastionWarrior = XCXClass(ShieldArtIDs, GatlingGunArtIDs, [6])
    Commando = XCXClass(DualSwordsArtIDs, DualGunsArtIDs, [7])
    WingedViper = XCXClass(DualSwordsArtIDs, DualGunsArtIDs, [8, 26, 31])
    FullMetalJaguar = XCXClass(DualSwordsArtIDs, DualGunsArtIDs, [9, 27, 35])
    PartisanEagle = XCXClass(JavelinArtIDs, SniperArtIDs, [10, 19, 25, 32, 36])
    AstralCrusader = XCXClass(JavelinArtIDs, SniperArtIDs, [11])
    Enforcer = XCXClass(KnifeArtsIDs, RaygunArtIDs, [12])
    Psycorrupter = XCXClass(KnifeArtsIDs, RaygunArtIDs, [13, 29, 30, 33, 34])
    Mastermind = XCXClass(KnifeArtsIDs, RaygunArtIDs, [14])
    BlastFencer = XCXClass(PhotonSaberArtIDs, PsychoLauncherArtIDs, [15, 23, 24])
    GalacticKnight = XCXClass(PhotonSaberArtIDs, PsychoLauncherArtIDs, [16, 38])
    
    AllClasses:list[XCXClass] = [Drifter, Striker, SamuraiGunner, Duelist, ShieldTrooper, BastionWarrior, Commando, WingedViper, FullMetalJaguar, PartisanEagle, AstralCrusader, Enforcer, Psycorrupter, Mastermind, BlastFencer, GalacticKnight]
    
    for i in range(1,39):
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{i:02}Growth.json")
        
        classGroup:XCXClass = None 
        for cls in AllClasses:
            if i in cls.classIndexes:
                classGroup = cls
                break
        if classGroup == None:
            return
            
        for rank in growFile.rows:
            meleeLearn = rank[f"LearnArts01"]
            rangedLearn = rank[f"LearnArts02"]
            
            if meleeLearn == 0 and rangedLearn == 0: continue # You dont learn arts here
            
            # You are learning 1 art, so we randomize if its melee or ranged
            if (meleeLearn != 0 and rangedLearn == 0) or (meleeLearn == 0 and rangedLearn != 0): 
                if Helper.OddsCheck(50):
                    meleeLearn = classGroup.melee.SelectRandomMember()
                else:
                    rangedLearn = classGroup.ranged.SelectRandomMember()
            
             # You learn 2 arts at same rank you get one of each ranged and melee
            if meleeLearn != 0 and rangedLearn != 0:
                meleeLearn = classGroup.melee.SelectRandomMember()
                rangedLearn = classGroup.ranged.SelectRandomMember()
            
            # Assignment
            rank[f"LearnArts01"] = meleeLearn 
            rank[f"LearnArts02"] = rangedLearn
            
        growFile.Close()
        
    # multigun is weird, special thing that can be equipped by all