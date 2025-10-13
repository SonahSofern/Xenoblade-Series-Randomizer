import json, random, copy, traceback, math
from XC2.XC2_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as e, Interactables

StaticEnemyData:list[e.EnemyGroup] = []
                                                                                                                                                                                                                                                                                                          
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isVanillaAggro, matchSize:Interactables.Option):
    global StaticEnemyData
    # GroupFightViolations = GetGroupFightViolations()
    # GroupFightIDs = GetGroupFightIDs()
    # SoloFightViolations = GetSoloFightViolations()
    # soloFightIDs = [179, 182, 184, 185, 186, 187, 189, 190, 258, 260, 262, 256, 604] # Includes both 1 and 2 person party fights
    ignoreKeys = ['$id', 'Lv', 'LvRand', 'ExpRev', 'GoldRev', 'WPRev', 'SPRev', 'DropTableID', 'DropTableID2', 'DropTableID3', 'PreciousID', 'Score', 'ECube', 'Flag', 'DrawWait', 'ZoneID', 'TimeSet', 'WeatherSet', 'DriverLev', "HpOver"]
    aggroKeys = ['Detects', 'SearchRange', 'SearchAngle', 'SearchRadius', 'BatInterval', 'BatArea', 'BatAreaType']
    isMatchSize = matchSize.GetState()
    isStatBalance = True
    if isVanillaAggro:
        ignoreKeys.extend(aggroKeys)
    
    actKeys = ["FlyHeight", "ActType"]
    with open("XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = e.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID", "ParamID", eneData, paramData, rscData, permanentBandaids=[lambda: EarthBreathNerf(), lambda: AeshmaCoreHPNerf(paramData), lambda: GortOgreUppercutRemoval(paramData)], actKeys=actKeys)
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                
                for oldEn in eRando.arrangeData["rows"]:
                    if eRando.FilterEnemies(oldEn, targetGroup):
                        continue 
                    
                    newEn = eRando.CreateRandomEnemy(StaticEnemyData)
                  
                    # if Options.BossEnemyOption_Solo.GetState():
                    #     eRando.BalanceFight(oldEn, newEn, soloFightIDs, SoloFightViolations) 
                    # if Options.BossEnemyOption_Group.GetState():
                    #     eRando.BalanceFight(oldEn, newEn, GroupFightIDs, GroupFightViolations) 
                        
                    if isMatchSize:
                        EnemySizeHelper(oldEn, newEn, eRando)
                        
                    if not isMatchSize and targetGroup == IDs.BossMonsters: # Forces red rings to be gone if you dont scale bosses to avoid softlocks, you cannot hit enemies outside rings and they can spawn weird when big
                        RedRingRemoval()
                        
                    if isStatBalance:
                        StatBalancing(oldEn, newEn, eRando)
                        
                        
                    CloneEnemiesDefeatCondition(oldEn, newEn) 
                    
                    eRando.ActTypeFix(newEn, oldEn)
                    
                    # Blade Act Fix
                    if newEn["EnemyBladeID"] != 0:
                        for enBlade in eRando.arrangeData["rows"]:
                            if enBlade['$id'] == newEn['EnemyBladeID']:
                                CreateBlade(enBlade, oldEn, newEn, eRando)
                                break
                            
                    AionRoomFix(oldEn, newEn, eRando) 
                                                
                    eRando.CopyKeys(oldEn, newEn, ignoreKeys) # Keep in mind this will overwrite changes made to the old enemy 
                    
                        
                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()
                                        
                Bandaids(eneData, isBoss, eRando) # Changes based on ID after the initial swap

                JSONParser.CloseFile(eRando.arrangeData, eneFile)
                JSONParser.CloseFile(eRando.paramData, paramFile)
                JSONParser.CloseFile(eRando.rscData, rscFile)


def StatBalancing(oldEn, newEn, eRando:e.EnemyRandomizer):
    eRando.ChangeStats([newEn], [("HpMaxRev", eRando.FindParam(oldEn)["HpMaxRev"])]) # Makes HP match previous enemy stats in XC2 generally stay around 1000 and dont need balancing but HP varies wildly and can lead to unfair early games this will stop that

