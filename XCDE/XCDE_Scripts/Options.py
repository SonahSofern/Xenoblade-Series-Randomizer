import PcArts
from scripts.Interactables import Option, SubOption
from scripts import Helper
import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Tutorials, Armor, MiscQOL, Scales, NPC, Weapons, Items, Cutscenes, IDs, Landmarks

OptionList =[]
General = 1
Character  = 2
Enemies = 3
Musica = 5
QOL = 4
Funny = 6

# # General
# TradeOption = Option("NPC Trades", General, "Randomizes chosen categories of NPC trades", [lambda: NPC.Trades()], descData=lambda: NPC.NPCTradesDesc())
# TradeOption_Weapon = SubOption("Weapons", TradeOption)
# TradeOption_Armor = SubOption("Armor", TradeOption)
# TradeOption_Gem = SubOption("Gems", TradeOption)
# TradeOption_Collectibles = SubOption("Collectibles", TradeOption)
# TradeOption_Materials = SubOption("Materials", TradeOption)

TradeOption = Option("Trading", General, "Randomizes the offers of NPC trades into the chosen options", [lambda: Items.TradeOptions()], descData=lambda: Items.TradeOptionsDesc(), hasSpinBox = True)
TradeOption_KeepType = SubOption("Keep Item Type", TradeOption)
TradeOptions_Collectables = SubOption("Collectables", TradeOption, hasSpinBox=True)
TradeOptions_Materials = SubOption("Materials", TradeOption, hasSpinBox=True)
TradeOptions_Armor = SubOption("Armor", TradeOption, hasSpinBox=True)
TradeOptions_Weapons = SubOption("Weapons", TradeOption, hasSpinBox=True)
TradeOptions_Gems = SubOption("Gems", TradeOption, hasSpinBox=True)
TradeOptions_Crystals = SubOption("Crystals", TradeOption, hasSpinBox=True)
TradeOptions_ArtBooks = SubOption("Art Books", TradeOption, hasSpinBox=True)
TradeOptions_KeyItems = SubOption("Key Items", TradeOption, hasSpinBox=True)

CollectableOptions = Option("Collectable Orbs", General, "Randomizes collectables on the field into the chosen options", [lambda: Items.Collectables()], hasSpinBox = True, descData=lambda: Items.CollectDesc())
CollectableOptions_Collectables = SubOption("Collectables", CollectableOptions, hasSpinBox=True)
CollectableOptions_Materials = SubOption("Materials", CollectableOptions, hasSpinBox=True)
CollectableOptions_Armor = SubOption("Armor", CollectableOptions, hasSpinBox=True)
CollectableOptions_Weapons = SubOption("Weapons", CollectableOptions, hasSpinBox=True)
CollectableOptions_Gems = SubOption("Gems", CollectableOptions, hasSpinBox=True)
CollectableOptions_Crystals = SubOption("Crystals", CollectableOptions, hasSpinBox=True)
CollectableOptions_ArtBooks = SubOption("Art Books", CollectableOptions, hasSpinBox=True)
CollectableOptions_KeyItems = SubOption("Key Items", CollectableOptions, hasSpinBox=True)

