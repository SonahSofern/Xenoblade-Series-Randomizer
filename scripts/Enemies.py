import json, random, copy, traceback, math
from scripts import Helper, JSONParser

class EnemyGroup():
    def __init__(self):
        self.originalGroup = []
        self.currentGroup = []
    
    def RefreshCurrentGroup(self):
        self.currentGroup = copy.deepcopy(self.originalGroup)
    
    def SelectRandomMember(self):
        en = random.choice(self.currentGroup)
        self.RemoveMember(en)
        return en
        
    def RemoveMember(self, en):
        self.currentGroup.remove(en)
        if self.currentGroup == []:
            self.RefreshCurrentGroup()
        
def isBadEnemy(en, validEnemies):
    if en["$id"] not in validEnemies:
        return True
    
def GenEnemyData(eneData, NormalIDs, UniqueIDs, BossIDs, SuperbossIDs, NormalGroup, UniqueGroup, BossGroup, SuperbossGroup):
    '''Creates the data in a nested list if it does not already exist, this is only to be copied from never altered'''
    for en in eneData["rows"]:
        if isBadEnemy(en, NormalIDs + UniqueIDs + BossIDs + SuperbossIDs):
            continue
        enID = en["$id"]
        if enID in NormalIDs:
            group = NormalGroup
        elif enID in UniqueIDs:
            group = UniqueGroup
        elif enID in BossIDs:
            group = BossGroup
        elif enID in SuperbossIDs:
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
        
    def ResolveViolation(self, enemy):
        if self.lvDiff < 0: # If we are losing levels only let them lose up to half their original level
            mult = 0.6
        else:
            mult = 1.25
        levelCap = max(int(enemy["Lv"] * mult), 1)
        newLv = max(enemy["Lv"] + self.lvDiff, levelCap)
        # print(f"Resolved violation from level {enemy["Lv"]} to level: {newLv}")
        enemy["Lv"] = newLv

def BalanceFight(oldEn, newEn, groupFightIDs, violationList):
    if oldEn["$id"] not in groupFightIDs:
        return
    for vio in violationList:
        if newEn["$id"] in vio.ids:
            vio.ResolveViolation(oldEn)
            break
        
def FindRSC(paramData, RSCData, enemy, rscKey, paramKey):
    param = FindParam(paramData, enemy, paramKey)
    for rsc in RSCData["rows"]:
        if param[rscKey] == rsc["$id"]:
            return rsc

def FindParam(paramData, enemy, paramKey):
    for param in paramData["rows"]:
        if param["$id"] == enemy[paramKey]:
            return param

def FilterEnemies(en, targetGroup, isEnemies, validEnemies):
    '''Returns true if enemy has been filtered out'''
    if not (en["$id"] in targetGroup):
        return True
    if not Helper.OddsCheck(isEnemies.GetSpinbox()):
        return True
    if isBadEnemy(en, validEnemies):
        return True

def CopyKeys(en, newEn, ignoreKeys):
    for key in en:
        if key in ignoreKeys:
            continue
        en[key] = newEn[key]
        
def ActTypeFix(newEnemy, oldEnemy, RSCData, paramData, arrangeData): 
    '''Changes enemies act types to accommodate random spawn locations'''
            
    oldRSC = FindRSC(paramData, RSCData, oldEnemy)
    newRSC = FindRSC(paramData, RSCData, newEnemy)
    if oldRSC["ActType"] != newRSC["ActType"]:  
        ChangeStats([newEnemy], [("ActType", oldRSC["ActType"]), ("FlyHeight", oldRSC["FlyHeight"])], arrangeData, paramData, RSCData)
         
def ChangeStats(enemy = [], keyVal = [], arrangeData = None, paramData = None, RSCData = None, paramKey = "", rscKey = "", arrangeFilePath = "", paramFilePath = "", rscFilePath = ""):
    """
    Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
    Args:
        enemyID (list[int]): The IDs from EnArrange.
        keys (list[tuple]): The keys and their new value in EnParam to change.
        arrangeData/paramData/RSCData: If left as default this will open the files and get the data, change it then close, otherwise you can pass the data.
    """  
    def LocalChange(paramData, RSCData, en):
        param = FindParam(paramData, en, "ParamID")
        newParam = copy.deepcopy(param)
        newParamID =  len(paramData["rows"]) + 1
        newParam["$id"] = newParamID
        
        rsc = FindRSC(paramData, RSCData, en, "ResourceID", "ParamID")
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
        with open(arrangeFilePath, 'r+', encoding='utf-8') as arrangeFile:
            with open(paramFilePath, 'r+', encoding='utf-8') as paramFile:
                with open(rscFilePath, 'r+', encoding='utf-8') as RSCFile:   
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

def BigEnemyBossFightSizeFix(oldEn, newEn, bossIDs): # Makes big enemies in boss fights smaller
    if oldEn["$id"] not in bossIDs:
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
            