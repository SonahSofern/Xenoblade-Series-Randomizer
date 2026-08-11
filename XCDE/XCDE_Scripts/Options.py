from scripts.Interactables import Option, SubOption, Spinbox, SubSpinbox, SubDropdown, Dropdown
from scripts import Helper, XCRandomizer
from XCDE.XCDE_Scripts import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Armor, MiscQOL, Scales, NPC, Weapons, Items, IDs
import scripts.Interactables
game = "XCDE"
scripts.Interactables.Game = game

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

EnemyDropOption = Option("Enemy Drops", General, "Randomizes the chosen types of loot from enemies", [lambda: Items.EnemyDrops()], descData=lambda: Items.EnemyDropsDesc())
EnemyDropOptions_Materials = SubOption("Materials", EnemyDropOption)
EnemyDropOptions_Armor = SubOption("Armor", EnemyDropOption)
EnemyDropOptions_Weapons = SubOption("Weapons", EnemyDropOption)
EnemyDropOptions_ArtBooks = SubOption("Art Books", EnemyDropOption)

CollectableOptions = Option("Collectable Orbs", General, "Randomizes collectables on the field into the chosen types", [lambda: Items.Collectables()], descData=lambda: Items.CollectDesc())
CollectableOptions_Collectables = SubOption("Collectables", CollectableOptions)
CollectableOptions_Collectables_Spinbox = SubSpinbox(CollectableOptions_Collectables, default=30, description=weightsSpinDescription)
CollectableOptions_Materials = SubOption("Materials", CollectableOptions)
CollectableOptions_Materials_Spinbox = SubSpinbox(CollectableOptions_Materials, default=30)
CollectableOptions_Armor = SubOption("Armor", CollectableOptions)
CollectableOptions_Armor_Spinbox = SubSpinbox(CollectableOptions_Armor, default=5)
CollectableOptions_Weapons = SubOption("Weapons", CollectableOptions)
CollectableOptions_Weapons_Spinbox = SubSpinbox(CollectableOptions_Weapons, default=5)
CollectableOptions_Gems = SubOption("Gems", CollectableOptions)
CollectableOptions_Gems_Spinbox = SubSpinbox(CollectableOptions_Gems, default=10)
CollectableOptions_ArtBooks = SubOption("Art Books", CollectableOptions)
CollectableOptions_ArtBooks_Spinbox = SubSpinbox(CollectableOptions_ArtBooks, default=1)

CollectapediaOptions = Option("Collectapedia Rewards", General, "Randomizes rewards from the collectapedia into the chosen types", [lambda: Items.Collectapedia()], descData=lambda: Items.CollectapediaDesc())
CollectapediaOptions_Collectables = SubOption("Collectables", CollectapediaOptions)
CollectapediaOptions_Collectables_Spinbox = SubSpinbox(CollectapediaOptions_Collectables, default=1, description=weightsSpinDescription)
CollectapediaOptions_Materials = SubOption("Materials", CollectapediaOptions)
CollectapediaOptions_Materials_Spinbox = SubSpinbox(CollectapediaOptions_Materials, default=1)
CollectapediaOptions_Armor = SubOption("Armor", CollectapediaOptions)
CollectapediaOptions_Armor_Spinbox = SubSpinbox(CollectapediaOptions_Armor, default=15)
CollectapediaOptions_Weapons = SubOption("Weapons", CollectapediaOptions)
CollectapediaOptions_Weapons_Spinbox = SubSpinbox(CollectapediaOptions_Weapons, default=15)
CollectapediaOptions_Gems = SubOption("Gems", CollectapediaOptions)
CollectapediaOptions_Gems_Spinbox = SubSpinbox(CollectapediaOptions_Gems, default=15)
CollectapediaOptions_ArtBooks = SubOption("Art Books", CollectapediaOptions)
CollectapediaOptions_ArtBooks_Spinbox = SubSpinbox(CollectapediaOptions_ArtBooks, default=10)

