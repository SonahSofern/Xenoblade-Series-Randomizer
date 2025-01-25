import json, random
from Enhancements import *

common = 0
rare = 1
legendary = 2

def EnemyArtAttributes(spinBox):
    with open("./_internal/JsonOutputs/common/BTL_Arts_En.json", 'r+', encoding='utf-8') as EnArtsFile:
        with open("./_internal/JsonOutputs/common_ms/btl_arts_en_ms.json", 'r+', encoding='utf-8') as NamesFile:      
            enArtsData = json.load(EnArtsFile)
            nameData = json.load(NamesFile)
            newNameID = 457 # Starting id to add new names to old names file
            for art in enArtsData["rows"]:
                if spinBox < random.randrange(0,100): # Spinbox value check
                    continue
                if art["Name"] == 0: # Avoid changing autoattacks and things with no name
                    continue
                rarity = random.choice([common,common,common,rare,rare,legendary]) # choose rarity
                validChanges = FindValidChanges(art, rarity)  # i dont want to overwrite previous behaviour so check what i can change on an art
                if not validChanges: # Make sure theres at least one valid change to make
                    continue
                newNameID += 1

                
                myChange = random.choice(validChanges) # choose a change to apply
                newNamePrefix = myChange()
                
                
                for name in nameData["rows"]: # Get the old name
                    if name["$id"] == art["Name"]:
                        oldName = name["name"]
                        break

                newName = { # create new name
                    "$id" : newNameID,
                    "style" : 15,
                    "name" : f"[System:Color name=green]{newNamePrefix}[/System:Color] {oldName}"
                }
                art["Name"] =  newNameID # Set new name id to the art
                nameData["rows"].append(newName) # add newname
                
                # Buff
                # Enhancement

            
            NamesFile.seek(0)
            NamesFile.truncate()
            json.dump(nameData, NamesFile, indent=2, ensure_ascii=False)
        EnArtsFile.seek(0)
        EnArtsFile.truncate()
        json.dump(enArtsData, EnArtsFile, indent=2, ensure_ascii=False)
        
def FindValidChanges(art, rarity):
    ValidChanges = []
    if art["Recast"] not in [0]:    # Art has a Cooldown
        ValidChanges.append(lambda: Cooldown(art, rarity)) # Cooldown
    if art["ArtsDeBuff"] in [0]: # Only change arts with no debuff
        ValidChanges.append(lambda: Debuff(art))                # Debuff
    if art["Target"] in [0]: # Only change art reactions that target enemies
        for i in range(1,17): # Check that the art has at least one an empty hit to place a combo into
            if art[f"ReAct{i}"] == 0 and art[f"HitFrm{i}"] != 0:
                ValidChanges.append(lambda: Reaction(art))
                break
    return ValidChanges

def AOE(art, rarity):
    HitTypes = {
        "Single": [0],
        "Circle": [1],
        "Cone": [2]
        
    }

def Reaction(art):
    FullReactions = {
        "Combo" : [1,2,3,4],
        "KB": [5,6,7,8,9],
        "BD": [10,11,12,13,14]
    }
    name,values = random.choice(list(FullReactions.items()))
    for i in range(1,17):
        if art[f"HitFrm{i}"] == 0: # Make sure there is a hit
            break
        if art[f"ReAct{i}"] != 0: # Make sure it doesnt already have a reaction 
            continue
        art[f"ReAct{i}"] = random.choice(values)
    return name

def Debuff(art):
    Debuffs = {
        "Taunt" : 11,
        "Stench": 12,
        "Shackle": 13,
        "Shackle": 14,
        "NlHeal": 15,
        "Doom": 21,
        "Def↓": 23,
        "EDef↓": 24,
        "Res↓": 25,
        "Rage": 35
    }
    name,value = random.choice(list(Debuffs.items()))
    art["ArtsDeBuff"] = value
    return name
    

def Cooldown(art, rarity): 
    if rarity == common:
        div = 2
    elif rarity == rare:
        div = 4
    elif rarity == legendary:
        div = 6
    
    art["Recast"] //= div
    return f"CD↓{'+' * rarity}"






