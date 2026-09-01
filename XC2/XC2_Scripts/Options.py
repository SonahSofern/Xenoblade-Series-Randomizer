from scripts import JSONParser,Helper, XCRandomizer
from XC2.XC2_Scripts.IDs import *
from tkinter import *
from XC2.XC2_Scripts import QOL as QualityOfLife, Accessories, AuxCores, Misc, BladeSpecials, CoreCrystals as CoreCry, DriverArts, EleCombo, EnemyArts, EnemyEnhancements, FieldSkills, SkillTrees, IDs, MusicShuffling, BladeStats, Skips, Enhancements, Cosmetics, Items as I, Scales, CharacterRandomization, Enemy, WeaponChips, YellowSkills
from XC2.XC2_Scripts.Race_Mode import RaceMode
from XC2.XC2_Scripts.Torna_Logic import TornaMain
from XC2.XC2_Scripts.UM_Hunt import UMHuntMain

from scripts.Interactables import Option, SubOption, MutuallyExclusivePairing, Dropdown, Spinbox, SubSpinbox, SubDropdown, DropdownOption, Category
import scripts.Interactables
game = "XC2"
scripts.Interactables.Game = game

# Prio
First = 0
Last = 100
BladeRandoPrio = 0

# Dont forget quest rando adding random quests into the main story to spice it up

Items = 1
Driver  = 2
Blade = 3
Enemies = 4
QOL = 5
Funny = 6
CosmeticsTab = 7
GameModeTab = 8


Tabs = {
    Items: "Items",
    Driver: "Drivers",
    Blade: "Blades",
    Enemies: "Enemies",
    QOL: "Quality of Life",
    Funny: "Funny",
    CosmeticsTab: "Cosmetics",
    GameModeTab: "Game Modes",
}

weightsSpinDescription = "Weights ↓"


# General
AccessoriesOption = Option("Accessories", Items, "Randomizes the effects of Accessories", [lambda: Accessories.RandomizeAccessoryEnhancements(), lambda: Accessories.SearchAndSetDisplayIDs()], descData=lambda: Accessories.AccessoriesDesc(AccessoriesOption.name, "accessory"))
AuxCoresOption = Option("Aux Cores", Items, "Randomizes the effects of Aux Cores", [lambda: AuxCores.RandomizeAuxCoreEnhancements(), lambda: Accessories.SearchAndSetDisplayIDs()], descData=lambda: Accessories.AccessoriesDesc(AuxCoresOption.name, "aux core"))
AccessoryShopsOption = Option("Accessory Shops", Items, "Randomizes the contents of Accessory Shops", [lambda: I.RandomizeAccessoryShops()], descData=lambda: I.AccessoryShopDescription())
PouchItemShopOption = Option("Pouch Item Shops", Items, "Randomizes the contents of Pouch Item Shops", [lambda: I.RandomizePouchItemShops()], descData=lambda: I.PouchItemShopDesc())
WeaponChipShopOption = Option("Weapon Chip Shops", Items, "Randomizes Weapon Chips in Weapon Chip Shops", [lambda: I.RandomizeWeaponChipShops()], descData=lambda: I.WeaponChipDesc())
TreasureChestOption = Option("Treasure Chests", Items, "Randomizes the contents of Treasure Chests", preRandoCommands=[lambda: I.RandomizeTreasureBoxes()], prio = 51, descData=lambda: I.TreasureChestDescription())
TreasureChestOption_Accessories = SubOption("Accessories", TreasureChestOption)
TreasureChestOption_Accessories_Spinbox = SubSpinbox(TreasureChestOption_Accessories, default=30, description=weightsSpinDescription)
TreasureChestOption_WeaponChips = SubOption("Weapon Chips", TreasureChestOption)
TreasureChestOption_WeaponChips_Spinbox = SubSpinbox(TreasureChestOption_WeaponChips, default=10)
TreasureChestOption_AuxCores = SubOption("Aux Cores", TreasureChestOption)
TreasureChestOption_AuxCores_Spinbox = SubSpinbox(TreasureChestOption_AuxCores, default=10)
TreasureChestOption_RefinedAuxCores = SubOption("Refined Aux Cores", TreasureChestOption)
TreasureChestOption_RefinedAuxCores_Spinbox = SubSpinbox(TreasureChestOption_RefinedAuxCores, default=10)
TreasureChestOption_CoreCrystals = SubOption("Core Crystals", TreasureChestOption)
TreasureChestOption_CoreCrystals_Spinbox = SubSpinbox(TreasureChestOption_CoreCrystals, default=5)
TreasureChestOption_RareBlades = SubOption("Rare Blades", TreasureChestOption, [lambda: CoreCry.CustomCoreCrystalRando()])
TreasureChestOption_RareBlades_Spinbox = SubSpinbox(TreasureChestOption_RareBlades, default=5)

