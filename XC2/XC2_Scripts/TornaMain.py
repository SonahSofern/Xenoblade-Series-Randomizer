from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests

def AllTornaRando():
    TornaRecipes.CreateTornaRecipeList()
    TornaQuests.SelectRandomPointGoal()
    ChosenSupporterAmounts = [1,16,32,48,64]
    TornaQuests.SelectCommunityQuests(ChosenSupporterAmounts)