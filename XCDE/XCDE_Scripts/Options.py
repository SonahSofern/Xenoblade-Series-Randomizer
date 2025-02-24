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

MusicOption = Option("Randomizes Music", Misce, "Randomizes what music plays where", [lambda: Music.MusicRando()]) #https://xenobladedata.github.io/xb1de/bdat/bdat_common/bgmlist.html
MusicOption_RemoveVision = SubOption("Remove Vision Music", MusicOption)
MusicOption_RemoveLowTension = SubOption("Remove Low Tension Music", MusicOption)

# ShopOption = Option() #https://xenobladedata.github.io/xb1de/bdat/bdat_common/shoplist.html