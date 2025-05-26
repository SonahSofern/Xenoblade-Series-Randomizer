from tkinter import ttk
from scripts import JSONParser,Helper
from IDs import *
from tkinter import *
import _Accessories, _DriverArts, SkillTrees, _AuxCores, IDs, _GreenSkills, _WeaponChips, EnemyRandoLogic, _EnemyEnhancements, _EnemyArts, MusicShuffling, TrustBeam, CoreCrystalAdjustments, BladeWeaponClassRando
import TutorialShortening, GachaModifications, FieldSkillAdjustments, Enhancements, BigItems, RaceMode, UMHuntMain, Cosmetics, AccessoryShops, CollectionPoints, PouchItemShops, TreasureChests, ButtonCombos, EnemyDrops, _EleCombo
import _YellowSkills, _BladeSpecials, Scales, DLCFlagQOL, CharacterRandomization
import TornaMain
from scripts.Interactables import Option, SubOption
# Prio
First = 0
Last = 100

General = 1
Driver  = 2
Blade = 3
Enemies = 4
Misce = 5
QOL = 6
Funny = 7
CosmeticsTab = 8
GameModeTab = 9

# General
AccessoryShopsOption = Option("Accessory Shops", General, "Randomizes the contents of Accessory Shops", [lambda: AccessoryShops.RandoAccessoryShops()], _hasSpinBox = True, descData=lambda: AccessoryShops.AccessoryShopDescription())
AccessoryShopsOption_Accessories = SubOption("Accessories", AccessoryShopsOption)
AccessoryShopsOption_TornaAccessories = SubOption("Torna Accessories", AccessoryShopsOption)
AccessoryShopsOption_WeaponChips = SubOption("Weapon Chips", AccessoryShopsOption)
AccessoryShopsOption_AuxCores = SubOption("Aux Cores", AccessoryShopsOption)
AccessoryShopsOption_RefinedAuxCores = SubOption("Refined Aux Cores", AccessoryShopsOption)
AccessoryShopsOption_CoreCrystals = SubOption("Core Crystals", AccessoryShopsOption)
AccessoryShopsOption_Deeds = SubOption("Shop Deeds", AccessoryShopsOption)
AccessoryShopsOption_CollectionPointMaterials = SubOption("Collection Point Materials", AccessoryShopsOption)
AccessoryShopsOption_PouchItems = SubOption("Pouch Items", AccessoryShopsOption)
CollectionPointsOption = Option("Collection Points", General, "Randomizes the contents of Collection Points", [lambda: CollectionPoints.RandoCollectionPoints()], _hasSpinBox = True, descData=lambda: CollectionPoints.CollectionPointDescriptions())
CollectionPointsOption_Accessories = SubOption("Accessories", CollectionPointsOption)
CollectionPointsOption_TornaAccessories = SubOption("Torna Accessories", CollectionPointsOption)
CollectionPointsOption_WeaponChips = SubOption("Weapon Chips", CollectionPointsOption)
CollectionPointsOption_AuxCores = SubOption("Aux Cores", CollectionPointsOption)
CollectionPointsOption_RefinedAuxCores = SubOption("Refined Aux Cores", CollectionPointsOption)
CollectionPointsOption_CoreCrystals = SubOption("Core Crystals", CollectionPointsOption)
CollectionPointsOption_Deeds = SubOption("Shop Deeds", CollectionPointsOption)
CollectionPointsOption_CollectionPointMaterials = SubOption("Collection Point Materials", CollectionPointsOption)
PouchItemShopOption = Option("Pouch Item Shops", General, "Randomizes the contents of Pouch Item Shops", [lambda: PouchItemShops.RandoPouchShops()], _hasSpinBox = True, descData=lambda: PouchItemShops.PouchItemShopDesc())
PouchItemShopOption_Accessories = SubOption("Accessories", PouchItemShopOption)
PouchItemShopOption_TornaAccessories = SubOption("Torna Accessories", PouchItemShopOption)
PouchItemShopOption_WeaponChips = SubOption("Weapon Chips", PouchItemShopOption)
PouchItemShopOption_AuxCores = SubOption("Aux Cores", PouchItemShopOption)
PouchItemShopOption_RefinedAuxCores = SubOption("Refined Aux Cores", PouchItemShopOption)
PouchItemShopOption_CoreCrystals = SubOption("Core Crystals", PouchItemShopOption)
PouchItemShopOption_Deeds = SubOption("Shop Deeds", PouchItemShopOption)
PouchItemShopOption_CollectionPointMaterials = SubOption("Collection Point Materials", PouchItemShopOption)
PouchItemShopOption_PouchItems = SubOption("Pouch Items", PouchItemShopOption)
TreasureChestOption = Option("Treasure Chests", General, "Randomizes the contents of Treasure Chests",[lambda: TreasureChests.RandoTreasureBoxes()], _prio = 51, _hasSpinBox = True, descData=lambda: TreasureChests.TreasureChestDescription())
TreasureChestOption_Accessories = SubOption("Accessories", TreasureChestOption)
TreasureChestOption_TornaAccessories = SubOption("Torna Accessories", TreasureChestOption)
TreasureChestOption_WeaponChips = SubOption("Weapon Chips", TreasureChestOption)
TreasureChestOption_AuxCores = SubOption("Aux Cores", TreasureChestOption)
TreasureChestOption_RefinedAuxCores = SubOption("Refined Aux Cores", TreasureChestOption)
TreasureChestOption_CoreCrystals = SubOption("Core Crystals", TreasureChestOption)
TreasureChestOption_Deeds = SubOption("Shop Deeds", TreasureChestOption)
TreasureChestOption_CollectionPointMaterials = SubOption("Collection Point Materials", TreasureChestOption)
WeaponChipShopOption = Option("Weapon Chip Shops", General, "Randomizes Weapon Chips in Weapon Chip Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)], descData=lambda: _WeaponChips.WeaponChipDesc())

# Drivers
DriversOption = Option("Driver", Driver, "Randomizes which drivers appear in the world", [lambda: CharacterRandomization.CharacterRandomization()], _resetCommands=[lambda: CharacterRandomization.resetGlobals()])
DriverAccessoriesOption = Option("Driver Accessories", Driver, "Randomizes effects of Accessories", [lambda: _Accessories.RandomizeAccessoryEnhancements()], descData=lambda: _Accessories.AccessoriesDesc())
DriverArtsOption = Option("Driver Arts", Driver, "Randomizes effects of all driver arts", [lambda: (_DriverArts.DriverArtRandomizer(), _DriverArts.GenCustomArtDescriptions("./XC2/_internal/JsonOutputs/common/BTL_Arts_Dr.json", "./XC2/_internal/JsonOutputs/common_ms/btl_arts_dr_cap.json"))], _hasSpinBox = True,spinDefault=40, descData=lambda: _DriverArts.DriverArtDescription())
DriverArtsOption_AutoAttacks = SubOption("Auto Attacks", DriverArtsOption, [], _defState = False)
DriverArtsOption_SingleReaction = SubOption("Single Reaction", DriverArtsOption, [])
DriverArtsOption_MultipleReactions = SubOption("Multiple Reactions", DriverArtsOption, [])
DriverArtsOption_Debuffs = SubOption("Debuffs", DriverArtsOption, [])
DriverArtsOption_Buffs = SubOption("Buffs", DriverArtsOption, [])
DriverArtsOption_Enhancements = SubOption("Enhancements", DriverArtsOption, [])
DriverArtsOption_Cooldown = SubOption("Cooldown", DriverArtsOption, [])
DriverArtsOption_Damage = SubOption("Damage", DriverArtsOption, [])
DriverArtsOption_AnimationSpeed = SubOption("Animation Speed", DriverArtsOption, [])
DriverArtsOption_AOE= SubOption("AOE", DriverArtsOption, [])
DriverSkillTreesOption = Option("Driver Skill Trees", Driver, "Randomizes driver's skill trees", [lambda: SkillTrees.RandomizeSkillEnhancements()], descData=lambda: SkillTrees.Descriptions())
DriverSkillTreesOption_NonstandardSkills = SubOption("Nonstandard Skills", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyArtsCancel = SubOption("Early Arts Cancel", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyXYBAttack = SubOption("Early XYB Attack", DriverSkillTreesOption)

# Blades
BladesOption = Option("Blades", Blade, "Randomizes when blades appear in the story", [lambda: CharacterRandomization.CharacterRandomization()], _hasSpinBox = True, _resetCommands=[lambda: CharacterRandomization.resetGlobals()])
BladesOption_Dromarch = SubOption("Randomize Dromarch", BladesOption)
BladesOption_Healer = SubOption("Guaranteed Healer", BladesOption)
BladeAuxCoresOption = Option("Blade Aux Cores", Blade, "Randomizes the effects of Aux Cores", [lambda: _AuxCores.RandomizeAuxCoreEnhancements()])
BladeAuxCoreSlotsOption = Option("Blade Aux Core Slots", Blade, "Randomizes a Blade's maximum Aux Core Slots", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), IDs.BladeAuxCoreSlotDistribution)])
BladeArtsOption = Option("Blade Arts", Blade, "Randomizes a Blade's combat arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), BladeArts, BladeArts)])
BladeBattleSkillsOption = Option("Blade Battle Skills", Blade, "Randomizes a Blade's battle (yellow) skill tree", [lambda: _YellowSkills.RandomizeBattleSkills()], _hasSpinBox = True)
BladeBattleSkillsOption_Duplicates = SubOption("Allow Duplicates", BladeBattleSkillsOption)
BladeFieldSkillsOption = Option("Blade Field Skills", Blade, "Randomizes a Blade's field (green) skill tree", [lambda: _GreenSkills.RandomizeFieldSkills()])
BladeFieldSkillsOption_QuestSkills = SubOption("Quest Skills", BladeFieldSkillsOption)
BladeCooldownOption = Option("Blade Cooldowns", Blade, "Randomizes a Blade's swap cooldown", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
BladeDefensesOption = Option("Blade Defenses", Blade, "Randomizes a Blade's Physical and Ether Defense", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)])
BladeElementsOption = Option("Blade Elements", Blade, "Randomizes a Blade's element", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))])
BladeModsOption = Option("Blade Stat Mods", Blade, "Randomizes a Blade's Stat Modifiers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(1,100), BladeModDistribution)])
BladeSpecialButtonsOption = Option("Blade Button Combos", Blade, "Randomizes what button a special uses for its button challenge",[lambda: ButtonCombos.BladeSpecialButtonChallenges()])
BladeSpecialButtonsOption_A = SubOption("A", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_B = SubOption("B", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_X = SubOption("X", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_Y = SubOption("Y", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_Mystery = SubOption("?", BladeSpecialButtonsOption)
BladeSpecialOption = Option("Blade Specials", Blade, "Randomizes each hit of a blade special to have a random effects", [lambda:(_BladeSpecials.BladeSpecials())], _hasSpinBox = True)
BladeSpecialOption_Reaction = SubOption("Reactions", BladeSpecialOption)
BladeSpecialOption_Enhancement = SubOption("Enhancement", BladeSpecialOption)
BladeSpecialOption_Debuffs = SubOption("Debuff", BladeSpecialOption)
BladeWeaponChipsOption = Option("Blade Weapon Chips", Blade, "Randomizes the effects of weapon chips", [lambda:_WeaponChips.ChangeWeaponRankNames()], _hasSpinBox = True)
BladeWeaponChipsOption_AutoAtk = SubOption("Auto Attacks", BladeWeaponChipsOption, _defState= True)
BladeWeaponChipsOption_CritRate = SubOption("Crit Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["CriRate"],Helper.InclRange(0,100), BladeWeaponCritDistribution)],_defState= True)
BladeWeaponChipsOption_GuardRate = SubOption("Guard Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["GuardRate"],Helper.InclRange(0,100), BladeWeaponGuardDistribution)],_defState= True)
BladeWeaponChipsOption_Enhancement = SubOption("Enhancements", BladeWeaponChipsOption, [lambda: _WeaponChips.RandomizeWeaponEnhancements()], _defState= True)
BladeWeaponClassOption = Option("Blade Weapon Class", Blade, "Randomizes weapon roles (ATK, TNK, HLR)", [lambda: BladeWeaponClassRando.BladeWeaponClassRandomization()], descData=lambda: BladeWeaponClassRando.BladeWeaponClassDesc())
BladeCombosOption = Option("Blade Combos", Blade, "", [lambda: _EleCombo.BladeComboRandomization()])
BladeCombosOption_ElementRoutes = SubOption("Element Routes", BladeCombosOption)
BladeCombosOption_Damage = SubOption("Damage", BladeCombosOption)
BladeCombosOption_DOT = SubOption("DoT", BladeCombosOption)
BladeCombosOption_Reactions = SubOption("Reactions", BladeCombosOption)
BladeCombosOption_AOE = SubOption("AOE", BladeCombosOption)

# Enemies
EnemiesOption = Option("Enemies", Enemies, "Randomizes what enemies appear in the world", [lambda: EnemyRandoLogic.EnemyLogic()], descData= lambda: EnemyRandoLogic.Description())
EnemiesOption_Bosses = SubOption("Bosses", EnemiesOption)
EnemiesOption_QuestEnemies = SubOption("Quest Enemies", EnemiesOption)
EnemiesOption_UniqueMonsters = SubOption("Unique Monsters", EnemiesOption)
EnemiesOption_Superbosses = SubOption("Superbosses", EnemiesOption)
EnemiesOption_NormalEnemies = SubOption("Normal Enemies", EnemiesOption)
EnemiesOption_MixedTypes = SubOption("Mix Enemies Between Types", EnemiesOption)
EnemiesOption_BalancedLevels = SubOption("Balanced Levels", EnemiesOption)
EnemiesOption_BalanceEnemyGroups = SubOption("Balanced Enemy Groups", EnemiesOption)
EnemyEnhancementsOption = Option("Enemy Enhancements", Enemies, "Gives enemies a random enhancement; it is displayed by their name", [lambda: _EnemyEnhancements.EnemyEnhances()], _hasSpinBox = True, descData=lambda: _EnemyEnhancements.EnemyEnhancementDescriptions())
EnemyArtEffectsOption = Option("Enemy Art Effects", Enemies, "Gives enemies a random bonus effect to their arts; it is displayed by their art's name", [lambda: _EnemyArts.EnemyArtAttributes()], _hasSpinBox = True)
EnemyArtEffectsOption_Reactions = SubOption("Reactions", EnemyArtEffectsOption)
EnemyArtEffectsOption_AOE = SubOption("AOE", EnemyArtEffectsOption)
EnemyArtEffectsOption_Buffs = SubOption("Buffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Debuffs = SubOption("Debuffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Enhancements = SubOption("Enhancements", EnemyArtEffectsOption)
EnemyDropOption = Option("Enemy Drops", Enemies, "Randomizes enemy drops/loot", [lambda: EnemyDrops.RandoEnemyDrops()], _hasSpinBox = True)
EnemyDropOption_Accessories = SubOption("Accessories", EnemyDropOption)
EnemyDropOption_TornaAccessories = SubOption("Torna Accessories", EnemyDropOption)
EnemyDropOption_WeaponChips = SubOption("Weapon Chips", EnemyDropOption)
EnemyDropOption_AuxCores = SubOption("Aux Cores", EnemyDropOption)
EnemyDropOption_RefinedAuxCores = SubOption("Refined Aux Cores", EnemyDropOption)
EnemyDropOption_CoreCrystals = SubOption("Core Crystals", EnemyDropOption)
EnemyDropOption_Deeds = SubOption("Shop Deeds", EnemyDropOption)
EnemyDropOption_CollectionPointMaterials = SubOption("Collection Point Materials", EnemyDropOption)
EnemyAggroOption = Option("Enemy Aggro", Enemies, "The percentage of all non-boss and non-quest enemies that will aggro the player", [lambda: EnemyRandoLogic.EnemyAggroProportion()], _hasSpinBox = True)
EnemyMovespeedOption = Option("Enemy Movespeed", Enemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))])

# Misc
MusicOption = Option("Music", Misce, "Randomizes Music", [lambda: MusicShuffling.MusicShuffle()], descData=lambda: MusicShuffling.MusicRandoDescription())
MusicOption_MixBattleAndEnv = SubOption("Mix Battle and Environment Themes", MusicOption, _defState = False)
TrustLineOption = Option("Trust Lines", Misce, "Randomizes blade-driver trust lines in battle (colors, power, etc.)", [lambda: TrustBeam.BeamRandomizer()])
CustomCoreCrystalOption = Option("Custom Core Crystals", Misce, "Adds Core Crystals with guaranteed Rare Blades to Treasure Chests", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()], _hasSpinBox = True, _spinDesc = "% of Chests", descData= lambda: CoreCrystalAdjustments.Description())
# DifficultyOption = Option("Difficulty", Misce, "Forces this difficulty, regardless of what is chosen in the options menu")
# DifficultyOption_Easy = SubOption("Easy", DifficultyOption)
# DifficultyOption_Normal = SubOption("Normal", DifficultyOption)
# DifficultyOption_BOC = SubOption("Bringer of Chaos", DifficultyOption)
# DifficultyOption_Ultimate = SubOption("Ultimate", DifficultyOption)

# QOL
FreelyEngageBladesOption = Option("Freely Engage Blades", QOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])
CTMCOption = Option("Chest Type Matches Contents", QOL, "Chest model and label changes depending on tier of loot", [lambda: RaceMode.ChestTypeMatching()], _prio = 95, descData = lambda: RaceMode.CTMCDescription())
TreasureChestVisOption =  Option("Treasure Chest Visibility", QOL, "Increases the range you can see treasure chests from", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
RemoveFieldSkillsOption = Option("Remove Story Field Skills", QOL, "Removes field skill checks", [lambda: FieldSkillAdjustments.RemoveFieldSkills()], ["Remove All Field Skills", []])
RemoveFieldSkillsOption_AllFieldSkills = SubOption("Remove All Field Skills", RemoveFieldSkillsOption)
EverlastingPouchItemsOption = Option("Everlasting Pouch Items", QOL, "Makes Pouch Items last as long as possible", [lambda: JSONParser.ChangeJSONFile(["common/ITM_FavoriteList.json"],["Time"], Helper.InclRange(0,255), [6099])])
CondenseGoldOption = Option("Condense Gold Loot", QOL, "Condenses gold in chests so you can see other items", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"),["goldPopMin", "goldPopMax"], Helper.InclRange(0,100000), [1])])
MutePopupsOption = Option("Mute Popups", QOL, "Stops blade skill and pouch item refill popups", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[89], ["sheet06"], [""])])
MutePopupsOption_Landmarks = SubOption("Landmarks", MutePopupsOption, [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[85], ["sheet04"], [""])])
EnhancementDisplayOption = Option("Enhancement Display", QOL, "Shows when enhancements activate in battle", [lambda: Enhancements.SearchAndSetDisplayIDs()])
EasySkillTreesOption = Option("Fast Blade Skill Trees", QOL, "Makes trust the only condition for levelling up a blade's skill tree", [lambda: SkillTrees.BladeSkillTreeShortening()])
FasterDriverSkillTrees = Option("Fast Driver Skill Trees", QOL, "Decreases SP required for each node")
FasterDriverSkillTrees_2 = SubOption("2x", FasterDriverSkillTrees, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], ['row[key] // 2'])], _defState = False)
FasterDriverSkillTrees_4 = SubOption("4x", FasterDriverSkillTrees, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], ['row[key] // 4'])], _defState = False)
FasterDriverSkillTrees_8 = SubOption("8x", FasterDriverSkillTrees, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], ['row[key] // 8'])], _defState = False)
FasterDriverSkillTrees_16 = SubOption("16x", FasterDriverSkillTrees, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], ['row[key] // 16'])], _defState = False)
FasterDriverSkillTrees_32 = SubOption("32x", FasterDriverSkillTrees, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/_internal/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], ['row[key] // 32'])], _defState = False)
FasterLevelsOption = Option("Faster Levels", QOL, "Decreases EXP required for each levelup")
FasterLevelsOption_2 = SubOption("2x", FasterLevelsOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 2'])], _defState = False)
FasterLevelsOption_4 = SubOption("4x", FasterLevelsOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 4'])], _defState = False)
FasterLevelsOption_8 = SubOption("8x", FasterLevelsOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 8'])], _defState = False)
FasterLevelsOption_16 = SubOption("16x", FasterLevelsOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 16'])], _defState = False)
FasterLevelsOption_32 = SubOption("32x", FasterLevelsOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 32'])], _defState = False)
ShortcutsOption = Option("Shortcuts", QOL, "Various speedups for the main story quests")
ShortenTutorialOption = SubOption("Tutorials Skip", ShortcutsOption, [lambda: TutorialShortening.ShortenedTutorial()])
ShortcutsOption_PuzzleTreeWoodSkip = SubOption("Puzzletree Wood Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCollect.json"],[18,19], ["Count"], 0)])
ShortcutsOption_GatherNia = SubOption("Nia Rumours Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCondition.json"],[7], ["ConditionID"], 1)])
StartwithIncreasedMovespeedOption = Option("Increased Movespeed", QOL, "Adds a shop deed to the DLC items to increase your movement speed", [lambda: DLCFlagQOL.AddMovespeedDeed()], _hasSpinBox = True, _spinMin = 0, _spinMax = 50, _spinIncr = 5, _spinDesc = "% Increase (x10)", _spinWidth = 5, spinDefault = 50)
NewGamePlusFlagsOptions = Option("NG+ Flags", QOL, "Enables many NG+ behaviours like unlocked hidden driver skill trees, unlocked chain attacks from the start, unlocked blade slots etc. These must be accepted from the DLC Menu to work.", [lambda: DLCFlagQOL.CreateDLCtoSetFlag(["2nd Blade Equip Slot", "3rd Blade Equip Slot"], [35327, 35328], [2,2], [0,0], [1,1], [1,1])])
NewGamePlusFlagsOptions_Blades = SubOption("NG+ Blades", NewGamePlusFlagsOptions, [lambda: GachaModifications.UnlockNGPlusBlades()])
NewGamePlusFlagsOptionsHiddenDriverSkillTree = SubOption("Hidden Skill Tree Unlocked", NewGamePlusFlagsOptions, [lambda: DLCFlagQOL.FixIssuesCausedByNGPlusFlag()])

