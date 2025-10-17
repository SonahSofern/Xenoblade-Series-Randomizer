import json, random, copy, traceback, math
from XC2.XC2_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as e, Interactables

StaticEnemyData:list[e.EnemyGroup] = []

ValidEnemyPopFileNames = ["ma01a_FLD_EnemyPop.json", "ma02a_FLD_EnemyPop.json", "ma04a_FLD_EnemyPop.json", "ma05a_FLD_EnemyPop.json", "ma05c_FLD_EnemyPop.json", "ma07a_FLD_EnemyPop.json", "ma07c_FLD_EnemyPop.json", "ma08a_FLD_EnemyPop.json", "ma08c_FLD_EnemyPop.json", "ma10a_FLD_EnemyPop.json", "ma10c_FLD_EnemyPop.json", "ma11a_FLD_EnemyPop.json", "ma13a_FLD_EnemyPop.json", "ma13c_FLD_EnemyPop.json", "ma15a_FLD_EnemyPop.json", "ma15c_FLD_EnemyPop.json", "ma16a_FLD_EnemyPop.json", "ma17a_FLD_EnemyPop.json", "ma17c_FLD_EnemyPop.json", "ma18a_FLD_EnemyPop.json", "ma18c_FLD_EnemyPop.json", "ma20a_FLD_EnemyPop.json", "ma20c_FLD_EnemyPop.json", "ma21a_FLD_EnemyPop.json", "ma40a_FLD_EnemyPop.json", "ma41a_FLD_EnemyPop.json", "ma42a_FLD_EnemyPop.json"]
                                                                                                                                                                                                                                                                                                          
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies, isVanillaAggro, matchSize:Interactables.SubOption, balanceStats:Interactables.SubOption):
    global StaticEnemyData
    EnemyCounts = GetEnemyCounts()
    GroupFightViolations = GetGroupFightViolations()
    SoloFightViolations = GetSoloFightViolations()
    paramRev = ["ParamRev"] # https://www.xenoserieswiki.org/wiki/Module:XC2_enemy_stat
    ignoreKeys = ['$id', 'Lv', 'LvRand', 'ExpRev', 'GoldRev', 'WPRev', 'SPRev', 'DropTableID', 'DropTableID2', 'DropTableID3', 'PreciousID', 'Score', 'ECube', 'Flag', 'DrawWait', 'ZoneID', 'TimeSet', 'WeatherSet', 'DriverLev', "HpOver"] + paramRev
    aggroKeys = ['Detects', 'SearchRange', 'SearchAngle', 'SearchRadius', 'BatInterval', 'BatArea', 'BatAreaType']
    isMatchSize = matchSize.GetState()
    isBalanceStats = balanceStats.GetState()
    if isVanillaAggro:
        ignoreKeys.extend(aggroKeys)
    actKeys = ["FlyHeight", "ActType"]
    with open("XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC2/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC2/JsonOutputs/common/RSC_En.json", 'r+', encoding='utf-8') as rscFile:
                with open("XC2/JsonOutputs/common/BTL_Arts_En.json", 'r+', encoding='utf-8') as artFile:
                    paramData = json.load(paramFile)
                    rscData = json.load(rscFile)
                    eneData = json.load(eneFile)
                    artData = json.load(artFile)

                    eRando = e.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "ResourceID", "ParamID", eneData, paramData, rscData, artData, permanentBandaids=[lambda: EarthBreathNerf(), lambda: AeshmaCoreHPNerf(paramData), lambda: GortOgreUppercutRemoval(paramData)], actKeys=actKeys)

                    if StaticEnemyData == []:
                        StaticEnemyData = eRando.GenEnemyData()

                    for oldEn in eRando.arrangeData["rows"]:
                        if eRando.FilterEnemies(oldEn, targetGroup):
                            continue

                        newEn = eRando.CreateRandomEnemy(StaticEnemyData)

                        if Options.BossEnemyOption_Solo.GetState():
                            eRando.BalanceFight(oldEn, newEn, SoloFightViolations, EnemyCounts)
                        if Options.BossEnemyOption_Group.GetState():
                            eRando.BalanceFight(oldEn, newEn, GroupFightViolations, EnemyCounts)

                        if isMatchSize:
                            EnemySizeHelper(oldEn, newEn, eRando)

                        if not isMatchSize and targetGroup == IDs.BossMonsters: # Forces red rings to be gone if you dont scale bosses to avoid softlocks, you cannot hit enemies outside rings and they can spawn weird when big
                            RedRingRemoval()

                        CloneEnemiesDefeatCondition(oldEn, newEn)

                        eRando.ActTypeFix(newEn, oldEn)

                        # Blade Act Fix
                        if newEn["EnemyBladeID"] != 0:
                            for enBlade in eRando.arrangeData["rows"]:
                                if enBlade['$id'] == newEn['EnemyBladeID']:
                                    CreateBlade(enBlade, oldEn, newEn, eRando)
                                    break
                        
                        if isBalanceStats:
                            eRando.HealthBalancing(oldEn, newEn, "HpMaxRev")
                        
                        AionRoomFix(oldEn, newEn, eRando)

                        eRando.CopyKeys(oldEn, newEn, ignoreKeys) # Keep in mind this will overwrite changes made to the old enemy

                    for group in StaticEnemyData:
                        group.RefreshCurrentGroup()

                    Bandaids(eneData, isBoss, eRando) # Changes based on ID after the initial swap

                    JSONParser.CloseFile(eRando.arrangeData, eneFile)
                    JSONParser.CloseFile(eRando.paramData, paramFile)
                    JSONParser.CloseFile(eRando.rscData, rscFile)
                    JSONParser.CloseFile(eRando.artData, artFile)


