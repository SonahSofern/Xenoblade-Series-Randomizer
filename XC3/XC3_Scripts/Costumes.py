import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions

# def CostumeRando(): # Causing a bug sometimes not worth keeping since costumes are where you choose the outfits it makes sense to not randomize that.
#     with open("XC3/JsonOutputs/sys/RSC_PcCostumeOpen.json", 'r+', encoding='utf-8') as costumeFile:
#         costumeData = json.load(costumeFile)
#         ignoreKeys = ["Talent", "$id", "ID"]
#         ignoreIDs = [28,29,30]
#         CostumeGroup = Helper.RandomGroup()
#         CostumeGroup.GenData(costumeData["rows"])
        
#         for costume in costumeData["rows"]:
#             if costume["$id"] in ignoreKeys:
#                 continue
#             newCostume = CostumeGroup.SelectRandomMember()
#             Helper.CopyKeys(costume, newCostume, ignoreKeys)

#         JSONParser.CloseFile(costumeData, costumeFile)
        
def LearnedClassOutfits():
    '''Randomizes the addons when you equip another class, doesn't seem to affect your default class'''
    with open("XC3/JsonOutputs/btl/BTL_Talent.json", 'r+', encoding='utf-8') as talentFile:
        talentData = json.load(talentFile)
        talGroup = Helper.RandomGroup() 
        talGroup.GenData(Helper.InclRange(1, 26, [13]) + [30,31])
        
        for tal in talentData["rows"]:
            if tal["$id"] > 34:
                continue
            tal["PcTalentParts"] = talGroup.SelectRandomMember()
        
        JSONParser.CloseFile(talentData, talentFile)