CollectapediaOptions = Option("Collectapedia Rewards", General, "Randomizes rewards from the collectapedia into the chosen options", [lambda: Items.Collectapedia()], descData=lambda: Items.CollectapediaDesc(), hasSpinBox = True)
CollectapediaOptions_KeepType = SubOption("Keep Item Type", CollectapediaOptions)
CollectapediaOptions_Collectables = SubOption("Collectables", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_Materials = SubOption("Materials", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_Armor = SubOption("Armor", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_Weapons = SubOption("Weapons", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_Gems = SubOption("Gems", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_Crystals = SubOption("Crystals", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_ArtBooks = SubOption("Art Books", CollectapediaOptions, hasSpinBox=True)
CollectapediaOptions_KeyItems = SubOption("Key Items", CollectapediaOptions, hasSpinBox=True)


EnemyDropOption = Option("Enemy Drops", General, "Randomizes loot from enemies", [lambda: Items.EnemyDrops()], descData=lambda: Items.EnemyDropsDesc(), hasSpinBox = True)
EnemyDropOption_KeepType = SubOption("Keep Item Type", EnemyDropOption)
EnemyDropOptions_Collectables = SubOption("Collectables", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_Materials = SubOption("Materials", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_Armor = SubOption("Armor", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_Weapons = SubOption("Weapons", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_Gems = SubOption("Gems", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_Crystals = SubOption("Crystals", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_ArtBooks = SubOption("Art Books", EnemyDropOption, hasSpinBox=True)
EnemyDropOptions_KeyItems = SubOption("Key Items", EnemyDropOption, hasSpinBox=True)


GiantsChestOption = Option("Giants Chests", General, "Randomizes the contents of Giants Chests into the chosen options", [lambda: Items.GiantsChests()], descData=lambda: Items.GiantsChestsDesc(), hasSpinBox = True)
GiantsChest_KeepType = SubOption("Keep Item Type", GiantsChestOption)
GiantsChestOptions_Collectables = SubOption("Collectables", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_Materials = SubOption("Materials", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_Armor = SubOption("Armor", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_Weapons = SubOption("Weapons", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_Gems = SubOption("Gems", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_Crystals = SubOption("Crystals", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_ArtBooks = SubOption("Art Books", GiantsChestOption, hasSpinBox=True)
GiantsChestOptions_KeyItems = SubOption("Key Items", GiantsChestOption, hasSpinBox=True)


ShopOption = Option("Shops", General, "Randomizes the contents of shops", [lambda: Items.Shops()], descData=lambda: Items.ShopsDesc(), hasSpinBox = True) # Key item rando settings would be fun 
ShopOption_KeepType = SubOption("Keep Item Type", ShopOption)
ShopOptions_Collectables = SubOption("Collectables", ShopOption, hasSpinBox=True)
ShopOptions_Materials = SubOption("Materials", ShopOption, hasSpinBox=True)
ShopOptions_Armor = SubOption("Armor", ShopOption, hasSpinBox=True)
ShopOptions_Weapons = SubOption("Weapons", ShopOption, hasSpinBox=True)
ShopOptions_Gems = SubOption("Gems", ShopOption, hasSpinBox=True)
ShopOptions_ArtBooks = SubOption("Art Books", ShopOption, hasSpinBox=True)
ShopOptions_KeyItems = SubOption("Key Items", ShopOption, hasSpinBox=True)


QuestRewardsOption = Option("Quest Rewards", General, "Randomizes the rewards from quests into the chosen options", [lambda: Items.QuestRewards()], descData=lambda: Items.QuestRewardsDesc(), hasSpinBox = True)
QuestRewardsOption_KeepType = SubOption("Keep Item Type", QuestRewardsOption)
QuestRewardsOptions_Collectables = SubOption("Collectables", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_Materials = SubOption("Materials", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_Armor = SubOption("Armor", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_Weapons = SubOption("Weapons", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_Gems = SubOption("Gems", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_Crystals = SubOption("Crystals", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_ArtBooks = SubOption("Art Books", QuestRewardsOption, hasSpinBox=True)
QuestRewardsOptions_KeyItems = SubOption("Key Items", QuestRewardsOption, hasSpinBox=True)


# https://xenobladedata.github.io/xb1de/bdat/bdat_common/FLD_valpoplist.html#1 Red orbs found here not sure what to do with them yet

# Enemy
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: EnemiesScript.Enemies(IDs.NormalEnemies, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: EnemiesScript.Enemies(IDs.UniqueEnemies + IDs.SuperbossEnemies, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)

BossEnemyOption = Option("Story Bosses", Enemies, "Randomizes bosses into the chosen types", [lambda: EnemiesScript.Enemies(IDs.BossEnemies, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption), lambda: EnemiesScript.EgilArenaFix()], descData=lambda: EnemiesScript.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption)


# Character
GemOption = Option("Gems", Character, "Randomizes the effects of Gems and Crystals", [lambda: Gems.Gems()], descData=lambda: Gems.GemDescriptions())
GemOption_Power = SubOption("Power", GemOption)
GemOption_Effect = SubOption("Effects", GemOption)
GemOption_Unused = SubOption("Unused Effects", GemOption)
GemOption_FreeEquip = SubOption("Freely Equip to Weapons/Armor", GemOption)
GemOption_NoCap = SubOption("Gem Caps", GemOption)
AffinityTreeOption = Option("Skill Trees", Character, "Randomizes all character's skill trees", [lambda: SkillTrees.SkillRando()], descData=lambda: SkillTrees.SkillTreeDesc(), hasSpinBox = True)
AffinityTreeOption_Effect = SubOption("Skill", AffinityTreeOption)
AffinityTreeOption_Power = SubOption("Power", AffinityTreeOption)
AffinityTreeOption_LinkCost = SubOption("Affinity Coin Cost", AffinityTreeOption)
AffinityTreeOption_Shape = SubOption("Node Shape", AffinityTreeOption)
PlayerArtsOption = Option("Player Arts",Character, "Randomizes character's arts and their effects", [lambda: PcArts.RandomizePcArts()], descData=lambda: PcArts.ArtsDescriptions())
PlayerArtsOption_Power = SubOption("Power", PlayerArtsOption)
# PlayerArtsOption_BalancedUnlockLevels = SubOption("Balanced Unlock Levels", PlayerArtsOption)
# PlayerArtsOption_Duplicates = SubOption("Allow Duplicates", PlayerArtsOption)
# PlayerArtsOption_EarlyArtsUnlock = SubOption("Unlock All Arts at Level 1", PlayerArtsOption)
PlayerArtsOption_ArtGroups = SubOption("Keep Combo Arts Together", PlayerArtsOption)
PlayerArtsOption_Summons = SubOption("Keep Melia's Summons", PlayerArtsOption)
# PlayerArtsOption_GuestArts = SubOption("Include Guest Arts", PlayerArtsOption)
# PlayerArtsOption_Cooldown = SubOption("Cooldown", PlayerArtsOption)
EquipmentOption = Option("Armor", Character, "Randomizes effects of Armor", [lambda: Armor.ArmorRando()], descData=lambda: Armor.ArmorDesc())
EquipmentOption_Appearance = SubOption("Appearance", EquipmentOption)
EquipmentOption_CrazyAppearance = SubOption("Crazy Appearance", EquipmentOption)
# EquipmentOption_Defenses = SubOption("Defenses", EquipmentOption)
EquipmentOption_GemSlots = SubOption("Gem Slots", EquipmentOption)
EquipmentOption_WeightClass = SubOption("Weight Class", EquipmentOption)
WeaponOption = Option("Weapons", Character, "Randomizes effects of Weapons", [lambda: Weapons.WeaponRando()], descData=lambda: Weapons.WepDesc())
WeaponOption_Appearance = SubOption("Appearance", WeaponOption)
# WeaponOption_Damage = SubOption("Damage", WeaponOption)
# WeaponOption_Defense = SubOption("Block", WeaponOption)
# WeaponOption_Crit = SubOption("Crit", WeaponOption)
WeaponOption_Gems = SubOption("Gem Slots", WeaponOption)


# Misc
BattleMusicOption = Option("Battle Music", Musica, "Randomizes the chosen battle themes onto all battle themes", [lambda: Music.MusicRando(Music.AllBattleThemes, Music.UsedBattleThemes)]) #https://xenobladedata.github.io/xb1de/bdat/bdat_common/bgmlist.html
for song in Music.AllBattleThemes:
    song.CreateOption(BattleMusicOption, Music.UsedBattleThemes)
BossMusicOption = Option("Boss Music", Musica, "Randomizes the chosen boss themes onto all boss themes", [lambda: Music.MusicRando(Music.AllBossThemes, Music.UsedBossThemes)])
for song in Music.AllBossThemes:
    song.CreateOption(BossMusicOption, Music.UsedBossThemes)
EnvironmentCutsceneMusicOption = Option("Environment/Cutscene Music", Musica, "Randomizes the chosen environment/cutscene themes onto all environment themes", [lambda: Music.MusicRando(Music.AllEnvironmentThemes + Music.AllCutsceneThemes, Music.UsedEnvironmentThemes + Music.UsedCutsceneThemes)])
for song in Music.AllEnvironmentThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedEnvironmentThemes)
for song in Music.AllCutsceneThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedCutsceneThemes)
JingleMusicOption = Option("Jingles", Musica, "Randomizes the chosen jingles onto all jingles", [lambda: Music.MusicRando(Music.AllJingles, Music.UsedJingles)])
for song in Music.AllJingles:
    song.CreateOption(JingleMusicOption, Music.UsedJingles)

# QOL
TutorialSkipsOption = Option("Tutorial Skips", QOL, "Reduces tutorials as much as possible", [lambda: Tutorials.TutorialSkips()])
FasterLvOption = Option("EXP Boost", QOL, "Decreases level up requirements by a set amount (Recommended 3x to rush the story).", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=3)
FasterSkillTrees = Option("SP Boost", QOL, "Decreases SP (skill point) requirements for skill trees", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_PSVskill.json"], ["point_PP"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=2)
FasterArtLevels = Option("AP Boost", QOL, "Increases AP (art point) gains for art level ups",[lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["en_exp"], [f'row[key] * {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=2)
MovespeedOption = Option("Quickstep", QOL, "The gem man will gift you two free quickstep gems.", [lambda: MiscQOL.Quickstep()], hasSpinBox=True, _spinDesc="% Speed", _spinMax=100)

# CutsceneSkipOption = Option("Cutscene Skips", QOL, "Skips all possible cutscenes", [lambda: Cutscenes.CutsceneSkipper()])

# Funny
# EnemyScaleOption = Option("Enemy Scale", Funny, "Randomizes a % of enemy sizes.", [lambda: Scales.EnemyScales()], hasSpinBox=True)
NPCScaleOption = Option("NPC Scale", Funny, "Randomizes a % of npc sizes.", [lambda: Scales.NPCScales()], hasSpinBox = True)
RemoveStartingArmorOption = Option("Remove Starting Equipment", Funny, "Removes starting armor on all the main characters.", [lambda: Armor.RemoveStartingGear()])
NPCModelsOption = Option("NPC Models", Funny, "Randomizes NPC models *Experimental, can cause crashes", [lambda: NPC.NPCModelRando()], hasSpinBox = True)

# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html

# Collectapedia bdat_menu_item