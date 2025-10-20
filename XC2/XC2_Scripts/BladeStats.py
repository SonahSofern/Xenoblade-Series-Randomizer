import random
from scripts import JSONParser, Helper, PopupDescriptions
from XC2.XC2_Scripts import Options
import json

WeaponTypeRoles = [2,3,3,1,1,1,1,2,2,2,2,2,1,1,3,3,2,2,1,3,2,1,2,2,1,1,2,2,2,1,3,2,2,3,2,1]
BladeDefenseDistribution = [0,0,0,0,5,5,5,5,5,5,5,10,10,10,10,10,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,25,25,25,30,30,35,35,40,40,45,50,55]
BladeModDistribution = [5,5,5,10,10,10,10,10,15,15,15,20,20,20,25,25,25,25,25,30,30,30,30,35,35,40,40,45,45,50]
BladeAuxCoreSlotDistribution = [0,1,1,1,2,2,2,2,2,3,3]
BladeWeaponCritDistribution = [0,0,0,0,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,15,15,15,15,15,15,20,20,20,25,30,35,40,45,50,70,100]
BladeWeaponGuardDistribution = [0,0,0,0,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,15,15,15,15,15,15,20,20,20,25,30,35,40,45,50,70,100]

def BladeWeaponClassRandomization():
    PoppiNewTypeRoles = []
    NewTypeRoles = WeaponTypeRoles.copy()
    random.shuffle(NewTypeRoles)
    with open("./XC2/JsonOutputs/common/ITM_PcWpnType.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            row["Role"] = NewTypeRoles[row["$id"] - 1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_HanaRole.json", 'r+', encoding='utf-8') as file: # Poppi
        data = json.load(file)
        for row in data['rows']:
            PoppiNewTypeRoles.append(row["Role"])
        random.shuffle(PoppiNewTypeRoles)
        for row in data["rows"]:
            row["Role"] = PoppiNewTypeRoles[row["$id"] - 56001]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BladeWeaponClassDesc():
    BladeWeaponDesc = PopupDescriptions.Description()
    BladeWeaponDesc.Header(Options.BladeStatsOption_Class.name)
    BladeWeaponDesc.Text("When enabled, this option randomizes the class for a given weapon type, also changing the class for all blades that use that weapon.\n\nThis option will always make 17 ATK, 12 TNK, and 7 HLR weapons, the same as the base game.\n\n")
    BladeWeaponDesc.Text("Poppiswap Role Cores are also randomized when this option is enabled.")
    return BladeWeaponDesc