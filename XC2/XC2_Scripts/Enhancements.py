import random, json
from scripts import JSONParser, Helper

Baby = [1,2,4,5]
Mini = [1,7,14,20]
Small = [10,20,35,50]
Medium = [20,40,70,100]
High= [70,100,130,150]
Large = [30,100,200,300]
Mega = [60,200,400,600]
Massive = [300,600,1000,1500]
Giga = [1000,1700,2500,3000]


EnhanceEffectsList = []
DisplayTagList = []
EnhanceClassList = []
EnhanceID = 3896
DisplayTagID = 65


class Enhancement: 
    id = 0
    name = ""
    EnhanceEffect = 0
    Param1 =   0
    Param2 =  0
    Caption = 0
    Caption2 = 0
    Description = ""
    Rarity = 0
    ReversePar1 = False
    ReversePar2 = False
    addToList = True
    DisTag = ""
    def __init__(self,Name, Enhancement, Caption, Param1 = [0,0,0,0], Param2 = [0,0,0,0], Description = "", ReversePar1 = False, ReversePar2  = False, addToList = True, DisTag = "", max = [0,0], isRounded = True):
        self.name = Name
        self.EnhanceEffect = Enhancement
        self.Caption = Caption
        self.Caption2 = Caption
        self.Param1 = Param1
        self.Param2 = Param2
        self.Description = Description
        self.ReversePar1 = ReversePar1
        self.ReversePar2 = ReversePar2
        self.addToList = addToList
        self.DisTag = DisTag
        self.max = max
        self.isRounded = isRounded
        if self.addToList:
            EnhanceClassList.append(self)
            
        if self.DisTag != "":
            global DisplayTagID
            DisplayTagDict = {
            "$id": DisplayTagID,
            "style": 36,
            "name": self.DisTag,
            "enhanceEff": self.EnhanceEffect
            }
            DisplayTagID += 1
            DisplayTagList.append(DisplayTagDict)

    def RollEnhancement(self, forcedRarity = None, scalingFactor = 1):
        global EnhanceID
        self.id = EnhanceID
        EnhanceID += 1
        Common = 0
        Rare = 1
        Legendary = 2
        if forcedRarity == None:
            self.Rarity = random.choice([Common,Common,Common, Rare,Rare, Legendary])
        else:
            self.Rarity = forcedRarity
        self.scalingFactor = scalingFactor
        def SetParams(ParameterChoices, isReverse):
            Multiplier = 1/scalingFactor if isReverse else scalingFactor

            if ParameterChoices == [0,0,0,0]:
                Parameter = 0
            elif len(ParameterChoices) == 1:
                Parameter = ParameterChoices[0]
            else:
                Parameter = random.uniform(ParameterChoices[self.Rarity+(1*isReverse)],ParameterChoices[self.Rarity + 1 - (2*isReverse)])

                    
            Parameter *= Multiplier
            
            if self.isRounded:
                Parameter = round(Parameter)
                
            return Parameter
            
        if self.Description != "":
            JSONParser.ChangeJSONLine(["common_ms/btl_enhance_cap.json"],[self.Caption], ["name"], self.Description)
            
        EnhanceEffectsDict = {
            "$id": EnhanceID,
            "EnhanceEffect": self.EnhanceEffect,
            "Param1": SetParams(self.Param1, self.ReversePar1),
            "Param2": SetParams(self.Param2, self.ReversePar2),
            "Caption": self.Caption,
            "Caption2": self.Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])
        
def AddCustomEnhancements():
    global EnhanceID
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], Helper.InclRange(1,1000), [1000], [241, 250, 245,54,143,257,259])
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[45], ["Param"], random.randrange(20,51, 5)) # Battle damage up after a certain time uses nonstandard parameter this fixes it
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[181], ["Param"], random.randrange(30,71, 5)) # Healing with low HP
    JSONParser.ChangeJSONLine(["common/BTL_EnhanceEff.json"],[90], ["Param"], random.randrange(10,61,5)) # Healing with low HP
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json", EnhanceEffectsList)
    EnhanceID = 3896
    EnhanceEffectsList.clear()

def HandleAllRange(start, stop, step):
    pass
    

