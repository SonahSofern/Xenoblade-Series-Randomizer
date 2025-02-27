import json, random
from scripts import Interactables

AllMusic = []
Env = 1 # Environment Themes
Cut = 2 # Cutscene Themes
Battle = 3 # Battle Themes
Boss = 4 # Boss Theme
Jingle = 5 # Jingles

Good = "Good"
Bad = "Bad"

class Music:
    def __init__(self,_song, _fileName, _type = [], _isGood = Good):
        self.songName = _song
        self.fileName = _fileName   
        self.isGood = _isGood
        self.type = _type
        AllMusic.append(self)
        
        Interactables.SubOption(self.songName, parent, [lambda: UsedEnvironmentThemes.append(self)])
        
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

def MusicRando(Songs:list[Music]):
    with open("./XCDE/_internal/JsonOutputs/bdat_common/bgmlist.json", 'r+', encoding='utf-8') as bgmFile:
        bgmData = json.load(bgmFile)
        
        # RemoveInvalidSongs(Songs)
        
        for bgm in bgmData["rows"]:
            name = bgm["file_name"]
            if any(song.fileName == name for song in Songs):
                bgm["file_name"] = random.choice(Songs).fileName
                
        bgmFile.seek(0)
        bgmFile.truncate()
        json.dump(bgmData, bgmFile, indent=2, ensure_ascii=False)


# def RemoveInvalidSongs(Songs):
#     for bgm in Songs: # 
#         if bgm in InvalidSongsList:
#             Songs.remove(bgm)
        

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



InvalidSongsList = []

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
PrisonIsland = Music("PrisonIsland", "f13_loop", [Env])
ValakMountain = Music("ValakMountain", "f14_loop", [Env])
SwordValley = Music("SwordValley", "f15_loop", [Env])
GalahadFortress = Music("GalahadFortress", "f16_loop", [Env])
TheFallenLand = Music("TheFallenLand", "f17_loop", [Env])
HiddenMachinaVillage = Music("HiddenMachinaVillage", "f18_loop", [Env])
MechonisField = Music("MechonisField", "f19_loop", [Env])
AgnirathaMechonisCapital = Music("AgnirathaMechonisCapital", "f20_loop", [Env])
CentralFactory = Music("CentralFactory", "f21_loop", [Env])
BionisInteriorCarcass = Music("BionisInteriorCarcass", "f22_loop", [Env])
Colony6Rebuilding = Music("Colony6Rebuilding", "f23_loop", [Env])
MemorysEnd = Music("MemorysEnd", "f24_loop", [Env])
InTheRefugeeCamp = Music("InTheRefugeeCamp", "f25_loop", [Env])
TheEndLiesAhead = Music("TheEndLiesAhead", "f26_loop", [Env])
GranDellFC = Music("GranDellFC", "f51_loop", [Env])
BionisShoulderFC = Music("BionisShoulderFC", "f52_loop", [Env])

# Battle Themes
TimeToFight = Music("TimeToFight", "b01_loop", [Battle])
MechanicalRhythm = Music("MechanicalRhythm", "b03_loop", [Battle])
TimeToFightBionisShoulder = Music("TimeToFightBionisShoulder", "b51_loop", [Battle])
Fogbeasts = Music("Fogbeasts", "b52_loop", [Battle])
EnemiesClosingIn = Music("EnemiesClosingIn", "b08_loop", [Battle], Bad)
SearchingGlance = Music("SearchingGlance", "b10_loop", [Battle], Bad)
IrregularBound = Music("IrregularBound", "b11_loop", [Battle], Bad)
ZanzasWorld = Music("ZanzasWorld", "b12_loop", [Battle], Bad)
VisionsOfTheFuture = Music("VisionsOfTheFuture", "b09_loop", [Battle], Bad)

