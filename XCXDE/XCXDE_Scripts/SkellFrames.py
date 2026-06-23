from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, Helper, StatRand, PopupDescriptions

class SkellFrames:
    def __init__(self):
        self.CHR = 0
        self.DEF = 0

def RandomizeSkells():
    '''Randomizes skell frames'''
    sklDefFile = JSONParser.File("XCXDE/JsonOutputs/common/DEF_DlList.json")
    sklChrFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    wpnFile = JSONParser.File("XCXDE/JsonOutputs/common/WPN_DlList.json")
    amrFile = JSONParser.File("XCXDE/JsonOutputs/common/AMR_DlList.json")
    
    skellGroup:Helper.RandomGroup = GenSkellData(sklDefFile, sklChrFile)
    
    for defSkl in sklDefFile.rows:
        if defSkl["$id"] not in IDs.PlayerDefSkellFrameIDs: continue
        newSkell:SkellFrames = skellGroup.SelectRandomMember()
        
        # Force ares skell for testing
        if defSkl["$id"] == 51: # Starter Skell
            while newSkell.CHR["$id"] not in [251,250] :
                newSkell:SkellFrames = skellGroup.SelectRandomMember()
        
        for chrSkl in sklChrFile.rows:
            if defSkl["Frame"] != chrSkl["$id"]: continue 
            
            BalanceStats(chrSkl, newSkell)
            
            if newSkell.CHR["flag(Ares)"]:
                BalanceAresTypeGear(chrSkl, newSkell, wpnFile, amrFile)
            else: 
                ClearSkellGear(newSkell)
                
            Helper.CopyKeys(chrSkl, newSkell.CHR, ["$id", "Level", "MakerLv", "Price", "flag(Rental)"])
            Helper.CopyKeys(defSkl, newSkell.DEF, ["$id", "ID", "Insure", "Render", "Frame"])
            break
        
    sklDefFile.Close()
    sklChrFile.Close()
    wpnFile.Close()
    amrFile.Close()

def GenSkellData(sklDefFile:JSONParser.File, sklChrFile:JSONParser.File):
    '''Generate the frames data into a group'''
    skellGroup = Helper.RandomGroup()
    for skl in sklDefFile.rows:
        if skl["$id"] not in IDs.PlayerDefSkellFrameIDs: continue
        frm = SkellFrames()
        frm.DEF = skl
        for chrSkl in sklChrFile.rows:
            if skl["Frame"] != chrSkl["$id"]: continue 
            frm.CHR = chrSkl
            skellGroup.AddNewData(frm)
            break
    return skellGroup
        
def ClearSkellGear(skell:SkellFrames):
    '''Clear skell equipment as a way to balance its new level'''
    for i in range(0,5):
        skell.DEF[f"Wpn[{i}]"] = 0
        skell.DEF[f"Armor[{i}]"] = 0
        
def BalanceStats(oldSkl, newSklFrame:SkellFrames):
    '''Skell stats need to be adjusted for a balanced experience'''
    oldLv = oldSkl["Level"]
    newLv = newSklFrame.CHR["Level"]
    if oldLv == newLv: return
    
    # (level, level): [HP, Fight, Shoot, Mind, DexFight, DexShoot, Dodge, FuelMax] multipliers that intend to match what a skell of x level should be
    levelDict ={
        (50,60): [1.7, 3.0, 3.9, 3.4, 1.5, 1.7, 2.6, 2.4],
        (30,60): [2.6, 4.6, 5.5, 4.8, 1.7, 1.8, 3.8, 3.5],
        (20,60): [4.8, 6.9, 7.6, 6.5, 2.0, 2.0, 4.5, 4.2],
        (30,50): [1.6, 1.6, 1.6, 1.6, 1.6, 1.5, 1.7, 1.6],
        (20,50): [2.9, 2.6, 2.3, 2.2, 1.8, 1.8, 1.8, 1.8],
        (20,30): [1.9, 1.7, 1.6, 1.5, 1.4, 1.3, 1.3, 1.3],
    }
    stats = ["Hp", "Fight", "Shoot", "Mind", "DexFight", "DexShoot", "Dodge", "FuelMax"]
    # GetLevelMults(stats)
    
    if oldLv > newLv:
        mults = levelDict[(newLv, oldLv)]
        isMult = True
    else:    
        mults = levelDict[(oldLv, newLv)]
        isMult = False
    
    for stat, mult in zip(stats, mults):
        if isMult:
            newStat = int(newSklFrame.CHR[stat]*mult)
        else:
            newStat = int(newSklFrame.CHR[stat]/mult)
        newSklFrame.CHR[stat] = min(newStat, StatRand.b16)

