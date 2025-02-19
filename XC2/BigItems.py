import json
import random

def BigItemsRando():
    with open("./XC2/_internal/JsonOutputs/common_gmk/RSC_dropitemParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row["endScale"] = random.randint(1, 30)
            row["isSpin"] = random.randint(0,1)
            row["spinSpeed"] = random.randint(60, 1000)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)