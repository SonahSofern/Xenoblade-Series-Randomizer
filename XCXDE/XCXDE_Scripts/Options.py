from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XCXDE.XCXDE_Scripts import Enemy, IDs, Items as Item, QOL as q, PartyMem, Skell

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
# https://xenobladedata.github.io/xbx/bdat/common_local_us/DRP_ItemTable.html#309

# Items
# Shops (SHP_* ) (NO POINT theres only one shop and it has almost every item in the game, just randomize the item effects themselves)
# ShopOption = Option("Shops", Items, "Randomizes NLA's shop inventories into the same item type", [lambda: Item.QuestRewards()])
# ShopOption_Wep = SubOption("Weapon Shop", ShopOption)
# ShopOption_Arm = SubOption("Armor Shop", ShopOption)
# ShopOption_SkWep = SubOption("Skell Weapon Shop", ShopOption)
# ShopOption_SkArm = SubOption("Skell Armor Shop", ShopOption)
# ShopOption_SkFrame = SubOption("Skell Frame Shop", ShopOption)


# Field Skill Drops
TboxOption = Option("Field Checks", Items, "Randomizes treasures from field checks into the chosen types", [lambda: Item.Tbox()])
TboxOption_Gear = SubOption("Ground Gear", TboxOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
TboxOption_Gems = SubOption("Augments", TboxOption, hasSpinBox=True, spinDefault=30)
TboxOption_SkellGear = SubOption("Skell Gear", TboxOption, hasSpinBox=True, spinDefault=10) 
TboxOption_SkellGems = SubOption("Skell Augments", TboxOption, hasSpinBox=True, spinDefault=10)
TboxOption_Probes = SubOption("Probes", TboxOption, hasSpinBox=True, spinDefault=40)
TboxOption_Collectibles = SubOption("Collectibles", TboxOption, hasSpinBox=True, spinDefault=5)
TboxOption_Materials = SubOption("Materials", TboxOption, hasSpinBox=True, spinDefault=5)
TboxOption_Precious = SubOption("Key Items", TboxOption, hasSpinBox=True, spinDefault=5)
TboxOption_Misc = SubOption("Misc.", TboxOption, hasSpinBox=True, spinDefault=5)

# Quest Rewards https://xenobladedata.github.io/xbx/bdat/common_local_us/QUEST_itemset.html
QuestRewardOption = Option("Quest Rewards", Items, "Randomizes quest rewards into the chosen types", [lambda: Item.QuestRewards()])
QuestRewardOption_Gear = SubOption("Ground Gear", QuestRewardOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
QuestRewardOption_Gems = SubOption("Augments", QuestRewardOption, hasSpinBox=True, spinDefault=20)
QuestRewardOption_SkellGear = SubOption("Skell Gear", QuestRewardOption, hasSpinBox=True, spinDefault=20) 
QuestRewardOption_SkellGems = SubOption("Skell Augments", QuestRewardOption, hasSpinBox=True, spinDefault=10)
QuestRewardOption_Probes = SubOption("Probes", QuestRewardOption, hasSpinBox=True, spinDefault=10)
QuestRewardOption_Collectibles = SubOption("Collectibles", QuestRewardOption, hasSpinBox=True, spinDefault=1)
QuestRewardOption_Materials = SubOption("Materials", QuestRewardOption, hasSpinBox=True, spinDefault=2)
QuestRewardOption_Precious = SubOption("Key Items", QuestRewardOption, hasSpinBox=True, spinDefault=5)
QuestRewardOption_Misc = SubOption("Misc.", QuestRewardOption, hasSpinBox=True, spinDefault=5)

# Ticket Shop https://xenobladedata.github.io/xbx/bdat/common_local_us/ITM_TradeList.html
TicketExchangeOption = Option("Ticket Rewards", Items, "Randomizes the ticket exchange shop into the chosen types", [lambda: Item.TicketShop()])
TicketExchangeOption_Gear = SubOption("Ground Gear", TicketExchangeOption, hasSpinBox=True, spinDefault=10, spinDesc=weightsSpinDescription)
TicketExchangeOption_Gems = SubOption("Augments", TicketExchangeOption, hasSpinBox=True, spinDefault=10)
TicketExchangeOption_SkellGear = SubOption("Skell Gear", TicketExchangeOption, hasSpinBox=True, spinDefault=10) 
TicketExchangeOption_SkellGems = SubOption("Skell Augments", TicketExchangeOption, hasSpinBox=True, spinDefault=10)
TicketExchangeOption_Probes = SubOption("Probes", TicketExchangeOption, hasSpinBox=True, spinDefault=20)
TicketExchangeOption_Collectibles = SubOption("Collectibles", TicketExchangeOption, hasSpinBox=True, spinDefault=40)
TicketExchangeOption_Materials = SubOption("Materials", TicketExchangeOption, hasSpinBox=True, spinDefault=40)
TicketExchangeOption_Precious = SubOption("Key Items", TicketExchangeOption, hasSpinBox=True, spinDefault=40)
TicketExchangeOption_Misc = SubOption("Misc.", TicketExchangeOption, hasSpinBox=True, spinDefault=40)

# Collectapedia Rewards https://xenobladedata.github.io/xbx/bdat/common_local_us/collepediareward.html
CollectapediaRewardOption = Option("Collectapedia Rewards", Items, "Randomizes collectapedia rewards into the chosen types", [lambda: Item.CollectapediaRewards()])
CollectapediaRewardOption_Gear = SubOption("Ground Gear", CollectapediaRewardOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
CollectapediaRewardOption_Gems = SubOption("Augments", CollectapediaRewardOption, hasSpinBox=True, spinDefault=40)
CollectapediaRewardOption_SkellGear = SubOption("Skell Gear", CollectapediaRewardOption, hasSpinBox=True, spinDefault=10) 
CollectapediaRewardOption_SkellGems = SubOption("Skell Augments", CollectapediaRewardOption, hasSpinBox=True, spinDefault=20)
CollectapediaRewardOption_Probes = SubOption("Probes", CollectapediaRewardOption, hasSpinBox=True, spinDefault=20)
CollectapediaRewardOption_Collectibles = SubOption("Collectibles", CollectapediaRewardOption, hasSpinBox=True, spinDefault=1)
CollectapediaRewardOption_Materials = SubOption("Materials", CollectapediaRewardOption, hasSpinBox=True, spinDefault=1)
CollectapediaRewardOption_Precious = SubOption("Key Items", CollectapediaRewardOption, hasSpinBox=True, spinDefault=5)
CollectapediaRewardOption_Misc = SubOption("Misc.", CollectapediaRewardOption, hasSpinBox=True, spinDefault=1)

# Enemy Drops
EnemyDropOption = Option("Enemy Drops", Items, "Randomizes enemy drops into the chosen types", [lambda: Item.EnemyDrops()])
EnemyDropOption_Gear = SubOption("Ground Gear", EnemyDropOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
EnemyDropOption_Gems = SubOption("Augments", EnemyDropOption, hasSpinBox=True, spinDefault=20)
EnemyDropOption_SkellGear = SubOption("Skell Gear", EnemyDropOption, hasSpinBox=True, spinDefault=20) 
EnemyDropOption_SkellGems = SubOption("Skell Augments", EnemyDropOption, hasSpinBox=True, spinDefault=10)
EnemyDropOption_Probes = SubOption("Probes", EnemyDropOption, hasSpinBox=True, spinDefault=1)
EnemyDropOption_Collectibles = SubOption("Collectibles", EnemyDropOption, hasSpinBox=True, spinDefault=5)
EnemyDropOption_Materials = SubOption("Materials", EnemyDropOption, hasSpinBox=True, spinDefault=50)
EnemyDropOption_Precious = SubOption("Key Items", EnemyDropOption, hasSpinBox=True, spinDefault=5)
EnemyDropOption_Misc = SubOption("Misc.", EnemyDropOption, hasSpinBox=True, spinDefault=5)


# Probe effects https://xenobladedata.github.io/xbx/bdat/common_local_us/ITM_BeaconList.html


# Enemies
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsterIDs, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_Size.GetState())], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True, prio=2)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=10, spinDesc=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True, spinDefault=1)
NormalEnemyOption_Aggro = SubOption("Vanilla Aggro", NormalEnemyOption)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.TyrantMonsterIDs + IDs.SuperbossMonstersIDs, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True, prio=2)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=1, spinDesc=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=10)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=1)
UniqueEnemyOption_Aggro = SubOption("Vanilla Aggro", UniqueEnemyOption)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonstersIDs, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, True, True, finalBoss=BossEnemyOption_FinalBoss.GetState())], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True, prio=2)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=2, spinDesc=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False, hasSpinBox=True, spinDefault=1)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)
# BossEnemyOption_Group = SubOption("Balance Group Fights", BossEnemyOption)

