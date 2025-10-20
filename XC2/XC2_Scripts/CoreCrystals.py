import json
from scripts import Helper, JSONParser, PopupDescriptions
import random
from XC2.XC2_Scripts import Options, IDs
from XC2.XC2_Scripts.Race_Mode import RaceMode

# BladeIDs = [1008, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1050, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1104, 1108, 1109, 1105, 1106, 1107, 1111]

ValidCrystalListIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]

def RareBladeProbabilityEqualizer(): # makes it so all blades are equally likely to be pulled
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Condition", "Assure1", "Assure2", "Assure3", "Assure4", "Assure5"] , 0)
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
        cryData = json.load(blFile)
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

def FixOpeningSoftlock():
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



def RandomizeCrystalList():
    Crystals = Helper.RandomGroup()
    Crystals.AddNewData(ValidCrystalListIDs)
    CrystalCount = 0
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            if cry["$id"] not in ValidCrystalListIDs:
                continue
            CrystalCount += 1
            cry["BladeID"] = Crystals.SelectRandomMember()
            cry["Price"] = 20000
            cry["Condition"] = 0
            cry["ValueMax"] = 1
            cry["NoMultiple"] = CrystalCount*11
            # Choose a blade
            # Remove from list
            
    

def AdjustingCrystalList():
    Helper.ColumnAdjust("XC2/JsonOutputs/common/ITM_CrystalList.json", ["Condition", "BladeID", "CommonID", "CommonWPN", "CommonAtr"], 0)
    ITMCrystalFile = 
    with open(ITMCrystalFile, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for k in range(0, len(ValidCrystalListIDs)):
            for row in data["rows"]:
                if row["$id"] == ValidCrystalListIDs[k]:
                    row["BladeID"] = RandomBlades[k]
                    row["Condition"] = 0
                    row["ValueMax"] = 1
                    row["NoMultiple"] = k + 11
                    break
        for row in data["rows"]:
            for i in range(45011,45014):
                if row["$id"] == i:
                    row["RareTableProb"] = 0
                    row["RareBladeRev"] = 0
                    row["AssureP"] = 0
        JSONParser.CloseFile(data, file)

def FindtheBladeNames():
    if Options.TreasureChestOption_RareBlades.GetState():
        ValidCrystalListIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
        CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("./XC2/JsonOutputs/common/ITM_CrystalList.json",["$id"], ValidCrystalListIDs, "BladeID")
        CorrespondingBladeNameIDs = Helper.AdjustedFindBadValuesList("./XC2/JsonOutputs/common/CHR_Bl.json", ["$id"], CorrespondingBladeIDs, "Name")
        CorrespondingBladeNames = Helper.AdjustedFindBadValuesList("./XC2/JsonOutputs/common_ms/chr_bl_ms.json", ["$id"], CorrespondingBladeNameIDs, "name")
        # DebugLog.DebugCoreCrystalAddition(ValidCrystalListIDs, CorrespondingBladeNames)
        ITMCrystalAdditions(CorrespondingBladeNames, CorrespondingBladeIDs)

def ITMCrystalAdditions(BladeNames, CorrespondingBladeIDs):
    with open("./XC2/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file:     
        IDNumbers = Helper.InclRange(16, 58)
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": f"{BladeNames[i]}\'s Core Crystal"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(CorrespondingBladeIDs)):
                if row["BladeID"] == CorrespondingBladeIDs[i]:
                    row["Name"] = IDNumbers[i]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

