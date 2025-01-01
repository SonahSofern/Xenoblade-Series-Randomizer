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
ID = 10000
class Enhance:
    id = ID
    EnhanceEffect =0
    Param1 =   0
    Param2 =  0
    Caption = 0
    Caption2 = 0
    Rarity = ""
    def __init__(self, Enhancement, Caption = 0,  Param1 = [0,0,0,0], Param2 = [0,0,0,0]):
        global ID
        self.Rarity = random.choice([Common, Rare, Legendary])
        
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

        self.Param1 = SetParams(Param1)
        self.Param2 = SetParams(Param2)
        
        EnhanceEffectsDict = {
            "$id": ID,
            "EnhanceEffect": Enhancement,
            "Param1": self.Param1,
            "Param2": self.Param2,
            "Caption": Caption,
            "Caption2": Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])
        IDs.ValidCustomEnhancements.append(ID)
        ID += 1

def RunCustomEnhancements(NewCap):
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], [Helper.InclRange(1,1000)], [NewCap])
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[45], ["Param"], random.randrange(1,51)) # Battle damage up after a certain time uses nonstandard parameter this fixes it
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[181], ["Param"], random.randrange(30,71)) # Healing with low HP
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[90], ["Param"], random.randrange(10,61)) # Healing with low HP
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)

    
HPBoost =       Enhance(1,1, Small)
StrengthBoost = Enhance(2,2, Small)
EtherBoost = Enhance(3,3, Small)
DexBoost = Enhance(4,4, Small)
AgiBoost = Enhance(5,5, Small)
LuckBoost = Enhance(6,6, Small)
CritBoost = Enhance(7,7, Medium)
PhysDefBoost = Enhance(8,8, Medium)
EthDefBoost = Enhance(9,9, Medium)
BlockBoost = Enhance(10,10, Medium)
FlatHPBoost = Enhance(11,11, Massive)
FlatStrengthBoost = Enhance(12,12, Medium)
FlatEtherBoost = Enhance(13,13, Medium)
FlatDexBoost = Enhance(14,14, Large)
FlatAgiBoost = Enhance(15,15, Small)
FlatLuckBoost =Enhance(16,16, Medium)
FlatCritBoost = Enhance(17,17, Small)
FlatDefBoost = Enhance(18,18, Mini)
FlatEthDefBoost = Enhance(19,19,Mini)
FlatBlockBoost = Enhance(20,20,Mini)
TitanDamageUp = Enhance(21,222,[6], Mega)
MachineDamageUp = Enhance(21, 221, [5], Large)
HumanoidDamageUp = Enhance(21, 220, [4], Large)
AquaticDamageUp = Enhance(21, 219, [3], Mega)
AerialDamageUp = Enhance(21, 218, [2], Large)
InsectDamageUp = Enhance(21, 217, [1], Large)
BeastDamageUp = Enhance(21, 216, [0], Large)
TitanExecute = Enhance(22, 229, [6], Baby)
MachineExecute = Enhance(22, 228, [5], Baby)
HumanoidExecute = Enhance(22, 227, [4], Baby)
AquaticExecute = Enhance(22, 226, [3], Baby)
AerialExecute = Enhance(22, 225, [2], Baby)
InsectExecute = Enhance(22, 224, [1], Baby)
BeastExecute = Enhance(22, 223, [0], Baby)
BladeComboDamUp = Enhance(23,21, Large)
FusionComboDamUp = Enhance(24,22, Large)
EtherCounter = Enhance(25,23, Massive)
PhysCounter = Enhance(26,24, Massive) # This is interesting because jins stuned swallow uses this and inflicts blowdown from this effect want to figure out how
AutoAttackHeal = Enhance(27,26, Mini)
SpecialHeal = Enhance(28,27, Baby) # This also is used for driver art healing (according to the caption which might be wrong) want to figure this out too
EnemyKillHeal = Enhance(29,30, Medium)
CritHeal = Enhance(30,31, Small)
CritDamageUp = Enhance(31,32, Medium)
PercentDoubleAuto = Enhance(32,33, Medium)
FrontDamageUp = Enhance(33,34, Large)
SideDamageUp = Enhance(34,35, Large)
BackDamageUp = Enhance(35,36, Large)
SurpriseAttackUp = Enhance(36,37, Giga)
ToppleDamageUp = Enhance(37,38, Large)
LaunchDamageUp = Enhance(38,39, Large)
SmashDamageUp = Enhance(39,40, Large)
HigherLVEnemyDamageUp = Enhance(40,41, Large)
AllyDownDamageUp = Enhance(41,42, Mega)
GuardAnnulAttack = Enhance(42,43, Medium)
AnnulReflect = Enhance(43,44, Medium)
DamageUpWhenHpDown = Enhance(44,45, Small, Large)
BattleDurationDamageUp = Enhance(45,46, Large) # Uses weird parameter see above
DamageUpOnEnemyKill = Enhance(46,47, Medium)
BreakDurationUp = Enhance(47,48, Medium)
ToppleDurationUp = Enhance(48,49, Medium)
LaunchDurationUp = Enhance(49,50, Medium)
AutoAttackDamageUp = Enhance(50,51, Mega)
AggroedEnemyDamageUp = Enhance(51,52, Large)
IndoorsDamageUp = Enhance(52,53, Medium)
OutdoorsDamageUp = Enhance(53,54, Small)
BladeSwitchDamageUp = Enhance(54,55, Small)
OppositeGenderBladeDamageUp = Enhance(55,56, Medium)
ReduceEnemyToppleResist = Enhance(56,57, Medium) # [ML:Enhance kind=Param1 ]% put that there to make game show the change?
ReduceEnemyLaunchResist = Enhance(57,58, Medium)
OnBlockNullDamage = Enhance(59, 59, Small)
HPLowEvasion = Enhance(62, 60, Small, Medium)
EvasionWhileMoving = Enhance(63, 61, Medium)
HPLowBlockRate = Enhance(64, 62, Small, Medium)
ReduceDamageFromNearbyEnemies = Enhance(65, 63, Small)
ReduceDamageOnLowHP = Enhance(66,64, Small, Small)
HighHPDamageUp = Enhance(67,65, Reverse(Medium),Large )
ReduceSpikeDamage =Enhance(68,66, Medium)
BreakResistUp = Enhance(69, 67, Medium)
ToppleResistUp = Enhance(70, 68, Medium)
LaunchResistUp = Enhance(71, 69, Medium)
SmashResistUp = Enhance(72, 70, Medium)
BlowdownResistUp = Enhance(73, 71, Medium)
KnockbackResistUp = Enhance(74, 72, Medium)
DefenseAnnullResistUp = Enhance(75, 73, Medium)
AutoAttackAggroDown = Enhance(77, 75, Large)
AutoAttackAggroUp = Enhance(78, 76, Large)
SpecialAndArtsAggroDown = Enhance(79, 77, Medium)
# SpecialAggroDown = EnhanceEff(79, 79, Medium) uses same enchance id so idk how this works
SpecialAndArtsAggroUp = Enhance(80, 81, Medium)
AggroReductionUp = Enhance(81, 85, Small)
AggroEverySecond = Enhance(82, 86, Small) # Get UI to show the increase
StartBattleAggro = Enhance(83, 92, Giga)
RevivalHP = Enhance(84, 96, Large)
RevivalHPTeammate = Enhance(85, 97, Large)
HealingArtsUp = Enhance(88, 98, Small)
IncreaseSelfHeal = Enhance(89,99, Medium)
SpecialRechargeCancelling = Enhance(92, 100, Medium)
AutoAttackCancelDamageUp = Enhance(93, 101, Medium)
Unbeatable = Enhance(94, 102, Medium)
NightAccuracy = Enhance(95, 103, Large)
DayAccuracy = Enhance(96, 104, Large)
ExpEnemiesBoost = Enhance(97, 105, Medium)
WPEnemiesBoost = Enhance(98, 106, Large)
PartyGaugeExcellentFill = Enhance(101, 109, Small) # Show amount
PartyGaugeCritFill = Enhance(102, 112, Mini) #Show Amount
PartyGaugeDriverArtFill = Enhance(103, 115, Baby)
DamageUpEnemyNumber = Enhance(104, 116, Medium)
ReflectDamageUp = Enhance(105, 117, Large)
CritDuringChain = Enhance(107, 118, Medium)
ChainAttackHeal = Enhance(108, 119, Medium)
DriverReviveChainAttack = Enhance(109, 120)
PartyGaugeFillEndChain = Enhance(110, 121, Medium) # Show amount
EtherCannonRange =Enhance(111, 122, Mini)
WhenDiesHealAllies = Enhance(112, 123, Medium)
FirstArtDamage = Enhance(114,125, Mega)
RingABell = Enhance(115, 126, Medium)
AutoBalancer = Enhance(116, 127)
EnemyGoldDrop = Enhance(117, 128, Large)
AllWeaponAttackUp = Enhance(120, 130, Small)
PreventAffinityLossOnDeath = Enhance(121, 131)
AffinityUpButtonChallenge = Enhance(122, 132, Medium)
MissAffinityUp = Enhance(123, 133, Small)
DamageTakenAffinityUp = Enhance(124,134, Small)
BladeArtsTriggerUp = Enhance(125, 135, Large)
BladeArtDuration = Enhance(126, 136, Medium)
AffinityMaxBarrier = Enhance(127, 137, Small)
AffinityMaxAttack = Enhance(128, 138, Medium)
AffinityMaxEvade = Enhance(129, 139, Small)
HunterChem = Enhance(130, 140, Mega)
ShoulderToShoulder = Enhance(131, 141, Mega)
BladeCooldownReduc = Enhance(132, 142, Medium)
PartyHealBladeSwitch = Enhance(133, 143, Small)
AffinityRange = Enhance(134, 144, Mega)
LV1Damage = Enhance(135, 145,[1], Large)
LV2Damage = Enhance(135, 145,[2], Large)
LV3Damage = Enhance(135, 145,[3], Large)
LV4Damage = Enhance(135, 145,[4], Large)
SmallHpPotCreate = Enhance(136, 146, Small)
PotionEffectUp = Enhance(137, 147, Medium)
PurifyingFlames = Enhance(138, 148, Small, Mini)
ForeSight = Enhance(139, 149, Small)
DreamOfTheFuture = Enhance(140, 150)
ReduceEnemyBladeComboDamage = Enhance(142, 151, Medium)
DamagePerEvadeUp = Enhance(143, 152, Mini)
ArtsRechargeMaxAffinity = Enhance(144, 154, Small)
ReduceAggroFromAttacks = Enhance(145, 155, Small)
PhyAndEthDefenseUp = Enhance(146, 156, Small)
ChanceToPerfectHitAndEvade = Enhance(147, 157, Small)
Reflection = Enhance(148, 158, Small)
MaxAffinityEvadeXAttacks = Enhance(149, 159, Mini)
ToppleANDLaunchDamageUp = Enhance(150, 160, Large)
InstaKill = Enhance(151,161, Baby)
PartyDamageReducMAxAffinity = Enhance(152, 162, Mini)
KaiserZone = Enhance(153, 163, Medium)
TastySnack = Enhance(154, 164, Medium)
HealingUpMaxAffinity =  Enhance(155, 165, Small)
AggroPerSecondANDAggroUp  = Enhance(156, 166, Small, Small)
MoreDamTakeLessAllyLowOrDown = Enhance(157, 167, Large, Small)
StopThinking = Enhance(158, 168, Medium, Baby)
LowHPSpecialUp = Enhance(159, 169, Baby) #Uses decimals weird one not sure how it scales
TranquilGuard = Enhance(160, 171, Small)
HPRestoreFusionCombo = Enhance(161, 172, Baby)
AttackUpGoldUp = Enhance(162, 173, Baby, Mega)
EnemyDropGoldOnHit = Enhance(163, 174, Medium)
ReduceEnemyChargeMaxAffinity = Enhance(164, 175, Small)
VersusBossUniqueEnemyDamageUp = Enhance(165, 176, Medium)
DidIDoThat = Enhance(166, 177, Mini)
AnnulEnemyDefAndSPecialDamageUp = Enhance(167, 178, Small)
GlassCannon = Enhance(168, 179, Large, Small)
AnnulDef = Enhance(169, 180, Medium)
Transmigration = Enhance(170, 181, Medium)
ElementalWeaknessDamageUP = Enhance(171, 182, Large) #Show
GravityPinwheel = Enhance(172, 183, Small, Baby)
AutoAttackSpeed= Enhance(173, 184, Large)
DoubleHitExtraAutoDamage = Enhance(174, 185, Large)
ToppleDamageANDDurationUp = Enhance(175, 186, Medium, Mini)
EvadeDrainHp = Enhance(176, 187, Mini)
AggroReducOnLandingHit = Enhance(177, 188, Medium)
RecoverRechargeCrit = Enhance(178, 189, Medium)
SpecialAffinityUp = Enhance(179,191, Medium)
BreakResDown = Enhance(180, 192, Small)
RepeatSpecialDamage = Enhance(182, 193, Small)
Twang = Enhance(183, 194, Small, Baby)
MaxAffinityAccuracy = Enhance(184, 195, Large)
PotionStayLonger = Enhance(185, 196, Small)
FemaleDamageUp = Enhance(186, 197, Mini)
DealMoreTakeLessMaxAffinity = Enhance(187, 198, Mini, Small)
CritUpChainAttackSelected =Enhance(188,199,Medium)
DealDamageWhenSwappedIn = Enhance(189, 200, Mini)
CancelWindowUp = Enhance(191, 201, Medium)
RestoreHitDamageToParty = Enhance(192, 202, Baby)
AddBufferTimeSwitchingToComboBlade = Enhance(193, 203, Medium)
PartyDamageMaxAffinity = Enhance(194, 204, Mini)
AegisDriver = Enhance(195, 205, Medium, Small)
AegisParty = Enhance(196, 206)
ReduceFireDamage = Enhance(58, 207, [1], Medium)
ReduceWaterDamage = Enhance(58, 208, [2], Medium)
ReduceWindDamage = Enhance(58, 209, [3], Medium)
ReduceEarthDamage = Enhance(58, 210, [4], Medium)
ReduceElectricDamage = Enhance(58, 211, [5], Medium)
ReduceIceDamage = Enhance(58, 212, [6], Medium)
ReduceLightDamage = Enhance(58, 213, [7], Medium)
ReduceDarkDamage = Enhance(58, 214, [8], Medium)
ChainAttackPower = Enhance(106, 215, Baby) # Show
LowHPHeal = Enhance(181, 230, Baby)
ArtUseHeal = Enhance(86, 231, Baby)
AutoDriverArtCancelHeal = Enhance(91, 233, Baby)
TakeDamageHeal = Enhance(90, 235, Mini)
HealMoving = Enhance(87, 236, Mini)
MaxAffinityHeal = Enhance(141,237,Mini)
AbsorbFireBlock = Enhance(60, 238, [1])
AbsorbWaterBlock = Enhance(60, 239, [2])
AbsorbWindBlock = Enhance(60, 240, [3])
AbsorbEarthBlock = Enhance(60, 241, [4])
AbsorbElectricBlock = Enhance(60, 242, [5])
AbsorbIceBlock = Enhance(60, 243, [6])
AbsorbLightBlock = Enhance(60, 244, [7])
AbsorbDarkBlock = Enhance(60, 245, [8])
ReflectFireBlock = Enhance(61, 246, [1])
ReflectWaterBlock = Enhance(61, 247, [2])
ReflectWindBlock = Enhance(61, 248, [3])
ReflectEarthBlock = Enhance(61, 249, [4])
ReflectElectricBlock = Enhance(61, 250, [5])
ReflectIceBlock = Enhance(61, 251, [6])
ReflectLightBlock = Enhance(61, 252, [7])
ReflectDarkBlock = Enhance(61, 253, [8])
AegisPowerUp = Enhance(119, 254, [1], Small)
CatScimPowerUp = Enhance(119, 255, [2], Small)
TwinRingPowerUp = Enhance(119, 256, [3], Small)
DrillShieldPowerUp = Enhance(119, 257, [4], Small)
MechArmsPowerUp = Enhance(119, 258, [5], Small)
VarSaberPowerUp = Enhance(119, 259, [6], Small)
WhipswordPowerUp = Enhance(119, 260, [7], Small)
BigBangPowerUp = Enhance(119, 261, [8], Small)
DualScythesPowerUp = Enhance(119, 262, [9], Small)
GreataxePowerUp = Enhance(119, 263, [10], Small)
MegalancePowerUp = Enhance(119, 264, [11], Small)
EtherCannonPowerUp = Enhance(119, 265, [12], Small)
ShieldHammerPowerUp = Enhance(119, 266, [13], Small)
ChromaKatanaPowerUp = Enhance(119, 267, [14], Small)
BitballPowerUp = Enhance(119, 268, [15], Small)
KnuckleClawsPowerUp = Enhance(119, 269, [16], Small)
HPGuardArtRechargeAttacked = Enhance(197,270, Mini)
Jamming = Enhance(198, 271, Medium)
XStartBattle = Enhance(113, 272, [0])
YStartBattle = Enhance(113, 274, [1])
BStartBattle = Enhance(113, 276, [2])
ArtCancel = Enhance(190, 278)
BladeSwitchCooldownWithArts = Enhance(200, 279, Small)
TauntRes = Enhance(217, 280, Medium)
DriverShackRes = Enhance(218, 281, Medium)
BladeShackRes = Enhance(219, 282, Medium)
BurstDestroyAnotherOrb = Enhance(226, 283)
HpPotChanceFor2 = Enhance(227, 284, Medium)
DestroyOrbOpposingElement = Enhance(228, 285)
TargetNearbyOrbsChainAttack = Enhance(229, 286, Medium)
TargetDamagedNonOpposingElement = Enhance(230, 287)
StenchRes = Enhance(231, 288, Medium)
HPPotOnHitAgain = Enhance(227, 289)
BladeComboOrbAdder = Enhance(234,290, Medium)
EvadeDriverArt = Enhance(32, 292)
RetainAggro = Enhance(235, 293, Medium)
DamageUpOnDeath = Enhance(238, 295, Large)
AutoSpeedArtsSpeed= Enhance(240, 296, Small, Small)
LV4EachUseDmageUp = Enhance(241, 297, Large)
Vision = Enhance(242, 298, Reverse(Medium))
AwakenPurge = Enhance(243, 299, Medium)
PartyCritMaxAffinity = Enhance(244, 300, Small)
DamageUpPerCrit = Enhance(245, 301, Mini)
RechargeOnEvade = Enhance(248, 304, Baby)
DamageAndEvadeAffinityMax = Enhance(269, 305, Medium, Mini)
PartyLaunchDamageUp = Enhance(249, 306, Mega)
PotionPickupDamageUp = Enhance(250, 307, Small)
ItemCollectionRange = Enhance(251, 308, Mega)
CombatSpeed = Enhance(211, 309, Mega)
NullHealRes = Enhance(252, 310, Medium)
DoomRes = Enhance(253, 311, Medium)
PartyDrainRes = Enhance(254, 312, Medium)
DealTakeMore = Enhance(255, 313, Medium, Medium)
AllDebuffRes = Enhance(258, 316, Small)
DamageUpOnCancel = Enhance(259, 317, Mini)
PurgeRage = Enhance(261, 318, Medium)
DamageAndCritUpMaxAffinity = Enhance(263, 320, Medium, Medium)
ReducesTerrainDamage = Enhance(264, 334, Medium)
SpecialRecievesAfterImage = Enhance(213, 335, Baby)
#There are some torna effects not including them recoverable hp.