# Boss Themes
AnObstacleInOurPath = Music("AnObstacleInOurPath", "b05_loop", [Boss])
YouWillKnowOurNames = Music("YouWillKnowOurNames", "b02_loop", [Boss])
ZanzaTheDivine = Music("ZanzaTheDivine", "b06_loop", [Boss])
ATragicDecision = Music("ATragicDecision", "b15_loop", [Boss])
RoarFromBeyond = Music("RoarFromBeyond", "b53_loop", [Boss])
UnfinishedBusiness = Music("UnfinishedBusiness", "e03", [Boss])
TheGodSlayingSword = Music("TheGodSlayingSword", "b07_loop", [Boss])
EngageTheEnemy = Music("EngageTheEnemy", "e04", [Boss])

# Jingles
CollectopediaLineCompleted = Music("CollectopediaLineCompleted", "j01", [Jingle])
CollectopediaPageCompleted = Music("CollectopediaPageCompleted", "j02", [Jingle])
NewObjectiveReceived = Music("NewObjectiveReceived", "j03", [Jingle])
NewAreaFound = Music("NewAreaFound", "j04", [Jingle])
SecretAreaFound = Music("SecretAreaFound", "j05", [Jingle])

# Cutscene Themes
PrologueA = Music("PrologueA", "e01_a", [Cut, Battle])
PrologueB = Music("PrologueB", "e01_b", [Cut, Battle])
MainTheme = Music("MainTheme", "e02", [Cut])
MainThemeLoop = Music("MainThemeLoop", "e02_loop", [Cut])
BionisAwakening = Music("BionisAwakening", "e05", [Cut])
AncientMysteries = Music("AncientMysteries", "e06", [Cut])
ASpiritualPlace = Music("ASpiritualPlace", "e07", [Cut])
ASpiritualPlaceLoop = Music("ASpiritualPlaceLoop", "e07_loop", [Cut])
Epilogue = Music("Epilogue", "e08", [Cut])
Memories = Music("Memories", "e09", [Cut])
MemoriesLoop = Music("MemoriesLoop", "e09_loop", [Cut])
EverydayLife = Music("EverydayLife", "e10", [Cut])
EverydayLifeLoop = Music("EverydayLifeLoop", "e10_loop", [Cut])
RikiTheLegendaryHeropon = Music("RikiTheLegendaryHeropon", "e11", [Cut])
RikiTheLegendaryHeroponLoop = Music("RikiTheLegendaryHeroponLoop", "e11_loop", [Cut])
ReminiscenceV1 = Music("ReminiscenceV1", "e12_v1", [Cut])
ReminiscenceV1Loop = Music("ReminiscenceV1Loop", "e12_v1_loop", [Cut])
ReminiscenceV2 = Music("ReminiscenceV2", "e12_v2", [Cut])
ReminiscenceV2Loop = Music("ReminiscenceV2Loop", "e12_v2_loop", [Cut])
AFriendOnMyMind = Music("AFriendOnMyMind", "e13", [Cut])
AFriendOnMyMindLoop = Music("AFriendOnMyMindLoop", "e13_loop", [Cut])
ShulkAndFiora = Music("ShulkAndFiora", "e14", [Cut])
ShulkAndFioraLoop = Music("ShulkAndFioraLoop", "e14_loop", [Cut])
Apprehension = Music("Apprehension", "e15", [Cut], Bad)
ApprehensionLoop = Music("ApprehensionLoop", "e15_loop", [Cut], Bad)
Tension = Music("Tension", "e16", [Cut], Bad)
TensionLoop = Music("TensionLoop", "e16_loop", [Cut])
Face = Music("Face", "e17", [Cut])
FaceLoop = Music("FaceLoop", "e17_loop", [Cut])
Disquiet = Music("Disquiet", "e18", [Cut], Bad)
DisquietLoop = Music("DisquietLoop", "e18_loop", [Cut], Bad)
Crisis = Music("Crisis", "e20", [Cut])
CrisisLoop = Music("CrisisLoop", "e20_loop", [Cut])
EgilsTheme = Music("EgilsTheme", "e21", [Cut], Bad)
EgilsThemeLoop = Music("EgilsThemeLoop", "e21_loop", [Cut], Bad)
ShadowsCreeping = Music("ShadowsCreeping", "e22", [Cut], Bad)
ShadowsCreepingLoop = Music("ShadowsCreepingLoop", "e22_loop", [Cut], Bad)
IntrigueV1 = Music("IntrigueV1", "e23_v1", [Cut], Bad)
IntrigueV1Loop = Music("IntrigueV1Loop", "e23_v1_loop", [Cut], Bad)
IntrigueV2 = Music("IntrigueV2", "e23_v2", [Cut], Bad)
IntrigueV2Loop = Music("IntrigueV2Loop", "e23_v2_loop", [Cut], Bad)
    
