
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy
from pathlib import Path

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix:         
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies         
# Keves Queen is unkillable (its not the NoKill (its named slightly different) Flag on enemy)    

StaticEnemyData:list[Enemy.EnemyGroup] = []

ValidEnemyPopFileNames = ["ma01a_GMK_EnemyPop.json", "ma04a_GMK_EnemyPop.json", "ma07a_GMK_EnemyPop.json", "ma09a_GMK_EnemyPop.json", "ma11a_GMK_EnemyPop.json", "ma14a_GMK_EnemyPop.json", "ma15a_GMK_EnemyPop.json", "ma17a_GMK_EnemyPop.json", "ma22a_GMK_EnemyPop.json", "ma25a_01_GMK_EnemyPop.json", "ma25a_02_GMK_EnemyPop.json", "ma25a_03_GMK_EnemyPop.json", "ma25a_04_GMK_EnemyPop.json", "ma25a_05_GMK_EnemyPop.json", "ma25a_06_GMK_EnemyPop.json", "ma25a_07_GMK_EnemyPop.json", "ma25a_08_GMK_EnemyPop.json", "ma25a_09_GMK_EnemyPop.json", "ma25a_10_GMK_EnemyPop.json", "ma25a_11_GMK_EnemyPop.json", "ma25a_12_GMK_EnemyPop.json", "ma25a_13_GMK_EnemyPop.json", "ma25a_14_GMK_EnemyPop.json", "ma25a_15_GMK_EnemyPop.json", "ma25a_16_GMK_EnemyPop.json", "ma25a_17_GMK_EnemyPop.json", "ma25a_18_GMK_EnemyPop.json", "ma25a_19_GMK_EnemyPop.json", "ma25a_50_GMK_EnemyPop.json", "ma25a_51_GMK_EnemyPop.json", "ma25a_52_GMK_EnemyPop.json", "ma25a_53_GMK_EnemyPop.json", "ma40a_GMK_EnemyPop.json", "ma44a_GMK_EnemyPop.json", "ma45a_GMK_EnemyPop.json", "ma46a_GMK_EnemyPop.json", "ma90a_GMK_EnemyPop.json", "ma90gmk_GMK_EnemyPop.json"]

def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSizeOption:Options.Option, isBossGroupBalancing):
    global StaticEnemyData
    EnemyCounts = GetEnemyCounts()
    GroupFightViolations = GetGroupFightViolations()
    Aggro = ["<AB4BA3D5>", "<1104E9C5>", "<B5C5F3B3>", "<EC666A80>", "<64251F47>", "<3B6DFBC4>"]
    RetryBattleLandmark = "<9A220E4D>"
    PostBattleConqueredPopup = "CatMain" # Currently not using it has weird effects fights take a long time to end after enemy goes down without it happens eithery way with UMs so something is wrong with UMS
    ignoreKeys = ["$id", "ID", PostBattleConqueredPopup,  "Level", "IdMove", "NamedFlag", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "IdMove", "FlgNoVanish", "FlgSerious", RetryBattleLandmark, "<3CEBD0A4>", "<C6717CFE>", "FlgKeepSword", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"] + Aggro
    actKeys = ["ActType", "FlyHeight", "SwimHeight"]
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as rscFile:
                with open("XC3/JsonOutputs/btl/BTL_Arts_En.json", 'r+', encoding='utf-8') as artFile:
                    paramData = json.load(paramFile)
                    rscData = json.load(rscFile)
                    eneData = json.load(eneFile)
                    artData = json.load(artFile)
                    isMatchSize = isMatchSizeOption.GetState()

                    eRando = Enemy.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "Resource", "IdBattleEnemy", eneData, paramData, rscData, artData, actKeys=actKeys)

                    if StaticEnemyData == []:
                        StaticEnemyData = eRando.GenEnemyData()

                    for en in eneData["rows"]:
                        if eRando.FilterEnemies(en, targetGroup):
                            continue

                        newEn = eRando.CreateRandomEnemy(StaticEnemyData)

                        eRando.ActTypeFix(newEn, en) # Flying Enemies and some enemies in Erythia will still fall despite act type fix

                        HPLimitFix(en, newEn)

                        if isBossGroupBalancing:
                            eRando.BalanceFight(en, newEn, GroupFightViolations, EnemyCounts)

                        if isMatchSizeOption.GetState():
                            EnemySizeHelper(en, newEn, eRando)

                        Helper.CopyKeys(en, newEn, ignoreKeys)

                    for group in StaticEnemyData:
                        group.RefreshCurrentGroup()

                    Bandaids(eRando)

                    JSONParser.CloseFile(eneData, eneFile)
                    JSONParser.CloseFile(paramData, paramFile)
                    JSONParser.CloseFile(rscData, rscFile)