GiantsChestOption = Option("Giants Chests", General, "Randomizes the contents of Giants Chests into the chosen types", [lambda: Items.GiantsChests()], descData=lambda: Items.GiantsChestsDesc())
GiantsChestOptions_Collectables = SubOption("Collectables", GiantsChestOption, defState=False)
GiantsChestOptions_Collectables_Spinbox = SubSpinbox(GiantsChestOptions_Collectables, default=0, description=weightsSpinDescription)
GiantsChestOptions_Materials = SubOption("Materials", GiantsChestOption)
GiantsChestOptions_Materials_Spinbox = SubSpinbox(GiantsChestOptions_Materials, default=1)
GiantsChestOptions_Armor = SubOption("Armor", GiantsChestOption)
GiantsChestOptions_Armor_Spinbox = SubSpinbox(GiantsChestOptions_Armor, default=10)
GiantsChestOptions_Weapons = SubOption("Weapons", GiantsChestOption)
GiantsChestOptions_Weapons_Spinbox = SubSpinbox(GiantsChestOptions_Weapons, default=10)
GiantsChestOptions_Gems = SubOption("Gems", GiantsChestOption)
GiantsChestOptions_Gems_Spinbox = SubSpinbox(GiantsChestOptions_Gems, default=10)
GiantsChestOptions_ArtBooks = SubOption("Art Books", GiantsChestOption)
GiantsChestOptions_ArtBooks_Spinbox = SubSpinbox(GiantsChestOptions_ArtBooks, default=10)

QuestRewardsOption = Option("Quest Rewards", General, "Randomizes the rewards from quests into the chosen types", [lambda: Items.QuestRewards()], descData=lambda: Items.QuestRewardsDesc())
QuestRewardsOptions_Collectables = SubOption("Collectables", QuestRewardsOption)
QuestRewardsOptions_Collectables_Spinbox = SubSpinbox(QuestRewardsOptions_Collectables, default=1, description=weightsSpinDescription)
QuestRewardsOptions_Materials = SubOption("Materials", QuestRewardsOption)
QuestRewardsOptions_Materials_Spinbox = SubSpinbox(QuestRewardsOptions_Materials, default=5)
QuestRewardsOptions_Armor = SubOption("Armor", QuestRewardsOption)
QuestRewardsOptions_Armor_Spinbox = SubSpinbox(QuestRewardsOptions_Armor, default=10)
QuestRewardsOptions_Weapons = SubOption("Weapons", QuestRewardsOption)
QuestRewardsOptions_Weapons_Spinbox = SubSpinbox(QuestRewardsOptions_Weapons, default=10)
QuestRewardsOptions_Gems = SubOption("Gems", QuestRewardsOption)
QuestRewardsOptions_Gems_Spinbox = SubSpinbox(QuestRewardsOptions_Gems, default=10)
QuestRewardsOptions_ArtBooks = SubOption("Art Books", QuestRewardsOption)
QuestRewardsOptions_ArtBooks_Spinbox = SubSpinbox(QuestRewardsOptions_ArtBooks, default=2)
# https://xenobladedata.github.io/xb1de/bdat/bdat_common/FLD_valpoplist.html#1 Red orbs found here not sure what to do with them yet