# Too much hard coded stuff for this to work, also it doesn't really accomplish much the biggest change is your starting stuff which can just be randomized anyway
# ClassTreeOption = Option("Class Tree", Character, "Randomizes the class advancement tree and default player class", [lambda: Class.ClassTree()]) # https://xenobladedata.github.io/xbx/bdat/common_local_us/CHR_ClassInfo.html
CharacterOption = Option("Party Members", Character, "Randomizes party members", [lambda: PartyMem.Members()])
CharacterOption_Duplicates = SubOption("Allow Duplicates", CharacterOption)
CharacterOption_BalanceGear = SubOption("Balance Starting Gear", CharacterOption)
# Gems https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_ItemSkill_inner.html#2191
# Weapons
# Armor
# Skells
intensityText= "Intensity (Low 1 - High 100)"

SkellStats = Option("Skell Stats", Skells, "Randomizes the base stats of skells in a balanced way", [lambda: Skell.SkellBaseStats(SkellStats.GetSpinbox())], hasSpinBox=True, spinDesc=intensityText, spinMin=1)
SkellArmor = Option("Skell Gear", Skells, "Randomizes the stats of Skell Gear")
SkellArmor_Arm = SubOption("Skell Armor", SkellArmor, [lambda: Skell.SkellArmorStats(SkellArmor_Arm.GetSpinbox())], hasSpinBox=True, spinDesc=intensityText, spinMin=1)
SkellArmor_Wep = SubOption("Skell Weapon", SkellArmor, [lambda: Skell.SkellWepStats(SkellArmor_Wep.GetSpinbox())], hasSpinBox=True, spinDesc=intensityText, spinMin=1)
SkellArts = Option("Skell Arts", Skells, "Randomizes the skell art strength")

