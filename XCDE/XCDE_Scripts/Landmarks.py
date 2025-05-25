import json, random, Options, IDs
from scripts import JSONParser, Helper

def LandmarkRando():
    ObjectList = []
    dontReplace = Helper.InclRange(655,680) + [650,651]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/KP_list.json", 'r+', encoding='utf-8') as lmFile:
        lmData = json.load(lmFile)
        for lm in lmData["rows"]:
            ObjectList.append([lm["model"], lm["motion"], lm["action"], lm["effect"], lm["sound"]])

        for lm in lmData["rows"]:
            if lm["$id"] in dontReplace or lm["model"].startswith("en"):
                continue
                
            choice = random.choice(ObjectList)
            lm["model"] = choice[0]
            lm["motion"] = choice[1]
            lm["action"] = choice[2]
            lm["effect"] = choice[3]
            lm["sound"] = choice[4]   
            # lm["model"] = 	"np020201"				
            # lm["motion"] = "mn020101"
            # lm["action"] = "mn020208"
            # lm["effect"] = ""
            # lm["sound"] = "sn302701"               
        JSONParser.CloseFile(lmData, lmFile)


# # Through this i can create entirely new maps I believe, would be an insane amount of work but interesting because the map objects keep their collision so I could theoretically make a floor by extenmding the file with a bunch of flat objects or just increase the scale of one.
# def LandmarkRando():
#     ObjectList = []
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/_internal/JsonOutputs/bdat_common/mapobjfile{area}.json", 'r+', encoding='utf-8') as lmFile:
#                 lmData = json.load(lmFile)
#                 for lm in lmData["rows"]:
#                     ObjectList.append(lm["resource"])

                        
#                 JSONParser.CloseFile(lmData, lmFile)
#         except:
#             pass
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{area}/mapobjlist{area}.json", 'r+', encoding='utf-8') as lmaFile:
#                 lmaData = json.load(lmaFile)
#                 for lm in lmaData["rows"]:
#                     lm["ground"] = 1
#                     lm["scale"] = 100

                        
#                 JSONParser.CloseFile(lmaData, lmaFile)
#         except:
#             pass
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/_internal/JsonOutputs/bdat_common/mapobjfile{area}.json", 'r+', encoding='utf-8') as lmFile:
#                 lmData = json.load(lmFile)
#                 for lm in lmData["rows"]:
#                     # lm["resource"] = random.choice(ObjectList)
#                     lm["resource"] = "oj510014"

                        
#                 JSONParser.CloseFile(lmData, lmFile)
#         except:
#             pass

# def LandmarkRando():
#     with open("./XCDE/_internal/JsonOutputs/bdat_common/MNU_ColorList.json", 'r+', encoding='utf-8') as lmFile:
#         lmData = json.load(lmFile)
#         colorKeys = ["col_r", "col_g", "col_b"]
#         for lm in lmData["rows"]:
#             lm["col_r"] = 255
#             lm["col_g"] = 255
#             lm["col_b"] = 0
                
#         JSONParser.CloseFile(lmData, lmFile)
