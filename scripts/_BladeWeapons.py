import json, random, Helper

WeaponsList = [] # Once the torna blades get their weapons fixed and allowed to be upgraded we can put them here

# Predefined Special Cases
AegisSwordData = {"id": 1, "DefWeapon": 5001}
BroadswordData =  {"id": 17, "DefWeapon": 5961}
WhipswordsData =  {"id": 7, "DefWeapon": 5361}
BigBangEdgeData =  {"id": 8, "DefWeapon": 5421}
DualScythesData ={"id": 9, "DefWeapon": 5481}
CatalystScimitarData = {"id": 2, "DefWeapon": 5061}
DrillShieldData ={"id": 4, "DefWeapon": 5181}
MechArmsData ={"id":5, "DefWeapon": 5241}
VariableSaberData = {"id":6, "DefWeapon": 5301}

class Weapon:
    def __init__(self, _ID, _SpecialReplacements = [], _InvalidReplacements= [], _onlySpecialReplacements = False):
        self.ID = _ID
        self.Replacements = [
            {"id": 3, "DefWeapon": 5121},
            {"id": 10, "DefWeapon": 5541},
            {"id": 11, "DefWeapon": 5601},
            {"id": 12, "DefWeapon": 5661},
            {"id": 13, "DefWeapon": 5721},
            {"id": 14, "DefWeapon": 5061},
            {"id": 15, "DefWeapon": 5841},
            {"id": 16, "DefWeapon": 5901},
            {"id": 36, "DefWeapon": 6350},
            {"id": 34, "DefWeapon": 6050},
            {"id": 33, "DefWeapon": 5990},
            {"id": 35, "DefWeapon": 6290}
        ]
        SpecialReplacements = _SpecialReplacements
        
        if _onlySpecialReplacements: # Clears the defaults if we only want special replacements (Tora for example)
            self.Replacements.clear()
            
        for repl in self.Replacements: # Remove invalid ones
            if repl in _InvalidReplacements:
                self.Replacements.remove(repl) 
            
        for repl in SpecialReplacements:
            self.Replacements.append(repl) # Add any special replacements
        WeaponsList.append(self) # Add to the list

AegisSword = Weapon(1, [ BroadswordData, WhipswordsData, BigBangEdgeData, DualScythesData, CatalystScimitarData])
CatScim = Weapon(2, [AegisSwordData, BroadswordData, WhipswordsData, BigBangEdgeData, DualScythesData])
TwinRings = Weapon(3)
DrillShield = Weapon(4, [ VariableSaberData, MechArmsData],[],True )
MechArms = Weapon(5, [DrillShieldData, VariableSaberData],[] ,True)
VariableSaber = Weapon(6, [DrillShieldData, MechArmsData],[], True)
Whipsword = Weapon(7)
BigBangEdge = Weapon(8)
DualScythes = Weapon(9)
Greataxe = Weapon(10)
Megalance = Weapon(11)
EtherCannon = Weapon(12)
ShieldHammer = Weapon(13)
ChromaKatana = Weapon(14)
Bitball = Weapon(15)
KnuckleClaws = Weapon(16)
Broadsword = Weapon(17, [AegisSwordData, WhipswordsData, BigBangEdgeData, DualScythesData, CatalystScimitarData], [{"id": 12, "DefWeapon": 5661}])


def WepRando():
     with open("./_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as BladeFile:
        BlData = json.load(BladeFile)
        InvalidBladeIds = [1008, 1013, 1042,1103, 1081, 1078,1079,1080, 1077] + Helper.InclRange(1082, 1101) + Helper.InclRange(1113, 1132) # Roc and all the utsuros
        
        # Might have to give vandahm a custom blade with scythes instead of roc because if i want to randomize roc it will break vandahm

        for Blade in BlData["rows"]:

            curID = Blade["$id"]
            if curID in InvalidBladeIds: # Skip the invalid blades
                continue
                    
            
            for Wep in WeaponsList:
                if Blade["WeaponType"] == Wep.ID:
                    replWep = random.choice(Wep.Replacements)
                    Blade["WeaponType"] = replWep["id"]
                    Blade["DefWeapon"] = replWep["DefWeapon"]
                    break
            
                    
                    
        BladeFile.seek(0)
        BladeFile.truncate()
        json.dump(BlData, BladeFile, indent=2, ensure_ascii=False)


def FixArtLevels():
    pass
    # Make art levels on BTL_DRArts all 0 so we start with the arts
    
def FixBladeWepModels():
    pass
    # Make ONLYWPN on chr bl false for the ones we want to change 
    
def FixSpecialWeapons():
    pass
    # Make sure blades specials use that weapon in one of their parameters because it is need to work