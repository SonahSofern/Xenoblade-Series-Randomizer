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
        return copy.deepcopy(en)
        
    def RemoveMember(self, en):
        self.currentGroup.remove(en)
        if self.currentGroup == []:
            self.RefreshCurrentGroup()

class ParamModification:
    def __init__(self, fieldNames:list[str], C=0.5, K=0.5, isReciprocal=False):
        self.fieldNames = fieldNames
        self.C = C
        self.K = K
        self.isReciprocal = isReciprocal

class ArtModification:
    def __init__(self, paramFields:list[str], artFieldNames:list[str], C=0.5, K=0.5, isReciprocal=False):
        self.paramFields = paramFields
        self.artFieldNames = artFieldNames
        self.C = C
        self.K = K
        self.isReciprocal = isReciprocal

class Violation:
    def __init__(self, oldIDs:list[int]=[], newIDs:list[int]=[], paramMods:list[ParamModification]=[], artMods:list[ArtModification]=[], lvDiff=0):
        """
        Initialize a Violation.
        Args:
            ids (list): List of IDs that represent the violation enemy, from CHR_EnArrange.
            lvDiff (int): The number of levels this enemy loses/gains when placed in a group fight.
            TODO: Once done, fix this block comment
        """
        self.oldIDs = oldIDs
        self.newIDs = newIDs
        self.paramMods = paramMods
        self.artMods = artMods
        self.lvDiff = lvDiff

    def ResolveLevelDiff(self, enemy):
        if self.lvDiff == 0:
            return

        if self.lvDiff < 0:  # If we are losing levels only let them lose up to half their original level
            mult = 0.6
        else:
            mult = 1.25
        levelCap = max(int(enemy["Lv"] * mult), 1)
        newLv = max(enemy["Lv"] + self.lvDiff, levelCap)
        #print(f"Resolved violation from level {enemy["Lv"]} to level: {newLv} for enemyID={enemy["$id"]}")

        enemy["Lv"] = newLv
        
        
