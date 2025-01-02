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
HPBoost =       Enhancement("Health",1,1, Small)
StrengthBoost = Enhancement("Strength", 2,2, Small)
EtherBoost = Enhancement("Ether", 3,3, Small)
DexBoost = Enhancement("Dexterity",4,4, Small)
AgiBoost = Enhancement("Agility",5,5, Small)
LuckBoost = Enhancement("Lucky",6,6, Small)
CritBoost = Enhancement("Critical",7,7, Medium)
PhysDefBoost = Enhancement("Phys Def",8,8, Medium)
EthDefBoost = Enhancement("Ether Def",9,9, Medium)
BlockBoost = Enhancement("Block",10,10, Medium)
FlatHPBoost = Enhancement("Health",11,11, Massive)
FlatStrengthBoost = Enhancement("Strength",12,12, Medium)
FlatEtherBoost = Enhancement("Ether",13,13, Medium)
FlatDexBoost = Enhancement("Dexterity",14,14, Large)
FlatAgiBoost = Enhancement("Agility",15,15, Small)
FlatLuckBoost =Enhancement("Luck",16,16, Medium)
FlatCritBoost = Enhancement("Critical",17,17, Small)
FlatDefBoost = Enhancement("Phys Def",18,18, Mini)
FlatEthDefBoost = Enhancement("Eth Def",19,19,Mini)
FlatBlockBoost = Enhancement("Block",20,20,Mini)
TitanDamageUp = Enhancement("Titan",21,222,[6], Mega)
MachineDamageUp = Enhancement("Machine",21, 221, [5], Large)
HumanoidDamageUp = Enhancement("Humanoid",21, 220, [4], Large)
AquaticDamageUp = Enhancement("Aquatic",21, 219, [3], Mega)
AerialDamageUp = Enhancement("Aerial",21, 218, [2], Large)
InsectDamageUp = Enhancement("Insect",21, 217, [1], Large)
BeastDamageUp = Enhancement("Beast",21, 216, [0], Large)
TitanExecute = Enhancement("Titan",22, 229, [6], Baby)
MachineExecute = Enhancement("Machine",22, 228, [5], Baby)
HumanoidExecute = Enhancement("Humanoid",22, 227, [4], Baby)
AquaticExecute = Enhancement("Aquatic",22, 226, [3], Baby)
AerialExecute = Enhancement("Aerial",22, 225, [2], Baby)
InsectExecute = Enhancement("Insect",22, 224, [1], Baby)
BeastExecute = Enhancement("Beast",22, 223, [0], Baby)
BladeComboDamUp = Enhancement("Bl Combo",23,21, Large)
FusionComboDamUp = Enhancement("Fus Combo",24,22, Large)
EtherCounter = Enhancement("Eth Counter",25,23, Giga)
PhysCounter = Enhancement("Phys Counter",26,24, Giga)
AutoAttackHeal = Enhancement("Auto Vamp",27,26, Mini)
SpecialANDArtHeal = Enhancement("Omnivamp",28,27, Baby, Description="Restores [ML:Enhance kind=Param1 ]% HP of damage dealt when\n a Special or Art connects.", DescriptionID=340)
ArtDamageHeal = Enhancement("Omnivamp",28, 28, Small) # This goes on arts only or else it will heal from special and arts
EnemyKillHeal = Enhancement("Scavenger",29,30, Medium)
CritHeal = Enhancement("Crit Vamp",30,31, Small)
CritDamageUp = Enhancement("Crit Damage",31,32, Medium)
PercentDoubleAuto = Enhancement("Doublestrike",32,33, Medium)
FrontDamageUp = Enhancement("Front",33,34, Large)
SideDamageUp = Enhancement("Side",34,35, Large)
BackDamageUp = Enhancement("Back",35,36, Large)
SurpriseAttackUp = Enhancement("Suprise",36,37, Giga)
ToppleDamageUp = Enhancement("Topple",37,38, Large)
LaunchDamageUp = Enhancement("Launch",38,39, Large)
SmashDamageUp = Enhancement("Smash",39,40, Mega)
HigherLVEnemyDamageUp = Enhancement("Underdog",40,41, Large)
AllyDownDamageUp = Enhancement("Comeback",41,42, Mega)
GuardAnnulAttack = Enhancement("Pierce",42,43, Medium)
AnnulReflect = Enhancement("Phase",43,44, Medium)
DamageUpWhenHpDown = Enhancement("Desperation",44,45, Small, Large)
BattleDurationDamageUp = Enhancement("Delayed",45,46, Large) # Uses weird parameter see above
DamageUpOnEnemyKill = Enhancement("Massacre",46,47, Medium)
BreakDurationUp = Enhancement("B Duration",47,48, Medium)
ToppleDurationUp = Enhancement("T Duration",48,49, Medium)
LaunchDurationUp = Enhancement("L Duration",49,50, Medium)
AutoAttackDamageUp = Enhancement("Automatic",50,51, Mega)
AggroedEnemyDamageUp = Enhancement("Self Defense",51,52, Large)
IndoorsDamageUp = Enhancement("Indoor",52,53, Medium)
OutdoorsDamageUp = Enhancement("Outdoor",53,54, Small)
BladeSwitchDamageUp = Enhancement("Switchup",54,55, Small)
OppositeGenderBladeDamageUp = Enhancement("Counterpart",55,56, Medium)
ReduceEnemyToppleResist = Enhancement("Toppler",56,57, Medium) # [ML:Enhance kind=Param1 ]% put that there to make game show the change?
ReduceEnemyLaunchResist = Enhancement("Breaker",57,58, Medium)
OnBlockNullDamage = Enhancement("Guardian",59, 59, Small)
HPLowEvasion = Enhancement("Sway",62, 60, Small, Medium)
EvasionWhileMoving = Enhancement("Agile",63, 61, Medium)
HPLowBlockRate = Enhancement("Block",64, 62, Small, Medium)
ReduceDamageFromNearbyEnemies = Enhancement("Aura",65, 63, Small)
ReduceDamageOnLowHP = Enhancement("Everlasting",66,64, Small, Small)
HighHPDamageUp = Enhancement("Confidence",67,65, Reverse(Medium),Large )
ReduceSpikeDamage =Enhancement("Spike Breaker",68,66, Medium)
BreakResistUp = Enhancement("Unbreakable",69, 67, Medium)
ToppleResistUp = Enhancement("Untoppleable",70, 68, Medium)
LaunchResistUp = Enhancement("Unlaunchable",71, 69, Medium)
SmashResistUp = Enhancement("Unsmashable",72, 70, Medium)
BlowdownResistUp = Enhancement("Unblowdownable",73, 71, Medium)
KnockbackResistUp = Enhancement("Unknockbackable",74, 72, Medium)
DefenseAnnulResistUp = Enhancement("Unpierceable",75, 73, Medium)
AutoAttackAggroDown = Enhancement("Aggro Down",77, 75, Large)
AutoAttackAggroUp = Enhancement("Aggro Up",78, 76, Large)
SpecialAndArtsAggroDown = Enhancement("Aggro Down",79, 77, Medium) # Custom Descriptoion
# SpecialAggroDown = EnhanceEff(79, 79, Medium) uses same enchance id so idk how this works
SpecialAndArtsAggroUp = Enhancement("Aggro Up",80, 81, Medium)
AggroReductionUp = Enhancement("Friendly",81, 85, Small)
AggroEverySecond = Enhancement("Provocative",82, 86, Small) # Get UI to show the increase
StartBattleAggro = Enhancement("Irksome",83, 92, Giga)
RevivalHP = Enhancement("Revival",84, 96, Large)
RevivalHPTeammate = Enhancement("Revival",85, 97, Large)
HealingArtsUp = Enhancement("Support",88, 98, Small)
IncreaseSelfHeal = Enhancement("Lively",89,99, Medium)
SpecialRechargeCancelling = Enhancement("Special",92, 100, Medium)
AutoAttackCancelDamageUp = Enhancement("Full Auto",93, 101, Medium)
Unbeatable = Enhancement("Unbeatable",94, 102, Medium)
NightAccuracy = Enhancement("Nocturnal",95, 103, Large)
DayAccuracy = Enhancement("Diurnal",96, 104, Large)
ExpEnemiesBoost = Enhancement("Wisdom",97, 105, Medium)
WPEnemiesBoost = Enhancement("Expert",98, 106, Large)
PartyGaugeExcellentFill = Enhancement("Party",101, 109, Small) # Show amount
PartyGaugeCritFill = Enhancement("Party",102, 112, Mini) #Show Amount
PartyGaugeDriverArtFill = Enhancement("Party",103, 115, Baby)
DamageUpEnemyNumber = Enhancement("Underdog",104, 116, Medium)
ReflectDamageUp = Enhancement("Reflection",105, 117, Large)
CritDuringChain = Enhancement("Critical",107, 118, Medium)
ChainAttackHeal = Enhancement("Chain Heal",108, 119, Medium)
DriverReviveChainAttack = Enhancement("Resurrection",109, 120)
PartyGaugeFillEndChain = Enhancement("Rechain",110, 121, Medium) # Show amount
EtherCannonRange =Enhancement("Sniper",111, 122, Mini)
WhenDiesHealAllies = Enhancement("Wish",112, 123, Medium)
FirstArtDamage = Enhancement("STRIKE",114,125, Mega)
RingABell = Enhancement("Special",115, 126, Medium)
AutoBalancer = Enhancement("Balancer",116, 127)
EnemyGoldDrop = Enhancement("Alchemy",117, 128, Large)
AllWeaponAttackUp = Enhancement("Master",120, 130, Small)
PreventAffinityLossOnDeath = Enhancement("Affinity",121, 131)
AffinityUpButtonChallenge = Enhancement("Affinity",122, 132, Medium)
MissAffinityUp = Enhancement("Affinity",123, 133, Small)
DamageTakenAffinityUp = Enhancement("Affinity",124,134, Small)
BladeArtsTriggerUp = Enhancement("Artsy",125, 135, Large)
BladeArtDuration = Enhancement("Artsy",126, 136, Medium)
AffinityMaxBarrier = Enhancement("Barrier",127, 137, Small)
AffinityMaxAttack = Enhancement("Battlecry",128, 138, Medium)
AffinityMaxEvade = Enhancement("Dodgy",129, 139, Small)
HunterChem = Enhancement("Hunter",130, 140, Mega)
ShoulderToShoulder = Enhancement("Prey",131, 141, Mega)
BladeCooldownReduc = Enhancement("Swapper",132, 142, Medium)
PartyHealBladeSwitch = Enhancement("Parting Gift",133, 143, Small)
AffinityRange = Enhancement("Bluetooth",134, 144, Mega)
LV1Damage = Enhancement("LV1 Damage",135, 145,[1], Large)
LV2Damage = Enhancement("LV2 Damage",135, 145,[2], Large)
LV3Damage = Enhancement("LV3 Damage",135, 145,[3], Large)
LV4Damage = Enhancement("LV4 Damage",135, 145,[4], Large)
SmallHpPotCreate = Enhancement("Bottle",136, 146, Small)
PotionEffectUp = Enhancement("Potioneer",137, 147, Medium)
PurifyingFlames = Enhancement("Purifying",138, 148, Small, Mini)
ForeSight = Enhancement("Foresight",139, 149, Small)
DreamOfTheFuture = Enhancement("Dream",140, 150)
ReduceEnemyBladeComboDamage = Enhancement("",142, 151, Medium)
DamagePerEvadeUp = Enhancement("",143, 152, Mini)
ArtsRechargeMaxAffinity = Enhancement("",144, 154, Small)
ReduceAggroFromAttacks = Enhancement("",145, 155, Small)
PhyAndEthDefenseUp = Enhancement("",146, 156, Small)
ChanceToPerfectHitAndEvade = Enhancement("",147, 157, Small)
Reflection = Enhancement("",148, 158, Small)
MaxAffinityEvadeXAttacks = Enhancement("",149, 159, Mini)
ToppleANDLaunchDamageUp = Enhancement("",150, 160, Large)
InstaKill = Enhancement("",151,161, Baby)
PartyDamageReducMAxAffinity = Enhancement("",152, 162, Mini)
KaiserZone = Enhancement("",153, 163, Medium)
TastySnack = Enhancement("",154, 164, Medium)
HealingUpMaxAffinity =  Enhancement("",155, 165, Small)
AggroPerSecondANDAggroUp  = Enhancement("",156, 166, Small, Small)
MoreDamTakeLessAllyLowOrDown = Enhancement("",157, 167, Large, Small)
StopThinking = Enhancement("",158, 168, Medium, Baby)
LowHPSpecialUp = Enhancement("",159, 169, Baby) #Uses decimals weird one not sure how it scales
TranquilGuard = Enhancement("",160, 171, Small)
HPRestoreFusionCombo = Enhancement("",161, 172, Baby)
AttackUpGoldUp = Enhancement("",162, 173, Baby, Mega)
EnemyDropGoldOnHit = Enhancement("",163, 174, Medium)
ReduceEnemyChargeMaxAffinity = Enhancement("",164, 175, Small)
VersusBossUniqueEnemyDamageUp = Enhancement("",165, 176, Medium)
DidIDoThat = Enhancement("",166, 177, Mini)
AnnulEnemyDefAndSPecialDamageUp = Enhancement("",167, 178, Small)
GlassCannon = Enhancement("",168, 179, Large, Small)
AnnulDef = Enhancement("",169, 180, Medium)
Transmigration = Enhancement("",170, 181, Medium)
ElementalWeaknessDamageUP = Enhancement("",171, 182, Large) #Show
GravityPinwheel = Enhancement("",172, 183, Small, Baby)
AutoAttackSpeed= Enhancement("",173, 184, Large)
DoubleHitExtraAutoDamage = Enhancement("",174, 185, Large)
ToppleDamageANDDurationUp = Enhancement("",175, 186, Medium, Mini)
EvadeDrainHp = Enhancement("",176, 187, Mini)
AggroReducOnLandingHit = Enhancement("",177, 188, Medium)
RecoverRechargeCrit = Enhancement("",178, 189, Medium)
SpecialAffinityUp = Enhancement("",179,191, Medium)
BreakResDown = Enhancement("",180, 192, Small)
RepeatSpecialDamage = Enhancement("",182, 193, Small)
Twang = Enhancement("",183, 194, Small, Baby)
MaxAffinityAccuracy = Enhancement("",184, 195, Large)
PotionStayLonger = Enhancement("",185, 196, Small)
FemaleDamageUp = Enhancement("",186, 197, Mini)
DealMoreTakeLessMaxAffinity = Enhancement("",187, 198, Mini, Small)
CritUpChainAttackSelected =Enhancement("",188,199,Medium)
DealDamageWhenSwappedIn = Enhancement("",189, 200, Mini)
CancelWindowUp = Enhancement("",191, 201, Medium)
RestoreHitDamageToParty = Enhancement("",192, 202, Baby)
AddBufferTimeSwitchingToComboBlade = Enhancement("",193, 203, Medium)
PartyDamageMaxAffinity = Enhancement("",194, 204, Mini)
AegisDriver = Enhancement("",195, 205, Medium, Small)
AegisParty = Enhancement("",196, 206)
ReduceFireDamage = Enhancement("",58, 207, [1], Medium)
ReduceWaterDamage = Enhancement("",58, 208, [2], Medium)
ReduceWindDamage = Enhancement("",58, 209, [3], Medium)
ReduceEarthDamage = Enhancement("",58, 210, [4], Medium)
ReduceElectricDamage = Enhancement("",58, 211, [5], Medium)
ReduceIceDamage = Enhancement("",58, 212, [6], Medium)
ReduceLightDamage = Enhancement("",58, 213, [7], Medium)
ReduceDarkDamage = Enhancement("",58, 214, [8], Medium)
ChainAttackPower = Enhancement("",106, 215, Baby) # Show
LowHPHeal = Enhancement("",181, 230, Baby)
ArtUseHeal = Enhancement("",86, 231, Baby)
AutoDriverArtCancelHeal = Enhancement("",91, 233, Baby)
TakeDamageHeal = Enhancement("",90, 235, Mini)
HealMoving = Enhancement("",87, 236, Mini)
MaxAffinityHeal = Enhancement("",141,237,Mini)
AbsorbFireBlock = Enhancement("",60, 238, [1])
AbsorbWaterBlock = Enhancement("",60, 239, [2])
AbsorbWindBlock = Enhancement("",60, 240, [3])
AbsorbEarthBlock = Enhancement("",60, 241, [4])
AbsorbElectricBlock = Enhancement("",60, 242, [5])
AbsorbIceBlock = Enhancement("",60, 243, [6])
AbsorbLightBlock = Enhancement("",60, 244, [7])
AbsorbDarkBlock = Enhancement("",60, 245, [8])
ReflectFireBlock = Enhancement("",61, 246, [1])
ReflectWaterBlock = Enhancement("",61, 247, [2])
ReflectWindBlock = Enhancement("",61, 248, [3])
ReflectEarthBlock = Enhancement("",61, 249, [4])
ReflectElectricBlock = Enhancement("",61, 250, [5])
ReflectIceBlock = Enhancement("",61, 251, [6])
ReflectLightBlock = Enhancement("",61, 252, [7])
ReflectDarkBlock = Enhancement("",61, 253, [8])
AegisPowerUp = Enhancement("",119, 254, [1], Small)
CatScimPowerUp = Enhancement("",119, 255, [2], Small)
TwinRingPowerUp = Enhancement("",119, 256, [3], Small)
DrillShieldPowerUp = Enhancement("",119, 257, [4], Small)
MechArmsPowerUp = Enhancement("",119, 258, [5], Small)
VarSaberPowerUp = Enhancement("",119, 259, [6], Small)
WhipswordPowerUp = Enhancement("",119, 260, [7], Small)
BigBangPowerUp = Enhancement("",119, 261, [8], Small)
DualScythesPowerUp = Enhancement("",119, 262, [9], Small)
GreataxePowerUp = Enhancement("",119, 263, [10], Small)
MegalancePowerUp = Enhancement("",119, 264, [11], Small)
EtherCannonPowerUp = Enhancement("",119, 265, [12], Small)
ShieldHammerPowerUp = Enhancement("",119, 266, [13], Small)
ChromaKatanaPowerUp = Enhancement("",119, 267, [14], Small)
BitballPowerUp = Enhancement("",119, 268, [15], Small)
KnuckleClawsPowerUp = Enhancement("",119, 269, [16], Small)
HPGuardArtRechargeAttacked = Enhancement("",197,270, Mini)
Jamming = Enhancement("",198, 271, Medium)
XStartBattle = Enhancement("X Start",113, 272, [0])
YStartBattle = Enhancement("Y Start",113, 274, [1])
BStartBattle = Enhancement("B Start",113, 276, [2])
ArtCancel = Enhancement("Arts Cancel",190, 278)
BladeSwitchCooldownWithArts = Enhancement("",200, 279, Small)
TauntRes = Enhancement("",217, 280, Medium)
DriverShackRes = Enhancement("",218, 281, Medium)
BladeShackRes = Enhancement("",219, 282, Medium)
BurstDestroyAnotherOrb = Enhancement("",226, 283)
HpPotChanceFor2 = Enhancement("",227, 284, Medium)
DestroyOrbOpposingElement = Enhancement("",228, 285)
TargetNearbyOrbsChainAttack = Enhancement("",229, 286, Medium)
TargetDamagedNonOpposingElement = Enhancement("",230, 287)
StenchRes = Enhancement("",231, 288, Medium)
HPPotOnHitAgain = Enhancement("",227, 289)
BladeComboOrbAdder = Enhancement("",234,290, Medium)
EvadeDriverArt = Enhancement("",32, 292)
RetainAggro = Enhancement("",235, 293, Medium)
DamageUpOnDeath = Enhancement("",238, 295, Large)
AutoSpeedArtsSpeed= Enhancement("",240, 296, Small, Small)
LV4EachUseDmageUp = Enhancement("",241, 297, Large)
Vision = Enhancement("",242, 298, Reverse(Medium))
AwakenPurge = Enhancement("",243, 299, Medium)
PartyCritMaxAffinity = Enhancement("",244, 300, Small)
DamageUpPerCrit = Enhancement("",245, 301, Mini)
RechargeOnEvade = Enhancement("",248, 304, Baby)
DamageAndEvadeAffinityMax = Enhancement("",269, 305, Medium, Mini)
PartyLaunchDamageUp = Enhancement("",249, 306, Mega)
PotionPickupDamageUp = Enhancement("",250, 307, Small)
ItemCollectionRange = Enhancement("",251, 308, Mega)
CombatSpeed = Enhancement("",211, 309, Mega)
NullHealRes = Enhancement("",252, 310, Medium)
DoomRes = Enhancement("",253, 311, Medium)
PartyDrainRes = Enhancement("",254, 312, Medium)
DealTakeMore = Enhancement("",255, 313, Medium, Medium)
AllDebuffRes = Enhancement("",258, 316, Small)
DamageUpOnCancel = Enhancement("",259, 317, Mini)
PurgeRage = Enhancement("",261, 318, Medium)
DamageAndCritUpMaxAffinity = Enhancement("",263, 320, Medium, Medium)
ReducesTerrainDamage = Enhancement("",264, 334, Medium)
SpecialRecievesAfterImage = Enhancement("",213, 335, Baby)
EyeOfJustice = Enhancement("Eye of Shining Justice",236,294)
#There are some torna effects not including them recoverable hp.
