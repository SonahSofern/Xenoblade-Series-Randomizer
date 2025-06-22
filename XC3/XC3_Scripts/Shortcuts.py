import json, random
from scripts import JSONParser, Helper, PopupDescriptions


def TutorialSkips():
    Unskippable = []
    
    # with open("XC3/JsonOutputs/fld/FLD_ConditionTutorial.json", 'r+', encoding='utf-8') as tutFile:
    #     tutData = json.load(tutFile)
    #     for tut in tutData["rows"]:
    #         tut["TutorialID"] = 0
    #     JSONParser.CloseFile(tutData, tutFile)
    with open("XC3/JsonOutputs/prg/SYS_Tutorial.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for tut in tutData["rows"]:
            if tut["$id"] in Unskippable:
                continue
            tut["EnemyInfo"] = 0
            tut["Repeat"] = 0
            tut["<CA1A7DB1>"] = 0
        JSONParser.CloseFile(tutData, tutFile)
    with open("XC3/JsonOutputs/sys/SYS_SystemOpen.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for tut in tutData["rows"]:
            if tut["$id"] in  [30, 31, 32, 33, 34, 35, 36, 37, 38]:
                tut["Flag"] = 21567 # Flag for class point accummulation which seems to be instantly
        JSONParser.CloseFile(tutData, tutFile)
    # with open("XC3/JsonOutputs/prg/SYS_TutorialEnemyInfo.json", 'r+', encoding='utf-8') as tutFile:
    #     tutData = json.load(tutFile)
    #     for tut in tutData["rows"]:
    #         tut["<10FF2123>"] = 0
    #         tut["<1A391DEB>"] = 0
    #         tut["<032170A4>"] = 0
    #     JSONParser.CloseFile(tutData, tutFile)
    
    
    # def TutorialSkips():
    # Unskippable = [277]
    # # with open("XC3/JsonOutputs/fld/FLD_ConditionTutorial.json", 'r+', encoding='utf-8') as tutFile:
    # #     tutData = json.load(tutFile)
    # #     for tut in tutData["rows"]:
    # #         if tut["$id"] in Unskippable:
    # #             continue
    # #         tut["TutorialID"] = 0
    # #     JSONParser.CloseFile(tutData, tutFile)
    # # with open("XC3/JsonOutputs/fld/FLD_ConditionList.json", 'r+', encoding='utf-8') as tutFile:
    # #     # 5 
    # #     tutData = json.load(tutFile)
    # #     for tut in tutData["rows"]:
    # #         if tut["$id"] in Unskippable:
    # #             continue
    # #         tut["Condition"] = 0
    # #     JSONParser.CloseFile(tutData, tutFile)
    # with open("XC3/JsonOutputs/mnu/MNU_TipsList.json", 'r+', encoding='utf-8') as tutFile:
    #     # 5 
    #     tutData = json.load(tutFile)
    #     for tut in tutData["rows"]:
    #         if tut["Condition1"] in Unskippable:
    #             continue
    #         tut["Condition1"] = 0
    #         tut["Title"] = 0
    #         tut["BaseImageNo"] = 0
    #         for i in range(1,4):  
    #             tut[f"Comment{i}"] = 0
    #             tut[f"ImageNo{i}"] = 0
    #             tut[f"PageTitle{i}"] = 0

            
    #     JSONParser.CloseFile(tutData, tutFile)
    # # with open("XC3/JsonOutputs/prg/SYS_Tutorial.json", 'r+', encoding='utf-8') as tutFile:
    # #     tutData = json.load(tutFile)
    # #     for tut in tutData["rows"]:
    # #         tut["EnemyInfo"] = 0
    # #         tut["Repeat"] = 0
    # #         tut["<CA1A7DB1>"] = 0
    # #     JSONParser.CloseFile(tutData, tutFile)
