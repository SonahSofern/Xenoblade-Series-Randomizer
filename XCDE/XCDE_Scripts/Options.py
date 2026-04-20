from scripts.Interactables import Option, SubOption
from scripts import Helper
from XCDE.XCDE_Scripts import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Tutorials, Armor, MiscQOL, Scales, NPC, Weapons, Items, Cutscenes, IDs, Landmarks
import scripts.Interactables

scripts.Interactables.Game = "XCDE" 

General = 1
Character  = 2
Enemies = 3
Musica = 5
QOL = 4
Funny = 6

Tabs = {
    General: 'Items',
    Character: 'Characters',
    Enemies: 'Enemies',
    QOL: 'Quality of Life',
    Musica: 'Music',
    Funny: 'Funny',
}

weightsSpinDescription = "Weights ↓"

# General
ShopOption = Option("Shops", General, "Randomizes the contents of shops", [lambda: Items.Shops()], descData=lambda: Items.ShopsDesc()) # Key item rando settings would be fun 
TradeOption = Option("Trading", General, "Randomizes the offers of NPC trades", [lambda: Items.TradeOptions()], descData=lambda: Items.TradeOptionsDesc())

CollectableOptions = Option("Collectable Orbs", General, "Randomizes collectables on the field into the chosen types", [lambda: Items.Collectables()], descData=lambda: Items.CollectDesc())
CollectableOptions_Collectables = SubOption("Collectables", CollectableOptions, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
CollectableOptions_Materials = SubOption("Materials", CollectableOptions, hasSpinBox=True, spinDefault=30)
CollectableOptions_Armor = SubOption("Armor", CollectableOptions, hasSpinBox=True, spinDefault=5)
CollectableOptions_Weapons = SubOption("Weapons", CollectableOptions, hasSpinBox=True, spinDefault=5)
CollectableOptions_Gems = SubOption("Gems", CollectableOptions, hasSpinBox=True, spinDefault=10)
CollectableOptions_ArtBooks = SubOption("Art Books", CollectableOptions, hasSpinBox=True, spinDefault=1)

CollectapediaOptions = Option("Collectapedia Rewards", General, "Randomizes rewards from the collectapedia into the chosen types", [lambda: Items.Collectapedia()], descData=lambda: Items.CollectapediaDesc())
CollectapediaOptions_Collectables = SubOption("Collectables", CollectapediaOptions, hasSpinBox=True, spinDesc=weightsSpinDescription, spinDefault=1)
CollectapediaOptions_Materials = SubOption("Materials", CollectapediaOptions, hasSpinBox=True, spinDefault=1)
CollectapediaOptions_Armor = SubOption("Armor", CollectapediaOptions, hasSpinBox=True, spinDefault=15)
CollectapediaOptions_Weapons = SubOption("Weapons", CollectapediaOptions, hasSpinBox=True, spinDefault=15)
CollectapediaOptions_Gems = SubOption("Gems", CollectapediaOptions, hasSpinBox=True, spinDefault=15)
CollectapediaOptions_ArtBooks = SubOption("Art Books", CollectapediaOptions, hasSpinBox=True, spinDefault=10)


GiantsChestOption = Option("Giants Chests", General, "Randomizes the contents of Giants Chests into the chosen types", [lambda: Items.GiantsChests()], descData=lambda: Items.GiantsChestsDesc())
GiantsChestOptions_Collectables = SubOption("Collectables", GiantsChestOption, hasSpinBox=True, spinDesc=weightsSpinDescription, defState=False, spinDefault=0)
GiantsChestOptions_Materials = SubOption("Materials", GiantsChestOption, hasSpinBox=True, spinDefault=1)
GiantsChestOptions_Armor = SubOption("Armor", GiantsChestOption, hasSpinBox=True, spinDefault=10)
GiantsChestOptions_Weapons = SubOption("Weapons", GiantsChestOption, hasSpinBox=True, spinDefault=10)
GiantsChestOptions_Gems = SubOption("Gems", GiantsChestOption, hasSpinBox=True, spinDefault=10)
GiantsChestOptions_ArtBooks = SubOption("Art Books", GiantsChestOption, hasSpinBox=True, spinDefault=10)

QuestRewardsOption = Option("Quest Rewards", General, "Randomizes the rewards from quests into the chosen types", [lambda: Items.QuestRewards()], descData=lambda: Items.QuestRewardsDesc())
QuestRewardsOptions_Collectables = SubOption("Collectables", QuestRewardsOption, hasSpinBox=True, spinDesc=weightsSpinDescription, spinDefault=1)
QuestRewardsOptions_Materials = SubOption("Materials", QuestRewardsOption, hasSpinBox=True, spinDefault=5)
QuestRewardsOptions_Armor = SubOption("Armor", QuestRewardsOption, hasSpinBox=True, spinDefault=10)
QuestRewardsOptions_Weapons = SubOption("Weapons", QuestRewardsOption, hasSpinBox=True, spinDefault=10)
QuestRewardsOptions_Gems = SubOption("Gems", QuestRewardsOption, hasSpinBox=True, spinDefault=10)
QuestRewardsOptions_ArtBooks = SubOption("Art Books", QuestRewardsOption, hasSpinBox=True, spinDefault=2)

EnemyDropOption = Option("Enemy Drops", General, "Randomizes the chosen types of loot from enemies", [lambda: Items.EnemyDrops()], descData=lambda: Items.EnemyDropsDesc())
EnemyDropOptions_Materials = SubOption("Materials", EnemyDropOption)
EnemyDropOptions_Armor = SubOption("Armor", EnemyDropOption)
EnemyDropOptions_Weapons = SubOption("Weapons", EnemyDropOption)
EnemyDropOptions_ArtBooks = SubOption("Art Books", EnemyDropOption)
# https://xenobladedata.github.io/xb1de/bdat/bdat_common/FLD_valpoplist.html#1 Red orbs found here not sure what to do with them yet


# Enemy
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: EnemiesScript.Enemies(IDs.NormalEnemies, NormalEnemyOption, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption_Size.GetState())], descData=lambda: EnemiesScript.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=15, spinDesc=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, defState=False, hasSpinBox=True, spinDefault=1)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: EnemiesScript.Enemies(IDs.UniqueEnemies + IDs.SuperbossEnemies, UniqueEnemyOption, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption_Size.GetState())], descData=lambda: EnemiesScript.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=1, spinDesc=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=15)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=2)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: EnemiesScript.Enemies(IDs.BossEnemies, BossEnemyOption, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, True, BossEnemyOption_FinalBoss.GetState()), lambda: EnemiesScript.EgilArenaFix()], descData=lambda: EnemiesScript.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=2, spinDesc=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False, hasSpinBox=True, spinDefault=1)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)

