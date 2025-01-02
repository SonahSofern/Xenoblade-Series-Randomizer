import JSONParser, Helper, random, IDs


Baby = [1,2,4,5]
Mini = [1,7,14,20]
Small = [10,20,35,50]
Medium = [20,40,70,100]
Large = [30,100,200,300]
Mega = [60,200,400,600]
Massive = [300,600,1000,1500]
Giga = [1000,1700,2500,3000]

Common = 0
Rare = 1
Legendary = 2

def Reverse(listToReverse):
    listCopy = listToReverse
    listCopy.reverse()
    return listCopy


EnhanceEffectsList = []
EnhanceClassList = []
DescriptionList = []
ID = 3896

class Enhancement: # Fix random calls that happen before seeding, make the random calls happen later loop over the created list when randomize is clicked which generates the rarities
    id = 0
    name = ""
    EnhanceEffect = 0
    Param1 =   0
    Param2 =  0
    Caption = 0
    Caption2 = 0
    Rarity = 0
    def __init__(self,Name, Enhancement, Caption = 0,  Param1 = [0,0,0,0], Param2 = [0,0,0,0], Description = None, DescriptionID = 0):
        global ID
        self.Rarity = random.choice([Common, Rare, Legendary])
        self.id = ID
        self.name = Name
        IDs.ValidCustomEnhancements.append(ID)
        def SetParams(ParameterChoices):
            if ParameterChoices == Baby:
                Pstep = 1
            else:
                Pstep = 5
            if len(ParameterChoices) == 1:
                Parameter = ParameterChoices[0]
            else:
                try:
                    if self.Rarity == Common:
                        Parameter = random.randrange(ParameterChoices[0],ParameterChoices[1]+1,Pstep)
                    elif self.Rarity == Rare:
                        Parameter = random.randrange(ParameterChoices[1],ParameterChoices[2]+1,Pstep)
                    elif self.Rarity == Legendary:
                        Parameter = random.randrange(ParameterChoices[2],ParameterChoices[3]+1,Pstep)
                except:
                    Parameter = 0
            return Parameter


        if Description != None:
            DescriptionDict = {   
            "$id": DescriptionID,
            "style": 41,
            "name": Description        
            }
            DescriptionList.append([DescriptionDict])

            
            
        self.Param1 = SetParams(Param1)
        self.Param2 = SetParams(Param2)
        
        EnhanceEffectsDict = {
            "$id": self.id,
            "EnhanceEffect": Enhancement,
            "Param1": self.Param1,
            "Param2": self.Param2,
            "Caption": Caption,
            "Caption2": Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])
        EnhanceClassList.append(self)
        ID += 1
        
def RunCustomEnhancements():
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], [Helper.InclRange(1,1000)], [9999])
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[45], ["Param"], random.randrange(1,51)) # Battle damage up after a certain time uses nonstandard parameter this fixes it
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[181], ["Param"], random.randrange(30,71)) # Healing with low HP
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[90], ["Param"], random.randrange(10,61)) # Healing with low HP
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)
    JSONParser.ExtendJSONFile("common_ms/btl_enhance_cap.json", DescriptionList)

    # names are adjectives
