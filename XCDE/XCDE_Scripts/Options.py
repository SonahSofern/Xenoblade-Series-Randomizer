import PcArts
from scripts.Interactables import Option, SubOption
from scripts import Helper
import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Tutorials, Armor, MiscQOL, Scales, NPC, Weapons, FieldCollectables, Cutscenes, IDs, Landmarks

OptionList =[]
Loot = 1
Character  = 2
Enemies = 3
Musica = 4
QOL = 5
Funny = 6
GameModeTab = 7

# General
TradeOption = Option("NPC Trades", Loot, "Randomizes chosen categories of NPC trades", [lambda: NPC.Trades()], descData=lambda: NPC.NPCTradesDesc())
TradeOption_Weapon = SubOption("Weapons", TradeOption)
TradeOption_Armor = SubOption("Armor", TradeOption)
TradeOption_Gem = SubOption("Gems", TradeOption)
TradeOption_Collectibles = SubOption("Collectibles", TradeOption)
TradeOption_Materials = SubOption("Materials", TradeOption)

CollectableOptions = Option("Collectable Orbs", Loot, "Randomizes collectables on the field into the chosen options", [lambda: FieldCollectables.FieldItems()], _hasSpinBox = True, descData=lambda: FieldCollectables.CollectDesc())
CollectableOptions_Collectables = SubOption("Collectables", CollectableOptions)
CollectableOptions_Materials = SubOption("Materials", CollectableOptions)
CollectableOptions_Armor = SubOption("Armor", CollectableOptions)
CollectableOptions_Weapons = SubOption("Weapons", CollectableOptions)
CollectableOptions_Gems = SubOption("Gems", CollectableOptions)
CollectableOptions_Crystals = SubOption("Crystals", CollectableOptions)
CollectableOptions_ArtBooks = SubOption("Art Books", CollectableOptions)
CollectableOptions_KeyItems = SubOption("Key Items", CollectableOptions)

CollectapediaOption = Option("Collectapedia Rewards", Loot, "Randomizes", [])

EnemyDropOption = Option("Enemy Drops", Loot, "Randomizes", [])

QuestRewardsOption = Option("Quest Rewards", Loot, "Randomizes", [])

GiantsChestOption = Option("Giants Chests", Loot, "Randomizes", [])

ShopOption = Option("Shops", Loot, "Randomizes", []) # Key item rando settings would be fun 

# https://xenobladedata.github.io/xb1de/bdat/bdat_common/FLD_valpoplist.html#1 Red orbs found here not sure what to do with them yet

# Enemy
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: EnemiesScript.Enemies(IDs.NormalEnemies, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(NormalEnemyOption.name), _hasSpinBox = True)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: EnemiesScript.Enemies(IDs.UniqueEnemies + IDs.SuperbossEnemies, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(UniqueEnemyOption.name), _hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)

BossEnemyOption = Option("Story Bosses", Enemies, "Randomizes bosses into the chosen types", [lambda: EnemiesScript.Enemies(IDs.BossEnemies, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption), lambda: EnemiesScript.EgilArenaFix()], descData=lambda: EnemiesScript.EnemyDesc(BossEnemyOption.name), _hasSpinBox = True)
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
GemOption_NoCap = SubOption("Remove Gem Stat Caps", GemOption)
AffinityTreeOption = Option("Skill Trees", Character, "Randomizes all character's skill trees", [lambda: SkillTrees.SkillRando()], descData=lambda: SkillTrees.SkillTreeDesc(), _hasSpinBox = True)
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
FasterLvOption = Option("EXP Boost", QOL, "Decreases level up requirements by a set amount (Recommended 3x to rush the story).", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], _hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=3)
FasterSkillTrees = Option("SP Boost", QOL, "Decreases SP (skill point) requirements for skill trees", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_PSVskill.json"], ["point_PP"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], _hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=2)
FasterArtLevels = Option("AP Boost", QOL, "Increases AP (art point) gains for art level ups",[lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["en_exp"], [f'row[key] * {FasterLvOption.GetSpinbox()}'])], _hasSpinBox = True, _spinMin = 0, _spinMax = 256, _spinIncr = 1, _spinDesc = "x", spinDefault=2)
MovespeedOption = Option("Quickstep", QOL, "The gem man will gift you two free quickstep gems.", [lambda: MiscQOL.Quickstep()], _hasSpinBox=True, _spinDesc="% Speed", _spinMax=100)

# CutsceneSkipOption = Option("Cutscene Skips", QOL, "Skips all possible cutscenes", [lambda: Cutscenes.CutsceneSkipper()])

# Funny
EnemyScaleOption = Option("Enemy Scale", Funny, "Randomizes a % of enemy sizes.", [lambda: Scales.EnemyScales()], _hasSpinBox=True)
NPCScaleOption = Option("NPC Scale", Funny, "Randomizes a % of npc sizes.", [lambda: Scales.NPCScales()], _hasSpinBox = True)
RemoveStartingArmorOption = Option("Remove Starting Equipment", Funny, "Removes starting armor on all the main characters.", [lambda: Armor.RemoveStartingGear()])
NPCModelsOption = Option("NPC Models", Funny, "Randomizes NPC models *Experimental, can cause crashes", [lambda: NPC.NPCModelRando()], _hasSpinBox = True)

# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html

# Collectapedia bdat_menu_item