def GetLevelMults(stats):
    '''Averages the difference between skell levels stats for each stat'''
    sklDefFile = JSONParser.File("XCXDE/JsonOutputs/common/DEF_DlList.json")
    sklChrFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    wpnFile = JSONParser.File("XCXDE/JsonOutputs/common/WPN_DlList.json")
    amrFile = JSONParser.File("XCXDE/JsonOutputs/common/AMR_DlList.json")


    SkellDict = {
        20: [],
        30: [],
        50: [],
        60: []
    }
    for skl in sklChrFile.rows:
        for defSkl in sklDefFile.rows:
            if defSkl["$id"] not in IDs.PlayerDefSkellFrameIDs: continue
            if defSkl["Frame"] != skl["$id"]: continue
            SkellDict[skl["Level"]].append(skl)
            break

    levelDict ={
        (50,60): [],
        (30,60): [],
        (20,60): [],
        (30,50): [],
        (20,50): [],
        (20,30): [],
    }

    levelDict2 ={
        (50,60): [],
        (30,60): [],
        (20,60): [],
        (30,50): [],
        (20,50): [],
        (20,30): [],
    }

    for lv, lv2 in levelDict.keys():
        for stat in stats:
            for skl in SkellDict[lv]:
                for skl2 in SkellDict[lv2]:
                    diff = skl2[stat]/skl[stat]
                    levelDict[(lv, lv2)].append(diff)
            avg = round(sum(levelDict[(lv, lv2)])/len(levelDict[(lv, lv2)]), 1)
            levelDict2[(lv, lv2)].append(avg)
    for lv, lv2 in levelDict2.keys():
        print(f"({lv},{lv2}): {levelDict2[(lv, lv2)]},")

def BalanceAresTypeGear(chrOldSkl, newSkell:SkellFrames, wpnFile:JSONParser.File, amrFile:JSONParser.File):
    '''Ares gear cannot be removed so it needs to be balanced for the skell it randomized into'''
    oldLv = chrOldSkl["Level"]
    newLv = newSkell.CHR["Level"]
    if oldLv == newLv: return
    
    multDict ={
        (50,60): 2,
        (30,60): 3,
        (20,60): 4,
        (30,50): 2.5,
        (20,50): 3.5,
        (20,30): 2,
    }
    
    if oldLv > newLv:
        mult = multDict[(newLv, oldLv)]
    else:    
        mult = 1/multDict[(oldLv, newLv)]
    
    # Mult the armors hp, def, price, affixes
    for i in range(0,5):
        targetArmorID = newSkell.DEF[f"Armor[{i}]"]
        for amr in amrFile.rows:
            if amr["$id"] != targetArmorID: continue
            for stat in ["Hp", "def", "Price"]:
                amr[stat] = min(int(amr[stat] * mult), StatRand.b16)
            
            # Remove the Affixes
            for j in range(0,3):
                amr[f"Affix[{j}]"] = 0
            break
    
    
    AGHASURA_IDs = [2674, 2675, 2676]
    # Mult the weapons damage, price. affixes
    for i in range(0,10):
        targetWeaponID = newSkell.DEF[f"Wpn[{i}]"]
        for wpn in wpnFile.rows:
            if wpn["$id"] != targetWeaponID: continue
            
            if wpn["$id"] in AGHASURA_IDs: # Ares AGHASURA cannon needs special nerf what the fk was monolith cooking
                wpn["Damage"] *= mult # Apply the mult an extra time
                
            for stat in ["Damage", "Price"]:
                wpn[stat] = min(int(wpn[stat] * mult), StatRand.b16)
            
            # Remove the Affixes
            for j in range(0,3):
                wpn[f"Affix[{j}]"] = 0
            break
        
def SkellFrameDesc(name):
    sklFrameDesc = PopupDescriptions.Description()
    sklFrameDesc.Header(name)
    sklFrameDesc.Text("This randomizes the skells in the game. Your starting skell could be any normally obtainable skell. Skells are balanced for their new levels.")
    return sklFrameDesc