EnemyDropOption = Option("Enemy Drops", Items, "Randomizes enemy drops", [lambda: I.RandomizeEnemyDrops()], prio=51, descData=lambda: I.EnemyDropDescription())
EnemyDropOption_Accessories = SubOption("Accessories", EnemyDropOption)
EnemyDropOption_Accessories_Spinbox = SubSpinbox(EnemyDropOption_Accessories, default=30, description=weightsSpinDescription)
EnemyDropOption_WeaponChips = SubOption("Weapon Chips", EnemyDropOption)
EnemyDropOption_WeaponChips_Spinbox = SubSpinbox(EnemyDropOption_WeaponChips, default=10)
EnemyDropOption_AuxCores = SubOption("Aux Cores", EnemyDropOption)
EnemyDropOption_AuxCores_Spinbox = SubSpinbox(EnemyDropOption_AuxCores, default=10)
EnemyDropOption_RefinedAuxCores = SubOption("Refined Aux Cores", EnemyDropOption)
EnemyDropOption_RefinedAuxCores_Spinbox = SubSpinbox(EnemyDropOption_RefinedAuxCores, default=10)
EnemyDropOption_CoreCrystals = SubOption("Core Crystals", EnemyDropOption)
EnemyDropOption_CoreCrystals_Spinbox = SubSpinbox(EnemyDropOption_CoreCrystals, default=5)
EnemyDropOption_RareBlades = SubOption("Rare Blades", EnemyDropOption, [lambda: CoreCry.CustomCoreCrystalRando()])
EnemyDropOption_RareBlades_Spinbox = SubSpinbox(EnemyDropOption_RareBlades, default=5)

QuestRewardsOption = Option("Quest Rewards", Items, "Randomizes quest rewards, including merc missions", [lambda: I.RandomizeQuestRewards()], prio=51, descData=lambda: I.QuestRewardDescription())
QuestRewardsOption_Accessories = SubOption("Accessories", QuestRewardsOption)
QuestRewardsOption_Accessories_Spinbox = SubSpinbox(QuestRewardsOption_Accessories, default=30, description=weightsSpinDescription)
QuestRewardsOption_WeaponChips = SubOption("Weapon Chips", QuestRewardsOption)
QuestRewardsOption_WeaponChips_Spinbox = SubSpinbox(QuestRewardsOption_WeaponChips, default=10)
QuestRewardsOption_AuxCores = SubOption("Aux Cores", QuestRewardsOption)
QuestRewardsOption_AuxCores_Spinbox = SubSpinbox(QuestRewardsOption_AuxCores, default=10)
QuestRewardsOption_RefinedAuxCores = SubOption("Refined Aux Cores", QuestRewardsOption)
QuestRewardsOption_RefinedAuxCores_Spinbox = SubSpinbox(QuestRewardsOption_RefinedAuxCores, default=10)
QuestRewardsOption_CoreCrystals = SubOption("Core Crystals", QuestRewardsOption)
QuestRewardsOption_CoreCrystals_Spinbox = SubSpinbox(QuestRewardsOption_CoreCrystals, default=5)
QuestRewardsOption_RareBlades = SubOption("Rare Blades", QuestRewardsOption, [lambda: CoreCry.CustomCoreCrystalRando()])
QuestRewardsOption_RareBlades_Spinbox = SubSpinbox(QuestRewardsOption_RareBlades, default=5)

# Drivers
DriversOption = Option("Drivers", Driver, "Randomizes which drivers appear in the story", [lambda: CharacterRandomization.CharacterRandomization()], prio=First, preRandoCommands=[lambda: CharacterRandomization.resetGlobals()], descData=lambda: CharacterRandomization.DriversDescriptions())
DriversOption_Nia = SubOption("Guarantee Early Nia", DriversOption, defState = False)
DriverArtsOption = Option("Driver Arts", Driver, "Randomizes the effects of driver arts", [lambda: (DriverArts.DriverArtRandomizer(), DriverArts.GenCustomArtDescriptions("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", "./XC2/JsonOutputs/common_ms/btl_arts_dr_cap.json"))], descData=lambda: DriverArts.DriverArtDescription())
DriverArtsOption_Spinbox = Spinbox(DriverArtsOption)
spinArts = "%"
DriverArtsOption_AutoAttacks = SubOption("Auto Attacks", DriverArtsOption, defState=False)
# DriverArtsOption_AutoAttacks_Spinbox = SubSpinbox(DriverArtsOption_AutoAttacks, default=20, description="% of auto attacks")
DriverArtsOption_Reaction = SubOption("Reaction", DriverArtsOption)
DriverArtsOption_Reaction_Dropdown = SubDropdown(DriverArtsOption_Reaction, [DropdownOption("Single"), DropdownOption("Multi")])
# DriverArtsOption_SingleReaction = SubOption("Single Reaction", DriverArtsOption)
# DriverArtsOption_SingleReaction_Spinbox = SubSpinbox(DriverArtsOption_SingleReaction, default=20, description=spinArts)
# DriverArtsOption_MultipleReactions = SubOption("Multiple Reactions", DriverArtsOption)
# DriverArtsOption_MultipleReactions_Spinbox = SubSpinbox(DriverArtsOption_MultipleReactions, default=20, description=spinArts)
DriverArtsOption_Debuffs = SubOption("Debuffs", DriverArtsOption)
# DriverArtsOption_Debuffs_Spinbox = SubSpinbox(DriverArtsOption_Debuffs, default=40, description=spinArts)
DriverArtsOption_Buffs = SubOption("Buffs", DriverArtsOption)
# DriverArtsOption_Buffs_Spinbox = SubSpinbox(DriverArtsOption_Buffs, default=10, description=spinArts)
DriverArtsOption_Enhancements = SubOption("Enhancements", DriverArtsOption)
# DriverArtsOption_Enhancements_Spinbox = SubSpinbox(DriverArtsOption_Enhancements, default=70, description=spinArts)
DriverArtsOption_Cooldown = SubOption("Cooldown", DriverArtsOption)
# DriverArtsOption_Cooldown_Spinbox = SubSpinbox(DriverArtsOption_Cooldown, default=20, description=spinArts)
DriverArtsOption_Damage = SubOption("Damage", DriverArtsOption)
# DriverArtsOption_Damage_Spinbox = SubSpinbox(DriverArtsOption_Damage, default=20, description=spinArts)
DriverArtsOption_AnimationSpeed = SubOption("Animation Speed", DriverArtsOption)
# DriverArtsOption_AnimationSpeed_Spinbox = SubSpinbox(DriverArtsOption_AnimationSpeed, default=20, description=spinArts)
DriverArtsOption_AOE = SubOption("AOE", DriverArtsOption)
# DriverArtsOption_AOE_Spinbox = SubSpinbox(DriverArtsOption_AOE, default=10, description=spinArts)