def SearchAndSetDisplayIDs():
    global DisplayTagID
    with open("./XC2/JsonOutputs/common/BTL_EnhanceEff.json", 'r+', encoding='utf-8') as EnEffFile:
        with open("./XC2/JsonOutputs/common_ms/btl_buff_ms.json", 'r+', encoding='utf-8') as btlBuffFile:
            EnEff = json.load(EnEffFile)
            btlBuff = json.load(btlBuffFile)
            disList = DisplayTagList

            
            for eff in EnEff["rows"]:   # sets names in EnhanceEff File
                for enhancement in disList:        
                    if enhancement["enhanceEff"] == eff["$id"]:
                        eff["Name"] = enhancement["$id"]
                        break

            for item in disList: # adds name to ms file
                btlBuff["rows"].append({
                    "$id": item["$id"],
                    "style": item["style"],
                    "name": item["name"],   
                })
        
            btlBuffFile.seek(0)
            btlBuffFile.truncate()
            json.dump(btlBuff, btlBuffFile, indent=2, ensure_ascii=False)       
        EnEffFile.seek(0)
        EnEffFile.truncate()
        json.dump(EnEff,  EnEffFile, indent=2, ensure_ascii=False)    



HPBoost = Enhancement("Health",1,1, Small)
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
BladeComboDamUp = Enhancement("Combo",23,21, Large)
FusionComboDamUp = Enhancement("Combo",24,22, Large)
EtherCounter = Enhancement("Eth Counter",25,23, Giga)
PhysCounter = Enhancement("Phys Counter",26,24, Giga, addToList=False)
AutoAttackHeal = Enhancement("Auto Vamp",27,26, Mini)
SpecialANDArtHeal = Enhancement("Omnivamp",28,27, Baby, Description="Restores [ML:Enhance kind=Param1 ]% HP of damage dealt when\n a Special or Art connects.")
ArtDamageHeal = Enhancement("Omnivamp",28, 28, Small) # This goes on arts only or else it will heal from special and arts
EnemyKillHeal = Enhancement("Scavenger",29,30, Medium)
CritHeal = Enhancement("Crit Vamp",30,31, Mini)
CritDamageUp = Enhancement("Crit Damage",31,32, Medium)
PercentDoubleAuto = Enhancement("Doublestrike",32,33, Medium, DisTag="Doublestrike")
FrontDamageUp = Enhancement("Front",33,34, Medium)
SideDamageUp = Enhancement("Side",34,35, Medium)
BackDamageUp = Enhancement("Back",35,36, Medium)
SurpriseAttackUp = Enhancement("Surprise",36,37, Giga, DisTag="Surprise!")
ToppleDamageUp = Enhancement("Topple",37,38, Large, DisTag="Topple Damage ↑")
LaunchDamageUp = Enhancement("Launch",38,39, Large, DisTag="Launch Damage ↑")
SmashDamageUp = Enhancement("Smash",39,40, Mega, DisTag="Smash Damage ↑")
HigherLVEnemyDamageUp = Enhancement("Underdog",40,41, Large)
AllyDownDamageUp = Enhancement("Comeback",41,42, Mega, DisTag="Strength ↑")
GuardAnnulAttack = Enhancement("Pierce",42,43, Medium, DisTag="Pierce")
AnnulReflect = Enhancement("Phase",43,44, Medium, DisTag="Phase")
DamageUpWhenHpDown = Enhancement("Desperation",44,45, Small, Large, DisTag="Desperation Attack")
BattleDurationDamageUp = Enhancement("Delayed",45,46, High, DisTag="Strength ↑") # Uses weird parameter see above
DamageUpOnEnemyKill = Enhancement("Massacre",46,47, Medium, DisTag="Damage ↑", max=[100,600])
BreakDurationUp = Enhancement("Duration",47,48, Medium, DisTag="Break Duration ↑")
ToppleDurationUp = Enhancement("Duration",48,49, Medium, DisTag="Topple Duration ↑")
LaunchDurationUp = Enhancement("Duration",49,50, Medium, DisTag="Launch Duration ↑")
AutoAttackDamageUp = Enhancement("Automatic",50,51, Mega)
AggroedEnemyDamageUp = Enhancement("Self Defense",51,52, Large)
IndoorsDamageUp = Enhancement("Indoor",52,53, Medium)
OutdoorsDamageUp = Enhancement("Outdoor",53,54, Small)
BladeSwitchDamageUp = Enhancement("Switchup",54,55, Small, max=[100,500])
OppositeGenderBladeDamageUp = Enhancement("Counterpart",55,56, Medium)
ReduceEnemyToppleResist = Enhancement("Toppler",56,57, Medium)
ReduceEnemyLaunchResist = Enhancement("Breaker",57,58, Medium)
OnBlockNullDamage = Enhancement("Guardian",59, 59, Small, DisTag="Null Damage")
HPLowEvasion = Enhancement("Sway",62, 60, Small, Medium, DisTag="Sway")
EvasionWhileMoving = Enhancement("Agile",63, 61, Medium)
HPLowBlockRate = Enhancement("Block",64, 62, Small, Medium, DisTag="Block ↑")
ReduceDamageFromNearbyEnemies = Enhancement("Guardian",65, 63, Mini)
ReduceDamageOnLowHP = Enhancement("Everlasting",66,64, Small, Small)
HighHPDamageUp = Enhancement("Confidence",67,65, Medium,Large, ReversePar1=True )
ReduceSpikeDamage =Enhancement("Spike Breaker",68,66, Medium)
BreakResistUp = Enhancement("Fluid",69, 67, Medium)
ToppleResistUp = Enhancement("Lithe",70, 68, Medium)
LaunchResistUp = Enhancement("Heavyweight",71, 69, Medium)
SmashResistUp = Enhancement("Unsmashable",72, 70, Medium)
BlowdownResistUp = Enhancement("Steady",73, 71, Medium)
KnockbackResistUp = Enhancement("Steady",74, 72, Medium)
DefenseAnnulResistUp = Enhancement("Unpierceable",75, 73, Medium)
AutoAttackAggroDown = Enhancement("Aggro ↓",77, 75, Large)
AutoAttackAggroUp = Enhancement("Aggro ↑",78, 76, Large)
SpecialAndArtsAggroDown = Enhancement("Aggro ↓",79, 77, Medium)
SpecialAggroDown = Enhancement("Aggro ↓",79, 79, Medium) # For Specials only 
SpecialAndArtsAggroUp = Enhancement("Aggro ↑",80, 81, Medium)
AggroReductionUp = Enhancement("Friendly",81, 85, Small)
AggroEverySecond = Enhancement("Provocative",82, 86, Small, Description="Increases aggro every second by [ML:Enhance kind=Param1 ].") # didnt work??
StartBattleAggro = Enhancement("Irksome",83, 92, Giga) # distag didnt work
RevivalHP = Enhancement("Revival",84, 96, Large, DisTag="Revival HP↑")
RevivalHPTeammate = Enhancement("Revival",85, 97, Large, DisTag="Revival HP↑")
HealingArtsUp = Enhancement("Support",88, 98, Small)
IncreaseSelfHeal = Enhancement("Lively",89,99, Medium)
SpecialRechargeCancelling = Enhancement("Special",92, 100, Medium)
AutoAttackCancelDamageUp = Enhancement("Skillful",93, 101, Medium, DisTag="Cancel Dmg↑")
Unbeatable = Enhancement("Unbeatable",94, 102, Medium, DisTag="Unbeatable")
NightAccuracy = Enhancement("Nocturnal",95, 103, Large, DisTag="Noctural")
DayAccuracy = Enhancement("Diurnal",96, 104, Large, DisTag="Diurnal")
ExpEnemiesBoost = Enhancement("Wisdom",97, 105, Medium)
WPEnemiesBoost = Enhancement("Expert",98, 106, Large)
PartyGaugeExcellentFill = Enhancement("Party",101, 109, Small, Description="Fills the Party Gauge on an\n\"Excellent\" Special by [ML:Enhance kind=Param1 ].")
PartyGaugeCritFill = Enhancement("Party",102, 112, Mini, Description="Fills the Party Gauge for\neach critical hit delivered by [ML:Enhance kind=Param1].")
PartyGaugeDriverArtFill = Enhancement("Party",103, 115, Baby, Description="Fills the Party Gauge\nfor each Driver Art used by [ML:Enhance kind=Param1].")
DamageUpEnemyNumber = Enhancement("Underdog",104, 116, Medium, max=[100,500])
ReflectDamageUp = Enhancement("Reflection",105, 117, Large)
CritDuringChain = Enhancement("Critical",107, 118, Medium)
ChainAttackHeal = Enhancement("Chain Heal",108, 119, Medium)
DriverReviveChainAttack = Enhancement("Resurrection",109, 120)
PartyGaugeFillEndChain = Enhancement("Rechain",110, 121, Medium, Description="Fills the Party Gauge\nat the end of each Chain Attack by [ML:Enhance kind=Param1 ].")
EtherCannonRange =Enhancement("Sniper",111, 122, Mini)
WhenDiesHealAllies = Enhancement("Wish",112, 123, Medium, DisTag="Wish Heal")
FirstArtDamage = Enhancement("STRIKE",114,125, Mega, DisTag="First Strike")
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
AffinityMaxAttack = Enhancement("Battlecry",128, 138, Medium, DisTag="Damage ↑")
AffinityMaxEvade = Enhancement("Dodgy",129, 139, Small, DisTag="Evasion ↑")
HunterChem = Enhancement("Hunter",130, 140, Mega, DisTag="Hunter's Chemistry")
ShoulderToShoulder = Enhancement("Prey",131, 141, Mega, DisTag="Shoulder-to-Shoulder")
BladeCooldownReduc = Enhancement("Swapper",132, 142, Medium)
PartyHealBladeSwitch = Enhancement("Parting Gift",133, 143, Small, DisTag="Switch Heal")
AffinityRange = Enhancement("Bluetooth",134, 144, Mega)
LV1Damage = Enhancement("Lv1↑ Damage",135, 145,[1], Large, DisTag="Boosted Lv1")
LV2Damage = Enhancement("Lv2↑ Damage",135, 145,[2], Large, DisTag="Boosted Lv2")
LV3Damage = Enhancement("Lv3↑ Damage",135, 145,[3], Large, DisTag="Boosted Lv3")
LV4Damage = Enhancement("Lv4↑ Damage",135, 145,[4], Large, DisTag="Boosted Lv4")
SmallHpPotCreate = Enhancement("Bottle",136, 146, Small)
PotionEffectUp = Enhancement("Potioneer",137, 147, Medium, DisTag="Potion ↑")
PurifyingFlames = Enhancement("Purifying",138, 148, Small, Mini)
ForeSight = Enhancement("Foresight",139, 149, Small)
DreamOfTheFuture = Enhancement("Dream",140, 150, addToList=False)
ReduceEnemyBladeComboDamage = Enhancement("Blade↓",142, 151, Medium, DisTag="Resist Combo")
DamagePerEvadeUp = Enhancement("Counterattack",143, 152, Mini, DisTag="Damage ↑", max=[100,400])
ArtsRechargeMaxAffinity = Enhancement("Arts Charging",144, 154, Small)
ReduceAggroFromAttacks = Enhancement("Aggro↓",145, 155, Small)
PhyAndEthDefenseUp = Enhancement("Full Guard",146, 156, Small)
ChanceToPerfectHitAndEvade = Enhancement("Parry",147, 157, Mini, DisTag="Perfection")
Reflection = Enhancement("Reflection",148, 158, Small)
MaxAffinityEvadeXAttacks = Enhancement("Harmony",149, 159, Mini, DisTag="Harmony Evasion")
ToppleANDLaunchDamageUp = Enhancement("Top Launch",150, 160, Large)
InstaKill = Enhancement("Instakill",151,161, Baby)
PartyDamageReducMaxAffinity = Enhancement("Guardian",152, 162, Mini)
KaiserZone = Enhancement("Kaiser",153, 163, Medium)
TastySnack = Enhancement("Snack",154, 164, Medium)
HealingUpMaxAffinity = Enhancement("Healing",155, 165, Small)
AggroPerSecondANDAggroUp  = Enhancement("Aggy",156, 166, Small, Small)
MoreDamTakeLessAllyLowOrDown = Enhancement("Super",157, 167, Large, Small)
StopThinking = Enhancement("Enthrall",158, 168, Medium, Baby)
LowHPSpecialUp = Enhancement("Specialist",159, 169, [0.5,0.7,1,1.5]) #Uses decimals weird one not sure how it scales boosted special shows up wrong
TranquilGuard = Enhancement("Stance",160, 171, Small)
HPRestoreFusionCombo = Enhancement("Fusion",161, 172, Baby)
AttackUpGoldUp = Enhancement("Mercenary",162, 173, Baby, Mega, Description="Increases attack power by [ML:Enhance kind=Param1 ]% as gold is\ncollected during battle (max: [ML:Enhance kind=Param2 ]%).")
EnemyDropGoldOnHit = Enhancement("Pickpocket",163, 174, Medium)
ReduceEnemyChargeMaxAffinity = Enhancement("Syrup",164, 175, Small)
VersusBossUniqueEnemyDamageUp = Enhancement("Challenger",165, 176, Medium)
DidIDoThat = Enhancement("Repeat",166, 177, Small)
AnnulEnemyDefAndSpecialDamageUp = Enhancement("Pierce+",167, 178, Small)
GlassCannon = Enhancement("Reckless",168, 179, Large, Small)
AnnulDef = Enhancement("Pierce",169, 180, Medium)
Transmigration = Enhancement("Transmigration",170, 181, Medium)
ElementalWeaknessDamageUP = Enhancement("Elementalist",171, 182, Large, Description= "Increases damage dealt when elemental\nweakness exploited by [ML:Enhance kind=Param1 ]% (affects all).") 
GravityPinwheel = Enhancement("Rebound",172, 183, Small, Baby)
AutoAttackSpeed= Enhancement("Tempo",173, 184, Large)
DoubleHitExtraAutoDamage = Enhancement("Restrike",174, 185, Large)
ToppleDamageANDDurationUp = Enhancement("Piledriver",175, 186, Medium, Mini)
EvadeDrainHp = Enhancement("Evade",176, 187, Mini) # Rocs Evasion art
AggroReducOnLandingHit = Enhancement("Concussion",177, 188, Medium)
RecoverRechargeCrit = Enhancement("Flurry",178, 189, Medium)
SpecialAffinityUp = Enhancement("Specialist",179,191, Medium)
BreakResDown = Enhancement("Breaker",180, 192, Small)
RepeatSpecialDamage = Enhancement("Magician",182, 193, Small, DisTag="Special ↑", max=[100,500])
Twang = Enhancement("Twang",183, 194, Small, Baby)
MaxAffinityAccuracy = Enhancement("Hone",184, 195, Large)
PotionStayLonger = Enhancement("Preservative",185, 196, Small)
FemaleDamageUp = Enhancement("Girly",186, 197, Mini)
DealMoreTakeLessMaxAffinity = Enhancement("Overwhelm",187, 198, Mini, Small)
CritUpChainAttackSelected =Enhancement("Critical",188,199,Medium)
BladeSwapDamage = Enhancement("Entrance",189, 200, Mini)
CancelWindowUp = Enhancement("Canceller",191, 201, Medium)
RestoreHitDamageToParty = Enhancement("Vamp",192, 202, Baby)
AddBufferTimeSwitchingToComboBlade = Enhancement("Buffer",193, 203, Medium)
PartyDamageMaxAffinity = Enhancement("Partygoer",194, 204, Mini)
AegisDriver = Enhancement("Dream",195, 205, addToList=False)
AegisParty = Enhancement("Dream",196, 206, addToList=False)
ReduceFireDamage = Enhancement("Fire↓",58, 207, [1], Medium, DisTag="Fire ↓")
ReduceWaterDamage = Enhancement("Water↓",58, 208, [2], Medium, DisTag="Water ↓")
ReduceWindDamage = Enhancement("Wind↓",58, 209, [3], Medium, DisTag= "Wind ↓")
ReduceEarthDamage = Enhancement("Earth↓",58, 210, [4], Medium, DisTag="Earth ↓")
ReduceElectricDamage = Enhancement("Electric↓",58, 211, [5], Medium, DisTag="Electric ↓")
ReduceIceDamage = Enhancement("Ice↓",58, 212, [6], Medium, DisTag="Ice ↓")
ReduceLightDamage = Enhancement("Light↓",58, 213, [7], Medium, DisTag="Light ↓")
ReduceDarkDamage = Enhancement("Dark↓",58, 214, [8], Medium, DisTag="Dark ↓")
ChainAttackPower = Enhancement("Superchain",106, 215, Baby, Description="Increases attack power ratio\nat the start of a Chain Attack by [ML:Enhance kind=Param1 ].")
LowHPRegen = Enhancement("Regenerate",181, 230, Mini)
ArtUseHeal = Enhancement("Art Heal",86, 231, Baby)
AutoDriverArtCancelHeal = Enhancement("Heal",91, 233, Baby)
TakeDamageHeal = Enhancement("Mending",90, 235, Mini, DisTag="Mend")
HealMoving = Enhancement("Rehab",87, 236, Mini)
MaxAffinityHeal = Enhancement("Recovery",141,237,Mini)
AbsorbFireBlock = Enhancement("Fire",60, 238, [1], addToList=False)
AbsorbWaterBlock = Enhancement("Water",60, 239, [2], addToList=False)
AbsorbWindBlock = Enhancement("Wind",60, 240, [3], addToList=False)
AbsorbEarthBlock = Enhancement("Earth",60, 241, [4], addToList=False)
AbsorbElectricBlock = Enhancement("Electric",60, 242, [5], addToList=False)
AbsorbIceBlock = Enhancement("Ice",60, 243, [6], addToList=False)
AbsorbLightBlock = Enhancement("Light",60, 244, [7], addToList=False)
AbsorbDarkBlock = Enhancement("Dark",60, 245, [8], addToList=False)
ReflectFireBlock = Enhancement("Fire",61, 246, [1], addToList=False)
ReflectWaterBlock = Enhancement("Water",61, 247, [2], addToList=False)
ReflectWindBlock = Enhancement("Wind",61, 248, [3], addToList=False)
ReflectEarthBlock = Enhancement("Earth",61, 249, [4], addToList=False)
ReflectElectricBlock = Enhancement("Electric",61, 250, [5], addToList=False)
ReflectIceBlock = Enhancement("Ice",61, 251, [6], addToList=False)
ReflectLightBlock = Enhancement("Light",61, 252, [7], addToList=False)
ReflectDarkBlock = Enhancement("Dark",61, 253, [8], addToList=False)
AegisPowerUp = Enhancement("Aegis",119, 254, [1], Small)
CatScimPowerUp = Enhancement("Scimitar",119, 255, [2], Small)
TwinRingPowerUp = Enhancement("Ring",119, 256, [3], Small)
DrillShieldPowerUp = Enhancement("Drill",119, 257, [4], Small)
MechArmsPowerUp = Enhancement("Arms",119, 258, [5], Small)
VarSaberPowerUp = Enhancement("Saber",119, 259, [6], Small)
WhipswordPowerUp = Enhancement("Whipsword",119, 260, [7], Small)
BigBangPowerUp = Enhancement("Big Bang",119, 261, [8], Small)
DualScythesPowerUp = Enhancement("Scythe",119, 262, [9], Small)
GreataxePowerUp = Enhancement("Greataxe",119, 263, [10], Small)
MegalancePowerUp = Enhancement("Megalance",119, 264, [11], Small)
EtherCannonPowerUp = Enhancement("Cannon",119, 265, [12], Small)
ShieldHammerPowerUp = Enhancement("Shield",119, 266, [13], Small)
ChromaKatanaPowerUp = Enhancement("Katana",119, 267, [14], Small)
BitballPowerUp = Enhancement("Bitball",119, 268, [15], Small)
KnuckleClawsPowerUp = Enhancement("Claws",119, 269, [16], Small)
HPGuardArtRechargeAttacked = Enhancement("Reversal",197,270, Mini, DisTag="Reversal")
Jamming = Enhancement("Jamming",198, 271, Small, DisTag="Jamming")
XStartBattle = Enhancement("X Start",113, 272, [0])
YStartBattle = Enhancement("Y Start",113, 274, [1])
BStartBattle = Enhancement("B Start",113, 276, [2])
ArtCancel = Enhancement("Arts Cancel",190, 278)
BladeSwitchCooldownWithArts = Enhancement("Ready",200, 279, Small)
TauntRes = Enhancement("Calm",217, 280, Medium)
DriverShackRes = Enhancement("Free",218, 281, Medium)
BladeShackRes = Enhancement("Free",219, 282, Medium)
BurstDestroyAnotherOrb = Enhancement("Splash",226, 283, DisTag="Orb Splash")
HpPotChanceFor2 = Enhancement("Potted",227, 284, Medium, addToList=False)
DestroyOrbOpposingElement = Enhancement("Element X",228, 285, DisTag="Orb Buster")
TargetNearbyOrbsChainAttack = Enhancement("Splash",229, 286, Medium, DisTag="Orb Splash")
TargetDamagedNonOpposingElement = Enhancement("Splash",230, 287, DisTag="Orb Focus")
StenchRes = Enhancement("Anosmic",231, 288, Medium)
DamageAndEvadeAffinityMax = Enhancement("Counterattack",269, 305, Medium, Mini)
ForcedHPPotionOnHit = Enhancement("Potter",227, 289)
BladeComboOrbAdder = Enhancement("Orbs",234,290, Medium)
EvadeDriverArt = Enhancement("Evader",32, 292)
RetainAggro = Enhancement("Grudge",235, 293, Medium, DisTag="Grudge")
DamageUpOnDeath = Enhancement("Martyr",238, 295, Large, max=[100,700])
AutoSpeedArtsSpeed= Enhancement("Lightning",240, 296, Small, Small)
LV4EachUseDmageUp = Enhancement("Glow",241, 297, Large, max=[200,2000])
Vision = Enhancement("Monado",242, 298, Medium, ReversePar1=True)
AwakenPurge = Enhancement("Sleepy",243, 299, Medium)
PartyCritMaxAffinity = Enhancement("Critical",244, 300, Small)
DamageUpPerCrit = Enhancement("Exploit",245, 301, Baby, Baby, max=[100,500])
RechargeOnEvade = Enhancement("Flicker",248, 304, Baby)
PartyLaunchDamageUp = Enhancement("Sky High",249, 306, Mega)
PotionPickupDamageUp = Enhancement("Drunkard",250, 307, Small, DisTag="Damage ↑", max=[100,1000])
ItemCollectionRange = Enhancement("Collector",251, 308, Mega)
CombatMoveSpeed = Enhancement("Blitz",211, 309, [40,50,60,70]) # Distag Repeats each step u take
NullHealRes = Enhancement("Healers",252, 310, Medium)
DoomRes = Enhancement("Optimist",253, 311, Medium)
PartyDrainRes = Enhancement("Party",254, 312, Medium)
DealTakeMore = Enhancement("Reckless",255, 313, Medium, Medium)
AllDebuffRes = Enhancement("Dream",258, 316, Small)
DamageUpOnCancel = Enhancement("Rhythm",259, 317, Mini, max=[100,500])
PurgeRage = Enhancement("Soothe",261, 318, Medium)
DamageAndCritUpMaxAffinity = Enhancement("Lucky",263, 320, Medium, Medium)
ReducesTerrainDamage = Enhancement("Weathered",264, 334, Medium, DisTag="Terrain Resist")
SpecialRecievesAfterImage = Enhancement("Afterimage",213, 335, Baby, DisTag="Afterimage")
EyeOfJustice = Enhancement("Eye of Shining Justice",236,294, DisTag="Shining Justice")
#There are some torna effects not including them recoverable hp.
# These do not have descriptions by default I dont think I can add more descriptions iirc
EtherDamageReduce = Enhancement("Ether↓", 201, 0, [20,40,60,80],  addToList=False)
PhysicalDamageReduce = Enhancement("Physical↓", 202, 0, [20,40,60,80],  addToList=False)
EtherDamageRecievedUp = Enhancement("Ether↑", 203, 0, [20,40,60,80],  addToList=False)
PhysicalDamageRecievedUp = Enhancement("Physical↑", 204, 0, [20,40,60,80],  addToList=False)
ElementalWeaknessUp = Enhancement("Elemental Weakness↑", 205, 0, [50,100,150,200], addToList=False)
ConsumeAllyDamageUp = Enhancement("Consumer", 206, 0, [30,60,90,120], addToList=False)
RaisesBladeComboIfOrb = Enhancement("Orby", 207, 0, addToList=False)
RemoveAllAggro = Enhancement("Aggro Null", 208, 0, addToList=False) # Put on ally arts
AggroUpForDamage = Enhancement("Aggro↑", 209, 0, [50,70,90,120], addToList=False)
PermaRegen = Enhancement("Regen", 210, 0, [30,30,30,30], [1,2,3,4], addToList=False)
BladeComboTimeDown = Enhancement("Blade↓", 212, 0, [50,70,90,100], addToList=False)
PerAllyDamageUp = Enhancement("Per Ally DMG↑", 214, 0, Small, addToList=False)
EnrageAllies = Enhancement("Enrage Allies", 215, 0, Medium, addToList=False)
LoseHPOnArt = Enhancement("HpLoss", 220, 0, Baby, addToList=False)
BuffDebuffDurationUp = Enhancement("Buff Debuff Time ↑", 221, Large, addToList=False)
ArtRechargeUp = Enhancement("Recharge↑", 225, Baby, addToList=False)
HpDownDamageUp = Enhancement("Low HP Damage↑", 232, Small, addToList=False) 
PartyGaugeDrain = Enhancement("Party Drain", 237, 0, Medium, addToList=False)
ChainAttackSeal = Enhancement("Chain Seal", 260, 0, [1,1,2,3], addToList=False)
