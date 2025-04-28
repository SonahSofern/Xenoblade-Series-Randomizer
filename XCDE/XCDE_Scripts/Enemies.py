
import json, random, Options, IDs, copy, traceback, math
from scripts import Helper, JSONParser
class Enemy:
    def __init__(self, enelistArea, enelist):
        self.eneListArea = enelistArea
        self.enelist = enelist

# Dummy = [296, 329, 330, 331, 332, 333, 343, 651, 1204, 1206, 1329, 1548, 1625, 1626, 2602, 2603]
# BadEnemies = [220, 1154, 1157, 2403, 2406, 2413, 2750, 2906, 2908, 2909] + Helper.InclRange(370,388) + Helper.InclRange(930,997)+ Helper.InclRange(1131,1195)+ Helper.InclRange(1239, 1300)+ Helper.InclRange(701,778)+ Helper.InclRange(1769,1799)+ Helper.InclRange(1850,1897)

def Enemies():
    MechonFamily = [1,2,4] # 4 Seems to share a lot of enemies that are aquatic, but mukhar is family 4 and we dont want him early so it cuts a few enemies off that we mightve wanted otherwise oh well
    TelethiaFamily = 9
    BadForMechon = [30, 31, 32,33, 63, 64, 65] # List of ids for the early game to make sure mechon arent placed here
    BadForTelethia = [30,31,61,62, 134, 265, 266, 268, 416, 417, 534] # Ids for early game so you dont get soul readed
    NormalEnemies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 41, 43, 52, 53, 55, 56, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 101, 102, 103, 104, 105, 106, 108, 109, 110, 115, 116, 117, 118, 119, 120, 121, 122, 123, 126, 127, 128, 129, 130, 132, 133, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 165, 166, 167, 168, 169, 170, 171, 173, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 267, 269, 280, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 297, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 319, 320, 321, 322, 323, 324, 326, 327, 328, 335, 336, 337, 340, 341, 342, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 418, 419, 420, 421, 422, 426, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 549, 550, 551, 552, 553, 554, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 649, 650, 800, 901, 902, 903, 904, 908, 909, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1055, 1057, 1059, 1060, 1061, 1062, 1063, 1064, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1201, 1202, 1203, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1450, 1451, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1536, 1537, 1547, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1617, 1618, 1619, 1620, 1621, 1623, 1624, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1734, 1735, 1736, 1737, 1738, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1915, 1916, 1917, 1918, 1919, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2118, 2119, 2120, 2121, 2122, 2132, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2228, 2229, 2230, 2231, 2232, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2310, 2311, 2313, 2314, 2401, 2402, 2404, 2405, 2409, 2410, 2412, 2504, 2506, 2507, 2508, 2701, 2702, 2703, 2704, 2705, 2706, 2707, 2708, 2709, 2710, 2711, 2712, 2713, 2714, 2715, 2718, 2719, 2720, 2721, 2722, 2723, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2741, 2742, 2763, 2764, 2765, 2766, 2767, 2768, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2784, 2785, 2786, 2787, 2788, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844, 2845, 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2867, 2868, 2869, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2901, 2902, 2903, 2904, 2905, 2907, 2910, 2911, 2922, 2923, 2924, 2925, 2926, 2927, 2928, 2929, 2932, 3051, 3052, 3053, 3054, 3055, 3056, 3095, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105, 3106, 3151, 3152, 3153, 3154, 3155, 3156, 3201, 3202, 3203, 3204, 3205, 3251, 3252, 3253, 3254, 3255, 3256, 3301, 3302, 3303, 3304, 3305, 3306, 3351, 3352, 3353, 3354, 3401, 3402, 3451, 3452, 3453, 3454, 3455, 3456, 3457, 3501, 3502, 3503, 3504, 3505]
    UniqueEnemies = [34, 36, 37, 38, 40, 42, 44, 45, 46, 47, 48, 49, 50, 51, 111, 112, 113, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 281, 282, 283, 284, 317, 318, 423, 424, 425, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 910, 911, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1452, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1614, 1615, 1616, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1920, 1921, 1922, 1923, 1924, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2724, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762]
    BossEnemies = [30,31,61,62, 134, 265, 266, 268, 416, 417, 534, 636, 637,638, 907, 906, 905, 1039, 1205, 1436, 1535, 1622, 1914, 2115, 2116, 2117, 2123, 2218 ,2501, 2505, 2601, 339, 338, 2309, 1326, 1328, 1327, 1315, 1316, 1317, 1538, 2407, 2408, 2411]
    SuperbossEnemies = [1438, 1733, 548, 1448, 1449]
    
    isNormal = Options.EnemyOption_Normal.GetState()
    isUnique = Options.EnemyOption_Unique.GetState()
    isBoss = Options.EnemyOption_Boss.GetState()
    isSuper = Options.EnemyOption_Superboss.GetState()
    isMixed = Options.EnemyOption_MixTypes.GetState()
    isDupe = Options.EnemyOption_Duplicates.GetState()
    
    ChosenEnemyIds = []
    if isNormal:
        ChosenEnemyIds.extend(NormalEnemies)
    if isUnique:
        ChosenEnemyIds.extend(UniqueEnemies)
    if isBoss:
        ChosenEnemyIds.extend(BossEnemies)
    if isSuper:
        ChosenEnemyIds.extend(SuperbossEnemies)
        
    CombinedNormalEnemyData:list[Enemy] = []
    CombinedUniqueEnemyData:list[Enemy] = []
    CombinedBossEnemyData:list[Enemy] = []
    CombinedSuperbossEnemyData:list[Enemy] = []
    # "run_speed" Do NOT include run speed it lags the game to 1 fps "detects", "assist", "search_range", "search_angle",
    CopiedStats = ["move_speed", "frame", "size", "scale", "family","elem_phx", "elem_eth", "anti_state", "resi_state", "elem_tol", "elem_tol_dir", "down_grd", "faint_grd", "front_angle", "avoid", "delay", "hit_range_far", "dbl_atk", "cnt_atk", "chest_height", "spike_elem", "spike_type", "spike_range", "spike_dmg", "spike_state", "spike_state_val", "atk1", "atk2", "atk3", "arts1", "arts2", "arts3", "arts4", "arts5", "arts6", "arts7", "arts8"]
    CopiedStatsWithRatios = ["hp", "str", "eth", "Lv_up_hp", "Lv_up_str", "Lv_up_eth"] # Not doing agility its too finicky and scales slowly compared to the other stats
    CopiedInfo = ["name", "resource", "c_name_id", "mnu_vision_face"]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/BTL_enelist.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)    

        # Create our list of enemies from all the area files and Combine the data into the class
        for file in IDs.areaFileListNumbers:
            try:   
                with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                    eneAreaData = json.load(eneAreaFile)
                    for enemy in eneAreaData["rows"]:
                        if enemy["$id"] not in ChosenEnemyIds: # Ignore non chosen enemies
                            continue
                        for en in eneData["rows"]:
                            enID = en["$id"]
                            if enID == enemy["$id"]:
                                enemyCopy = copy.copy(enemy)
                                enCopy = copy.copy(en)
                                newEnemy = Enemy(enemyCopy, enCopy)
                                if enID in NormalEnemies:
                                    CombinedNormalEnemyData.append(newEnemy)
                                elif enID in BossEnemies:
                                    CombinedBossEnemyData.append(newEnemy)
                                elif enID in UniqueEnemies:
                                    CombinedUniqueEnemyData.append(newEnemy)
                                elif enID in SuperbossEnemies:
                                    CombinedSuperbossEnemyData.append(newEnemy)
                                # PrintEnemy(newEnemy)
                                break   
                    JSONParser.CloseFile(eneAreaData, eneAreaFile)
            except:
                continue   
        # Randomly assign enemies     
        for file in IDs.areaFileListNumbers:
            try:   
                with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/VoEnemy.json", 'r+', encoding='utf-8') as eneVoiceFile:
                        eneVoiceData = json.load(eneVoiceFile)
                        eneAreaData = json.load(eneAreaFile)
                        for enemy in eneAreaData["rows"]:   
                            

                            if enemy["$id"] not in ChosenEnemyIds: # Only want to replace enemies chosen from our groups
                                continue
                            
                            enID = enemy["$id"]
                            
                            if isMixed:
                                group = CombinedNormalEnemyData + CombinedUniqueEnemyData + CombinedSuperbossEnemyData + CombinedBossEnemyData
                            elif enID in NormalEnemies:
                                group = CombinedNormalEnemyData
                            elif enID in BossEnemies:
                                group = CombinedBossEnemyData
                            elif enID in UniqueEnemies:
                                group = CombinedUniqueEnemyData
                            elif enID in SuperbossEnemies:
                                group = CombinedSuperbossEnemyData
                                
                            chosen = random.choice(group) # Choose from the desired pool                     
                            
                            # Telethia Early
                            if (enemy["$id"] in BadForTelethia) and (chosen.eneListArea["family"] == TelethiaFamily):
                                for i in range(1,9):
                                    if chosen.eneListArea[f"arts{i}"] == 666:
                                        chosen.eneListArea[f"arts{i}"] = 0# Remove soul read if we get an early telethia
                        
                            # Mechon Early
                            while (enemy["$id"] in BadForMechon) and (chosen.eneListArea["family"] in MechonFamily):
                                chosen = random.choice(group) # Rechoose if we get an early mechon
                                # print("Stopped mechon")

                            # Fix voice lines
                            for voiceID in eneVoiceData["rows"]:
                                if chosen.enelist["$id"] == voiceID["enemy"]: # If the chosen enemy has a voice
                                    voiceID["enemy"] = enemy["$id"] # Set the ID
                                    break    
                                
                                
                            # Balance spikes
                            SpikeBalancer(enemy, chosen.eneListArea)
                            
                            # Copy stats with ratios to original stats
                            replacementTotalStats = TotalStats(chosen.eneListArea, CopiedStatsWithRatios)
                            originalTotalStats = TotalStats(enemy, CopiedStatsWithRatios)
                            # print("\n") 
                            # print(f"ID {enemy["$id"]} Replaced With ID {chosen.eneListArea["$id"]} Stat Total: {originalTotalStats}")
                            
                            # Copy chosen stats over
                            for key in CopiedStats: 
                                enemy[key] = chosen.eneListArea[key]

                            for key in CopiedStatsWithRatios:
                                enemy[key] = KeepStatRatio(enemy, chosen.eneListArea, key, replacementTotalStats, originalTotalStats)
                                
                            for ene in eneData["rows"]:
                                if (ene["$id"] == enID):
                                    for key in CopiedInfo:
                                        ene[key] = chosen.enelist[key]
                                    break
                                
                                            
                            if (not isDupe): # Remove enemy if player wants 1 to 1
                                group.remove(chosen)
                        JSONParser.CloseFile(eneVoiceData, eneVoiceFile)
                        JSONParser.CloseFile(eneAreaData, eneAreaFile)  

            except Exception as error:
                pass
                # print(f"{traceback.format_exc()}") # shows the full error
        JSONParser.CloseFile(eneData, eneFile)
        RingRemoval() 
    
