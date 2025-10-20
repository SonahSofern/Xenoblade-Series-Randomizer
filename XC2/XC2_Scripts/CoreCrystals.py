import json
from scripts import Helper, JSONParser, PopupDescriptions
import random
from XC2.XC2_Scripts import Options, IDs


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
    CrystalIDsGroup = Helper.RandomGroup()
    CrystalIDsGroup.AddNewData(ValidCrystalListIDs)
    CrystalCount = 0
    
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            
            if cry in [45011,45012,45013]: # Turns off rare blade pulls
                cry["RareTableProb"] = 0
                cry["RareBladeRev"] = 0
                cry["AssureP"] = 0
            
            if cry["$id"] not in ValidCrystalListIDs:
                continue
            
            chosenBladeID = CrystalIDsGroup.SelectRandomMember()
            CrystalCount += 1
            cry["BladeID"] = chosenBladeID
            cry["Price"] = 20000
            cry["Condition"] = 0
            cry["ValueMax"] = 1
            cry["NoMultiple"] = CrystalCount*11 # 11 was here because it worked weirdly the nomultiple value it needed a difference of 10 or something to work
            
        JSONParser.CloseFile(cryData, cryFile)
            
def ApplyNewBladeNames():
    CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common/ITM_CrystalList.json",["$id"], ValidCrystalListIDs, "BladeID")
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

