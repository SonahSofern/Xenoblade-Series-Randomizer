from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XC3.XC3_Scripts import Shortcuts, Skills, Characters, QOL as Quality
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

CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])

SkillOptions = Option("Class Skills", Character, "Randomizes class skills", [lambda: Skills.SkillRando()], hasSpinBox=True)

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])
ClassLearningOption = Option("Class Aptitude", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, _spinDesc = "x Faster")
MoveSpeedOption = Option("Movespeed", QOL, "Gives you fast movement speed", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, _spinDesc = "% Speed")

# Gems
# Enemies
# Movespeed QOL
# All Item Randos (Enemy Drops, Containers, Quest Drops, Shops, Supply Drops, Collectables, Ether Cylinders?)
# Class (unlock, skills)
# Arts
# Costumes


#Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html