# EnvironmentThemes = [
# "f01_loop", # - Hometown
# "f02_loop", # - Colony 9
# "f03_loop", # - Tephra Cave
# "f04_loop", # - Gaur Plain
# "f05_loop", # - Colony 6 - Ether Mine
# "f06_loop", # - Satorl Marsh
# "f07_loop", # - Forest of the Nopon
# "f08_loop", # - Frontier Village
# "f10_loop", # - Where the Ancestors Sleep
# "f11_loop", # - Eryth Sea
# "f12_loop", # - Alcamoth, Imperial Capital
# "f13_loop", # - Prison Island
# "f14_loop", # - Valak Mountain
# "f15_loop", # - Sword Valley
# "f16_loop", # - Galahad Fortress
# "f17_loop", # - The Fallen Land
# "f18_loop", # - Hidden Machina Village
# "f19_loop", # - Mechonis Field
# "f20_loop", # - Agniratha, Mechonis Capital
# "f21_loop", # - Central Factory
# "f22_loop", # - Bionis Interior (Carcass)
# "f23_loop", # - Colony 6 - Rebuilding / Restoration
# "f24_loop", # - Memory's End (Spacey Ambience Song)
# "f25_loop", # - In The Refugee Camp (Escape Boat Camping)
# "f26_loop", # - The End Lies Ahead (To The Final Battle, Prison Island)
# "f51_loop", # - Gran Dell FC
# "f52_loop", # - Bionis' Shoulder FC

# # Non-Default Environmental Songs

# "a01_loop", # - Hometown
# "a02_loop", # - Colony 9
# "a03_loop", # - Gaur Plain
# "a04_loop", # - Satorl Marsh
# "a05_loop", # - Forest of the Nopon (Makna Forest)
# "a06_loop", # - Frontier Village
# "a08_loop", # - Eryth Sea
# "a09_loop", # - Alcamoth, Imperial Capital
# "a10_loop", # - Valak Mountain
# "a11_loop", # - Sword Valley
# "a12_loop", # - The Fallen Land
# "a14_loop", # - Agniratha, Mechonis Capital
# "a15_loop", # - Bionis Interior (Pulse)
# "a16_loop", # - Colony 6 - Silence
# "a17_loop", # - Colony 6 - Hope
# "a18_loop", # - Colony 6 - Future 
# "a51_loop", # - Gran Dell FC
# "a52_loop", # - Bionis' Shoulder FC
# ]

# BattleThemes = [
# "b01_loop", # - Time to Fight!
# "b03_loop", # - Mechanical Rhythm
# "b51_loop", # - Time to Fight! (Bionis Shoulder) FC
# "b52_loop", # - Fogbeasts
# "b08_loop", # - Enemies Closing In
# "b10_loop", # - Searching Glance
# "b11_loop", # - Irregular Bound
# "b12_loop", # - Zanza's World
# "b09_loop", # - Visions of the Future
# ]

# BossThemes = [
# "b05_loop", # - An Obstacle in Our Path
# "b02_loop", # - You Will Know Our Names
# "b06_loop", # - Zanza the Divine
# "b15_loop", # - A Tragic Decision
# "b53_loop", # - Roar from Beyond
# "e03",      # - Unfinished Business
# "b07_loop", # - The God Slaying Sword
# "e04",      # - Engage the Enemy
# ]



# Jingles = [
# "j01",       # - Collectopaedia Line Completed
# "j02",       # - Collectopaedia Page Completed
# "j03",       # - New Objective Received
# "j04",       # - New Area Found
# "j05",       # - Secret Area Found
# ]

