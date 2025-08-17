#  no_bgm
from XC3.XC3_Scripts import IDs, Options
from scripts import JSONParser, Helper, PopupDescriptions
import json, random


def Music():
    Helper.FileShuffle("XC3/JsonOutputs/prg/bgmlist.json") # Neither work
    # with open("XC3/JsonOutputs/prg/bgmlist.json", 'r+', encoding='utf-8') as bgmFile: # This method didnt work cant change motion and also icons (probably should just use the quest that unlocks them, swapping it to unlocking another)
    #     bgmData = json.load(bgmFile)
    #     for bgm in bgmData["rows"]:
    #         bgm["file_name"] = "no_bgm"
    #     JSONParser.CloseFile(bgmData,bgmFile)