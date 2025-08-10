from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XC3.XC3_Scripts import Shortcuts, Skills, Heroes, QOL as Quality, Enemy , IDs, Enhancements, Accessories, Gems
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
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsters, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption)], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.UniqueMonsters + IDs.SuperbossMonsters, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True)

BossEnemyOption = Option("Story Bosses", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonsters, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption)], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, hasSpinBox=True)
BossEnemyOption_GroupFights = SubOption("Balance Group Fights", BossEnemyOption)

AccessoriesOption = Option("Accessories", Character, "Randomizes the effects of Accessories", [lambda: Accessories.AccessoryRando()])
GemsOption = Option("Gems", Character, "Randomizes the effects of gems.", [lambda: Gems.GemRando()])
SkillOptions = Option("Class Skills", Character, "Randomizes class skills", [lambda: Skills.SkillRando()], hasSpinBox=True)
SkillOptions_Vanilla = SubOption("Vanilla Skills", SkillOptions)
SkillOptions_Unused = SubOption("Unused Skills", SkillOptions)
PlayerArtsOption = Option("Arts", Character) # Probably only want to add extra effects not create entirely new arts like 2 and alter already exisiting effects strengths
HerosOption = Option("Heroes", Character, "Randomizes what heroes appear in the world", [lambda: Heroes.HeroSwaps()])

ShortcutsOption = Option("Shortcuts", QOL, "Speeds up various parts of the main quest")
ShortcutsOption_Tutorials = SubOption("Tutorial Skip", ShortcutsOption, [lambda: Shortcuts.TutorialSkips()])
ClassLearningOption = Option("Class Aptitude", QOL, "Increases the rate at which your characters learn classes", [lambda: Quality.ClassAptitude()], hasSpinBox=True, spinDesc = "x Faster")
MoveSpeedOption = Option("Movespeed", QOL, "Colony 4's affinity reward will be instant and a movespeed deed.", [lambda: Quality.EarlyMoveSpeed()], hasSpinBox=True, spinDesc = "% Speed", spinMin=1, spinMax=255, spinIncr=10)
# AscendedClassOption = Option("Ascended Classes", QOL, "Classes begin the game being able to reach rank 20 (DOESNT WORK)", [lambda: Quality.AscendedClassEarly()]) # https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroDictionary.html set the wakeupquest to 120

#Roguelike enemy files https://xenobladedata.github.io/xb3_200_dlc4/BTL_ChSU_EnemyTable.html