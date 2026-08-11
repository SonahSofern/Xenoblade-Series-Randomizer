from scripts.Interactables import Option, SubOption, Label, SubSpinbox, SubDropdown, Spinbox
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
ShopOption_Accessories = SubOption("Accessories", ShopOption)
ShopOption_Accessories_Spinbox = SubSpinbox(ShopOption_Accessories, default=20, description=weightsSpinDescription)
ShopOption_Collectables = SubOption("Collectables", ShopOption)
ShopOption_Collectables_Spinbox = SubSpinbox(ShopOption_Collectables, default=5)
ShopOption_Precious = SubOption("Key Items", ShopOption)
ShopOption_Precious_Spinbox = SubSpinbox(ShopOption_Precious, default=1)

EnemyNormalDropOption = Option("Enemy Drops", General, "Randomizes Enemy Drops (not including materials)", [lambda: Items.EnemyDrops()])
EnemyNormalDrop_Accessories = SubOption("Accessories", EnemyNormalDropOption)
EnemyNormalDrop_Accessories_Spinbox = SubSpinbox(EnemyNormalDrop_Accessories, default=20, description=weightsSpinDescription)
EnemyNormalDrop_Precious = SubOption("Key Items", EnemyNormalDropOption)
EnemyNormalDrop_Precious_Spinbox = SubSpinbox(EnemyNormalDrop_Precious, default=2)

TreasureBoxOption = Option("Containers", General, "Randomizes the contents of Containers and Supply Drops", [lambda: Items.TreasureBoxes()])
TreasureBoxOption_Accessories = SubOption("Accessories", TreasureBoxOption)
TreasureBoxOption_Accessories_Spinbox = SubSpinbox(TreasureBoxOption_Accessories, default=20, description=weightsSpinDescription)
TreasureBoxOption_Collectables = SubOption("Collectables", TreasureBoxOption)
TreasureBoxOption_Collectables_Spinbox = SubSpinbox(TreasureBoxOption_Collectables, default=5)
TreasureBoxOption_Precious = SubOption("Key Items", TreasureBoxOption)
TreasureBoxOption_Precious_Spinbox = SubSpinbox(TreasureBoxOption_Precious, default=1)

QuestRewardsOption = Option("Quest Rewards", General, "Randomizes the item rewards from Quests", [lambda: Items.QuestRewards()])
QuestRewardOption_Accessories = SubOption("Accessories", QuestRewardsOption)
QuestRewardOption_Accessories_Spinbox = SubSpinbox(QuestRewardOption_Accessories, default=20, description=weightsSpinDescription)
QuestRewardOption_Collectables = SubOption("Collectables", QuestRewardsOption)
QuestRewardOption_Collectables_Spinbox = SubSpinbox(QuestRewardOption_Collectables, default=5)
QuestRewardOption_Precious = SubOption("Key Items", QuestRewardsOption)
QuestRewardOption_Precious_Spinbox = SubSpinbox(QuestRewardOption_Precious, default=1)

CollectapediaRewardsOption = Option("Collectopaedia Card Rewards", General, "Randomizes the item rewards from Collectopaedia Cards", [lambda: Items.CollectopaediaCards()])
CollectapediaRewardsOption_Accessories = SubOption("Accessories", CollectapediaRewardsOption)
CollectapediaRewardsOption_Accessories_Spinbox = SubSpinbox(CollectapediaRewardsOption_Accessories, default=20, description=weightsSpinDescription)
CollectapediaRewardsOption_Collectables = SubOption("Collectables", CollectapediaRewardsOption)
CollectapediaRewardsOption_Collectables_Spinbox = SubSpinbox(CollectapediaRewardsOption_Collectables, default=1)
CollectapediaRewardsOption_Precious = SubOption("Key Items", CollectapediaRewardsOption)
CollectapediaRewardsOption_Precious_Spinbox = SubSpinbox(CollectapediaRewardsOption_Precious, default=4)

# CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])
enemySpinDefaultVal = 10
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsters, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, True, False, NormalEnemyOption_OopsAll.GetState(), NormalEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), stepSpeed=0.005)
NormalEnemyOption_Spinbox = Spinbox(NormalEnemyOption)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Normal_Spinbox = SubSpinbox(NormalEnemyOption_Normal, default=enemySpinDefaultVal, description=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Unique_Spinbox = SubSpinbox(NormalEnemyOption_Unique, default=2)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Boss_Spinbox = SubSpinbox(NormalEnemyOption_Boss, default=2)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)
NormalEnemyOption_Superboss_Spinbox = SubSpinbox(NormalEnemyOption_Superboss, default=1)
NormalEnemyOption_OopsAll = SubOption("Oops All", NormalEnemyOption)
NormalEnemyOption_OopsAll_Dropdown = SubDropdown(NormalEnemyOption_OopsAll, Enemy.GetOopsAllPool())
NormalEnemyOption_Multiply = SubOption("More Enemies", NormalEnemyOption, [lambda: Enemy.MultiplyEnemies(NormalEnemyOption_Multiply_Spinbox.GetState(), IDs.NormalMonsters)])
NormalEnemyOption_Multiply_Spinbox = SubSpinbox(NormalEnemyOption_Multiply, min=2, max=5, increment=1, default=2, description="x Enemies")
# NormalEnemyOption_MatchSize = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.UniqueMonsters + IDs.SuperbossMonsters, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, True, False, UniqueEnemyOption_OopsAll.GetState(), UniqueEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name))
UniqueEnemyOption_Spinbox = Spinbox(UniqueEnemyOption)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Normal_Spinbox = SubSpinbox(UniqueEnemyOption_Normal, default=2, description=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Unique_Spinbox = SubSpinbox(UniqueEnemyOption_Unique, default=enemySpinDefaultVal)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Boss_Spinbox = SubSpinbox(UniqueEnemyOption_Boss, default=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss_Spinbox = SubSpinbox(UniqueEnemyOption_Superboss, default=2)
UniqueEnemyOption_OopsAll = SubOption("Oops All", UniqueEnemyOption)
UniqueEnemyOption_OopsAll_Dropdown = SubDropdown(UniqueEnemyOption_OopsAll, Enemy.GetOopsAllPool())
UniqueEnemyOption_Multiply = SubOption("More Enemies", UniqueEnemyOption, [lambda: Enemy.MultiplyEnemies(UniqueEnemyOption_Multiply_Spinbox.GetState(), IDs.UniqueMonsters)])
UniqueEnemyOption_Multiply_Spinbox = SubSpinbox(UniqueEnemyOption_Multiply, min=2, max=5, increment=1, default=2, description="x Enemies")

# UniqueEnemyOption_MatchSize = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonsters, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, False, BossEnemyOption_OopsAll.GetState(), BossEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name))
BossEnemyOption_Spinbox = Spinbox(BossEnemyOption)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
BossEnemyOption_Normal_Spinbox = SubSpinbox(BossEnemyOption_Normal, default=3, description=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
BossEnemyOption_Unique_Spinbox = SubSpinbox(BossEnemyOption_Unique, default=6)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
BossEnemyOption_Boss_Spinbox = SubSpinbox(BossEnemyOption_Boss, default=20)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False)
BossEnemyOption_Superboss_Spinbox = SubSpinbox(BossEnemyOption_Superboss, default=1)
# BossEnemyOption_GroupFights = SubOption("Balance Group Fights", BossEnemyOption)
BossEnemyOption_OopsAll = SubOption("Oops All", BossEnemyOption)
BossEnemyOption_OopsAll_Dropdown = SubDropdown(BossEnemyOption_OopsAll, Enemy.GetOopsAllPool())
BossEnemyOption_Multiply = SubOption("More Enemies", BossEnemyOption, [lambda: Enemy.MultiplyEnemies(BossEnemyOption_Multiply_Spinbox.GetState(), IDs.BossMonsters)])
BossEnemyOption_Multiply_Spinbox = SubSpinbox(BossEnemyOption_Multiply, min=2, max=5, increment=1, default=2, description="x Enemies")

AccessoriesOption = Option("Accessories", Character, "Randomizes the effects of Accessories", [lambda: Accessories.AccessoryRando()])
GemsOption = Option("Gems", Character, "Randomizes the effects of Gems", [lambda: Gems.GemRando()])

MajorSkillOption = Option("Major Skills", Character, "Randomizes the chosen major skill categories", [lambda: Skills.SkillRandoMain()])
MajorSkillOption_Spinbox = Spinbox(MajorSkillOption)
MajorSkillOption_MatchClassType = SubOption("Match Role Type", MajorSkillOption)
MajorSkillOption_MatchClassType_Spinbox = SubSpinbox(MajorSkillOption_MatchClassType, default=70, description="% Matching Skills")
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
        mainOption = Option(name, Character, "Randomizes " + name + " into the chosen types", [lambda: Arts.ArtRando(targetIDs, subClassArts, subOuroArts, subTalentArts, subOuroTalentArts, subHackerArts, spinBox.GetState(), extraIgnoreKeys)])
        spinBox = Spinbox(mainOption)
        subClassArts = SubOption(nameClassArts, mainOption, hasSpinBox=True, spinDefault=defaultArtSpinWeight, spinDesc=weightsSpinDescription) # Currently not used so leaving as the old method
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
TutorialSkipOption = Option("Tutorial Skips", QOL, "Removes tutorials, as a side effect also gives access to all systems from the start", [lambda: Shortcuts.TutorialSkips()])
FasterLevelsOption = Option("EXP Boost", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["XC3/JsonOutputs/btl/BTL_Grow.json"], ["LevelExp", "LevelExp2"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])])
FasterLevelsOption_Spinbox = Spinbox(FasterLevelsOption, default=2, increment= 1, description = "x Faster")
FasterApitudeOption = Option("CP Boost", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()])
FasterApitudeOption_Spinbox = Spinbox(FasterApitudeOption, description = "x Faster", default=2)
FasterAffinityGrowthOption = Option("AP Boost", QOL, "Decreases AP required for each Affinity Growth node (Future Redeemed)", [lambda: Quality.AffinityGrowthReduction(FasterAffinityGrowthOption.GetSpinbox())])
FasterAffinityGrowthOption_Spinbox = Spinbox(FasterAffinityGrowthOption, default=2, increment = 1, description = "x Faster")
MoveSpeedOption = Option("Speed Boost", QOL, "Colony 4's affinity reward will be instant and a movespeed deed", [lambda: Quality.EarlyMoveSpeed()])
MoveSpeedOption_Spinbox = Spinbox(MoveSpeedOption, description = "% Speed", min=1, max=255, increment=10)
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