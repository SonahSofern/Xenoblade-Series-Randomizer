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
    Small = [1,50]
    Medium = [1,100]
    Large  = [1,300]
    Mega = [1,600]
    Giga = [1, 3000]
    
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
    EtherCounter = EnhanceEff(25,23, Giga)
    PhysCounter = EnhanceEff(26,24, Giga) # This is interesting because jins stuned swallow uses this and inflicts blowdown from this effect want to figure out how
    AutoAttackHeal = EnhanceEff(27,26, Small)
    SpecialHeal = EnhanceEff(28,27, Baby) # This also is used for driver art healing (according to the caption which might be wrong) want to figure this out too
    EnemyKillHeal = EnhanceEff(29,30, Medium)
    CritHeal = EnhanceEff(30,31, Small, 31)
    CritDamageUp = EnhanceEff(31, Large)
    PercentDoubleAuto = EnhanceEff(32, Medium)
    FrontDamageUp = EnhanceEff(33, Large)
    SideDamageUp = EnhanceEff(34, Large)
    BackDamageUp = EnhanceEff(35, Large)
    SurpriseAttackUp = EnhanceEff(36, Giga)
    ToppleDamageUp = EnhanceEff(37, Large)
    LaunchDamageUp = EnhanceEff(38, Large)
    SmashDamageUp = EnhanceEff(39, Large)
    HigherLVEnemyDamageUp = EnhanceEff(40, Large)
    AllyDownDamageUp = EnhanceEff(41, Mega)
    GuardAnnulAttack = EnhanceEff(42, Medium)
    AnnulReflect = EnhanceEff(43, Medium)
    DamageUpWhenHpDown = EnhanceEff(44, Large, Small)
    BattleDurationDamageUp = EnhanceEff(45, Large)
    DamageUpOnEnemyKill = EnhanceEff(46, Medium) # Uses weird parameter see above
    BreakDurationUp = EnhanceEff(47, Medium)
    ToppleDurationUp = EnhanceEff(48, Medium)
    LaunchDurationUp = EnhanceEff(49, Medium)
    AutoAttackDamageUp = EnhanceEff(50, Mega)
    AggroedEnemyDamageUp = EnhanceEff(51, Large)
    IndoorsDamageUp = EnhanceEff(52, Medium)
    OutdoorsDamageUp = EnhanceEff(53, Small)
    BladeSwitchDamageUp = EnhanceEff(54, Small)
    OppositeGenderBladeDamageUp = EnhanceEff(55, Medium)
    ReduceEnemyToppleResist = EnhanceEff(56, Medium) # [ML:Enhance kind=Param1 ]% put that there to make game show the change?
    ReduceEnemyLaunchResist = EnhanceEff(57, Medium)
    

def StandardEnhanceRun():
    IncreaseEffectCaps(9999)
    if len(EnhanceEffectsList) == 0:
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
        CreateEnhanceObjects()
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)
    
    
