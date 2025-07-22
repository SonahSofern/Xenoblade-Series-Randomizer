from tkinter import ttk
from scripts import JSONParser,Helper
from XC2.XC2_Scripts.IDs import *
from tkinter import *
from XC2.XC2_Scripts import _Accessories, _DriverArts, SkillTrees, _AuxCores, IDs, _GreenSkills, _WeaponChips, EnemyRandoLogic, _EnemyEnhancements, _EnemyArts, MusicShuffling, TrustBeam, CoreCrystalAdjustments, BladeStats,TutorialShortening, GachaModifications, FieldSkillAdjustments, Enhancements, BigItems, RaceMode, UMHuntMain, Cosmetics, AccessoryShops, CollectionPoints, PouchItemShops, TreasureChests, ButtonCombos, EnemyDrops, _EleCombo,_YellowSkills, _BladeSpecials, Scales, DLCFlagQOL, CharacterRandomization, TornaMain, ObjectNameCleanup
from scripts.Interactables import Option, SubOption, MutuallyExclusivePairing
import scripts.Interactables
scripts.Interactables.Game = "XC2"
# Prio
First = 0
Last = 100

Items = 1
Driver  = 2
Blade = 3
Enemies = 4
Misce = 5
QOL = 6
Funny = 7
CosmeticsTab = 8
GameModeTab = 9
TornaTab = 10


Tabs = {
    Items: "🎁 Items",
    Driver: "🧍 Drivers",
    Blade: "🔷 Blades",
    Enemies: "💀 Enemies",
    Misce: "♪ Music",
    QOL: "🐇 Quality of Life",
    Funny: "😄 Funny",
    CosmeticsTab: "👚 Cosmetics",
    GameModeTab: "♘ Game Modes",
    TornaTab: "🞛 Torna"
}


