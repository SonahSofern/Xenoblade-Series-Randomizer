from scripts.Interactables import Option, SubOption, Label
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
    General: 'Items',
    Character: 'Characters',
    Enemies: 'Enemies',
    QOL: 'Quality of Life',
    # Funny: 'Funny',
    # Musica: "Music",
}

weightsSpinDescription = "Weights ↓"

ShopOption = Option("Shops", General, "Randomizes shop contents", [lambda: Items.Shops()])
ShopOption_Accessories = SubOption("Accessories", ShopOption, hasSpinBox=True, spinDefault=20, spinDesc=weightsSpinDescription)
ShopOption_Collectables = SubOption("Collectables", ShopOption, hasSpinBox=True, spinDefault=5)
ShopOption_Precious = SubOption("Key Items", ShopOption, hasSpinBox=True, spinDefault=1)

EnemyNormalDropOption = Option("Enemy Drops", General, "Randomizes Enemy Drops (not including materials)", [lambda: Items.EnemyDrops()])
EnemyNormalDrop_Accessories = SubOption("Accessories", EnemyNormalDropOption, hasSpinBox=True, spinDefault=20, spinDesc=weightsSpinDescription)
EnemyNormalDrop_Precious = SubOption("Key Items", EnemyNormalDropOption, hasSpinBox=True, spinDefault=2)

TreasureBoxOption = Option("Containers", General, "Randomizes the contents of Containers and Supply Drops", [lambda: Items.TreasureBoxes()])
TreasureBoxOption_Accessories = SubOption("Accessories", TreasureBoxOption, hasSpinBox=True, spinDefault=20, spinDesc=weightsSpinDescription)
TreasureBoxOption_Collectables = SubOption("Collectables", TreasureBoxOption, hasSpinBox=True, spinDefault=5)
TreasureBoxOption_Precious = SubOption("Key Items", TreasureBoxOption, hasSpinBox=True, spinDefault=1)

QuestRewardsOption = Option("Quest Rewards", General, "Randomizes the item rewards from Quests", [lambda: Items.QuestRewards()])
QuestRewardOption_Accessories = SubOption("Accessories", QuestRewardsOption, hasSpinBox=True, spinDefault=20, spinDesc=weightsSpinDescription)
QuestRewardOption_Collectables = SubOption("Collectables", QuestRewardsOption, hasSpinBox=True, spinDefault=5)
QuestRewardOption_Precious = SubOption("Key Items", QuestRewardsOption, hasSpinBox=True, spinDefault=1)

CollectapediaRewardsOption = Option("Collectopaedia Card Rewards", General, "Randomizes the item rewards from Collectopaedia Cards", [lambda: Items.CollectopaediaCards()])
CollectapediaRewardsOption_Accessories = SubOption("Accessories", CollectapediaRewardsOption, hasSpinBox=True, spinDefault=20, spinDesc=weightsSpinDescription)
CollectapediaRewardsOption_Collectables = SubOption("Collectables", CollectapediaRewardsOption, hasSpinBox=True, spinDefault=1)
CollectapediaRewardsOption_Precious = SubOption("Key Items", CollectapediaRewardsOption, hasSpinBox=True, spinDefault=4)

# CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])
enemySpinDefaultVal = 10
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsters, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_MatchSize.GetState(), False)], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True, stepSpeed=0.005)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal, spinDesc=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=2)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=2)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True, spinDefault=1)
NormalEnemyOption_MatchSize = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.UniqueMonsters + IDs.SuperbossMonsters, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, UniqueEnemyOption_MatchSize.GetState(), False)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=2, spinDesc=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=enemySpinDefaultVal)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=2)
UniqueEnemyOption_MatchSize = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonsters, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, BossEnemyOption_GroupFights)], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=3, spinDesc=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=6)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=20)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState = False, hasSpinBox=True, spinDefault=1)
BossEnemyOption_GroupFights = SubOption("Balance Group Fights", BossEnemyOption)

AccessoriesOption = Option("Accessories", Character, "Randomizes the effects of Accessories", [lambda: Accessories.AccessoryRando()])
GemsOption = Option("Gems", Character, "Randomizes the effects of Gems", [lambda: Gems.GemRando()])

