import json, random
from scripts import Interactables

Env = 1 # Environment Themes
Cut = 2 # Cutscene Themes
Battle = 3 # Battle Themes
Boss = 4 # Boss Theme
Jingle = 5 # Jingles

Good = "Good"
Bad = "Bad"

AllEnvironmentThemes = []
AllCutsceneThemes = []
AllBattleThemes = []
AllBossThemes = []
AllJingles = []

UsedEnvironmentThemes = []
UsedCutsceneThemes = []
UsedBattleThemes = []
UsedBossThemes = []
UsedJingles = []

class Music:
    def __init__(self,_song, _fileName, _type = [], _isGood = Good):
        self.songName = _song
        self.fileName = _fileName   
        self.isGood = _isGood
        self.type = _type
        
        # Create the entire lists
        if Env in self.type:
            AllEnvironmentThemes.append(self)
        if Cut in self.type:
            AllCutsceneThemes.append(self)
        if Battle in self.type:
            AllBattleThemes.append(self)
        if Boss in self.type:
            AllBossThemes.append(self)
        if Jingle in self.type:
            AllJingles.append(self) 
            
    def CreateOption(self, parent, list):
        if self.isGood:
            defState = True
        else:
            defState = False
        Interactables.SubOption(self.songName, parent, [lambda: list.append(self)],_defState=defState)


def MusicRando(Songs:list[Music], TempList:list[Music]):
    with open("./XCDE/JsonOutputs/bdat_common/bgmlist.json", 'r+', encoding='utf-8') as bgmFile:
        bgmData = json.load(bgmFile)
            
        for bgm in bgmData["rows"]:
            name = bgm["file_name"]
            if any(song.fileName == name for song in Songs):
                bgm["file_name"] = random.choice(TempList).fileName
                
        bgmFile.seek(0)
        bgmFile.truncate()
        json.dump(bgmData, bgmFile, indent=2, ensure_ascii=False)
    # print(list(x.songName for x in UsedBossThemes))
    TempList.clear()


# Environment Themes
Hometown = Music("Hometown", "f01_loop", [Env])
Colony9 = Music("Colony 9", "f02_loop", [Env])
TephraCave = Music("Tephra Cave", "f03_loop", [Env])
GaurPlain = Music("Gaur Plain", "f04_loop", [Env])
Colony6EtherMine = Music("Colony 6 Ether Mine", "f05_loop", [Env])
SatorlMarsh = Music("Satorl Marsh", "f06_loop", [Env])
ForestOfTheNopon = Music("Forest Of The Nopon", "f07_loop", [Env])
FrontierVillage = Music("Frontier Village", "f08_loop", [Env])
WhereTheAncestorsSleep = Music("Where The Ancestors Sleep", "f10_loop", [Env])
ErythSea = Music("Eryth Sea", "f11_loop", [Env])
AlcamothImperialCapital = Music("Alcamoth Imperial Capital", "f12_loop", [Env])
PrisonIsland = Music("Prison Island", "f13_loop", [Env])
ValakMountain = Music("Valak Mountain", "f14_loop", [Env])
SwordValley = Music("Sword Valley", "f15_loop", [Env])
GalahadFortress = Music("Galahad Fortress", "f16_loop", [Env])
TheFallenLand = Music("The Fallen Land", "f17_loop", [Env])
HiddenMachinaVillage = Music("Hidden Machina Village", "f18_loop", [Env])
MechonisField = Music("Mechonis Field", "f19_loop", [Env])
AgnirathaMechonisCapital = Music("Agniratha Mechonis Capital", "f20_loop", [Env])
CentralFactory = Music("Central Factory", "f21_loop", [Env])
BionisInteriorCarcass = Music("Bionis Interior Carcass", "f22_loop", [Env])
Colony6Rebuilding = Music("Colony 6 Rebuilding", "f23_loop", [Env])
MemorysEnd = Music("Memorys End", "f24_loop", [Env])
InTheRefugeeCamp = Music("In The Refugee Camp", "f25_loop", [Env])
TheEndLiesAhead = Music("The End Lies Ahead", "f26_loop", [Env])
GranDellFC = Music("Gran Dell FC", "f51_loop", [Env])
BionisShoulderFC = Music("Bionis Shoulder FC", "f52_loop", [Env])

# Battle Themes
TimeToFight = Music("Time To Fight!", "b01_loop", [Battle])
MechanicalRhythm = Music("Mechanical Rhythm", "b03_loop", [Battle])
TimeToFightBionisShoulder = Music("Time To Fight! Bionis Shoulder", "b51_loop", [Battle])
Fogbeasts = Music("Fogbeasts", "b52_loop", [Battle])
EnemiesClosingIn = Music("Enemies Closing In", "b08_loop", [Battle], Bad)
SearchingGlance = Music("Searching Glance", "b10_loop", [Battle], Bad)
IrregularBound = Music("Irregular Bound", "b11_loop", [Battle], Bad)
ZanzasWorld = Music("Zanzas World", "b12_loop", [Battle], Bad)
VisionsOfTheFuture = Music("Visions Of The Future", "b09_loop", [Battle], Bad)

