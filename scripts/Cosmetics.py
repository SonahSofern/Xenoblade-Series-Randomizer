import json, random, IDs


class Cosmetic:
    def __init__(self, model: str, characterID: int, characterName:str):
        self.model = model
        self.characterID = characterID
        self.characterName = characterName
        
# Character Numbers
Rex = "Rex"
Nia = "Nia"
Tora = "Tora"
Morag = "Morag"
Zeke = "Zeke"
Pyra = "Pyra"
Mythra = "Mythra"
Dromarch = "Dromarch"
Poppiα = "Poppiα"
PoppiQT = "PoppiQT"
PoppiQTπ = "PoppiQTπ"
Brighid = "Brighid"
Pandoria = "Pandoria"

# Blades
JadeOrchidBrighid = Cosmetic("bl/bl121001", 1009, Brighid)
WaterLilyBrighid = Cosmetic("bl/bl111001", 1009, Brighid)
CrimsonOrchidBrighid = Cosmetic("bl/bl101001", 1009, Brighid)
DefaultBrighid = Cosmetic("bl/bl001001", 1009, Brighid)

MagicalPinkPandoria = Cosmetic("bl/bl120901", 1010, Pandoria)
MermaidBluePandoria = Cosmetic("bl/bl100901", 1010, Pandoria)
BeachDatePandoria = Cosmetic("bl/bl110901", 1010, Pandoria)
DefaultPandoria = Cosmetic("bl/bl000901", 1010, Pandoria)
ClearGlassesPandoria = Cosmetic("bl/bl000902", 1010, Pandoria)

ObsidianDromarch = Cosmetic("bl/bl120501", 1004, Dromarch)
SavageDromarch = Cosmetic("bl/bl100501", 1004, Dromarch)
DefaultDromarch = Cosmetic("bl/bl000501", 1004, Dromarch)

DevotedMarigoldNia = Cosmetic("bl/bl120403", 1011, Nia)
SincerePrimroseNia = Cosmetic("bl/bl120402", 1011, Nia)
LoyalBellflowerNia = Cosmetic("bl/bl120401", 1011, Nia)
DefaultBladeNia = Cosmetic("bl/bl000401", 1011, Nia)

CarbonMythra = Cosmetic("bl/bl120201", 1002, Mythra)
RadiantBeachMythra = Cosmetic("bl/bl110201", 1002, Mythra)
PyraStyleMythra = Cosmetic("bl/bl100201", 1002, Mythra)
DefaultMythra = Cosmetic("bl/bl000201", 1002, Mythra)

MythraStylePyra = Cosmetic("bl/bl100102", 1001, Pyra)
DisguisedPyra = Cosmetic("bl/bl100101", 1001, Pyra)
BlueSkyPyra = Cosmetic("bl/bl120101", 1001, Pyra)
ProSwimmerPyra = Cosmetic("bl/bl110101", 1001, Pyra)
DefaultPyra = Cosmetic("bl/bl000101", 1001, Pyra)

DefaultPoppiα = Cosmetic("bl/bl000601", 1005, Poppiα)
CornflowerPoppiα = Cosmetic("bl/bl120601", 1005, Poppiα)
SwimLessonPoppiα = Cosmetic("bl/bl110601", 1005, Poppiα)

DefaultPoppiQT = Cosmetic("bl/bl000701", 1006, PoppiQT)
AntiquePrincessPoppiQT = Cosmetic("bl/bl120701", 1006, PoppiQT)

DefaultPoppiQTπ = Cosmetic("bl/bl000801", 1007, PoppiQTπ)
NanoOrangeQTπ = Cosmetic("bl/bl120801", 1007, PoppiQTπ)

# Drivers
CloudSeaKingRex = Cosmetic("pc/pc120101", 1, Rex)
CloudSeaSharkRex = Cosmetic("pc/pc110101", 1, Rex)
PrototypeSuitRex = Cosmetic("pc/pc100101", 1, Rex)
MasterDriverRex = Cosmetic("pc/pc000103", 1, Rex)
HelmetedRex = Cosmetic("pc/pc000102", 1, Rex)
DefaultRex = Cosmetic("pc/pc000101", 1, Rex)

ObligatoryLeaveMorag = Cosmetic("pc/pc110601", 6, Morag)
DressUniformMorag = Cosmetic("pc/pc100601", 6, Morag)
ScarletInquisitorMorag = Cosmetic("pc/pc120601", 6, Morag)
DefaultMorag = Cosmetic("pc/pc000601", 6, Morag)

SurfinatorZeke = Cosmetic("pc/pc110501", 3, Zeke)
EmbercakeZeke = Cosmetic("pc/pc100501", 3, Zeke)
ShiningJusticeZeke = Cosmetic("pc/pc120501", 3, Zeke)
DefaultZeke = Cosmetic("pc/pc000501", 3, Zeke)
HoodedZeke = Cosmetic("pc/pc000502", 3, Zeke)

