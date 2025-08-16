import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from scripts.Helper import FileShuffle
from XC3.XC3_Scripts import Options


class ChaosOption():
    def __init__(self, name, function):
        self.name = name
        self.function = function
        ChaosSubOptions.append(self)

ChaosSubOptions:list[ChaosOption] = []

ChainAttackCam = ChaosOption("Chain Attack Camera", lambda: FileShuffle("XC3/JsonOutputs/btl/BTL_ChainAttackCam.json"))
BattleAchievements = ChaosOption("Battle Achievements", lambda: FileShuffle("XC3/JsonOutputs/btl/BTL_Achievement.json"))
Weather = ChaosOption("Weather", lambda: FileShuffle("XC3/JsonOutputs/sys/SYS_WeatherRate.json"))
EnemyVoices = ChaosOption("Enemy Voices", lambda: FileShuffle("XC3/JsonOutputs/sys/VO_BattleEN.json"))