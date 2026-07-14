from scripts import JSONParser, StatRand, Helper, PopupDescriptions
from XCXDE.XCXDE_Scripts import IDs, Options

maxMult = 3

def ArtStatRando(intensity):
    ArtStats(intensity)
    ArtEnhancements(intensity)

def ArtStats(intensity):
    statRando = StatRand.Stat(maxMult, intensity)
    
    pcArtsFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    for art in pcArtsFile.rows:
        # Damage, Cooldown
        for stat in ["DmgMgn", "RecastFrm"]:
            mult = statRando.RollBalancedMult()
            for i in range(0,5):
                statRando.ApplyMult(art, f"{stat}[{i}]", mult)
        
        # Upgrade Cost
        mult = statRando.RollBalancedMult()
        for i in range(0,5):
            statRando.ApplyMult(art, f"Btlpt[{i}]", mult, min=0, max=StatRand.b8)
    pcArtsFile.Close()
    
     # TP Cost
    artsFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_ArtsList.json")
    artsMsFile = JSONParser.File("XCXDE/JsonOutputs/common_ms/BTL_ArtsList_ms.json")
    for art in artsFile.rows:
        statRando.ApplyMult(art, "DecDmp", statRando.RollBalancedMult(), min=0, roundedDigits=-2)
        ShowNewTpCosts(art, artsMsFile)
    artsFile.Close()
    artsMsFile.Close()
        
    # Buff Duration
    buffFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_BuffList.json")
    for buff in buffFile.rows:
        if buff["$id"] not in Helper.InclRange(54,80) + [241,242,243,283,284,285,286]: continue
        mult = statRando.RollBalancedMult()
        for i in range(1,7):
            statRando.ApplyMult(buff, f"Life{i}", mult)
    buffFile.Close()

def ShowNewTpCosts(art, artsMsFile:JSONParser.File):
    '''When randomizing TP costs we add the new cost to the in battle UI'''
    for artMs in artsMsFile.rows:
        if artMs["$id"] == art["Caption"]:
            oldName:str = artMs["name"]
            if '(TP)' not in oldName: return
            newTpCost = f"({art["DecDmp"]} TP)"
            artMs["name"] = oldName.replace("(TP)", newTpCost)
            return
    

def ArtEnhancements(intensity):
    '''Art enhancement currently paired with stats, they are unique to arts so can be adjusted without messing with other things'''
    statRando = StatRand.Stat(2, intensity)
    enhFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_Enhance.json")
    artFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    
    # Ids from BTL_PcArtsInfo
    param1MultArtIDs = [6, 8, 17, 19, 33, 81, 119, 142, 143, 158, 159] # Don't change param1 of this art
    param2MultArtIDs = [6, 8, 17, 19, 33, 119, 161] # Don't change param2 of this art
    ratioMultArtIDs = [33] # Change ratio of this art
    
    for art in artFile.rows:
        if art[f"Enhance[0]"] == 0: continue # This art has no enhancements so go next
        
        # Get the 5 level of enhancements that the art has
        targetEnhancementIDs = []
        for i in range(0,5):
            targetEnhancementIDs.append(art[f"Enhance[{i}]"])
            
        # Roll one mult for all 5 levels of this skill for each category
        if art["$id"] not in param1MultArtIDs: param1Mult = statRando.RollBalancedMult() 
        if art["$id"] not in param2MultArtIDs: param2Mult = statRando.RollBalancedMult()
        if art["$id"] in ratioMultArtIDs: ratioMult = statRando.RollBalancedMult()
    
        for enh in enhFile.rows:
            if enh["$id"] not in targetEnhancementIDs: continue
            if art["$id"] not in param1MultArtIDs: statRando.ApplyMult(enh, "param1", param1Mult)
            if art["$id"] not in param2MultArtIDs: statRando.ApplyMult(enh, "param2", param2Mult)
            if art["$id"] in ratioMultArtIDs: statRando.ApplyMult(enh, "ratio", ratioMult)
    
    enhFile.Close()
    artFile.Close()
    
def ArtUnlockOrder(): # Fix the PCArtsInfo
    artFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_ArtsList.json")
    artInfoFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json") # '''PcArtsInfo is indirectly linked to BTL_ArtsList, so id 1 is the same art. Just need to shuffle this file with the other'''
    rows = len(artFile.rows)
    class Art():
        def __init__(self, ArtsList, ArtsInfo):
            self.artsList = ArtsList
            self.artsInfo = ArtsInfo
    
    # Generate and sort the artgroup
    AllSortedGroups:list[Helper.RandomGroup] = []
    for group in IDs.AllWeaponGroups:
        artGroup = Helper.RandomGroup()
        
        for artID in range(rows):
            if artFile.rows[artID]["$id"] not in group: continue
            
            # and add to the correct group
            artGroup.AddNewData(Art(artFile.rows[artID], artInfoFile.rows[artID]))
                
        AllSortedGroups.append(artGroup)
    
    for artID in range(rows):
        curID = artFile.rows[artID]["$id"]
        if curID not in IDs.ArtIDs: continue
        
        # Find the arts weapon group
        group = None
        for artGroup in AllSortedGroups:
            if any(originalArt.artsList.get("$id") == curID for originalArt in artGroup.originalGroup):
                group = artGroup
                break
        if group == None: 
            raise Exception("Couldn't find weapon group")
        
        # roll new art
        newArt:Art = group.SelectRandomMember()
        
        # Set new art
        Helper.CopyKeys(artFile.rows[artID], newArt.artsList, ["$id", "ID"])
        Helper.CopyKeys(artInfoFile.rows[artID], newArt.artsInfo, ["$id", "ID"])
        
    artFile.Close()
    artInfoFile.Close()
                                                                                                                                                                                                                                                                   
def ArtDesc(name, newName):
    artRandoDesc = PopupDescriptions.Description()
    artRandoDesc.Header(newName)
    artRandoDesc.Text(f"Randomizes the strength (cooldown, damage, tp cost, etc.) of arts within {round(1/maxMult, 3)}-{maxMult} times the original amount.")
    artRandoDesc.Header(name)
    artRandoDesc.Text(f"Randomizes art unlocking. For example, Drifter uses rifle and knife, so the drifter class will be given random knife and rifle arts from any in the game.")
    artRandoDesc.Tag("Intensity")
    artRandoDesc.Text(StatRand.IntensityDescription)
    return artRandoDesc