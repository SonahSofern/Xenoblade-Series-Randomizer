from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables

scripts.Interactables.Game = "XCXDE" 

General = 1
Character  = 2
Enemies = 3
Musica = 5
QOL = 4
Funny = 6

Tabs = {
    General: '🞛 Items',
    Character: '🧍 Characters',
    Enemies: '💀 Enemies',
    QOL: '🐇 Quality of Life',
    Musica: '♪ Music',
    Funny: '😄 Funny',
}
TestOption = Option("X Test", General, "Randomizes the offers of NPC trades into the chosen options")