# Boss Themes
AnObstacleInOurPath = Music("An Obstacle In Our Path", "b05_loop", [Boss])
YouWillKnowOurNames = Music("You Will Know Our Names", "b02_loop", [Boss])
ZanzaTheDivine = Music("Zanza The Divine", "b06_loop", [Boss])
ATragicDecision = Music("A Tragic Decision", "b15_loop", [Boss])
RoarFromBeyond = Music("Roar From Beyond", "b53_loop", [Boss])
UnfinishedBusiness = Music("Unfinished Business", "e03", [Boss])
TheGodSlayingSword = Music("The God Slaying Sword", "b07_loop", [Boss])
EngageTheEnemy = Music("Engage The Enemy", "e04", [Boss])

# Jingles
CollectopediaLineCompleted = Music("Collectopedia Line Completed", "j01", [Jingle])
CollectopediaPageCompleted = Music("Collectopedia Page Completed", "j02", [Jingle])
NewObjectiveReceived = Music("New Objective Received", "j03", [Jingle])
NewAreaFound = Music("New Area Found", "j04", [Jingle])
SecretAreaFound = Music("Secret Area Found", "j05", [Jingle])

# Cutscene Themes
PrologueA = Music("Prologue A", "e01_a", [Cut])
PrologueB = Music("Prologue B", "e01_b", [Cut])
# MainTheme = Music("Main Theme", "e02", [Cut])
MainThemeLoop = Music("Main Theme", "e02_loop", [Cut])
BionisAwakening = Music("Bionis Awakening", "e05", [Cut])
AncientMysteries = Music("Ancient Mysteries", "e06", [Cut])
# ASpiritualPlace = Music("A Spiritual Place", "e07", [Cut])
ASpiritualPlaceLoop = Music("A Spiritual Place", "e07_loop", [Cut])
Epilogue = Music("Epilogue", "e08", [Cut])
# Memories = Music("Memories", "e09", [Cut])
MemoriesLoop = Music("Memories", "e09_loop", [Cut])
# EverydayLife = Music("Everyday Life", "e10", [Cut])
EverydayLifeLoop = Music("Everyday Life", "e10_loop", [Cut])
# RikiTheLegendaryHeropon = Music("Riki The Legendary Heropon", "e11", [Cut])
RikiTheLegendaryHeroponLoop = Music("Riki The Legendary Heropon", "e11_loop", [Cut])
# ReminiscenceV1 = Music("Reminiscence V1", "e12_v1", [Cut])
ReminiscenceV1Loop = Music("Reminiscence V1", "e12_v1_loop", [Cut])
# ReminiscenceV2 = Music("Reminiscence V2", "e12_v2", [Cut])
ReminiscenceV2Loop = Music("Reminiscence V2", "e12_v2_loop", [Cut])
# AFriendOnMyMind = Music("A Friend On My Mind", "e13", [Cut])
AFriendOnMyMindLoop = Music("A Friend On My Mind", "e13_loop", [Cut])
# ShulkAndFiora = Music("Shulk And Fiora", "e14", [Cut])
ShulkAndFioraLoop = Music("Shulk And Fiora", "e14_loop", [Cut])
# Apprehension = Music("Apprehension", "e15", [Cut], Bad)
ApprehensionLoop = Music("Apprehension", "e15_loop", [Cut], Bad)
# Tension = Music("Tension", "e16", [Cut], Bad)
TensionLoop = Music("Tension", "e16_loop", [Cut])
# Face = Music("Face", "e17", [Cut])
FaceLoop = Music("Face", "e17_loop", [Cut])
# Disquiet = Music("Disquiet", "e18", [Cut], Bad)
DisquietLoop = Music("Disquiet", "e18_loop", [Cut], Bad)
# Crisis = Music("Crisis", "e20", [Cut])
CrisisLoop = Music("Crisis", "e20_loop", [Cut])
# EgilsTheme = Music("Egils Theme", "e21", [Cut], Bad)
EgilsThemeLoop = Music("Egils Theme", "e21_loop", [Cut], Bad)
# ShadowsCreeping = Music("Shadows Creeping", "e22", [Cut], Bad)
ShadowsCreepingLoop = Music("Shadows Creeping", "e22_loop", [Cut], Bad)
# IntrigueV1 = Music("Intrigue V1", "e23_v1", [Cut], Bad)
IntrigueV1Loop = Music("Intrigue V1", "e23_v1_loop", [Cut], Bad)
# IntrigueV2 = Music("Intrigue V2", "e23_v2", [Cut], Bad)
IntrigueV2Loop = Music("Intrigue V2", "e23_v2_loop", [Cut], Bad)