def CreateBlade(enBlade, oldEn, newEn, eRando:e.EnemyRandomizer): # Because there is only 1 blade referenced for each enemy we have to create new blades (Since blades are not referenced in gimmick files it is fine)
    newBlade = copy.deepcopy(enBlade)
    newID =  len(eRando.arrangeData["rows"]) + 1
    newBlade["$id"] = newID
    eRando.arrangeData["rows"].append(newBlade)
    newEn["EnemyBladeID"] = newID
    eRando.ActTypeFix(newBlade, oldEn)
    EnemySizeHelper(oldEn, newBlade, eRando)

def RedRingRemoval():
    for name in ValidEnemyPopFileNames:
        with open(f"XC2/JsonOutputs/common_gmk/{name}", 'r+', encoding='utf-8') as popFile:
            popData = json.load(popFile)
            for pop in popData["rows"]:
                pop["battlelockname"] = 0
            JSONParser.CloseFile(popData, popFile)
        
def EnemySizeHelper(oldEn, newEn, eRando:e.EnemyRandomizer):
    Supermassive = 4
    Massive = 3
    Large = 2
    Normal = 1
    Small = 0

    # Aion, Ophion, and Siren, Nekkel Mammut (Not truly supermassive but its actual size is much bigger than its chrsize (2))
    SupermassiveEnemies = [265, 275, 1137, 1449, 1450, 1758]

    if oldEn["$id"] in SupermassiveEnemies:
        oldEn["ChrSize"] = Supermassive
    if newEn["$id"] in SupermassiveEnemies:
        newEn["ChrSize"] = Supermassive
    
    multDict = {
        (Supermassive, Massive): 3,
        (Supermassive, Large): 5,
        (Supermassive, Normal): 7,
        (Supermassive, Small): 10,
        (Massive, Large): 2,
        (Massive, Normal): 3,
        (Massive, Small): 5,
        (Large, Normal): 1,
        (Large, Small): 2,
        (Normal, Small): 1,
    }
    keys = ["Scale"]
    eRando.EnemySizeMatch(oldEn, newEn, keys, multDict)

    # Reset size if scaled higher than massive
    if oldEn["ChrSize"] > Massive:
        oldEn["ChrSize"] = Massive
    if newEn["ChrSize"] > Massive:
        newEn["ChrSize"] = Massive

def Bandaids(eneData, isBoss, eRando):
    '''Bandaids intented to be ran once'''
    ForcedWinFights([3,6])
    SummonsFix(eneData)
    if isBoss.GetState():
        TornaIntroChanges(eRando)

def GetEnemyCounts():
    enemyCounts = dict()
    # I don't want regular overworld enemies to be stronger/weaker because they spawn several of them in a pack, and
    # it's not consistent when they do that (standard Volffs are sometimes 1, sometimes 2, etc). I want to keep counts
    # only for bosses, UMs, quest enemies, etc
    BossLikeEnemies = [IDs.BossMonsters, IDs.UniqueMonsters, IDs.SuperbossMonsters]
    for name in ValidEnemyPopFileNames:
        with open(f"XC2/JsonOutputs/common_gmk/{name}", 'r+', encoding='utf-8') as popFile:
            popData = json.load(popFile)
            for row in popData["rows"]:
                # Enemies may appear as more than one enemy in the same fight. For example, the Tirkins in chapter 4
                # are separated as two groups of 3 and 1, despite being the exact same enemy
                # To account for this, we sum all the instances before adding it to the overall counter
                thisFightCount = dict()
                for i in Helper.InclRange(1,4):
                    id = row[f"ene{i}ID"]
                    count = row[f"ene{i}num"]
                    if id in BossLikeEnemies: # Valid enemy
                        thisFightCount[id] = thisFightCount.get(id, 0) + count
                for key, val in thisFightCount.items():
                    enemyCounts[key] = val

    return enemyCounts

 # Solo Fight Violations
