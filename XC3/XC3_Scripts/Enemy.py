
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix:         
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies         

StaticEnemyData:list[Enemy.EnemyGroup] = []

                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSizeOption:Options.Option, isBossGroupBalancing):
    global StaticEnemyData
    GroupFightViolations = GetGroupFightViolations()
    GroupFightIDs = GetGroupFightIDs()
    Aggro = ["<AB4BA3D5>", "<1104E9C5>", "<B5C5F3B3>", "<EC666A80>", "<64251F47>", "<3B6DFBC4>"]
    RetryBattleLandmark = "<9A220E4D>"
    PostBattleConqueredPopup = "CatMain" # Currently not using it has weird effects fights take a long time to end after enemy goes down without it happens eithery way with UMs so something is wrong with UMS
    ignoreKeys = ["$id", "ID", PostBattleConqueredPopup, "Level", "IdMove", "NamedFlag", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "FlgFixed", "IdMove", "FlgNoVanish", "FlgSpDead" , "KillEffType", "FlgSerious", RetryBattleLandmark, "<3CEBD0A4>", "<C6717CFE>", "FlgKeepSword", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"] + Aggro
    actKeys = ["ActType"]
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                isMatchSize = isMatchSizeOption.GetState()
                
                eRando = Enemy.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "Resource", "IdBattleEnemy", eneData, paramData, rscData, actKeys=actKeys)
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                
                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue 
                        
                    newEn = eRando.CreateRandomEnemy(StaticEnemyData)
                
                    eRando.ActTypeFix(newEn, en) # Flying Enemies and some enemies in Erythia will still fall despite act type fix
                    
                    HPLimitFix(en, newEn, eRando)
                    
                    # if isBossGroupBalancing:
                    #     eRando.BalanceFight(en, newEn, GroupFightIDs, GroupFightViolations)
                        
                    if isMatchSize:
                        EnemySizeHelper(en, newEn, eRando)
                        
                    IntroFightBalances(en, newEn, eRando)
                    
                    Helper.CopyKeys(en, newEn, ignoreKeys)
                        
                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()
                
                if StaticEnemyData == []:
                    Bandaids(eRando)
                
                JSONParser.CloseFile(eneData, eneFile)
                JSONParser.CloseFile(paramData, paramFile)
                JSONParser.CloseFile(rscData, rscFile)

def HPLimitFix(en, newEn, eRando:Enemy.EnemyRandomizer):
    oldRSC = eRando.FindParam(en)
    newRSC = eRando.FindParam(newEn)
    
    if oldRSC["LowerLimitHP"] != newRSC["LowerLimitHP"]:  
        eRando.ChangeStats([newEn], [("LowerLimitHP", oldRSC["LowerLimitHP"])])


def SummonFix(): # For now this is lower priority for how difficult it would be to fix so im removing summons
    with open("XC3/JsonOutputs/btl/BTL_EnSummon.json", 'r+', encoding='utf-8') as summonFile:
        summonData = json.load(summonFile)
        for summon in summonData["rows"]:
            for i in range(1,4):
                summon[f"EnemyID0{i}"] = 0
        JSONParser.CloseFile(summonData, summonFile)
    

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

def GetGroupFightViolations():
    return []

def GetGroupFightIDs():
    return []

def BreakTutorial(eRando:Enemy.EnemyRandomizer): # Tutorial that requires an enemy to be break, topple, dazed
    breakTutorial = [738]
    eRando.ChangeStats(breakTutorial, [("RstBreak", 0)])

def IntroFightBalances(en, newEn, eRando:Enemy.EnemyRandomizer):
    introTutorial = [449, 450, 451, 452, 453, 454, 455]
    bossIntroFights = [456, 457]
    returningToColony =  [737 ,739]
    breakTutorial = [738]
    Piranhax = [588]
    DrifterRopl = [458]
    StealthShip = [460,461,462]
    Sentry = [463]
    AgnusTrio = [464,465,466]
    MysteriousEnemy = [467]
    cantLoseFights = introTutorial + bossIntroFights + returningToColony
    introFights = breakTutorial + Piranhax + DrifterRopl + Sentry + StealthShip + AgnusTrio + MysteriousEnemy + cantLoseFights

    if en["$id"] in introFights:
        oldEnParam = eRando.FindParam(en)
        if en["$id"] in cantLoseFights:
            hpChange = 5
        else:
            hpChange = oldEnParam["StRevHp"]
        eRando.ChangeStats([newEn], [("StRevHp", hpChange),("StRevStr", oldEnParam["StRevStr"]),("StRevHeal", oldEnParam["StRevHeal"]),("StRevDex", oldEnParam["StRevDex"]),("StRevAgi", oldEnParam["StRevAgi"])])
    
def Bandaids(eRando):
    BreakTutorial(eRando)
    SummonFix()
    
def EnemyDesc(name):
    desc = PopupDescriptions.Description()
    desc.Header("Enemies")
    desc.Text("This randomizes enemies in the world from the target category into the chosen ones.")
    desc.Header(Options.BossEnemyOption_MatchSize.name)
    desc.Text("Shrinks/grows enemies to match the size of the original enemy.")
    return desc