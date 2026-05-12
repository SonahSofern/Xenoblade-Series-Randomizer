
import json, copy
from XC3.XC3_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy
from pathlib import Path

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz

StaticEnemyData:list[Helper.RandomGroup] = []
ValidEnemyPopFileNames = ["ma01a_GMK_EnemyPop.json", "ma04a_GMK_EnemyPop.json", "ma07a_GMK_EnemyPop.json", "ma09a_GMK_EnemyPop.json", "ma11a_GMK_EnemyPop.json", "ma14a_GMK_EnemyPop.json", "ma15a_GMK_EnemyPop.json", "ma17a_GMK_EnemyPop.json", "ma22a_GMK_EnemyPop.json", "ma25a_01_GMK_EnemyPop.json", "ma25a_02_GMK_EnemyPop.json", "ma25a_03_GMK_EnemyPop.json", "ma25a_04_GMK_EnemyPop.json", "ma25a_05_GMK_EnemyPop.json", "ma25a_06_GMK_EnemyPop.json", "ma25a_07_GMK_EnemyPop.json", "ma25a_08_GMK_EnemyPop.json", "ma25a_09_GMK_EnemyPop.json", "ma25a_10_GMK_EnemyPop.json", "ma25a_11_GMK_EnemyPop.json", "ma25a_12_GMK_EnemyPop.json", "ma25a_13_GMK_EnemyPop.json", "ma25a_14_GMK_EnemyPop.json", "ma25a_15_GMK_EnemyPop.json", "ma25a_16_GMK_EnemyPop.json", "ma25a_17_GMK_EnemyPop.json", "ma25a_18_GMK_EnemyPop.json", "ma25a_19_GMK_EnemyPop.json", "ma25a_50_GMK_EnemyPop.json", "ma25a_51_GMK_EnemyPop.json", "ma25a_52_GMK_EnemyPop.json", "ma25a_53_GMK_EnemyPop.json", "ma40a_GMK_EnemyPop.json", "ma44a_GMK_EnemyPop.json", "ma45a_GMK_EnemyPop.json", "ma46a_GMK_EnemyPop.json", "ma90a_GMK_EnemyPop.json", "ma90gmk_GMK_EnemyPop.json"]

