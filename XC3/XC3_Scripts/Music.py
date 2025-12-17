#  no_bgm
from XC3.XC3_Scripts import IDs, Options
from scripts import JSONParser, Helper, PopupDescriptions
import json, random


def Music():
    Helper.FileShuffle("XC3/JsonOutputs/prg/bgmlist.json") # Neither work
    # with open("XC3/JsonOutputs/prg/bgmlist.json", 'r+', encoding='utf-8') as bgmFile: 
    #     bgmData = json.load(bgmFile)
    #     for bgm in bgmData["rows"]:
    #         bgm["file_name"] = "no_bgm"
    #     JSONParser.CloseFile(bgmData,bgmFile)