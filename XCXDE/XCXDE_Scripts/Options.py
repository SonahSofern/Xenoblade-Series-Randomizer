from scripts.Interactables import Option, SubOption, SubSpinbox, Spinbox, Dropdown, SubDropdown
from scripts import Helper
import scripts.Interactables
from XCXDE.XCXDE_Scripts import Enemy, Gear, IDs, Items as Item, QOL as q, PartyMem, Art, Skill, SkellFrames

scripts.Interactables.Game = "XCXDE" 

Items = 1
Character  = 2
Enemies = 3
QOL = 4
Skells = 5 
Misc = 6

Tabs = {
    Items: 'Items',
    Character: 'Characters',
    Skells: 'Skells',
    Enemies: 'Enemies',
    QOL: 'Quality of Life',
    # Misc: 'Misc.'
}

weightsSpinDescription = "Weights ↓"
intensityText= "Intensity (Low 1 - High 100)"

# ---------- POTENTIAL ----------
# http://127.0.0.1:5500/html/MNU_MemberChange.html#21 Party member join conditions?
# Faster Party Affinity
# Gems https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_ItemSkill_inner.html#2191
# Skills (Make enhance file and option to add new skills)
# SkellArts = Option("Skell Arts", Skells, "Randomizes the skell art strength")
# Soul Voices https://xenobladedata.github.io/xbx/bdat/common_local_us/BTL_SoulArts.html
# SKell Flight Music? https://xenobladedata.github.io/xbx/bdat/common_local_us/RSC_BgmCondition.html
# SkellEasyCruiseOption = Option("Easy Cruise Mode", QOL, "Hraesvelg Cruise Mode is unlocked") # FLD_questlist 2524 is the hraesvelg cruise mode quest, somethere there unlocks it.
# ---------- POTENTIAL ----------

# ---------- NOT DOING ----------
# Color Randomization https://xenobladedata.github.io/xbx/bdat/common_local_us/CLR_List.html # Was the players colors and like the barracks not relevant
# Overdrive Route Rando (Can't because theres no way to see what changed)
# Enemy/Appendage Drops (NO POINT) https://xenobladedata.github.io/xbx/bdat/common_local_us/DRP_ItemTable.html#309
# Items
# Shops (SHP_* ) (NO POINT theres only one shop and it has almost every item in the game, just randomize the item effects themselves)
# ShopOption = Option("Shops", Items, "Randomizes NLA's shop inventories into the same item type", [lambda: Item.QuestRewards()])
# ShopOption_Wep = SubOption("Weapon Shop", ShopOption)
# ShopOption_Arm = SubOption("Armor Shop", ShopOption)
# ShopOption_SkWep = SubOption("Skell Weapon Shop", ShopOption)
# ShopOption_SkArm = SubOption("Skell Armor Shop", ShopOption)
# ShopOption_SkFrame = SubOption("Skell Frame Shop", ShopOption)
# ClassTreeOption = Option("Class Tree", Character, "Randomizes the class advancement tree and default player class", [lambda: Class.ClassTree()]) # https://xenobladedata.github.io/xbx/bdat/common_local_us/CHR_ClassInfo.html # Too much hard coded stuff for this to work, also it doesn't really accomplish much the biggest change is your starting stuff which can just be randomized anyway
# ---------- NOT DOING ----------


