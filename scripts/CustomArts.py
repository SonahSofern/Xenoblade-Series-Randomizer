import json
import random
from IDs import Lv1ArtCDs, Lv1DamageRatios, EnhancementSets, ValidArtIDs, EvasionEnhancementIDs, SpecialEffectArtIDs, ArtDebuffs, AutoAttacks, ArtBuffs, HitReactions, HitReactionDistribution, OriginalAOECaptionIDs
import JSONParser
import Helper
import IDs

# def DriverArtRando(OptionsRunDict): # We want custom descriptions for the driver arts, so we need to check the status of all options that affect it before randomizing. The last option that messes with the descriptions should also make the custom descriptions as well.
#     ArtsRandoDone = IDs.ArtRandoCompleteness
#     if ArtsRandoDone == 0:
#         DebuffRando = OptionsRunDict["Driver Art Debuffs"]["optionTypeVal"].get()
#         ReactionRando = OptionsRunDict["Driver Art Reaction"]["optionTypeVal"].get()
#         CooldownRando = OptionsRunDict["Driver Art Cooldowns"]["optionTypeVal"].get()
#         DamageRatioRando = OptionsRunDict["Driver Art Damage Ratio"]["optionTypeVal"].get()
#         EnhancementRando = OptionsRunDict["Driver Art Enhancements"]["optionTypeVal"].get()

#         DebuffSliderOdds = OptionsRunDict["Driver Art Debuffs"]["spinBoxVal"].get()
#         ReactionSliderOdds = OptionsRunDict["Driver Art Reaction"]["spinBoxVal"].get()

#         ReplaceWithDebuffs = OptionsRunDict["Driver Art Debuffs"]["subOptionObjects"]["Debuffs"]["subOptionTypeVal"].get()
#         ReplaceWithBuffs = OptionsRunDict["Driver Art Debuffs"]["subOptionObjects"]["Buffs"]["subOptionTypeVal"].get()
#         ReplaceWithDoom = OptionsRunDict["Driver Art Debuffs"]["subOptionObjects"]["Doom"]["subOptionTypeVal"].get()
#         ClearVanillaReactions = OptionsRunDict["Driver Art Reaction"]["subOptionObjects"]["Clear Vanilla Reactions"]["subOptionTypeVal"].get()
#         MultipleReactions = OptionsRunDict["Driver Art Reaction"]["subOptionObjects"]["Multiple Reactions"]["subOptionTypeVal"].get()

#         if DebuffRando:
#             ValidDebuffReplacements = []
#             if ReplaceWithDebuffs:
#                 ValidDebuffReplacements.extend(list(set(ArtDebuffs)-set([21,35])))
#             if ReplaceWithBuffs:
#                 ValidDebuffReplacements.extend(ArtBuffs)
#             if ReplaceWithDoom:
#                 ValidDebuffReplacements.extend([21])
#             ValidDebuffReplacements = list(set(ValidDebuffReplacements))
#             ChangeJSONFileArtsRando(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, ValidDebuffReplacements, AutoAttacks, DebuffSliderOdds)
#         if ReactionRando:
#             if ClearVanillaReactions:
#                 Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", Helper.StartsWith("ReAct", 1,16), 0)    
#             ChangeJSONFileArtsRando(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactionDistribution, AutoAttacks, ReactionSliderOdds)
#             if not MultipleReactions:
#                 JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], ValidArtIDs, RemoveReactionsFromNonLastHit)
#         if CooldownRando:
#             RandomArtCooldowns()
#         if DamageRatioRando:
#             RandomArtDamageRatios()
#         if EnhancementRando:
#             RandomArtEnhancements()
#         CustomArtDescriptionGenerator()
#         IDs.ArtRandoCompleteness = 1

def RandomArtReactions():
    pass

def RandomArtDebuffs():
    pass

def RandomArtCooldowns(): # randomizes art cooldowns
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                row["Recast1"] = random.choice(Lv1ArtCDs)
                for j in range(2, 7):
                    row[f"Recast{j}"] = row[f"Recast{j-1}"] - random.choice([0, 0, 0, 1, 1, 2])
                    if row[f"Recast{j}"] < 1:
                        row[f"Recast{j}"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtDamageRatios(): # randomizes damage ratios
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                row["DmgMgn1"] = random.choice(Lv1DamageRatios)
                for j in range(2, 7):
                    row[f"DmgMgn{j}"] = row[f"DmgMgn{j-1}"] + random.choice([20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 50, 50])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtEnhancements(): # randomizes art enhancements
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                if row["$id"] not in SpecialEffectArtIDs:
                    row["ArtsBuff"] = 0
                SelectedEnhancementList = random.choice(EnhancementSets)
                for j in range(1, 7):
                    row[f"Enhance{j}"] = SelectedEnhancementList[j-1]
                if row["Enhance1"] in EvasionEnhancementIDs: # Evasion Art Enhancement
                    row["ArtsBuff"] = 2
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)


