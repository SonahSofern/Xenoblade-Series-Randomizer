import json, random
def Driver():
    
    invalidDr = [10,11,13,14,15,16,12,17,18,19,20,21,22,23,24,25]
    sharedTags = ["Name", "Model", "Motion", "Com_Eff"]
    with open("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", 'r+', encoding='utf-8') as driverFile:
        driverData = json.load(driverFile)
        drList = []
        for dr in driverData["rows"]: # Gen our list of drivers
            if dr["$id"] in invalidDr:
                continue
            drList.append(dr)
        for dr in driverData["rows"]:
            char = random.choice(drList)
            for tag in sharedTags:
                dr[tag] = char[tag]
             
        
        driverFile.seek(0)
        driverFile.truncate()
        json.dump(driverData, driverFile, indent=2, ensure_ascii=False)