# Field Skill Drops
TboxOption = Option("Field Checks", Items, "Randomizes treasures from field checks into the chosen types", [lambda: Item.Tbox()], descData=lambda: Item.TboxDescription(TboxOption.name))
TboxOption_Gear = SubOption("Ground Gear", TboxOption)
TboxOption_Gear_Spinbox = SubSpinbox(TboxOption_Gear, default=30, description=weightsSpinDescription)
TboxOption_Gems = SubOption("Augments", TboxOption)
TboxOption_Gems_Spinbox = SubSpinbox(TboxOption_Gems, default=30)
TboxOption_SkellGear = SubOption("Skell Gear", TboxOption)
TboxOption_SkellGear_Spinbox = SubSpinbox(TboxOption_SkellGear, default=10)
TboxOption_SkellGems = SubOption("Skell Augments", TboxOption)
TboxOption_SkellGems_Spinbox = SubSpinbox(TboxOption_SkellGems, default=10)
TboxOption_Probes = SubOption("Probes", TboxOption)
TboxOption_Probes_Spinbox = SubSpinbox(TboxOption_Probes, default=40)
TboxOption_Collectibles = SubOption("Collectibles", TboxOption)
TboxOption_Collectibles_Spinbox = SubSpinbox(TboxOption_Collectibles, default=5)
TboxOption_Materials = SubOption("Materials", TboxOption)
TboxOption_Materials_Spinbox = SubSpinbox(TboxOption_Materials, default=5)
TboxOption_Precious = SubOption("Key Items", TboxOption)
TboxOption_Precious_Spinbox = SubSpinbox(TboxOption_Precious, default=5)
TboxOption_Misc = SubOption("Misc.", TboxOption)
TboxOption_Misc_Spinbox = SubSpinbox(TboxOption_Misc, default=5)

# Quest Rewards https://xenobladedata.github.io/xbx/bdat/common_local_us/QUEST_itemset.html
QuestRewardOption = Option("Quest Rewards", Items, "Randomizes quest rewards into the chosen types", [lambda: Item.QuestRewards()])
QuestRewardOption_Gear = SubOption("Ground Gear", QuestRewardOption)
QuestRewardOption_Gear_Spinbox = SubSpinbox(QuestRewardOption_Gear, default=30, description=weightsSpinDescription)
QuestRewardOption_Gems = SubOption("Augments", QuestRewardOption)
QuestRewardOption_Gems_Spinbox = SubSpinbox(QuestRewardOption_Gems, default=20)
QuestRewardOption_SkellGear = SubOption("Skell Gear", QuestRewardOption)
QuestRewardOption_SkellGear_Spinbox = SubSpinbox(QuestRewardOption_SkellGear, default=20)
QuestRewardOption_SkellGems = SubOption("Skell Augments", QuestRewardOption)
QuestRewardOption_SkellGems_Spinbox = SubSpinbox(QuestRewardOption_SkellGems, default=10)
QuestRewardOption_Probes = SubOption("Probes", QuestRewardOption)
QuestRewardOption_Probes_Spinbox = SubSpinbox(QuestRewardOption_Probes, default=10)
QuestRewardOption_Collectibles = SubOption("Collectibles", QuestRewardOption)
QuestRewardOption_Collectibles_Spinbox = SubSpinbox(QuestRewardOption_Collectibles, default=1)
QuestRewardOption_Materials = SubOption("Materials", QuestRewardOption)
QuestRewardOption_Materials_Spinbox = SubSpinbox(QuestRewardOption_Materials, default=2)
QuestRewardOption_Precious = SubOption("Key Items", QuestRewardOption)
QuestRewardOption_Precious_Spinbox = SubSpinbox(QuestRewardOption_Precious, default=5)
QuestRewardOption_Misc = SubOption("Misc.", QuestRewardOption)
QuestRewardOption_Misc_Spinbox = SubSpinbox(QuestRewardOption_Misc, default=5)

