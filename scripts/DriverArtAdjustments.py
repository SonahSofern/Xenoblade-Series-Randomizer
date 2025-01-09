import Helper, JSONParser
from IDs import *

def RandomizeReactions(OptionsRunDict):
    # Randomizes all hits of all arts
    JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactionDistribution, InvalidTargetIDs=AutoAttacks)

    # If not randomizing multiple reactions, remove all reactions from non-last hits
    if not OptionsRunDict["Driver Art Reactions"]['subOptionObjects']['Multiple Reactions']['subOptionTypeVal'].get():
        JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], Arts, RemoveReactionsFromNonLastHit)

def RemoveReactionsFromNonLastHit(art):
    last_hit = -1
    for i in range(16, 0, -1):
        if art['HitFrm' + str(i)] != 0 and last_hit == -1: # The final hit
            last_hit = i
        elif i < last_hit: # Before the final hit
            art['ReAct' + str(i)] = 0
        else: # Reactions which come after the final hit (unused, but let's keep the table clean for debugging purposes)
            art['ReAct' + str(i)] = 0
