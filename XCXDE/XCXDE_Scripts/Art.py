from scripts import JSONParser, StatRand, Helper, PopupDescriptions
from XCXDE.XCXDE_Scripts import IDs, Options

maxMult = 2

def ArtStatRando(intensity):
    ArtStats(intensity)
    ArtEnhancements(intensity)

def ArtStats(intensity):
    artFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    statRando = StatRand.Stat(maxMult, intensity)
    
    for art in artFile.rows:
        for stat in ["DmgMgn", "RecastFrm"]:
            mult = statRando.RollBalancedMult()
            for i in range(0,5):
                    statRando.ApplyMult(art, f"{stat}[{i}]", mult)
    artFile.Close()
    
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

def ArtUnlockOrder():
    ArtOrder()
    FixStartingArts()

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
    
    def RollArt(group:Helper.RandomGroup, newLearnList = []):
        '''Choose until we get a non duplicate art'''
        newLearn = group.SelectRandomMember()
        rollCount = 0
        while newLearn in newLearnList:
            newLearn = group.SelectRandomMember()
            
            # Because you can get a melee art in am originally ranged position it can lead to situation where you have to entire melee group and are still trying to get another melee art in that case you just dont get an art
            rollCount += 1
            if rollCount > 30:
                newLearn = 0
                break
            
        return newLearn
    
    for i in range(1,39):
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{i:02}Growth.json")
        
        classGroup:XCXClass = None 
        for cls in AllClasses:
            if i in cls.classIndexes:
                classGroup = cls
                break
        if classGroup == None:
            return
            
        newLearnList = [] # Keeps track of what arts this class already has
        
        for rank in growFile.rows:
            meleeLearn = rank[f"LearnArts01"]
            rangedLearn = rank[f"LearnArts02"]
            
            # You dont learn arts here
            if meleeLearn == 0 and rangedLearn == 0: continue 
            
            # You are learning 1 art, so we randomize if its melee or ranged
            elif (meleeLearn != 0 and rangedLearn == 0) or (meleeLearn == 0 and rangedLearn != 0): 
                if Helper.OddsCheck(50):
                    newMeleeLearn = RollArt(classGroup.melee, newLearnList)
                    newRangedLearn = 0
                else:
                    newRangedLearn = RollArt(classGroup.ranged, newLearnList)
                    newMeleeLearn = 0
            
            # You learn 2 arts at same rank you get one of each ranged and melee
            elif meleeLearn != 0 and rangedLearn != 0:
                newMeleeLearn = RollArt(classGroup.melee, newLearnList)
                newRangedLearn = RollArt(classGroup.ranged, newLearnList)
                                  
            # Assignment
            rank[f"LearnArts01"] = newMeleeLearn 
            rank[f"LearnArts02"] = newRangedLearn
            
            # Add to keep track of what we learned so far
            if newMeleeLearn != 0: newLearnList.append(newMeleeLearn) 
            if newRangedLearn != 0: newLearnList.append(newRangedLearn)
            
        growFile.Close()
        
    # multigun is weird, special thing that can be equipped by all
   
def FixStartingArts():
    # Needed to fix not just crosses, all the starting arts for characters
    chrData = JSONParser.File("XCXDE/JsonOutputs/common/DEF_PcList.json")
    playerChar = [23]
    # Loop over the characters
    for chr in chrData.rows:
        if chr["$id"] not in IDs.PartyMembersIDs + playerChar:
            continue
        
        # clear their defaults arts
        for i in range(1,9):
            chr[f"ArtsNo{i}"] = 0
            chr[f"ArtsLv{i}"] = 0
            
        # Find the new arts IDs
        clsRank = chr["ClassLevel"]
        clsType = chr["ClassType"]
        newArts = []
        
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{clsType:02}Growth.json")
        for rank in growFile.rows:
            if rank["$id"] > clsRank: break
            if rank["LearnArts01"] != 0:
                newArts.append(rank["LearnArts01"])
            if rank["LearnArts02"] != 0:
                newArts.append(rank["LearnArts02"])
        growFile.Close()
        
        # Apply new art IDs to character PcList
        for i in Helper.InclRange(1, len(newArts)):
            chr[f"ArtsNo{i}"] = newArts[i - 1]
            chr[f"ArtsLv{i}"] = 1
            
    chrData.Close()
    
                                                                                                                                                                                                                                                                                
def ArtDesc(name, newName):
    artRandoDesc = PopupDescriptions.Description()
    artRandoDesc.Header(name)
    artRandoDesc.Text(f"Randomizes art unlocking. For example, Drifter uses rifle and knife, so the drifter class will be given random knife and rifle arts from any in the game.")
    artRandoDesc.Header(newName)
    artRandoDesc.Text(f"Randomizes the strength of arts within {1/maxMult}-{maxMult} times the original amount.")
    artRandoDesc.Text(StatRand.IntensityDescription)
    return artRandoDesc