# Ticket Shop https://xenobladedata.github.io/xbx/bdat/common_local_us/ITM_TradeList.html
TicketExchangeOption = Option("Material Market", Items, "Randomizes the material market (ticket shop) into the chosen types", [lambda: Item.TicketShop()])
TicketExchangeOption_Gear = SubOption("Ground Gear", TicketExchangeOption)
TicketExchangeOption_Gear_Spinbox = SubSpinbox(TicketExchangeOption_Gear, default=10, description=weightsSpinDescription)
TicketExchangeOption_Gems = SubOption("Augments", TicketExchangeOption)
TicketExchangeOption_Gems_Spinbox = SubSpinbox(TicketExchangeOption_Gems, default=10)
TicketExchangeOption_SkellGear = SubOption("Skell Gear", TicketExchangeOption)
TicketExchangeOption_SkellGear_Spinbox = SubSpinbox(TicketExchangeOption_SkellGear, default=10)
TicketExchangeOption_SkellGems = SubOption("Skell Augments", TicketExchangeOption)
TicketExchangeOption_SkellGems_Spinbox = SubSpinbox(TicketExchangeOption_SkellGems, default=10)
TicketExchangeOption_Probes = SubOption("Probes", TicketExchangeOption)
TicketExchangeOption_Probes_Spinbox = SubSpinbox(TicketExchangeOption_Probes, default=20)
TicketExchangeOption_Collectibles = SubOption("Collectibles", TicketExchangeOption)
TicketExchangeOption_Collectibles_Spinbox = SubSpinbox(TicketExchangeOption_Collectibles, default=40)
TicketExchangeOption_Materials = SubOption("Materials", TicketExchangeOption)
TicketExchangeOption_Materials_Spinbox = SubSpinbox(TicketExchangeOption_Materials, default=40)
TicketExchangeOption_Precious = SubOption("Key Items", TicketExchangeOption)
TicketExchangeOption_Precious_Spinbox = SubSpinbox(TicketExchangeOption_Precious, default=40)
TicketExchangeOption_Misc = SubOption("Misc.", TicketExchangeOption)
TicketExchangeOption_Misc_Spinbox = SubSpinbox(TicketExchangeOption_Misc, default=40)

# Collectapedia Rewards https://xenobladedata.github.io/xbx/bdat/common_local_us/collepediareward.html
CollectapediaRewardOption = Option("Collectapedia Rewards", Items, "Randomizes collectapedia rewards into the chosen types", [lambda: Item.CollectapediaRewards()])
CollectapediaRewardOption_Gear = SubOption("Ground Gear", CollectapediaRewardOption)
CollectapediaRewardOption_Gear_Spinbox = SubSpinbox(CollectapediaRewardOption_Gear, default=30, description=weightsSpinDescription)
CollectapediaRewardOption_Gems = SubOption("Augments", CollectapediaRewardOption)
CollectapediaRewardOption_Gems_Spinbox = SubSpinbox(CollectapediaRewardOption_Gems, default=40)
CollectapediaRewardOption_SkellGear = SubOption("Skell Gear", CollectapediaRewardOption)
CollectapediaRewardOption_SkellGear_Spinbox = SubSpinbox(CollectapediaRewardOption_SkellGear, default=10)
CollectapediaRewardOption_SkellGems = SubOption("Skell Augments", CollectapediaRewardOption)
CollectapediaRewardOption_SkellGems_Spinbox = SubSpinbox(CollectapediaRewardOption_SkellGems, default=20)
CollectapediaRewardOption_Probes = SubOption("Probes", CollectapediaRewardOption)
CollectapediaRewardOption_Probes_Spinbox = SubSpinbox(CollectapediaRewardOption_Probes, default=20)
CollectapediaRewardOption_Collectibles = SubOption("Collectibles", CollectapediaRewardOption)
CollectapediaRewardOption_Collectibles_Spinbox = SubSpinbox(CollectapediaRewardOption_Collectibles, default=1)
CollectapediaRewardOption_Materials = SubOption("Materials", CollectapediaRewardOption)
CollectapediaRewardOption_Materials_Spinbox = SubSpinbox(CollectapediaRewardOption_Materials, default=1)
CollectapediaRewardOption_Precious = SubOption("Key Items", CollectapediaRewardOption)
CollectapediaRewardOption_Precious_Spinbox = SubSpinbox(CollectapediaRewardOption_Precious, default=5)
CollectapediaRewardOption_Misc = SubOption("Misc.", CollectapediaRewardOption)
CollectapediaRewardOption_Misc_Spinbox = SubSpinbox(CollectapediaRewardOption_Misc, default=1)