def GetSoloFightViolations():
    soloFightIDs = [179, 182, 184, 185, 186, 187, 189, 190, 258, 260, 262, 256, 604] # Includes both 1 and 2 person party fights

    SoloUniqueMonstersViolations = e.Violation(soloFightIDs, IDs.UniqueMonsters, lvDiff=-15)
    SoloSuperbossMonstersViolations = e.Violation(soloFightIDs, IDs.SuperbossMonsters, lvDiff=-30)
    SoloBossMonsterViolations = e.Violation(soloFightIDs, IDs.BossMonsters, lvDiff=-15)
    SoloFightViolations:list[e.Violation] = [SoloUniqueMonstersViolations, SoloSuperbossMonstersViolations, SoloBossMonsterViolations]

    return SoloFightViolations

# Group Fight Violations 
def GetGroupFightViolations():
    Default_Params = [
        e.ParamModification(['StrengthRev', 'PowEtherRev']),
        e.ParamModification(['HpMaxRev'], C=0.7)
    ]
    Default = e.Violation([], [], Default_Params)

    # Note: The following were checked explicitly and I don't think they need nerfing besides the universal nerfs, so they're not listed below:
    # - Malos w/ Sever
    # - Patroka (both w/ Perdido and with her lance)
    # - Mikhail (both w/ Cressidus and with his fans)
    # - Aeshma's Core (Phase 1 might need the healing re-evaluated though)
    # - Amalthus (Though we should keep an eye on Domination)
    # - Slithe Jagron
    #
    # The following nerfs are currently implemented:
    # - Akhos w/ Obrona: cooldown of Checkmate
    # - Akhos w/ bow: cooldown of Black Wave and White Wave
    # - Jin: cooldown of Skyward Slash
    # - Malos w/ Monado: cooldown of Monado Cyclone, Monado Jail, and Monado Eater
    Akhos_Obrona = e.Violation([], [206, 212, 267], Default_Params, [e.ArtModification(['ArtsNum3'], ['Recast'], isReciprocal=True)])
    Akhos_Bow = e.Violation([], [238], Default_Params,[e.ArtModification(['ArtsNum3', 'ArtsNum4'], ['Recast'], isReciprocal=True)])
    Jin = e.Violation([], [231, 241, 244, 272, 253], Default_Params, [e.ArtModification(['ArtsNum2'], ['Recast'], isReciprocal=True)])
    Malos_Monado = e.Violation([], [243, 245, 273, 1443, 1446, 1447], Default_Params, [e.ArtModification(['ArtsNum3', 'ArtsNum4', 'ArtsNum6'], ['Recast'], isReciprocal=True)])
    Aion = e.Violation([], [265, 275], [
        e.ParamModification(['StrengthRev', 'PowEtherRev']),
        e.ParamModification(['HpMaxRev'], C=0.7, K=1) # Much heavier HP scaling based on number of enemies
    ])

    return [Default, Akhos_Obrona, Akhos_Bow, Jin, Malos_Monado, Aion]

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
    
# def EnemyAggro(): # Not going to add aggro to enemies because it would be disproportional to the area there enemy is in. For example if i tgive them batArea and a large area you could get stuck inside a small area (ship) with enemies perma aggroing you
#     odds = Options.EnemyAggroOption.GetSpinbox()
#     with open(f"XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as eneFile:
#         eneData = json.load(eneFile)
#         for en in eneData["rows"]:
#             if not Helper.OddsCheck(odds):
#                 continue
#             if en["$id"] in IDs.BossMonsters:
#                 continue
#             en["Detects"] = 0
#         JSONParser.CloseFile(eneData, eneFile)

    
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
    EnemyRandoDesc.Header(Options.NormalEnemyOption_Stats.name)
    EnemyRandoDesc.Text("This balances stats (mainly HP) for all fights of this category. Hp varies greatly in XC2 and this helps counterract that.")
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