def CreateBlade(enBlade, oldEn, newEn, eRando:e.EnemyRandomizer): # Because there is only 1 blade referenced for each enemy we have to create new blades (Since blades are not referenced in gimmick files it is fine)
    newBlade = copy.deepcopy(enBlade)
    newID =  len(eRando.arrangeData["rows"]) + 1
    newBlade["$id"] = newID
    eRando.arrangeData["rows"].append(newBlade)
    newEn["EnemyBladeID"] = newID
    eRando.ActTypeFix(newBlade, oldEn)
    EnemySizeHelper(oldEn, newBlade, eRando)

def RedRingRemoval():
    ValidEnemyPopFileNames = ["ma01a_FLD_EnemyPop.json", "ma02a_FLD_EnemyPop.json", "ma04a_FLD_EnemyPop.json", "ma05a_FLD_EnemyPop.json", "ma05c_FLD_EnemyPop.json", "ma07a_FLD_EnemyPop.json", "ma07c_FLD_EnemyPop.json", "ma08a_FLD_EnemyPop.json", "ma08c_FLD_EnemyPop.json", "ma10a_FLD_EnemyPop.json", "ma10c_FLD_EnemyPop.json", "ma11a_FLD_EnemyPop.json", "ma13a_FLD_EnemyPop.json", "ma13c_FLD_EnemyPop.json", "ma15a_FLD_EnemyPop.json", "ma15c_FLD_EnemyPop.json", "ma16a_FLD_EnemyPop.json", "ma17a_FLD_EnemyPop.json", "ma17c_FLD_EnemyPop.json", "ma18a_FLD_EnemyPop.json", "ma18c_FLD_EnemyPop.json", "ma20a_FLD_EnemyPop.json", "ma20c_FLD_EnemyPop.json", "ma21a_FLD_EnemyPop.json", "ma40a_FLD_EnemyPop.json", "ma41a_FLD_EnemyPop.json", "ma42a_FLD_EnemyPop.json"]
    for name in ValidEnemyPopFileNames:
        with open(f"XC2/JsonOutputs/common_gmk/{name}", 'r+', encoding='utf-8') as popFile:
            popData = json.load(popFile)
            for pop in popData["rows"]:
                pop["battlelockname"] = 0
            JSONParser.CloseFile(popData, popFile)
        
def EnemySizeHelper(oldEn, newEn, eRando:e.EnemyRandomizer):
    Massive = 3
    Large = 2
    Normal = 1
    Small = 0
    
    multDict = {
        (Massive, Large): 2,
        (Massive, Normal): 3,
        (Massive, Small): 5,
        (Large, Normal): 1,
        (Large, Small): 2,
        (Normal, Small): 1,
    }
    keys = ["Scale"]
    eRando.EnemySizeMatch(oldEn, newEn, keys, multDict)

def Bandaids(eneData, isBoss, eRando):
    '''Bandaids intented to be ran once'''
    ForcedWinFights([3,6])
    SummonsFix(eneData)
    if isBoss.GetState():
        TornaIntroChanges(eRando)

 # Solo Fight Violations
def GetSoloFightViolations():
    SoloUniqueMonstersViolations = e.Violation(IDs.UniqueMonsters, -15)
    SoloSuperbossMonstersViolations = e.Violation(IDs.SuperbossMonsters, -30)
    SoloBossMonsterViolations = e.Violation(IDs.BossMonsters, -15)
    SoloFightViolations:list[e.Violation] = [SoloUniqueMonstersViolations, SoloSuperbossMonstersViolations, SoloBossMonsterViolations]
    return SoloFightViolations

