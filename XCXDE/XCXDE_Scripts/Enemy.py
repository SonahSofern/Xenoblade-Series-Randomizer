
import json
from XCXDE.XCXDE_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

StaticEnemyData:list[Helper.RandomGroup] = []

# Enemy Names for map hexs should be updated with their replacement

def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSize = False, isBossGroupBalancing = False, isMatchStats = False, finalBoss = False):
    global StaticEnemyData
    
    if StaticEnemyData == []:
        firstRun = True
    else:
        firstRun = False
    
    ignoreKeys = ["$id", "LvMin", "LvMax", "LvRev", "Exp" "ZoneUD", "Partner", "Flag(Named)", "Flag(mBoss)", "Flag(ignoreLv)", "Flag(Leader)", "AiLeader", "Flag(FAOff)", "BGMID", "NoEncountSkip", "SearchParamID", "MoveRange", "FieldPatternID", "ZoneID", "PopCost", 'PopProxyCost']
    # EnemyCounts = GetEnemyCounts()
    # GroupFightViolations = GetGroupFightViolations()
    rscTestKeys = ['Resource', 'TypeFamily', 'TypeGenus', 'Material', 'RiseDescend', 'ProxyID', 'Radius', 'FightDistance', 'PermitHeight', 'RayCheckU', 'RayCheckD', 'SearchBaseBone', 'UndX', 'UndZ', 'UndMinX', 'UndMaxX', 'UndMinZ', 'UndMaxZ', 'UndDeg', 'ExArea', 'TurnAngle', 'FrontAngle', 'NoEncountSkip', 'VoDir', 'EffPack', 'EffCmn', 'Parts', 'PathMot', 'PathChr', 'Action', 'SePack', 'ClipEvent', 'Com_SE', 'Com_Eff', 'Com_Vo', 'Mflag(Vip)', 'Mflag(Map)', 'Mflag(Evt)', 'AttackID', 'AttackNum', 'HudName', 'HudOffset', '<044870FF>', '<7D67F533>']
    proxyIDs = ['ProxyID'] # Enemies need to keep their original proxy id because in boss fights they dont spawn
    rscKeys = [] + proxyIDs
    retainNonArrangeKeys = ["DistanceXZ", "DistanceY", "DepopDistanceXZ", "DepopDistanceY", "ReleaseDistanceXZ", "ReleaseDistanceY", "ReleasePcDistanceXZ", "ReleasePcDistanceXZ", "FightDistance", "PemitHeight", "RiseDescend", "Radius"] #'FlyHeight', 'SwimHeight'
    
    eneFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnList.json")
    paramFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnParam.json")
    rscFile = JSONParser.File("XCXDE/JsonOutputs/common/RSC_EnList.json")
    
    eRando = Enemy.EnemyRandomizer(IDs.NormalMonsterIDs, IDs.TyrantMonsterIDs, IDs.BossMonstersIDs, IDs.SuperbossMonstersIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID",  "ParamID", eneFile.data, paramFile.data, rscFile.data)

    if firstRun:
        StaticEnemyData = eRando.GenEnemyData(eRando.arrangeData["rows"])

    for en in eneFile.rows:
        if eRando.FilterEnemies(en, targetGroup):
            continue

        newEn = eRando.CreateRandomEnemy(StaticEnemyData)
        
        eRando.RetainNonArrangeStats(newEn, en, retainNonArrangeKeys + rscKeys) 
        
        # ForcedArtsManager(en, newEn, eRando)
            
        # if isBossGroupBalancing:
        #     eRando.BalanceFight(en, newEn, GroupFightViolations, EnemyCounts)

        if isMatchSize:
            EnemySizeHelper(en, newEn)

        IntroFightBalances(en, newEn, eRando)
        InvincibleEnemy(newEn)
        
        # eRando.HealthBalancing(en, newEn, 'HpMaxRev')

        Helper.CopyKeys(en, newEn, ignoreKeys)

        HpLimitEffects(en) # Removes HPLimit values from replacement enemies and enforces it in certain locationsa

    for group in StaticEnemyData:
        group.RefreshCurrentGroup()

    # if firstRun:
    #     Bandaids()
        
    eneFile.Close()
    paramFile.Close()
    rscFile.Close()

def EnemySizeHelper(enemy, chosen):
    '''Helps match enemy size to replacement size'''
    Small = 1
    Medium = 2
    Large = 3
    XL = 4
    Megafauna = 5
    
    multDict = {
        (Megafauna, XL): 5,
        (Megafauna, Large): 6,
        (Megafauna, Medium): 8,
        (Megafauna, Small): 10,
        (XL, Large): 3,
        (XL, Medium): 4,
        (XL, Small): 5,
        (Large, Medium): 1.5,
        (Large, Small): 2,
        (Medium, Small): 1
    }
    Enemy.EnemySizeMatch(enemy, chosen, ["ScaleMin", "ScaleMax"], multDict, "ChrSize", chosen["ScaleMin"], 5, 5000)
  
def InvincibleEnemy(newEn):
    '''Some enemies have invincible auras on startup that never end. This removes them.'''
    InvincibleStartupBuffIDs = [134, 138, 159, 178, 192, 235]
    if newEn["StartupBuff"] in InvincibleStartupBuffIDs:
        newEn["StartupBuff"] = 0
        newEn["StartupBuffLv"] = 0
        

def IntroFightBalances(en, newEn, eRando:Enemy.EnemyRandomizer):
    introFightIDs = [348, 349, 350]
    if en["$id"] in introFightIDs:
        oldEnParam = eRando.FindParam(en)
        eRando.ChangeStats([newEn], [("HpMaxRev", oldEnParam["HpMaxRev"]), ("PowFightRev", oldEnParam["PowFightRev"]), ("PowShootRev", oldEnParam["PowShootRev"]), ("PowMindRev", oldEnParam["PowMindRev"]), ("DodgeRev", oldEnParam["DodgeRev"]), ("DexFightRev", oldEnParam["DexFightRev"]), ("DexShootRev", oldEnParam["DexShootRev"]), ("Def", oldEnParam["Def"]), ("RstPhysics", oldEnParam["RstPhysics"]), ("RstDebuffHalf", oldEnParam["RstDebuffHalf"]), ("RstDebuffFull", oldEnParam["RstDebuffFull"]) ])
                                                                                                                                                                                                                                                                                                            

def HpLimitEffects(en):
    HPLimitFightIDs = [431,441,460,470,1755,1756] # DLC seemingly didnt have any but im skeptical because there is a VITA fight that ends at 50% hp (ID 4093)
    NoKillEnhancement = 7809
    '''Xenoblade X uses a Enhancement to stop characters from dying in phased fights, this keeps that effect on the location and removes it if not on a phased location'''
    if en["$id"] not in HPLimitFightIDs: # Remove it from non HPLimitFights
        for i in range(1,4):
            if en[f"EnhanceID{i}"] == NoKillEnhancement: 
                en[f"EnhanceID{i}"] = 0 
    else: # Add it to limit required fights
        foundLim = False
        for i in range(1,4):
            if en[f"EnhanceID{i}"] == NoKillEnhancement:
                foundLim = True
                break
        if not foundLim:
            slot = 3
            # Find an empty slot if there is one
            for i in range(1,4):
                if en[f"EnhanceID{i}"] == 0:
                    slot = i
            en[f"EnhanceID{slot}"] = NoKillEnhancement
            
            
                                                                                                                                                                                                                                                                                           
def EnemyDesc():
    pass