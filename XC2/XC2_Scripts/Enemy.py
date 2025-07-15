import json, random, copy, traceback, math
from XC2.XC2_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions

class EnemyGroup():
    def __init__(self):
        self.originalGroup = []
        self.currentGroup = []
        
    def isEmpty(self):
        if self.originalGroup == []:
            return True
        else:
            return False
    
    def RefreshCurrentGroup(self):
        self.currentGroup = copy.deepcopy(self.originalGroup)

NormalGroup = EnemyGroup()
UniqueGroup = EnemyGroup()
BossGroup = EnemyGroup()
SuperbossGroup = EnemyGroup()
StaticEnemyData = [NormalGroup, UniqueGroup, BossGroup, SuperbossGroup]
                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies):
    with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        
        GenEnemyData(eneData)
        
        RandomAssignment(eneData, targetGroup, GenWeights(isNormal, isUnique, isBoss, isSuperboss), isEnemies)

        Bandaids()
        
        JSONParser.CloseFile(eneData, eneFile)

def RandomAssignment(eneData, targetGroup, weights, isEnemies):
    keysList = ['ParamID', 'EnemyBladeID', 'BladeID', 'BladeAtr', 'ExtraParts', 'Name', 'Debug_Name', 'HpOver', 'ExpRev', 'GoldRev', 'WPRev', 'SPRev', 'DropTableID', 'DropTableID2', 'DropTableID3', 'Scale', 'ChrSize', 'TurnSize', 'CamSize', 'LinkRadius', 'BatInterval', 'BatArea', 'EN_WATER_DEAD_NONE', 'BatAreaType', 'DrawWait', 'AiGroup', 'AiGroupNum', 'BookID', 'EnhanceID1', 'EnhanceID2', 'EnhanceID3', 'ParamRev', 'RstDebuffRev', 'HealPotTypeRev', 'SummonID', 'BGMID', 'SeEnvID', 'Race', 'LvMin', 'LvMax', 'ScaleMin', 'ScaleMax']
    # Randomly Assign
    for en in eneData["rows"]:
        if not (en["$id"] in targetGroup):
            continue
        if not Helper.OddsCheck(isEnemies.GetSpinbox()):
            continue
        if isBadEnemy(en):
            continue
     
        enemyGroup = random.choices(StaticEnemyData, weights)[0]
        newEn = random.choice(enemyGroup.currentGroup)
        
        enemyGroup.currentGroup.remove(newEn) # If group is empty
        if enemyGroup.currentGroup == []:
            enemyGroup.RefreshCurrentGroup()
            
        for key in keysList:
            en[key] = newEn[key]
 
def isBadEnemy(en):
    if en["$id"] not in (IDs.NormalMonsters + IDs.BossMonsters + IDs.UniqueMonsters + IDs.SuperbossMonsters + SummonedEnemies):
        return True

def GenEnemyData(eneData):
    '''Creates the data in a nested list if it does not already exist, this is only to be copied from never altered'''
    if NormalGroup.isEmpty():
        
        for en in eneData["rows"]:
            if isBadEnemy(en):
                continue
            enID = en["$id"]
            if enID in IDs.NormalMonsters:
                group = NormalGroup
            elif enID in IDs.UniqueMonsters:
                group = UniqueGroup
            elif enID in IDs.BossMonsters:
                group = BossGroup
            elif enID in IDs.SuperbossMonsters:
                group = SuperbossGroup
            
            group.currentGroup.append(en.copy())
            group.originalGroup.append(en.copy())

def GenWeights(isNormal, isUnique, isBoss, isSuperboss):
    weights = [0,0,0,0]
    if isNormal.GetState():
        weights[0] = isNormal.GetSpinbox()
    if isUnique.GetState():
        weights[1] = isUnique.GetSpinbox()
    if isBoss.GetState():
        weights[2] = isBoss.GetSpinbox()
    if isSuperboss.GetState():
        weights[3] = isSuperboss.GetSpinbox()
    return weights

def ForcedWinFights(fights = []):
    filename = "XC2/JsonOutputs/common/FLD_QuestBattle.json"
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in fights: #battle on gramps at start of game
                row["ReducePCHP"] = 1
        JSONParser.CloseFile(data, file)


def AeshmaCoreHPNerf(): #this fight sucks
    with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 318:
                row["HpMaxRev"] = 1500 # nerfed hp by 5/6ths
        JSONParser.CloseFile(data, file)
  