# FinalBossOption = Option("Final Boss", Enemies, "Forces the final boss to be one of your choices")

# Character
GemOption = Option("Gems", Character, "Randomizes the effects of Gems and Crystals", [lambda: Gems.Gems()], descData=lambda: Gems.GemDescriptions())
GemOption_Power = SubOption("Power", GemOption)
GemOption_Effect = SubOption("Effects", GemOption)
GemOption_Unused = SubOption("Unused Effects", GemOption)
GemOption_FreeEquip = SubOption("Freely Equip to Weapons/Armor", GemOption)
GemOption_NoCap = SubOption("Gem Caps", GemOption)
AffinityTreeOption = Option("Skill Trees", Character, "Randomizes all character's skill trees", [lambda: SkillTrees.SkillRando()], descData=lambda: SkillTrees.SkillTreeDesc(), hasSpinBox = True)
AffinityTreeOption_Effect = SubOption("Skill Shuffle", AffinityTreeOption)
AffinityTreeOption_Power = SubOption("Power", AffinityTreeOption)
AffinityTreeOption_LinkCost = SubOption("Affinity Coin Cost", AffinityTreeOption)
AffinityTreeOption_Shape = SubOption("Node Shape", AffinityTreeOption)
PlayerArtsOption = Option("Arts", Character, "Randomizes character's arts and their effects", [lambda: PcArts.RandomizePcArts()], descData=lambda: PcArts.ArtsDescriptions())
PlayerArtsOption_Arts = SubOption("Arts Shuffle", PlayerArtsOption)
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
FasterLvOption = Option("EXP Boost", QOL, "Decreases level up requirements by a set amount (Recommended 3x to rush the story).", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, spinMin = 0, spinMax = 256, spinIncr = 1, spinDesc = "x", spinDefault=3)
FasterSkillTrees = Option("SP Boost", QOL, "Decreases SP (skill point) requirements for skill trees", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_PSVskill.json"], ["point_PP"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, spinMin = 0, spinMax = 256, spinIncr = 1, spinDesc = "x", spinDefault=2)
FasterArtLevels = Option("AP Boost", QOL, "Increases AP (art point) gains for art level ups",[lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_growlist.json"], ["en_ap"], [f'row[key] * {FasterLvOption.GetSpinbox()}'])], hasSpinBox = True, spinMin = 0, spinMax = 256, spinIncr = 1, spinDesc = "x", spinDefault=2)
MovespeedOption = Option("Quickstep", QOL, "The gem man will gift you two free quickstep gems.", [lambda: MiscQOL.Quickstep()], hasSpinBox=True, spinDesc="% Speed", spinMax=100)

# CutsceneSkipOption = Option("Cutscene Skips", QOL, "Skips all possible cutscenes", [lambda: Cutscenes.CutsceneSkipper()])

# Funny
# EnemyScaleOption = Option("Enemy Scale", Funny, "Randomizes a % of enemy sizes.", [lambda: Scales.EnemyScales()], hasSpinBox=True)
NPCScaleOption = Option("NPC Scale", Funny, "Randomizes a % of npc sizes.", [lambda: Scales.NPCScales()], hasSpinBox = True)
RemoveStartingArmorOption = Option("Remove Starting Equipment", Funny, "Removes starting armor on all the main characters.", [lambda: Armor.RemoveStartingGear()])
NPCModelsOption = Option("NPC Models", Funny, "Randomizes NPC models *Experimental, can cause crashes", [lambda: NPC.NPCModelRando()], hasSpinBox = True)

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html

# Collectapedia bdat_menu_item

# https://nenkai.github.io/XenoDocs/xc1de/tables/bdat_common/