import json, random
from  XCDE.XCDE_Scripts import Options, IDs
from scripts import JSONParser, Helper




# # Through this i can create entirely new maps I believe, would be an insane amount of work but interesting because the map objects keep their collision so I could theoretically make a floor by extenmding the file with a bunch of flat objects or just increase the scale of one.
# def LandmarkRando():
#     ObjectList = []
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/JsonOutputs/bdat_common/mapobjfile{area}.json", 'r+', encoding='utf-8') as lmFile:
#                 lmData = json.load(lmFile)
#                 for lm in lmData["rows"]:
#                     ObjectList.append(lm["resource"])

                        
#                 JSONParser.CloseFile(lmData, lmFile)
#         except:
#             pass
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/JsonOutputs/bdat_ma{area}/mapobjlist{area}.json", 'r+', encoding='utf-8') as lmaFile:
#                 lmaData = json.load(lmaFile)
#                 for lm in lmaData["rows"]:
#                     lm["ground"] = 1
#                     lm["scale"] = 100

                        
#                 JSONParser.CloseFile(lmaData, lmaFile)
#         except:
#             pass
#     for area in IDs.areaFileListNumbers:
#         try:
#             with open(f"./XCDE/JsonOutputs/bdat_common/mapobjfile{area}.json", 'r+', encoding='utf-8') as lmFile:
#                 lmData = json.load(lmFile)
#                 for lm in lmData["rows"]:
#                     # lm["resource"] = random.choice(ObjectList)
#                     lm["resource"] = "oj510014"

                        
#                 JSONParser.CloseFile(lmData, lmFile)
#         except:
#             pass

# def LandmarkRando():
#     with open("./XCDE/JsonOutputs/bdat_common/MNU_ColorList.json", 'r+', encoding='utf-8') as lmFile:
#         lmData = json.load(lmFile)
#         colorKeys = ["col_r", "col_g", "col_b"]
#         for lm in lmData["rows"]:
#             lm["col_r"] = 255
#             lm["col_g"] = 255
#             lm["col_b"] = 0
                
#         JSONParser.CloseFile(lmData, lmFile)