DriverSkillTreesOption = Option("Driver Skill Trees", Driver, "Randomizes driver's skill trees", [lambda: SkillTrees.RandomizeSkillEnhancements()], descData=lambda: SkillTrees.Descriptions())
DriverSkillTreesOption_NonstandardSkills = SubOption("Nonstandard Skills", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyArtsCancel = SubOption("Early Arts Cancel", DriverSkillTreesOption)
DriverSkillTreesOption_EarlyXYBAttack = SubOption("Early XYB Attack", DriverSkillTreesOption)

# Blades
BladesOption = Option("Blades", Blade, "Randomizes which blades appear in the story", [lambda: CharacterRandomization.CharacterRandomization()], prio=BladeRandoPrio, preRandoCommands=[lambda: CharacterRandomization.resetGlobals()], descData=lambda: CharacterRandomization.BladesDescriptions())
BladesOption_Spinbox = Spinbox(BladesOption)
BladesOption_Dromarch = SubOption("Randomize Dromarch", BladesOption)
BladesOption_Healer = SubOption("Guarantee Healing Art", BladesOption)
BladeNGPlusOption = Option("Enable NG+ Blades", Blade, "Allows NG+ blades to be included in randomization", [lambda: CoreCry.CressidusTresspassRemoval()], prio= BladeRandoPrio-1, descData=lambda: CoreCry.NGPlusBladeDesc())
BladeNGPlusOption_Balance = SubOption("Balance NG+ Blades", BladeNGPlusOption, [lambda: CoreCry.NewGamePlusBladeBalancing()], filePlaceCommands=[lambda: XCRandomizer.FilePlacer(["Loader/plugins/ngPlusBladeChips.nro"], "../../../0100e95004038000/romfs/skyline/plugins", game=game)])
BladeArtsOption = Option("Blade Arts", Blade, "Randomizes a Blade's combat arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), BladeArts, BladeArts)])
BladeBattleSkillsOption = Option("Blade Battle Skills", Blade, "Randomizes a Blade's battle (yellow) skill tree", [lambda: YellowSkills.RandomizeBattleSkills()])
BladeBattleSkillsOption_Spinbox = Spinbox(BladeBattleSkillsOption)
BladeBattleSkillsOption_Duplicates = SubOption("Allow Duplicates", BladeBattleSkillsOption)
BladeFieldSkillsOption = Option("Blade Field Skills", Blade, "Randomizes a Blade's field (green) skill tree", [lambda: FieldSkills.RandomizeFieldSkills()])
BladeFieldSkillsOption_QuestSkills = SubOption("Quest Skills", BladeFieldSkillsOption)
BladeSpecialOption = Option("Blade Specials", Blade, "Randomizes each hit of a blade special to have a random effect", [lambda:(BladeSpecials.BladeSpecials())])
BladeSpecialOption_Spinbox = Spinbox(BladeSpecialOption, default=10, max=30)
BladeSpecialOption_Reaction = SubOption("Reactions", BladeSpecialOption)
BladeSpecialOption_Enhancement = SubOption("Enhancement", BladeSpecialOption)
BladeSpecialOption_Debuffs = SubOption("Debuff", BladeSpecialOption)
BladeWeaponChipsOption = Option("Blade Weapon Chips", Blade, "Randomizes the effects of weapon chips", [lambda:WeaponChips.ChangeWeaponRankNames()])
BladeWeaponChipsOption_Spinbox = Spinbox(BladeWeaponChipsOption)
# BladeWeaponChipsOption_AutoAtk = SubOption("Auto Attacks", BladeWeaponChipsOption, defState= True)
BladeWeaponChipsOption_CritRate = SubOption("Crit Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["CriRate"],Helper.InclRange(0,100), BladeStats.BladeWeaponCritDistribution)])
BladeWeaponChipsOption_GuardRate = SubOption("Guard Rate", BladeWeaponChipsOption, [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["GuardRate"],Helper.InclRange(0,100), BladeStats.BladeWeaponGuardDistribution)])
BladeWeaponChipsOption_Enhancement = SubOption("Enhancements", BladeWeaponChipsOption, [lambda: WeaponChips.RandomizeWeaponEnhancements()])
BladeCombosOption = Option("Blade Combos", Blade, "Randomizes blade elemental combos", [lambda: EleCombo.BladeComboRandomization()], descData=lambda: EleCombo.BladeCombosDescription())
BladeCombosOption_ElementRoutes = SubOption("Element Routes", BladeCombosOption)
BladeCombosOption_Damage = SubOption("Damage", BladeCombosOption)
BladeCombosOption_DOT = SubOption("DoT", BladeCombosOption)
BladeCombosOption_Reactions = SubOption("Reactions", BladeCombosOption)
BladeCombosOption_AOE = SubOption("AOE", BladeCombosOption)
BladeStatsOption = Option("Blade Stats", Blade, "Randomizes various stats of blades")
BladeStatsOption_AuxCoreSlots = SubOption("Aux Core Slots", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), BladeStats.BladeAuxCoreSlotDistribution)])
BladeStatsOption_Cooldown = SubOption("Swap Cooldowns", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
BladeStatsOption_Element = SubOption("Elements", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8), TornaBladeIDs)]) # Ignoring torna blade IDs because their art and special effects break on other elements
BladeStatsOption_Defenses = SubOption("Defenses", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeStats.BladeDefenseDistribution)])
BladeStatsOption_Mods = SubOption("Stat Mods", BladeStatsOption, [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(1,100), BladeStats.BladeModDistribution)])
BladeStatsOption_Class = SubOption("Weapon Class", BladeStatsOption, [lambda: BladeStats.BladeWeaponClassRandomization()])

