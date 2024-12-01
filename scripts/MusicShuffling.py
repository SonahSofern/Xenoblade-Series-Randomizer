from IDs import ValidMusicFileNames, EnemyBattleMusicFileNames, BGMMusicFileNames
import JSONParser

def SeparateBGMandBattle():
    JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], EnemyBattleMusicFileNames, EnemyBattleMusicFileNames)
    JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], BGMMusicFileNames, BGMMusicFileNames)
    