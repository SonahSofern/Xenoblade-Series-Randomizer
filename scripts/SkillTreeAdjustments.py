import Helper, random, json

DriverSkillTreeIDs = Helper.InclRange(1,177) + Helper.InclRange(179, 270) # Excluding Zeke's Eye of Shining Justice 

ArtsCancelIDsDLC = [194, 224, 253]
ArtsCancelIDsBaseGame = [14, 43, 74, 102, 131, 165]
StartWithBIDs = [24, 33, 72, 112, 145, 174, 282, 234, 264]
StartWithXIDs = [11, 55, 61, 103, 132, 161, 191, 221, 243]
StartWithYIDs = [2, 42, 83, 94, 123, 153, 204, 213, 251]
Surviveon1IDs = [10, 39, 65, 95, 130, 160, 190, 220, 250]

OtherIDs = list(set(DriverSkillTreeIDs) - set(ArtsCancelIDsDLC) - set(ArtsCancelIDsBaseGame) - set(StartWithBIDs) - set(StartWithXIDs) - set(StartWithYIDs) - set(Surviveon1IDs))

BaseSkillTreeLists = {}

for i in range(0, 9):
    if i != 2:
        BaseSkillTreeLists[i] = [StartWithBIDs[i], StartWithXIDs[i], StartWithYIDs[i], Surviveon1IDs[i]]
    else:
        BaseSkillTreeLists[i] = [StartWithBIDs[i], StartWithXIDs[i], StartWithYIDs[i], Surviveon1IDs[i], 178] # Give back eye of shining justice to Zeke

FilePaths = ["./_internal/JsonOutputs/common/BTL_Skill_Dr_Table01.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table02.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table03.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table04.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table05.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table06.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"]

def BalancingSkillTreeRando(OptionsRunDict):
    print("Making random and balanced Driver Skill Trees")
    RandomOtherIDs = OtherIDs.copy()
    random.shuffle(RandomOtherIDs)
    for i in range(0, 9):
        CurrList = []
        if i == 2:
            for k in range(1, 25):
                RandIndex = k + k * i
                CurrList.append(RandomOtherIDs[RandIndex])
        else:
            for k in range(1, 26):
                RandIndex = k + k * i
                CurrList.append(RandomOtherIDs[RandIndex])
        CurrList += BaseSkillTreeLists[i]
        random.shuffle(CurrList)
        if i < 6:
            CurrList.insert(0, ArtsCancelIDsBaseGame[i])
        if i >= 6:
            CurrList.insert(0, ArtsCancelIDsDLC[i-6])
        if not OptionsRunDict["Early Arts Cancel"]["optionTypeVal"].get():
            # print("Shuffling in Arts Cancel")
            random.shuffle(CurrList)
        CurrFile = FilePaths[i]
        with open(CurrFile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                row["SkillID"] = CurrList[row["$id"] - 1]
                if row["$id"] == 1 and OptionsRunDict["Early Arts Cancel"]["optionTypeVal"].get():
                    print("Arts Cancel is Tier 1, and the trees are random.")
                    row["NeedSp"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def Tier1ArtsCancel(OptionsRunDict):
    if not OptionsRunDict["Balanced Skill Trees"]["optionTypeVal"].get():
        print("Putting Arts Cancel into Tier 1 (no random trees).")
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
                    try:
                        if (row["RowNum"] == ReplRow) and (row["ColumnNum"] == ReplCol) and (row["Round"] == ReplRound):
                            row["SkillID"] = OrigID
                            #break
                    except:
                        pass
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)