# Enemies
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsters, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_Aggro, NormalEnemyOption_Size.GetState(), NormalEnemyOption_Stats, isOopsAll=NormalEnemyOption_OopsAll.GetState(), oopsAllVal=NormalEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), prio=2)
NormalEnemyOption_Spinbox = Spinbox(NormalEnemyOption)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Normal_Spinbox = SubSpinbox(NormalEnemyOption_Normal, default=10, description=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Unique_Spinbox = SubSpinbox(NormalEnemyOption_Unique, default=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Boss_Spinbox = SubSpinbox(NormalEnemyOption_Boss, default=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)
NormalEnemyOption_Superboss_Spinbox = SubSpinbox(NormalEnemyOption_Superboss, default=1)
NormalEnemyOption_Stats = SubOption("Balance Stats", NormalEnemyOption)
NormalEnemyOption_Aggro = SubOption("Vanilla Aggro", NormalEnemyOption)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)
NormalEnemyOption_OopsAll = SubOption("Oops All", NormalEnemyOption, defState=False)
NormalEnemyOption_OopsAll_Dropdown = SubDropdown(NormalEnemyOption_OopsAll, Enemy.GetOopsAllPool(), sort=True)
NormalEnemyOption_Multiply = SubOption("More Enemies", NormalEnemyOption, [lambda: Enemy.EnemyMultiplier(NormalEnemyOption_Multiply_Spinbox.GetState(), IDs.NormalMonsters)], defState=False)
NormalEnemyOption_Multiply_Spinbox = SubSpinbox(NormalEnemyOption_Multiply, 2, 4, 1, 2, "x Enemies")

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.UniqueMonsters + IDs.SuperbossMonsters, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, UniqueEnemyOption_Aggro, UniqueEnemyOption_Size.GetState(), UniqueEnemyOption_Stats, isOopsAll=UniqueEnemyOption_OopsAll.GetState(), oopsAllVal=UniqueEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), prio=2)
UniqueEnemyOption_Spinbox = Spinbox(UniqueEnemyOption)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Normal_Spinbox = SubSpinbox(UniqueEnemyOption_Normal, default=1, description=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Unique_Spinbox = SubSpinbox(UniqueEnemyOption_Unique, default=10)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Boss_Spinbox = SubSpinbox(UniqueEnemyOption_Boss, default=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss_Spinbox = SubSpinbox(UniqueEnemyOption_Superboss, default=1)
UniqueEnemyOption_Stats = SubOption("Balance Stats", UniqueEnemyOption)
UniqueEnemyOption_Aggro = SubOption("Vanilla Aggro", UniqueEnemyOption)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)
UniqueEnemyOption_OopsAll = SubOption("Oops All", UniqueEnemyOption, defState=False)
UniqueEnemyOption_OopsAll_Dropdown = SubDropdown(UniqueEnemyOption_OopsAll, Enemy.GetOopsAllPool(), sort=True)
UniqueEnemyOption_Multiply = SubOption("More Enemies", UniqueEnemyOption, [lambda: Enemy.EnemyMultiplier(UniqueEnemyOption_Multiply_Spinbox.GetState(), IDs.UniqueMonsters)], defState=False)
UniqueEnemyOption_Multiply_Spinbox = SubSpinbox(UniqueEnemyOption_Multiply, 2, 7, 1, 2, "x Enemies")

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonsters, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, True, BossEnemyOption_Stats, matchPhase=BossEnemyOption_MatchPhase.GetState(), finalBoss=BossEnemyOption_FinalBoss.GetState(), isOopsAll=BossEnemyOption_OopsAll.GetState(), oopsAllVal=BossEnemyOption_OopsAll_Dropdown.GetState())], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), prio=2)
BossEnemyOption_Spinbox = Spinbox(BossEnemyOption)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
BossEnemyOption_Normal_Spinbox = SubSpinbox(BossEnemyOption_Normal, default=2, description=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
BossEnemyOption_Unique_Spinbox = SubSpinbox(BossEnemyOption_Unique, default=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
BossEnemyOption_Boss_Spinbox = SubSpinbox(BossEnemyOption_Boss, default=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False)
BossEnemyOption_Superboss_Spinbox = SubSpinbox(BossEnemyOption_Superboss, default=1)
BossEnemyOption_Stats = SubOption("Balance Stats", BossEnemyOption)
BossEnemyOption_Solo = SubOption("Balance Solo Fights", BossEnemyOption)
BossEnemyOption_Group = SubOption("Balance Group Fights", BossEnemyOption)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)
BossEnemyOption_MatchPhase = SubOption("Match Phase", BossEnemyOption)
BossEnemyOption_OopsAll = SubOption("Oops All", BossEnemyOption, defState=False)
BossEnemyOption_OopsAll_Dropdown = SubDropdown(BossEnemyOption_OopsAll, Enemy.GetOopsAllPool(), sort=True)
BossEnemyOption_Multiply = SubOption("More Enemies", BossEnemyOption, [lambda: Enemy.EnemyMultiplier(BossEnemyOption_Multiply_Spinbox.GetState(), IDs.BossMonsters + IDs.TornaFinalbossMonsters + IDs.FinalbossMonsters)], defState=False)
BossEnemyOption_Multiply_Spinbox = SubSpinbox(BossEnemyOption_Multiply, 2, 7, 1, 2, "x Enemies")

EnemyEnhancementsOption = Option("Enemy Enhancements", Enemies, "Gives enemies a random enhancement", [lambda: EnemyEnhancements.EnemyEnhances()], descData=lambda: EnemyEnhancements.EnemyEnhancementDescriptions())
EnemyArtEffectsOption_Spinbox = Spinbox(EnemyEnhancementsOption, default=30)
EnemyEnhancementsOption_ShowInName = SubOption("Display in Name", EnemyEnhancementsOption)

EnemyArtEffectsOption = Option("Enemy Art Effects", Enemies, "Gives enemies a random bonus effect to their arts; it is displayed by their\nart's name", [lambda: EnemyArts.EnemyArtAttributes()], descData=lambda: EnemyArts.EnemyArtEnhancementDescriptions())
EnemyArtEffectsOption_Spinbox = Spinbox(EnemyArtEffectsOption, default=50)
EnemyArtEffectsOption_Reactions = SubOption("Reactions", EnemyArtEffectsOption)
EnemyArtEffectsOption_AOE = SubOption("AOE", EnemyArtEffectsOption)
EnemyArtEffectsOption_Buffs = SubOption("Buffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Debuffs = SubOption("Debuffs", EnemyArtEffectsOption)
EnemyArtEffectsOption_Enhancements = SubOption("Enhancements", EnemyArtEffectsOption)

# QOL
TutorialShorteningOption = Option("Tutorial Skips", QOL, "Skips as many tutorials and early argentum quests as possible.", [lambda: Skips.ShortenedTutorial()])
ShortcutsOption = Option("Quest Skips", QOL, "Various speedups/skips for tedious main story quests")
ShortcutsOption_PuzzleTreeWoodSkip = SubOption("Puzzletree Wood Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCollect.json"],[18,19], ["Count"], 0)])
# ShortcutsOption_GatherNia = SubOption("Nia Rumours Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCondition.json"],[7], ["ConditionID"], 1)])
ShortcutsOption_GatherNia = SubOption("Nia Rumours Skip", ShortcutsOption, [lambda: Skips.NextQuestSkipper({35:38})])
ShortcutsOption_ThiefRumours = SubOption("Roc Thief Rumours Skip", ShortcutsOption, [lambda: Skips.BaseGameStorySkip([2028], "Normal")])
ShortcutsOption_MorArdainEnterFactory = SubOption("Materials Stakeout Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_MercenariesMission.json"],[248], ["RequestPerformance"], 1)])
ShortcutsOption_IndolQuiz = SubOption("Indol Quiz Skip", ShortcutsOption, [lambda: Skips.IndolQuizSkip()])
ShortcutsOption_FeedingAnArmy = SubOption("Feeding an Army Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCollect.json"], [293,294,295,296], ["Count"], 0)])
ShortcutsOption_CrossDesert = SubOption("To Cross a Desert Skip", ShortcutsOption, [lambda: JSONParser.ChangeJSONLine(["common/FLD_QuestCollect.json"], [300,301], ["Count"], 0)])
communitySpinDesc = "Member(s)"
CommunityMembersOption = Option("Community Members", QOL, "Adjusts how many members/quests are required for each community level in Torna", [lambda: QualityOfLife.CommunityQOL()])
CommunityMembersOption_LV1 = SubOption("Level 1", CommunityMembersOption)
CommunityMembersOption_LV1_Spinbox = SubSpinbox(CommunityMembersOption_LV1, default=1, max=1, description=communitySpinDesc)
CommunityMembersOption_LV2 = SubOption("Level 2", CommunityMembersOption)
CommunityMembersOption_LV2_Spinbox = SubSpinbox(CommunityMembersOption_LV2, default=2, max=16, increment=4, description=communitySpinDesc)
CommunityMembersOption_LV3 = SubOption("Level 3", CommunityMembersOption)
CommunityMembersOption_LV3_Spinbox = SubSpinbox(CommunityMembersOption_LV3, default=3, max=32, increment=8, description=communitySpinDesc)
CommunityMembersOption_LV4 = SubOption("Level 4", CommunityMembersOption)
CommunityMembersOption_LV4_Spinbox = SubSpinbox(CommunityMembersOption_LV4, default=4, max=48, increment=16, description=communitySpinDesc)
CommunityMembersOption_LV5 = SubOption("Level 5", CommunityMembersOption)
CommunityMembersOption_LV5_Spinbox = SubSpinbox(CommunityMembersOption_LV5, default=5, max=64, increment=16, description=communitySpinDesc)
CommunityMembersOption_LVMAX = SubOption("Level MAX", CommunityMembersOption)
CommunityMembersOption_LVMAX_Spinbox = SubSpinbox(CommunityMembersOption_LVMAX, default=6, max=89, increment=32, description=communitySpinDesc)

