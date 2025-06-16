import random
from scripts import JSONParser, Helper, PopupDescriptions
from XC2.XC2_Scripts import Options
import json

from XC2.XC2_Scripts.IDs import WeaponTypeRoles

def BladeWeaponClassRandomization():
    PoppiNewTypeRoles = []
    NewTypeRoles = WeaponTypeRoles.copy()
    random.shuffle(NewTypeRoles)
    with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpnType.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            row["Role"] = NewTypeRoles[row["$id"] - 1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/ITM_HanaRole.json", 'r+', encoding='utf-8') as file: # Poppi
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