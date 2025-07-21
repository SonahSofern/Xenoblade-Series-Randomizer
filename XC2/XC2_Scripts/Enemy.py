import json, random, copy, traceback, math
from XC2.XC2_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as e


StaticEnemyData:list[e.EnemyGroup] = []
                                                                                                                                                                                                                                                                                                          
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies):
    global StaticEnemyData
    GroupFightViolations = GetGroupFightViolations()
    GroupFightIDs = GetGroupFightIDs()
    SoloFightViolations = GetSoloFightViolations()
    soloFightIDs = [179, 182, 258, 260, 262, 256, 604]
    ignoreKeys = ['$id', 'Lv', 'LvRand', 'ExpRev', 'GoldRev', 'WPRev', 'SPRev', 'DropTableID', 'DropTableID2', 'DropTableID3', 'PreciousID', 'Score', 'ECube', 'Flag', 'Detects', 'SearchRange', 'SearchAngle', 'SearchRadius', 'BatInterval', 'BatArea', 'BatAreaType', 'DrawWait', 'ZoneID', 'TimeSet', 'WeatherSet', 'DriverLev']
    
    with open("XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = e.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID", "ParamID", eneData, paramData, rscData)
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                    Bandaids(eneData)
                    if isBoss.GetState():
                        BaseGameIntroChanges(eRando)
                        TornaIntroChanges(eRando)
                
                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue 
                    
                    newEn = eRando.GetRandomEnemy(StaticEnemyData)
                
                    eRando.ActTypeFix(newEn, en)
                    
                    # Blade Act Fix
                    if newEn["EnemyBladeID"] != 0:
                        for enBlade in eneData["rows"]:
                            if enBlade['$id'] == newEn['EnemyBladeID']:
                                eRando.ActTypeFix(enBlade, en)
                    
                    if Options.BossEnemyOption_Solo.GetState():
                        eRando.BalanceFight(en, newEn, soloFightIDs, SoloFightViolations)
                    if Options.BossEnemyOption_Group.GetState():
                        eRando.BalanceFight(en, newEn, GroupFightIDs, GroupFightViolations)
                        
                    eRando.BigEnemyBossFightSizeFix(en, newEn)
                    CloneEnemiesDefeatCondition(en, newEn)
                    AionRoomFix(en, newEn, eRando)
                    
                    eRando.CopyKeys(en, newEn, ignoreKeys)
                        
                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()
                
                JSONParser.CloseFile(eneData, eneFile)
                JSONParser.CloseFile(paramData, paramFile)
                JSONParser.CloseFile(rscData, rscFile)


def Bandaids(eneData):
    '''Bandaids intented to be ran once'''
    ForcedWinFights([3,6])
    AeshmaCoreHPNerf()
    # GortOgreUppercutRemoval()
    EarthBreathNerf()
    SummonsFix(eneData)

def GetSoloFightViolations():
        # Solo Fight Violations
    SoloUniqueMonstersViolations = e.Violation(IDs.UniqueMonsters, -15)
    SoloSuperbossMonstersViolations = e.Violation(IDs.SuperbossMonsters, -30)
    SoloBossMonsterViolations = e.Violation(IDs.BossMonsters, -15)
    SoloFightViolations:list[e.Violation] = [SoloUniqueMonstersViolations, SoloSuperbossMonstersViolations, SoloBossMonsterViolations]
    return SoloFightViolations

def GetGroupFightViolations():
        # Group Fight Violations 
    Jin = e.Violation([1754, 231, 241, 244, 253, 272], -10)
    Akhos = e.Violation([212, 238, 267])
    Malos = e.Violation([214, 243, 245, 268, 273], -10)
    Patroka = e.Violation([223, 239, 270])
    Mikhail = e.Violation([225, 240, 271])
    Aeshma = e.Violation([232,233,234], -10)
    Amalthus = e.Violation([254], -10)
    Aion = e.Violation([265, 275], -20)
    GroupUniqueMonstersViolations = e.Violation(IDs.UniqueMonsters, -5)
    GroupSuperbossMonstersViolations = e.Violation(IDs.SuperbossMonsters, -20)
    GroupBossMonsterViolations = e.Violation(IDs.BossMonsters, -10)
    GroupNormalMonsterViolation = e.Violation(IDs.NormalMonsters, 2)
    GroupFightViolations:list[e.Violation] = [Jin, Akhos, Malos, Patroka, Mikhail, Aeshma, Amalthus, Aion, GroupUniqueMonstersViolations, GroupSuperbossMonstersViolations, GroupBossMonsterViolations, GroupNormalMonsterViolation]
    return GroupFightViolations

def GetGroupFightIDs():
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
    return GroupFightIDs

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
        
def BaseGameIntroChanges(e:e.EnemyRandomizer):
    e.ChangeStats([179], [("HpMaxRev", 50)])
    
def TornaIntroChanges(e:e.EnemyRandomizer):
    e.ChangeStats([1430, 1429, 1428, 1454], [("HpMaxRev", 10)])

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
    
def AionRoomFix(origEn, newEn, eRando:e.EnemyRandomizer): # Aion sits really far down so raise enemies up
    AionIDs = [265, 275]
    if ((origEn["$id"] in AionIDs) and (newEn["$id"] not in AionIDs)): # Need a clause to keep original flyheight if the enemy is actually aion
        eRando.ChangeStats([newEn], [("FlyHeight", 200)])   
 
def EnemyDesc(name):
    pass