HPBoost =       Enhancement("Hearty",1,1, Small)
StrengthBoost = Enhancement("Strongman", 2,2, Small)
EtherBoost = Enhancement("Ethereal", 3,3, Small)
DexBoost = Enhancement("Dextrous",4,4, Small)
AgiBoost = Enhancement("Agile",5,5, Small)
LuckBoost = Enhancement("Lucky",6,6, Small)
CritBoost = Enhancement("Pinpoint",7,7, Medium)
# PhysDefBoost = Enhancement(8,8, Medium)
# EthDefBoost = Enhancement(9,9, Medium)
# BlockBoost = Enhancement(10,10, Medium)
# FlatHPBoost = Enhancement(11,11, Massive)
# FlatStrengthBoost = Enhancement(12,12, Medium)
# FlatEtherBoost = Enhancement(13,13, Medium)
# FlatDexBoost = Enhancement(14,14, Large)
# FlatAgiBoost = Enhancement(15,15, Small)
# FlatLuckBoost =Enhancement(16,16, Medium)
# FlatCritBoost = Enhancement(17,17, Small)
# FlatDefBoost = Enhancement(18,18, Mini)
# FlatEthDefBoost = Enhancement(19,19,Mini)
# FlatBlockBoost = Enhancement(20,20,Mini)
# TitanDamageUp = Enhancement(21,222,[6], Mega)
# MachineDamageUp = Enhancement(21, 221, [5], Large)
# HumanoidDamageUp = Enhancement(21, 220, [4], Large)
# AquaticDamageUp = Enhancement(21, 219, [3], Mega)
# AerialDamageUp = Enhancement(21, 218, [2], Large)
# InsectDamageUp = Enhancement(21, 217, [1], Large)
# BeastDamageUp = Enhancement(21, 216, [0], Large)
# TitanExecute = Enhancement(22, 229, [6], Baby)
# MachineExecute = Enhancement(22, 228, [5], Baby)
# HumanoidExecute = Enhancement(22, 227, [4], Baby)
# AquaticExecute = Enhancement(22, 226, [3], Baby)
# AerialExecute = Enhancement(22, 225, [2], Baby)
# InsectExecute = Enhancement(22, 224, [1], Baby)
# BeastExecute = Enhancement(22, 223, [0], Baby)
# BladeComboDamUp = Enhancement(23,21, Large)
# FusionComboDamUp = Enhancement(24,22, Large)
# EtherCounter = Enhancement(25,23, Giga)
# PhysCounter = Enhancement(26,24, Giga)
# AutoAttackHeal = Enhancement(27,26, Mini)
# SpecialANDArtHeal = Enhancement(28,27, Baby, Description="Restores [ML:Enhance kind=Param1 ]% HP of damage dealt when\n a Special or Art connects.", DescriptionID=340)
# ArtDamageHeal = Enhancement(28, 28, Small) # This goes on arts only or else it will heal from special and arts
# EnemyKillHeal = Enhancement(29,30, Medium)
# CritHeal = Enhancement(30,31, Small)
# CritDamageUp = Enhancement(31,32, Medium)
# PercentDoubleAuto = Enhancement(32,33, Medium)
# FrontDamageUp = Enhancement(33,34, Large)
# SideDamageUp = Enhancement(34,35, Large)
# BackDamageUp = Enhancement(35,36, Large)
# SurpriseAttackUp = Enhancement(36,37, Giga)
# ToppleDamageUp = Enhancement(37,38, Large)
# LaunchDamageUp = Enhancement(38,39, Large)
# SmashDamageUp = Enhancement(39,40, Mega)
# HigherLVEnemyDamageUp = Enhancement(40,41, Large)
# AllyDownDamageUp = Enhancement(41,42, Mega)
# GuardAnnulAttack = Enhancement(42,43, Medium)
# AnnulReflect = Enhancement(43,44, Medium)
# DamageUpWhenHpDown = Enhancement(44,45, Small, Large)
# BattleDurationDamageUp = Enhancement(45,46, Large) # Uses weird parameter see above
# DamageUpOnEnemyKill = Enhancement(46,47, Medium)
# BreakDurationUp = Enhancement(47,48, Medium)
# ToppleDurationUp = Enhancement(48,49, Medium)
# LaunchDurationUp = Enhancement(49,50, Medium)
# AutoAttackDamageUp = Enhancement(50,51, Mega)
# AggroedEnemyDamageUp = Enhancement(51,52, Large)
# IndoorsDamageUp = Enhancement(52,53, Medium)
# OutdoorsDamageUp = Enhancement(53,54, Small)
# BladeSwitchDamageUp = Enhancement(54,55, Small)
# OppositeGenderBladeDamageUp = Enhancement(55,56, Medium)
# ReduceEnemyToppleResist = Enhancement(56,57, Medium) # [ML:Enhance kind=Param1 ]% put that there to make game show the change?
# ReduceEnemyLaunchResist = Enhancement(57,58, Medium)
# OnBlockNullDamage = Enhancement(59, 59, Small)
# HPLowEvasion = Enhancement(62, 60, Small, Medium)
# EvasionWhileMoving = Enhancement(63, 61, Medium)
# HPLowBlockRate = Enhancement(64, 62, Small, Medium)
# ReduceDamageFromNearbyEnemies = Enhancement(65, 63, Small)
# ReduceDamageOnLowHP = Enhancement(66,64, Small, Small)
# HighHPDamageUp = Enhancement(67,65, Reverse(Medium),Large )
# ReduceSpikeDamage =Enhancement(68,66, Medium)
# BreakResistUp = Enhancement(69, 67, Medium)
# ToppleResistUp = Enhancement(70, 68, Medium)
# LaunchResistUp = Enhancement(71, 69, Medium)
# SmashResistUp = Enhancement(72, 70, Medium)
# BlowdownResistUp = Enhancement(73, 71, Medium)
# KnockbackResistUp = Enhancement(74, 72, Medium)
# DefenseAnnullResistUp = Enhancement(75, 73, Medium)
# AutoAttackAggroDown = Enhancement(77, 75, Large)
# AutoAttackAggroUp = Enhancement(78, 76, Large)
# SpecialAndArtsAggroDown = Enhancement(79, 77, Medium)
# # SpecialAggroDown = EnhanceEff(79, 79, Medium) uses same enchance id so idk how this works
# SpecialAndArtsAggroUp = Enhancement(80, 81, Medium)
# AggroReductionUp = Enhancement(81, 85, Small)
# AggroEverySecond = Enhancement(82, 86, Small) # Get UI to show the increase
# StartBattleAggro = Enhancement(83, 92, Giga)
# RevivalHP = Enhancement(84, 96, Large)
# RevivalHPTeammate = Enhancement(85, 97, Large)
# HealingArtsUp = Enhancement(88, 98, Small)
# IncreaseSelfHeal = Enhancement(89,99, Medium)
# SpecialRechargeCancelling = Enhancement(92, 100, Medium)
# AutoAttackCancelDamageUp = Enhancement(93, 101, Medium)
# Unbeatable = Enhancement(94, 102, Medium)
# NightAccuracy = Enhancement(95, 103, Large)
# DayAccuracy = Enhancement(96, 104, Large)
# ExpEnemiesBoost = Enhancement(97, 105, Medium)
# WPEnemiesBoost = Enhancement(98, 106, Large)
# PartyGaugeExcellentFill = Enhancement(101, 109, Small) # Show amount
# PartyGaugeCritFill = Enhancement(102, 112, Mini) #Show Amount
# PartyGaugeDriverArtFill = Enhancement(103, 115, Baby)
# DamageUpEnemyNumber = Enhancement(104, 116, Medium)
# ReflectDamageUp = Enhancement(105, 117, Large)
# CritDuringChain = Enhancement(107, 118, Medium)
# ChainAttackHeal = Enhancement(108, 119, Medium)
# DriverReviveChainAttack = Enhancement(109, 120)
# PartyGaugeFillEndChain = Enhancement(110, 121, Medium) # Show amount
# EtherCannonRange =Enhancement(111, 122, Mini)
# WhenDiesHealAllies = Enhancement(112, 123, Medium)
# FirstArtDamage = Enhancement(114,125, Mega)
# RingABell = Enhancement(115, 126, Medium)
# AutoBalancer = Enhancement(116, 127)
# EnemyGoldDrop = Enhancement(117, 128, Large)
# AllWeaponAttackUp = Enhancement(120, 130, Small)
# PreventAffinityLossOnDeath = Enhancement(121, 131)
# AffinityUpButtonChallenge = Enhancement(122, 132, Medium)
# MissAffinityUp = Enhancement(123, 133, Small)
# DamageTakenAffinityUp = Enhancement(124,134, Small)
# BladeArtsTriggerUp = Enhancement(125, 135, Large)
# BladeArtDuration = Enhancement(126, 136, Medium)
# AffinityMaxBarrier = Enhancement(127, 137, Small)
# AffinityMaxAttack = Enhancement(128, 138, Medium)
# AffinityMaxEvade = Enhancement(129, 139, Small)
# HunterChem = Enhancement(130, 140, Mega)
# ShoulderToShoulder = Enhancement(131, 141, Mega)
# BladeCooldownReduc = Enhancement(132, 142, Medium)
# PartyHealBladeSwitch = Enhancement(133, 143, Small)
# AffinityRange = Enhancement(134, 144, Mega)
# LV1Damage = Enhancement(135, 145,[1], Large)
# LV2Damage = Enhancement(135, 145,[2], Large)
# LV3Damage = Enhancement(135, 145,[3], Large)
# LV4Damage = Enhancement(135, 145,[4], Large)
# SmallHpPotCreate = Enhancement(136, 146, Small)
# PotionEffectUp = Enhancement(137, 147, Medium)
# PurifyingFlames = Enhancement(138, 148, Small, Mini)
# ForeSight = Enhancement(139, 149, Small)
# DreamOfTheFuture = Enhancement(140, 150)
# ReduceEnemyBladeComboDamage = Enhancement(142, 151, Medium)
# DamagePerEvadeUp = Enhancement(143, 152, Mini)
# ArtsRechargeMaxAffinity = Enhancement(144, 154, Small)
# ReduceAggroFromAttacks = Enhancement(145, 155, Small)
# PhyAndEthDefenseUp = Enhancement(146, 156, Small)
# ChanceToPerfectHitAndEvade = Enhancement(147, 157, Small)
# Reflection = Enhancement(148, 158, Small)
# MaxAffinityEvadeXAttacks = Enhancement(149, 159, Mini)
# ToppleANDLaunchDamageUp = Enhancement(150, 160, Large)
# InstaKill = Enhancement(151,161, Baby)
# PartyDamageReducMAxAffinity = Enhancement(152, 162, Mini)
# KaiserZone = Enhancement(153, 163, Medium)
# TastySnack = Enhancement(154, 164, Medium)
# HealingUpMaxAffinity =  Enhancement(155, 165, Small)
# AggroPerSecondANDAggroUp  = Enhancement(156, 166, Small, Small)
# MoreDamTakeLessAllyLowOrDown = Enhancement(157, 167, Large, Small)
# StopThinking = Enhancement(158, 168, Medium, Baby)
# LowHPSpecialUp = Enhancement(159, 169, Baby) #Uses decimals weird one not sure how it scales
# TranquilGuard = Enhancement(160, 171, Small)
# HPRestoreFusionCombo = Enhancement(161, 172, Baby)
# AttackUpGoldUp = Enhancement(162, 173, Baby, Mega)
# EnemyDropGoldOnHit = Enhancement(163, 174, Medium)
# ReduceEnemyChargeMaxAffinity = Enhancement(164, 175, Small)
# VersusBossUniqueEnemyDamageUp = Enhancement(165, 176, Medium)
# DidIDoThat = Enhancement(166, 177, Mini)
# AnnulEnemyDefAndSPecialDamageUp = Enhancement(167, 178, Small)
# GlassCannon = Enhancement(168, 179, Large, Small)
# AnnulDef = Enhancement(169, 180, Medium)
# Transmigration = Enhancement(170, 181, Medium)
# ElementalWeaknessDamageUP = Enhancement(171, 182, Large) #Show
# GravityPinwheel = Enhancement(172, 183, Small, Baby)
# AutoAttackSpeed= Enhancement(173, 184, Large)
# DoubleHitExtraAutoDamage = Enhancement(174, 185, Large)
# ToppleDamageANDDurationUp = Enhancement(175, 186, Medium, Mini)
# EvadeDrainHp = Enhancement(176, 187, Mini)
# AggroReducOnLandingHit = Enhancement(177, 188, Medium)
# RecoverRechargeCrit = Enhancement(178, 189, Medium)
# SpecialAffinityUp = Enhancement(179,191, Medium)
# BreakResDown = Enhancement(180, 192, Small)
# RepeatSpecialDamage = Enhancement(182, 193, Small)
# Twang = Enhancement(183, 194, Small, Baby)
# MaxAffinityAccuracy = Enhancement(184, 195, Large)
# PotionStayLonger = Enhancement(185, 196, Small)
# FemaleDamageUp = Enhancement(186, 197, Mini)
# DealMoreTakeLessMaxAffinity = Enhancement(187, 198, Mini, Small)
# CritUpChainAttackSelected =Enhancement(188,199,Medium)
# DealDamageWhenSwappedIn = Enhancement(189, 200, Mini)
# CancelWindowUp = Enhancement(191, 201, Medium)
# RestoreHitDamageToParty = Enhancement(192, 202, Baby)
# AddBufferTimeSwitchingToComboBlade = Enhancement(193, 203, Medium)
# PartyDamageMaxAffinity = Enhancement(194, 204, Mini)
# AegisDriver = Enhancement(195, 205, Medium, Small)
# AegisParty = Enhancement(196, 206)
# ReduceFireDamage = Enhancement(58, 207, [1], Medium)
# ReduceWaterDamage = Enhancement(58, 208, [2], Medium)
# ReduceWindDamage = Enhancement(58, 209, [3], Medium)
# ReduceEarthDamage = Enhancement(58, 210, [4], Medium)
# ReduceElectricDamage = Enhancement(58, 211, [5], Medium)
# ReduceIceDamage = Enhancement(58, 212, [6], Medium)
# ReduceLightDamage = Enhancement(58, 213, [7], Medium)
# ReduceDarkDamage = Enhancement(58, 214, [8], Medium)
# ChainAttackPower = Enhancement(106, 215, Baby) # Show
# LowHPHeal = Enhancement(181, 230, Baby)
# ArtUseHeal = Enhancement(86, 231, Baby)
# AutoDriverArtCancelHeal = Enhancement(91, 233, Baby)
# TakeDamageHeal = Enhancement(90, 235, Mini)
# HealMoving = Enhancement(87, 236, Mini)
# MaxAffinityHeal = Enhancement(141,237,Mini)
# AbsorbFireBlock = Enhancement(60, 238, [1])
# AbsorbWaterBlock = Enhancement(60, 239, [2])
# AbsorbWindBlock = Enhancement(60, 240, [3])
# AbsorbEarthBlock = Enhancement(60, 241, [4])
# AbsorbElectricBlock = Enhancement(60, 242, [5])
# AbsorbIceBlock = Enhancement(60, 243, [6])
# AbsorbLightBlock = Enhancement(60, 244, [7])
# AbsorbDarkBlock = Enhancement(60, 245, [8])
# ReflectFireBlock = Enhancement(61, 246, [1])
# ReflectWaterBlock = Enhancement(61, 247, [2])
# ReflectWindBlock = Enhancement(61, 248, [3])
# ReflectEarthBlock = Enhancement(61, 249, [4])
# ReflectElectricBlock = Enhancement(61, 250, [5])
# ReflectIceBlock = Enhancement(61, 251, [6])
# ReflectLightBlock = Enhancement(61, 252, [7])
# ReflectDarkBlock = Enhancement(61, 253, [8])
# AegisPowerUp = Enhancement(119, 254, [1], Small)
# CatScimPowerUp = Enhancement(119, 255, [2], Small)
# TwinRingPowerUp = Enhancement(119, 256, [3], Small)
# DrillShieldPowerUp = Enhancement(119, 257, [4], Small)
# MechArmsPowerUp = Enhancement(119, 258, [5], Small)
# VarSaberPowerUp = Enhancement(119, 259, [6], Small)
# WhipswordPowerUp = Enhancement(119, 260, [7], Small)
# BigBangPowerUp = Enhancement(119, 261, [8], Small)
# DualScythesPowerUp = Enhancement(119, 262, [9], Small)
# GreataxePowerUp = Enhancement(119, 263, [10], Small)
# MegalancePowerUp = Enhancement(119, 264, [11], Small)
# EtherCannonPowerUp = Enhancement(119, 265, [12], Small)
# ShieldHammerPowerUp = Enhancement(119, 266, [13], Small)
# ChromaKatanaPowerUp = Enhancement(119, 267, [14], Small)
# BitballPowerUp = Enhancement(119, 268, [15], Small)
# KnuckleClawsPowerUp = Enhancement(119, 269, [16], Small)
# HPGuardArtRechargeAttacked = Enhancement(197,270, Mini)
# Jamming = Enhancement(198, 271, Medium)
XStartBattle = Enhancement("X Start",113, 272, [0])
YStartBattle = Enhancement("Y Start",113, 274, [1])
BStartBattle = Enhancement("B Start",113, 276, [2])
ArtCancel = Enhancement("Arts Cancel",190, 278)
# BladeSwitchCooldownWithArts = Enhancement(200, 279, Small)
# TauntRes = Enhancement(217, 280, Medium)
# DriverShackRes = Enhancement(218, 281, Medium)
# BladeShackRes = Enhancement(219, 282, Medium)
# BurstDestroyAnotherOrb = Enhancement(226, 283)
# HpPotChanceFor2 = Enhancement(227, 284, Medium)
# DestroyOrbOpposingElement = Enhancement(228, 285)
# TargetNearbyOrbsChainAttack = Enhancement(229, 286, Medium)
# TargetDamagedNonOpposingElement = Enhancement(230, 287)
# StenchRes = Enhancement(231, 288, Medium)
# HPPotOnHitAgain = Enhancement(227, 289)
# BladeComboOrbAdder = Enhancement(234,290, Medium)
# EvadeDriverArt = Enhancement(32, 292)
# RetainAggro = Enhancement(235, 293, Medium)
# DamageUpOnDeath = Enhancement(238, 295, Large)
# AutoSpeedArtsSpeed= Enhancement(240, 296, Small, Small)
# LV4EachUseDmageUp = Enhancement(241, 297, Large)
# Vision = Enhancement(242, 298, Reverse(Medium))
# AwakenPurge = Enhancement(243, 299, Medium)
# PartyCritMaxAffinity = Enhancement(244, 300, Small)
# DamageUpPerCrit = Enhancement(245, 301, Mini)
# RechargeOnEvade = Enhancement(248, 304, Baby)
# DamageAndEvadeAffinityMax = Enhancement(269, 305, Medium, Mini)
# PartyLaunchDamageUp = Enhancement(249, 306, Mega)
# PotionPickupDamageUp = Enhancement(250, 307, Small)
# ItemCollectionRange = Enhancement(251, 308, Mega)
# CombatSpeed = Enhancement(211, 309, Mega)
# NullHealRes = Enhancement(252, 310, Medium)
# DoomRes = Enhancement(253, 311, Medium)
# PartyDrainRes = Enhancement(254, 312, Medium)
# DealTakeMore = Enhancement(255, 313, Medium, Medium)
# AllDebuffRes = Enhancement(258, 316, Small)
# DamageUpOnCancel = Enhancement(259, 317, Mini)
# PurgeRage = Enhancement(261, 318, Medium)
# DamageAndCritUpMaxAffinity = Enhancement(263, 320, Medium, Medium)
# ReducesTerrainDamage = Enhancement(264, 334, Medium)
# SpecialRecievesAfterImage = Enhancement(213, 335, Baby)
EyeOfJustice = Enhancement("Eye of Shining Justice",236,294)
#There are some torna effects not including them recoverable hp.
