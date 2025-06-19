from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables

scripts.Interactables.Game = "XC3" 
General = 1
Character  = 2
Enemies = 3
Musica = 5
QOL = 4

Tabs = {
    General: '🞛 Items',
    Character: '🧍 Characters',
    Enemies: '💀 Enemies',
    QOL: '🐇 Quality of Life',
    Musica: '♪ Music',
}

TestOption = Option("3 Test", General, "Randomizes the offers of NPC trades into the chosen options")
