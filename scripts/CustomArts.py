import json
import random
from IDs import Lv1ArtCDs, Lv1DamageRatios, EnhancementSets, ValidArtIDs

def RandomArtCooldowns(): # randomizes art cooldowns
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                row["Recast1"] = random.choice(Lv1ArtCDs)
                for j in range(2, 7):
                    row[f"Recast{j}"] = row[f"Recast{j-1}"] - random.choice([0, 0, 0, 1, 1, 2])
                    if row[f"Recast{j}"] < 1:
                        row[f"Recast{j}"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtDamageRatios(): # randomizes damage ratios
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                row["DmgMgn1"] = random.choice(Lv1DamageRatios)
                for j in range(2, 7):
                    row[f"DmgMgn{j}"] = row[f"DmgMgn{j-1}"] + random.choice([20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 50, 50])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtEnhancements(): # randomizes art enhancements
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                SelectedEnhancementList = random.choice(EnhancementSets)
                for j in range(1, 7):
                    row[f"Enhance{j}"] = SelectedEnhancementList[j-1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)