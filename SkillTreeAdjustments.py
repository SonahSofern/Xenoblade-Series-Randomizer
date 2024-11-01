import JSONParser
import Helper
import random
import json

DriverSkillTreeIDs = Helper.inclRange(1,270)

ArtsCancelIDsDLC = [194, 224, 253]
ArtsCancelIDsBaseGame = [14, 43, 74, 102, 131, 165]
StartWithBIDs = [24, 33, 72, 112, 145, 174, 282, 234, 264]
StartWithXIDs = [11, 55, 61, 103, 132, 161, 191, 221, 243]
StartWithYIDs = [2, 42, 83, 94, 123, 153, 204, 213, 251]
Surviveon1IDs = [10, 39, 65, 95, 130, 160, 190, 220, 250]

OtherIDs = list(set(DriverSkillTreeIDs) - set(ArtsCancelIDsDLC) - set(ArtsCancelIDsBaseGame) - set(StartWithBIDs) - set(StartWithXIDs) - set(StartWithYIDs) - set(Surviveon1IDs))

BaseSkillTreeLists = {}

for i in range(0, 9):
    BaseSkillTreeLists[i] = [StartWithBIDs[i], StartWithXIDs[i], StartWithYIDs[i], Surviveon1IDs[i]]

FilePaths = ["./_internal/JsonOutputs/common/BTL_Skill_Dr_Table01.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table02.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table03.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table04.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table05.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table06.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"]

#def ArtsCancelBehavior():
#    JSONParser.RandomizeBetweenRange("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], Helper.inclRange(0,50000),  [0], InvalidTargetIDs=Helper.inclRange(2,30))
#    JSONParser.RandomizeBetweenRange("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["NeedSp"], DriverSkillTrees,  [14], InvalidTargetIDs=Helper.inclRange(2,30))

def BalancingSkillTreeRando(CheckboxList, CheckboxStates):
    for j in range(0, len(CheckboxList)):
        if CheckboxList[j] == "Balanced Random Skill Trees Box":
            BalancedBox = j
        if CheckboxList[j] == "Arts Cancel on Tier 1 Box":
            ArtsCancelBox = j   
    if CheckboxStates[BalancedBox].get() == True:
        RandomOtherIDs = OtherIDs.copy()
        random.shuffle(RandomOtherIDs)
        for i in range(0, 9):
            CurrList = []
            for k in range(1, 26):
                RandIndex = k + k * i
                CurrList.append(RandomOtherIDs[RandIndex])
                pass
            CurrList += BaseSkillTreeLists[i]
            random.shuffle(CurrList)
            if i < 6:
                CurrList.insert(0, ArtsCancelIDsBaseGame[i])
            if i >= 6:
                CurrList.insert(0, ArtsCancelIDsDLC[i-6])
            if CheckboxStates[ArtsCancelBox].get() == False:
                random.shuffle(CurrList)
            CurrFile = FilePaths[i]
            with open(CurrFile, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    row["SkillID"] = CurrList[row["$id"] - 1]
                    if row["$id"] == 1 and CheckboxStates[ArtsCancelBox].get() == True:
                        row["NeedSp"] = 0
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)
    if (CheckboxStates[BalancedBox].get() == False) and (CheckboxStates[ArtsCancelBox].get() == True): 
        for i in range(0, 9):
            CurrFile = FilePaths[i]
            if i < 6:
                CorrEntry = ArtsCancelIDsBaseGame[i]
            if i >= 6:
                CorrEntry = ArtsCancelIDsDLC[i-6]
            with open(CurrFile, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    if row["$id"] == 1:
                        OrigID = row["SkillID"] 
                    if row["SkillID"] == CorrEntry:
                        ReplRound = row["Round"]
                        ReplRow = row["RowNum"]
                        ReplCol = row["ColumnNum"]
                        break
                for row in data["rows"]:
                    if row["$id"] == 1:
                        row["SkillID"] = CorrEntry
                        row["NeedSp"] = 0
                    if (row["RowNum"] == ReplRow) and (row["ColumnNum"] == ReplCol) and (row["Round"] == ReplRound):
                        row["SkillID"] = OrigID
                        break
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)