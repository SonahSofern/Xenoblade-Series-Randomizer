from IDs import EnemyBattleMusicMOVs, NonBattleMusicMOVs, NonBattleMusicIDs, EnemyBattleMusicIDs, ReplacementNonBattleMusicMOVs, ReplacementEnemyBattleMusicMOVs
import JSONParser
import Helper
import json
import random

# RSC_BgmCondition:
# An area usually has 2-3 conditions. If it has 3, its a weather related condition (music is adjusted for weather), usually can tell via large condition value
# condition of 454 is daytime
# condition of 453 is night time
# condition of 1 is debug area, only one this is tied to is gormott area theme
# priority column, value 0 is highest priority, will always play if given a choice of multiple songs. prio goes down as prio # goes up
# I don't know what causes the cave music and gormott lower music to play over other themes tbh.
# Torna fight themes overlap with base game file names ("m0x.wav"->"m2x.wav"), so you can't use them as enemy battle themes in the base game because those point to other themes used in cutscenes in the game.

def MusicShuffle(OptionsRunDict):
    if OptionsRunDict["Music"]["subOptionObjects"]["Seperate Battle and \nEnvironment Themes"]["subOptionTypeVal"].get():
        with open("./_internal/JsonOutputs/common/RSC_BgmList.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if row["$id"] in EnemyBattleMusicIDs:
                    row["filename"] = random.choice(ReplacementEnemyBattleMusicMOVs)
                    continue
                if row["$id"] in NonBattleMusicIDs:
                    row["filename"] = random.choice(ReplacementNonBattleMusicMOVs)
                    continue
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)  
    else:
        JSONParser.ChangeJSONFile(["common/RSC_BgmList.json"], ["filename"], NonBattleMusicMOVs + EnemyBattleMusicMOVs, NonBattleMusicMOVs + EnemyBattleMusicMOVs)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/EVT_listBf.json", ["edBgm"], 0)

