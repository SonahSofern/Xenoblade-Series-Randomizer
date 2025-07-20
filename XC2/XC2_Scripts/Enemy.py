import json, random, copy, traceback, math
from XC2.XC2_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions

class EnemyGroup():
    def __init__(self):
        self.originalGroup = []
        self.currentGroup = []
    
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
        
        firstGen = GenEnemyData(eneData)
        
        RandomAssignment(eneData, targetGroup, GenWeights(isNormal, isUnique, isBoss, isSuperboss), isEnemies)

        if firstGen:
            Bandaids(eneData)
        
        JSONParser.CloseFile(eneData, eneFile)
        
        
def RandomAssignment(eneData, targetGroup, weights, isEnemies):
    keysList = ['EnemyBladeID', 'BladeID', 'BladeAtr', 'ParamID', 'ExtraParts', 'Name', 'Debug_Name', 'HpOver', 'Scale', 'ChrSize', 'TurnSize', 'CamSize', 'LinkRadius', 'EN_WATER_DEAD_NONE', 'AiGroup', 'AiGroupNum', 'BookID', 'EnhanceID1', 'EnhanceID2', 'EnhanceID3', 'ParamRev', 'RstDebuffRev', 'HealPotTypeRev', 'SummonID', 'BGMID', 'SeEnvID', 'Race', 'LvMin', 'LvMax', 'ScaleMin', 'ScaleMax']
    # Randomly Assign
    with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
        with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as RSCfile:
            paramData = json.load(paramFile)
            RSCData = json.load(RSCfile)
            for en in eneData["rows"]:
                if not (en["$id"] in targetGroup):
                    continue
                if not Helper.OddsCheck(isEnemies.GetSpinbox()):
                    continue
                if isBadEnemy(en):
                    continue
            
                enemyGroup = random.choices(StaticEnemyData, weights)[0]
                newEn = random.choice(enemyGroup.currentGroup)
                
                # Remove enemy from group
                enemyGroup.currentGroup.remove(newEn)
                if enemyGroup.currentGroup == []:
                    enemyGroup.RefreshCurrentGroup()
                
                ActTypeFix(newEn, en, RSCData, paramData, eneData)
                
                if newEn["EnemyBladeID"] != 0:
                    for enBlade in eneData["rows"]:
                        if enBlade['$id'] == newEn['EnemyBladeID']:
                            ActTypeFix(enBlade, en, RSCData, paramData, eneData)
                
                if Options.BossEnemyOption_Solo.GetState():
                    BalanceSoloFights(en, enemyGroup)
                if Options.BossEnemyOption_Group.GetState():
                    BalanceGroupFights(en, newEn)
                
                BigEnemyRedCircleSizeFix(en, newEn)
                CloneEnemiesDefeatCondition(en, newEn)
                AionRoomFix(en, newEn, RSCData, paramData, eneData)
                
                for key in keysList:
                    en[key] = newEn[key]
                    
            for group in StaticEnemyData:
                group.RefreshCurrentGroup()
                  
            JSONParser.CloseFile(paramData, paramFile)                
            JSONParser.CloseFile(RSCData, RSCfile)   
 
def isBadEnemy(en):
    if en["$id"] not in (IDs.NormalMonsters + IDs.BossMonsters + IDs.UniqueMonsters + IDs.SuperbossMonsters):
        return True

