import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options

def ArtRando():
    ignoreKeys = ["$id", 'WpnType']
     
    StateKeys = ['StateName', 'StateName2', 'StateLoopNum', 'HitFrm01', 'HitFrm02', 'HitFrm03', 'HitFrm04', 'HitFrm05', 'HitFrm06', 'HitFrm07', 'HitFrm08', 'HitFrm09', 'HitFrm10', 'HitFrm11', 'HitFrm12', 'HitFrm13', 'HitFrm14', 'HitFrm15', 'HitFrm16'] # So actions match the original art

    artOdds = XC3.XC3_Scripts.Options.PlayerArtsOption.GetSpinbox()
    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        artList = Helper.RandomGroup()

        artList.GenData(artData["rows"])
        filteringList = copy.deepcopy(artList.originalGroup) # Make a copy because we cant filter this while looping over it
        for art in (filteringList):
            if not isValidArt(art):
                artList.FilterMember(art)
        
        # Replace the list
        for art in artData["rows"]:
            if not Helper.OddsCheck(artOdds):
                continue
            if not isValidArt(art):
                continue
            
            chosenArt = artList.SelectRandomMember()
                
            Helper.CopyKeys(art, chosenArt, ignoreKeys+StateKeys)

        JSONParser.CloseFile(artData, artFile)

def isValidArt(art):
    if art["Name"] == 0:
        return False
    if art["Caption"] == 0:
        return False
    if art["WpnType"] == 0:
        return False
    if art["Voice1"] == "":
        return False
    return True

def ArtEffects():
    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            if isValidArt(art):
                continue
        
        JSONParser.CloseFile(artData, artFile)