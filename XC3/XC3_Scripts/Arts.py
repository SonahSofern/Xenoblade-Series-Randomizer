import json, random
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import IDs

artGroupData = Helper.RandomGroup()
ouroArtGroupData = Helper.RandomGroup()
ouroTalentArtGroupData = Helper.RandomGroup()
talentArtGroupData = Helper.RandomGroup()
hackerArtGroupData = Helper.RandomGroup()
groupData:list[Helper.RandomGroup] = [artGroupData, ouroArtGroupData,talentArtGroupData, ouroTalentArtGroupData, hackerArtGroupData]

# Art hits fixes (need to match the original arts animations hits, so sword strike only hits once it just combines effects, but what about reactions hits)

# Tutorial Fights need to be vetted (theres one that forces you to break topple daze for example) # Am going to just remove the requirement

def ArtRando(targetGroupIDs, artOption, ouroArtOption, talentArtOption, ouroTalentArtOption, hackerArtOption, spinbox, extraIgnoreKeys):  
    global groupData  
    unlockFlag = "<A2275574>"
    SortingKeys =  ["ArtsCategory", "ArtsType"] # Keep things sorted in the menus
    StateKeys = ['StateName', 'StateName2', 'StateLoopNum', 'WpnType'] # So actions match the original art
    HitFrames = ['HitFrm01', 'HitFrm02', 'HitFrm03', 'HitFrm04', 'HitFrm05', 'HitFrm06', 'HitFrm07', 'HitFrm08', 'HitFrm09', 'HitFrm10', 'HitFrm11', 'HitFrm12', 'HitFrm13', 'HitFrm14', 'HitFrm15', 'HitFrm16']
    ignoreKeys = ["$id",  unlockFlag, "UseChr", "UseTalent", "WpnType"] + StateKeys + HitFrames + extraIgnoreKeys + SortingKeys

    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        if artGroupData.isEmpty(): 
            GenArtData(artData)  
            
        Weights = GenWeights(artOption, ouroArtOption, talentArtOption, ouroTalentArtOption, hackerArtOption)
        
        for art in artData["rows"]:
            if art["$id"] not in targetGroupIDs:
                continue
            if not Helper.OddsCheck(spinbox):
                continue
            
            chosenGroup = random.choices(groupData, Weights)
            chosenArt = chosenGroup[0].SelectRandomMember()  
            
            GrowMatchStrongest(chosenArt, art, "Stance")
            GrowMatchStrongest(chosenArt, art, "Recast") 
            GrowMatchStrongest(chosenArt, art, "DmgMgn") 
            GrowMatchStrongest(chosenArt, art, "Enhance")
            
            # Handle Duplicate named arts (just copy the result onto ones with the same name)
            if targetGroupIDs == IDs.ArtIDs:
                HandleArtCopies(chosenArt, art, artData, ignoreKeys)
            
            Helper.CopyKeys(art, chosenArt, ignoreKeys + HandleRecastKeys(chosenArt, art))
        
        # Refresh groups
        for group in groupData:
            group.RefreshCurrentGroup()
            
        JSONParser.CloseFile(artData, artFile)
        
def GetMatchLength(art, key, upper = 6):
    '''Returns the max levels + 1 for the art'''
    for i in range(1,upper):
        if art[f"{key}{i}"] == 0:
            return i
    return 6

def GrowMatchStrongest(chosenArt, originalArt, key):
    '''Matches levels between arts, some arts don't level up as much as others and it breaks them if so'''
    chosenMaxLength = GetMatchLength(chosenArt, key)
    originalMaxLength = GetMatchLength(originalArt, key)
    
    if chosenMaxLength == 1: # The chosen art does not scale through levels through this key so we dont bother
        return
    
    if originalMaxLength > chosenMaxLength:
        for i in range(chosenMaxLength, originalMaxLength):
            chosenArt[f"{key}{i}"] = chosenArt[f"{key}{chosenMaxLength-1}"]
    elif originalMaxLength < chosenMaxLength:
        pass
    else:
        pass

def HandleRecastKeys(chosenArt, originalArt):
    '''Various logic determining how to recast the art depending on the group and its replacement'''
    if (originalArt["$id"] in IDs.ArtIDs + IDs.HackerArtIDs) and (chosenArt["$id"] in IDs.ArtIDs + IDs.HackerArtIDs): # Art, Hacker -> Art, Hacker (If so we copy the recast keys)
        return []
    recastKeys = ["RecastType", "Recast1", "Recast2", "Recast3", "Recast4", "Recast5", "Region"]
    ouroborousRecastKeys = ["SpRecast1", "SpRecast2"]
    return recastKeys + ouroborousRecastKeys

def GenArtData(artData):
    for art in artData["rows"]:
        id = art["$id"]
        if id in IDs.ArtIDs:
            artGroupData.AddNewData(art)
        elif id in IDs.TalentArtIDs:
            talentArtGroupData.AddNewData(art)
        elif id in IDs.OuroborosArtIDs:
            ouroArtGroupData.AddNewData(art)
        elif id in IDs.OuroTalentArtIDs:
            ouroTalentArtGroupData.AddNewData(art)
        elif id in IDs.HackerArtIDs:
            hackerArtGroupData.AddNewData(art)
        else:
            continue

def GenWeights(art, ouroArt, talentArt, ouroTalentArt, hackerArt):
    weights = [0,0,0,0,0]
    if art.GetState():
        weights[0] = art.GetSpinbox()
    if ouroArt.GetState():
        weights[1] = ouroArt.GetSpinbox()
    if talentArt.GetState():
        weights[2] = talentArt.GetSpinbox()
    if ouroTalentArt.GetState():
        weights[3] = ouroTalentArt.GetSpinbox()
    if hackerArt.GetState():
        weights[4] = hackerArt.GetSpinbox()
    return weights

def HandleArtCopies(chosen, art, artData, ignoreKeys):
    for localArt in artData["rows"]:
        if localArt["Name"] == art["Name"] and localArt["UseChr"] == 0:
            Helper.CopyKeys(localArt, chosen, ignoreKeys)

# ArtCategory 
# 0 : Autos
# 1 : Arts, Mega Slash finishers, 
# 2 : Talent Arts
# 3 : Chain Attack Moves?
# 4 : Unused?