BestGirlFanTora = Cosmetic("pc/pc110301", 4, Tora)
BusterModeTora = Cosmetic("pc/pc100301", 4, Tora)
SkullfacePunkTora = Cosmetic("pc/pc120301", 4, Tora)
DefaultTora = Cosmetic("pc/pc000301", 4, Tora)

FancySundressNia = Cosmetic("pc/pc110201", 2, Nia)
CandyStripeNia = Cosmetic("pc/pc100201", 2, Nia)
BloodWitchNia = Cosmetic("pc/pc120201", 2, Nia)
DefaultDriverNia = Cosmetic("pc/pc000201", 2, Nia)



# Drivers
RexCosmetics = [
    "Master Driver Rex", 
    [lambda: IDs.ValidDriverCosmetics.append(MasterDriverRex)],
    "Cloud Sea King Rex", 
    [lambda: IDs.ValidDriverCosmetics.append(CloudSeaKingRex)],
    "Cloud Sea Shark Rex", 
    [lambda: IDs.ValidDriverCosmetics.append(CloudSeaSharkRex)],
    "Prototype Suit Rex", 
    [lambda: IDs.ValidDriverCosmetics.append(PrototypeSuitRex)],
    "Helmeted Rex", 
    [lambda: IDs.ValidDriverCosmetics.append(HelmetedRex)],
]

NiaDriverCosmetics = [
    "Blood Witch Nia", 
    [lambda: IDs.ValidDriverCosmetics.append(BloodWitchNia)],
    "Candy Stripe Nia", 
    [lambda: IDs.ValidDriverCosmetics.append(CandyStripeNia)],
    "Fancy Sundress Nia", 
    [lambda: IDs.ValidDriverCosmetics.append(FancySundressNia)],
]

ToraCosmetics = [
    "Buster Mode Tora", 
    [lambda: IDs.ValidDriverCosmetics.append(BusterModeTora)],
    "Skullface Punk Tora", 
    [lambda: IDs.ValidDriverCosmetics.append(SkullfacePunkTora)],
    "Best Girl Fan Tora", 
    [lambda: IDs.ValidDriverCosmetics.append(BestGirlFanTora)],
]

MoragCosmetics = [
    "Dress Uniform Morag", 
    [lambda: IDs.ValidDriverCosmetics.append(DressUniformMorag)],
    "Scarlet Inquisitor Morag", 
    [lambda: IDs.ValidDriverCosmetics.append(ScarletInquisitorMorag)],
    "Obligatory Leave Morag", 
    [lambda: IDs.ValidDriverCosmetics.append(ObligatoryLeaveMorag)],
]

ZekeCosmetics = [
    "Shining Justice Zeke", 
    [lambda: IDs.ValidDriverCosmetics.append(ShiningJusticeZeke)],
    "Embercake Zeke", 
    [lambda: IDs.ValidDriverCosmetics.append(EmbercakeZeke)],
    "Surfinator Zeke", 
    [lambda: IDs.ValidDriverCosmetics.append(SurfinatorZeke)],
]

# Blades
PyraCosmetics = [
    "Blue Sky Pyra", 
    [lambda: IDs.ValidBladeCosmetics.append(BlueSkyPyra)],
    "Disguised Pyra", 
    [lambda: IDs.ValidBladeCosmetics.append(DisguisedPyra)],
    "Mythra Style Pyra", 
    [lambda: IDs.ValidBladeCosmetics.append(MythraStylePyra)],
    "Pro Swimmer Pyra", 
    [lambda: IDs.ValidBladeCosmetics.append(ProSwimmerPyra)],
]

MythraCosmetics = [
    "Carbon Mythra", 
    [lambda: IDs.ValidBladeCosmetics.append(CarbonMythra)],
    "Pyra Style Mythra", 
    [lambda: IDs.ValidBladeCosmetics.append(PyraStyleMythra)],
    "Radiant Beach Mythra", 
    [lambda: IDs.ValidBladeCosmetics.append(RadiantBeachMythra)],
]

DromarchCosmetics = [
    "Obsidian Dromarch", 
    [lambda: IDs.ValidBladeCosmetics.append(ObsidianDromarch)],
    "Savage Dromarch", 
    [lambda: IDs.ValidBladeCosmetics.append(SavageDromarch)],
]

BrighidCosmetics = [
    "Jade Orchid Brighid", 
    [lambda: IDs.ValidBladeCosmetics.append(JadeOrchidBrighid)],
    "Crimson Orchid Brighid", 
    [lambda: IDs.ValidBladeCosmetics.append(CrimsonOrchidBrighid)],
    "Water Lily Brighid", 
    [lambda: IDs.ValidBladeCosmetics.append(WaterLilyBrighid)],
]

