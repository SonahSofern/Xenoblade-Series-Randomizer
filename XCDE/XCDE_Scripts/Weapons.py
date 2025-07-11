import json, random
from  XCDE.XCDE_Scripts import Options
from scripts import JSONParser, Helper, PopupDescriptions


def WeaponRando():
    with open("./XCDE/JsonOutputs/bdat_common/ITM_wpnlist.json", 'r+', encoding='utf-8') as wpnFile:
        
        isAppearance = Options.WeaponOption_Appearance.GetState()
        # isDam = Options.WeaponOption_Damage.GetState()
        # isDef = Options.WeaponOption_Defense.GetState()
        # isCrit = Options.WeaponOption_Crit.GetState()
        isGems = Options.WeaponOption_Gems.GetState()
        
        VanillaGuardRates = [0, 0, 0, 0, 15, 0, 0, 5, 0, 5, 0, 10, 10, 10, 10, 10, 10, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 3, 7, 0, 0, 5, 6, 8, 12, 15, 0, 0, 5, 18, 20, 13, 0, 0, 17, 20, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 9, 0, 0, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 14, 0, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 7, 0, 0, 0, 5, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 25, 5, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 4, 0, 8, 6, 5, 0, 0, 0, 10, 12, 0, 11, 14, 15, 13, 20, 0, 0, 7, 9, 9, 0, 11, 18, 14, 18, 0, 0, 12, 15, 15, 20, 10, 0, 0, 0, 15, 22, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 6, 0, 8, 9, 0, 0, 0, 10, 0, 0, 13, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 10, 6, 0, 0, 0, 0, 0, 0, 7, 0, 5, 0, 0, 0, 12, 0, 0, 0, 8, 0, 13, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 7, 0, 11, 0, 5, 0, 0, 13, 0, 15, 13, 15, 0, 9, 10, 12, 12, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 9, 5, 8, 0, 15, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 6, 0, 0, 0, 6, 0, 0, 8, 0, 8, 0, 0, 10, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 7, 0, 0, 9, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 7, 0, 12, 0, 15, 0, 0, 5, 0, 6, 0, 0, 0, 14, 15, 6, 9, 11, 5, 5, 0, 0, 0, 0, 0, 3, 6, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 7, 8, 8, 10, 0, 5, 10, 3, 0, 10, 0, 15, 5, 0, 12, 0, 17, 12, 5, 6]
        VanillaCritRates = [10, 5, 0, 10, 75, 1, 1, 10, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 8, 3, 3, 3, 3, 3, 3, 3, 3, 2, 4, 2, 2, 2, 2, 2, 2, 10, 10, 0, 0, 18, 4, 4, 4, 4, 4, 4, 0, 0, 30, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 5, 15, 5, 5, 5, 5, 5, 20, 5, 50, 10, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 5, 0, 0, 6, 5, 0, 0, 0, 0, 0, 14, 12, 0, 0, 0, 0, 16, 18, 0, 5, 0, 15, 0, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 0, 9, 8, 0, 14, 12, 0, 2, 0, 0, 5, 0, 10, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 9, 6, 0, 10, 0, 0, 5, 0, 10, 4, 4, 4, 4, 4, 4, 0, 2, 4, 0, 0, 8, 0, 9, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 12, 0, 5, 20, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 15, 25, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 0, 4, 0, 0, 0, 12, 13, 9, 0, 0, 7, 0, 0, 0, 0, 0, 5, 8, 0, 0, 0, 10, 0, 0, 0, 14, 15, 10, 0, 18, 10, 5, 0, 11, 0, 16, 10, 0, 15, 10, 10, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 0, 3, 10, 4, 7, 13, 5, 7, 0, 5, 0, 0, 12, 9, 15, 0, 11, 16, 0, 0, 0, 0, 18, 15, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 0, 4, 14, 7, 4, 16, 6, 10, 15, 10, 0, 5, 0, 3, 0, 12, 0, 8, 18, 20, 0, 6, 18, 8, 16, 15, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 6, 0, 7, 0, 3, 5, 0, 10, 20, 0, 0, 10, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 7, 8, 0, 10, 0, 0, 0, 15, 18, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 8, 5, 0, 10, 0, 5, 10, 6, 0, 10, 8, 0, 8, 0, 12, 10, 15, 10, 0, 0, 0, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 5, 10, 0, 8, 0, 0, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 6, 0, 8, 6, 0, 10, 0, 10, 0, 5, 0, 3, 8, 5, 0, 0, 20, 9, 10, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 0, 0, 9, 12, 6, 0, 0, 15, 10, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 6, 7, 0, 4, 7, 0, 10, 20, 10, 12, 0, 18, 0, 22, 9, 0, 14, 0, 16, 4, 3]

        styles = {
            1 : ['wp1101', 'wp1401', 'wp1201', 'wp1105', 'wp1301', 'wp1302', 'wp1303', 'wp1312', 'wp1311', 'wp1313', 'wp1601', 'wp1602'], # Removed , 'wp1501' junk sword because it doesnt have all of shulks animations/particles effects so feels bad to get this on monado
            2: ['wp2101', 'wp2102', 'wp2103', 'wp2105', 'wp2107', 'wp2109', 'wp2112', 'wp2113', 'wp2111', 'wp2119', 'wp2118', 'wp2116', 'wp2104', 'wp2117', 'wp2108', 'wp2114', 'wp2115', 'wp2106'],
            3: ['wp3101', 'wp3111'],
            4: ['wp4101', 'wp4111', 'wp4106', 'wp4301', 'wp4113', 'wp4108', 'wp4102', 'wp4112', 'wp4211', 'wp4114', 'wp4118', 'wp4201', 'wp4104', 'wp4107', 'wp4116', 'wp4103', 'wp4117'],
            5: ['wp5101', 'wp5111', 'wp5212', 'wp5201', 'wp5106', 'wp5102', 'wp5203', 'wp5105', 'wp5213', 'wp5116', 'wp5115', 'wp5104', 'wp5112', 'wp5114', 'wp5202', 'wp5211'],
            6: ['wp6101', 'wp6118', 'wp6103', 'wp6104', 'wp6111', 'wp6106', 'wp6117', 'wp6114', 'wp6115', 'wp6108', 'wp6113', 'wp6107', 'wp6102', 'wp6110', 'wp6105', 'wp6116', 'wp6112', 'wp6109'],
            7: ['wp7101', 'wp7108', 'wp7102', 'wp7111', 'wp7113', 'wp7104', 'wp7106', 'wp7107', 'wp7117', 'wp7112', 'wp7115', 'wp7103', 'wp7105', 'wp7114', 'wp7118', 'wp7116', 'wp7120'],
            8: ['wp8101', 'wp8201', 'wp8401', 'wp8211', 'wp8111', 'wp8106', 'wp8104', 'wp8105', 'wp8115', 'wp8301', 'wp8116', 'wp8114', 'wp8311'],
            # 9: ['wp9101'],
            # 10: ['wp0101'],
            14: ['wp6201', 'wp6211', 'wp6221'],
            15: ['wp6202', 'wp6212', 'wp6222'],
            # 16: ['wp6203']
            }

        wpnData = json.load(wpnFile)
        for wep in wpnData["rows"]:
            
            if isAppearance:
                Appearance(wep, styles)
                
            # if isDam:
            #     Damage(wep)
                
            # if isDef:
            #     Defenses(wep, VanillaGuardRates)
                
            # if isCrit:
            #     Crit(wep, VanillaCritRates)
                
            if isGems:
                Gems(wep)


        JSONParser.CloseFile(wpnData, wpnFile)

