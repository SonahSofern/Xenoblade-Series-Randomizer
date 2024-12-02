from IDs import EnemyBattleMusicMOVs, NonBattleMusicMOVs, NonBattleMusicIDs, EnemyBattleMusicIDs
import JSONParser
import EnemyRandoLogic
import json
import random

# RSC_BgmCondition:
# An area usually has 2-3 conditions. If it has 3, its a weather related condition (music is adjusted for weather), usually can tell via large condition value
# condition of 454 is daytime
# condition of 453 is night time
# condition of 1 is debug area, only one this is tied to is gormott area theme
# priority column, value 0 is highest priority, will always play if given a choice of multiple songs. prio goes down as prio # goes up
# I don't know what causes the cave music and gormott lower music to play over other themes tbh.

def SeparateBGMandBattle(OptionsRunDict):
    if OptionsRunDict["Music"]["subOptionObjects"]["Shuffle Battle Themes and Background Music Separately"]["subOptionTypeVal"].get():
        with open("./_internal/JsonOutputs/common/RSC_BgmList.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if row["$id"] in NonBattleMusicIDs:
                    row["filename"] = random.choice([x for x in NonBattleMusicMOVs if x not in ['event/m14_loop.wav', '']])
                if row["$id"] in EnemyBattleMusicIDs:
                    row["filename"] = random.choice([x for x in EnemyBattleMusicMOVs if x not in ['']])
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2)  
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/RSC_BgmCondition.json", ["Priority"], 0)
    else:
        JSONParser.ChangeJSON(["common/RSC_BgmList.json"], ["filename"], NonBattleMusicMOVs + EnemyBattleMusicMOVs, NonBattleMusicMOVs + EnemyBattleMusicMOVs)
        EnemyRandoLogic.ColumnAdjust("./_internal/JsonOutputs/common/RSC_BgmCondition.json", ["Priority"], 0)
        pass

