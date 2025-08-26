from scripts.Interactables import Option, SubOption, Header
from scripts import Helper
import scripts.Interactables
from XC3.XC3_Scripts import Shortcuts, Skills, Heroes, QOL as Quality, Enemy , IDs, Enhancements, Accessories, Gems, Arts, Items, Costumes, Class, Chaos, Music
scripts.Interactables.Game = "XC3" 

General = 1
Character  = 2
Enemies = 3
QOL = 4
Funny = 5
Musica = 6

Tabs = {
    General: '🞛 Items',
    Character: '🧍 Characters',
    Enemies: '💀 Enemies',
    QOL: '🐇 Quality of Life',
    # Funny: '😄 Funny',
    # Musica: "♪ Music",
}

ShopOption = Option("Shops", General, "Randomizes shop contents", [lambda: Items.Shops()])
ShopOption_IndividualItems = SubOption("Randomize Individual Items", ShopOption)
ShopOption_ShuffleShops = SubOption("Shuffle Shops", ShopOption)

EnemyNormalDropOption = Option("Enemy Drops", General, "Randomizes enemy accessory drops", [lambda: Items.EnemyNormalDrops()])
EnemyNormalDropOption_IndividualItems = SubOption("Randomize Individual Drops", EnemyNormalDropOption)
EnemyNormalDropOption_ShuffleDrops = SubOption("Shuffle Drops", EnemyNormalDropOption)

TreasureBoxOption = Option("Containers", General, "Randomizes the contents of containers", [lambda: Items.TreasureBoxes()])
TreasureBoxOption_IndividualItems = SubOption("Randomize Individual Items", TreasureBoxOption)
TreasureBoxOption_ShuffleBoxes = SubOption("Shuffle Containers", TreasureBoxOption)

# CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])
enemySpinDefaultVal = 10
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsters, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_MatchSize)], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
NormalEnemyOption_MatchSize = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.UniqueMonsters + IDs.SuperbossMonsters, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, UniqueEnemyOption_MatchSize)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
UniqueEnemyOption_MatchSize = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Story Bosses", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonsters, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, BossEnemyOption_MatchSize)], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
BossEnemyOption_GroupFights = SubOption("Balance Group Fights", BossEnemyOption)
BossEnemyOption_MatchSize = SubOption("Match Size", BossEnemyOption)

AccessoriesOption = Option("Accessories", Character, "Randomizes the effects of Accessories", [lambda: Accessories.AccessoryRando()])
GemsOption = Option("Gems", Character, "Randomizes the effects of Gems", [lambda: Gems.GemRando()])
SkillOptions = Option("Skills", Character, "Randomizes character skills", [lambda: Skills.SkillRandoMain()], hasSpinBox=True)
SkillOptions_Vanilla = SubOption("Allow Vanilla Skills", SkillOptions)
SkillOptions_Unused = SubOption("Allow Unused Skills", SkillOptions)
SkillOptions_Class = SubOption("Class Skills", SkillOptions)
SkillOptions_Ouroboros = SubOption("Ouroboros Skills", SkillOptions)
SkillOptions_SoulHacker = SubOption("Soulhacker Skills", SkillOptions)
SkillOptions_SingleNode = SubOption("Node Skills", SkillOptions)
# SkillOptions_MatchSkillClass = SubOption("Match Class Type", SkillOptions)


ArtsOption = Option("Class Arts", Character, "Randomizes class arts into the chosen types", [lambda: Arts.ArtRando()], hasSpinBox=True)
ArtsOption_Arts = SubOption("Arts", ArtsOption)
ArtsOption_OuroArts = SubOption("Ouroboros Arts", ArtsOption)
ArtsOption_TalentArts = SubOption("Talent Arts", ArtsOption)
ArtsOption_HackerArts = SubOption("Soul Hacker Arts", ArtsOption)
ArtsOption_OuroTalentArts = SubOption("Ouroboros Talent Arts", ArtsOption)

OuroArtsOption = Option("Ouroboros Arts", Character, "Randomizes Ouroboros arts into the chosen types", [lambda: Arts.ArtRando()], hasSpinBox=True)
OuroArtsOption_Arts = SubOption("Arts", OuroArtsOption)
OuroArtsOption_OuroArts = SubOption("Ouroboros Arts", OuroArtsOption)
OuroArtsOption_TalentArts = SubOption("Talent Arts", OuroArtsOption)
OuroArtsOption_HackerArts = SubOption("Soul Hacker Arts", OuroArtsOption)
OuroArtsOption_OuroTalentArts = SubOption("Ouroboros Talent Arts", OuroArtsOption)

