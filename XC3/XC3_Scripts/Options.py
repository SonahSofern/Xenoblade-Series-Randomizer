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
}

CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])

SkillOptions = Option("Class Skills", Character, "Randomizes class skills", [lambda: Skills.SkillRando()], hasSpinBox=True)

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])
ClassLearningOption = Option("Class Aptitude", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, spinDesc = "x Faster")
MoveSpeedOption = Option("Movespeed", QOL, "Colony 4's affinity reward will be instant and a movespeed deed.", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, spinDesc = "% Speed", spinMin=1, spinMax=255, spinIncr=10)
AscendedClassOption = Option("Ascended Classes", QOL, "Classes begin the game being able to reach rank 20", []) # https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroDictionary.html set the wakeupquest to 120

# Gems
# Enemies
# Movespeed QOL
# All Item Randos (Enemy Drops, Containers, Quest Drops, Shops, Supply Drops, Collectables, Ether Cylinders?)
# Class (unlock, skills)
# Arts
# Costumes


#Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html