def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isMatchSizeOption:Options.Option, isBossGroupBalancing):
    global StaticEnemyData
    
    if StaticEnemyData == []:
        firstRun = True
    else:
        firstRun = False
    
    foundone =['CatBGM',  '<EE7FFF6D>', '<F36BAFFD>','<0F7768D2>', '<9B3B9099>'] 
    curTesting = []
    findAggroFlags = [ '<EFCB57EC>', 'IconOffset', 'FlgMoveFloor', '<3828CCE4>', 'AlliesMsg', '<D3F77DFD>', 'FootPrintDetection', 'EffConvert', '<7C2FCBE1>', '<97002EDA>', 'VoGroup', 'NotEconomy', '<91DD0357>', 'AttenuationScale', '<C4D88A2B>', '<7D3D5DCB>', '<C313305B>', 'Score', '<4BAF120D>', '<7EFBB833>', '<277C5BBD>', '<65449302>', '<192EEE69>', '<F36D8D42>', '<76A4C736>']
    # passedTest = ['Model','ActType', 'FlyHeight', 'SwimHeight', 'Motion', 'MotRetarget','RscType', 'ChrID', 'IK', 'Sound', 'VoiceID', 'VoiceRand', 'VoiceDead', 'UniqueDirection', 'modelDirection', 'Event', '<5E3BE057>', '<28DE8575>', 'MoveBtlRate', 'CollisionRadius', '<8281BB89>', 'EffectType', '<B604D9F3>', '<3B53F852>', '<E4EB3419>', '<9693E350>', '<693A2A44>', '<6D9580C6>', 'WeaponA', 'WeaponB', 'WeaponC', 'RscPreset', 'StoryRsc', 'ChestHeight', , 'SwitchModel1', 'Visible1', 'SwitchModel2', 'Visible2', 'SwitchModel3', 'Visible3', 'SwitchModel4', 'Visible4', 'Color',  'EffStandLoop','Effect', ]
    # testNonArrangeKeys = ['Radius', 'EffScale',  'AngleFront', 'OffsetID',  '<DB52EFEF>', '<20C8E401>', 'BoneCenter', 'BoneCamera']
    testNonArrangeKeys = []
    EnemyCounts = GetEnemyCounts()
    GroupFightViolations = GetGroupFightViolations()
    Aggro = ["<AB4BA3D5>", "<1104E9C5>", "<B5C5F3B3>", "<EC666A80>", "<64251F47>", "<3B6DFBC4>"]
    specialFields = ['<B569BFB1>', '<352C263C>', '<BA57B736>'] # These fields being kept fixed a bug where cutscenes couldnt end fights and you would just sit there while the enemy kept aggroing you
    RetryBattleLandmark = "<9A220E4D>"
    PostBattleConqueredPopup = "CatMain" # Currently not using it has weird effects fights take a long time to end after enemy goes down without it happens eithery way with UMs so something is wrong with UMS
    ignoreKeys = ["$id", "ID", specialFields, PostBattleConqueredPopup, "Level", "IdMove", "NamedFlag", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "FlgFixed", "IdMove", "SpBattle", "FlgNoVanish", "FlgSpDead" , "KillEffType", "FlgSerious", RetryBattleLandmark, "<3CEBD0A4>", "<C6717CFE>", "FlgKeepSword", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"] + Aggro
    HPLimits = ["LowerLimitHP", "<60FB333A>"]
    retainNonArrangeKeys = ['FlyHeight', 'SwimHeight']
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as rscFile:
                with open("XC3/JsonOutputs/btl/BTL_Arts_En.json", 'r+', encoding='utf-8') as artFile:
                    paramData = json.load(paramFile)
                    rscData = json.load(rscFile)
                    eneData = json.load(eneFile)
                    artData = json.load(artFile)
                    
                    eRando = Enemy.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "Resource", "IdBattleEnemy", eneData, paramData, rscData, artData)
        
                    if firstRun:
                        StaticEnemyData = eRando.GenEnemyData(eRando.arrangeData["rows"])

                    for en in eneData["rows"]:
                        if eRando.FilterEnemies(en, targetGroup):
                            continue
                        
                        if FilterNPCEnemies(en["NPCName"]):
                            continue

                        newEn = eRando.CreateRandomEnemy(StaticEnemyData)
                        
                        eRando.RetainNonArrangeStats(newEn, en, retainNonArrangeKeys + HPLimits + testNonArrangeKeys + ActTypeFix(eRando, en, newEn)) # Flying Enemies and some enemies in Erythia will still fall despite act type fix (After testing I found this is because of the motion file in rsc. So there is no fix unless we change every enemies motion as they are being placed)
                        
                        ForcedArtsManager(en, newEn, eRando)
                            
                        if isBossGroupBalancing:
                            eRando.BalanceFight(en, newEn, GroupFightViolations, EnemyCounts)

                        if isMatchSizeOption:
                            EnemySizeHelper(en, newEn, eRando)

                        IntroFightBalances(en, newEn, eRando)
                        
                        eRando.HealthBalancing(en, newEn, 'StRevHp')

                        Helper.CopyKeys(en, newEn, ignoreKeys + curTesting)

                    for group in StaticEnemyData:
                        group.RefreshCurrentGroup()

                    if firstRun:
                        Bandaids()
                        
                    BreakTutorial(eRando)

                    JSONParser.CloseFile(eneData, eneFile)
                    JSONParser.CloseFile(paramData, paramFile)
                    JSONParser.CloseFile(rscData, rscFile)
                    JSONParser.CloseFile(artData, artFile)

def ActTypeFix(eRando:Enemy.EnemyRandomizer, oldEn, newEn):
    '''In XC3 its not enough to just swap act types to the old enemys spot. There are behaviors under the hood that rely on act type. For example a normally flying enemy will start soaring 50 feet above you if put as a grounded enemy. Normally flying enemy locations will just fall even if set to act type 2 and chest height fly height etc are kept. Same with some locations in the Erythia Sea. Instead we will conditionally swap act types. The behavior that lets normally swimming enemies survive on land is fixed by this method and the reverse.
    Returns the key to act type if we should keep it
    '''
    oldRSC = eRando.FindRSC(oldEn)
    newRSC = eRando.FindRSC(newEn)    
    Swim = 1
    
    if newRSC["ActType"] == Swim or oldRSC["ActType"] == Swim:
        return ["ActType"]
    
    return []
    
def MotionFix():
    '''Certain enemies will not work in new environments without motion of the old enemy. Flying enemies over cliffs will still fall and enemies deep in erythia waters will fall under the waves. This keeps the original motion.'''
    return ["Motion"]
    
def FilterNPCEnemies(enNPC):
    '''NPCs are also considered enemies in some cases so for now we will not randomize them'''
    if enNPC == "<00000000>":
        return False
    else:
        return True


