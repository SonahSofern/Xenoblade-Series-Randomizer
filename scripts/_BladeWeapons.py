import json, random

def WepRando():
     with open("./_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as BladeFile:
        BlData = json.load(BladeFile)
        
        # Might have to give vandahm a custom blade with scythes instead of roc because if i want to randomize roc it will break vandahm
        MasterDriverWeapons = {
            
        }
        WeaponsValidForAll = {
            "Twin Rings": {"id": 3, "DefWeapon": 5121},
            "Greataxe": {"id": 10, "DefWeapon": 5541},
            "Megalance": {"id": 11, "DefWeapon": 5601},
            "Ether Cannon": {"id": 12, "DefWeapon": 5661},
            "Shield Hammer": {"id": 13, "DefWeapon": 5721},
            "Chroma Katana": {"id": 14, "DefWeapon": 5061},
            "Bitball": {"id": 15, "DefWeapon": 5841},
            "Knuckle Claws": {"id": 16, "DefWeapon": 5901},
            "Uchigatana": {"id": 36, "DefWeapon": 6350},
            "Knives": {"id": 34, "DefWeapon": 6050},
            "Monado": {"id": 33, "DefWeapon": 5990},
            "Dual Swords": {"id": 35, "DefWeapon": 6290}
        }
        # Some characters dont have animations for some weapons
        for Blade in BlData["rows"]:
            newWep, wepData = random.choice(list(WeaponsValidForAll.items()))
            Blade["WeaponType"] = wepData["id"]
            Blade["DefWeapon"] = wepData["DefWeapon"]
            
                    
                    
        BladeFile.seek(0)
        BladeFile.truncate()
        json.dump(BlData, BladeFile, indent=2, ensure_ascii=False)
