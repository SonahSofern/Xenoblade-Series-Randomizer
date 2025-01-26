import json, JSONParser
import random
from IDs import Lv1ArtCDs, EnhancementSets, ValidArtIDs, EvasionEnhancementIDs, SpecialEffectArtIDs, AutoAttacks, OriginalAOECaptionIDs

def RandomArtReactions(OptionsRunDict):
    HitReactionDistribution = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,6,7,8,9,10,11,12,13,14]
    MultipleReactions = OptionsRunDict["Art Reactions"]["subOptionObjects"]["Multiple Reactions"]["subOptionTypeVal"].get()
    sliderOdds = OptionsRunDict["Art Reactions"]["spinBoxVal"].get()
    
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in AutoAttacks: # Ignore autoes
                continue
            if sliderOdds > random.randrange(0,100): # Check slider
                for i in range(1,17):
                    if row[f"HitFrm{i}"] == 0: # Check if there is actually a hit
                        break
                    else:
                        row[f"ReAct{i}"] =  random.choice(HitReactionDistribution) # Apply a random reaction
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
                
    if not MultipleReactions:
        JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], ValidArtIDs, RemoveReactionsFromNonLastHit)

def RandomArtCooldowns(OptionsRunDict): # randomizes art cooldowns
    sliderOdds = OptionsRunDict["Driver Arts"]["spinBoxVal"].get()
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                if sliderOdds > random.randrange(0,100):
                    row["Recast1"] = random.choice(Lv1ArtCDs)
                    for j in range(2, 7):
                        row[f"Recast{j}"] = row[f"Recast{j-1}"] - random.choice([0, 0, 0, 1, 1, 2])
                        if row[f"Recast{j}"] < 1:
                            row[f"Recast{j}"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtDamageRatios(OptionsRunDict): # randomizes damage ratios
    sliderOdds = OptionsRunDict["Driver Arts"]["spinBoxVal"].get()
    Lv1DamageRatios = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 125, 125, 130, 130, 130, 130, 130, 130, 140, 140, 140, 140, 144, 144, 144, 144, 144, 144, 144, 150, 150, 150, 150, 150, 150, 150, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 168, 168, 168, 168, 168, 168, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 210, 210, 210, 210, 210, 210, 210, 210, 210, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 230, 231, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 250, 250, 250, 250, 255, 255, 255, 260, 260, 260, 260, 260, 260, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 285, 285, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 315, 315, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 345, 345, 345, 345, 360, 360, 360, 360, 360, 360, 360, 360, 360, 375, 375, 375, 375, 390, 390, 390, 420, 420, 420]
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                if sliderOdds > random.randrange(0,100):
                    row["DmgMgn1"] = random.choice(Lv1DamageRatios)
                    for j in range(2, 7):
                        row[f"DmgMgn{j}"] = row[f"DmgMgn{j-1}"] + random.choice([20, 20, 30, 30, 30, 30, 30, 30, 40, 40, 40, 50, 50])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def RandomArtEnhancements(OptionsRunDict): # randomizes art enhancements
    sliderOdds = OptionsRunDict["Driver Arts"]["spinBoxVal"].get()
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidArtIDs:
                if sliderOdds > random.randrange(0,100):
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

    MoveType = {
        "Heal": [3],
        "Defend": [11]
    }

    Reactions = {
        "B" : [1],
        "T" : [2],
        "L" : [3],
        "S" : [4],
        "Kb": [5,6,7,8,9],
        "Bd": [10,11,12,13,14]
    }

    FullReactions = {
        "Break" : [1],
        "Topple" : [2],
        "Launch" : [3],
        "Smash" : [4],
        "Knockback": [5,6,7,8,9],
        "Blowdown": [10,11,12,13,14]
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
        "Low HP↑": [2790,2785],
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
        "Freeze": [30],
        "Enrage": [35]
    }
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", "r+", encoding='utf-8') as ArtsFile:     
        with open("./_internal/JsonOutputs/common_ms/btl_arts_dr_cap.json", "r+", encoding='utf-8') as DescFile:     
            artsData = json.load(ArtsFile)
            descData = json.load(DescFile)
            AnchorShotDesc = 0
            
            for art in artsData["rows"]:
                if art["$id"] in ValidArtIDs:
                    CurrDesc = art["Caption"]
                    CombinedCaption = ["","","","",""]
                    FirstDescriptionMod = 0
                    LastDescriptionMod = 0
                    # AOE
                    for key,values in RangeType.items():    
                        if art["RangeType"] in values:
                            CombinedCaption[0] += f"{key}"
                            break

                    # Type of Art
                    for key,values in MoveType.items():
                        if art["ArtsType"] in values:
                            CombinedCaption[1] += f"{key}"
                            break

                    # Reactions 
                    ReactCaption = ""
                    TypeReactions = []
                    for i in range(1,17):              
                        if art[f"HitDirID{i}"] != 0:
                            for key,values in Reactions.items():
                                if art[f"ReAct{i}"] in values:
                                    ReactCaption += f"{key}->"
                                    TypeReactions.append(art[f"ReAct{i}"])
                                    break
                    ReactCaption = ReactCaption[:-2]
                    if len(ReactCaption) > 15: # If the length is too long, shorten it to "Driver Combo"
                        ReactCaption = "Driver Combo"
                    elif len(TypeReactions) == 1: # If the length is 1, spell out the reaction
                        for key,values in FullReactions.items():
                            if TypeReactions[0] in values:
                                ReactCaption = f"{key}"
                                break
                    CombinedCaption[2] = ReactCaption
                        
                    # Enhancements
                    for key,values in Enhancements.items():
                        if art["Enhance1"] in values:
                            CombinedCaption[3] += f"{key}"
                            break
                        
                    # Debuffs                       
                    for key,values in Debuffs.items():
                        if art["ArtsDeBuff"] in values:
                            CombinedCaption[4] = f"{key}"
                            break

                    # Putting it all together
                    TotalArtDescription = ""    
                    for i in range(0, len(CombinedCaption)):
                        if CombinedCaption[i] != "":
                            FirstDescriptionMod = i
                            break
                    for i in range(len(CombinedCaption) - 1, 0, -1):
                        if CombinedCaption[i] != "":
                            LastDescriptionMod = i
                            break
                    TotalArtDescription += CombinedCaption[FirstDescriptionMod]
                    if FirstDescriptionMod != LastDescriptionMod:
                        for i in range(FirstDescriptionMod + 1, LastDescriptionMod + 1):
                            if CombinedCaption[i] != "":
                                TotalArtDescription += " / "
                                TotalArtDescription += CombinedCaption[i]

                    if TotalArtDescription == "":
                        TotalArtDescription = "No Effects"

                    # Update Descriptions
                    for desc in descData["rows"]:
                        if desc["$id"] == CurrDesc:
                            desc["name"] = TotalArtDescription
                            break

            for desc in descData["rows"]:
                if desc["$id"] == 4:
                    AnchorShotDesc = desc["name"]
                    break
            for desc in descData["rows"]:
                if desc["$id"] == 5:
                    desc["name"] = AnchorShotDesc
                    break
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