# CutsceneThemes =[
# "e01_a",     # - Prologue A
# "e01_b",     # - Prologue B
# "e02",       # - Main Theme (3:40)
# "e02_loop",  # - Main Theme Loop (7:30)
# "e03",       # - Unfinished Business
# "e04",       # - Engage the Enemy
# "e05",       # - Bionis' Awakening
# "e06",       # - Ancient Mysteries
# "e07",       # - A Spiritual Place
# "e07_loop",  # - A Spiritual Place Loop (5:29)
# "e08",       # - Epilogue
# "e09",       # - Memories
# "e09_loop",  # - Memories Loop (6:11)
# "e10",       # - Everyday Life (2:12)
# "e10_loop",  # - Everyday Life Loop (4:12)
# "e11",       # - Riki the Legendary Heropon
# "e11_loop",  # - Riki the Legendary Heropon Loop (5:03)
# "e12_v1",    # - Reminiscence 
# "e12_v1_loop", # - Reminiscence Loop (6:13)
# "e12_v2",    # - Reminiscence (Music Box) 
# "e12_v2_loop", # - Reminiscence (Music Box) Loop (6:06)
# "e13",       # - A Friend On My Mind
# "e13_loop",  # - A Friend On My Mind Loop (5:17)
# "e14",       # - Shulk and Fiora
# "e14_loop",  # - Shulk and Fiora Loop (6:14)
# "e15",       # - Apprehension
# "e15_loop",  # - Apprehension Loop (5:30)
# "e16",       # - Tension
# "e16_loop",  # - Tension Loop (5:48)
# "e17",       # - Face
# "e17_loop",  # - Face Loop
# "e18",       # - Disquiet -- The song that sounds like something banging in the wind
# "e18_loop",  # - Disquiet Loop
# "e19",       # - Apprehension
# "e19_loop",  # - Apprehension Looped
# "e20",       # - Crisis
# "e20_loop",  # - Crisis Looped (3:42)
# "e21",       # - Egil's Theme (Anger, Darkness of the Heart)
# "e21_loop",  # - Egil's Theme Looped (6:24)
# "e22",      # - Shadows Creeping
# "e22_loop",  # - Shadows Creeping Looped (6:10)
# "e23_v1",    # - Intrigue (2:32)
# "e23_v1_loop", # - Intrigue Looped (5:14)
# "e23_v2",    # - Intrigue (v2) (2:48) -- Has more strings melody, more to it.
# "e23_v2_loop", # - Intrigue (v2) Looped (5:46)
# "e23_v3",    # - Intrigue (v3) (2:48) -- Has even more strings melody!
# "e23_v3_loop", # - Intriuge (v3) Looped (5:46)
# "e24",       # - Towering Shadow (Gigantic Silhouette)
# "e24_loop",  # - Towering Shadow Looped (5:49)
# "e25",       # - Sorrow
# "e25_loop",  # - Sorrow Looped (5:06)
# "e26_v1",    # - Once We Part Ways
# "e26_v1_loop", # - Once We Part Ways Loop (6:56)
# "e26_v2",    # - Thoughts Enshrined (While I Think)
# "e26_v2_loop", # - Thoughts Enshrined (6:52)
# "e27",       # - Regret
# "e27_loop",  # - Regret Looped (5:15)
# "e28",       # - The Battle Is Upon Us (The Night Before the Decisive Battle)
# "e28_loop",  # - The Battle Is Upon Us Looped (6:57)
# "e29",       # - Futures That Lie Ahead (To One's Own Future)
# "e29_loop",  # - Futures That Lie Ahead Looped (6:50)
# "e30_v1",    # - Majesty (Grandeur) 
# "e30_v1_loop", # - Majesty Looped (7:22)
# "e30_v2",    # - Majesty (End-Game, Providence)
# "e31_v1",    # - Hope v1 (Unused Song) (3:18)
# "e31_v1_loop", # - Hope v2 Looped (6:46)
# "e31_v2",    # - Hope v2 (1:35)
# "e31_v2_loop", # - Hope v2 Looped (3:20)
# "e32",       # - Riki's Kindness (Riki's Tenderness)
# "e32_loop", # - Riki's Kindness Looped (4:50)
# "e33",       # - The Monado Awakens (0:35)
# "e34",       # - Urgency (1:11)
# "e34_loop",  # - Urgency Loop (2:24) 
# ]

