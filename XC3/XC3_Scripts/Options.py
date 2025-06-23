from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XC3.XC3_Scripts import Shortcuts, Skills
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

TestOption = Option("Empty", General, "Nothing to see yet!")

SkillOptions = Option("Class Skills", Character, "Randomizes class skills", [lambda: Skills.SkillRando()])

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])

#Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html