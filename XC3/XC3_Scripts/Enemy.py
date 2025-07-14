
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs
from scripts import Helper, JSONParser, PopupDescriptions

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix: 
# Land Enemies falling beneath water
# Land enemies falling in the sky          
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies             
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
    with open(f"XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        
        GenEnemyData(eneData)
        
        RandomAssignment(eneData, targetGroup, GenWeights(isNormal, isUnique, isBoss, isSuperboss), isEnemies)

        Bandaids()
        
        JSONParser.CloseFile(eneData, eneFile)

def RandomAssignment(eneData, targetGroup, weights, isEnemies):
    keysList = ['DebugName', 'MapID', 'CatMain', 'CatBGM', '<B569BFB1>', '<352C263C>', '<BA57B736>', 'Scale', 'EliteScale', 'ScalePlus', 'WeaponScale', 'ChrSize', 'TurnSize', 'LevPlus', '<64251F47>', '<3B6DFBC4>', '<EE7FFF6D>', '<F36BAFFD>', 'AiBase', '<0F7768D2>', '<9B3B9099>', 'IdBgm', 'IdBattleEnemy', '<C6717CFE>', 'FlgColiOff', '<EFCB57EC>', 'IconOffset', 'FlgSpDead', '<3828CCE4>', 'FlgSerious', '<3CEBD0A4>', '<9A220E4D>', 'KillEffType', 'SpBattle', '<EC666A80>', '<AB4BA3D5>', '<1104E9C5>', '<B5C5F3B3>', 'MsgName', 'NPCName', 'AlliesMsg', '<D3F77DFD>', 'GetRatio', 'GetEnArts', 'GetEnSkill', 'FootPrintDetection', 'EffConvert', '<7C2FCBE1>', '<97002EDA>', 'VoGroup', 'NotEconomy', 'ExpRate', 'GoldRate', '<91DD0357>', 'AttenuationScale', '<C4D88A2B>', '<7D3D5DCB>', 'NamedSpCond', '<C313305B>', 'Score', '<4BAF120D>', '<7EFBB833>', '<277C5BBD>', '<65449302>', '<192EEE69>', '<F36D8D42>', '<76A4C736>']         # ignoreKeys = ["$id", "ID", "Level", "IdMove", "NamedFlag", "IdDropPrecious", "FlgKeepSword", "FlgNoVanish", "FlgDmgFloor", "FlgMoveFloor", "FlgLevAttack", "FlgLevBattleOff", "FlgFixed", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "FlgNoFalling"]
    # Randomly Assign
    for en in eneData["rows"]:
        if not (en["$id"] in targetGroup):
            continue
        if not Helper.OddsCheck(isEnemies.GetSpinbox()):
            continue
     
        enemyGroup = random.choices(StaticEnemyData, weights)[0]
        newEn = random.choice(enemyGroup.currentGroup)
        
        enemyGroup.currentGroup.remove(newEn) # If group is empty
        if enemyGroup.currentGroup == []:
            enemyGroup.RefreshCurrentGroup()
            
        for key in keysList:
            en[key] = newEn[key]
 
def isBadEnemy(en):
    if en["$id"] in IDs.badEnemies:
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

def SwimmingEnemiesDoomFix():
    with open(f"XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        for en in eneData["rows"]:
            if en["ActType"] == 1:
                en["ActType"] = 0
        JSONParser.CloseFile(eneData, eneFile)

def Bandaids():
    SwimmingEnemiesDoomFix()
    
def EnemyDesc(name):
    pass