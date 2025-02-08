import json, JSONParser
import random
from IDs import EnhancementSets, ValidArtIDs, EvasionEnhancementIDs, SpecialEffectArtIDs, AutoAttacks


def DriverArtRandomizer(optionDict):
    with open("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        isAutoAttacks = optionDict["Driver Arts"]["subOptionObjects"]["Auto Attacks"]["subOptionTypeVal"].get()
        multipleReactions = optionDict["Driver Arts"]["subOptionObjects"]["Multiple Reactions"]["subOptionTypeVal"].get()
        isReactions = optionDict["Driver Arts"]["subOptionObjects"]["Reactions"]["subOptionTypeVal"].get()
        isCooldowns = optionDict["Driver Arts"]["subOptionObjects"]["Cooldown"]["subOptionTypeVal"].get()
        isDamage = optionDict["Driver Arts"]["subOptionObjects"]["Damage"]["subOptionTypeVal"].get()

        odds = optionDict["Driver Arts"]["spinBoxVal"].get()
        
        for art in artData["rows"]:
            
            if (not isAutoAttacks) and (isAutoAttacks or (art["$id"] in AutoAttacks)): # Ignore auto attacks unless the option is clicked
                continue
            validChanges = FindValidChanges(art, odds,  multipleReactions, isReactions, isCooldowns, isDamage) # Find Valid Changes

            for change in validChanges: # Apply Changes
                change()
        
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
 
def FindValidChanges(art,odds, multipleReactions, isReactions, isCooldowns, isDamage):
    validChanges = []
    
    if isReactions and (art["Target"] == 0) and (odds > random.randrange(0,100)): # Ensures Targeting enemy
        validChanges.append(lambda: Reaction(art, multipleReactions))
    if isCooldowns and (odds > random.randrange(0,100)):
        validChanges.append(lambda: Cooldowns(art))
    if isDamage and (odds > random.randrange(0,100)):
        validChanges.append(lambda: Damage(art))
    return validChanges


def Reaction(art, multReact):
    ValidReactions = {
        "Break" : [1],
        "Topple": [2],
        "Launch": [3],
        "Smash": [4],
        "KB": [5,6,7,8,9],
        "BD": [10,11,12,13,14],
    }
    
    for i in range(1,17):
        name,values = random.choice(list(ValidReactions.items()))
        if art[f"HitFrm{i}"] == 0: # Make sure there is a hit
            art[f"ReAct{i-1}"] = random.choice(values) # Adds something to the last hit
            break
        if multReact:
            art[f"ReAct{i}"] =  random.choice(values) # Adds each hit

def Cooldowns(art): # randomizes art cooldowns
    CD = random.randrange(2,12)
    for i in range(1,7):
        step = random.choice([0,0,0,1,1,2])
        if CD > step:
            CD -= step
        art[f"Recast{i}"] = CD

def Damage(art): # randomizes damage ratios
    DMG = random.randrange(100,200,10)
    for i in range(1,7):
        step = random.choice([0,0,20,20,50,100])
        DMG += step
        art[f"DmgMgn{i}"] = DMG

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
        "Evade": [2825,2866,2872],
        "Flying↑": [2700],
        "Front↑": [2740],
        "Vamp": [2735,2878],
        "Party Vamp": [2845],
        "High HP↑": [2800,2805],
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
        # "Stench": [12], # This one makes annoying noise and doesnt affect most enemies, im not even sure it affects enemy drivers tbh
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
                            CombinedCaption[0] += f"[System:Color name=green]{key}[/System:Color]"
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
                                    ReactCaption += f"[System:Color name=tutorial]{key}[/System:Color]->"
                                    TypeReactions.append(art[f"ReAct{i}"])
                                    break
                    ReactCaption = ReactCaption[:-2]
                    # if len(ReactCaption) > 15: # If the length is too long, shorten it to "Driver Combo"
                    #     ReactCaption = "[System:Color name=tutorial]Driver Combo[/System:Color]"
                    if len(TypeReactions) == 1: # If the length is 1, spell out the reaction
                        for key,values in FullReactions.items():
                            if TypeReactions[0] in values:
                                ReactCaption = f"[System:Color name=tutorial]{key}[/System:Color]"
                                break
                    CombinedCaption[2] = ReactCaption
                        
                    # Enhancements
                    for key,values in Enhancements.items():
                        if art["Enhance1"] in values:
                            CombinedCaption[3] += f"[System:Color name=green]{key}[/System:Color]"
                            break
                        
                    # Debuffs                       
                    for key,values in Debuffs.items():
                        if art["ArtsDeBuff"] in values:
                            CombinedCaption[4] = f"[System:Color name=red]{key}[/System:Color]"
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