TalentArtsOption = Option("Talent Arts", Character, "Randomizes Talent arts into the chosen types", [lambda: Arts.ArtRando()], hasSpinBox=True)
TalentArtsOption_Arts = SubOption("Arts", TalentArtsOption)
TalentArtsOption_OuroArts = SubOption("Ouroboros Arts", TalentArtsOption)
TalentArtsOption_TalentArts = SubOption("Talent Arts", TalentArtsOption)
TalentArtsOption_HackerArts = SubOption("Soul Hacker Arts", TalentArtsOption)
TalentArtsOption_OuroTalentArts = SubOption("Ouroboros Talent Arts", TalentArtsOption)

OuroTalentArtsOption = Option("Ouroboros Talent Arts", Character, "Randomizes Ouroboros Talent arts into the chosen types", [lambda: Arts.ArtRando()], hasSpinBox=True)
OuroTalentArtsOption_Arts = SubOption("Arts", OuroTalentArtsOption)
OuroTalentArtsOption_OuroArts = SubOption("Ouroboros Arts", OuroTalentArtsOption)
OuroTalentArtsOption_TalentArts = SubOption("Talent Arts", OuroTalentArtsOption)
OuroTalentArtsOption_HackerArts = SubOption("Soul Hacker Arts", OuroTalentArtsOption)
OuroTalentArtsOption_OuroTalentArts = SubOption("Ouroboros Talent Arts", OuroTalentArtsOption)

ArtsOptionHeader = Header([ArtsOption, OuroArtsOption, OuroTalentArtsOption])

# HerosOption = Option("Heroes", Character, "Randomizes what heroes appear in the world", [lambda: Heroes.HeroSwaps()])
CostumesOption = Option("Class Costumes", Character, "Randomizes class outfits", [lambda: Costumes.CostumeRando()])
ClassOption = Option("Class", Character, "Randomizes classes", [lambda: Class.TalentRando()])
ClassOption_DefaultClasses = SubOption("Default Classes", ClassOption)
ClassOption_HeroClasses = SubOption("Hero Classes", ClassOption)

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])
FasterLevelsOption = Option("Faster Levels", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["XC3/JsonOutputs/btl/BTL_Grow.json"], ["LevelExp", "LevelExp2"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1, spinDesc = "x Faster")
FasterApitudeOption = Option("Faster Class Points", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, spinDesc = "x Faster", spinDefault=2)
MoveSpeedOption = Option("Movespeed", QOL, "Colony 4's affinity reward will be instant and a movespeed deed.", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, spinDesc = "% Speed", spinMin=1, spinMax=255, spinIncr=10)
# AscendedClassOption = Option("Ascended Classes", QOL, "Classes begin the game being able to reach rank 20 (DOESNT WORK)", [lambda: Quality.AscendedClassEarly()]) # https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroDictionary.html set the wakeupquest to 120
EarlyArtsCancelOption = Option("Early Arts Cancel", QOL, "The Art of Flow is given during the introduction", [lambda: Quality.ArtOfFlowEarly()])
GemCraftingOption = Option("Easy Gem Crafting", QOL, "Reduces the material requirements for gem crafting", [lambda: Gems.EasyGemCrafting()])

# # Funny
# ChaosOption = Option("Chaos", Funny, "Shuffles a ton of files around, from voice lines to chain attack cameras. This will make your game chaotic and unstable.")
# for opt in Chaos.ChaosSubOptions:
#     SubOption(opt.name, ChaosOption, [opt.function], _defState = True)
    
# Music
# TestMusicOption = Option("Music", Musica, "", [lambda: Music.Music()])
# Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html

# XYZ of literally everything in the field https://xenobladedata.github.io/xb3_200_dlc4/SYS_GimmickLocation_dlc04.html#27830
# Cutscenes https://xenobladedata.github.io/xb3_200_dlc4/EVT_listEv.html#10277
# How do DLC4 Combos work like the explosion finishers on launched enemies
# Nopon shops are weird
# All main quest here https://xenobladedata.github.io/xb3_200_dlc4/QST_Purpose.html#3