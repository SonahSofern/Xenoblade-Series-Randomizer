import json, random
from Enhancements import *

def EnemyArts(spinbox):
    Arts = {
        "Skin Upgrade": 176,
        "Life Plant": 393,
        "Reset Punch": 50,
        "Element Breaker": 990,
        "Cold Era": 582
    }
    with open("./_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as EnFile:
        EnData = json.load(EnFile) # Adds a single new art to enemies to art 16
        for en in EnData["rows"]:
            if spinbox < random.randrange(0,100): # Spinbox value check
                continue
            en["ArtsNum16"] = random.choice(list(Arts.values()))
        EnFile.seek(0)
        EnFile.truncate()
        json.dump(EnData, EnFile, indent=2, ensure_ascii=False)  


def EnemyArtAttributes(spinBox):
    with open("./_internal/JsonOutputs/common/BTL_Arts_En.json", 'r+', encoding='utf-8') as EnArtsFile:
        with open("./_internal/JsonOutputs/common/BTL_Arts_BlSp.json", 'r+', encoding='utf-8') as EnBlArtsFile:
            with open("./_internal/JsonOutputs/common_ms/btl_arts_en_ms.json", 'r+', encoding='utf-8') as EnArtsNamesFile:  
                with open("./_internal/JsonOutputs/common_ms/btl_arts_blsp_ms.json", 'r+', encoding='utf-8') as EnBlArtsNamesFile:  
                    with open("./_internal/JsonOutputs/common_ms/btl_arts_bl_ms.json", 'r+', encoding='utf-8') as BlArtsNamesFile:  
                        with open("./_internal/JsonOutputs/common/BTL_Arts_Bl.json", 'r+', encoding='utf-8') as BlArtsFile:  
                            enArtsData = json.load(EnArtsFile)
                            enBlArtsData = json.load(EnBlArtsFile)
                            enArtsNameData = json.load(EnArtsNamesFile)
                            enBlArtsNameData = json.load(EnBlArtsNamesFile)
                            blArtNameData = json.load(BlArtsNamesFile)
                            blArtsData = json.load(BlArtsFile)
                            
                            ChangeArts(enArtsData, enArtsNameData, spinBox)
                            ChangeArts(enBlArtsData, enBlArtsNameData, spinBox)
                            # ChangeArts(blArtsData, blArtNameData, spinBox) # Currently this will change ally and enemy because they use the same files :/
                            
                            BlArtsFile.seek(0)
                            BlArtsFile.truncate()
                            json.dump(blArtsData, BlArtsFile, indent=2, ensure_ascii=False)  
                        BlArtsNamesFile.seek(0)
                        BlArtsNamesFile.truncate()
                        json.dump(blArtNameData, BlArtsNamesFile, indent=2, ensure_ascii=False)  
                    EnBlArtsNamesFile.seek(0)
                    EnBlArtsNamesFile.truncate()
                    json.dump(enBlArtsNameData, EnBlArtsNamesFile, indent=2, ensure_ascii=False)  
                EnArtsNamesFile.seek(0)
                EnArtsNamesFile.truncate()
                json.dump(enArtsNameData, EnArtsNamesFile, indent=2, ensure_ascii=False)  
            EnBlArtsFile.seek(0)
            EnBlArtsFile.truncate()
            json.dump(enBlArtsData, EnBlArtsFile, indent=2, ensure_ascii=False)
        EnArtsFile.seek(0)
        EnArtsFile.truncate()
        json.dump(enArtsData, EnArtsFile, indent=2, ensure_ascii=False)
        
def ChangeArts(artData, artNameData, spinBox):
    newNameID = 457 # Starting id to add new names to old names file
    for art in artData["rows"]:
        try:
            if art["Camera1"] == 0 and art["Camera2"] == 0 and art["Camera3"] == 0:
                pass
            else:
                continue
        except:
            pass # Needed to target only arts with no camera data because that corresponds with valid enemy blade arts 
        if spinBox < random.randrange(0,100): # Spinbox value check
            continue
        if art["Name"] == 0: # Avoid changing autoattacks and things with no name
            continue
        validChanges = FindValidChanges(art)  # i dont want to overwrite previous behaviour so check what i can change on an art
        if not validChanges: # Make sure theres at least one valid change to make
            continue
        newNameID += 1

        
        myChange = random.choice(validChanges) # choose a change to apply
        newNamePrefix = myChange()
        
        
        for name in artNameData["rows"]: # Get the old name
            if name["$id"] == art["Name"]:
                oldName = name["name"]
                break

        newName = { # create new name
            "$id" : newNameID,
            "style" : 15,
            "name" : f"[System:Color name=green]{newNamePrefix}[/System:Color] {oldName}"
        }
        art["Name"] =  newNameID # Set new name id to the art
        artNameData["rows"].append(newName) # add newname
        
def FindValidChanges(art):
    ValidChanges = []
    # try:
    #     if art["Recast"] not in [0]:    # Art has a Cooldown
    #         ValidChanges.append(lambda: Cooldown(art)) # Cooldown
    # except:
    #     pass # BTL_Arts_Bl doesnt have this
    # try:
    #     if art["ArtsDeBuff"] in [0]: # Only change arts with no debuff
    #         ValidChanges.append(lambda: Debuff(art))                # Debuff
    # except:
    #     pass # Enemy blade arts dont have ArtsDeBuff for some reason
    # for i in range(1,17): # Check that the art has at least one an empty hit to place a combo into
    #     if art[f"ReAct{i}"] == 0 and art[f"HitFrm{i}"] != 0:
    #         ValidChanges.append(lambda: Reaction(art))
    #         break
    # if art["ArtsBuff"] == 0: # Change arts that dont already do buff stuff
    #     ValidChanges.append(lambda: Buff(art))
    # try:
    #     if art["Enhance"] == 0: # Add enhancements only to arts without them
    #         ValidChanges.append(lambda: Enhancements(art))
    # except:
    #     pass # BTL_Arts_Bl doesnt have this
    if art["RangeType"] == 0 and art["ArtsType"] in [1,2,3]: # Make sure art is single target and a physical ether or healing move
        ValidChanges.append(lambda: AOE(art))
    return ValidChanges

ValidSkills = []
class EnemyArtEnhancements(Enhancement):
    def __init__(self, name, enhancement, para1 = [0,0,0,0],para2 = [0,0,0,0]):
        self.name = name
        self.EnhanceEffect = enhancement.EnhanceEffect
        self.Caption = 0
        self.addToList = False
        self.Param1 = para1
        self.Param2 = para2
        ValidSkills.append(self)
    
backatk = EnemyArtEnhancements("Back↑", BackDamageUp, [40,60,80,100])
frontatk = EnemyArtEnhancements("Front↑", FrontDamageUp, [20,40,60,80])
pierce = EnemyArtEnhancements("Pierce", GuardAnnulAttack, [100,100,100,100])
lowhpDamage = EnemyArtEnhancements("HP↓Dmg↑", DamageUpWhenHpDown, [10,20,30,40])
transmig = EnemyArtEnhancements("Flip", Transmigration, [100,100,100,100])
vamp = EnemyArtEnhancements("Vamp", ArtDamageHeal, [200,400,600,800])

def Enhancements(art):
    skill = random.choice(ValidSkills)
    skill.RollEnhancement()
    art["Enhance"] = skill.id
    return skill.name

def AOE(art):
    
    CircleAroundTarget = 1
    ConeAhead = 2
    CircleAroundUser = 5
    RangeType = random.choice(CircleAroundTarget, ConeAhead, CircleAroundUser)
    RandomRadius = random.randint(5,10)
    
    art["RangeType"] = RangeType
    art["Radius"] =  RandomRadius # Not sure what makes a good radius
    return "AOE"

def Reaction(art):
    #F combo is forced combo so it cant be resisted
    FullReactions = {
        # "Combo" : [1,2,3,4],
        # "KB": [5,6,7,8,9],
        # "BD": [10,11,12,13,14],
        # "-Orb": [46],
        # "Element": [45,17, 35],
        # "Escape": [18]
        "Enrage": [19,39,37], # Type 10 art or Range type 1, also make sure enemy actually has an enrage form
        # "ElementRebound": [20],
        # "Aff↓": [21,22,23,24,25],
        # "BlCombo↓": [34,40,45],
        "Flames": [38], # Needs circle id 1-6
    }
    name,values = random.choice(list(FullReactions.items()))
    for i in range(1,17):
        if art[f"HitFrm{i}"] == 0: # Make sure there is a hit
            break
        if art[f"ReAct{i}"] != 0: # Make sure it doesnt already have a reaction 
            continue
        art[f"ReAct{i}"] = random.choice(values)
    return name


def Buff(art):
    Buffs = {
        "Evade": 2,
        "Block": 3,
        "Counter": 6,
        "↑Counter": 7,
        "Rflct": 5,
        "Invi": 4,
        "Absorb":  17
    }
    name,value = random.choice(list(Buffs.items()))
    art["ArtsBuff"] = value
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
        "Rage": 35, # We just resist rage strike??
        # "Fire": 33 Already have fire this might just be a different buff even though its only on brighids confining flames
    }
    name,value = random.choice(list(Debuffs.items()))
    art["ArtsDeBuff"] = value
    return name
    

def Cooldown(art): 
    art["Recast"] //= random.choice([2,4,6])
    return f"CD↓"


