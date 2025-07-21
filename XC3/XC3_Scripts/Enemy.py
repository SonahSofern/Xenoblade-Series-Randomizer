
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix:         
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies         
# Keves Queen is unkillable (its not the NoKill (its named slightly different) Flag on enemy)    

NormalGroup = Enemy.EnemyGroup()
UniqueGroup = Enemy.EnemyGroup()
BossGroup = Enemy.EnemyGroup()
SuperbossGroup = Enemy.EnemyGroup()
StaticEnemyData = [NormalGroup, UniqueGroup, BossGroup, SuperbossGroup]
                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies):
    global StaticEnemyData
    GroupFightViolations = GetGroupFightViolations()
    GroupFightIDs = GetGroupFightIDs()
    ignoreKeys = ["$id", "ID", "Level", "Scale", "EliteScale", "IdMove", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "FlgNoVanish", "FlgSerious", "<3CEBD0A4>", "FlgKeepSword", "FlgColonyReleased", "GetRatio", "GetEnArts", "GetEnSkill", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"]
    
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = Enemy.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "Resource", "IdBattleEnemy", eneData, paramData, rscData)
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                    Bandaids(eneData)
                    if isBoss.GetState():
                        IntroFightBalances(eRando)
                
                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue 
                    
                    newEn = eRando.GetRandomEnemy(StaticEnemyData)
                
                    eRando.ActTypeFix(newEn, en)
                    
                    if Options.BossEnemyOption_Group.GetState():
                        eRando.BalanceFight(en, newEn, GroupFightIDs, GroupFightViolations)
                        
                    eRando.BigEnemyBossFightSizeFix(en, newEn)
                    
                    eRando.CopyKeys(en, newEn, ignoreKeys)
                        
                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()
                
                JSONParser.CloseFile(eneData, eneFile)
                JSONParser.CloseFile(paramData, paramFile)
                JSONParser.CloseFile(rscData, rscFile)

def IntroFightBalances(eRando):
    pass

def Bandaids(eneData):
    pass
    
def EnemyDesc(name):
    pass