def SpikeBalancer(enemy, chosen): # spike damage is 10x the spike_dmg value
    if chosen["spike_dmg"] != 0:
        spikePerLv = 0.7 # base spike given per level
        expectedPowerLv = chosen["lv"] * spikePerLv # The expected power level of the spike before any changes
        actualPowerLv = chosen["spike_dmg"]
        spikeMult = actualPowerLv/expectedPowerLv # If enemy has a stronger/weaker spike than something of its level make the spike stronger/weaker but still balanced
        newPowerLv = int(enemy["lv"] * spikeMult)
        chosen["spike_dmg"] = max(min(newPowerLv, 255), 1) # Set the new amount between 1 and 255
        # print(f"Level: {enemy["lv"]}")
        # print(f"Spike Damage: {chosen["spike_dmg"] * 10}")
    if (chosen["spike_state_val"] == 220) and (enemy["lv"] <= 60): # Removes instant death spikes from all fights below level 60
        chosen["spike_state_val"] = 0
        


def TotalStats(chosen, keys):
    total = 0
    for key in keys:
        total += chosen[key]
    return total    
    
def KeepStatRatio(enemy, chosen, key, replacementTotal, originalTotal):
    ratio = chosen[key]/replacementTotal
    origStat = enemy[key]
    newStat = min(math.ceil((ratio*originalTotal)), 65535)
    # print(f"{key}: {origStat} - {newStat}")
    return newStat