# Group Fight Violations 
def GetGroupFightViolations():
    Jin = e.Violation([1754, 231, 241, 244, 253, 272], -10)
    Akhos = e.Violation([212, 238, 267])
    Malos = e.Violation([214, 243, 245, 268, 273], -10)
    Malos = e.Violation([214, 243, 245, 268, 273], [("Lv", 15)])
    Patroka = e.Violation([223, 239, 270])
    Mikhail = e.Violation([225, 271])
    Aeshma = e.Violation([232,233,234], -10)
    Amalthus = e.Violation([254], -10)
    Aion = e.Violation([265, 275], -20)
    GroupUniqueMonstersViolations = e.Violation(IDs.UniqueMonsters, -5)
    GroupSuperbossMonstersViolations = e.Violation(IDs.SuperbossMonsters, -20)
    GroupBossMonsterViolations = e.Violation(IDs.BossMonsters, -5)
    GroupNormalMonsterViolation = e.Violation(IDs.NormalMonsters, 2)
    return [Jin, Akhos, Malos, Patroka, Mikhail, Aeshma, Amalthus, Aion, GroupUniqueMonstersViolations, GroupSuperbossMonstersViolations, GroupBossMonsterViolations, GroupNormalMonsterViolation]

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
    return Puffots + Bandits + VandhamTrio + ArdanianSoldiers + Tirkin + TantaleseKnight + AkhosTrio + Phantasm + Guldos + IndolSoldier

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
                # print(f"Added DeadAll to row {quest["$id"]} of QuestBattle, because it got {newEn["$id"]}")
                break
        JSONParser.CloseFile(questData, questFile)

def GortOgreUppercutRemoval(paramData): # Gort 2's Ogre Uppercut seems to be buggy, reported to crash game in certain situations, so it's being removed for the time being.
    for row in paramData["rows"]:
        if row["$id"] == 1434:
            row["ArtsNum4"] = 963 # replaced Ogre Uppercut with a second instance of Ogre Flame
            break

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

    
def TornaIntroChanges(e:e.EnemyRandomizer):
    e.ChangeStats([1430, 1429, 1428, 1454], [("HpMaxRev", 10)])

def ForcedWinFights(fights = []):
    with open("XC2/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in fights: #battle on gramps at start of game
                row["ReducePCHP"] = 1
        JSONParser.CloseFile(data, file)

def AeshmaCoreHPNerf(paramData): # Aeshma is almost unkillable with its regen active
    for row in paramData["rows"]:
        if row["$id"] == 318:
            row["HpMaxRev"] = 1500 # nerfed hp by 5/6ths
    
def AionRoomFix(origEn, newEn, eRando:e.EnemyRandomizer): # Aion sits really far down so raise enemies up
    AionIDs = [265, 275]
    if ((origEn["$id"] in AionIDs) and (newEn["$id"] not in AionIDs)):
        eRando.ChangeStats([newEn], [("FlyHeight", 500)])   
 
def EnemyDesc(name):
    EnemyRandoDesc = PopupDescriptions.Description()
    EnemyRandoDesc.Header(name)
    EnemyRandoDesc.Text(f"{name} are the target group to be randomized.")
    EnemyRandoDesc.Text(f"The suboption for those categories are what those enemies will be randomized into.")
    EnemyRandoDesc.Text(f"The spinbox for each option is the weight of that category.")
    if name == Options.BossEnemyOption.name:
        EnemyRandoDesc.Header(Options.BossEnemyOption_Solo.name)
        EnemyRandoDesc.Text("This will balance required fights that are fought solo, by adjusting the levels of the encounter")
        EnemyRandoDesc.Header(Options.BossEnemyOption_Group.name)
        EnemyRandoDesc.Text("This will balance required fights that are large groups of enemies, by adjusting the levels of the encounter if an enemy is strong in groups.")
    if name != Options.BossEnemyOption.name:
        EnemyRandoDesc.Header(Options.NormalEnemyOption_Aggro.name)
        EnemyRandoDesc.Text("If this setting is on, enemies will keep their original aggro. For example, if a Krabble is replaced by Amalthus, it will keep the krabble's aggro type and radius.")
    EnemyRandoDesc.Header(Options.NormalEnemyOption_Size.name)
    EnemyRandoDesc.Text("This will match the size of the new enemy to the original enemy. For example, Ophion (a big enemy), when replaced with a krabble (a small enemy), will force the Krabble to match Ophions size for that instance of it. This helps with indoor areas as massive enemies will be shrunk to match their new environment.")
    return EnemyRandoDesc