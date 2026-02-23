NormalMonsterIDs = []
TyrantMonsterIDs = []
BossMonstersIDs = []
SuperbossMonstersIDs = []

import json
with open("XCXDE/JsonOutputs/common/CHR_EnList.json", 'r+', encoding='utf-8') as eneFile:
    eneData = json.load(eneFile)
    for en in eneData["rows"]:
        enID = en["$id"]
        if en["Flag(mBoss)"]:
            BossMonstersIDs.append(enID)
        elif en["Named"]:
            TyrantMonsterIDs.append(enID)
        else:
            NormalMonsterIDs.append(enID)

print(NormalMonsterIDs)
print(TyrantMonsterIDs)
print(BossMonstersIDs)
print(SuperbossMonstersIDs)