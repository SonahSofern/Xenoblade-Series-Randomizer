from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XCXDE.XCXDE_Scripts import Enemy, IDs, Items as Item

scripts.Interactables.Game = "XCXDE" 

Items = 1
Character  = 2
Enemies = 3
QOL = 4
Skells = 5 

Tabs = {
    Items: 'Items',
    Character: 'Characters',
    Skells: 'Skells',
    Enemies: 'Enemies',
    QOL: 'Quality of Life',
}

weightsSpinDescription = "Weights ↓"

# Enemy/Appendage Drops (NO POINT)
# Items

# https://xenobladedata.github.io/xbx/bdat/common_local_us/DRP_ItemTable.html#309
# Field Skill Drops # https://xenobladedata.github.io/xbx/bdat/common_local_us/FLD_TboxAll.html
TboxOption = Option("Treasures", Items, "Randomizes treasures from Archaeological, Mechanical and Biological field checks", [lambda: Item.Tbox()])
TboxOption_Gear = SubOption("Ground Gear", TboxOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
TboxOption_SkellGear = SubOption("Skell Gear", TboxOption, hasSpinBox=True, spinDefault=30)
TboxOption_Gems = SubOption("Augments", TboxOption, hasSpinBox=True, spinDefault=30)
TboxOption_SkellGems = SubOption("Skell Augments", TboxOption, hasSpinBox=True, spinDefault=30)
TboxOption_Probes = SubOption("Probes", TboxOption, hasSpinBox=True, spinDefault=30)
TboxOption_Collectibles = SubOption("Collectibles", TboxOption, hasSpinBox=True, spinDefault=30)


# Quest Rewards
# Shops (SHP_* )
# Collectapedia Rewards https://xenobladedata.github.io/xbx/bdat/common_local_us/collepediareward.html

# Probe effects https://xenobladedata.github.io/xbx/bdat/common_local_us/ITM_BeaconList.html


# Enemies
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsterIDs, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption)], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True, prio=2)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=10, spinDesc=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True, spinDefault=1)
NormalEnemyOption_Aggro = SubOption("Vanilla Aggro", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.TyrantMonsterIDs + IDs.SuperbossMonstersIDs, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True, prio=2)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=1, spinDesc=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=10)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=1)
UniqueEnemyOption_Aggro = SubOption("Vanilla Aggro", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonstersIDs, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, True, finalBoss=BossEnemyOption_FinalBoss.GetState())], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True, prio=2)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=2, spinDesc=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False, hasSpinBox=True, spinDefault=1)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)
# BossEnemyOption_Group = SubOption("Balance Group Fights", BossEnemyOption)

# ClassTreeOption = Option("Class Tree", Character, "Randomizes the class advancement tree") # https://xenobladedata.github.io/xbx/bdat/common_local_us/CHR_ClassInfo.html
# Gems https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_ItemSkill_inner.html#2191
# Weapons
# Armor
# Skells

# ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
# ShortcutsOption_MainQuestReqs = SubOption("Chapter Prerequisites Skip", ShortcutsOption)
# TutorialSkipOption = Option("Tutorial Skip", QOL, "Removes tutorials") 
FasterLevelsOption = Option("EXP Boost", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["XCXDE/JsonOutputs/common/BTL_Growlist.json"], ["LevelExp"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1, spinDesc = "x Faster")
FasterClassOption = Option("CP Boost", QOL, "Decreases CP required for each class levelup", [lambda: Helper.MathmaticalColumnAdjust(["XCXDE/JsonOutputs/common/BTL_ClassGrowlist.json"], ["LevelCpR0", "LevelCpR1", "LevelCpR2"], [f'row[key] // {FasterClassOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1, spinDesc = "x Faster")
# BetterFrontierNavOption = Option("Frontier Nav Boost", QOL, "Faster rewards from FrontierNav")
# Skell = Option("Skell", QOL, "QOL options for Skells")
# Skell_EasyLisc = SubOption("Easy Skell Liscense", Skell)
# Skell_EarlyLisc = SubOption("Early Skell Liscense", Skell)
# Skell_EasyFlight = SubOption("Easy Flight Module", Skell)
# Skell_EarlyFlight = SubOption("Early Flight Module", Skell)


# Funny
# Color Randomization https://xenobladedata.github.io/xbx/bdat/common_local_us/CLR_List.html