def BigEnemyCollisionFix(): # Fixes ophion/other large enemies going outside the spawn circle and flying out of range in a boss fight. no longer used
    with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as file: 
        BigEnemies = [64,65,70,154,245,249,252]
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in BigEnemies:
                row["CharColli"] = 0 #removes enemy collision
                row["EnRadius"] = 255 #sets radius you can hit them
                row["EnRadius2"] = 255 # sets radius they can hit you
        JSONParser.CloseFile(data, file)


def GortOgreUppercutRemoval(): # Gort 2's Ogre Uppercut seems to be buggy, reported to crash game in certain situations, so it's being removed for the time being.
    with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1434:
                row["ArtsNum4"] = 963 # replaced Ogre Uppercut with a second instance of Ogre Flame
        JSONParser.CloseFile(data, file)

def EarthBreathNerf(): # Cressidus's Earth Breath is pretty strong if the enemy happens to show up early. Nerfed by 3/4ths.
    with open("XC2/JsonOutputs/common/BTL_Arts_Bl.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 218:
                row["DmgMgn1"] = 500
                row["DmgMgn2"] = 500
                row["DmgMgn3"] = 500
                row["DmgMgn4"] = 500
                row["DmgMgn5"] = 500
                row["DmgMgn6"] = 500
        JSONParser.CloseFile(data, file)

def Bandaids():
    ForcedWinFights([3,6])
    AeshmaCoreHPNerf()
    BigEnemyCollisionFix()
    GortOgreUppercutRemoval()
    EarthBreathNerf()
    TornaWave1FightChanges()
    FishFix()
    FlyingFix()
    SummonsFix()
    # Is enemydupebosscondition still a problem need to test

def FishFix():
    pass

def FlyingFix():
    pass
# Going to not randomize these summonsed enemies and set their level to whatever the original summoners level is now
SummonedEnemies = [1, 6, 1568, 1569, 1593, 1599, 66, 67, 1641, 122, 135, 150, 152, 154, 1700, 1724, 1725, 1726, 1727, 1731, 724, 725, 726, 727, 728, 242, 1371, 1881, 1787, 1788, 1789, 1285, 1805, 1806, 1807, 1304, 1308, 1347, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 846, 1362, 1364, 1365, 1363, 1367, 1368, 1369, 1370, 1883, 1372, 1885, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1384, 1385, 1383, 1420, 1521, 1533]
def SummonsFix():
    with open("XC2/JsonOutputs/common/BTL_Summon.json", 'r+', encoding='utf-8') as summonFile:
        with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
            with open(f"XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as enParamFile:
                with open(f"XC2/JsonOutputs/common/BTL_Arts_En.json", 'r+', encoding='utf-8') as artFile:
                    summonData = json.load(summonFile)
                    eneData = json.load(eneFile)
                    artData = json.load(artFile)
                    enParamData = json.load(enParamFile)
                    testlist = []
                    for sum in summonData["rows"]:
                        for sumGroup in sum["EnemyID"]:
                            if sumGroup != 0:
                                testlist.append(sumGroup)
                    print(list(set(testlist)))
                    
                    # for art in artData["rows"]:
                    #     if art["Summon"] != 0:
                    #         for en in 
                            
                            
                    # JSONParser.CloseFile()
            

  
def EnemyAggro(): 
    odds = Options.EnemyAggroOption.GetSpinbox()
    with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        for en in eneData["rows"]:
            if not Helper.OddsCheck(odds):
                continue
            if en["Flag"]["mBoss"]:
                continue
            en["Detects"] = 0
        JSONParser.CloseFile(eneData, eneFile)
            
def EnemyDesc(name):
    pass


#------------------------------------------------------TORNA SPECIFIC------------------------------------------------------#

def TornaWave1FightChanges(): # we can't allow the player to lose the first fight, since the quest condition is a gimmick corresponding to clearing the entire enemy wave, not a battle that they can lose through the param ReducePCHP
    DesiredParams = [307, 17, 306, 308] # basically give the new enemy the old enemy's stats
    TargetIDs = [0,0,0,0] # IDs we want to target to give the nerfed stats
    with open("./XC2/JsonOutputs/common_gmk/ma40a_FLD_EnemyPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            CurRowID = row["$id"]
            match CurRowID:
                case 40547:
                    TargetIDs[0] = row["ene1ID"]
                case 40548:
                    TargetIDs[1] = row["ene1ID"]
                    TargetIDs[2] = row["ene2ID"]
                case 40549:
                    TargetIDs[3] = row["ene1ID"]
                case 40550:
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for enemy in range(len(TargetIDs)):
        JSONParser.ChangeJSONLine(["common/CHR_EnArrange.json"], [TargetIDs[enemy]], ["ParamRev"], DesiredParams[enemy])   