# Funny
ProjTreasureChestOption = Option("Projectile Treasure Chests", Funny, "Launches your items from chests",[lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [15])])
BladeSizeOption = Option("Blade Size", Funny, "Randomizes the size of Blades", [lambda: Scales.BladeScales()], _hasSpinBox = True)
NPCSizeOption = Option("NPC Size", Funny, "Randomizes the size of NPCs", [lambda: Scales.NPCScales()], _hasSpinBox = True)
EnemySizeOption = Option("Enemy Size", Funny, "Randomizes the size of enemies", [lambda: Scales.EnemyScales()], _hasSpinBox = True)
FieldItemOption = Option("Field Item Size", Funny, "Randomizes the size and spin rate of items dropped on the field.", [lambda: BigItems.BigItemsRando()], descData=lambda: BigItems.BigItemsDesc())

# Cosmetics
BladeWeaponCosmeticsOption = Option("Blade Weapon Cosmetics", CosmeticsTab, "Keeps all default weapon models regardless of chips", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["OnlyWpn"], [0], [1])], spinDefault=25)
CosmeticsOption = Option("Character Outfits", CosmeticsTab, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics.Cosmetics()],_prio=51, _hasSpinBox = True, descData=lambda: Cosmetics.CosmeticsDescription()) # Sub are created by another class
for opt in Cosmetics.CosmeticsList: # To gen these since listing them here would be annoying
    opt.CreateSubOptions(CosmeticsOption)

