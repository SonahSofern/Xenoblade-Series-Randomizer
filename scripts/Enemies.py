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
        print(f"Resolved violation from level {enemy["Lv"]} to level: {newLv}")
        enemy["Lv"] = newLv


class EnemyRandomizer():
    def __init__(self, NormalIDs, UniqueIDs, BossIDs, SuperbossIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, rscKey, paramKey, arrangeData, paramData, rscData):
        # Enemy Groups
        self.NormalIDs = NormalIDs
        self.UniqueIDs = UniqueIDs
        self.BossIDs = BossIDs
        self.SuperbossIDs = SuperbossIDs
        
        # Settings
        self.isEnemies = isEnemies
        self.isNormal = isNormal
        self.isUnique = isUnique
        self.isBoss = isBoss
        self.isSuperboss = isSuperboss
        
        self.rscKey = rscKey
        self.paramKey = paramKey
        
        # File Data
        self.paramData = paramData 
        self.arrangeData = arrangeData
        self.rscData = rscData
        
        self.NormalGroup = EnemyGroup()
        self.UniqueGroup = EnemyGroup()
        self.BossGroup = EnemyGroup()
        self.SuperbossGroup = EnemyGroup()
  
    def isBadEnemy(self, en):
        if en["$id"] not in self.NormalIDs + self.UniqueIDs + self.BossIDs + self.SuperbossIDs:
            return True
        
    def GenEnemyData(self):
        '''Creates the data in a nested list if it does not already exist, this is only to be copied from never altered'''
        for en in self.arrangeData["rows"]:
            if self.isBadEnemy(en):
                continue
            enID = en["$id"]
            if enID in self.NormalIDs:
                group = self.NormalGroup
            elif enID in self.UniqueIDs:
                group = self.UniqueGroup
            elif enID in self.BossIDs:
                group = self.BossGroup
            elif enID in self.SuperbossIDs:
                group = self.SuperbossGroup
            
            group.currentGroup.append(en.copy())
            group.originalGroup.append(en.copy())
        return [self.NormalGroup, self.UniqueGroup, self.BossGroup, self.SuperbossGroup]
    
    def GenWeights(self):
        weights = [0,0,0,0]
        if self.isNormal.GetState():
            weights[0] = self.isNormal.GetSpinbox()
        if self.isUnique.GetState():
            weights[1] = self.isUnique.GetSpinbox()
        if self.isBoss.GetState():
            weights[2] = self.isBoss.GetSpinbox()
        if self.isSuperboss.GetState():
            weights[3] = self.isSuperboss.GetSpinbox()
        return weights

    def BalanceFight(self, oldEn, newEn, fightIDs, violationList):
        if oldEn["$id"] not in fightIDs:
            return
        for vio in violationList:
            if newEn["$id"] in vio.ids:
                vio.ResolveViolation(oldEn)
                break
            
    def FindRSC(self, enemy):
        param = self.FindParam(enemy)
        for rsc in self.rscData["rows"]:
            try:
                if param[self.rscKey] == rsc["$id"]:
                    return rsc
            except:
                pass

    def FindParam(self, enemy):
        for param in self.paramData["rows"]:
            if param["$id"] == enemy[self.paramKey]:
                return param

    def FilterEnemies(self, en, targetGroup):
        '''Returns true if enemy has been filtered out'''
        if not (en["$id"] in targetGroup):
            return True
        if not Helper.OddsCheck(self.isEnemies.GetSpinbox()):
            return True
        if self.isBadEnemy(en):
            return True

    def CopyKeys(self, en, newEn, ignoreKeys = []):
        for key in en:
            if key in ignoreKeys:
                continue
            if key in newEn:
                en[key] = newEn[key]
            
    def ActTypeFix(self, newEnemy, oldEnemy): 
        '''Changes enemies act types to accommodate random spawn locations'''
        oldRSC = self.FindRSC(oldEnemy)
        newRSC = self.FindRSC(newEnemy)
        
        if oldRSC["ActType"] != newRSC["ActType"]:  
            self.ChangeStats([newEnemy], [("ActType", oldRSC["ActType"]), ("FlyHeight", oldRSC["FlyHeight"])])
    
    def GetRandomEnemy(self, StaticEnemyData):
        newEn = random.choices(StaticEnemyData, self.GenWeights())[0].SelectRandomMember()
        return newEn
       
    def ChangeStats(self, targetIDs = [], keyVal = []):
        """
        Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
        Args:
            targetIDs (list[int]): The IDs from EnArrange.
            keys (list[tuple]): The keys and their new value in parameters or resource files to change.
        """  
        for en in self.arrangeData["rows"]:
            if en["$id"] not in targetIDs:
                continue
            param = self.FindParam(en)
            newParam = copy.deepcopy(param)
            newParamID =  len(self.paramData["rows"]) + 1
            newParam["$id"] = newParamID
            
            rsc = self.FindRSC(en)
            newRSC = copy.deepcopy(rsc)
            newRSCID =  len(self.rscData["rows"]) + 1
            newRSC["$id"] = newRSCID
            
            for key, val in keyVal:
                if key in newParam:
                    newParam[key] = val
                    
            for key, val in keyVal:
                if key in newRSC:
                    newRSC[key] = val

            en["ParamID"] = newParamID
            newParam["ResourceID"] = newRSCID
            self.paramData["rows"].append(newParam)
            self.rscData["rows"].append(newRSC)
                    

    def BigEnemyBossFightSizeFix(self, oldEn, newEn): # Makes big enemies in boss fights smaller
        if oldEn["$id"] not in self.BossIDs:
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
                