def HPLimitFix(en, newEn):
    # New enemy takes old enemy hp limit
    pass

def EnemySizeHelper(oldEn, newEn, eRando:Enemy.EnemyRandomizer):
    Massive = 3
    Large = 2
    Normal = 1
    Small = 0
    
    multDict = {
        (Massive, Large): 3,
        (Massive, Normal): 4,
        (Massive, Small): 5,
        (Large, Normal): 3,
        (Large, Small): 4,
        (Normal, Small): 1,
    }
    keys = ["Scale", "EliteScale", "WeaponScale"]
    eRando.EnemySizeMatch(oldEn, newEn, keys, multDict)

def GetEnemyCounts():
    enemyCounts = dict()
    # I don't want regular overworld enemies to be stronger/weaker because they spawn several of them in a pack, and
    # it's not consistent when they do that (standard Volffs are sometimes 1, sometimes 2, etc). I want to keep counts
    # only for bosses, UMs, quest enemies, etc
    BossLikeEnemies = [IDs.BossMonsters, IDs.UniqueMonsters, IDs.SuperbossMonsters]

    basePath = Path("XC3/JsonOutputs")

    for name in ValidEnemyPopFileNames:
        # Try the base game folder first
        filePath = basePath / "map" / name

        # Not there...try the dlc folder
        if not filePath.exists():
            filePath = basePath / "dlc" / name

        # Not there either... try the zzz folder
        if not filePath.exists():
            filePath = basePath / "zzz" / name

        with filePath.open('r+', encoding='utf-8') as popFile:
            popData = json.load(popFile)
            for row in popData["rows"]:
                # Enemies may appear as more than one enemy in the same fight. For example, the Tirkins in XC2 chapter 4
                # are separated as two groups of 3 and 1, despite being the exact same enemy
                # To account for this, we sum all the instances before adding it to the overall counter
                # I am unsure if this is also a problem in XC3, but I don't feel like reading all the pop files to check
                thisFightCount = dict()
                for i in Helper.InclRange(1,6):
                    id = row[f"EnemyID{i}"]
                    count = row[f"PopCount{i}"]
                    if id in BossLikeEnemies: # Valid enemy
                        thisFightCount[id] = thisFightCount.get(id, 0) + count
                for key, val in thisFightCount.items():
                    enemyCounts[key] = val

    return enemyCounts

def GetGroupFightViolations():
    Default_Params = [
        Enemy.ParamModification(['StRevStr', 'StRevHeal']),
        Enemy.ParamModification(['StRevHP'], C=0.7)
    ]
    Default = Enemy.Violation([], [], Default_Params)

    return [Default]

def IntroFightBalances(eRando:Enemy.EnemyRandomizer):
    introFights = [449, 450, 451, 452, 453, 454, 455]
    bossIntroFights = [456, 457]
    eRando.ChangeStats(introFights, [("StRevHp", 5)])
    eRando.ChangeStats(bossIntroFights, [("StRevHp", 20)])

def Bandaids(eRando):
    IntroFightBalances(eRando)
    
def EnemyDesc(name):
    desc = PopupDescriptions.Description()
    desc.Header("Enemies")
    desc.Text("This randomizes enemies in the world from the target category into the chosen ones.")
    desc.Header(Options.BossEnemyOption_MatchSize.name)
    desc.Text("Shrinks/grows enemies to match the size of the original enemy.")
    return desc