
import json, random, copy, traceback, math
from XCXDE.XCXDE_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

StaticEnemyData:list[Helper.RandomGroup] = []

def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSizeOption:Options.Option, isBossGroupBalancing, isMatchStats = False, finalBoss = False):
    global StaticEnemyData
    
    if StaticEnemyData == []:
        firstRun = True
    else:
        firstRun = False
    
    ignoreKeys = []
    # EnemyCounts = GetEnemyCounts()
    # GroupFightViolations = GetGroupFightViolations()
    retainNonArrangeKeys = [] #'FlyHeight', 'SwimHeight'
    with open("XCXDE/JsonOutputs/common/CHR_EnList.json", 'r+', encoding='utf-8') as eneFile:
        with open("XCXDE/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
            with open("XCXDE/JsonOutputs/common/RSC_EnList.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = Enemy.EnemyRandomizer(IDs.NormalMonsterIDs, IDs.TyrantMonsterIDs, IDs.BossMonstersIDs, IDs.SuperbossMonstersIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ParamID", "ResourceID", eneData, paramData, rscData)
    
                if firstRun:
                    StaticEnemyData = eRando.GenEnemyData(eRando.arrangeData["rows"])

                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue

                    newEn = eRando.CreateRandomEnemy(StaticEnemyData)
                    
                    # eRando.RetainNonArrangeStats(newEn, en, retainNonArrangeKeys) # Flying Enemies and some enemies in Erythia will still fall despite act type fix (After testing I found this is because of the motion file in rsc. So there is no fix unless we change every enemies motion as they are being placed)
                    
                    # ForcedArtsManager(en, newEn, eRando)
                        
                    # if isBossGroupBalancing:
                    #     eRando.BalanceFight(en, newEn, GroupFightViolations, EnemyCounts)

                    # if isMatchSize:
                    #     EnemySizeHelper(en, newEn, eRando)

                    # IntroFightBalances(en, newEn, eRando)
                    
                    # eRando.HealthBalancing(en, newEn, 'HpMaxRev')

                    Helper.CopyKeys(en, newEn, ignoreKeys)

                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()

                # if firstRun:
                #     Bandaids()
                    
                JSONParser.CloseFile(eneData, eneFile)
                JSONParser.CloseFile(paramData, paramFile)
                JSONParser.CloseFile(rscData, rscFile)
                                                                                                                                                                                                                                                                                                            