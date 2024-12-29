import Helper, JSONParser
from IDs import *

def RandomizeReactions(OptionsRunDict):
    # Randomizes All Arts
    JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactionDistribution, InvalidTargetIDs=AutoAttacks)

    # If only randomizing the final hit, remove randomized values on all but the final hit
    if OptionsRunDict["Driver Art Reactions"]['subOptionObjects']['Final Hit Only']['subOptionTypeVal'].get():
        for artID, numHits in zip(Arts, ArtNumHits):
            for hit in range(1, numHits):
                JSONParser.ChangeJSONLine(["common/BTL_Arts_Dr.json"],[artID],['ReAct' + str(hit)],0)