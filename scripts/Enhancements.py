import JSONParser, Helper, random, IDs

Baby = [1,5]
Mini = [1,20]
Small = [10,50]
Medium = [20,100]
Large  = [30,300]
Mega = [60,600]
Massive = [300,1500]
Giga = [1000, 3000]
EnhanceEffectsList = []
ID = 4000
class EnhanceEff:
    
    def __init__(self, Enhancement, Caption = 0,  Param1 = [], Param2 = []):
        global ID
        if Param1 == []:
            Param1Val = 0
        elif len(Param1) == 1:
            Param1Val = Param1[0]
        elif Param1 == Baby:
            Param1Val = random.randrange(Param1[0],Param1[1])
        else:
            Param1Val = random.randrange(Param1[0],Param1[1],5)
            
        if Param2 == []:
            Param2Val = 0   
        elif len(Param2) == 1:
            Param2Val = Param2[0]
        elif Param2 == Baby:
            Param2Val = random.randrange(Param2[0],Param2[1])
        else:
            Param2Val = random.randrange(Param2[0], Param2[1],5)    
        
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
    DamageTakenAffinityUp = EnhanceEff(124,134, Small)
    BladeArtsTriggerUp = EnhanceEff(125, 135, Large)
    BladeArtDuration = EnhanceEff(126, 136, Medium)
    AffinityMaxBarrier = EnhanceEff(127, 137, Small)
    AffinityMaxAttack = EnhanceEff(128, 138, Medium)
    AffinityMaxEvade = EnhanceEff(129, 139, Small)
    HunterChem = EnhanceEff(130, 140, Mega)
    ShoulderToShoulder = EnhanceEff(131, 141, Mega)
    BladeCooldownReduc = EnhanceEff(132, 142, Medium)
    PartyHealBladeSwitch = EnhanceEff(133, 143, Small)
    AffinityRange = EnhanceEff(134, 144, Mega)
    LV1Damage = EnhanceEff(135, 145,1, Large)
    LV2Damage = EnhanceEff(135, 145,2, Large)
    LV3Damage = EnhanceEff(135, 145,3, Large)
    LV4Damage = EnhanceEff(135, 145,4, Large)
    SmallHpPotCreate = EnhanceEff(136, 146, Small)
    PotionEffectUp = EnhanceEff(137, 147, Medium)
    PurifyingFlames = EnhanceEff(138, 148, Small, Mini)
    ForeSight = EnhanceEff(139, 149, Small)
    DreamOfTheFuture = EnhanceEff(140, 150)
    ReduceEnemyBladeComboDamage = EnhanceEff(142, 151, Medium)
    DamagePerEvadeUp = EnhanceEff(143, 152, Mini)
    ArtsRechargeMaxAffinity = EnhanceEff(144, 154, Small)
    ReduceAggroFromAttacks = EnhanceEff(145, 155, Small)
    PhyAndEthDefenseUp = EnhanceEff(146, 156, Small)
    ChanceToPerfectHitAndEvade = EnhanceEff(147, 157, Small)
    Reflection = EnhanceEff(148, 158, Small)
    MaxAffinityEvadeXAttacks = EnhanceEff(149, 159, Mini)
    ToppleANDLaunchDamageUp = EnhanceEff(150, 160, Large)
    InstaKill = EnhanceEff(151,161, Baby)
    PartyDamageReducMAxAffinity = EnhanceEff(152, 162, Mini)
    KaiserZone = EnhanceEff(153, 163, Medium)
    TastySnack = EnhanceEff(154, 164, Medium)
    HealingUpMaxAffinity =  EnhanceEff(155, 165, Small)
    AggroPerSecondANDAggroUp  = EnhanceEff(156, 166, Small, Small)
    MoreDamTakeLessAllyLowOrDown = EnhanceEff(157, 167, Large, Small)
    StopThinking = EnhanceEff(158, 168, Medium, Baby)
    LowHPSpecialUp = EnhanceEff(159, 169, [1.5]) #Uses decimals weird one not sure how it scales
    TranquilGuard = EnhanceEff(160, 171, Small)
    HPRestoreFusionCombo = EnhanceEff(161, 172, Baby)
    AttackUpGoldUp = EnhanceEff(162, 173, Baby, Mega)
    EnemyDropGoldOnHit = EnhanceEff(163, 174, Medium)
    ReduceEnemyChargeMaxAffinity = EnhanceEff(164, 175, Small)
    VersusBossUniqueEnemyDamageUp = EnhanceEff(165, 176, Medium)
    DidIDoThat = EnhanceEff(166, 177, Mini)
    AnnulEnemyDefAndSPecialDamageUp = EnhanceEff(167, 178, Small)
    GlassCannon = EnhanceEff(168, 179, Large, Small)
    AnnulDef = EnhanceEff(169, 180, Medium)
    Transmigration = EnhanceEff(170, 181, Medium)
    ElementalWeaknessDamageUP = EnhanceEff(171, 182, Large) #Show
    GravityPinwheel = EnhanceEff(172, 183, Small, Baby)
    AutoAttackSpeed= EnhanceEff(173, 184, Large)
    DoubleHitExtraAutoDamage = EnhanceEff(174, 185, Large)
    ToppleDamageANDDurationUp = EnhanceEff(175, 186, Medium, Mini)
    EvadeDrainHp = EnhanceEff(176, 187, Mini)
    AggroReducOnLandingHit = EnhanceEff(177, 188, Medium)
    RecoverRechargeCrit = EnhanceEff(178, 189, Medium)
    SpecialAffinityUp = EnhanceEff(179,191, Medium)
    BreakResDown = EnhanceEff(180, 192, Small)
    RepeatSpecialDamage = EnhanceEff(182, 193, Small)
    Twang = EnhanceEff(183, 194, Small, Baby)
    MaxAffinityAccuracy = EnhanceEff(184, 195, Large)
    PotionStayLonger = EnhanceEff(185, 196, Small)
    FemaleDamageUp = EnhanceEff(186, 197, Mini)
    DealMoreTakeLessMaxAffinity = EnhanceEff(187, 198, Mini, Small)
    CritUpChainAttackSelected =EnhanceEff(188,199,Medium)
    DealDamageWhenSwappedIn = EnhanceEff(189, 200, Mini)
    CancelWindowUp = EnhanceEff(191, 201, Medium)
    RestoreHitDamageToParty = EnhanceEff(192, 202, Baby)
    AddBufferTimeSwitchingToComboBlade = EnhanceEff(193, 203, Medium)
    PartyDamageMaxAffinity = EnhanceEff(194, 204, Mini)
    AegisDriver = EnhanceEff(195, 205, Medium, Small)
    AegisParty = EnhanceEff(196, 206)
    ReduceFireDamage = EnhanceEff(58, 207, [1], Medium)
    ReduceWaterDamage = EnhanceEff(58, 208, [2], Medium)
    ReduceWindDamage = EnhanceEff(58, 209, [3], Medium)
    ReduceEarthDamage = EnhanceEff(58, 210, [4], Medium)
    ReduceElectricDamage = EnhanceEff(58, 211, [5], Medium)
    ReduceIceDamage = EnhanceEff(58, 212, [6], Medium)
    ReduceLightDamage = EnhanceEff(58, 213, [7], Medium)
    ReduceDarkDamage = EnhanceEff(58, 214, [8], Medium)
  
    
    
    
    
    
    
    
    
        
    
    
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
    IDs.CustomEnhancements = Helper.InclRange(4000, ID)
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)
    
    
