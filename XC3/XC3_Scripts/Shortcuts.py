import json, random
from scripts import JSONParser, Helper, PopupDescriptions

def TutorialSkips(): # For some reason visually the game wont load the entire hud until aftyer the first boss in the intro but thats fine
    TutorialRemoval()
    UnlockAllSystemsTutorialsLocked()
        
def TutorialRemoval():  
    with open("XC3/JsonOutputs/prg/SYS_Tutorial.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for tut in tutData["rows"]:
            if tut["$id"] in []:
                continue
            tut["EnemyInfo"] = 0
            tut["Repeat"] = 0
            tut["<CA1A7DB1>"] = 0
        JSONParser.CloseFile(tutData, tutFile)   
        
def UnlockAllSystemsTutorialsLocked():
    with open("XC3/JsonOutputs/sys/SYS_SystemOpen.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        nonTutorialIds = [47,48,49,50,51,58,59,65,66,67,72,77,84]
        for tut in tutData["rows"]:
            if tut["$id"] in  nonTutorialIds:
                continue
            tut["Flag"] = 21022 # Flag set very early instantly unlocks everything basically probably will cause issues so testing is required
        JSONParser.CloseFile(tutData, tutFile)
    SetTipNotificationsOff()
# https://xenobladedata.github.io/xb3_200_dlc4/MNU_option_notice.html Can set a default of dont show tips cause you get a barrage of them

def SetTipNotificationsOff(): # Barrage of notifications should be off by default if you unlock the systems
    with open("XC3/JsonOutputs/mnu/MNU_option_notice.json", 'r+', encoding='utf-8') as notiFile:
        notiData = json.load(notiFile)
        for noti in notiData["rows"]:
            if noti["$id"] == 44:
                noti["default_value"] = 100
                break
        JSONParser.CloseFile(notiData, notiFile)