# Levitaths = [161,162,215, 1341] Title Screen Levitaths?

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_MainQuestReqs = SubOption("Skip Chapter Prerequisites", ShortcutsOption, [lambda: q.EasyStoryPrerequisites()])
ShortcutsOption_SkellHell = SubOption("Skip Skell License Exam", ShortcutsOption, [lambda: q.SkellExamSkip()])
SkellFlightOption = Option("Early Flight Module", QOL, "Flight Module is unlocked immediately after getting skells", [lambda: q.EarlyFlight()]) # https://xenobladedata.github.io/xbx/bdat/common_local_us/CHR_DlList.html

# TutorialSkipOption = Option("Tutorial Skip", QOL, "Removes tutorials") 
FasterLevelsOption = Option("EXP Boost", QOL, "Decreases EXP required for each levelup", [lambda: Helper.MathmaticalColumnAdjust(["XCXDE/JsonOutputs/common/BTL_Growlist.json"], ["LevelExp"], [f'row[key] // {FasterLevelsOption.GetSpinbox()}'])], hasSpinBox=True, spinDefault=2, spinIncr = 1, spinDesc = "x Faster")
FasterClassOption = Option("CP Boost", QOL, "Decreases CP required for each class levelup", [lambda: q.FasterClassRanks(FasterClassOption.GetSpinbox())], hasSpinBox=True, spinDefault=2, spinMin=2, spinMax= 10, spinIncr = 1, spinDesc = "x Faster")
YellowBubbleOption = Option("Info Range", QOL, "Increased range for collecting info bubbles", [lambda: q.InfoRangeIncrease(YellowBubbleOption.GetSpinbox(), YellowBubbleOption_Mute.GetState())], hasSpinBox=True, spinDesc="x Range", spinDefault=15, spinMin=2)
YellowBubbleOption_Mute = SubOption("Mute Callouts", YellowBubbleOption)
# SKell Flight Music? https://xenobladedata.github.io/xbx/bdat/common_local_us/RSC_BgmCondition.html
# Faster Party Affinity

# BetterFrontierNavOption = Option("Frontier Nav Boost", QOL, "Faster rewards from FrontierNav")
# SkellLiscOption = Option("Skell License Unlock", QOL, "Sets the unlock chapter for skells")
# SkellLiscOption_ChSelect = SubOption("Fixed Unlock", SkellLiscOption, hasSpinBox=True, spinMax=12, spinDesc="Unlock Chapter") # https://xenobladedata.github.io/xbx/bdat/common_local_us/FLD_questlist.html#1143
# SkellLiscOption_ChSelect = SubOption("Random Unlock", SkellLiscOption)

# SkellEasyCruiseOption = Option("Easy Cruise Mode", QOL, "Hraesvelg Cruise Mode is unlocked") # FLD_questlist 2524 is the hraesvelg cruise mode quest, somethere there unlocks it.


from scripts import Onefile
if not Onefile.isOneFile:
    OPWeapon = Option("OP Weapons", QOL, "For Testing makes starter weapons op", [lambda: q.OpWep()])


# Funny
# Color Randomization https://xenobladedata.github.io/xbx/bdat/common_local_us/CLR_List.html