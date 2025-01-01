import Enhancements, IDs, JSONParser

# Icons

Boots = 0
Helm = 1
Vest = 2
Necklace = 3
Belt = 4
Backpack= 5
Gloves = 6
Dice = 7
Jewelry = 8
Medal = 9


IDStart = 0
CustomAccessoriesDictList = []
NameDictList = []

class CustomAcc:
    id = 0
    Name = 0
    DebugName = ""
    ArmorType = 0
    Enhance1 = 0
    AddAtr = 0
    Price = 0
    Rarity = 0
    Flag = {
        "NoSell": 0,
        "EqPC01": 1,
        "EqPC02": 1,
        "EqPC03": 1,
        "EqPC04": 1,
        "EqPC05": 1,
        "EqPC06": 1,
        "EqPC07": 1,
        "EqPC08": 1,
        "EqPC09": 1,
        "EqPC10": 1,
        "EqPC11": 1,
        "EqPC12": 1
    }
    PArmor = 0
    EArmor = 0
    Bns_HpMax = 0
    Bns_Strength = 0
    Bns_PowEther = 0
    Bns_Dex = 0
    Bns_Agility = 0
    Bns_Luck = 0
    Enhance2 = 0
    Icon = 0
    Zone = 0
    Zone2 = 0
    IraZone = 0
    IraZone2 = 0
    sortJP = 181800
    sortGE = 126900
    sortFR = 39400
    sortSP = 27000
    sortIT = 37300
    sortGB = 27300
    sortCN = 145100
    sortTW = 68900
    Driver = 0
    Model = ""
    def __init__(self, Name, RENAMELATER, Price = 5000, Icon = Dice, PArmor = 0, EArmor = 0, HP = 0, Str = 0, Eth = 0, Dex = 0, Agi = 0, Lck = 0):
        global IDStart
        global CustomAccessoriesDictList
        IDStart += 1
        IDs.CustomAccessoriesIds.append(IDStart)
        self.Name = Name
        self.Enhance1 = RENAMELATER.id
        self.Price = Price
        self.Rarity = RENAMELATER.Rarity
        self.PArmor = PArmor
        self.EArmor = EArmor
        self.Bns_HpMax = HP
        self.Bns_Strength = Str
        self.Bns_PowEther = Eth
        self.Bns_Dex = Dex
        self.Bns_Agility = Agi
        self.Bns_Luck = Lck
        self.Icon = Icon
        self.id = IDStart

        myNameDict = {          
            "$id": self.id,
            "style": 36,
            "name": self.Name
            } 

        
        
        CustomAccessoryDict = {
        "$id": self.id,
        "Name": self.id,
        "DebugName": self.DebugName,
        "ArmorType": self.ArmorType,
        "Enhance1": self.Enhance1,
        "AddAtr": self.AddAtr,
        "Price": self.Price * (self.Rarity + 1),
        "Rarity": self.Rarity,
        "Flag": self.Flag,
        "PArmor": self.PArmor,
        "EArmor": self.EArmor,
        "Bns_HpMax": self.Bns_HpMax,
        "Bns_Strength": self.Bns_Strength,
        "Bns_PowEther": self.Bns_PowEther,
        "Bns_Dex": self.Bns_Dex,
        "Bns_Agility": self.Bns_Agility,
        "Bns_Luck": self.Bns_Luck,
        "Enhance2": self.Enhance2,
        "Icon": self.Icon,
        "Zone": self.Zone,
        "Zone2": self.Zone2,
        "IraZone": self.IraZone,
        "IraZone2": self.IraZone2,
        "sortJP": self.sortJP,
        "sortGE": self.sortGE,
        "sortFR": self.sortFR,
        "sortSP": self.sortSP,
        "sortIT": self.sortIT,
        "sortGB": self.sortGB,
        "sortCN": self.sortCN,
        "sortTW": self.sortTW,
        "Driver": self.Driver,
        "Model": self.Model
        }
        
        CustomAccessoriesDictList.append(CustomAccessoryDict)
        NameDictList.append(myNameDict)
        
        
