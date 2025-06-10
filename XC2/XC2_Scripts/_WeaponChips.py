import json, random
from Enhancements import *
import Options
from scripts import PopupDescriptions

def RandomizeWeaponEnhancements():
    InvalidSkillEnhancements = [ArtCancel,EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, BladeSwapDamage,CatScimPowerUp, EvadeDrainHp, EvadeDriverArt, EtherCannonRange,ArtDamageHeal, DreamOfTheFuture]
    ValidWeaponNames = ["Rings", "Ball", "Cannon", "Sword", "Slayer", "Edge", "Brand", "Scimitar", "Cleaver", "Shield", "Destroyer", "Plate", "Pavise", "Gauntlets", "Arms", "Saber", "Slicer", "Whips", "Claw", "Scythes", "Sickles", "Gutters", "Hatchet", "Axe", "Greataxe", "Lance", "Mecha-Spear", "Hammer", "Smasher", "Tachi", "Katana", "Knuckles", "Fists", "Nodachi", "Crosier", "Gunknives"]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    InvalidNames = ["Monado", "Well-Used Blades", "Archetype Ralzes", "Halteclere", "Masamune"]
    with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file:
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_pcwpn_ms.json", 'r+', encoding='utf-8') as wepNames:
            
            slider = Options.BladeWeaponChipsOption.GetSpinbox()
            enhanceFile = json.load(file)
            skillNameFile = json.load(wepNames)
            for Wep in enhanceFile["rows"]:
                
                if slider < random.randrange(0,100):
                    continue
                
                skillNameID = Wep["Name"]
                enhancement = random.choice(ValidSkills)
                while enhancement.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                    enhancement = random.choice(ValidSkills)
                enhancement.RollEnhancement()
                for skillName in skillNameFile["rows"]:  
                    if skillName["$id"] == skillNameID:
                        if skillName["name"] in InvalidNames:
                            continue      
                        oldName = skillName["name"]
                        oldName = skillName["name"]
                        oldNameList = oldName.split()
                        
                        lastWord = oldNameList[-1]
                        for item in oldNameList:
                            if item in ValidWeaponNames:
                                lastWord = item    

                        skillName["name"] = f"{enhancement.name} {lastWord}"
                        break
                    
                Wep["Enhance1"] = enhancement.id
            
                
            wepNames.seek(0)
            wepNames.truncate()
            json.dump(skillNameFile, wepNames, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(enhanceFile, file, indent=2, ensure_ascii=False)

#range should be between 0 and 1300
def RandomizePowerLevels(): # this makes the weapon chips uniform in their power level based on the rank they are
    if not Options.UMHuntOption.GetState():
        WeaponStrengthList = Helper.ExtendListtoLength([], 20, "[]")
        WeaponDamageRanges = Helper.ExtendListtoLength([[26, 75]], 20, "[inputlist[i-1][0] + 55, inputlist[i-1][1] + 55]")
        WeaponRankPool = []
        for rank in range(1, 21):
            WeaponRankPool.extend([rank, rank, rank])
        random.shuffle(WeaponRankPool)
        with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
            data = json.load(file)
            for row in data["rows"]:
                if Helper.OddsCheck(Options.BladeWeaponChipsOption.GetSpinbox()):
                    row["Rank"] = WeaponRankPool[row["$id"]-10001]
                    for i in range(1, 37):
                        WeaponStrengthList[row["Rank"] - 1].append(row[f"CreateWpn{i}"])
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file: # Sets damage of weapon based on rank of chip, with a little extra wiggle room
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(WeaponStrengthList)):
                if row["$id"] in WeaponStrengthList[i]:
                    row["Damage"] = random.randrange(int(WeaponDamageRanges[i][0]*0.75), int(WeaponDamageRanges[i][1]*1.25))
                    row["Rank"] = i + 1 #this is an unused value in the code afaik, but keeping this identical as the rank of the chip itself, in case the code checks this.
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ChangeWeaponRankNames():
    if not Options.UMHuntOption.GetState():
        if Options.BladeWeaponChipsOption_AutoAtk.GetState() and Options.BladeWeaponChipsOption.GetState():
            RandomizePowerLevels()
        WeaponStrengthNameList = Helper.ExtendListtoLength([], 20, "[]")
        with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
            data = json.load(file)
            for row in data["rows"]:
                WeaponStrengthNameList[row["Rank"] - 1].append(row["Name"])
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_pcwpnchip_ms.json", 'r+', encoding='utf-8') as file: # Renames chips according to their rank
            data = json.load(file)
            for row in data["rows"]:
                for rank in range(len(WeaponStrengthNameList)):
                    if row["$id"] in WeaponStrengthNameList[rank]:
                        row["name"] = f"{row["name"]} [System:Color name=red]({rank + 1})[/System:Color]"
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)



def WeaponChipDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.WeaponChipShopOption.name)
    desc.Text("Randomizes all chips in each weapon chip shop.\nTheir price is tied to the chip not the shop.")
    desc.Image("WeaponChipRando.png", "XC2", 800)
    desc.Text("This often makes the game very easy as weapon chips are one of the most important things in damage calculations.")
    return desc