FieldSkillOption = Option("Field Skills", QOL, "Reduce field skill tedium")
FieldSkillOption_Reduce = SubOption("Reduce All Field Skills", FieldSkillOption, commands=[lambda: FieldSkills.ReduceFieldSkillsLevels()])
FieldSkillOption_Reduce_Spinbox = SubSpinbox(FieldSkillOption_Reduce, max=12, default=3, increment=1, description="Level(s) Reduced")
FieldSkillOption_Remove = SubOption("Remove Field Skills", FieldSkillOption, defState=False, commands=[lambda: FieldSkills.DropdownRemoveStoryFieldSkills()])
FieldSkillOption_Remove_Dropdown = SubDropdown(FieldSkillOption_Remove, [DropdownOption("Story"), DropdownOption("All")], sort=False)
EasySkillTreesOption = Option("Easy Affinity Trees", QOL, "Makes trust the only condition for leveling up a blade's affinity tree", [lambda: SkillTrees.BladeSkillTreeShortening(IDs.ValidBladeIDs, 15), lambda: SkillTrees.BladeSkillTreeShortening(IDs.TornaBladeIDs, 15)])
BoostOption = Option("Resource Boosts", QOL, "Various boosts to resources (exp, wp etc.)")
BoostOption_EXP = SubOption("EXP Boost", BoostOption, [lambda: Helper.MathmaticalColumnAdjust(["./XC2/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], [f'row[key] // {BoostOption_EXP_Spinbox.GetState()}'])])
BoostOption_EXP_Spinbox = SubSpinbox(BoostOption_EXP, default=2, min=2, increment=1, description="x Faster")
BoostOption_SP = SubOption("SP Boost", BoostOption, [lambda: Helper.MathmaticalColumnAdjust(Helper.StartsWith("./XC2/JsonOutputs/common/BTL_Skill_Dr_Table0", 1, 6, addJson=True) + ["XC2/JsonOutputs/common/BTL_Skill_Dr_Table17.json", "XC2/JsonOutputs/common/BTL_Skill_Dr_Table18.json", "XC2/JsonOutputs/common/BTL_Skill_Dr_Table19.json"], ["NeedSp"], [f'row[key] // {BoostOption_SP_Spinbox.GetState()}'])])
BoostOption_SP_Spinbox = SubSpinbox(BoostOption_SP, default=2, increment=1, min=2, description="x Faster")
BoostOption_WP = SubOption("WP Boost", BoostOption, [lambda: Helper.MathmaticalColumnAdjust(["XC2/JsonOutputs/common/BTL_Arts_Dr.json"], ["NeedWP1", "NeedWP2", "NeedWP3", "NeedWP4", "NeedWP5"], [f'row[key] // {BoostOption_WP_Spinbox.GetState()}'])])
BoostOption_WP_Spinbox = SubSpinbox(BoostOption_WP, 2, increment=1, default=2, description="x Faster")
BoostOption_Speed = SubOption("Movespeed Boost", BoostOption, [lambda: QualityOfLife.AddMovespeedDeed()])
BoostOption_Speed_Spinbox = SubSpinbox(BoostOption_Speed,0,500,5,150, description="% Increase")
FreelyEngageBladesOption = Option("Freely Engage Blades", QOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])
ChestOption = Option("Treasure Chests", QOL, "Suboptions control various things about treasure chests", prio = Last) # Not using the description because that only applies to Race Mode. Race Mode should just automatically enforce CTMC
ChestOption_CTMCOption = SubOption("Chest Type Matches Contents", ChestOption, [lambda: I.ChestTypeMatchesContentsValue()], prio = Last)
ChestOption_VisibilityOption = SubOption("Increase Chest Visibility", ChestOption, [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
ChestOption_CondenseGoldOption = SubOption("Condense Gold Loot", ChestOption, [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"),["goldPopMin", "goldPopMax"], Helper.InclRange(0,100000), [1])])
# PickupRangeOption = Option("Increase Pickup Range", QOL, "Increases your pickup range" , [lambda: QualityOfLife.CollectionRange()]) No longer needed now that chests QOL is forced so they disappear and let you get the loot
EverlastingPouchItemsOption = Option("Everlasting Pouch Items", QOL, "Makes Pouch Items last as long as possible", [lambda: JSONParser.ChangeJSONFile(["common/ITM_FavoriteList.json"],["Time"], Helper.InclRange(0,255), [6099])])
MutePopupsOption = Option("Mute Popups", QOL, "Stops blade skill and pouch item refill popups", [lambda: (JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[89], ["sheet06"], [""]), JSONParser.ChangeJSONLine(["common/MNU_Layer_Dlc03.json"],[320], ["sheet06"], [""]))])
MutePopupsOption_Landmarks = SubOption("Landmarks", MutePopupsOption, [lambda: (JSONParser.ChangeJSONLine(["common/MNU_Layer.json"], [85], ["sheet04"], [""]),JSONParser.ChangeJSONLine(["common/MNU_Layer_Dlc03.json"],[316], ["sheet04"], [""]))])
NewGamePlusFlagsOption = Option("NG+ Flags", QOL, "Enables many NG+ behaviours like unlocked hidden driver skill trees, unlocked chain attacks from the start, unlocked blade slots etc. These must be accepted from the DLC Menu to work.", [lambda: QualityOfLife.CreateDLCtoSetFlag(["2nd Blade Equip Slot", "3rd Blade Equip Slot"], [35327, 35328], [2,2], [0,0], [1,1], [1,1]), lambda: QualityOfLife.CreateDLCtoSetFlag(["Driver Skill Tree Key"], [48589], Condition = [1853]), lambda: CoreCry.UnlockNGPlusBladesGacha()])

# Funny
MusicOption = Option("Music", Funny, "Randomizes Music", [lambda: MusicShuffling.MusicShuffle()], descData=lambda: MusicShuffling.MusicRandoDescription())
MusicOption_MixBattleAndEnv = SubOption("Mix Battle/Environment Themes", MusicOption, defState = False)
BladeSpecialButtonsOption = Option("Button Combos", Funny, "Randomizes inputs for button challenges", [lambda: Misc.BladeSpecialButtonChallenges()])
BladeSpecialButtonsOption_ABXY = SubOption("ABXY", BladeSpecialButtonsOption)
BladeSpecialButtonsOption_Mystery = SubOption("?", BladeSpecialButtonsOption)
ProjTreasureChestOption = Option("Projectile Treasure Chests", Funny, "Launches your items from chests",[lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [15])])
BladeSizeOption = Option("Blade Size", Funny, "Randomizes the size of Blades", [lambda: Scales.BladeScales()], prio=0)
BladeSizeOption_Spinbox = Spinbox(BladeSizeOption)
NPCSizeOption = Option("NPC Size", Funny, "Randomizes the size of NPCs", [lambda: Scales.NPCScales()])
NPCSizeOption_Spinbox = Spinbox(NPCSizeOption)
# EnemySizeOption = Option("Enemy Size", Funny, "Randomizes the size of enemies", [lambda: Scales.EnemyScales()], prio=0)
# EnemySizeOption_Spinbox = Spinbox(EnemySizeOption)
# FieldItemOption = Option("Field Item Size", Funny, "Randomizes the size and spin rate of items dropped on the field.", [lambda: Misc.BigItemsRando()], descData=lambda: Misc.BigItemsDesc())

# Cosmetics
BladeWeaponCosmeticsOption = Option("Default Weapon Appearance", CosmeticsTab, "Keeps all default weapon models regardless of chips", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["OnlyWpn"], [0], [1])])
TrustLineOption = Option("Blade Trust Lines", CosmeticsTab, "Randomizes blade-driver trust lines in battle (colors, power, etc.)", [lambda: Misc.BeamRandomizer()])
CosmeticsOption = Option("Character Outfits", CosmeticsTab, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics.Cosmetics()], prio=51, descData=lambda: Cosmetics.CosmeticsDescription()) # Sub are created by another class
CosmeticsOption_Spinbox = Spinbox(CosmeticsOption, default=10, max=30)
for opt in Cosmetics.CosmeticsList: # To gen these since listing them here would be annoying
    opt.CreateSubOptions(CosmeticsOption)

# Game Modes
RaceModeOption = Option("Race Mode", GameModeTab, "Play through a condensed version of the game in this mode!", [lambda: RaceMode.RaceModeChanging()], descData = lambda: RaceMode.RaceModeDescription(), stepSpeed=0.01)
RaceModeOption_Zohar = SubOption("Zohar Fragment Hunt", RaceModeOption)
RaceModeOption_DLC = SubOption("DLC Item Removal", RaceModeOption)
UMHuntOption = Option("Unique Monster Hunt", GameModeTab, "Defeat Unique Monsters in this Roguelike mode!", [lambda: UMHuntMain.UMHunt()], descData= lambda: UMHuntMain.Description(), stepSpeed=0.01)
UMHuntOption_Spinbox = Spinbox(UMHuntOption, 1, 10, 1, 10, "Round(s)")
UMHuntOption_SuperbossWave = SubOption("Superboss Wave", UMHuntOption)
UMHuntOption_RandomLandmarks = SubOption("Random Starting Landmarks", UMHuntOption)

# Torna
# TornaCategory = TabCategory(GameModeTab, "Torna", [])

TornaMainOption = Option("Torna Randomization", GameModeTab, "Randomizes the Torna DLC, in a logic-based method.", [lambda: TornaMain.AllTornaRando()], descData=lambda:TornaMain.TornaMainDescription())
TornaMainOption_CollectionPoints = SubOption("Collection Points", TornaMainOption)
TornaMainOption_EnemyDrops = SubOption("Enemy Drops", TornaMainOption)
TornaMainOption_EnemyDrops_Spinbox = SubSpinbox(TornaMainOption_EnemyDrops, default=1, min=1, max=8, increment=1, description="Items")
TornaMainOption_GroundItems = SubOption("Ground Items", TornaMainOption)
TornaMainOption_Shops = SubOption("Shops", TornaMainOption)
TornaMainOption_Shops_Spinbox = SubSpinbox(TornaMainOption_Shops, default=1, min=1, max=15, increment=1, description="Items")
TornaMainOption_SideQuests = SubOption("Side Quests", TornaMainOption)
TornaMainOption_SideQuests_Spinbox = SubSpinbox(TornaMainOption_SideQuests, default=1, min=1, max=4, increment=1, description="Items")
TornaMainOption_TreasureChests = SubOption("Treasure Chests", TornaMainOption)
TornaMainOption_TreasureChests_Spinbox = SubSpinbox(TornaMainOption_TreasureChests, default=1, min=1, max=8, increment=1, description="Items")

TornaCreateSpoilerLog = Option("Torna Spoiler Log", GameModeTab, "Outputs a Spoiler Log containing information on where each item is placed, located in XC2/Torna_Spoiler_Logs folder.")
TornaAddHints = Option("Torna In-Game Hints", GameModeTab, "Adds hints to the in the \"Tips\" Submenu in-game.", descData=lambda:TornaMain.TornaHintDescription())
TornaAddHints_ItemHints = SubOption("Item Hints", TornaAddHints)
TornaAddHints_ItemHints_Spinbox = SubSpinbox(TornaAddHints_ItemHints, 1, 12, 1, 1, "Hints")
TornaAddHints_LocProgHints = SubOption("Location Hints", TornaAddHints)
TornaAddHints_LocProgHints_Spinbox = SubSpinbox(TornaAddHints_LocProgHints, 1, 12, 1, 1, "Hints")
TornaObjectColorMatchesContents = Option("Torna Gilded Required Check Names", GameModeTab, "Turns names of Checks with Progression Items gold.", descData=lambda:TornaMain.TornaCCMCDescription())
TornaChooseCommunityReqs = Option("Torna Community Level Requirements", GameModeTab, "Changes the Community Level requirement for the story events.", descData=lambda:TornaMain.TornaStoryReqChangeDescription())
TornaChooseCommunityReqs_Gate1Req = SubOption("Gate 1 Required Level", TornaChooseCommunityReqs)
TornaChooseCommunityReqs_Gate1Req_Spinbox = SubSpinbox(TornaChooseCommunityReqs_Gate1Req, default=0, min=0, max=2, increment=1)
TornaChooseCommunityReqs_Gate2Req = SubOption("Gate 2 Required Level", TornaChooseCommunityReqs)
TornaChooseCommunityReqs_Gate2Req_Spinbox = SubSpinbox(TornaChooseCommunityReqs_Gate2Req, default=0, min=0, max=4, increment=1)

TornaRemoveGormottChecks = Option("Torna Gormott Exceptions", GameModeTab, "Progression Items will not be found in Checks near locations in Gormott selected below.")
for loc in TornaMain.GormottNametoLocID.keys(): # Automatically Generates these
    SubOption(loc, TornaRemoveGormottChecks)
TornaRewardsonUnreqSidequests = Option("Torna Unrequired Sidequests", GameModeTab, "Sidequests not chosen for the main story requirements or story gates can have Progression Items on their rewards.")


MutuallyExclusivePairing([TornaMainOption, TornaAddHints, TornaObjectColorMatchesContents, TornaChooseCommunityReqs, TornaCreateSpoilerLog, TornaRemoveGormottChecks, TornaRewardsonUnreqSidequests], [AccessoriesOption, CommunityMembersOption, QuestRewardsOption, AuxCoresOption, AccessoryShopsOption, PouchItemShopOption, TreasureChestOption, WeaponChipShopOption, DriversOption, BladesOption, BladeArtsOption, BladeFieldSkillsOption, BladeWeaponChipsOption, BladeCombosOption, BladeStatsOption, NormalEnemyOption, UniqueEnemyOption, BossEnemyOption, EnemyDropOption, TreasureChestOption, FreelyEngageBladesOption, ChestOption, FieldSkillOption, EasySkillTreesOption, BoostOption, NewGamePlusFlagsOption, ProjTreasureChestOption, BladeWeaponCosmeticsOption, CosmeticsOption, RaceModeOption, UMHuntOption])
MutuallyExclusivePairing([UMHuntOption], [TutorialShorteningOption, AccessoryShopsOption, NewGamePlusFlagsOption, PouchItemShopOption, TreasureChestOption, WeaponChipShopOption, DriversOption, BladeWeaponChipsOption, AccessoriesOption, AuxCoresOption, NormalEnemyOption, BossEnemyOption, UniqueEnemyOption, EnemyDropOption, TreasureChestOption, EasySkillTreesOption, BoostOption, RaceModeOption, FieldSkillOption])
MutuallyExclusivePairing([RaceModeOption], [DriversOption, BladesOption, ShortcutsOption, ChestOption, TutorialShorteningOption])
    
# Currently Disabled for Various Reasons
# Blade Names (moved so that blade name rando doesn't mess up Race Mode getting blade IDs)
# GenStandardOption("Blade Names", TabBlades, "Randomizes a Blade's name", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
# GenStandardOption("Less UI", TabQOL, "Removes some of the unneccessary on screen UI (Blade Swap and Current Objective)", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03"], [""])])
# GenStandardOption("Screenshot Mode", TabQOL, "Removes most UI for screenshots", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03", "sheet04"], ""), lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[86], ["sheet02", "sheet03"], "")])
# GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
# GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
# GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
# GenStandardOption("Blade Weapons", TabBlades, "Randomizes a Blade Weapon type, for example Pyra can now be a Knuckle Claws user", [lambda: _BladeWeapons.WepRando()])
# GenStandardOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials,  list(set(BladeSpecials) - set([215])))]) works okay, but animations dont connect feels mid
# DebugLog.CreateDebugLog(OptionDictionary, Version, randoSeedEntry.get())
# GenStandardOption("Enemy Arts", TabEnemies, "Gives enemies new arts", [lambda: _EnemyArts.EnemyArts(OptionDictionary["Enemy Arts"]["spinBoxVal"].get())],optionType=Spinbox)
# EnemyMovespeedOption = Option("Enemy Movespeed", Enemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))])
# GenStandardOption("Enemy Rage", TabEnemies, "Randomizes the effects of enemy enraged states", ["common/BTL_Aura"])   
# EnemyAggroOption = Option("Enemy Aggro", Enemies, "Reduces the number of enemies who aggro you by a percentage", [lambda: Enemy.EnemyAggro()], hasSpinBox = True)
# TornaCompatibleOptions = [BladeSpecialButtonsOption, TornaChooseCommunityReqs, CondenseGoldOption, TornaCreateSpoilerLog, EnhancementDisplayOption, EverlastingPouchItemsOption, FieldItemOption, TornaObjectColorMatchesContents, StartwithIncreasedMovespeedOption, MusicOption, MutePopupsOption, NPCSizeOption, TornaRemoveGormottChecks, ShortcutsOption, TornaAddHints, TornaMainOption, TreasureChestVisOption, TrustLineOption, TornaRewardsonUnreqSidequests, EnemyEnhancementsOption, EnemyArtEffectsOption, BladeWeaponChipsOption, BladeSpecialOption, BladeBattleSkillsOption]
