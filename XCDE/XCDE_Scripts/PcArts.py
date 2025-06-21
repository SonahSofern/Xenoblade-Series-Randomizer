import json, random
from XCDE.XCDE_Scripts import Options
import scripts.Helper, scripts.JSONParser, scripts.PopupDescriptions

TalentArts = [102,101,100,44,99,43,98,42,62,97,154,1,2,19,36,41,61,79,96,119,120,121,122,123,124,125,126,127,153,171,152] # Need to shuffle these seperately for various reasons
DLCArts = [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187]
GuestArts = [144,145,146,147,148,149]
PonspectorDLCArts = [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]
ShulkMonadoArts = [3,4,5,6,7,8,9,10]
DunbanMonadoArts = [150,151]
MeliaSummonsNames = [205, 207, 209, 217, 221, 223, 225, 231]
ReynGuardShift = [22] # Wont work on other characters

# Setting to make arts all cost tp instead of having cooldowns basically auto attack recharging arts
# Setting to tie arts to weapon https://xenobladedata.github.io/xb1de/bdat/bdat_common/ITM_wpnlist.html#137 
# Setting that randomizes effects of arts

class ActMatch: # A class so that when arts get randomized their animation somewhat matches their effects by changing pc_arts act_idx
    def __init__(self, _pcID, _SingleAttack, _AOEAttack, _Buff, startLv = 1, artSlots = 15):
        self.pcID = _pcID
        self.SingleAttack = _SingleAttack
        self.AOEAttack = _AOEAttack
        self.Buff = _Buff
        self.startLv = startLv
        self.slots = artSlots
        
# Groups for the option to keep arts together
class ArtGroup:
    def __init__(self, _group):
        self.group = _group # Group of name iDS
    def chooseChar(self, charList):
        self.chosenChar = random.choice(charList)
        return self.chosenChar
        


