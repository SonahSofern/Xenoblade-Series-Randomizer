import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options

# Talent Arts
# Ouroborous Arts
# Debug Arts
# Autoattacks
# Arts
# Super Combos (Slash Bomb, Mega Smash)

# Motion States
Autos = [1,2]
Arts = []
OuroborousArts = [231,]

# ArtCategory 
# 0 : Autos
# 1 : Arts, Mega Slash finishers, 
# 2 : Talent Arts
# 3 : Chain Attack Moves?
# 4 : Unused?

class Art:
    def __init__(self):
        self.originalUserArt = None
        self.learnedUserArt = None
        
    def isFullyPopulated(self):
        if self.originalUserArt != None and self.learnedUserArt != None:
            return True
    
def ArtRando():
    unlockFlag = "<A2275574>"
    StateKeys = ['StateName', 'StateName2', 'StateLoopNum', 'WpnType'] # So actions match the original art
    HitFrames = ['HitFrm01', 'HitFrm02', 'HitFrm03', 'HitFrm04', 'HitFrm05', 'HitFrm06', 'HitFrm07', 'HitFrm08', 'HitFrm09', 'HitFrm10', 'HitFrm11', 'HitFrm12', 'HitFrm13', 'HitFrm14', 'HitFrm15', 'HitFrm16']
    ignoreKeys = ["$id",  unlockFlag, "UseChr", "UseTalent", "WpnType"] + StateKeys + HitFrames
    
    artOdds = XC3.XC3_Scripts.Options.ArtsOption.GetSpinbox()
    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        with open("XC3/JsonOutputs/battle/msg_btl_arts_name.json", 'r+', encoding='utf-8') as nameFile:
            artData = json.load(artFile)
            nameData = json.load(nameFile)
            
            artList = Helper.RandomGroup()
            
            # Build the arts list
            for name in nameData["rows"]:
                newArt = Art()
                for art in artData["rows"]:
                    if not isValidArt(art):
                        continue
                    if art["Name"] == name["$id"]:
                        if (art["UseChr"] != 0) and (newArt.originalUserArt == None):
                            newArt.originalUserArt = copy.deepcopy(art)
                        elif newArt.learnedUserArt == None:
                            newArt.learnedUserArt = copy.deepcopy(art)
                        if newArt.isFullyPopulated():
                            break
                artList.AddNewData(newArt)
            
            
            
            # Replace the list
            try:
                for name in nameData["rows"]:
                    chosenArt:Art = artList.SelectRandomMember()
                    while not chosenArt.isFullyPopulated():
                        artList.FilterMember(chosenArt)
                        chosenArt:Art = artList.SelectRandomMember()
                        
                    for art in artData["rows"]:
                        if not isValidArt(art):
                            continue  
                        if not Helper.OddsCheck(artOdds):
                            continue
                        if art["Name"] == name["$id"]:
                            if art["UseChr"] != 0:
                                Helper.CopyKeys(art, chosenArt.originalUserArt, ignoreKeys)
                            else:
                                Helper.CopyKeys(art, chosenArt.learnedUserArt, ignoreKeys)
            except Exception as e:
                print(e)
                            
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
    if art["ArtsCategory"] != 1: # Only do Arts
        return False
    return True