# dummylist = []
def PrintEnemy(enemy:Enemy):
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/BTL_enelist_ms.json", 'r+', encoding='utf-8') as enNamesFile:
        with open(f"./XCDE/_internal/JsonOutputs/bdat_common_ms/ene_arts_ms.json", 'r+', encoding='utf-8') as enArtNamesFile:
            with open(f"./XCDE/_internal/Enemies.txt", 'a', encoding='utf-8') as enemyTXT:
                enemyNameData = json.load(enNamesFile)
                enemyArtNameData = json.load(enArtNamesFile)

                for name in enemyNameData["rows"]:
                    if enemy.enelist["name"] == name["$id"]:
                        # if "Dummy" in name["name"]:#  used to weed out dummy enemies
                        #     dummylist.append(enemy.enelist["$id"])
                        # print(f"Name: {name['name']}")
                        enemyTXT.write(f" Name: {name['name']} ")
                        break
                for name in enemyArtNameData["rows"]:
                    for i in range(1,9):
                        if enemy.eneListArea[f"arts{i}"] == name["$id"]:
                            # print(f"Art {i}: {name['name']}")
                            enemyTXT.write(f" Art {i}: {name['name']} ")
                            break
                enemyTXT.write("\n")
        #     enArtNamesFile.seek(0)
        #     enArtNamesFile.truncate()
        #     json.dump(enemyArtNameData, enArtNamesFile, indent=2, ensure_ascii=False)
        # enNamesFile.seek(0)
        # enNamesFile.truncate()
        # json.dump(enemyNameData, enArtNamesFile, indent=2, ensure_ascii=False)
    
    # with open(f"./XCDE/_internal/Enemies.txt", 'a', encoding='utf-8') as enemyTXT: # Clear our enemies file
    #     enemyTXT.seek(0)
    #     enemyTXT.truncate()

# Used for starting fight had some weird thing with the enemies
def RingRemoval():
    RemoveLocks = [2]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_ma1401/FieldLock1401.json", 'r+', encoding='utf-8') as lockFile:
        lockData = json.load(lockFile)
        for lock in lockData["rows"]:
            if lock["$id"] in RemoveLocks:
                lock["popID1"] = 0
                lock["popID2"] = 0
        JSONParser.CloseFile(lockData, lockFile)