
from XCXDE.XCXDE_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

StaticEnemyData:list[Helper.RandomGroup] = []

# Enemy Names for map hexs should be updated with their replacement

def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSize = False):
    global StaticEnemyData
    
    if StaticEnemyData == []:
        firstRun = True
    else:
        firstRun = False
    
    # gameCondId controls if enemy spawns based on a condition so keep the original conditions
    soundEffects = "SeEnvID" # Controls the distance at which you hear the sound effects not what the SE is so if we keep it vanilla it should help with loud enemies (Zhu Pharg, )
    ignoreKeys = ["$id", "gameCondId", "ParamRev", "LvMin", "LvMax", "LvRev", "Exp" "ZoneUD", "Partner", "Flag(Named)", "Flag(mBoss)", "Flag(ignoreLv)", "Flag(Leader)", "AiLeader", "Flag(FAOff)", "BGMID", "NoEncountSkip", "SearchParamID", "MoveRange", "FieldPatternID", "ZoneID", "PopCost", 'PopProxyCost', "PopParamID", "GroupID"]
    # rscTestKeys = ['Resource', 'TypeFamily', 'TypeGenus', 'Material', 'RiseDescend', 'ProxyID', 'Radius', 'FightDistance', 'PermitHeight', 'RayCheckU', 'RayCheckD', 'SearchBaseBone', 'UndX', 'UndZ', 'UndMinX', 'UndMaxX', 'UndMinZ', 'UndMaxZ', 'UndDeg', 'ExArea', 'TurnAngle', 'FrontAngle', 'NoEncountSkip', 'VoDir', 'EffPack', 'EffCmn', 'Parts', 'PathMot', 'PathChr', 'Action', 'SePack', 'ClipEvent', 'Com_SE', 'Com_Eff', 'Com_Vo', 'Mflag(Vip)', 'Mflag(Map)', 'Mflag(Evt)', 'AttackID', 'AttackNum', 'HudName', 'HudOffset', '<044870FF>', '<7D67F533>']
    proxyIDs = ["ProxyID", "Mflag(Vip)", "Mflag(Map)", "Mflag(Evt)"] # Enemies need to keep their original proxy id and Mflags because in boss fights they dont spawn
    drawDistanceThings = ["DistanceXZ", "DistanceY", "DepopDistanceXZ", "DepopDistanceY", "ReleaseDistanceXZ", "ReleaseDistanceY", "Radius"]
    retainNonArrangeKeys = ["ReleasePcDistanceXZ", "ReleasePcDistanceXZ", "FightDistance", "PermitHeight", "RiseDescend"] + proxyIDs + drawDistanceThings #'FlyHeight', 'SwimHeight'
    
    eneFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnList.json")
    paramFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnParam.json")
    rscFile = JSONParser.File("XCXDE/JsonOutputs/common/RSC_EnList.json")
    
    eRando = Enemy.EnemyRandomizer(IDs.NormalMonsterIDs, IDs.TyrantMonsterIDs, IDs.BossMonstersIDs, IDs.SuperbossMonstersIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID",  "ParamID", eneFile.data, paramFile.data, rscFile.data)

    if firstRun:
        StaticEnemyData = eRando.GenEnemyData(eRando.arrangeData["rows"])

    for en in eneFile.rows:
        extraKeys = []
        
        if eRando.FilterEnemies(en, targetGroup):
            continue

        newEn = eRando.CreateRandomEnemy(StaticEnemyData)
        
        eRando.RetainNonArrangeStats(newEn, en, retainNonArrangeKeys) 

        if isMatchSize:
            EnemySizeHelper(en, newEn)
            extraKeys.append("ChrSize") # If you match enemy sizes the size mechanic in X should match so big enemies are still stronger

        IntroFightBalances(en, newEn, eRando)
        InvincibleEnemy(newEn)
        
        # eRando.HealthBalancing(en, newEn, 'HpMaxRev')

        Helper.CopyKeys(en, newEn, ignoreKeys + extraKeys + [soundEffects])

        HpLimitEffects(en)

    for group in StaticEnemyData:
        group.RefreshCurrentGroup()
    
    NerfSummonEnemies()
        
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
        (Megafauna, XL): 6,
        (Megafauna, Large): 7,
        (Megafauna, Medium): 9,
        (Megafauna, Small): 15,
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
    InvincibleStartupBuffIDs = [134, 138, 159, 178, 192, 235, 256]
    if newEn["StartupBuff"] in InvincibleStartupBuffIDs:
        newEn["StartupBuff"] = 0
        newEn["StartupBuffLv"] = 0
        

def IntroFightBalances(en, newEn, eRando:Enemy.EnemyRandomizer):
    introFightIDs = [348, 349, 350]
    if en["$id"] in introFightIDs:
        oldEnParam = eRando.FindParam(en)
        eRando.ChangeStats([newEn], [("HpMaxRev", oldEnParam["HpMaxRev"]), ("PowFightRev", oldEnParam["PowFightRev"]), ("PowShootRev", oldEnParam["PowShootRev"]), ("PowMindRev", oldEnParam["PowMindRev"]), ("DodgeRev", oldEnParam["DodgeRev"]), ("DexFightRev", oldEnParam["DexFightRev"]), ("DexShootRev", oldEnParam["DexShootRev"]), ("Def", oldEnParam["Def"]), ("RstPhysics", oldEnParam["RstPhysics"]), ("RstDebuffHalf", oldEnParam["RstDebuffHalf"]), ("RstDebuffFull", oldEnParam["RstDebuffFull"]) ])
                                                                                                                                                                                                                                                                                                            

def HpLimitEffects(en):
    '''Xenoblade X uses a Enhancement to stop characters from dying in phased fights, this keeps that effect on the location and removes it if not on a phased location'''
    HPLimitFightIDs = [431,441,460,470,1755,1756] # DLC seemingly didnt have any but im skeptical because there is a VITA fight that ends at 50% hp (ID 4093)
    NoKillEnhancement = 7809
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
   

# A script to handle summoned enemy levels

# After enemy randomization
# Check all enemies that have summon arts
# Create a new summon art for each
# Create a new summon enemy for each with matching level to the summoning enemy
def NerfSummonEnemies():
    # cannot find the link to perform the above concept. It is probably hard coded to each art. Instead just setting level of all summoned enemies to 1
    eneFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnList.json")
    for en in eneFile.rows:
        if en["$id"] in IDs.SummonMonsterIDs:
            # Put summons levels to 1 because there is currently no way to balance them
            en["LvMin"] = 1
            en["LvMax"] = 1 
            
            # Shrink summons in case its a small arena
            en["ScaleMin"] = en["ScaleMin"] // 3
            en["ScaleMax"] = en["ScaleMax"] // 3   
    eneFile.Close()
   
                                                                                                                                                                                                                                                                                           
def EnemyDesc(name):
    EnemyRandoDesc = PopupDescriptions.Description()
    EnemyRandoDesc.Header(name)
    EnemyRandoDesc.Text(f"{name} are the target group to be randomized.")
    EnemyRandoDesc.Text(f"The suboption for those categories are what those enemies will be randomized into.")
    EnemyRandoDesc.Text(f"The spinbox for each option is the weight of that category. The higher a weight the more likely a type of enemy will be chosen as a replacement enemy.")
    if name != Options.BossEnemyOption.name:
        # EnemyRandoDesc.Header(Options.NormalEnemyOption_Aggro.name)
        # EnemyRandoDesc.Text("This will leave enemy aggro with the original enemies. So that you can navigate areas in the originally balanced way. Otherwise you might have to fight many encounters to nagivate an area, or none in an area that you normally would.")
        EnemyRandoDesc.Header(Options.NormalEnemyOption_Size.name)
        EnemyRandoDesc.Text("This will match the size of the new enemy to the original enemy. For example, Terebra (a small enemy), when replaced with a Millesaur (a big enemy), will force the Millesaur to match the small size for that instance of it.")
    return EnemyRandoDesc