# General
AccessoriesOption = Option("Accessories", Items, "Randomizes effects of Accessories", [lambda: _Accessories.RandomizeAccessoryEnhancements()], descData=lambda: _Accessories.AccessoriesDesc())
AuxCoresOption = Option("Aux Cores", Items, "Randomizes the effects of Aux Cores", [lambda: _AuxCores.RandomizeAuxCoreEnhancements()])
AccessoryShopsOption = Option("Accessory Shops", Items, "Randomizes the contents of Accessory Shops", [lambda: AccessoryShops.RandoAccessoryShops()], hasSpinBox = True, descData=lambda: AccessoryShops.AccessoryShopDescription())
AccessoryShopsOption_Accessories = SubOption("Accessories", AccessoryShopsOption)
AccessoryShopsOption_TornaAccessories = SubOption("Torna Accessories", AccessoryShopsOption)
AccessoryShopsOption_WeaponChips = SubOption("Weapon Chips", AccessoryShopsOption)
AccessoryShopsOption_AuxCores = SubOption("Aux Cores", AccessoryShopsOption)
AccessoryShopsOption_RefinedAuxCores = SubOption("Refined Aux Cores", AccessoryShopsOption)
AccessoryShopsOption_CoreCrystals = SubOption("Core Crystals", AccessoryShopsOption)
AccessoryShopsOption_Deeds = SubOption("Shop Deeds", AccessoryShopsOption)
AccessoryShopsOption_CollectionPointMaterials = SubOption("Collection Point Materials", AccessoryShopsOption)
AccessoryShopsOption_PouchItems = SubOption("Pouch Items", AccessoryShopsOption)
CollectionPointsOption = Option("Collection Points", Items, "Randomizes the contents of Collection Points", [lambda: CollectionPoints.RandoCollectionPoints()], hasSpinBox = True, descData=lambda: CollectionPoints.CollectionPointDescriptions())
CollectionPointsOption_Accessories = SubOption("Accessories", CollectionPointsOption)
CollectionPointsOption_TornaAccessories = SubOption("Torna Accessories", CollectionPointsOption)
CollectionPointsOption_WeaponChips = SubOption("Weapon Chips", CollectionPointsOption)
CollectionPointsOption_AuxCores = SubOption("Aux Cores", CollectionPointsOption)
CollectionPointsOption_RefinedAuxCores = SubOption("Refined Aux Cores", CollectionPointsOption)
CollectionPointsOption_CoreCrystals = SubOption("Core Crystals", CollectionPointsOption)
CollectionPointsOption_Deeds = SubOption("Shop Deeds", CollectionPointsOption)
CollectionPointsOption_CollectionPointMaterials = SubOption("Collection Point Materials", CollectionPointsOption)
PouchItemShopOption = Option("Pouch Item Shops", Items, "Randomizes the contents of Pouch Item Shops", [lambda: PouchItemShops.RandoPouchShops()], hasSpinBox = True, descData=lambda: PouchItemShops.PouchItemShopDesc())
PouchItemShopOption_Accessories = SubOption("Accessories", PouchItemShopOption)
PouchItemShopOption_TornaAccessories = SubOption("Torna Accessories", PouchItemShopOption)
PouchItemShopOption_WeaponChips = SubOption("Weapon Chips", PouchItemShopOption)
PouchItemShopOption_AuxCores = SubOption("Aux Cores", PouchItemShopOption)
PouchItemShopOption_RefinedAuxCores = SubOption("Refined Aux Cores", PouchItemShopOption)
PouchItemShopOption_CoreCrystals = SubOption("Core Crystals", PouchItemShopOption)
PouchItemShopOption_Deeds = SubOption("Shop Deeds", PouchItemShopOption)
PouchItemShopOption_CollectionPointMaterials = SubOption("Collection Point Materials", PouchItemShopOption)
PouchItemShopOption_PouchItems = SubOption("Pouch Items", PouchItemShopOption)
TreasureChestOption = Option("Treasure Chests", Items, "Randomizes the contents of Treasure Chests",[lambda: TreasureChests.RandoTreasureBoxes()], prio = 51, hasSpinBox = True, descData=lambda: TreasureChests.TreasureChestDescription())
TreasureChestOption_Accessories = SubOption("Accessories", TreasureChestOption)
TreasureChestOption_TornaAccessories = SubOption("Torna Accessories", TreasureChestOption)
TreasureChestOption_WeaponChips = SubOption("Weapon Chips", TreasureChestOption)
TreasureChestOption_AuxCores = SubOption("Aux Cores", TreasureChestOption)
TreasureChestOption_RefinedAuxCores = SubOption("Refined Aux Cores", TreasureChestOption)
TreasureChestOption_CoreCrystals = SubOption("Core Crystals", TreasureChestOption)
TreasureChestOption_Deeds = SubOption("Shop Deeds", TreasureChestOption)
TreasureChestOption_CollectionPointMaterials = SubOption("Collection Point Materials", TreasureChestOption)
WeaponChipShopOption = Option("Weapon Chip Shops", Items, "Randomizes Weapon Chips in Weapon Chip Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)], descData=lambda: _WeaponChips.WeaponChipDesc())

# Drivers
DriversOption = Option("Drivers", Driver, "Randomizes which drivers appear in the story", [lambda: CharacterRandomization.CharacterRandomization()], preRandoCommands=[lambda: CharacterRandomization.resetGlobals()], descData=lambda: CharacterRandomization.DriversDescriptions())
DriversOption_Nia = SubOption("Guarantee Early Nia", DriversOption, _defState = False)
DriverArtsOption = Option("Driver Arts", Driver, "Randomizes effects of all driver arts", [lambda: (_DriverArts.DriverArtRandomizer(), _DriverArts.GenCustomArtDescriptions("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", "./XC2/JsonOutputs/common_ms/btl_arts_dr_cap.json"))], hasSpinBox = True,spinDefault=40, descData=lambda: _DriverArts.DriverArtDescription())
spinArts = "%"
DriverArtsOption_AutoAttacks = SubOption("Auto Attacks", DriverArtsOption, [], _defState = False, hasSpinBox=True, spinDesc="% of auto attacks", spinDefault=20)
DriverArtsOption_SingleReaction = SubOption("Single Reaction", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_MultipleReactions = SubOption("Multiple Reactions", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_Debuffs = SubOption("Debuffs", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_Buffs = SubOption("Buffs", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_Enhancements = SubOption("Enhancements", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_Cooldown = SubOption("Cooldown", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_Damage = SubOption("Damage", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_AnimationSpeed = SubOption("Animation Speed", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverArtsOption_AOE= SubOption("AOE", DriverArtsOption, [], hasSpinBox=True, spinDesc=spinArts, spinDefault=20)
DriverSkillTreesOption = Option("Driver Skill Trees", Driver, "Randomizes driver's skill trees", [lambda: SkillTrees.RandomizeSkillEnhancements()], descData=lambda: SkillTrees.Descriptions())
DriverSkillTreesOption_NonstandardSkills = SubOption("Nonstandard Skills", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyArtsCancel = SubOption("Early Arts Cancel", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyXYBAttack = SubOption("Early XYB Attack", DriverSkillTreesOption)

# Blades
BladesOption = Option("Blades", Blade, "Randomizes when blades appear in the story", [lambda: CharacterRandomization.CharacterRandomization()], hasSpinBox = True, preRandoCommands=[lambda: CharacterRandomization.resetGlobals()], descData=lambda: CharacterRandomization.BladesDescriptions())
BladesOption_Dromarch = SubOption("Randomize Dromarch", BladesOption)
BladesOption_Healer = SubOption("Guarantee Healing Art", BladesOption)
BladeArtsOption = Option("Blade Arts", Blade, "Randomizes a Blade's combat arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), BladeArts, BladeArts)])
BladeBattleSkillsOption = Option("Blade Battle Skills", Blade, "Randomizes a Blade's battle (yellow) skill tree", [lambda: _YellowSkills.RandomizeBattleSkills()], hasSpinBox = True)
BladeBattleSkillsOption_Duplicates = SubOption("Allow Duplicates", BladeBattleSkillsOption)
BladeFieldSkillsOption = Option("Blade Field Skills", Blade, "Randomizes a Blade's field (green) skill tree", [lambda: _GreenSkills.RandomizeFieldSkills()])
BladeFieldSkillsOption_QuestSkills = SubOption("Quest Skills", BladeFieldSkillsOption)
BladeSpecialButtonsOption = Option("Blade Button Combos", Funny, "Randomizes what button a special uses for its button challenge",[lambda: ButtonCombos.BladeSpecialButtonChallenges()])
BladeSpecialButtonsOption_A = SubOption("A", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_B = SubOption("B", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_X = SubOption("X", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_Y = SubOption("Y", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_Mystery = SubOption("?", BladeSpecialButtonsOption)
BladeSpecialOption = Option("Blade Specials", Blade, "Randomizes each hit of a blade special to have a random effects", [lambda:(_BladeSpecials.BladeSpecials())], hasSpinBox = True)
BladeSpecialOption_Reaction = SubOption("Reactions", BladeSpecialOption)
BladeSpecialOption_Enhancement = SubOption("Enhancement", BladeSpecialOption)
BladeSpecialOption_Debuffs = SubOption("Debuff", BladeSpecialOption)
BladeWeaponChipsOption = Option("Blade Weapon Chips", Blade, "Randomizes the effects of weapon chips", [lambda:_WeaponChips.ChangeWeaponRankNames()], hasSpinBox = True)
BladeWeaponChipsOption_AutoAtk = SubOption("Auto Attacks", BladeWeaponChipsOption, _defState= True)
BladeWeaponChipsOption_CritRate = SubOption("Crit Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["CriRate"],Helper.InclRange(0,100), BladeWeaponCritDistribution)],_defState= True)
BladeWeaponChipsOption_GuardRate = SubOption("Guard Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["GuardRate"],Helper.InclRange(0,100), BladeWeaponGuardDistribution)],_defState= True)
BladeWeaponChipsOption_Enhancement = SubOption("Enhancements", BladeWeaponChipsOption, [lambda: _WeaponChips.RandomizeWeaponEnhancements()], _defState= True)
BladeCombosOption = Option("Blade Combos", Blade, "Randomizes blade elemental combos", [lambda: _EleCombo.BladeComboRandomization()], descData=lambda: _EleCombo.BladeCombosDescription())
BladeCombosOption_ElementRoutes = SubOption("Element Routes", BladeCombosOption)
BladeCombosOption_Damage = SubOption("Damage", BladeCombosOption)
BladeCombosOption_DOT = SubOption("DoT", BladeCombosOption)
BladeCombosOption_Reactions = SubOption("Reactions", BladeCombosOption)
BladeCombosOption_AOE = SubOption("AOE", BladeCombosOption)
BladeStatsOption = Option("Blade Stats", Blade, "Randomizes various stats of blades")
BladeStatsOption_AuxCoreSlots = SubOption("Aux Core Slots", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), IDs.BladeAuxCoreSlotDistribution)])
BladeStatsOption_Cooldown = SubOption("Cooldowns", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
BladeStatsOption_Element = SubOption("Elements", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))])
BladeStatsOption_Defenses = SubOption("Defenses", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)])
BladeStatsOption_Mods = SubOption("Stat Mods", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(1,100), BladeModDistribution)])
BladeStatsOption_Class = SubOption("Weapon Class", BladeStatsOption, [lambda: BladeStats.BladeWeaponClassRandomization()])

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
EnemyEnhancementsOption = Option("Enemy Enhancements", Enemies, "Gives enemies a random enhancement; it is displayed by their name", [lambda: _EnemyEnhancements.EnemyEnhances()], hasSpinBox = True, descData=lambda: _EnemyEnhancements.EnemyEnhancementDescriptions())
EnemyArtEffectsOption = Option("Enemy Art Effects", Enemies, "Gives enemies a random bonus effect to their arts; it is displayed by their\nart's name", [lambda: _EnemyArts.EnemyArtAttributes()], hasSpinBox = True, descData=lambda: _EnemyArts.EnemyArtEnhancementDescriptions())
EnemyArtEffectsOption_Reactions = SubOption("Reactions", EnemyArtEffectsOption)
EnemyArtEffectsOption_AOE = SubOption("AOE", EnemyArtEffectsOption)
EnemyArtEffectsOption_Buffs = SubOption("Buffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Debuffs = SubOption("Debuffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Enhancements = SubOption("Enhancements", EnemyArtEffectsOption)
EnemyDropOption = Option("Enemy Drops", Items, "Randomizes enemy drops", [lambda: EnemyDrops.RandoEnemyDrops()], hasSpinBox = True)
EnemyDropOption_Accessories = SubOption("Accessories", EnemyDropOption)
EnemyDropOption_TornaAccessories = SubOption("Torna Accessories", EnemyDropOption)
EnemyDropOption_WeaponChips = SubOption("Weapon Chips", EnemyDropOption)
EnemyDropOption_AuxCores = SubOption("Aux Cores", EnemyDropOption)
EnemyDropOption_RefinedAuxCores = SubOption("Refined Aux Cores", EnemyDropOption)
EnemyDropOption_CoreCrystals = SubOption("Core Crystals", EnemyDropOption)
EnemyDropOption_Deeds = SubOption("Shop Deeds", EnemyDropOption)
EnemyDropOption_CollectionPointMaterials = SubOption("Collection Point Materials", EnemyDropOption)
EnemyAggroOption = Option("Enemy Aggro", Enemies, "The percentage of all non-boss and non-quest enemies that will aggro the player", [lambda: EnemyRandoLogic.EnemyAggroProportion()], hasSpinBox = True)

# Misc
MusicOption = Option("Music", Misce, "Randomizes Music", [lambda: MusicShuffling.MusicShuffle()], descData=lambda: MusicShuffling.MusicRandoDescription())
MusicOption_MixBattleAndEnv = SubOption("Mix Battle/Environment Themes", MusicOption, _defState = False)
CustomCoreCrystalOption = Option("Custom Core Crystals", Items, "Adds Core Crystals with guaranteed Rare Blades to Treasure Chests", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()], prio = 52, hasSpinBox = True, spinDesc = "% of Chests", descData= lambda: CoreCrystalAdjustments.Description())
# DifficultyOption = Option("Difficulty", Misce, "Forces this difficulty, regardless of what is chosen in the options menu")
# DifficultyOption_Easy = SubOption("Easy", DifficultyOption)
# DifficultyOption_Normal = SubOption("Normal", DifficultyOption)
# DifficultyOption_BOC = SubOption("Bringer of Chaos", DifficultyOption)
# DifficultyOption_Ultimate = SubOption("Ultimate", DifficultyOption)

# QOL
FreelyEngageBladesOption = Option("Freely Engage Blades", QOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])
CTMCOption = Option("Chest Type Matches Contents", QOL, "Chest model and label changes depending on tier of loot", [lambda: RaceMode.ChestTypeMatching()], prio = 95, descData = lambda: RaceMode.CTMCDescription())
TreasureChestVisOption =  Option("Treasure Chest Visibility", QOL, "Increases the range you can see treasure chests from", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
RemoveFieldSkillsOption = Option("Remove Story Field Skills", QOL, "Removes field skill checks", [lambda: FieldSkillAdjustments.RemoveFieldSkills()], ["Remove All Field Skills", []])
RemoveFieldSkillsOption_AllFieldSkills = SubOption("Remove All Field Skills", RemoveFieldSkillsOption)
EverlastingPouchItemsOption = Option("Everlasting Pouch Items", QOL, "Makes Pouch Items last as long as possible", [lambda: JSONParser.ChangeJSONFile(["common/ITM_FavoriteList.json"],["Time"], Helper.InclRange(0,255), [6099])])
CondenseGoldOption = Option("Condense Gold Loot", QOL, "Condenses gold in chests so you can see other items", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"),["goldPopMin", "goldPopMax"], Helper.InclRange(0,100000), [1])])
MutePopupsOption = Option("Mute Popups", QOL, "Stops blade skill and pouch item refill popups", [lambda: (JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[89], ["sheet06"], [""]), JSONParser.ChangeJSONLine(["common/MNU_Layer_Dlc03.json"],[320], ["sheet06"], [""]))])
MutePopupsOption_Landmarks = SubOption("Landmarks", MutePopupsOption, [lambda: (JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[85], ["sheet04"], [""]),JSONParser.ChangeJSONLine(["common/MNU_Layer_Dlc03.json"],[316], ["sheet04"], [""]))])
EnhancementDisplayOption = Option("Enhancement Display", QOL, "Shows when enhancements activate in battle", [lambda: Enhancements.SearchAndSetDisplayIDs()])
EasySkillTreesOption = Option("Easy Affinity Trees", QOL, "Makes trust the only condition for levelling up a blade's affinity tree", [lambda: SkillTrees.BladeSkillTreeShortening()])
FasterDriverSkillTrees = Option("Fast Driver Skill Trees", QOL, "Decreases SP required for each node", [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["./XC2/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "./XC2/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "./XC2/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], [f'row[key] // {FasterDriverSkillTrees.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1,  spinDesc = "x Faster")
FasterLevelsOption = Option("Faster Levels", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["./XC2/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2,spinIncr = 1, spinDesc = "x Faster")
ShortcutsOption = Option("Shortcuts", QOL, "Various speedups for the main story quests")
ShortcutsOption_Tutorials = SubOption("Tutorials Skip", ShortcutsOption, [lambda: TutorialShortening.ShortenedTutorial()])
ShortcutsOption_PuzzleTreeWoodSkip = SubOption("Puzzletree Wood Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCollect.json"],[18,19], ["Count"], 0)])
ShortcutsOption_GatherNia = SubOption("Nia Rumours Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCondition.json"],[7], ["ConditionID"], 1)])
ShortcutsOption_IndolQuiz = SubOption("Indol Quiz Skip", ShortcutsOption, [lambda: TutorialShortening.IndolQuizSkip()])
StartwithIncreasedMovespeedOption = Option("Increased Movespeed", QOL, "Adds a shop deed to the DLC items to increase your movement speed", [lambda: DLCFlagQOL.AddMovespeedDeed()], hasSpinBox = True, spinMin = 0, spinMax = 50, spinIncr = 5, spinDesc = "% Increase (x10)", spinWidth = 2, spinDefault = 50)
NewGamePlusFlagsOptions = Option("NG+ Flags", QOL, "Enables many NG+ behaviours like unlocked hidden driver skill trees, unlocked chain attacks from the start, unlocked blade slots etc. These must be accepted from the DLC Menu to work.", [lambda: DLCFlagQOL.CreateDLCtoSetFlag(["2nd Blade Equip Slot", "3rd Blade Equip Slot"], [35327, 35328], [2,2], [0,0], [1,1], [1,1])])
NewGamePlusFlagsOptions_Blades = SubOption("NG+ Blades", NewGamePlusFlagsOptions, [lambda: GachaModifications.UnlockNGPlusBlades()])
NewGamePlusFlagsOptionsHiddenDriverSkillTree = SubOption("Hidden Skill Tree Unlocked", NewGamePlusFlagsOptions, [lambda: DLCFlagQOL.FixIssuesCausedByNGPlusFlag()])

# Funny
ProjTreasureChestOption = Option("Projectile Treasure Chests", Funny, "Launches your items from chests",[lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [15])])
BladeSizeOption = Option("Blade Size", Funny, "Randomizes the size of Blades", [lambda: Scales.BladeScales()], hasSpinBox = True)
NPCSizeOption = Option("NPC Size", Funny, "Randomizes the size of NPCs", [lambda: Scales.NPCScales()], hasSpinBox = True)
EnemySizeOption = Option("Enemy Size", Funny, "Randomizes the size of enemies", [lambda: Scales.EnemyScales()], hasSpinBox = True)
FieldItemOption = Option("Field Item Size", Funny, "Randomizes the size and spin rate of items dropped on the field.", [lambda: BigItems.BigItemsRando()], descData=lambda: BigItems.BigItemsDesc())

# Cosmetics
BladeWeaponCosmeticsOption = Option("Blade Weapon Cosmetics", CosmeticsTab, "Keeps all default weapon models regardless of chips", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["OnlyWpn"], [0], [1])], spinDefault=25)
TrustLineOption = Option("Blade Trust Lines", CosmeticsTab, "Randomizes blade-driver trust lines in battle (colors, power, etc.)", [lambda: TrustBeam.BeamRandomizer()])
CosmeticsOption = Option("Character Outfits", CosmeticsTab, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics.Cosmetics()],prio=51, hasSpinBox = True, descData=lambda: Cosmetics.CosmeticsDescription()) # Sub are created by another class
for opt in Cosmetics.CosmeticsList: # To gen these since listing them here would be annoying
    opt.CreateSubOptions(CosmeticsOption)

# Game Modes
RaceModeOption = Option("Race Mode", GameModeTab, "Play through a condensed version of the game in this mode!", [lambda: RaceMode.RaceModeChanging()], descData = lambda: RaceMode.RaceModeDescription())
RaceModeOption_Zohar = SubOption("Zohar Fragment Hunt", RaceModeOption)
RaceModeOption_DLC = SubOption("DLC Item Removal", RaceModeOption)
UMHuntOption = Option("Unique Monster Hunt", GameModeTab, "Defeat Unique Monsters in this Roguelike mode!", [lambda: UMHuntMain.UMHunt()], hasSpinBox = True, spinMin = 1, spinMax = 10, spinIncr = 1, spinDesc = "Round(s)", spinWidth = 2, spinDefault = 10, descData= lambda: UMHuntMain.Description())
UMHuntOption_SuperbossWave = SubOption("Superboss Wave", UMHuntOption)
UMHuntOption_RandomLandmarks = SubOption("Random Starting Landmarks", UMHuntOption)

# Torna
TornaMainOption = Option("Torna Randomization", TornaTab, "Randomizes the Torna DLC, in a logic-based method.", [lambda: TornaMain.AllTornaRando()], descData=lambda:TornaMain.TornaMainDescription())
TornaMainOption_CollectionPoints = SubOption("Collection Points", TornaMainOption)
TornaMainOption_EnemyDrops = SubOption("Enemy Drops", TornaMainOption, hasSpinBox = True, spinMin = 1, spinMax = 8, spinIncr = 1, spinWidth = 1, spinDefault = 1, spinDesc = "Items")
TornaMainOption_GroundItems = SubOption("Ground Items", TornaMainOption)
TornaMainOption_Shops = SubOption("Shops", TornaMainOption, hasSpinBox = True, spinMin = 1, spinMax = 15, spinIncr = 1, spinWidth = 2, spinDefault = 1, spinDesc = "Items")
TornaMainOption_SideQuests = SubOption("Side Quests", TornaMainOption, hasSpinBox = True, spinMin = 1, spinMax = 4, spinIncr = 1, spinWidth = 1, spinDefault = 1, spinDesc = "Items")
TornaMainOption_TreasureChests = SubOption("Treasure Chests", TornaMainOption, hasSpinBox = True, spinMin = 1, spinMax = 8, spinIncr = 1, spinWidth = 1, spinDefault = 1, spinDesc = "Items")
TornaCreateSpoilerLog = Option("Create Torna Spoiler Log", TornaTab, "Outputs a Spoiler Log containing information on where each item is placed, located in XC2/Torna_Spoiler_Logs folder.")
TornaAddHints = Option("Torna In-Game Hints", TornaTab, "Adds hints to the in the \"Tips\" Submenu in-game.", descData=lambda:TornaMain.TornaHintDescription())
TornaAddHints_ItemHints = SubOption("Item Hints", TornaAddHints, hasSpinBox = True, spinMin = 1, spinMax = 12, spinIncr = 1, spinWidth = 2, spinDefault = 1, spinDesc = "Hints")
TornaAddHints_LocProgHints = SubOption("Location Hints", TornaAddHints, hasSpinBox = True, spinMin = 1, spinMax = 12, spinIncr = 1, spinWidth = 2, spinDefault = 1, spinDesc = "Hints")
TornaObjectColorMatchesContents = Option("Gilded Required Check Names", TornaTab, "Turns names of Checks with Progression Items gold.", descData=lambda:TornaMain.TornaCCMCDescription())
TornaChooseCommunityReqs = Option("Community Level Story Requirements", TornaTab, "Changes the Community Level requirement for the story events.", descData=lambda:TornaMain.TornaStoryReqChangeDescription())
TornaChooseCommunityReqs_Gate1Req = SubOption("Gate 1 Required Level", TornaChooseCommunityReqs, hasSpinBox = True, spinMin = 0, spinMax = 2, spinIncr = 1, spinWidth = 1, spinDefault = 0)
TornaChooseCommunityReqs_Gate2Req = SubOption("Gate 2 Required Level", TornaChooseCommunityReqs, hasSpinBox = True, spinMin = 0, spinMax = 4, spinIncr = 1, spinWidth = 1, spinDefault = 0)
TornaRemoveGormottChecks = Option("Remove Certain Gormott Checks", TornaTab, "Progression Items will not be found in Checks near locations in Gormott selected below.")
for loc in TornaMain.GormottNametoLocID.keys(): # Automatically Generates these
    SubOption(loc, TornaRemoveGormottChecks, _defState = True)
TornaRewardsonUnreqSidequests = Option("Progression on Unrequired Sidequests", TornaTab, "Sidequests not chosen for the main story requirements or story gates can have Progression Items on their rewards.")

#TornaCompatibleOptions = [BladeSpecialButtonsOption, TornaChooseCommunityReqs, CondenseGoldOption, TornaCreateSpoilerLog, EnhancementDisplayOption, EverlastingPouchItemsOption, FieldItemOption, TornaObjectColorMatchesContents, StartwithIncreasedMovespeedOption, MusicOption, MutePopupsOption, NPCSizeOption, TornaRemoveGormottChecks, ShortcutsOption, TornaAddHints, TornaMainOption, TreasureChestVisOption, TrustLineOption, TornaRewardsonUnreqSidequests, EnemyEnhancementsOption, EnemyArtEffectsOption, BladeWeaponChipsOption, BladeSpecialOption, BladeBattleSkillsOption]

# any torna option with a lambda gets the incompatible list
MutuallyExclusivePairing([TornaMainOption, TornaAddHints, TornaObjectColorMatchesContents, TornaChooseCommunityReqs, TornaCreateSpoilerLog, TornaRemoveGormottChecks, TornaRewardsonUnreqSidequests], [AccessoriesOption, AuxCoresOption, AccessoryShopsOption, CollectionPointsOption, PouchItemShopOption, TreasureChestOption, WeaponChipShopOption, DriversOption, BladesOption, BladeArtsOption, BladeFieldSkillsOption, BladeWeaponChipsOption, BladeCombosOption, BladeStatsOption, EnemiesOption, EnemyDropOption, EnemyAggroOption, CustomCoreCrystalOption, FreelyEngageBladesOption, CTMCOption, RemoveFieldSkillsOption, EasySkillTreesOption, FasterLevelsOption, NewGamePlusFlagsOptions, ProjTreasureChestOption, EnemySizeOption, BladeWeaponCosmeticsOption, CosmeticsOption, RaceModeOption, UMHuntOption])

MutuallyExclusivePairing([UMHuntOption], [AccessoryShopsOption, CollectionPointsOption, PouchItemShopOption, TreasureChestOption, WeaponChipShopOption, DriversOption, BladeWeaponChipsOption, AccessoriesOption, AuxCoresOption, EnemiesOption, EnemyDropOption, CustomCoreCrystalOption, FasterDriverSkillTrees, EasySkillTreesOption, FasterLevelsOption, RaceModeOption])

MutuallyExclusivePairing([RaceModeOption], [DriversOption, BladesOption])

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
# EnemyMovespeedOption = Option("Enemy Movespeed", Enemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))])
# GenStandardOption("Enemy Rage", TabEnemies, "Randomizes the effects of enemy enraged states", ["common/BTL_Aura"])   