MajorSkillOption = Option("Major Skills", Character, "Randomizes the chosen major skill categories", [lambda: Skills.SkillRandoMain()], hasSpinBox=True)
MajorSkillOption_MatchClassType = SubOption("Match Role Type", MajorSkillOption, hasSpinBox=True, spinDesc="% Matching Skills", spinDefault=70)
MajorSkillOption_VanillaSkills = SubOption("Allow Vanilla Pool", MajorSkillOption)
MajorSkillOption_CustomSkills = SubOption("Allow Custom Pool", MajorSkillOption)
MajorSkillOption_ClassSkills = SubOption("Class Skills", MajorSkillOption)
MajorSkillOption_OuroSkills = SubOption("Ouroboros Skills", MajorSkillOption)
MajorSkillOption_HackerSkills = SubOption("Soul Hacker Skills", MajorSkillOption)
MajorSkillOption_InoSkills = SubOption("Ino Skills", MajorSkillOption)
MajorSkillOption_AffinityGrowthSkills = SubOption("Affinity Growth Skills", MajorSkillOption)
MajorSkillOption_UnitySkills = SubOption("Unity Pairing Skills", MajorSkillOption)

MinorSkillOption = Option("Minor Skills", Character, "Randomizes minor skills among themselves", [lambda: Skills.MinorSkillShuffle(IDs.InoTreeNodes + IDs.UroTreeNodes + IDs.DLC4TreeNodes)])

nameClassArts = "Class Arts"
nameOuroArts = "Ouroborous Arts"
nameTalentArts = "Class Talent Arts"
nameOuroTalentArts = "Ouroborous Talent Arts"
nameHackerArts = "Soul Hacker Arts"

class ArtShuffleOption():
    def __init__(self, name, targetIDs, extraIgnoreKeys = []):
        defaultArtSpinWeight = 10
        mainOption = Option(name, Character, "Randomizes " + name + " into the chosen types", [lambda: Arts.ArtRando(targetIDs, subClassArts, subOuroArts, subTalentArts, subOuroTalentArts, subHackerArts, mainOption.GetSpinbox(), extraIgnoreKeys)], hasSpinBox=True)
        subClassArts = SubOption(nameClassArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight, spinDesc=weightsSpinDescription)
        subOuroArts = SubOption(nameOuroArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight)
        subTalentArts = SubOption(nameTalentArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight)
        subOuroTalentArts = SubOption(nameOuroTalentArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight)
        subHackerArts = SubOption(nameHackerArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight)

# ClassArtOption = ArtShuffleOption(nameClassArts, IDs.ArtIDs)
# OuroArtOption = ArtShuffleOption(nameOuroArts, IDs.OuroborosArtIDs)
# TalentArtOption = ArtShuffleOption(nameTalentArts, IDs.TalentArtIDs)
# OuroTalentArtOption = ArtShuffleOption(nameOuroTalentArts, IDs.OuroTalentArtIDs)
# SoulHackerArtOption = ArtShuffleOption(nameHackerArts, IDs.HackerArtIDs)

# HerosOption = Option("Heroes", Character, "Randomizes what heroes appear in the world", [lambda: Heroes.HeroSwaps()])
CostumesOption = Option("Class Costumes", Character, "Randomizes class outfits", [lambda: Costumes.LearnedClassOutfits()])
# ClassOption = Option("Class", Character, "Randomizes classes", [lambda: Class.TalentRando()])
# ClassOption_DefaultClasses = SubOption("Default Classes", ClassOption)
# ClassOption_HeroClasses = SubOption("Hero Classes", ClassOption)

# ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
TutorialSkipOption = Option("Tutorial Skip", QOL, "Removes tutorials, also gives access to all systems from the start", [lambda: Shortcuts.TutorialSkips()])
FasterLevelsOption = Option("EXP Boost", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["XC3/JsonOutputs/btl/BTL_Grow.json"], ["LevelExp", "LevelExp2"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1, spinDesc = "x Faster")
FasterApitudeOption = Option("CP Boost", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, spinDesc = "x Faster", spinDefault=2)
MoveSpeedOption = Option("Speed Boost", QOL, "Colony 4's affinity reward will be instant and a movespeed deed", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, spinDesc = "% Speed", spinMin=1, spinMax=255, spinIncr=10)
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