def CreateCustomAccessories():
    Enhancements.RunCustomEnhancements(9999)
    
    while IDStart < 687:
        # MonadoHairpin = CustomAcc("Monado Hairpin", Enhancements.Vision, 5000, Jewelry)
        # PurgingAwaken = CustomAcc("Awaken Stone", Enhancements.PurgeRage, 5000, Necklace)
        # HPVest = CustomAcc("Healthy Vest", Enhancements.HPBoost, 5000, Vest)
        # StrBelt = CustomAcc("Strength Gloves", Enhancements.StrengthBoost, 5000, Belt)
        # EthGlasses = CustomAcc("Ether Glasses", Enhancements.EtherBoost, 2000,Helmet)
        # AgiShoes = CustomAcc("Agility Boots", Enhancements.AgiBoost, 1000, Boots)
        # DexGloves = CustomAcc("Dexterity Gloves", Enhancements.DexBoost, 500, Gloves)
        # Luck = CustomAcc("Lucky Choker", Enhancements.LuckBoost, 100, Medal)
        # HPFlat = CustomAcc("Healthy Vest", Enhancements.FlatHPBoost, 500, Vest)
        # StrengthFlat = CustomAcc("Strength Gloves", Enhancements.FlatStrengthBoost, 1000, Gloves)
        # FlatEth = CustomAcc("Ether Glasses", Enhancements.FlatEtherBoost, 1500, Helmet)
        # FlatDexBoost = CustomAcc("Dexterity Gloves", Enhancements.FlatDexBoost, 250, Gloves)
        # FlatAgiBoost = CustomAcc("Agility Boots", Enhancements.FlatAgiBoost, 5000, Boots)
        # FlatLuckBoost = CustomAcc("Lucky Choker", Enhancements.FlatLuckBoost, 100, Necklace)
        # TitanDamage = CustomAcc("Titan Slayers Band", Enhancements.TitanDamageUp, 100, Jewelry)
        # MachineDamage = CustomAcc("Circuit Slayers Helm", Enhancements.MachineDamageUp, 5000, Helmet)
        # HumanoidDamage = CustomAcc("Humanoid Hunters Belt", Enhancements.HumanoidDamageUp, 10000, Belt)
        # AquaticDamage = CustomAcc("Fishhook", Enhancements.AquaticDamageUp, 100, Dice)
        # AerialDamage = CustomAcc("Anti-Air Boots", Enhancements.AerialDamageUp, 400, Boots)
        # InsectDamage = CustomAcc("Newspaper", Enhancements.InsectDamageUp, 600, Dice)
        # BeastDamage = CustomAcc("Hunter's Cloak", Enhancements.BeastDamageUp, 2000, Vest)
        # TitanExecute = CustomAcc("Titan Smite", Enhancements.TitanExecute, 5000, Dice)
        # MachineExecute = CustomAcc("Shortcircuit", Enhancements.MachineExecute, 10000, Dice)
        # HumanoidExecute = CustomAcc("Hom's Bane", Enhancements.HumanoidExecute, 25000, Dice)
        # AquaticExecute = CustomAcc("Poison Bait", Enhancements.AquaticExecute, 9000, Dice)
        # AerialExecute = CustomAcc("Seeds", Enhancements.AerialExecute, 13000, Dice)
        # InsectExecute = CustomAcc("Insecticide", Enhancements.InsectExecute, 16000, Dice)
        # BeastExecute = CustomAcc("Wild Rifle", Enhancements.BeastExecute, 25000, Dice)
        # FusionDam = CustomAcc("Fusion Burst", Enhancements.FusionComboDamUp)
        # EtherCounter = CustomAcc("Tesla Coil", Enhancements.EtherCounter, 7000)
        # BladeComboDamageUp = CustomAcc("Blade Comboifyer", Enhancements.BladeComboDamUp, 10000, Medal)
        # PhysCounter = CustomAcc("Spike Vest", Enhancements.PhysCounter, 10000, Vest)
        # AutoAttackHeal = CustomAcc("Vampire Gloves", Enhancements.AutoAttackHeal, 10000, Gloves)
        # SpecialArtHeal = CustomAcc("Vampire Choker", Enhancements.SpecialANDArtHeal, 40000, Necklace)  
        # EnemyKillHeal = CustomAcc("Vulture Gloves", Enhancements.EnemyKillHeal, 200, Gloves)
        # CritHeal = CustomAcc("Modern Medal", Enhancements.CritHeal, 20000, Medal)
        # CritDamageUp = CustomAcc("Critical Headband", Enhancements.CritDamageUp, 10000, Helm)
        # DoubleAuto = CustomAcc("Reverb", Enhancements.PercentDoubleAuto, 2000, Gloves)
        # FrontDamage = CustomAcc("Clash", Enhancements.FrontDamageUp, 10000, Medal)
        # SideDamage = CustomAcc("Peripheral", Enhancements.SideDamageUp, 15000, Medal)
        # BackDamage = CustomAcc("Backstabber", Enhancements.BackDamageUp, 15000, Gloves)
        # Suprise = CustomAcc("Suprise!", Enhancements.SurpriseAttackUp, 1000, Necklace)
        # ToppleDamage = CustomAcc("Beatdown", Enhancements.ToppleDamageUp, 2000, Gloves)
        # LaunchDamage = CustomAcc("Air Combo", Enhancements.LaunchDamageUp, 6000, Medal)
        # SmashDamage = CustomAcc("Spike Gloves", Enhancements.SmashDamageUp, 1000, Gloves)
        # HigherLevelDamage = CustomAcc("Underdog", Enhancements.HigherLVEnemyDamageUp, 15000, Boots)
        AllyDownDamage = CustomAcc("Last Stand", Enhancements.AllyDownDamageUp, 1000, Medal)
        AnnulGuard= CustomAcc("Phaser", Enhancements.GuardAnnulAttack, 5000, Medal)
        
        
        Boots = 0
        Helm = 1
        Vest = 2
        Necklace = 3
        Belt = 4
        Backpack= 5
        Gloves = 6
        Dice = 7
        Jewelry = 8
        Medal = 9

    JSONParser.ReplaceJSONFile("common/ITM_PcEquip.json", CustomAccessoriesDictList)
    JSONParser.ReplaceJSONFile("common_ms/itm_pcequip.json", NameDictList)
    
    # Dont Work for now
    # 
