import PcArts
from scripts.Interactables import Option, SubOption
from scripts import Helper
import PcArts, Music, AffinityTrees, Gems, Enemies as EnemiesScript
OptionList =[]

General = 1
Character  = 2
Enemies = 3
Misce = 4
QOL = 5
Funny = 6
CosmeticsTab = 7
GameModeTab = 8

# LevelDiffOption = Option("Level Penalties", General, "Removes the harsh level penalties and bonuses from the game for more fair combat")

EnemyOption = Option("Enemies", Enemies, "Randomizes enemy in the overworld", [lambda: EnemiesScript.Enemies()])

GemOption = Option("Gems", Character, "Randomizes the effects of Gems", [lambda: Gems.Gems()])
GemOption_NoCap = SubOption("Remove Cap", GemOption)
GemOption_FreeEquip = SubOption("Freely Equip to Weapons and Armor", GemOption)
AffinityTreeOption = Option("Affinity Skill Trees", Character, "Randomizes your skill trees", [lambda: AffinityTrees.SkillRando()])
AffinityTreeOption_Shape = SubOption("Node Shape", AffinityTreeOption)
AffinityTreeOption_Power = SubOption("Power", AffinityTreeOption)
AffinityTreeOption_LinkCost = SubOption("Link Cost", AffinityTreeOption)
PlayerArtsOption = Option("Player Arts",Character, "Randomizes the effects of your arts", [lambda: PcArts.RandomizePcArts()])
PlayerArtsOption_Cooldown = SubOption("Cooldown", PlayerArtsOption)
PlayerArtsOption_EarlyArtsUnlock = SubOption("Unlock All Arts at Level 1", PlayerArtsOption)
PlayerArtsOption_Summons = SubOption("Keep Melia's Summons", PlayerArtsOption)
PlayerArtsOption_ArtGroups = SubOption("Keep Combo Arts Together", PlayerArtsOption)
PlayerArtsOption_GuestArts = SubOption("Include Guest Arts", PlayerArtsOption)
PlayerArtsOption_KeepUnlockLevels = SubOption("Balanced Unlock Levels", PlayerArtsOption, [lambda: PcArts.BalanceArtUnlockLevels()])
BattleMusicOption = Option("Battle Music", Misce, "Randomizes battle themes among themselves", [lambda: Music.MusicRando(Music.AllBattleThemes, Music.UsedBattleThemes)]) #https://xenobladedata.github.io/xb1de/bdat/bdat_common/bgmlist.html
for song in Music.AllBattleThemes:
    song.CreateOption(BattleMusicOption, Music.UsedBattleThemes)
BossMusicOption = Option("Boss Music", Misce, "Randomizes boss themes among themselves", [lambda: Music.MusicRando(Music.AllBossThemes, Music.UsedBossThemes)])
for song in Music.AllBossThemes:
    song.CreateOption(BossMusicOption, Music.UsedBossThemes)
EnvironmentCutsceneMusicOption = Option("Environment/Cutscene Music", Misce, "Randomizes environment/cutscene themes among themselves", [lambda: Music.MusicRando(Music.AllEnvironmentThemes + Music.AllCutsceneThemes, Music.UsedEnvironmentThemes + Music.UsedCutsceneThemes)])
for song in Music.AllEnvironmentThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedEnvironmentThemes)
for song in Music.AllCutsceneThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption, Music.UsedCutsceneThemes)
JingleMusicOption = Option("Jingles", Misce, "Randomizes jingles among themselves", [lambda: Music.MusicRando(Music.AllJingles, Music.UsedJingles)])
for song in Music.AllJingles:
    song.CreateOption(JingleMusicOption, Music.UsedJingles)


# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html