# # Enemy Drops
# EnemyDropOption = Option("Enemy Drops", Items, "Randomizes enemy drops into the chosen types", [lambda: Item.EnemyDrops()])
# EnemyDropOption_Gear = SubOption("Ground Gear", EnemyDropOption, hasSpinBox=True, spinDefault=30, spinDesc=weightsSpinDescription)
# EnemyDropOption_Gems = SubOption("Augments", EnemyDropOption, hasSpinBox=True, spinDefault=20)
# EnemyDropOption_SkellGear = SubOption("Skell Gear", EnemyDropOption, hasSpinBox=True, spinDefault=20) 
# EnemyDropOption_SkellGems = SubOption("Skell Augments", EnemyDropOption, hasSpinBox=True, spinDefault=10)
# EnemyDropOption_Probes = SubOption("Probes", EnemyDropOption, hasSpinBox=True, spinDefault=1)
# EnemyDropOption_Collectibles = SubOption("Collectibles", EnemyDropOption, hasSpinBox=True, spinDefault=5)
# EnemyDropOption_Materials = SubOption("Materials", EnemyDropOption, hasSpinBox=True, spinDefault=50)
# EnemyDropOption_Precious = SubOption("Key Items", EnemyDropOption, hasSpinBox=True, spinDefault=5)
# EnemyDropOption_Misc = SubOption("Misc.", EnemyDropOption, hasSpinBox=True, spinDefault=5)

# Enemies
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsterIDs, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_OopsAll.GetState(), NormalEnemyOption_OopsAll_Dropdown.GetState(), NormalEnemyOption_Size.GetState())], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), prio=2)
NormalEnemyOption_Spinbox = Spinbox(NormalEnemyOption)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
NormalEnemyOption_Normal_Spinbox = SubSpinbox(NormalEnemyOption_Normal, default=20, description=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
NormalEnemyOption_Unique_Spinbox = SubSpinbox(NormalEnemyOption_Unique, default=6)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
NormalEnemyOption_Boss_Spinbox = SubSpinbox(NormalEnemyOption_Boss, default=6)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)
NormalEnemyOption_Superboss_Spinbox = SubSpinbox(NormalEnemyOption_Superboss, default=1)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)
NormalEnemyOption_OopsAll = SubOption("Oops All", NormalEnemyOption)
NormalEnemyOption_OopsAll_Dropdown = SubDropdown(NormalEnemyOption_OopsAll, Enemy.GetOopsAllDropdowns())

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.TyrantMonsterIDs + IDs.SuperbossMonstersIDs, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, UniqueEnemyOption_OopsAll.GetState(), UniqueEnemyOption_OopsAll_Dropdown.GetState(), UniqueEnemyOption_Size.GetState())], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), prio=2)
UniqueEnemyOption_Spinbox = Spinbox(UniqueEnemyOption)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
UniqueEnemyOption_Normal_Spinbox = SubSpinbox(UniqueEnemyOption_Normal, default=1, description=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
UniqueEnemyOption_Unique_Spinbox = SubSpinbox(UniqueEnemyOption_Unique, default=15)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
UniqueEnemyOption_Boss_Spinbox = SubSpinbox(UniqueEnemyOption_Boss, default=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)
UniqueEnemyOption_Superboss_Spinbox = SubSpinbox(UniqueEnemyOption_Superboss, default=1)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)
UniqueEnemyOption_OopsAll = SubOption("Oops All", UniqueEnemyOption)
UniqueEnemyOption_OopsAll_Dropdown = SubDropdown(UniqueEnemyOption_OopsAll, Enemy.GetOopsAllDropdowns())

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonstersIDs, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, BossEnemyOption_OopsAll.GetState(), BossEnemyOption_OopsAll_Dropdown.GetState(), isMatchSize=True)], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), prio=2)
BossEnemyOption_Spinbox = Spinbox(BossEnemyOption)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
BossEnemyOption_Normal_Spinbox = SubSpinbox(BossEnemyOption_Normal, default=6, description=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
BossEnemyOption_Unique_Spinbox = SubSpinbox(BossEnemyOption_Unique, default=12)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
BossEnemyOption_Boss_Spinbox = SubSpinbox(BossEnemyOption_Boss, default=30)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False)
BossEnemyOption_Superboss_Spinbox = SubSpinbox(BossEnemyOption_Superboss, default=1)
BossEnemyOption_OopsAll = SubOption("Oops All", BossEnemyOption)
BossEnemyOption_OopsAll_Dropdown = SubDropdown(BossEnemyOption_OopsAll, Enemy.GetOopsAllDropdowns())

