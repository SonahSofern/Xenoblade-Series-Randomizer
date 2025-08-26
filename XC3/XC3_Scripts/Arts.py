import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options
from XC3.XC3_Scripts import IDs

Data = Helper.RandomGroup()

def ArtRando(targetGroupIDs):  
    global Data  
    unlockFlag = "<A2275574>"
    StateKeys = ['StateName', 'StateName2', 'StateLoopNum', 'WpnType'] # So actions match the original art
    HitFrames = ['HitFrm01', 'HitFrm02', 'HitFrm03', 'HitFrm04', 'HitFrm05', 'HitFrm06', 'HitFrm07', 'HitFrm08', 'HitFrm09', 'HitFrm10', 'HitFrm11', 'HitFrm12', 'HitFrm13', 'HitFrm14', 'HitFrm15', 'HitFrm16']
    ignoreKeys = ["$id",  unlockFlag, "UseChr", "UseTalent", "WpnType"] + StateKeys + HitFrames
    
    with open("XC3/JsonOutputs/btl/BTL_Arts_PC.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        if Data.isEmpty():
            Data.GenData(artData)            
        
        for art in artData["rows"]:
            if art["$id"] not in targetGroupIDs:
                continue
            
            # Choose an art group with weights and then a random member from the group
            # Copy Keys
            # Handle Duplicate named arts (just copy the result onto ones with the same name)
            
            
            
            
            
        
        JSONParser.CloseFile(artData, artFile)

# ArtCategory 
# 0 : Autos
# 1 : Arts, Mega Slash finishers, 
# 2 : Talent Arts
# 3 : Chain Attack Moves?
# 4 : Unused?