import PcArts
from scripts.Interactables import Option, SubOption
from scripts import Helper
import PcArts, Music, SkillTrees, Gems, Enemies as EnemiesScript, Tutorials, Armor
OptionList =[]

General = 1
Character  = 2
Enemies = 3
Misce = 4
QOL = 5
Funny = 6
GameModeTab = 7

# LevelDiffOption = Option("Level Penalties", General, "Removes the harsh level penalties and bonuses from the game for more fair combat")

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

# EquipmentOption_Appearance = SubOption("Appearance", EquipmentOption)
# EquipmentOption_UniqueGems = SubOption("Gems", EquipmentOption)
# EquipmentOption_Slots = SubOption("Slots", EquipmentOption)


# Misc
BattleMusicOption = Option("Battle Music", Misce, "Randomizes the chosen battle themes onto all battle themes", [lambda: Music.MusicRando(Music.AllBattleThemes, Music.UsedBattleThemes)]) #https://xenobladedata.github.io/xb1de/bdat/bdat_common/bgmlist.html
for song in Music.AllBattleThemes:
    song.CreateOption(BattleMusicOption, Music.UsedBattleThemes)
BossMusicOption = Option("Boss Music", Misce, "Randomizes the chosen boss themes onto all boss themes", [lambda: Music.MusicRando(Music.AllBossThemes, Music.UsedBossThemes)])
for song in Music.AllBossThemes:
    song.CreateOption(BossMusicOption, Music.UsedBossThemes)
EnvironmentCutsceneMusicOption = Option("Environment/Cutscene Music", Misce, "Randomizes the chosen environment/cutscene themes onto all environment themes", [lambda: Music.MusicRando(Music.AllEnvironmentThemes + Music.AllCutsceneThemes, Music.UsedEnvironmentThemes + Music.UsedCutsceneThemes)])
for song in Music.AllEnvironmentThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedEnvironmentThemes)
for song in Music.AllCutsceneThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedCutsceneThemes)
JingleMusicOption = Option("Jingles", Misce, "Randomizes the chosen jingles onto all jingles", [lambda: Music.MusicRando(Music.AllJingles, Music.UsedJingles)])
for song in Music.AllJingles:
    song.CreateOption(JingleMusicOption, Music.UsedJingles)

TutorialSkipsOption = Option("Tutorial Skips", QOL, "Reduces tutorials as much as possible", [lambda: Tutorials.TutorialSkips()])
FasterLvOption = Option("Fast Levels", QOL, "Decreases level up requirements by a set amount.")
FasterLvOption_2 = SubOption("2x", FasterLvOption, [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], ['row[key] // 2'])])
FasterLvOption_4 = SubOption("4x", FasterLvOption, [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], ['row[key] // 4'])], _defState = False)
FasterLvOption_8 = SubOption("8x", FasterLvOption, [lambda: Helper.MathmaticalColumnAdjust(["./XCDE/_internal/JsonOutputs/bdat_common/BTL_growlist.json"], ["level_exp"], ['row[key] // 8'])], _defState = False)


# Funny

# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html

# Character models rando https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_Stream_full_dr.html