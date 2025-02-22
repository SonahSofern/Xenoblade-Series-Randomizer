import PcArts
from scripts.Interactables import Option, SubOption
import PcArts
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
