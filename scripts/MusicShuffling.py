from IDs import ValidMusicFileNames, EnemyBattleMusicFileNames, BGMMusicFileNames
import JSONParser

def SeparateBGMandBattle(OptionsRunDict):
    if OptionsRunDict["Music"]["subOptionObjects"]["Shuffle Battle Themes and Background Music Separately"]["subOptionTypeVal"].get():
        JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], EnemyBattleMusicFileNames, EnemyBattleMusicFileNames)
        JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], BGMMusicFileNames, BGMMusicFileNames)
    else:
        JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], ValidMusicFileNames, ValidMusicFileNames)
    