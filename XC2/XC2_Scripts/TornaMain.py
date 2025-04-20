from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests, TornaEnemies, TornaAreas

def AllTornaRando():
    TornaRecipes.CreateTornaRecipeList()
    TornaQuests.SelectRandomPointGoal()
    ChosenSupporterAmounts = [1,16,32,48,64] # have a few sliders going forwards to let the player change this amount
    ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests = TornaQuests.SelectCommunityQuests(ChosenSupporterAmounts)
    Areas = TornaAreas.CreateAreaInfo(Sidequests, Mainquests)
    Enemies = TornaEnemies.AdjustEnemyRequirements(Sidequests, Mainquests, Areas)