import json, random, IDs


#Blades
JadeOrchidBrighid = "bl/bl121001"
WaterLilyBrighid = "bl/bl111001"
CrimsonOrchidBrighid = "bl/bl101001"
DefaultBrighid = "bl/bl001001"
MagicalPinkPandoria = "bl/bl120901"
MermaidBluePandoria = "bl/bl100901"
BeachDatePandoria = "bl/bl110901"
DefaultPandoria = "bl/bl000901"
ClearGlassesPandoria = "bl/bl000902"
ObsidianDromarch = "bl/bl120501"
SavageDromarch = "bl/bl100501"
DefaultDromarch = "bl/bl000501"
DevotedMarigoldNia = "bl/bl120403"
SincerePrimroseNia = "bl/bl120402"
LoyalBellflowerNia = "bl/bl120401"
DefaultBladeNia = "bl/bl000401"
CarbonMythra = "bl/bl120201"
RadiantBeachMythra = "bl/bl110201"
PyraStyleMythra = "bl/bl100201"
DefaultMythra = "bl/bl000201"
# Cant find Massive Melee Mythra bl/bl value
MythraStylePyra = "bl/bl100102"
DisguisedPyra = "bl/bl100101"
BlueSkyPyra = "bl/bl120101"
ProSwimmerPyra = "bl/bl110101"
DefaultPyra = "bl/bl000101"
DefaultPoppiα = "bl/bl000601"
CornflowerPoppiα = "bl/bl120601"
SwimLessonPoppiα = "bl/bl110601"
DefaultPoppiQT = "bl/bl000701"
AntiquePrincessPoppiQT = "bl/bl120701"
DefaultPoppiQTπ = "bl/bl000801"
NanoOrangeQTπ = "bl/bl120801"

#Drivers
CloudSeaKingRex = "pc/pc120101"
CloudSeaSharkRex = "pc/pc110101"
PrototypeSuitRex = "pc/pc100101"
MasterDriverRex = "pc/pc000103"
HelmetedRex = "pc/pc000102"
DefaultRex = "pc/pc000101"
ObligatoryLeaveMorag = "pc/pc110601"
DressUniformMorag = "pc/pc100601"
ScarletInquisitorMorag = "pc/pc120601"
DefaultMorag = "pc/pc000601"
SurfinatorZeke = "pc/pc110501"
EmbercakeZeke = "pc/pc100501"
ShiningJusticeZeke = "pc/pc120501"
DefaultZeke = "pc/pc000501"
HoodedZeke = "pc/pc000502"
BestGirlFanTora = "pc/pc110301"
BusterModeTora = "pc/pc100301"
SkullfacePunkTora = "pc/pc120301"
DefaultTora = "pc/pc000301"
FancySundressNia = "pc/pc110201"
CandyStripeNia = "pc/pc100201"
BloodWitchNia = "pc/pc120201"
DefaultDriverNia  = "pc/pc000201"

# Character Numbers
Rex = 1
NiaDriver = 2
Tora = 4
Morag = 6
Zeke = 3
Pyra = 1001
Mythra = 1002
Dromarch = 1004
Poppiα = 1005
PoppiQT = 1006
PoppiQTπ = 1007
Brighid = 1009
Pandoria = 1010
NiaBlade = 1011


# Drivers
RexCosmetics = [
    "Master Driver Rex", [lambda: IDs.ValidDriverCosmetics.append([MasterDriverRex, Rex])],
    "Cloud Sea King Rex", [lambda: IDs.ValidDriverCosmetics.append([CloudSeaKingRex, Rex])],
    "Cloud Sea Shark Rex", [lambda: IDs.ValidDriverCosmetics.append([CloudSeaSharkRex, Rex])],
    "Prototype Suit Rex", [lambda: IDs.ValidDriverCosmetics.append([PrototypeSuitRex, Rex])],
    "Helmeted Rex", [lambda: IDs.ValidDriverCosmetics.append([HelmetedRex, Rex])],
]

NiaDriverCosmetics = [
    "Blood Witch Nia", [lambda: IDs.ValidDriverCosmetics.append([BloodWitchNia, NiaDriver])],
    "Candy Stripe Nia", [lambda: IDs.ValidDriverCosmetics.append([CandyStripeNia, NiaDriver])],
    "Fancy Sundress Nia", [lambda: IDs.ValidDriverCosmetics.append([FancySundressNia, NiaDriver])],
]

ToraCosmetics = [
    "Buster Mode Tora", [lambda: IDs.ValidDriverCosmetics.append([BusterModeTora, Tora])],
    "Skullface Punk Tora", [lambda: IDs.ValidDriverCosmetics.append([SkullfacePunkTora, Tora])],
    "Best Girlfan Tora", [lambda: IDs.ValidDriverCosmetics.append([BestGirlFanTora, Tora])],
]