class EnemyRandomizer():
    def __init__(self, NormalIDs, UniqueIDs, BossIDs, SuperbossIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, rscKey, paramKey, arrangeData, paramData, rscData, artData, scaleKey = "Scale", permanentBandaids = [], actKeys = [], duringRandomizationBandaids = []):
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
        self.scaleKey = scaleKey
        self.actKeys = actKeys
        
        # File Data
        self.paramData = paramData 
        self.arrangeData = arrangeData
        self.rscData = rscData
        self.artData = artData
        
        self.NormalGroup = EnemyGroup()
        self.UniqueGroup = EnemyGroup()
        self.BossGroup = EnemyGroup()
        self.SuperbossGroup = EnemyGroup()
        
        self.permanentBandaids = permanentBandaids
  
    def isBadEnemy(self, en):
        if en["$id"] not in self.NormalIDs + self.UniqueIDs + self.BossIDs + self.SuperbossIDs:
            return True
        
    def GenEnemyData(self):
        for aid in self.permanentBandaids:
            aid()
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

    def BalanceFight(self, oldEn, newEn, violationList:list[Violation], enemyCounts:dict):
        # TODO: Document formula
        def BalanceFormula(M, N, C, K):
            # return C ** (math.copysign(1, N - M) * (abs(N - M) ** K)) # Old Formula
            return C ** (math.copysign(1, N / M - 1) * (abs(N / M - 1) ** K))

        def GetViolations():
            # Find the violation for this specific enemy
            vios = list()
            for vio in violationList:
                # Only old IDs are specified
                if vio.oldIDs and not vio.newIDs:
                    if oldEn["$id"] in vio.oldIDs:
                        vios.append(vio)
                # Only new IDs are specified
                elif vio.newIDs and not vio.oldIDs:
                    if newEn["$id"] in vio.newIDs:
                        vios.append(vio)
                # Both old and new IDs are specified, must match both
                else:
                    if oldEn["$id"] in vio.oldIDs and newEn["$id"] in vio.newIDs:
                        vios.append(vio)

            # Find the default violation if there is still nothing
            # Default violations are defined by an empty list of IDs
            if not vios:
                for vio in violationList:
                    if not vio.oldIDs and not vio.newIDs:
                        vios.append(vio)

            return vios

        vios = GetViolations()

        for vio in vios:
            vio.ResolveLevelDiff(oldEn)

            M = enemyCounts[newEn["$id"]] if newEn["$id"] in enemyCounts.keys() else 1
            N = enemyCounts[oldEn["$id"]] if oldEn["$id"] in enemyCounts.keys() else 1

            oldParams = self.FindParam(newEn)
            allParamChanges = []

            # Arts are changed first because a change in arts creates another change in the params
            for artMod in vio.artMods:
                for paramField in artMod.paramFields:
                    allArtChanges = []
                    art = self.FindArt(oldParams[paramField])
                    for artField in artMod.artFieldNames:
                        multiplier = BalanceFormula(M, N, artMod.C, artMod.K)
                        if multiplier == 1: # Do not make this change unless something actually changes
                            continue
                        oldValue = art[artField]
                        if artMod.isReciprocal:
                            newValue = math.floor(oldValue * (1 / multiplier))
                        else:
                            newValue = math.floor(oldValue * multiplier)
                        allArtChanges.append((artField, newValue))
                    if allArtChanges:
                        self.ChangeArts(newEn, paramField, art, allArtChanges)
                        newArtID = len(self.artData["rows"])
                        allParamChanges.append((paramField, newArtID))

            for paramMod in vio.paramMods:
                for paramField in paramMod.fieldNames:
                    multiplier = BalanceFormula(M, N, paramMod.C, paramMod.K)
                    if multiplier == 1: # Do not make this change unless something actually changes
                        continue
                    oldValue = oldParams[paramField]
                    if paramMod.isReciprocal:
                        newValue = math.floor(oldParams[paramField] * (1 / multiplier))
                    else:
                        newValue = math.floor(oldValue * multiplier)
                    allParamChanges.append((paramField, newValue))
            if allParamChanges:
                self.ChangeStats([newEn], allParamChanges)
            
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

    def FindArt(self, artId):
        for art in self.artData["rows"]:
            if art["$id"] == artId:
                return art

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
           
    def EnemySizeMatch(self, oldEn, newEn, keysList, multDict): # Makes big enemies in boss fights smaller
        '''Enemies that are replaced will have that enemy attempt to match the size of the original'''
        newSize = newEn["ChrSize"]
        oldSize = oldEn["ChrSize"]
        
        if newSize == oldSize:
            return

        defMult = 1
        defScale = 100
        minScale = 10
        if oldEn["$id"] == 455:
            pass
        
        if (oldSize, newSize) in multDict:
            newMult = multDict[(oldSize, newSize)]
        elif (newSize, oldSize) in multDict:
            newMult = (1/multDict[(newSize, oldSize)])
        else:
            newMult = 1
        
        for key in keysList:
            newEn[key] = max(int(defScale * newMult), minScale) 
        
    def ActTypeFix(self, newEnemy, oldEnemy): 
        '''Changes enemies act types to accommodate random spawn locations'''
        oldRSC = self.FindRSC(oldEnemy)
        newRSC = self.FindRSC(newEnemy)
        
        actKeysList = []
        for key in self.actKeys:
            actKeysList.append((key, oldRSC[key]))
        
        if oldRSC["ActType"] != newRSC["ActType"]:  
            self.ChangeStats([newEnemy], actKeysList)
    
    def CreateRandomEnemy(self, StaticEnemyData:list[EnemyGroup]):
        '''Returns a random enemy using weights from the groups generated'''
        newEn = random.choices(StaticEnemyData, self.GenWeights())[0].SelectRandomMember()
        return newEn
       
    def ChangeStats(self, targetEn = [], keyVal = []):
        """
        Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
        Args:
            targetIDs (list[int]): The IDs from EnArrange OR an enemy dictionary.
            keys (list[tuple]): The keys and their new value in parameters or resource files to change.
        """  
        handledTargetEn = []
        for target in targetEn:
            if isinstance(target, dict):
                handledTargetEn.append(target)
            else:
                for en in self.arrangeData["rows"]:
                    if en["$id"] in targetEn:
                        handledTargetEn.append(en)
        
        for en in handledTargetEn:
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

            en[self.paramKey] = newParamID
            newParam[self.rscKey] = newRSCID
            self.paramData["rows"].append(newParam)
            self.rscData["rows"].append(newRSC)

    def ChangeArts(self, en, paramField, art, keyVal=[]):
        """
        Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
        Args:
            targetIDs (list[int]): The IDs from EnArrange OR an enemy dictionary.
            keys (list[tuple]): The keys and their new value in parameters or resource files to change.
            TODO: Create correct block comment
        """
        newArt = copy.deepcopy(art)
        newArtID = len(self.artData["rows"]) + 1
        newArt["$id"] = newArtID

        for key, val in keyVal:
            if key in newArt:
                newArt[key] = val

        #self.ChangeStats(en, [(paramField, newArtID)])

        self.artData["rows"].append(newArt)