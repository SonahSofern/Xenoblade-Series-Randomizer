import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options
from XC3.XC3_Scripts import IDs

artGroupData = Helper.RandomGroup()
ouroArtGroupData = Helper.RandomGroup()
ouroTalentArtGroupData = Helper.RandomGroup()
talentArtGroupData = Helper.RandomGroup()
hackerArtGroupData = Helper.RandomGroup()
groupData:list[Helper.RandomGroup] = [artGroupData, ouroArtGroupData,talentArtGroupData, ouroTalentArtGroupData, hackerArtGroupData]


def ArtRando(targetGroupIDs, artOption, ouroArtOption, talentArtOption, ouroTalentArtOption, hackerArtOption, spinbox, extraIgnoreKeys):  
    global groupData  
    unlockFlag = "<A2275574>"
    StateKeys = ['StateName', 'StateName2', 'StateLoopNum', 'WpnType'] # So actions match the original art
    HitFrames = ['HitFrm01', 'HitFrm02', 'HitFrm03', 'HitFrm04', 'HitFrm05', 'HitFrm06', 'HitFrm07', 'HitFrm08', 'HitFrm09', 'HitFrm10', 'HitFrm11', 'HitFrm12', 'HitFrm13', 'HitFrm14', 'HitFrm15', 'HitFrm16']
    ignoreKeys = ["$id",  unlockFlag, "UseChr", "UseTalent", "WpnType"] + StateKeys + HitFrames + extraIgnoreKeys
    
    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        if artGroupData.isEmpty(): 
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
                  
            
        Weights = GenWeights(artOption, ouroArtOption, talentArtOption, ouroTalentArtOption, hackerArtOption)
        
        for art in artData["rows"]:
            if art["$id"] not in targetGroupIDs:
                continue
            if not Helper.OddsCheck(spinbox):
                continue
            
            # Choose an art group with weights and then a random member from the group
            chosen = random.choices(groupData,Weights)[0].SelectRandomMember()            
            
            # Handle Duplicate named arts (just copy the result onto ones with the same name)
            if targetGroupIDs == IDs.ArtIDs:
                HandleArtCopies(chosen, art, artData, ignoreKeys)
            
            # Copy Keys
            Helper.CopyKeys(art, chosen, ignoreKeys)
        
        # Refresh groups
        for group in groupData:
            group.RefreshCurrentGroup()
            
        JSONParser.CloseFile(artData, artFile)

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


def FixMismatchLevelUpSlots():
    # Some arts have 0s in slots when levelled up past a certain point
    pass
# ArtCategory 
# 0 : Autos
# 1 : Arts, Mega Slash finishers, 
# 2 : Talent Arts
# 3 : Chain Attack Moves?
# 4 : Unused?