def Appearance(wep, styles):    
    for i in range(1,17):
        if i in [9,10,11,12,13,16]: # These arent values in the
            continue
        if wep[f"equip_pc{i}"] == 1: # Checks if the current weapon can be equipped and chooses a random cosmetic for that character (loading other characters weapons crashes)
            wep["resource"] = random.choice(styles[i])
            break

def Damage(wep):
    mult = random.choice([0.5,0.7,1.2,1.5])
    wep["dmg_low"] = int(wep["dmg_low"]*mult)
    wep["dmg_hi"] = int(wep["dmg_hi"]*mult)

def Defenses(wep, VanGuard:list):
    
    # Guard Rate
    grd = random.choice(VanGuard)
    VanGuard.remove(grd)
    wep["grd_rate"] = grd
    
    rates = [0.5,0.7,0.9,1.1,1.3,1.5]
    
    # Phy Def
    wep["arm_phy"] = min(int(wep["arm_phy"] * random.choice(rates)),255)
    
    # Ether Def
    wep["arm_eth"] = min(int(wep["arm_eth"] * random.choice(rates)), 255)

def Crit(wep, VanCrit:list):
    choice = random.choice(VanCrit)
    VanCrit.remove(choice)
    wep["att_lev"] = choice

def Gems(wep):
    if wep["uni_flag"]: # Dont want to modify unique weapons to keep vanilla feel. Plus redoing the gems requires knowledge of the weapons power level im surte i could make a formula but idk if i want to
        return
    
    wep["jwl_slot"] = random.choice([0,1,2,3])

def WepDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.WeaponOption_Appearance.name)
    myDesc.Text("This randomizes the appearance of weapons. It will only randomize among your characters normally obtainable cosmetics.\nFor example, Dunban will always have Dunban weapons.")
    myDesc.Header(Options.WeaponOption_Gems.name)
    myDesc.Text(f"This randomizes the gem slots in your weapons between 0 and 3 slots, this wont affect unique weapons.")
    return myDesc