# Enemy
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: EnemiesScript.Enemies(IDs.NormalEnemies, NormalEnemyOption, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption_Size.GetState(), NormalEnemyOption_OopsAll, NormalEnemyOption_OopsAll_Dropdown)], descData=lambda: EnemiesScript.EnemyDesc(NormalEnemyOption.name))
NormalEnemyOption_Spinbox = Spinbox(NormalEnemyOption)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Normal_Spinbox = SubSpinbox(NormalEnemyOption_Normal, default=15, description=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Unique_Spinbox = SubSpinbox(NormalEnemyOption_Unique, default=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Boss_Spinbox = SubSpinbox(NormalEnemyOption_Boss, default=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, defState=False)
NormalEnemyOption_Superboss_Spinbox = SubSpinbox(NormalEnemyOption_Superboss, default=1)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)
NormalEnemyOption_OopsAll = SubOption("Oops All", NormalEnemyOption, defState=False)
NormalEnemyOption_OopsAll_Dropdown = SubDropdown(NormalEnemyOption_OopsAll, EnemiesScript.GetOopsAllDropdowns())
NormalEnemyOption_Mult = SubOption("Multiply Enemy Count", NormalEnemyOption,  [lambda: EnemiesScript.MultiplyEnemies(NormalEnemyOption_Mult_Spinbox.GetState(), IDs.NormalEnemies)])
NormalEnemyOption_Mult_Spinbox = SubSpinbox(NormalEnemyOption_Mult, min=2, max=4, increment=1, default=2, description="x Enemies")

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: EnemiesScript.Enemies(IDs.UniqueEnemies + IDs.SuperbossEnemies, UniqueEnemyOption, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption_Size.GetState(), UniqueEnemyOption_OopsAll, UniqueEnemyOption_OopsAll_Dropdown)], descData=lambda: EnemiesScript.EnemyDesc(UniqueEnemyOption.name))
UniqueEnemyOption_Spinbox = Spinbox(UniqueEnemyOption)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Normal_Spinbox = SubSpinbox(UniqueEnemyOption_Normal, default=1, description=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Unique_Spinbox = SubSpinbox(UniqueEnemyOption_Unique, default=15)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Boss_Spinbox = SubSpinbox(UniqueEnemyOption_Boss, default=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss_Spinbox = SubSpinbox(UniqueEnemyOption_Superboss, default=2)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)
UniqueEnemyOption_OopsAll = SubOption("Oops All", UniqueEnemyOption, defState=False)
UniqueEnemyOption_OopsAll_Dropdown = SubDropdown(UniqueEnemyOption_OopsAll, EnemiesScript.GetOopsAllDropdowns())
UniqueEnemyOption_Mult = SubOption("Multiply Enemy Count", UniqueEnemyOption,  [lambda: EnemiesScript.MultiplyEnemies(UniqueEnemyOption_Mult_Spinbox.GetState(), IDs.UniqueEnemies)])
UniqueEnemyOption_Mult_Spinbox = SubSpinbox(UniqueEnemyOption_Mult, min=2, max=4, increment=1, default=2, description="x Enemies")

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: EnemiesScript.Enemies(IDs.BossEnemies, BossEnemyOption, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, True, BossEnemyOption_OopsAll, BossEnemyOption_OopsAll_Dropdown, BossEnemyOption_FinalBoss.GetState()), lambda: EnemiesScript.EgilArenaFix()], descData=lambda: EnemiesScript.EnemyDesc(BossEnemyOption.name))
BossEnemyOption_Spinbox = Spinbox(BossEnemyOption)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
BossEnemyOption_Normal_Spinbox = SubSpinbox(BossEnemyOption_Normal, default=2, description=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
BossEnemyOption_Unique_Spinbox = SubSpinbox(BossEnemyOption_Unique, default=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
BossEnemyOption_Boss_Spinbox = SubSpinbox(BossEnemyOption_Boss, default=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False)
BossEnemyOption_Superboss_Spinbox = SubSpinbox(BossEnemyOption_Superboss, default=1)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)
BossEnemyOption_OopsAll = SubOption("Oops All", BossEnemyOption, defState=False)
BossEnemyOption_OopsAll_Dropdown = SubDropdown(BossEnemyOption_OopsAll, EnemiesScript.GetOopsAllDropdowns())
BossEnemyOption_Mult = SubOption("Multiply Enemy Count", BossEnemyOption,  [lambda: EnemiesScript.MultiplyEnemies(BossEnemyOption_Mult_Spinbox.GetState(), IDs.LockEnemyFights + IDs.NonLockRequiredFights)])
BossEnemyOption_Mult_Spinbox = SubSpinbox(BossEnemyOption_Mult, min=2, max=4, increment=1, default=2, description="x Enemies")

# FinalBossOption = Option("Final Boss", Enemies, "Forces the final boss to be one of your choices")

# Character
GemOption = Option("Gems", Character, "Randomizes the effects of Gems and Crystals", [lambda: Gems.Gems()], descData=lambda: Gems.GemDescriptions())
GemOption_Power = SubOption("Power", GemOption)
GemOption_Effect = SubOption("Effects", GemOption)
GemOption_Unused = SubOption("Unused Effects", GemOption)
GemOption_FreeEquip = SubOption("Freely Equip to Weapons/Armor", GemOption)
GemOption_NoCap = SubOption("Gem Caps", GemOption)
AffinityTreeOption = Option("Skill Trees", Character, "Randomizes all character's skill trees", [lambda: SkillTrees.SkillRando()], descData=lambda: SkillTrees.SkillTreeDesc())
AffinityTreeOption_Spinbox = Spinbox(AffinityTreeOption)
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
TutorialSkipsOption = Option("Tutorial Skips", QOL, "Skips tutorial popups", filePlaceCommands=[lambda: XCRandomizer.FilePlacer(["Loader/plugins/xcdeRemoveTutorials.nro"], "../skyline/plugins", game=game)])
FasterLvOption = Option("EXP Boost", QOL, "Decreases level up requirements by a set amount (Recommended 3x to rush the story)", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], [f'row[key] // {FasterLvOption_Spinbox.GetState()}'])])
FasterLvOption_Spinbox = Spinbox(FasterLvOption, 0, 255, 1, 3, description="x Faster")
FasterSkillTrees = Option("SP Boost", QOL, "Decreases SP (skill point) requirements for skill trees", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_PSVskill.json"], ["point_PP"], [f'row[key] // {FasterSkillTrees_Spinbox.GetState()}'])])
FasterSkillTrees_Spinbox = Spinbox(FasterSkillTrees, 0, 255, 1, 2, description="x Faster")
FasterArtLevels = Option("AP Boost", QOL, "Increases AP (art point) gains for art level ups",[lambda: Helper.MathmaticalColumnAdjust(["./XCDE/JsonOutputs/bdat_common/BTL_growlist.json"], ["en_ap"], [f'row[key] * {FasterArtLevels_Spinbox.GetState()}'])])
FasterArtLevels_Spinbox = Spinbox(FasterArtLevels, 0, 255, 1, 2, description="x Faster")
MovespeedOption = Option("Quickstep", QOL, "The gem man will gift you two free quickstep gems", [lambda: MiscQOL.Quickstep()])
MovespeedOption_Spinbox = Spinbox(MovespeedOption, max=100, description="% Speed")
AreaAffinityOption = Option("Easy Affinity", QOL, "Area affinity is maxed out after any quest", [lambda: MiscQOL.QuestAffinity()])


# CutsceneSkipOption = Option("Cutscene Skips", QOL, "Skips all possible cutscenes", [lambda: Cutscenes.CutsceneSkipper()])

# Funny
# EnemyScaleOption = Option("Enemy Scale", Funny, "Randomizes a % of enemy sizes.", [lambda: Scales.EnemyScales()], hasSpinBox=True)
NPCScaleOption = Option("NPC Scale", Funny, "Randomizes a % of npc sizes.", [lambda: Scales.NPCScales()])
NPCScaleOption_Spinbox = Spinbox(NPCScaleOption, default=20)
RemoveStartingArmorOption = Option("Remove Starting Equipment", Funny, "Removes starting armor on all the main characters.", [lambda: Armor.RemoveStartingGear()])
NPCModelsOption = Option("NPC Models", Funny, "Randomizes NPC models *Experimental, can cause crashes", [lambda: NPC.NPCModelRando()])
NPCModelsOption_Spinbox = Spinbox(NPCModelsOption, default=30)

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html

# Collectapedia bdat_menu_item

# https://nenkai.github.io/XenoDocs/xc1de/tables/bdat_common/