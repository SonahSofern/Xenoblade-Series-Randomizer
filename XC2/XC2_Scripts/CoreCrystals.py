import json
from scripts import Helper, JSONParser, StatRand, PopupDescriptions
import random
from XC2.XC2_Scripts import IDs, CharacterRandomization, Options

def CustomCoreCrystalRando():
    if HasRanOnce(): return
    RandomizeCrystalList()
    ApplyNewBladeNames()
    FixOpeningSoftlock()
    FixRoc()
    FixArtReleaseLevels()
    RareBladeProbabilityEqualizer()
    LandofChallengeRelease()
    if Options.BladeNGPlusOption.GetState():
        AddMikhailToGacha()
        UnlockNGPlusBladesGacha()

def RareBladeProbabilityEqualizer(): # makes it so all blades are equally likely to be pulled
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Prob1", "Prob2", "Prob3", "Prob4", "Prob5"] , 1)

def LandofChallengeRelease(): #frees shulk, elma, fiora from land of challenge restriction
    Helper.SubColumnAdjust("XC2/JsonOutputs/common/CHR_Bl.json", "Flag", "OnlyChBtl", 0)

def FixArtReleaseLevels(): # Fixes issue with NG+ blades having incredibly high level requirements for arts
    with open("XC2/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            if art["ReleaseLv1"] > 10:
                for i in range(1, 6):
                    art[f"ReleaseLv{i}"] = random.choice([3,5,7,9])
        JSONParser.CloseFile(artData, artFile)

def FixRoc(): # Fixes Roc softlock as you need to pull him legit for a quest
    rocCrystalId = None
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            if cry["BladeID"] == 1008:
                cry["Condition"] = 2212
                rocCrystalId = cry["$id"]
                break
        JSONParser.CloseFile(cryData, cryFile)
    with open("XC2/JsonOutputs/common/MNU_BladeCreate.json", 'r+', encoding='utf-8') as blFile:
        blData = json.load(blFile)
        for bl in blData["rows"]:
            if bl["$id"] == 2:
                bl["limited_item"] = rocCrystalId
        JSONParser.CloseFile(blData, blFile)

def FixOpeningSoftlock(): # Game doesnt like it if we open cores before a certain point in the game iirc
    StartingCondListRow = Helper.GetMaxValue("XC2/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingCondScenarioRow = Helper.GetMaxValue("XC2/JsonOutputs/common/FLD_ConditionScenario.json", "$id") + 1
    with open("XC2/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondListRow, "Premise": 0, "ConditionType1": 1, "Condition1": StartingCondScenarioRow, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondScenarioRow, "ScenarioMin": 2001, "ScenarioMax": 10048, "NotScenarioMin": 0, "NotScenarioMax": 0})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["BladeID"] != 1008:
                row["Condition"] = StartingCondListRow
        JSONParser.CloseFile(data, file)    

def HasRanOnce():
    '''Checks if the crystals have been randomized already'''
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            if cry["$id"] == 45002 and cry["Price"] != 0:
                return True
        return False
    
def RandomizeCrystalList():
    CrystalCount = 0
    
    BladeIDsGroup = Helper.RandomGroup()
    for id in IDs.CoreCrystalBladeIDs:
        BladeIDsGroup.AddNewData(id)

    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            
            if cry["$id"] not in IDs.CustomCrystalIDs:
                continue
            
            chosenBladeID = BladeIDsGroup.SelectRandomMember()
            CrystalCount += 1
            cry["BladeID"] = chosenBladeID
            cry["Price"] = 5000
            cry["Condition"] = 0
            cry["ValueMax"] = 1
            cry["NoMultiple"] = CrystalCount*11 # 11 was here because it worked weirdly the nomultiple value it needed a difference of 10 or something to work
            
        JSONParser.CloseFile(cryData, cryFile)
    
def ApplyNewBladeNames(): # Dont love this because it loops back over everything and applies new things. Would be better to do it all the same time 
    CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common/ITM_CrystalList.json",["$id"], IDs.CustomCrystalIDs, "BladeID")
    CorrespondingBladeNameIDs = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common/CHR_Bl.json", ["$id"], CorrespondingBladeIDs, "Name")
    CorrespondingBladeNames = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common_ms/chr_bl_ms.json", ["$id"], CorrespondingBladeNameIDs, "name")

    with open("XC2/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file:     
        IDNumbers = Helper.InclRange(16, 58)
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": f"{CorrespondingBladeNames[i]}\'s Core Crystal"})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(CorrespondingBladeIDs)):
                if row["BladeID"] == CorrespondingBladeIDs[i]:
                    row["Name"] = IDNumbers[i]
                    break
        JSONParser.CloseFile(data, file)

def NewGamePlusBladeBalancing():
    ''' Make NG+ blades balanced by starting them at lower power and allowing chips to be put in their weapons'''
    
    # Edit their default weapons to be on par with lead chips (baby starting chips) and add new ones
    wpnFile = JSONParser.File("XC2/JsonOutputs/common/ITM_PcWpn.json")
    chipFile = JSONParser.File("XC2/JsonOutputs/common/ITM_PcWpnChip.json")
    
    ogWeaponTemplates = Helper.RandomGroup()
    # Fix default weapons
    for wpn in wpnFile.rows:
        if wpn["$id"] in [5971, 5972, 5973, 5974, 5975, 5976, 5977]:
            ogWeaponTemplates.AddNewData(wpn) # copy before altering the chips so the formula works down below
            wpn["Rank"] = 1
            wpn["Damage"] = random.randrange(10,20)
            wpn["CriRate"] = random.choice([5,10,15,20]) 
            wpn["Flag"]["Private"] = 0
            
    # Connect chips to new weapons
    for chip in chipFile.rows:
        for i in range(20,27): # CreateWeapons 20-27 which correspond to those NG+ blade weapons
            # find the target weapon
            newWeapon = Helper.copy.deepcopy(ogWeaponTemplates.originalGroup[i-20])
            
            newID = wpnFile.rows[-1]["$id"] + 1
            newWeapon["$id"] = newID # New ID
            newWeapon["Rank"] = chip["Rank"] # Rank, chips also have a rank attribute so just use that
            
            # rank 10 we want 50% of the max
            
            # Update Damage, Stab, Crit, Guard
            statMult = newWeapon["Rank"]/20 # Take a % of the rank 20 chip
            for stat in ["Damage", "Stability", "CriRate", "GuardRate"]:
                StatRand.ApplyMult(newWeapon, stat, statMult, min=14)
                
            # print(f"Weapon Type: {i} Rank: {newWeapon["Rank"]} Damage: {newWeapon["Damage"]}")
            
            # Add new weapon to rows
            wpnFile.rows.append(newWeapon)
            
            # Update this chip for new weapon
            chip[f"CreateWpn{i}"] = newID
    
    wpnFile.Close()
    chipFile.Close()  
        
    # Allow chip building on these blades
    blFile = JSONParser.File("XC2/JsonOutputs/common/CHR_Bl.json")
    for bl in blFile.rows:
        if bl["$id"] in IDs.NewGamePlusBladeIDs:
            bl["Flag"]["OnlyWpn"] = 1
            bl["Flag"]["NoBuildWpn"] = 0     
    blFile.Close()

def UnlockNGPlusBladesGacha():
    blFile = JSONParser.File("XC2/JsonOutputs/common/BLD_RareList.json")
    NGPlusCondition = 1789 # NG+ Blades
    CompleteSaveCondition = 3219 # Telos
    for bl in blFile.rows:
        if bl["Condition"] in [NGPlusCondition + CompleteSaveCondition]:
            bl["Condition"] = 0
    blFile.Close()

def AddMikhailToGacha():
    # Adds Mikhail to the Gacha table
    MikhailGachaRow = {
        "$id": 38,
        "Blade": CharacterRandomization.ReplacementCharacter2Original[1045],
        "Condition": 0,
    }
    for i in Helper.InclRange(1, 5):
        MikhailGachaRow["Prob" + str(i)] = 0.25  # Same as Akhos and Patroka
        MikhailGachaRow["Assure" + str(i)] = 0
    JSONParser.ExtendJSONFile("common/BLD_RareList.json", [[MikhailGachaRow]])

def CressidusTresspassRemoval():
    '''Removes tresspass, for some reason cressidus tresspass consistently crashes the game, I suspect its related to NG+ somehow'''
    blFile = JSONParser.File("XC2/JsonOutputs/common/CHR_Bl.json")
    blFile.Alter(1048, "BSkill3", 16)
    blFile.Close()

def NGPlusBladeDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.BladeNGPlusOption.name)
    desc.Text("This allows NG+ blades to be included in blade randomization, the gacha system, and as custom core crystals from item randomization")
    desc.Header(Options.BladeNGPlusOption_Balance.name)
    desc.Text("This balances NG+ blades by giving them weaker starting chips and allowing them to buy and place new chips on their weapons.")
    return desc