def ForcedArtsManager(oldEn, newEn, eRando:Enemy.EnemyRandomizer): # Do these enemies with party wiping arts that are meant to end a scene need to be removed?
    EnemyIDsWithForcedArts = [545, 941, 885, 4431, 3782, 378, 499, 4434, 4445, 4447] # FLD_EnemyData IDs
    ForcedArtsIDs = [426, 111, 1436, 943, 1887, 1897, 1959, 1962] # Arts that the game uses to progress a cutscene/story event
    
    '''Enemies with cutscene starting arts (Ghondor for example) need the effects removed when put in a different spot'''
    if newEn["$id"] in EnemyIDsWithForcedArts:
        newPar = eRando.FindParam(newEn)
        
        # Find the forced art
        for i in range(0, 16):
            if newPar[f"ArtsSlot{i}"] in ForcedArtsIDs:
                for art in eRando.artData["rows"]:
                    if art["$id"] == newPar[f"ArtsSlot{i}"]:
                        newPar[f"ArtsSlot{i}"] = 0
                break
            
    if oldEn["$id"] in EnemyIDsWithForcedArts: # If the old enemy has a cutscene art
        oldPar = eRando.FindParam(oldEn)
        newPar = eRando.FindParam(newEn)
        
        # Find the forced art
        for i in range(0, 16):
            if oldPar[f"ArtsSlot{i}"] in ForcedArtsIDs:
                for art in eRando.artData["rows"]:
                    if art["$id"] == oldPar[f"ArtsSlot{i}"]:
                        forcedArt = copy.deepcopy(art)
                        break
                break
        
        newArt = 0
        
        # Find new enemy art
        for i in range(0,16):
            if (newPar[f"ArtsSlot{i}"] != 0):
                for art in eRando.artData["rows"]:
                    if art["$id"] == newPar[f"ArtsSlot{i}"]:
                        newArt = copy.deepcopy(art)
                        break
                break
            
        if newArt == 0: # If we found NO arts look for the statename of the autoattacks and put that on the art
            for i in range(0,3):
                if (newPar[f"AutoSlot{i}"] != 0):
                    for art in eRando.artData["rows"]:
                        if art["$id"] == newPar[f"ArtsSlot{i}"]:
                            newArt = copy.deepcopy(art)
                            break
                    break
        
        if newArt == 0: # If its still 0 we found an enemy with no arts and no autos this should be reported
            raise Exception(f"Invalid Enemy. Report this ID to our discord please! (ID: {newEn["$id"]})")
            
        # newArtID = eRando.CreateArt(newArt, [("IntervalAT", forcedArt["IntervalAT"]), ("IntervalArts", forcedArt["IntervalArts"]), ("<7A0315FE>", forcedArt["<7A0315FE>"]), ("<F9031946>", forcedArt["<F9031946>"]), ("<59CE461C>", forcedArt["<59CE461C>"]), ("AiCond1", forcedArt["AiCond1"]), ("AiRate1", forcedArt["AiRate1"]), ("AiParam1", forcedArt["AiParam1"])]) # Ensures that a valid state for that enemy is on the art or else they wont use the art
        newArtID = eRando.CreateArt(forcedArt, [("StateName", newArt["StateName"]), ("WpnType", newArt["WpnType"])]) # Ensures that a valid state for that enemy is on the art or else they wont use the art
        
        # Plug that art into the enemy in slot 15 the last slot (very few enemies use this and the fight ends at this art anyway)
        eRando.ChangeStats([newEn], [(f"ArtsSlot15", newArtID)])
        
        return False

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
    Enemy.EnemySizeMatch(oldEn, newEn, keys, multDict)

def GetEnemyCounts():
    enemyCounts = dict()
    # I don't want regular overworld enemies to be stronger/weaker because they spawn several of them in a pack, and
    # it's not consistent when they do that (standard Volffs are sometimes 1, sometimes 2, etc). I want to keep counts
    # only for bosses, UMs, quest enemies, etc
    #BossLikeEnemies = [IDs.BossMonsters, IDs.UniqueMonsters, IDs.SuperbossMonsters]

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
                    #if id in BossLikeEnemies: # Valid enemy
                    thisFightCount[id] = thisFightCount.get(id, 0) + count
                for key, val in thisFightCount.items():
                    enemyCounts[key] = val

    return enemyCounts

def GetGroupFightViolations():
    Default_Params = [
        Enemy.ParamModification(['StRevStr', 'StRevHeal']),
        Enemy.ParamModification(['StRevHp'], C=0.7)
    ]
    Default = Enemy.Violation([], [], Default_Params)

    return [Default]

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
        eRando.ChangeStats([newEn], [("StRevHp", hpChange), ("StRevStr", oldEnParam["StRevStr"]), ("StRevHeal", oldEnParam["StRevHeal"]), ("StRevDex", oldEnParam["StRevDex"]), ("StRevAgi", oldEnParam["StRevAgi"])])
    
def Bandaids():
    SummonFix()
    
def EnemyDesc(name):
    EnemyRandoDesc = PopupDescriptions.Description()
    EnemyRandoDesc.Header(name)
    EnemyRandoDesc.Text(f"{name} are the target group to be randomized.")
    EnemyRandoDesc.Text(f"The suboption for those categories are what those enemies will be randomized into.")
    EnemyRandoDesc.Text(f"The spinbox for each option is the weight of that category.")
    if name != Options.BossEnemyOption.name:
        EnemyRandoDesc.Header(Options.NormalEnemyOption_MatchSize.name)
        EnemyRandoDesc.Text("Shrinks/grows enemies to match the size of the original enemy.")
    return EnemyRandoDesc