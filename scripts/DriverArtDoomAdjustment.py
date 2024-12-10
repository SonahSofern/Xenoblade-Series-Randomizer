import JSONParser
from IDs import ArtDebuffs, ArtBuffs, AutoAttacks

# we need this pop out because a suboption lambda runs after an option, 
# so the suboption "Include Doom" cant have the lambda be: rangeValidReplacements.extend(21), 
# since the randomization would happen before that point, and it wouldn't re-randomize with doom now in the pool.
# If we let the suboption lambda rerandomize again, it can now target only the artdebuffs, and so the art buffs that were shuffled in
# to the pool with the first round of randomization end up not getting rerandomized, effectively increasing the pool beyond the desired
# percentage of arts that have a debuff.

def DriverArtRando(OptionsRunDict):     
    if OptionsRunDict["Driver Art Debuffs"]["subOptionObjects"]["Include Doom"]["subOptionTypeVal"].get():
        JSONParser.ChangeJSON(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, list(set(ArtDebuffs + ArtBuffs)), InvalidTargetIDs=AutoAttacks)
    else:
        JSONParser.ChangeJSON(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, [x for x in (list(set(ArtDebuffs + ArtBuffs))) if x not in [21]], InvalidTargetIDs=AutoAttacks)