# Character
CharacterOption = Option("Party Members", Character, "Randomizes party members", [lambda: PartyMem.Members()], descData=lambda: PartyMem.PartyMemDesc(CharacterOption.name, CharacterOption_Duplicates.name))
CharacterOption_Duplicates = SubOption("Allow Duplicates", CharacterOption)
ArtsOption = Option("Arts", Character, "Randomizes various attributes of arts", descData=lambda: Art.ArtDesc(ArtsOption_LearnOrder.name, ArtsOption_Strength.name))
ArtsOption_LearnOrder = SubOption("Arts Learned", ArtsOption, [lambda: Art.ArtUnlockOrder()])
ArtsOption_Strength = SubOption("Art Strength", ArtsOption, [lambda: Art.ArtStatRando(ArtsOption_Strength_Spinbox.GetState())])
ArtsOption_Strength_Spinbox = SubSpinbox(ArtsOption_Strength, default=50, description=intensityText)
SkillOption = Option("Skill", Character, "Randomizes various attributes of skills", descData=lambda: Skill.SkillDesc(SkillOption_Strength.name))
SkillOption_LearnOrder = SubOption("Skills Learned", SkillOption, [lambda: Skill.SkillOrder()])
SkillOption_Strength = SubOption("Skill Strength", SkillOption, [lambda: Skill.SkillEnhancements(SkillOption_Strength_Spinbox.GetState())])
SkillOption_Strength_Spinbox = SubSpinbox(SkillOption_Strength, description=intensityText, default=50)
PlayerGear = Option("Ground Gear", Character, "Randomizes the stats of ground gear", descData=lambda: Gear.GearDesc(PlayerGear_Arm.name, PlayerGear_Wep.name))
PlayerGear_Arm = SubOption("Armor Stats", PlayerGear, [lambda: Gear.PlayerArmorStats(PlayerGear_Arm_Spinbox.GetState())])
PlayerGear_Arm_Spinbox = SubSpinbox(PlayerGear_Arm, min=1, default=50, description=intensityText)
PlayerGear_Wep = SubOption("Weapon Stats", PlayerGear, [lambda: Gear.PlayerWepStats(PlayerGear_Wep.GetSpinbox())])
PlayerGear_Wep_Spinbox = SubSpinbox(PlayerGear_Wep, min=1, default=50, description=intensityText)

