import json
import random
from IDs import Arts, AutoAttacks
import Options
import scripts.PopupDescriptions
from _Arts import *



def DriverArtRandomizer():
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        isAutoAttacks = Options.DriverArtsOption_AutoAttacks.GetState()
        isMultiReact = Options.DriverArtsOption_MultipleReactions.GetState()
        isReactions = Options.DriverArtsOption_SingleReaction.GetState()
        isCooldowns = Options.DriverArtsOption_Cooldown.GetState()
        isDamage = Options.DriverArtsOption_Damage.GetState()
        isEnhancements = Options.DriverArtsOption_Enhancements.GetState()
        isBuffs = Options.DriverArtsOption_Buffs.GetState()
        isDebuffs = Options.DriverArtsOption_Debuffs.GetState()
        isAOE = Options.DriverArtsOption_AOE.GetState()
        isSpeed = Options.DriverArtsOption_AnimationSpeed.GetState()
        odds = Options.DriverArtsOption.GetOdds()
        
        for art in artData["rows"]:
            if art["$id"] in [4,5,6,7]: # Dont change aegis since they get copied to later
                continue
            
            if (not isAutoAttacks) and (isAutoAttacks or (art["$id"] in AutoAttacks)): # Ignore auto attacks unless the option is clicked
                continue
            isEnemyTarget = (art["Target"] in [0,4]) # Ensures Targeting Enemy
    
            if (isReactions or isMultiReact) and isEnemyTarget:
                for j in range(1,17):
                    art[f"ReAct{j}"] = 0 # Clearing Defaults these are needed bc torna arts are weird so i cant clear them blindly before hand gotta follow these conditions so this is the easiest way
                if OddCheck(odds):
                    Reaction(art, isMultiReact)
                    
            if isCooldowns and OddCheck(odds):
                Cooldowns(art)
                
            if isDamage and OddCheck(odds):
                Damage(art)
                
            if isEnhancements and isEnemyTarget:
                for i in range(1,7):
                    art[f"Enhance{i}"] = 0
                if OddCheck(odds):
                    Enhancements(art)
                    
            if isBuffs:
                art["ArtsBuff"] = 0 
                if OddCheck(odds//2): # These are really strong so im lowering the odds
                    Buffs(art)
                    
            if isDebuffs and isEnemyTarget:
                art["ArtsDeBuff"] = 0
                if OddCheck(odds):
                    Debuffs(art)
                    
            if isAOE and isEnemyTarget:
                art["RangeType"] = 0
                if OddCheck(odds):
                    AOE(art)
                    
            if isSpeed and OddCheck(odds):
                AnimationSpeed(art)

        # Since Aegis and Broadsword Share Captions they need the same effects
        CopyArt(artData,305,4)
        CopyArt(artData,306,5)
        CopyArt(artData,308,6)
        CopyArt(artData,307,7)
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
 
def CopyArt(artData, copyID, artID): # Copies all relevant effects of the art for shared captions
    for art in artData["rows"]:
        if art["$id"] == copyID:
            copy = art
            break
    for art in artData["rows"]:
        if art["$id"] == artID:
            art["RangeType"] = copy["RangeType"]
            art["Radius"] =  copy["Radius"]
            art["Length"] = copy["Length"]
            for i in range(1,17):
                art[f"ReAct{i}"] = copy[f"ReAct{i}"]
            for i in range(1,7):
                art[f"Enhance{i}"] = copy[f"Enhance{i}"]
            art["ArtsDeBuff"] = copy["ArtsDeBuff"]
            art["ArtsBuff"] = copy["ArtsBuff"]
            break


def OddCheck(odds):
    return (odds > random.randrange(0,100))

def Reaction(art, multReact):
    for i in range(1,17):
        if art[f"ReAct{i}"] > 14: # Dont replace weird ones that just move blades
            continue
        choice = random.choice(ReactionGroup)
        if art[f"HitFrm{i}"] == 0 and (i != 16 and art[f"HitFrm{i+1}"] == 0): # Need the second condition because zenobias Ascension Blade 129 has no hit on frame 1 but afterwards has hits # Make sure there is a hit
            art[f"ReAct{i-1}"] = random.choice(choice.ids) # Adds something to the last hit
            break
        if multReact:
            art[f"ReAct{i}"] =  random.choice(choice.ids) # Adds each hit


initialCooldownRange = [5,14]
def Cooldowns(art): 
    CD = random.randrange(initialCooldownRange[0], initialCooldownRange[1])
    for i in range(1,7):
        step = random.choice([0,0,1,1,1,2])
        if CD > step:
            CD -= step
        art[f"Recast{i}"] = CD

def Damage(art): 
    DMG = random.randrange(100,325,5)
    initDMG = DMG
    # different damage scalings for different arts, chosen at random, added to make arts feel more unique. Arts with lower base damages should scale lower, while arts with higher base damages should scale higher
    scales = { 
        "low": [10, 15, 20],
        "med": [25, 30, 35],
        "high": [35, 40, 45]
    }
    for i in range(1,7):
        match initDMG:
            case initDMG if initDMG <= 175:
                chosenscale = "low"
            case initDMG if 175 < initDMG <= 250:
                chosenscale = "med"
            case initDMG if initDMG > 250:
                chosenscale = "high"
        step = random.choice(scales[chosenscale])
        DMG += step
        art[f"DmgMgn{i}"] = DMG
        
def Enhancements(art): 
    Enhancement = random.choice(EnhancementGroup) # Choose the group
    enh = random.choice(Enhancement.ids) # Choose the inner group
    for i in range(1,7):
        art[f"Enhance{i}"] = enh[i-1]



def Buffs(art):
    buff = random.choice(BuffGroup)
    art["ArtsBuff"] = random.choice(buff.ids)

def Debuffs(art):
    debuff = random.choice(DebuffGroup)
    art["ArtsDeBuff"] = random.choice(debuff.ids)

animationSpeedRange = [50,200]
def AnimationSpeed(art):
    art["ActSpeed"] = random.randrange(animationSpeedRange[0],animationSpeedRange[1],10)

def AOE(art):
    RangeType = random.choice(AOEGroup)
    RandomRadius = random.randint(10,15)
    RandomLength = random.randrange(2,17,4)
    art["RangeType"] = random.choice(RangeType.ids)
    art["Radius"] =  RandomRadius
    art["Length"] = RandomLength



def GenCustomArtDescriptions(artsFile, descFile, isSpecial = False, enhancementKey = "Enhance1"):
    with open(artsFile, "r+", encoding='utf-8') as ArtsFile:     
        with open(descFile, "r+", encoding='utf-8') as DescFile:     
            artsData = json.load(ArtsFile)
            descData = json.load(DescFile)
            AnchorShotDesc = 0
            
            for art in artsData["rows"]:
                CurrDesc = art["Caption"]
                CombinedCaption = ["","","","",""]
                FirstDescriptionMod = 0
                LastDescriptionMod = 0
                # AOE
                for aoe in AOEGroup:    
                    if art["RangeType"] in aoe.ids:
                        CombinedCaption[0] += f"[System:Color name=blue]{aoe.name}[/System:Color]"
                        break

                # Type of Art Not changing this currently 
                # for key,values in MoveType.items():
                #     if art["ArtsType"] in values:
                #         CombinedCaption[1] += f"{key}"
                #         break
                
                for buff in BuffGroup:
                    if art["ArtsBuff"] in buff.ids:
                        CombinedCaption[1] += f"[System:Color name=green]{buff.name}[/System:Color]"
                        break

                # Reactions 
                ReactCaption = ""
                TypeReactions = []
                art
                for i in range(1,17):              
                    if (art[f"HitDirID{i}"] != 0) or (isSpecial and (art[f"HitFrm{i}"] != 0)):
                        for react in ReactionGroup:
                            if art[f"ReAct{i}"] in react.ids:
                                ReactCaption += f"[System:Color name=tutorial]{react.abvName}[/System:Color]->"
                                TypeReactions.append(art[f"ReAct{i}"])
                                break
                ReactCaption = ReactCaption[:-2]
                # if len(ReactCaption) > 15: # If the length is too long, shorten it to "Driver Combo"
                #     ReactCaption = "[System:Color name=tutorial]Driver Combo[/System:Color]"
                if len(TypeReactions) == 1: # If the length is 1, spell out the reaction
                    for react in ReactionGroup:
                        if TypeReactions[0] in react.ids:
                            ReactCaption = f"[System:Color name=tutorial]{react.name}[/System:Color]"
                            break
                CombinedCaption[2] = ReactCaption
                    
                # Enhancements
                for enh in EnhancementGroup:
                    if any(art[enhancementKey] in sublist for sublist in enh.ids):
                        CombinedCaption[3] += f"{enh.name}"
                        break
                    
                # Debuffs   
                if (art.get("ArtsDeBuff") != None):                    
                    for debuff in DebuffGroup:
                        if art["ArtsDeBuff"] in debuff.ids:
                            CombinedCaption[4] = f"[System:Color name=red]{debuff.name}[/System:Color]"
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
                        if not isSpecial: 
                            if desc["$id"] == 4:   # Sets anchor shot 5 to anchor shot 4's description since they are the same art
                                TotalArtDescription = TotalArtDescription.replace(ReactCaption + " / ", "")   # Removes the reaction text from 4 because it is disabled until you get to uraya. 4 Corresponds to before uraya description and 5 is after uraya.
                                AnchorShotDesc = desc["name"]
                                desc["name"]
                            if desc["$id"] == 5:
                                desc["name"] = AnchorShotDesc
                                break
                        desc["name"] = TotalArtDescription
                        break

                    
            DescFile.seek(0)
            DescFile.truncate()
            json.dump(descData, DescFile, indent=2, ensure_ascii=False)             
        ArtsFile.seek(0)
        ArtsFile.truncate()
        json.dump(artsData, ArtsFile, indent=2, ensure_ascii=False)
        
        
def DriverArtDescriptions():
    desc= scripts.PopupDescriptions.Description()
    desc.Header(Options.DriverArtsOption.name)
    desc.Text("This option randomizes various effects of driver arts, even to effects that could not be obtained in the normal game.")
    desc.Image("artsimage.png", "XC2", 600)
    desc.Text("Any changes made will update the art's description in combat. These are color coded by type.")
    desc.Header(Options.DriverArtsOption_AutoAttacks.name)
    
    desc.Text("Applies your chosen options to each driver's autoattacks as well as arts.")
    desc.Header(f"{Options.DriverArtsOption_SingleReaction.name}/{Options.DriverArtsOption_MultipleReactions.name}")
    
    desc.Text("Allows single/multiple reaction(s) to be placed on arts, shown in yellow text. \nThese will be abbreviated if the description gets too long.\nIf both options are enabled multiple reactions will take priority.")
    for react in ReactionGroup:
        desc.Tag(f"{react.name} ({react.abvName})")
        desc.Text(react.desc)
        
    desc.Header(Options.DriverArtsOption_Debuffs.name)
    desc.Text("Allows Debuffs to be placed on arts, shown in red text.")

    for debuff in DebuffGroup:
        desc.Tag(debuff.name)
        desc.Text(debuff.desc)
        
    desc.Header(Options.DriverArtsOption_Buffs.name)
    desc.Text("Allows Buffs to be placed on arts, shown in green text.")
    for buff in BuffGroup:
        desc.Tag(buff.name)
        desc.Text(buff.desc)
    
    desc.Header(Options.DriverArtsOption_Enhancements.name)
    desc.Text("Randomizes the enhancements on arts, shown in neutral text.")
    for enh in EnhancementGroup:
        desc.Tag(enh.name)
        desc.Text(enh.desc)
        
    desc.Header(Options.DriverArtsOption_Cooldown.name)
    desc.Text(f"Randomizes cooldowns for arts. Each art has a random starting cooldown. Then each level up has a chance to lower the cooldown.")    
        
    desc.Header(Options.DriverArtsOption_Damage.name)
    desc.Text(f"Randomizes damage ratios of arts. Each art has a random starting ratio. Then each level up increases the damage by a random amount.")
    
    desc.Header(Options.DriverArtsOption_AnimationSpeed.name)
    desc.Text(f"Randomizes animation speeds of arts between {animationSpeedRange[0]} - {animationSpeedRange[1]}%.")
    
    desc.Header(Options.DriverArtsOption_AOE.name)
    desc.Text(f"Randomizes the AOE types of your arts.\nAOE around target\nAOE around user\nAOE cone")
    return desc