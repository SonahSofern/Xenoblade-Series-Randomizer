from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XC3.XC3_Scripts import Shortcuts, Skills, Characters, QOL as Quality, Enemy
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

# CharactersOption = Option("Heroes", Character, "Randomizes heroes", [lambda: Characters.CharacterSwaps()])
EnemyOption = Option("Enemies", Enemies, "Randomizes enemies", [lambda: Enemy.Enemies()])
# NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: EnemiesScript.Enemies(IDs.NormalEnemies, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True)
# NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption)
# NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption)
# NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption)
# NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption)

# UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: EnemiesScript.Enemies(IDs.UniqueEnemies + IDs.SuperbossEnemies, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: EnemiesScript.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
# UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption)
# UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption)
# UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption)
# UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption)

# BossEnemyOption = Option("Story Bosses", Enemies, "Randomizes bosses into the chosen types", [lambda: EnemiesScript.Enemies(IDs.BossEnemies, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption), lambda: EnemiesScript.EgilArenaFix()], descData=lambda: EnemiesScript.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
# BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption)
# BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption)
# BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption)
# BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption)

SkillOptions = Option("Class Skills", Character, "Randomizes class skills", [lambda: Skills.SkillRando()], hasSpinBox=True)

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])
ClassLearningOption = Option("Class Aptitude", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, spinDesc = "x Faster")
MoveSpeedOption = Option("Movespeed", QOL, "Colony 4's affinity reward will be instant and a movespeed deed.", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, spinDesc = "% Speed", spinMin=1, spinMax=255, spinIncr=10)
AscendedClassOption = Option("Ascended Classes", QOL, "Classes begin the game being able to reach rank 20", []) # https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroDictionary.html set the wakeupquest to 120

#Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html