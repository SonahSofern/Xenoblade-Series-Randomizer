
import json, random, copy, traceback, math
from XCXDE.XCXDE_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

StaticEnemyData:list[Enemy.EnemyGroup] = []

                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies):
    global StaticEnemyData
    ignoreKeys = ["$id", "ID", "Level", "Scale", "EliteScale", "IdMove", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "FlgNoVanish", "FlgSerious", "<3CEBD0A4>", "FlgKeepSword", "FlgColonyReleased", "GetRatio", "GetEnArts", "GetEnSkill", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"]
    
    with open("XCXDE/JsonOutputs/common/CHR_EnList.json", 'r+', encoding='utf-8') as eneFile:
        with open("XCXDE/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
            with open("XCXDE/JsonOutputs/common/RSC_EnList.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = Enemy.EnemyRandomizer(IDs.NormalMonsterIDs, IDs.TyrantMonsterIDs, IDs.BossMonstersIDs, IDs.SuperbossMonstersIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID", "ParamID", eneData, paramData, rscData, "Dm")
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                    Bandaids(eneData)
                    if isBoss.GetState():
                        IntroFightBalances(eRando)
                
                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue 
                    
                    newEn = eRando.GetRandomEnemy(StaticEnemyData)
                
                    # eRando.ActTypeFix(newEn, en)
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