def GenEnemyData(eneData):
    '''Creates the data in a nested list if it does not already exist, this is only to be copied from never altered'''
    if NormalGroup.originalGroup != []:
        return False
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
    return True
    
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
    with open("XC2/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in fights: #battle on gramps at start of game
                row["ReducePCHP"] = 1
        JSONParser.CloseFile(data, file)

def AeshmaCoreHPNerf(): # Aeshma is almost unkillable with its regen active
    with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 318:
                row["HpMaxRev"] = 1500 # nerfed hp by 5/6ths
        JSONParser.CloseFile(data, file)
  
def BalanceSoloFights(originalEn, enemyGroup): # 
    soloFightIDs = [179, 182, 258, 260, 262, 256, 604]
    if originalEn["$id"] in soloFightIDs:
        if enemyGroup == SuperbossGroup:
            lvDrop = 30
        elif enemyGroup == BossGroup:
            lvDrop = 15
        elif enemyGroup == UniqueGroup:
            lvDrop = 15 
        else:
            return
        halfOriginalLevel = max(int(originalEn["Lv"] // 2), 1)
        originalEn["Lv"] = max(originalEn["Lv"] - lvDrop, halfOriginalLevel)
        # print(f"Lowered lv of {originalEn["$id"]} by {lvDrop} to {originalEn["Lv"]}")

class Violation:
    def __init__(self, ids, lvDiff = -5):
        """
        Initialize a Violation.
        Args:
            ids (list): List of IDs that represent the violation enemy, from CHR_EnArrange.
            lvDiff (int): The number of levels this enemy loses/gains when placed in a group fight.
        """        
        self.ids = ids
        self.lvDiff = lvDiff
        ViolationList.append(self)
        
    def ResolveViolation(self, enemy):
        if self.lvDiff < 0: # If we are losing levels only let them lose up to half their original level
            mult = 0.6
        else:
            mult = 1.25
        levelCap = max(int(enemy["Lv"] * mult), 1)
        newLv = max(enemy["Lv"] + self.lvDiff, levelCap)
        # print(f"Resolved violation from level {enemy["Lv"]} to level: {newLv}")
        enemy["Lv"] = newLv
        
ViolationList:list[Violation] = []
Jin = Violation([1754, 231, 241, 244, 253, 272], -10)
Akhos = Violation([212, 238, 267])
Malos = Violation([214, 243, 245, 268, 273], -10)
Patroka = Violation([223, 239, 270])
Mikhail = Violation([225, 240, 271])
Aeshma = Violation([232,233,234], -10)
Amalthus = Violation([254], -10)
Aion = Violation([265, 275], -20)
UniqueMonstersViolations = Violation(IDs.UniqueMonsters, -5)
SuperbossMonstersViolations = Violation(IDs.SuperbossMonsters, -20)
BossMonsterViolations = Violation(IDs.BossMonsters, -10)
NormalMonsterViolation = Violation(IDs.NormalMonsters, 2)

ArdanianSoldiers = [189,190,219]
Puffots = [195]
Bandits = [196,197,198]
VandhamTrio = [199,201,202]
Tirkin = [220, 235]
TantaleseKnight = [237]
AkhosTrio = [238,239,240]
Phantasm = [242]
Guldos = [249]
IndolSoldier = [252]
GroupFightIDs = Puffots + Bandits + VandhamTrio + ArdanianSoldiers + Tirkin + TantaleseKnight + AkhosTrio + Phantasm + Guldos + IndolSoldier

def BalanceGroupFights(oldEn, newEn):
    if oldEn["$id"] not in GroupFightIDs:
        return
    for vio in ViolationList:
        if newEn["$id"] in vio.ids:
            vio.ResolveViolation(oldEn)
            break
    
def BigEnemyRedCircleSizeFix(oldEn, newEn): # Makes big enemies in boss fights smaller
    if oldEn["$id"] not in IDs.BossMonsters:
        return
    Massive = 3
    Large = 2
    minScale = 25
    
    if newEn["ChrSize"] == Large:
        scaleMult = .6
    elif newEn["ChrSize"] == Massive:
        scaleMult = .25
    elif newEn["Scale"] >= 200: # Some enemies are scaled up even if they arent normally gigantic
        scaleMult = .5
    else:
        return
    newEn["Scale"] = max(int(newEn["Scale"] * scaleMult), minScale)
             
def CloneEnemiesDefeatCondition(oldEn, newEn): # Forces all copies of enemies that clone themselves to be defeated in a boss encounter
    CloneEnemyIDs = [242, 281, 1882, 1884]
    if oldEn["$id"] not in IDs.BossMonsters:
        return
    if newEn["$id"] not in CloneEnemyIDs:
        return
    with open("XC2/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as questFile:
        questData = json.load(questFile)
        for quest in questData["rows"]:
            if quest["EnemyID"] == oldEn["$id"]:
                quest["DeadAll"] = 1
                print(f"Added DeadAll to row {quest["$id"]} of QuestBattle, because it got {newEn["$id"]}")
                break
        JSONParser.CloseFile(questData, questFile)

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

def Bandaids(eneData):
    '''Some bandaids intended to run if any rando is on, keep in mind these are meant to be ran once after initial randomization. Some things are better fixed during randomization.'''
    ForcedWinFights([3,6])
    AeshmaCoreHPNerf()
    # GortOgreUppercutRemoval()
    EarthBreathNerf()
    SummonsFix(eneData)
    
def FindRSC(paramData, RSCData, enemy):
    param = FindParam(paramData, enemy)
    for rsc in RSCData["rows"]:
        if param["ResourceID"] == rsc["$id"]:
            return rsc

def FindParam(paramData, enemy):
    for param in paramData["rows"]:
        if param["$id"] == enemy["ParamID"]:
            return param

def ActTypeFix(newEnemy, oldEnemy, RSCData, paramData, arrangeData): 
    '''Changes enemies act types to accommodate random spawn locations''' # This should be fixable by extending the RSCEN and EnParam
            
    oldRSC = FindRSC(paramData, RSCData, oldEnemy)
    newRSC = FindRSC(paramData, RSCData, newEnemy)
    if oldRSC["ActType"] != newRSC["ActType"]:            
        ChangeStats([newEnemy], [("ActType", oldRSC["ActType"]), ("FlyHeight", oldRSC["FlyHeight"])], arrangeData, paramData, RSCData)

   
def SummonsFix(eneData):
    for ene in eneData["rows"]:
        if ene["$id"] in IDs.SummonedEnemies:
            ene["DriverLev"] = 1 # Not a great solution the other way is to make a duplicate enemy for each time they are summoned and I woulid have to make new summon tables
    
def EnemyAggro(): # Not going to add aggro to enemies because it would be disproportional to the area there enemy is in. For example if i tgive them batArea and a large area you could get stuck inside a small area (ship) with enemies perma aggroing you
    odds = Options.EnemyAggroOption.GetSpinbox()
    with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        for en in eneData["rows"]:
            if not Helper.OddsCheck(odds):
                continue
            if en["$id"] in IDs.BossMonsters:
                continue
            en["Detects"] = 0
        JSONParser.CloseFile(eneData, eneFile)
   
def ChangeStats(enemy = [], keyVal = [], arrangeData = None, paramData = None, RSCData = None):
    """
    Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
    Args:
        enemyID (list[int]): The IDs from EnArrange.
        keys (list[tuple]): The keys and their new value in EnParam to change.
        arrangeData/paramData/RSCData: If left as default this will open the files and get the data, change it then close, otherwise you can pass the data.
    """  
    def LocalChange(paramData, RSCData, en):
        param = FindParam(paramData, en)
        newParam = copy.deepcopy(param)
        newParamID =  len(paramData["rows"]) + 1
        newParam["$id"] = newParamID
        
        rsc = FindRSC(paramData, RSCData, en)
        newRSC = copy.deepcopy(rsc)
        newRSCID =  len(RSCData["rows"]) + 1
        newRSC["$id"] = newRSCID
        
        for key, val in keyVal:
            if key in newParam:
                newParam[key] = val
                
        for key, val in keyVal:
            if key in newRSC:
                newRSC[key] = val

        en["ParamID"] = newParamID
        newParam["ResourceID"] = newRSCID
        paramData["rows"].append(newParam)
        RSCData["rows"].append(newRSC)
                
    if arrangeData == None: 
        with open("XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as arrangeFile:
            with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
                with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as RSCFile:   
                    arrangeData = json.load(arrangeFile)
                    paramData = json.load(paramFile)
                    RSCData = json.load(RSCFile)
                    for en in arrangeData["rows"]:
                        if en["$id"] in enemy:
                            LocalChange(paramData, RSCData, en)
                    JSONParser.CloseFile(arrangeData, arrangeFile)
                    JSONParser.CloseFile(paramData, paramFile)   
                    JSONParser.CloseFile(RSCData, RSCFile)
    else:
        for en in enemy:
            LocalChange(paramData, RSCData, en)
        

def TornaIntroChanges():
    ChangeStats([1430, 1429, 1428, 1454], [("HpMaxRev", 10)])

def AionRoomFix(origEn, newEn, rscData, paramData, enData): # Aion sits really far down so raise enemies up
    AionIDs = [265, 275]
    if ((origEn["$id"] in AionIDs) and (newEn["$id"] not in AionIDs)): # Need a clause to keep original flyheight if the enemy is actually aion
        ChangeStats([newEn], [("FlyHeight", 0)], enData, paramData, rscData)   
 
def EnemyDesc(name):
    pass