def GenCustomArtDescriptions():
    RangeType = {
        "AOE" : [3,5]
    }

    Reactions = {
        "B" : [1],
        "T" : [2],
        "L" : [3],
        "S" : [4],
        "Kb": [5,6,7,8,9],
        "Bd": [10,11,12,13,14]
    }

    Enhancements = {
        "Aggro↓" : [2830,2835],
        "Aggro↑" : [2850,2873],
        "Aggroed↑": [2795],
        "Aquatic↑": [2705],
        "Back↑": [2760,2755],
        "Cancel↑": [2810],
        "Crit↑": [2975],
        "Crit CD↓": [2840],
        "Evade": [2866,2872],
        "Flying↑": [2700],
        "Front↑": [2740],
        "Vamp": [2735,2878],
        "Party Vamp": [2845],
        "High HP↑": [2800,2805],
        "Evade": [2825],
        "HP Potion": [2815,2860],
        "Insect↑": [2685],
        "Launch↑": [2780,2775],
        "LowHP↑": [2790,2785],
        "Machine↑": [2730,2725],
        "Pierce": [2861],
        "Side↑": [2746,2745,2750],
        "Topple↑": [2770,2765],
        "Beast↑": [2680],
        "Humanoid↑": [2715]
    }

    Debuffs = {
        "Foe Crit↑": [1],
        "Foe Acc↑": [2],
        "Foe Art↑": [3],
        "Foe CD↓": [4],
        "Foe Shield": [5],
        "Foe Null React": [6],
        "Foe -Debuff": [7],
        "Foe Back↑": [8],
        "Foe Armor": [16],
        "Foe Atk↑": [17],
        "Taunt": [11],
        "Stench": [12],
        "Shackle Dr": [13],
        "Shackle Bl": [14],
        "Null Heal": [15],
        "Doom": [21],
        "P Def↓": [23],
        "E Def↓": [24],
        "Res↓": [25],
        "Stop": [30],
        "Enrage": [35]
    }
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", "r+", encoding='utf-8') as ArtsFile:     
        with open("./_internal/JsonOutputs/common_ms/btl_arts_dr_cap.json", "r+", encoding='utf-8') as DescFile:     
            artsData = json.load(ArtsFile)
            descData = json.load(DescFile)
            
            for art in artsData["rows"]:
                targetCaptionID = art["Caption"]
                rangeCaption = ""
                
                # AOE
                for key,values in RangeType.items():    
                    if art["RangeType"] in values:
                        rangeCaption += key
                        break
                    
                # Reactions 
                reactionCaption = ""
                for i in range(1,17):              
                    if art[f"HitFrm{i}"] != 0:
                        for key,values in Reactions.items():
                            if art[f"ReAct{i}"] in values:
                                reactionCaption += f"{key}/"
                    else:
                        break
                reactionCaption = reactionCaption[:-1] 
                    
                # Enhancements
                enhancementCaption = ""
                for key,values in Enhancements.items():
                    if art["Enhance1"] in values:
                        enhancementCaption += key
                        break
                    
                # Debuffs  
                debuffCaption = ""                      
                for key,values in Debuffs.items():
                    if art["ArtsDeBuff"] in values:
                        debuffCaption = key
                  
                # Update Descriptions  
                for desc in descData["rows"]:            
                    if desc["$id"] == targetCaptionID:
                        desc["name"] = f"{rangeCaption} {reactionCaption} {enhancementCaption} {debuffCaption}"  
                            
            DescFile.seek(0)
            DescFile.truncate()
            json.dump(descData, DescFile, indent=2, ensure_ascii=False)             
        ArtsFile.seek(0)
        ArtsFile.truncate()
        json.dump(artsData, ArtsFile, indent=2, ensure_ascii=False)
    

def RemoveReactionsFromNonLastHit(art):
    last_hit = -1
    last_react = -1
    for i in range(16, 0, -1):
        if art['HitFrm' + str(i)] != 0 and last_hit == -1: # The final hit
            last_hit = i
            if art['ReAct' + str(i)] != 0: # if the final hit contains the final reaction
                last_react = i
        elif (i < last_hit) & (last_react == -1): # Before the final hit, when the last reaction is not yet found
            if art['ReAct' + str(i)] != 0:
                last_react = i
        elif i < last_hit: # Before the final hit, when the last reaction has been found    
            art['ReAct' + str(i)] = 0
        else: # Reactions which come after the final hit (unused, but let's keep the table clean for debugging purposes)
            art['ReAct' + str(i)] = 0