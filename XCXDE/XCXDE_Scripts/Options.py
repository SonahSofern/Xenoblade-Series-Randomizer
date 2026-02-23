from scripts.Interactables import Option, SubOption
from scripts import Helper
import scripts.Interactables
from XCXDE.XCXDE_Scripts import Enemy, IDs

scripts.Interactables.Game = "XCXDE" 

General = 1
Character  = 2
Enemies = 3
Musica = 5
QOL = 4
Funny = 6

Tabs = {
    General: 'Items',
    Character: 'Characters',
    Enemies: 'Enemies',
    QOL: 'Quality of Life',
    Musica: 'Music',
    Funny: 'Funny',
}

weightsSpinDescription = "Weights ↓"

# Enemies
NormalEnemyOption = Option("Normal Monsters", Enemies, "Randomizes normal monsters into the chosen types", [lambda: Enemy.Enemies(IDs.NormalMonsterIDs, NormalEnemyOption_Normal, NormalEnemyOption_Unique, NormalEnemyOption_Boss, NormalEnemyOption_Superboss, NormalEnemyOption, NormalEnemyOption_Size.GetState(), NormalEnemyOption_Stats)], descData=lambda: Enemy.EnemyDesc(NormalEnemyOption.name), hasSpinBox = True, prio=2)
NormalEnemyOption_Normal = SubOption("Normal", NormalEnemyOption, hasSpinBox=True, spinDefault=10, spinDesc=weightsSpinDescription)
NormalEnemyOption_Unique = SubOption("Unique", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Boss = SubOption("Bosses", NormalEnemyOption, hasSpinBox=True, spinDefault=3)
NormalEnemyOption_Superboss = SubOption("Superbosses", NormalEnemyOption, hasSpinBox=True, spinDefault=1)
NormalEnemyOption_Stats = SubOption("Balance Stats", NormalEnemyOption)
NormalEnemyOption_Aggro = SubOption("Vanilla Aggro", NormalEnemyOption)
NormalEnemyOption_Size = SubOption("Match Size", NormalEnemyOption)

UniqueEnemyOption = Option("Unique Monsters", Enemies, "Randomizes unique monsters, including superbosses, into the chosen types", [lambda: Enemy.Enemies(IDs.TyrantMonsterIDs + IDs.SuperbossMonstersIDs, UniqueEnemyOption_Normal, UniqueEnemyOption_Unique, UniqueEnemyOption_Boss, UniqueEnemyOption_Superboss, UniqueEnemyOption, UniqueEnemyOption_Size.GetState(), UniqueEnemyOption_Stats)], descData=lambda: Enemy.EnemyDesc(UniqueEnemyOption.name), hasSpinBox = True, prio=2)
UniqueEnemyOption_Normal = SubOption("Normal", UniqueEnemyOption, hasSpinBox=True, spinDefault=1, spinDesc=weightsSpinDescription)
UniqueEnemyOption_Unique = SubOption("Unique", UniqueEnemyOption, hasSpinBox=True, spinDefault=10)
UniqueEnemyOption_Boss = SubOption("Bosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=5)
UniqueEnemyOption_Superboss = SubOption("Superbosses", UniqueEnemyOption, hasSpinBox=True, spinDefault=1)
UniqueEnemyOption_Stats = SubOption("Balance Stats", UniqueEnemyOption)
UniqueEnemyOption_Aggro = SubOption("Vanilla Aggro", UniqueEnemyOption)
UniqueEnemyOption_Size = SubOption("Match Size", UniqueEnemyOption)

BossEnemyOption = Option("Boss Monsters", Enemies, "Randomizes bosses into the chosen types", [lambda: Enemy.Enemies(IDs.BossMonstersIDs, BossEnemyOption_Normal, BossEnemyOption_Unique, BossEnemyOption_Boss, BossEnemyOption_Superboss, BossEnemyOption, True, True, BossEnemyOption_Stats, finalBoss=BossEnemyOption_FinalBoss.GetState())], descData=lambda: Enemy.EnemyDesc(BossEnemyOption.name), hasSpinBox = True, prio=2)
BossEnemyOption_Normal = SubOption("Normal", BossEnemyOption, hasSpinBox=True, spinDefault=2, spinDesc=weightsSpinDescription)
BossEnemyOption_Unique = SubOption("Unique", BossEnemyOption, hasSpinBox=True, spinDefault=4)
BossEnemyOption_Boss = SubOption("Bosses", BossEnemyOption, hasSpinBox=True, spinDefault=10)
BossEnemyOption_Superboss = SubOption("Superbosses", BossEnemyOption, defState=False, hasSpinBox=True, spinDefault=1)
BossEnemyOption_Stats = SubOption("Balance Stats", BossEnemyOption)
BossEnemyOption_FinalBoss = SubOption("Vanilla Final Boss", BossEnemyOption, defState=False)
BossEnemyOption_Solo = SubOption("Balance Solo Fights", BossEnemyOption)
BossEnemyOption_Group = SubOption("Balance Group Fights", BossEnemyOption)