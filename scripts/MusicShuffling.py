from IDs import AllMusicIDs, EnemyBattleMusicIDs, NonBattleMusicIDs
import JSONParser

def SeparateBGMandBattle(OptionsRunDict):
    if OptionsRunDict["Music"]["subOptionObjects"]["Shuffle Battle Themes and Background Music Separately"]["subOptionTypeVal"].get():
        JSONParser.ChangeJSON(["common/RSC_BgmCondition.json"], ["BgmIDA", "BgmIDB", "BgmIDC"], NonBattleMusicIDs, NonBattleMusicIDs)
        JSONParser.ChangeJSON(["common/CHR_EnArrange.json"], ["BGMID"], EnemyBattleMusicIDs, EnemyBattleMusicIDs)
    else:
        JSONParser.ChangeJSON(["common/RSC_BgmCondition.json"], ["BgmIDA", "BgmIDB", "BgmIDC"], AllMusicIDs, AllMusicIDs)
        JSONParser.ChangeJSON(["common/RSC_BgmCondition.json"], ["BGMID"], AllMusicIDs, AllMusicIDs)
    