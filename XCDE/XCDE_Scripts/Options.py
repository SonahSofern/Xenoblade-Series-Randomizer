import PcArts
from scripts.Interactables import Option, SubOption
import PcArts, Music
OptionList =[]

General = 1
Character  = 2
Enemies = 3
Misce = 4
QOL = 5
Funny = 6
CosmeticsTab = 7
GameModeTab = 8

PlayerArtsOption = Option("Player Arts",Character, "Randomizes the effects of your arts", [lambda: PcArts.RandomizePcArts()])
PlayerArtsOption_Cooldown = SubOption("Cooldown", PlayerArtsOption)
PlayerArtsOption_EarlyArtsUnlock = SubOption("Unlock All Arts at Level 1", PlayerArtsOption)
BattleMusicOption = Option("Battle Music", Misce, "Randomizes battle themes among themselves", [lambda: Music.MusicRando(Music.AllBattleThemes)]) #https://xenobladedata.github.io/xb1de/bdat/bdat_common/bgmlist.html
for song in Music.AllBattleThemes:
    song.CreateOption(BattleMusicOption)
BossMusicOption = Option("Boss Music", Misce, "Randomizes boss themes among themselves", [lambda: Music.MusicRando(Music.AllBossThemes)])
for song in Music.AllBossThemes:
    song.CreateOption(BossMusicOption)
EnvironmentCutsceneMusicOption = Option("Environment/Cutscene Music", Misce, "Randomizes environment themes among themselves", [lambda: Music.MusicRando(Music.AllEnvironmentThemes)])
for song in Music.AllEnvironmentThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption)
for song in Music.AllCutsceneThemes:
    song.CreateOption(EnvironmentCutsceneMusicOption)
JingleMusicOption = Option("Jingles", Misce, "Randomizes jingles among themselves", [lambda: Music.MusicRando(Music.AllJingles)])
for song in Music.AllJingles:
    song.CreateOption(JingleMusicOption)
    # SubOption(song.songName, EnvironmentCutsceneMusicOption, [lambda: Music.UsedEnvironmentThemes.append(self)])


# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html