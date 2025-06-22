import json, random
from scripts import JSONParser, Helper, PopupDescriptions


def TutorialSkips():
    with open("XC3/JsonOutputs/fld/FLD_ConditionTutorial.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for tut in tutData["rows"]:
            tut["TutorialID"] = 0
        JSONParser.CloseFile(tutData, tutFile)
    # with open("XC3/JsonOutputs/prg/SYS_Tutorial.json", 'r+', encoding='utf-8') as tutFile:
    #     tutData = json.load(tutFile)
    #     for tut in tutData["rows"]:
    #         tut["EnemyInfo"] = 0
    #         tut["Repeat"] = 0
    #         tut["<CA1A7DB1>"] = 0
    #     JSONParser.CloseFile(tutData, tutFile)
    # with open("XC3/JsonOutputs/prg/SYS_TutorialEnemyInfo.json", 'r+', encoding='utf-8') as tutFile:
    #     tutData = json.load(tutFile)
    #     for tut in tutData["rows"]:
    #         tut["<10FF2123>"] = 0
    #         tut["<1A391DEB>"] = 0
    #         tut["<032170A4>"] = 0
    #     JSONParser.CloseFile(tutData, tutFile)
