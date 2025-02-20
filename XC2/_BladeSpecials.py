import json, Options, _DriverArts, random
from scripts import Helper


def BladeSpecials():
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_Bl.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        isReact = Options.BladeSpecialOption_Reaction.GetState()
        isEnhancements = Options.BladeSpecialOption_Enhancement.GetState()
        isDebuffs = Options.BladeSpecialOption_Debuffs.GetState()
        odds = Options.BladeSpecialOption.GetOdds()
        
        for art in artData["rows"]:
            if isReact:
                for i in range(1,17):
                    if art[f"ReAct{i}"] > 14: # Ignore special cases that just move the blade around
                        continue
                if Helper.OddsCheck(odds):
                    _DriverArts.Reaction(art, True)
                
            if isEnhancements:
                if Helper.OddsCheck(odds):
                    Enhancements(art, _DriverArts.EnhancementSets)
                            
            if isDebuffs:
                art["ArtsDeBuff"] = 0
                if Helper.OddsCheck(odds):
                    _DriverArts.Debuffs(art)

                    
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
        BladeEXSpecials()
    _DriverArts.GenCustomArtDescriptions("./XC2/_internal/JsonOutputs/common/BTL_Arts_Bl.json", "./XC2/_internal/JsonOutputs/common_ms/btl_arts_bl_ms.json", True)


def Enhancements(art, EnhancementSet): 
    Enhancement = random.choice(EnhancementSet)
    for i in range(1,7):
        
        if art["Enhance1"] == 0: # Ignore specials that dont already have effects
            break
        
        art[f"Enhance{i}"] = Enhancement[i-1]
        

def BladeEXSpecials():
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_BlSp.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        isReact = Options.BladeSpecialOption_Reaction.GetState()
        isEnhancements = Options.BladeSpecialOption_Enhancement.GetState()
        odds = Options.BladeSpecialOption.GetOdds()
        
        for art in artData["rows"]:
            if isReact:
                for i in range(1,17):
                    if art[f"ReAct{i}"] > 14: # Ignore special cases that just move the blade around
                        continue
                if Helper.OddsCheck(odds):
                    _DriverArts.Reaction(art, True)
                
            if isEnhancements:
                if Helper.OddsCheck(odds):
                    EXEnhancements(art)
                                         
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
    _DriverArts.GenCustomArtDescriptions("./XC2/_internal/JsonOutputs/common/BTL_Arts_BlSp.json", "./XC2/_internal/JsonOutputs/common_ms/btl_arts_blsp_ms.json", True)

def EXEnhancements(art):
    Enhancement = random.choice(_DriverArts.EnhancementSets)
    art[f"Enhance"] = Enhancement[-1]