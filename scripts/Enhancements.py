import JSONParser, Helper, random

EnhanceEffectsList = []
ID = 4000
class EnhanceEff:
    
    def __init__(self, Enhancement, Caption = 0,  Param1 = [], Param2 = []):
        global ID
        if Param1 == []:
            Param1Val = 0
        elif len(Param1) == 1:
            Param1Val = Param1[0]
        else:
            Param1Val = random.randrange(Param1[0],Param1[1])
            
        if Param2 == []:
            Param2Val = 0   
        elif len(Param2) == 1:
            Param2Val = Param2[0]
        else:
            Param2Val = random.randrange(Param2[0], Param2[1])    
        
        EnhanceEffectsDict = {
            "$id": ID,
            "EnhanceEffect": Enhancement,
            "Param1":  Param1Val,
            "Param2": Param2Val,
            "Caption": Caption,
            "Caption2": Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])
        ID += 1

def IncreaseEffectCaps(NewCap):
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], [Helper.InclRange(1,1000)], [NewCap])
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[45], ["Param"], random.randrange(1,50)) # Battle damage up after a certain time uses nonstandard parameter this fixes it

    

def CreateEnhanceObjects():     # update the ids when i make more they only go to 4000
    Baby = [1,5]
    Mini = [1,20]
    Small = [10,50]
    Medium = [20,100]
    Large  = [30,300]
    Mega = [60,600]
    Massive = [300,1500]
    Giga = [1000, 3000]
    
    HPBoost =       EnhanceEff(1,1, Small)
    StrengthBoost = EnhanceEff(2,2, Small)
    EtherBoost = EnhanceEff(3,3, Small)
    DexBoost = EnhanceEff(4,4, Small)
    AgiBoost = EnhanceEff(5,5, Small)
    LuckBoost = EnhanceEff(6,6, Small)
    CritBoost = EnhanceEff(7,7, Medium)
    PhysDefBoost = EnhanceEff(8,8, Medium)
    EthDefBoost = EnhanceEff(9,9, Medium)
    BlockBoost = EnhanceEff(10,10, Medium)
    FlatHPBoost = EnhanceEff(11,11, [100,1200])
    FlatStrengthBoost = EnhanceEff(12,12, Medium)
    FlatEtherBoost = EnhanceEff(13,13, Medium)
    FlatDexBoost = EnhanceEff(14,14, Large)
    FlatAgiBoost = EnhanceEff(15,15, Small)
    FlatLuckBoost =EnhanceEff(16,16, Medium)
    FlatCritBoost = EnhanceEff(17,17, Small)
    FlatDefBoost = EnhanceEff(18,18, Mini)
    FlatEthDefBoost = EnhanceEff(19,19,Mini)
    FlatBlockBoost = EnhanceEff(20,20,Mini)
    TitanDamageUp = EnhanceEff(21,222,[6], Mega)
    MachineDamageUp = EnhanceEff(21, 221, [5], Large)
    HumanoidDamageUp = EnhanceEff(21, 220, [4], Large)
    AquaticDamageUp = EnhanceEff(21, 219, [3], Mega)
    AerialDamageUp = EnhanceEff(21, 218, [2], Large)
    InsectDamageUp = EnhanceEff(21, 217, [1], Large)
    BeastDamageUp = EnhanceEff(21, 216, [0], Large)
    TitanExecute = EnhanceEff(22, 229, [6], Baby)
    MachineExecute = EnhanceEff(22, 228, [5], Baby)
    HumanoidExecute = EnhanceEff(22, 227, [4], Baby)
    AquaticExecute = EnhanceEff(22, 226, [3], Baby)
    AerialExecute = EnhanceEff(22, 225, [2], Baby)
    InsectExecute = EnhanceEff(22, 224, [1], Baby)
    BeastExecute = EnhanceEff(22, 223, [0], Baby)
    BladeComboDamUp = EnhanceEff(23,21, Large)
    FusionComboDamUp = EnhanceEff(24,22, Large)
    EtherCounter = EnhanceEff(25,23, Massive)
    PhysCounter = EnhanceEff(26,24, Massive) # This is interesting because jins stuned swallow uses this and inflicts blowdown from this effect want to figure out how
    AutoAttackHeal = EnhanceEff(27,26, Mini)
    SpecialHeal = EnhanceEff(28,27, Baby) # This also is used for driver art healing (according to the caption which might be wrong) want to figure this out too
    EnemyKillHeal = EnhanceEff(29,30, Medium)
    CritHeal = EnhanceEff(30,31, Small)
    CritDamageUp = EnhanceEff(31,32, Large)
    PercentDoubleAuto = EnhanceEff(32,33, Medium)
    FrontDamageUp = EnhanceEff(33,34, Large)
    SideDamageUp = EnhanceEff(34,35, Large)
    BackDamageUp = EnhanceEff(35,36, Large)
    SurpriseAttackUp = EnhanceEff(36,37, Giga)
    ToppleDamageUp = EnhanceEff(37,38, Large)
    LaunchDamageUp = EnhanceEff(38,39, Large)
    SmashDamageUp = EnhanceEff(39,40, Large)
    HigherLVEnemyDamageUp = EnhanceEff(40,41, Large)
    AllyDownDamageUp = EnhanceEff(41,42, Mega)
    GuardAnnulAttack = EnhanceEff(42,43, Medium)
    AnnulReflect = EnhanceEff(43,44, Medium)
    DamageUpWhenHpDown = EnhanceEff(44,45, Small, Large)
    BattleDurationDamageUp = EnhanceEff(45,46, Large) # Uses weird parameter see above
    DamageUpOnEnemyKill = EnhanceEff(46,47, Medium)
    BreakDurationUp = EnhanceEff(47,48, Medium)
    ToppleDurationUp = EnhanceEff(48,49, Medium)
    LaunchDurationUp = EnhanceEff(49,50, Medium)
    AutoAttackDamageUp = EnhanceEff(50,51, Mega)
    AggroedEnemyDamageUp = EnhanceEff(51,52, Large)
    IndoorsDamageUp = EnhanceEff(52,53, Medium)
    OutdoorsDamageUp = EnhanceEff(53,54, Small)
    BladeSwitchDamageUp = EnhanceEff(54,55, Small)
    OppositeGenderBladeDamageUp = EnhanceEff(55,56, Medium)
    ReduceEnemyToppleResist = EnhanceEff(56,57, Medium) # [ML:Enhance kind=Param1 ]% put that there to make game show the change?
    ReduceEnemyLaunchResist = EnhanceEff(57,58, Medium)
    OnBlockNullDamage = EnhanceEff(59, 59, Small)
    HPLowEvasion = EnhanceEff(62, 60, Small, Medium)
    EvasionWhileMoving = EnhanceEff(63, 61, Medium)
    HPLowBlockRate = EnhanceEff(64, 62, Small, Medium)
    ReduceDamageFromNearbyEnemies = EnhanceEff(65, 63, Small)
    ReduceDamageOnLowHP = EnhanceEff(66,64, Small, Small)
    HighHPDamageUp = EnhanceEff(67,65, [70,90],Large )
    ReduceSpikeDamage =EnhanceEff(68,66, Medium)
    BreakResistUp = EnhanceEff(69, 67, Medium)
    ToppleResistUp = EnhanceEff(70, 68, Medium)
    LaunchResistUp = EnhanceEff(71, 69, Medium)
    SmashResistUp = EnhanceEff(72, 70, Medium)
    BlowdownResistUp = EnhanceEff(73, 71, Medium)
    KnockbackResistUp = EnhanceEff(74, 72, Medium)
    DefenseAnnullResistUp = EnhanceEff(75, 73, Medium)
    AutoAttackAggroDown = EnhanceEff(77, 75, Large)
    AutoAttackAggroUp = EnhanceEff(78, 76, Large)
    SpecialAndArtsAggroDown = EnhanceEff(79, 77, Medium)
    # SpecialAggroDown = EnhanceEff(79, 79, Medium) uses same enchance id so idk how this works
    SpecialAndArtsAggroUp = EnhanceEff(80, 81, Medium)
    AggroReductionUp = EnhanceEff(81, 85, Small)
    AggroEverySecond = EnhanceEff(82, 86, Small) # Get UI to show the increase
    StartBattleAggro = EnhanceEff(83, 92, [1000,8000])
    RevivalHP = EnhanceEff(84, 96, Large)
    RevivalHPTeammate = EnhanceEff(85, 97, Large)
    HealingArtsUp = EnhanceEff(88, 98, Small)
    IncreaseSelfHeal = EnhanceEff(89,99, Medium)
    SpecialRechargeCancelling = EnhanceEff(92, 100, Medium)
    AutoAttackCancelDamageUp = EnhanceEff(93, 101, Medium)
    Unbeatable = EnhanceEff(94, 102, Medium)
    NightAccuracy = EnhanceEff(95, 103, Large)
    DayAccuracy = EnhanceEff(96, 104, Large)
    ExpEnemiesBoost = EnhanceEff(97, 105, Medium)
    WPEnemiesBoost = EnhanceEff(98, 106, Large)
    PartyGaugeExcellentFill = EnhanceEff(101, 109, Small) # Show amount
    PartyGaugeCritFill = EnhanceEff(102, 112, Mini) #Show Amount
    PartyGaugeDriverArtFill = EnhanceEff(103, 115, Baby)
    DamageUpEnemyNumber = EnhanceEff(104, 116, Medium)
    ReflectDamageUp = EnhanceEff(105, 117, Large)
    CritDuringChain = EnhanceEff(107, 118, Medium)
    ChainAttackHeal = EnhanceEff(108, 119, Medium)
    DriverReviveChainAttack = EnhanceEff(109, 120)
    PartyGaugeFillEndChain = EnhanceEff(110, 121, Medium) # Show amount
    EtherCannonRange =EnhanceEff(111, 122, Mini)
    WhenDiesHealAllies = EnhanceEff(112, 123, Medium)
    FirstArtDamage = EnhanceEff(114,125, Mega)
    RingABell = EnhanceEff(115, 126, Medium)
    AutoBalancer = EnhanceEff(116, 127)
    EnemyGoldDrop = EnhanceEff(117, 128, Large)
    AllWeaponAttackUp = EnhanceEff(120, 130, Small)
    PreventAffinityLossOnDeath = EnhanceEff(121, 131)
    AffinityUpButtonChallenge = EnhanceEff(122, 132, Medium)
    MissAffinityUp = EnhanceEff(123, 133, Small)
    DamageTakenAffinityUp = EnhanceEff()
    
    
    Baby = [1,5]
    Mini = [1,20]
    Small = [10,50]
    Medium = [20,100]
    Large  = [30,300]
    Mega = [60,600]
    Massive = [300,1500]
    Giga = [1000, 3000]

def StandardEnhanceRun():
    IncreaseEffectCaps(9999)
    if len(EnhanceEffectsList) == 0:
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)
    
    
