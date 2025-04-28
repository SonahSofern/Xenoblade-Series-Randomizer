import PcArts
from scripts.Interactables import Option, SubOption
from scripts import Helper
import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Tutorials, Armor, MiscQOL, Scales, NPC, Weapons
OptionList =[]

General = 1
Character  = 2
Enemies = 3
Musica = 4
QOL = 5
Funny = 6
GameModeTab = 7

# LevelDiffOption = Option("Level Penalties", General, "Removes the harsh level penalties and bonuses from the game for more fair combat")

# General
TradeOption = Option("NPC Trades", General, "Randomizes NPC trades", [lambda: NPC.Trades()])
TradeOption_Weapon = SubOption("Weapons", TradeOption)
TradeOption_Armor = SubOption("Armor", TradeOption)
TradeOption_Gem = SubOption("Gems", TradeOption)
TradeOption_Collectibles = SubOption("Collectibles", TradeOption)
TradeOption_Materials = SubOption("Materials", TradeOption)
# Collectapedia

# Enemy
EnemyOption = Option("Enemies", Enemies, "Randomizes enemies in the overworld", [lambda: EnemiesScript.Enemies()])
EnemyOption_Normal = SubOption("Normal Monsters", EnemyOption)
EnemyOption_Unique = SubOption("Unique Monsters", EnemyOption)
EnemyOption_Boss = SubOption("Bosses", EnemyOption)
EnemyOption_Superboss = SubOption("Superbosses", EnemyOption)
EnemyOption_MixTypes = SubOption("Mix Enemy Types", EnemyOption, _defState=False)
EnemyOption_Duplicates = SubOption("Allow Duplicates", EnemyOption, _defState=False)

# Character
GemOption = Option("Gems", Character, "Randomizes the effects of Gems", [lambda: Gems.Gems()], descData=lambda: Gems.GemDescriptions())
GemOption_Power = SubOption("Power", GemOption)
GemOption_Effect = SubOption("Standard Effects", GemOption)
GemOption_Unused = SubOption("Unused Effects", GemOption)
GemOption_FreeEquip = SubOption("Freely Equip to Weapons/Armor", GemOption)
GemOption_NoCap = SubOption("Remove Gem Stat Caps", GemOption)
AffinityTreeOption = Option("Skill Trees", Character, "Randomizes all character's skill trees", [lambda: SkillTrees.SkillRando()], descData=lambda: SkillTrees.SkillTreeDesc())
AffinityTreeOption_Effect = SubOption("Skill", AffinityTreeOption)
AffinityTreeOption_Power = SubOption("Power Level", AffinityTreeOption)
AffinityTreeOption_LinkCost = SubOption("Affinity Coin Cost", AffinityTreeOption)
AffinityTreeOption_Shape = SubOption("Node Shape", AffinityTreeOption)
PlayerArtsOption = Option("Player Arts",Character, "Randomizes character's arts and their effects", [lambda: PcArts.RandomizePcArts()])
PlayerArtsOption_BalancedUnlockLevels = SubOption("Balanced Unlock Levels", PlayerArtsOption)
# PlayerArtsOption_EarlyArtsUnlock = SubOption("Unlock All Arts at Level 1", PlayerArtsOption)
PlayerArtsOption_ArtGroups = SubOption("Keep Combo Arts Together", PlayerArtsOption)
PlayerArtsOption_Summons = SubOption("Keep Melia's Summons", PlayerArtsOption)
PlayerArtsOption_GuestArts = SubOption("Include Guest Arts", PlayerArtsOption)
PlayerArtsOption_Cooldown = SubOption("Cooldown", PlayerArtsOption)
EquipmentOption = Option("Armor", Character, "Randomizes effects of Armor", [lambda: Armor.ArmorRando()])
EquipmentOption_RemoveStartingEq = SubOption("Remove Starting Equipment", EquipmentOption)
EquipmentOption_Appearance = SubOption("Appearance", EquipmentOption)
EquipmentOption_Defenses = SubOption("Defenses", EquipmentOption)
EquipmentOption_GemSlots = SubOption("Gem Slots", EquipmentOption)
EquipmentOption_WeightClass = SubOption("Weight Class", EquipmentOption)
EquipmentOption_CrazyArmors = SubOption("Crazy Armors", EquipmentOption)
WeaponOption = Option("Weapons", Character, "Randomizes effects of Weapons", [lambda: Weapons.WeaponRando()])
WeaponOption_Appearance = SubOption("Appearance", WeaponOption)
WeaponOption_Damage = SubOption("Damage", WeaponOption)
WeaponOption_Range = SubOption("Range", WeaponOption)
WeaponOption_Block = SubOption("Block", WeaponOption)
WeaponOption_Crit = SubOption("Crit", WeaponOption)
WeaponOption_Speed = SubOption("Speed", WeaponOption)
WeaponOption_Gems = SubOption("Slots", WeaponOption)


# Weapons



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

TutorialSkipsOption = Option("Tutorial Skips", QOL, "Reduces tutorials as much as possible", [lambda: Tutorials.TutorialSkips()])
FasterLvOption = Option("Fast Levels", QOL, "Decreases level up requirements by a set amount.", [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], [f'row[key] // {FasterLvOption.GetSpinbox()}'])], _hasSpinBox = True, _spinMin = 2, _spinMax = 256, _spinIncr = 2, _spinDesc = "x", spinDefault=2)
MovespeedOption = Option("Quickstep", QOL, "The gem man will gift you two free quickstep gems.", [lambda: MiscQOL.Quickstep()], _hasSpinBox=True, _spinDesc="% Speed", _spinMax=255)

# Funny
EnemyScaleOption = Option("Enemy Scale", Funny, "Randomizes a % of enemy sizes.", [lambda: Scales.EnemyScales()], _hasSpinBox=True)


# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html