# Game Modes
RaceModeOption = Option("Race Mode", GameModeTab, "Play through a condensed version of the game in this mode!", [lambda: RaceMode.RaceModeChanging()], descData = lambda: RaceMode.RaceModeDescription())
RaceModeOption_Zohar = SubOption("Zohar Fragment Hunt", RaceModeOption)
RaceModeOption_DLC = SubOption("DLC Item Removal", RaceModeOption)
UMHuntOption = Option("Unique Monster Hunt", GameModeTab, "Defeat Unique Monsters in this Roguelike mode!", [lambda: UMHuntMain.UMHunt()], _hasSpinBox = True, _spinMin = 1, _spinMax = 10, _spinIncr = 1, _spinDesc = "Round(s)", _spinWidth = 2, spinDefault = 10, descData= lambda: UMHuntMain.Description())
UMHuntOption_SuperbossWave = SubOption("Superboss Wave", UMHuntOption)
UMHuntOption_RandomLandmarks = SubOption("Random Starting Landmarks", UMHuntOption)

# Torna
# TornaMainOption = Option("Torna Randomization", GameModeTab, "WIP. Disabling any of the below options merely fills their rewards with non-progression items.", [lambda: TornaMain.AllTornaRando()])
# TornaOption_CollectionPoints = Option("Torna Collection Points", GameModeTab, "Randomizes collection point contents. Each collection point has the number of items equal to the spinbox, weighted equally." ,_hasSpinBox = True, _spinMin = 1, _spinMax = 4, _spinIncr = 1, _spinDesc = "Item(s)", _spinWidth = 1, spinDefault = 1)
# TornaOption_SideQuests = Option("Torna Side Quests", GameModeTab, "Randomizes sidequest rewards. Each sidequest has the number of rewards equal to the spinbox." ,_hasSpinBox = True, _spinMin = 1, _spinMax = 4, _spinIncr = 1, _spinDesc = "Item(s)", _spinWidth = 1, spinDefault = 1)
# TornaOption_EnemyDrops = Option("Torna Enemy Drops", GameModeTab, "Randomizes enemy drops. Each enemy drops a number of items equal to the spinbox upon defeat." ,_hasSpinBox = True, _spinMin = 1, _spinMax = 3, _spinIncr = 1, _spinDesc = "Item(s)", _spinWidth = 1, spinDefault = 1)
# TornaOption_TreasureChests = Option("Torna Treasure Chests", GameModeTab, "Randomizes treasure chest contents. Each chest contains a number of rewards equal to the spinbox." ,_hasSpinBox = True, _spinMin = 1, _spinMax = 7, _spinIncr = 1, _spinDesc = "Item(s)", _spinWidth = 1, spinDefault = 1)
# TornaOption_Shops = Option("Torna Shops", GameModeTab, "Randomizes items in shops and from traveling bards. Each shop contains a number of items equal to the spinbox, and are all purchaseable for gold." ,_hasSpinBox = True, _spinMin = 1, _spinMax = 16, _spinIncr = 1, _spinDesc = "Item(s)", _spinWidth = 2, spinDefault = 1)
# TornaOption_GroundItems = Option("Torna Ground Items", GameModeTab, "Randomizes items in the red bags on the ground. Each red bag contains 1 item.")
#TornaOption_ChooseLevel2CommunityReq = Option("Level 2 Community Req", GameModeTab, "Determines the number of people required for community.") # I don't know how to make this work in the game files for now.