PandoriaCosmetics = [
    "Magical Pink Pandoria", 
    [lambda: IDs.ValidBladeCosmetics.append(MagicalPinkPandoria)],
    "Mermaid Blue Pandoria", 
    [lambda: IDs.ValidBladeCosmetics.append(MermaidBluePandoria)],
    "Beach Date Pandoria", 
    [lambda: IDs.ValidBladeCosmetics.append(BeachDatePandoria)],
    "Clear Glasses Pandoria", 
    [lambda: IDs.ValidBladeCosmetics.append(ClearGlassesPandoria)],
]

NiaBladeCosmetics = [
    "Devoted Marigold Nia", 
    [lambda: IDs.ValidBladeCosmetics.append(DevotedMarigoldNia)],
    "Sincere Primrose Nia", 
    [lambda: IDs.ValidBladeCosmetics.append(SincerePrimroseNia)],
    "Loyal Bellflower Nia", 
    [lambda: IDs.ValidBladeCosmetics.append(LoyalBellflowerNia)],
]

PoppiαCosmetics = [
    "Cornflower Poppiα", 
    [lambda: IDs.ValidArtificialBladeCosmetics.append(CornflowerPoppiα)],
    "Swim Lesson Poppiα", 
    [lambda: IDs.ValidArtificialBladeCosmetics.append(SwimLessonPoppiα)],
]

PoppiQTCosmetics = [
    "Antique Princess PoppiQT", 
    [lambda: IDs.ValidArtificialBladeCosmetics.append(AntiquePrincessPoppiQT)],
]

PoppiQTπCosmetics = [
    "Nano Orange QTπ", 
    [lambda: IDs.ValidArtificialBladeCosmetics.append(NanoOrangeQTπ)],
]


def CosmeticPairs(nameData, itmData,odds, charKeyWord, cosmeticsList):
    pairs = {}
    for Acc in itmData["rows"]:
        if (odds > random.randint(0,99)):
            cosm:Cosmetic = random.choice(cosmeticsList)
            
            # Keep pairing since we cant make more names
            if Acc["Name"] in pairs:
                cosm = pairs[Acc["Name"]]["cosm"]
            else:
                pairs[Acc["Name"]] = {"cosm": cosm}
            
            
            for _Acc in nameData["rows"]:
                if _Acc["$id"] == Acc["Name"]:
                    oldName = _Acc["name"]
                    oldNameList = oldName.split()
                    firstWord = oldNameList[0]
                    _Acc["name"] = f"{firstWord} {cosm.characterName}"  
                    print(_Acc["name"])
                    break
                
            Acc["Model"] = cosm.model
            Acc[f"{charKeyWord}"] = cosm.characterID
            
def Cosmetics(optionDict):
    # Slider
    odds = optionDict["Character Outfits"]["spinBoxVal"].get()
    
    # Drivers
    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as file:
        with open("./_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as nameFile:  
            eqData = json.load(file)
            accNameData = json.load(nameFile)
            
            CosmeticPairs(accNameData, eqData, odds, "Driver", IDs.ValidDriverCosmetics)
            
            nameFile.seek(0)
            nameFile.truncate()
            json.dump(accNameData, nameFile, indent=2, ensure_ascii=False)
        file.seek(0)
        file.truncate()
        json.dump(eqData, file, indent=2, ensure_ascii=False)
        
    # Blades
    with open("./_internal/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as orbFile:
        with open("./_internal/JsonOutputs/common_ms/itm_orb.json", 'r+', encoding='utf-8') as nameFile:
            orbData = json.load(orbFile)
            nameData = json.load(nameFile)
            
            CosmeticPairs(nameData,orbData,odds,"Blade", IDs.ValidBladeCosmetics)
            
            nameFile.seek(0)
            nameFile.truncate()
            json.dump(nameData, nameFile, indent=2, ensure_ascii=False)
        orbFile.seek(0)
        orbFile.truncate()
        json.dump(orbData, orbFile, indent=2, ensure_ascii=False)
        
    # ArtificialBlades 
    with open("./_internal/JsonOutputs/common/ITM_HanaAssist.json", 'r+', encoding='utf-8') as file:
        eqData = json.load(file)
        for Acc in eqData["rows"]:
            if (odds > random.randint(0,99)):
                cosm:Cosmetic = random.choice(IDs.ValidArtificialBladeCosmetics) # these names are shared with regular ones so its not going to work to put poppi names on them when most cant equip those anyway
                Acc["Model"] = cosm.model
                Acc["Blade"] = cosm.characterID
        file.seek(0)
        file.truncate()
        json.dump(eqData, file, indent=2, ensure_ascii=False)
        
    # Clear globals
    IDs.ValidDriverCosmetics.clear()
    IDs.ValidBladeCosmetics.clear()
    IDs.ValidArtificialBladeCosmetics.clear()
