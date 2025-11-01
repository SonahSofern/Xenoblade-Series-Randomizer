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
            oldIDs (list): List of IDs that represent the original enemy, from CHR_EnArrange. Either this or newIDs may be used, but you don't need both
            newIDs (list): List of IDs that represent the replacement enemy, from CHR_EnArrange. Either this or oldIDs may be used, but you don't need both
            paramMods(list): List of parameter modifications to CHR_EnParam
            artMods(list): List of art modifications to BTL_Arts_En
            lvDiff (int): The number of levels this enemy loses/gains when placed in a violation fight.
        """
        self.oldIDs = oldIDs
        self.newIDs = newIDs
        self.paramMods = paramMods
        self.artMods = artMods
        self.lvDiff = lvDiff

    # def ResolveLevelDiff(self, enemy): # Not using because level gap changes XP rewards
    #     if self.lvDiff == 0:
    #         return

    #     if self.lvDiff < 0:  # If we are losing levels only let them lose up to half their original level
    #         mult = 0.6
    #     else:
    #         mult = 1.25
    #     levelCap = max(int(enemy["Lv"] * mult), 1)
    #     newLv = max(enemy["Lv"] + self.lvDiff, levelCap)
    #     #print(f"Resolved violation from level {enemy["Lv"]} to level: {newLv} for enemyID={enemy["$id"]}")

    #     enemy["Lv"] = newLv
        
        
class EnemyRandomizer():
    def __init__(self, NormalIDs, UniqueIDs, BossIDs, SuperbossIDs, isEnemies, isNormal, isUnique, isBoss, isSuperboss, rscKey, paramKey, arrangeData, paramData, rscData, artData, scaleKey = "Scale", permanentBandaids = [], duringRandomizationBandaids = []):
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

    def HealthBalancing(self, oldEn, newEn, healthParamKey, maxMult = 2):
        '''
        This function is neccessary because the HP stat in XC2 and XC3 vary wildly. Creating unbalanced fights. 
        '''
        oldEnParam = self.FindParam(oldEn)
        newEnParam = self.FindParam(newEn)
        calculatedMult = newEnParam[healthParamKey]/oldEnParam[healthParamKey] # Get the mult difference between the two 
        chosenMult = min(maxMult, calculatedMult) # Choose which is smaller 
        # print(chosenMult)
        self.ChangeStats([newEn], [(healthParamKey, int(chosenMult*oldEnParam[healthParamKey]))])

    def BalanceFight(self, oldEn, newEn, violationList:list[Violation], enemyCounts:dict):
        """
        Calculates a dynamic stat multiplier for game balancing based on a
        proportional change in the number of enemies.

        This function is designed to scale character stats up or down when they are
        randomized into a fight with a different number of enemies than they were
        originally designed for. For example, it can buff a character designed for a
        group of 4 when they fight alone, or nerf a solo boss when they appear in a
        group of 8.

        The core of the formula is based on the ratio of the new group size (N) to
        the original (M), making the scaling effect relative to the character's
        original context.

        Formula:                         K
                  sgn(N-M) * |(N/M) - 1|^
                C^

        Args:
            M (int): The original number of enemies for the character.
            N (int): The new, randomized number of enemies.
            C (float): The base balancing constant. This value determines the
                       strength of the multiplier. A good starting point is 0.5,
                       which would halve stats if the group size doubles.
            K (float): The scaling exponent, which tunes the "aggressiveness"
                       of the curve.
                       - K=1.0 provides a standard curve.
                       - K<1.0 makes the scaling less aggressive (decreased effect per additional enemy).
                       - K>1.0 makes the scaling more aggressive (increased effect per additional enemy).

        Returns:
            float: The calculated stat multiplier. A value > 1.0 is a buff,
                   and a value < 1.0 is a nerf.
        """
        def BalanceFormula(M, N, C, K):
            return C ** (math.copysign(1, N-M) * (abs(N/M - 1) ** K))

        # Helper function to get the violations which apply to this fight
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

        # Iterate over each violation which applies to the current fight
        vios:list[Violation] = GetViolations()
        for vio in vios:
            oldParams = self.FindParam(newEn)
            allParamChanges = []

            M = enemyCounts[newEn["$id"]] if newEn["$id"] in enemyCounts.keys() else 1
            N = enemyCounts[oldEn["$id"]] if oldEn["$id"] in enemyCounts.keys() else 1

            # Iterate over each art modification
            # Arts are changed first because a change in arts creates another change in the params
            for artMod in vio.artMods:
                # Iterate over each parameter which contains a reference to an art.
                for paramField in artMod.paramFields:
                    allArtChanges = []
                    art = self.FindArt(oldParams[paramField])
                    # Iterate over each art field which needs to change
                    for artField in artMod.artFieldNames:
                        multiplier = BalanceFormula(M, N, artMod.C, artMod.K)
                        if multiplier == 1: # Do not make the change unless something actually changes
                            continue
                        oldValue = art[artField]
                        if artMod.isReciprocal:
                            newValue = math.floor(oldValue * (1 / multiplier))
                        else:
                            newValue = math.floor(oldValue * multiplier)
                        allArtChanges.append((artField, newValue))
                    # Apply any changes to the arts
                    if allArtChanges:
                        self.ChangeArts(art, allArtChanges)
                        newArtID = len(self.artData["rows"])
                        allParamChanges.append((paramField, newArtID))

            # Iterate over each parameter modification
            for paramMod in vio.paramMods:
                # Iterate over each parameter which needs to change
                for paramField in paramMod.fieldNames:
                    multiplier = BalanceFormula(M, N, paramMod.C, paramMod.K)
                    if multiplier == 1: # Do not make the change unless something actually changes
                        continue
                    oldValue = oldParams[paramField]
                    if paramMod.isReciprocal:
                        newValue = math.floor(oldParams[paramField] * (1 / multiplier))
                    else:
                        newValue = math.floor(oldValue * multiplier)
                    allParamChanges.append((paramField, newValue))
            # Apply changes to the parameters
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
        
    def RetainNonArrangeStats(self, newEn, oldEn, keys):
        '''For retaining the old enemies stats that aren't controlled by enarrange, automatically handles flag nested dicts'''
        oldRSC = self.FindRSC(oldEn)
        oldPar = self.FindParam(newEn)
        keyVals = []
        
        def FlagHandler(key, dict):
            if key in dict:
                return dict[key]
            elif ("flag" in dict) and (key in dict["flag"]):
                return dict["flag"][key]
            else:
                return None
        
        for key in keys:
            if key in oldPar:
                keyVals.append((key, FlagHandler(key, oldPar)))
            elif key in oldRSC:
                keyVals.append((key, FlagHandler(key, oldRSC)))
        
        self.ChangeStats([newEn], keyVals)
    
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
                    if en["$id"] == target:
                        handledTargetEn.append(en)
                        break
                        
        
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

    def ChangeArts(self, art, keyVal=[]):
        """
        Allows changing the stats of an individual enemy ID in EnArrange by creating new EnParam and RSC_En for that enemy.
        Args:
            art (dict): art dictionary.
            keyVal (list[tuple]): The keys and their new value in art files to change.
        """
        newArt = copy.deepcopy(art)
        newArtID = len(self.artData["rows"]) + 1
        newArt["$id"] = newArtID

        for key, val in keyVal:
            if key in newArt:
                newArt[key] = val

        self.artData["rows"].append(newArt)