SkellFrameOption = Option("Skell Frames", Skells, "Randomizes skell frames", [lambda: SkellFrames.RandomizeSkells()], descData=lambda: SkellFrames.SkellFrameDesc(SkellFrameOption.name))
# SkellStats = Option("Skell Stats", Skells, "Randomizes the base stats of skells", [lambda: Gear.SkellBaseStats(SkellStats.GetSpinbox())], hasSpinBox=True, spinDesc=intensityText, spinMin=1)
SkellGear = Option("Skell Gear", Skells, "Randomizes the stats of skell gear", descData=lambda: Gear.GearDesc(SkellGear_Arm.name, SkellGear_Wep.name))
SkellGear_Arm = SubOption("Armor Stats", SkellGear, [lambda: Gear.SkellArmorStats(SkellGear_Arm.GetSpinbox())])
SkellGear_Arm_Spinbox = SubSpinbox(SkellGear_Arm, 1, default=50, description=intensityText)
SkellGear_Wep = SubOption("Weapon/Art Stats", SkellGear, [lambda: Gear.SkellWepStats(SkellGear_Wep.GetSpinbox())])
SkellGear_Wep_Spinbox = SubSpinbox(SkellGear_Wep, 1, default=50, description=intensityText)
SkellFrameOption = Option("Faster Skell", Skells, "Multiples your skell's driving speed (2x recommended)", [lambda: q.SkellMovement(SkellFrameOption_Spinbox.GetState())])
SkellFrameOption_Spinbox = Spinbox(SkellFrameOption, 2, 5, 1, 2, description="x Faster")

TutorialOption = Option("Tutorial Skips", QOL, "Skips all tutorial popups", [lambda: q.TutorialSkip()])
ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_MainQuestReqs = SubOption("Skip Chapter Prerequisites", ShortcutsOption, [lambda: q.EasyStoryPrerequisites()])
# ShortcutsOption_Chapter1 = SubOption("Skip Chapter 1", ShortcutsOption, [lambda: q.Chapter1Skip()]) # Early game slog skip (introduction to blade meeting lin etc., naig asks 3 questions)
ShortcutsOption_SkellHell = SubOption("Skip Skell License Exam", ShortcutsOption, [lambda: q.SkellExamSkip()])
EarlySkellOption = Option("Early Skell", QOL, "Talk to Vandahm (Blade Barracks) to take the Skell Liscense Exam early", [lambda: q.EarlyVandahmQuest()]) 
SkellFlightOption = Option("Early Flight Module", QOL, "Flight Module is unlocked immediately after getting skells", [lambda: q.EarlyFlight()])
BoostOption = Option("Resource Boosts", QOL, "Various resource boosts (exp, cp etc.)")
BoostOption_FNav = SubOption("FrontierNav Boost", BoostOption, [lambda: q.FrontierNavBoost(BoostOption_FNav.GetSpinbox())])
BoostOption_FNav_Spinbox = SubSpinbox(BoostOption_FNav, 2,100,1,10,description="x Rewards")
BoostOption_EXP = SubOption("EXP Boost", BoostOption, [lambda: q.FasterLevels(BoostOption_EXP.GetSpinbox())])
BoostOption_EXP_Spinbox = SubSpinbox(BoostOption_EXP, 2,16,1,2,description="x Faster")
BoostOption_CP = SubOption("CP Boost", BoostOption, [lambda: q.FasterClassRanks(BoostOption_CP_Spinbox.GetState())])
BoostOption_CP_Spinbox = SubSpinbox(BoostOption_CP, 2, 16, 1, 2, description="x Faster")
YellowBubbleOption = Option("Info Range", QOL, "Increased range for collecting info bubbles", [lambda: q.InfoRangeIncrease(YellowBubbleOption.GetSpinbox(), YellowBubbleOption_Mute.GetState())])
YellowBubbleOption_Spinbox = Spinbox(YellowBubbleOption, 2, default=15, description="x Range")
YellowBubbleOption_Mute = SubOption("Mute Callouts", YellowBubbleOption)
EnemyWeatherQOLOption = Option("Weather Conditions", QOL, "Removes weather conditions from enemies", [lambda: q.ClearEnemyWeatherCondition()])
# EasyGemCraftingOption = Option("Gem Crafting", QOL, "Makes miranium the only requirement for crafting gems to avoid material grinding", [lambda: q.EasyGemCrafting()])

from scripts import Onefile
if not Onefile.isOneFile:
    OPWeapon = Option("OP Weapons", QOL, "For Testing makes starter weapons op", [lambda: q.OpWep()])