# Setting that just shuffles arts
def RandomizePcArts():
    ShulkActs = ActMatch(1, _SingleAttack=[0,4,8,9,11,12],_AOEAttack=[5,7,15],_Buff=[1,3,2,6,10,13,14])
    ReynActs = ActMatch(2, _SingleAttack=[0,1,4,6,11,12],_AOEAttack=[3,13,15],_Buff=[0,2,5,7,8,9,10,14], artSlots=17)
    FioraActs = ActMatch(3,  _SingleAttack=[3,2,1,0],_AOEAttack=[3,2,1,0],_Buff=[3,2,1,0],startLv=-3, artSlots = 4)
    DunbanActs = ActMatch(4,  _SingleAttack=[0,1,3,5,9,14],_AOEAttack=[12,13,14],_Buff=[2,4,6,7,8,10,11,15])
    SharlaActs = ActMatch(5,  _SingleAttack=[0,1,7,11,14],_AOEAttack=[6,8,15],_Buff=[0,2,3,4,5,6,9,10,12,13], startLv=10)
    RikiActs = ActMatch(6,  _SingleAttack=[1,2,6,11,12,14,15],_AOEAttack=[0,4,6,7,9,10,13,15],_Buff=[0,3,5,8,10,13], startLv=10)
    MeliaActs = ActMatch(7,  _SingleAttack=[4,12],_AOEAttack=[5,14,15],_Buff=[0,1,2,3,6,7,8,9,10,11,13], startLv=10)
    SevenActs = ActMatch(8,  _SingleAttack=[0,2,3,10,11],_AOEAttack=[5,7,8,9,12,15],_Buff=[1,4,6,13,14], startLv=20)
    KinoActs = ActMatch(14,[0],[0],[0], artSlots=0)
    NeneActs = ActMatch(15,[0],[0],[0], artSlots=0)
    GaleSlashGroup = ArtGroup([107,91,89,95])
    StarlightKickGroup = ArtGroup([229,213])
    BoneUpperDiveSobat = ArtGroup([61,63])
    CharacterList:list[ActMatch] = [ShulkActs, ReynActs, FioraActs, DunbanActs, SharlaActs, RikiActs, MeliaActs, SevenActs]
    ArtGroups:list[ArtGroup] = [GaleSlashGroup, StarlightKickGroup, BoneUpperDiveSobat]

    # RemakeArtList()
    
    keepMeliaSummons = Options.PlayerArtsOption_Summons.GetState()
    isArtGroups = Options.PlayerArtsOption_ArtGroups.GetState()
    isPower = Options.PlayerArtsOption_Power.GetState()
    isArts = Options.PlayerArtsOption_Arts.GetState()
    
    editableList = CharacterList.copy()
    
    MeliaWeight(keepMeliaSummons, MeliaActs)
    
    # Dole out the special art groups
    for group in ArtGroups:
        chosen = group.chooseChar(CharacterList)
        chosen.slots = chosen.slots - len(group.group)
        
    invalidArtIds = TalentArts + DunbanMonadoArts + ShulkMonadoArts + PonspectorDLCArts + DLCArts + GuestArts
    
    
        
    with open("./XCDE/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        if isArts:
            for art in artData["rows"]:
        
                if art["$id"] in invalidArtIds: # Ignores invalid/ weird arts
                    continue
                
                if keepMeliaSummons and (art["name"] in MeliaSummonsNames): # Dont change the melias summons if we want her to keep em
                    continue
                
                # Random choice
                if editableList == []: # Renew the list if empty
                    editableList = CharacterList.copy()
                    
                if not ArtGroupManager(isArtGroups, art, ArtGroups):
                    char = random.choice(editableList)

                    char.slots = char.slots-1
                    if char.slots <= 0:
                        editableList.remove(char)
                    
                    AssignArt(art, char)

            BalanceArtUnlockLevels(artData, CharacterList)
            MatchArtBooks(artData)
            FixSharlasNewArts(art, SharlaActs, KinoActs)
            
        if isPower:
            for art in artData["rows"]:
                Power(art)


        scripts.JSONParser.CloseFile(artData, artFile)


def MeliaWeight(keepMeliaSummons, MeliaActs):
    if keepMeliaSummons: # If melia keeps her summons we reduce her slots
        MeliaActs.slots = 7
    else:
        MeliaActs.slots = 15

def ArtGroupManager(isArtGroups, art, ArtGroups):
    if isArtGroups:
        for artGroup in ArtGroups: # Ensures theres exists one set of grouped arts staying grouped
            if art["name"] in artGroup.group:
                AssignArt(art, artGroup.chosenChar)
                return True
    else:
        return False

def FixSharlasNewArts(art, SharlaActs, KinoActs): # Fixes the talent gauge working with her new arts
    if art["pc"] in [SharlaActs.pcID, KinoActs.pcID]: # Ensures former healer's new arts still increment the cooldown talent art
        art["tp"] = random.randrange(-25,-1)
    elif art["tp"] < 0: # If healer arts go on someone else it shouldnt buff their talent gauge
        art["tp"] = 0

def BalanceArtUnlockLevels(artData, CharacterList):
    for char in CharacterList: # Loop through the characters
        unlockLv = char.startLv - 3 # Starting level to unlock arts
        stepLv = [2,3,4,5,6] # How many levels for the next unlock 
        # print(char.pcID)
        count = 0
        for art in artData["rows"]:
            if art["$id"] in ShulkMonadoArts + TalentArts + DunbanMonadoArts + PonspectorDLCArts + DLCArts + GuestArts:
                continue
            if art["pc"] == char.pcID: # Find arts for a character
                count = count + 1
                getlv = min(max(unlockLv,0),80) # Max to frontload the arts a little bit so you get them early
                # print(f"ID: {art["$id"]} Lv: {getlv}")
                art["get_lv"] = getlv
                art["get_type"] = 1
                unlockLv += random.choice(stepLv)
        # print(f"Total: {count}\n")

def Mult(art, keys = [], mults = [60,180], rollOnce = False, maxVal = 255):
        mult = random.choice(mults)/100
        for key in keys:
            # print(key)
            # print(f"old: {art[key]}")
            art[key] = min(int(art[key] * mult),maxVal)
            # print(f"new: {art[key]}")
            # print("\n")
            # If we want seperate mult rolls for each
            if not rollOnce:
                mult = random.choice(mults)



def Power(art):
    
    Mult(art,["grow_powl", "grow_powh"], rollOnce=True)
    
    Mult(art,["rate1", "rate2"], [70,180], True, 4095)
    
    Mult(art,["st_time"], [70,140], maxVal=2047)
    Mult(art,["grow_st_time"])
    
    Mult(art,["sp_val2"])
    
    Mult(art,["st_val", "st_val2"], [50, 250])
    Mult(art,["grow_st_val"],[50,220])
    
    Mult(art,["tp"], [40,100], maxVal=127)
    
    Mult(art,["recast"], [80,120], True)
    Mult(art,["glow_recast"], [80,120], True, 31)
    
    
# Fixes art books
def MatchArtBooks(artData):
    with open("./XCDE/JsonOutputs/bdat_common/ITM_artslist.json", 'r+', encoding='utf-8') as artBookFile:
        artBookData = json.load(artBookFile)
        for book in artBookData["rows"]:
            for art in artData["rows"]:
                if art["$id"] == book["get_arts"]:
                    book["pc_type"] = art["pc"]
                    break
    # with open("./XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itemFile: currently dont care enough to rename the names in the descriptions
    #     with open("./XCDE/JsonOutputs/bdat_menu_item/MNU_item_mes_b.json", 'r+', encoding='utf-8') as artDescFile:
    #         with open("./XCDE/JsonOutputs/bdat_common/ITM_artslist.json", 'r+', encoding='utf-8') as artsListFile:
    #             itemData = json.load(itemFile)
    #             for art in artsListFile["rows"]:
                
            
                
def AssignArt(art, char:ActMatch):
    if art["pc"] == char.pcID: # If they get a vanilla art dont change the act no
        return
    
    art["pc"] = char.pcID
    
    if art["tgt"] in [2,3] or art["atk_type"] in [3]:
        art["act_idx"] = random.choice(char.Buff)
    elif art["range_type"] == 0:
        art["act_idx"] = random.choice(char.SingleAttack)
    else:
        art["act_idx"] = random.choice(char.AOEAttack)      
        


def ArtsDescriptions():
    ArtDesc = scripts.PopupDescriptions.Description()
    ArtDesc.Header(Options.PlayerArtsOption_Arts.name)
    ArtDesc.Text("Randomizes what character gets an art. Generally each character will have their vanilla total number of arts.\nThis doesn't include talent arts")
    ArtDesc.Header(Options.PlayerArtsOption_Power.name)
    ArtDesc.Text("Randomizes the strength of various aspects of arts and their level ups")
    ArtDesc.Image("spiritBreath.png", "XCDE", 600)
    # ArtDesc.Header(Options.PlayerArtsOption_BalancedUnlockLevels.name)
    # ArtDesc.Text("Ensures that your arts unlock consistently as your level up.\nOtherwise your might get really high levels arts and be stuck with nothing for most of the game.\nOn average your will unlock a new art every 2-3 levels.")
    ArtDesc.Header(Options.PlayerArtsOption_ArtGroups.name)
    ArtDesc.Text("Keep arts that have combos randomized to the same character.")
    ArtDesc.Tag("Gale Slash, Worldly Slash, Electric Gutbuster, Tempest Kick", pady=3, anchor="center")
    ArtDesc.Tag("Spear Break, Starlight Kick", pady=3, anchor="center")
    ArtDesc.Header(Options.PlayerArtsOption_Summons.name)
    ArtDesc.Text("Keeps Melia's summon arts on her, so that her talent art is not useless.")
    ArtDesc.Tag("Summon Wind, Summon Earth, Summon Ice, Summon Aqua, Summon Flare, Summon Bolt, Summon Copy and Power Effect", pady=3, anchor="center")
    # ArtDesc.Header(Options.PlayerArtsOption_Cooldown.name)
    # ArtDesc.Text(f"Chooses a random cooldown between {CooldownStartRange[0]}-{CooldownStartRange[1]}s then each level up reduces that cooldown by the original cooldown / {CooldownStepRange[0]}-{CooldownStepRange[1]}")
    return ArtDesc





# def namePrint(artList):
#     with open("./XCDE/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
#         artData = json.load(artFile)
#         nameList = []
#         for art in artData["rows"]:
#             if art["$id"] in artList:
#                 nameList.append(art["name"])
#         print(nameList)

# def RemakeArtList():    
#     with open("./XCDE/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
#         artData = json.load(artFile)
#         # isDupes = Options.PlayerArtsOption_Duplicates.GetState()
#         artList = []
#         keyList = ["name", "pc", "cast", "recast", "tp", "dex", "rate1", "rate2", "arts_type", "atk_type", "chain_type", "elem", "dmg_type", "dmg_time", "tgt", "range_type", "range", "range_val", "hate", "flag", "st_type", "st_val", "st_val2", "st_time", "st_itv", "sp_cnd", "sp_proc", "sp_val1", "sp_val2", "kb_type", "kb_lv", "grow_powl", "grow_powh", "grow_st_time", "grow_st_val", "glow_recast", "icon", "icon_base", "act_idx", "idx", "list_idx", "get_type", "get_lv", "melia_lv", "melia_slot_idx", "help"]
        
#         badReplacementArts = PonspectorDLCArts + GuestArts + DunbanMonadoArts + TalentArts + DLCArts
#         for art in artData["rows"]: # Build our list
#             if art["$id"] in badReplacementArts:
#                 continue
#             artList.append(art)
        
#         badReplacedArts =  PonspectorDLCArts + GuestArts + DunbanMonadoArts + TalentArts + DLCArts
#         for art in artData["rows"]: # Replace the old list with random choices from the new list
#             if art["$id"] in badReplacedArts:
#                 continue
            
#             newArt = random.choice(artList) # Choose a new art for that slot
#             # if isDupes:
#             #     artList.remove(newArt)
            
#             for key in keyList: # Replace everything
#                 art[key] = newArt[key]
#         scripts.JSONParser.CloseFile(artData, artFile)
        
        
#         # Edit the new data
