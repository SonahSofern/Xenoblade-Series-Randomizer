import Enhancements

# Icons
Jewelry = 8


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
    Icon = 6
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
    def __init__(self, Name, Enhance1, Price, Rarity, Icon, PArmor = 0, EArmor = 0, HP = 0, Str = 0, Eth = 0, Dex = 0, Agi = 0, Lck = 0):
        self.Name = Name
        self.Enhance1 = Enhance1
        self.Price = Price
        self.Rarity = Rarity
        self.PArmor = PArmor
        self.EArmor = EArmor
        self.Bns_HpMax = HP
        self.Bns_Strength = Str
        self.Bns_PowEther = Eth
        self.Bns_Dex = Dex
        self.Bns_Agility = Agi
        self.Bns_Luck = Lck
        self.Icon = Icon
    
def CreateCustomAccessories():
    MonadoHairpin = CustomAcc("Monado Hairpin", Enhancements.Vision.id, 5000, Enhancements.Vision.Rarity, Jewelry)