MoragCosmetics = [
    "Dress Uniform Morag", [lambda: IDs.ValidDriverCosmetics.append([DressUniformMorag, Morag])],
    "Scarlet Inquisitor Morag", [lambda: IDs.ValidDriverCosmetics.append([ScarletInquisitorMorag, Morag])],
    "Obligatory Leave Morag", [lambda: IDs.ValidDriverCosmetics.append([ObligatoryLeaveMorag, Morag])],
]

ZekeCosmetics = [
    "Shining Justice Zeke", [lambda: IDs.ValidDriverCosmetics.append([ShiningJusticeZeke, Zeke])],
    "Embercake Zeke", [lambda: IDs.ValidDriverCosmetics.append([EmbercakeZeke, Zeke])],
    "Surfinator Zeke", [lambda: IDs.ValidDriverCosmetics.append([SurfinatorZeke, Zeke])],
]

# Blades
PyraCosmetics = [
    "Blue Sky Pyra", [lambda: IDs.ValidBladeCosmetics.append([BlueSkyPyra, Pyra])],
    "Disguised Pyra", [lambda: IDs.ValidBladeCosmetics.append([DisguisedPyra, Pyra])],
    "Mythra-Style-Pyra", [lambda: IDs.ValidBladeCosmetics.append([MythraStylePyra, Pyra])],
    "Pro Swimmer Pyra", [lambda: IDs.ValidBladeCosmetics.append([ProSwimmerPyra, Pyra])],
]

MythraCosmetics = [
    "Carbon Mythra", [lambda: IDs.ValidBladeCosmetics.append([CarbonMythra, Mythra])],
    "Pyra-Style-Mythra", [lambda: IDs.ValidBladeCosmetics.append([PyraStyleMythra, Mythra])],
    "Radiant Beach Mythra", [lambda: IDs.ValidBladeCosmetics.append([RadiantBeachMythra, Mythra])],
]

DromarchCosmetics = [
    "Obsidian Dromarch", [lambda: IDs.ValidBladeCosmetics.append([ObsidianDromarch, Dromarch])],
    "Savage Dromarch", [lambda: IDs.ValidBladeCosmetics.append([SavageDromarch, Dromarch])],
]

BrighidCosmetics = [
    "Jade Orchid Brighid", [lambda: IDs.ValidBladeCosmetics.append([JadeOrchidBrighid, Brighid])],
    "Crimson Orchid Brighid", [lambda: IDs.ValidBladeCosmetics.append([CrimsonOrchidBrighid, Brighid])],
    "Water Lily Brighid", [lambda: IDs.ValidBladeCosmetics.append([WaterLilyBrighid, Brighid])],
]

PandoriaCosmetics = [
    "Magical Pink Pandoria", [lambda: IDs.ValidBladeCosmetics.append([MagicalPinkPandoria, Pandoria])],
    "Mermaid Blue Pandoria", [lambda: IDs.ValidBladeCosmetics.append([MermaidBluePandoria, Pandoria])],
    "Beach Date Pandoria", [lambda: IDs.ValidBladeCosmetics.append([BeachDatePandoria, Pandoria])],
]

NiaBladeCosmetics = [
    "Devoted Marigold Nia", [lambda: IDs.ValidBladeCosmetics.append([DevotedMarigoldNia, NiaBlade])],
    "Sincere Primrose Nia", [lambda: IDs.ValidBladeCosmetics.append([SincerePrimroseNia, NiaBlade])],
    "Loyal Bellflower Nia", [lambda: IDs.ValidBladeCosmetics.append([LoyalBellflowerNia, NiaBlade])],
]

PoppiαCosmetics = [
    "Cornflower Poppi α", [lambda: IDs.ValidArtificialBladeCosmetics.append([CornflowerPoppiα, Poppiα])],
    "Swim Lesson Poppi α", [lambda: IDs.ValidArtificialBladeCosmetics.append([SwimLessonPoppiα, Poppiα])],
]

PoppiQTCosmetics = [
    "Antique Princess QT", [lambda: IDs.ValidArtificialBladeCosmetics.append([AntiquePrincessPoppiQT, PoppiQT])],
]

PoppiQTπCosmetics = [
    "Nano Orange QTπ", [lambda: IDs.ValidArtificialBladeCosmetics.append([NanoOrangeQTπ, PoppiQTπ])],
]

def Cosmetics():
    #Drivers
    with open("./_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            choice = random.choice(IDs.ValidDriverCosmetics)
            row["Model"] = choice[0]
            row["Driver"] = choice[1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    #Blades
    with open("./_internal/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            choice = random.choice(IDs.ValidBladeCosmetics)
            row["Model"] = choice[0]
            row["Blade"] = choice[1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    #ArtificialBlades
    with open("./_internal/JsonOutputs/common/ITM_HanaAssist.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            choice = random.choice(IDs.ValidArtificialBladeCosmetics)
            row["Model"] = choice[0]
            row["Blade"] = choice[1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    IDs.ValidDriverCosmetics.clear()
    IDs.ValidBladeCosmetics.clear()
    IDs.ValidArtificialBladeCosmetics.clear()