# Currently Disabled for Various Reasons
# Blade Names (moved so that blade name rando doesn't mess up Race Mode getting blade IDs)
# GenStandardOption("Blade Names", TabBlades, "Randomizes a Blade's name", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
# GenStandardOption("Less UI", TabQOL, "Removes some of the unneccessary on screen UI (Blade Swap and Current Objective)", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03"], [""])])
# GenStandardOption("Screenshot Mode", TabQOL, "Removes most UI for screenshots", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03", "sheet04"], ""), lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[86], ["sheet02", "sheet03"], "")])
# CTMC (has to run after Race Mode in current iteration, needs to know what chests have what loot)
# GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
# GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
# GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
# GenStandardOption("Blade Weapons", TabBlades, "Randomizes a Blade Weapon type, for example Pyra can now be a Knuckle Claws user", [lambda: _BladeWeapons.WepRando()])
# GenStandardOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials,  list(set(BladeSpecials) - set([215])))]) works okay, but animations dont connect feels mid
# DebugLog.CreateDebugLog(OptionDictionary, Version, randoSeedEntry.get())
# GenStandardOption("Enemy Arts", TabEnemies, "Gives enemies new arts", [lambda: _EnemyArts.EnemyArts(OptionDictionary["Enemy Arts"]["spinBoxVal"].get())],optionType=Spinbox)
# GenStandardOption("Enemy Rage", TabEnemies, "Randomizes the effects of enemy enraged states", ["common/BTL_Aura"])   

