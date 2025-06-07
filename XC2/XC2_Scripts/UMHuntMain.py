import json, random, IDs, EnemyRandoLogic, RaceMode, math, Options, time, FieldSkillAdjustments, UMHuntDebugFunctions, UMHuntShopCreation, TutorialShortening
from Enhancements import *
from BladeRandomization import Replacement2Original
from scripts import Helper, JSONParser, PopupDescriptions

#Keeping these 3 separate from the already existing IDs in EnemyRandoLogic in case I want to do some balancing or something
AllUniqueMonsterDefaultIDs = [611, 612, 705, 706, 707, 708, 709, 710, 711, 712, 713, 715, 736, 738, 808, 809, 810, 811, 812, 814, 815, 816, 817, 819, 890, 891, 892, 893, 894, 895, 896, 898, 899, 926, 929, 953, 954, 955, 957, 958, 1019, 1020, 1023, 1025, 1026, 1101, 1102, 1104, 1106, 1108, 1109, 1111, 1112, 1113, 1114, 1115, 1131, 1132, 1134, 1155, 1156, 1157, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1255, 1256, 1258, 1260, 1261, 1262, 1264, 1265, 1563, 1564, 1566, 1567, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1670, 1774]
AllSuperBossDefaultIDs = [247, 714, 928, 1022, 1027, 1110, 1135, 1137, 1189, 1559, 1560, 1561, 1562, 1723, 1756, 1758, 1759, 1763, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1775, 1776, 1777, 1778, 1779, 1783, 1784, 1785, 1786, 1792, 1793, 1794, 1795, 1800, 1802, 1803, 1804, 1808, 1809, 1811, 1812, 1813, 1814, 1886]
AllNormalEnemyDefaultIDs = [313, 315, 339, 413, 476, 521, 523, 555, 568, 630, 631, 632, 633, 634, 638, 645, 646, 647, 648, 651, 652, 653, 655, 656, 659, 660, 662, 664, 665, 666, 668, 675, 676, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 691, 692, 694, 695, 699, 701, 703, 716, 717, 718, 719, 720, 721, 722, 723, 729, 730, 731, 732, 734, 749, 756, 757, 758, 762, 763, 764, 766, 771, 772, 773, 774, 794, 795, 796, 798, 800, 802, 804, 806, 825, 835, 843, 844, 847, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 865, 867, 868, 869, 870, 872, 873, 874, 875, 876, 877, 879, 880, 881, 882, 884, 886, 888, 901, 902, 903, 904, 905, 906, 907, 908, 909, 911, 912, 913, 914, 915, 916, 917, 918, 919, 922, 924, 931, 933, 937, 940, 941, 942, 945, 950, 951, 952, 959, 960, 961, 962, 963, 974, 977, 978, 979, 980, 981, 983, 989, 990, 991, 992, 994, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1015, 1016, 1017, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1050, 1051, 1060, 1061, 1063, 1064, 1069, 1070, 1072, 1073, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1098, 1100, 1127, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1171, 1176, 1177, 1178, 1190, 1191, 1192, 1193, 1194, 1195, 1198, 1208, 1209, 1213, 1214, 1217, 1221, 1222, 1228, 1232, 1233, 1235, 1241, 1251, 1254, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1276, 1277, 1279, 1281, 1282, 1283, 1284, 1286, 1287, 1288, 1320, 1321, 1322, 1324, 1326, 1329, 1366, 1380, 1396, 1399, 1421, 1455, 1456, 1459, 1460, 1461, 1462, 1463, 1464, 1466, 1473, 1474, 1476, 1477, 1478, 1479, 1483, 1487, 1488, 1496, 1498, 1500, 1501, 1503, 1507, 1508, 1511, 1513, 1515, 1522, 1529, 1530, 1531, 1532, 1535, 1536, 1539, 1541, 1542, 1543, 1544, 1545, 1547, 1550, 1565, 1570, 1571, 1572, 1573, 1574, 1577, 1578, 1580, 1582, 1583, 1584, 1586, 1587, 1588, 1590, 1591, 1595, 1597, 1600, 1601, 1603, 1606, 1608, 1609, 1611, 1612, 1613, 1617, 1622, 1623, 1624, 1625, 1626, 1627, 1629, 1630, 1631, 1635, 1636, 1637, 1638, 1639, 1640, 1642, 1643, 1645, 1646, 1647, 1649, 1650, 1652, 1656, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1728, 1729, 1730, 1732, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1757, 1760, 1761, 1762, 1764, 1780, 1781, 1782, 1790, 1791, 1796, 1797, 1798, 1799, 1801, 1810, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1882, 1884]
AllQuestDefaultEnemyIDs = [303, 304, 305, 307, 308, 309, 310, 318, 319, 320, 323, 324, 325, 326, 329, 332, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 356, 359, 365, 367, 369, 372, 373, 374, 375, 376, 383, 384, 385, 386, 389, 390, 391, 392, 393, 394, 395, 396, 399, 401, 403, 404, 405, 406, 407, 409, 411, 414, 415, 418, 436, 437, 445, 446, 447, 448, 450, 451, 454, 455, 456, 457, 458, 459, 461, 462, 463, 464, 466, 468, 470, 475, 477, 479, 481, 483, 485, 487, 488, 489, 490, 491, 492, 493, 495, 496, 497, 498, 500, 501, 503, 504, 506, 508, 510, 512, 513, 515, 517, 519, 525, 532, 533, 534, 535, 536, 538, 540, 542, 544, 546, 547, 548, 549, 550, 551, 552, 553, 557, 558, 559, 560, 561, 562, 563, 565, 566, 569, 570, 571, 572, 573, 576, 577, 578, 579, 581, 583, 588, 591, 593, 598, 600, 601, 602, 603, 604, 607, 608, 609, 610, 613, 640, 641, 642, 644, 649, 663, 667, 673, 740, 742, 744, 746, 750, 751, 752, 759, 760, 761, 778, 780, 782, 784, 785, 786, 787, 788, 789, 790, 791, 824, 827, 828, 829, 832, 833, 834, 837, 838, 839, 840, 848, 930, 934, 935, 939, 946, 947, 948, 949, 964, 965, 967, 970, 975, 984, 985, 996, 1035, 1036, 1041, 1053, 1054, 1058, 1059, 1066, 1074, 1075, 1076, 1077, 1078, 1093, 1094, 1095, 1096, 1097, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1128, 1145, 1147, 1148, 1151, 1152, 1153, 1154, 1158, 1159, 1160, 1162, 1164, 1167, 1168, 1169, 1172, 1173, 1174, 1196, 1197, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1212, 1215, 1223, 1226, 1229, 1230, 1231, 1236, 1237, 1238, 1239, 1240, 1242, 1245, 1246, 1248, 1249, 1250, 1343, 1344, 1345, 1348, 1386, 1387, 1388, 1389, 1391, 1393, 1395, 1397, 1398, 1400, 1402, 1404, 1405, 1406, 1407, 1408, 1410, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1422, 1423, 1424, 1425, 1457, 1458, 1465, 1467, 1468, 1469, 1470, 1471, 1472, 1482, 1484, 1485, 1486, 1489, 1490, 1491, 1497, 1499, 1502, 1512, 1516, 1518, 1519, 1526, 1527, 1528, 1534, 1537, 1540, 1546, 1548, 1549, 1551, 1575, 1576, 1579, 1581, 1585, 1589, 1592, 1594, 1596, 1598, 1602, 1604, 1605, 1607, 1610, 1614, 1616, 1618, 1619, 1621, 1628, 1634, 1644, 1648, 1651, 1653, 1655, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1686, 1687, 1688, 1689, 1690, 1888]
AllBossDefaultIDs = [179, 180, 181, 182, 184, 185, 186, 187, 189, 190, 191, 193, 195, 196, 197, 198, 199, 201, 202, 203, 204, 206, 208, 210, 212, 214, 216, 217, 219, 220, 221, 222, 223, 225, 227, 229, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 248, 249, 250, 251, 252, 253, 254, 266, 267, 268, 269, 270, 271, 274, 1342, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1448, 1454, 1632, 1733, 1746, 1747, 1748, 1749, 1754, 1755]
UnusedNormalValidEnemyDefaultIDs = [339, 413, 568, 630, 631, 632, 633, 634, 683, 716, 717, 718, 719, 720, 721, 722, 758, 901, 902, 903, 904, 905, 907, 937, 959, 960, 961, 962, 963, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1190, 1191, 1192, 1193, 1194, 1195, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1276, 1277, 1279, 1281, 1282, 1283, 1284, 1286, 1287, 1288, 1322, 1324, 1366, 1380, 1396, 1421, 1455, 1456, 1459, 1460, 1461, 1462, 1463, 1464, 1466, 1473, 1474, 1476, 1477, 1478, 1479, 1483, 1487, 1488, 1496, 1498, 1500, 1501, 1503, 1507, 1508, 1511, 1513, 1515, 1522, 1529, 1530, 1531, 1532, 1535, 1536, 1539, 1541, 1542, 1543, 1544, 1545, 1547, 1550, 1565, 1570, 1571, 1572, 1573, 1574, 1577, 1578, 1580, 1582, 1583, 1584, 1586, 1587, 1588, 1590, 1591, 1595, 1597, 1600, 1601, 1603, 1606, 1608, 1609, 1611, 1612, 1613, 1617, 1622, 1623, 1624, 1625, 1626, 1627, 1629, 1630, 1631, 1635, 1636, 1637, 1638, 1639, 1640, 1642, 1643, 1645, 1646, 1647, 1649, 1650, 1652, 1656, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1728, 1729, 1730, 1732, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1757, 1760, 1761, 1762, 1764, 1780, 1781, 1782, 1790, 1791, 1796, 1797, 1798, 1799, 1801, 1810, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1882, 1884]

# "Location": [Warp Cutscene, "chgEdID", Map Name, Map ID]
ContinentInfo = {"Gormott": [10043, 10044, "ma05a", 6], "Uraya": [10088, 10079, "ma07a", 9], "Mor Ardain": [10156, 10149, "ma08a", 10], "Leftheria": [10197, 10192, "ma15a", 14], "Temperantia": [10233, 10224, "ma10a", 11], "Tantal": [10272, 10269, "ma13a", 13], "Spirit Crucible": [10325, 10323, "ma16a", 15], "Cliffs of Morytha": [10351, 10345, "ma17a", 16], "Land of Morytha": [10369, 10363, "ma18a", 18], "World Tree": [10399, 10393, "ma20a", 20]}

TotalAreaPool = ["Gormott", "Uraya", "Mor Ardain", "Leftheria", "Temperantia", "Tantal", "Spirit Crucible", "Cliffs of Morytha", "Land of Morytha", "World Tree"]

# "Driver": ["scriptName", "scriptStartID"]
PartyMembersAddScripts = {"Tora": ["chapt02", 7], "Nia": ["chapt02", 9], "Morag": ["chapt05", 7], "Zeke": ["chapt06", 5]}

# Misc IDs

ValidRandomizeableBladeIDs = [1001, 1002, 1008, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1050, 1104, 1105, 1106, 1107, 1108, 1109, 1111]

# TO DO

# Known Issues: 
# Poppiswap is going to be fucked up with custom enhancements

def UMHunt():
    if not Options.ShortcutsOption.GetState(): # we want to always run the tutorial shortening, otherwise it breaks stuff. spent 2 hours trying to figure out why completely unrelated changes were bricking my save file
        TutorialShortening.ShortenedTutorial()
    elif not Options.ShortenTutorialOption.GetState():
        TutorialShortening.ShortenedTutorial()
    UMHuntShopCreation.CreateShopDictionaries()
    global SetCount, UMHuntDisableCondListID, UMHuntEnableCondListIDs
    SetCount = Options.UMHuntOption.GetSpinbox()
    UMHuntDisableCondListID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    UMHuntEnableCondListIDs = Helper.ExtendListtoLength([UMHuntDisableCondListID + 1], 10, "inputlist[i-1] + 1")
    ChosenAreaOrder = []
    GetDifficulty()
    CheckForSuperbosses()
    ChosenAreaOrder.extend(random.sample(TotalAreaPool, SetCount))
    #UMHuntDebugFunctions.DebugFindMonsters(ChosenAreaOrder)
    PartyMemberstoAdd = PartyMemberAddition()
    AreaUMs, AllAreaMonsters = CustomEnemyRando(ChosenAreaOrder)
    EnemySets = ChosenEnemySets(AreaUMs)
    WarpManagement(ChosenAreaOrder, PartyMemberstoAdd, EnemySets)
    CHR_EnArrangeAdjustments(AllAreaMonsters, EnemySets, ChosenAreaOrder)
    LandmarkAdjustments(ChosenAreaOrder)
    UMHuntShopCreation.ReAddFileGlobals(SetCount, UMHuntDisableCondListID, UMHuntEnableCondListIDs, ChosenDifficulty, ExtraSuperbosses, SuperbossCount, ChosenSuperbosses, SuperbossMaps, OneScenarioConditionList)
    UMHuntShopCreation.CreateNewReceipts()
    NoUnintendedRewards(ChosenAreaOrder)
    SpiritCrucibleEntranceRemoval()
    UMHuntShopCreation.ShopChanges(ChosenAreaOrder)
    BladeTrustRequirementChanges()
    PoppiswapCostChanges()
    MoveSpeedDeedSetup()
    LureRadiusDeedSetup()
    BalanceChanges(ChosenAreaOrder)
    RandomLandmarkCreation()
    CustomEnemyDrops(EnemySets)
    if ExtraSuperbosses:
        OhBoyHereWeGoAgain()
    Cleanup()
    UMHuntMenuTextChanges()
    #UMHuntDebugFunctions.DebugItemsPlace() # currently doesnt matter since I hide all the argentum chests anyways
    #UMHuntDebugFunctions.DebugEasyMode()
    #UMHuntDebugFunctions.DebugSpawnCountPrint(EnemySets, ChosenAreaOrder)
    #UMHuntDebugFunctions.DebugEnemyLevels(ChosenAreaOrder)

def GetDifficulty(): # Gets the difficulty chosen
    global ChosenDifficulty
    #if Options.UMHuntOption_DifficultyHard.GetState():
    #    ChosenDifficulty = "Hard"
    #elif Options.UMHuntOption_DifficultyNormal.GetState():
    #    ChosenDifficulty = "Normal"
    #else:
    ChosenDifficulty = "Easy"

def CheckForSuperbosses():
    global ExtraSuperbosses
    global SuperbossCount
    if (Options.UMHuntOption_SuperbossWave.GetState()) & (SetCount == 10):
        ExtraSuperbosses = True
        SuperbossCount = 5
    else:
        ExtraSuperbosses = False
        SuperbossCount = 0

def Cleanup():
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 25:
                row["PRTQuestID"] = 6
                row["FlagPRT"] = 0
            if row["$id"] == 15: # Talking to Spraine, this doesnt work with the Quest Flags turned off
                row["NextQuestA"] = 234
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    JSONParser.ChangeJSONLineInMultipleSpots(["common/EVT_listBf.json"], [10013], ["nextID", "scenarioFlag", "nextIDtheater"], [10464, 10009, 10464])
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", ["DefAcce", "DefWP", "DefSP"], 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", ["DefLv"], 10)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", ["DefWPType", "DefLvType"], 1)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", ["DefSPType"], 2)
    GimmickAdjustments()

def BalanceChanges(ChosenAreaOrder): # Moved to reduce clutter, doesn't matter order for these
    PneumaNerfs()
    SpiritCrucibleNerfs(ChosenAreaOrder)
    RaceMode.SecondSkillTreeCostReduc()
    BladeDefaultWeapons()

def GimmickAdjustments():
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_DoorGimmick.json", ["Condition"], 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_JumpGimmick.json", ["Condition"], 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_MapGimmick.json", ["Condition", "OP_Condition"], 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_ElevatorGimmick.json", ["OP_Condition"], 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_EffectPop.json", ["Condition", "QuestFlagMin", "QuestFlagMax"], 0)
    if not Options.RemoveFieldSkillsOption.GetState(): # if this isn't already enabled, turn it on. We need to remove all field skill checks for this mode.
        FieldSkillAdjustments.RemoveFieldSkills()
    with open("./XC2/_internal/JsonOutputs/common/FLD_LODList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [115, 117, 211, 226]: # door blocking gormott titan battleship hangar, door blocking gormott titan rest of battleship door in urayan titan's head that blocks off Vampire Bride Marion, Ether Gust Wall thingy in Uraya (it gets dispelled mid-cutscene, unlike the one in Gormott)
                row["flag"]["Visible"] = 0
                row["ScenarioFlagMin1"] = 1001
                row["ScenarioFlagMax1"] = 10048
                row["QuestFlag1"] = 0
                row["QuestFlagMin1"] = 0
                row["QuestFlagMax1"] = 0
                #row["LODID"] = 0 # when this is enabled, you can fall through the floor if you target the wrong ids lol
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BladeDefaultWeapons(): # Always make the default weapons for a blade the primitive versions
    Rank1Wpns = Helper.FindValues("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", ["Rank"], [1], "$id")
    ValidRank1WeaponIDs = [x for x in Rank1Wpns if x not in Helper.FindValues("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", ["Name"], [0], "$id") + [5970]]
    Rank1Types = Helper.FindValues("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", ["$id"], ValidRank1WeaponIDs, "WpnType")
    Rank1DefWeapons = {}
    for j in range(0, len(Rank1Types)):
        for i in range(1, max(Rank1Types) + 1):
            if Rank1Types[j] == i:
                Rank1DefWeapons[i] = ValidRank1WeaponIDs[j]
                break
    with open("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as file: # Changes default weapon to a rank 1 weapon
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ValidRandomizeableBladeIDs:
                try:
                    row["DefWeapon"] = Rank1DefWeapons[row["WeaponType"]]
                except:
                    pass
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PneumaNerfs(): # Mods, break her kneecaps
    with open("./XC2/_internal/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 5970:
                row["Damage"] = 1 # Nerfing her base damage to 1 seems good enough, you can still use her for elemental combos, but it wont do much damage. The utility is still nice, but won't let you cheese a fight
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SpiritCrucibleNerfs(ChosenAreaOrder): # Spirit Crucible is way too oppressive when the unique monsters can be so strong
    if "Spirit Crucible" in ChosenAreaOrder[:3]: # if spirit crucible is one of the first 3 chosen areas, no affinity or art restrictions
        Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_MapRev.json", ["KizunaCap"], 1000)
        Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_MapRev.json", ["ArtSp"], 3)  
    elif "Spirit Crucible" in ChosenAreaOrder[:6]: # if spirit crucible is in areas 4->6, nerfs to art restrictions
        Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_MapRev.json", ["KizunaCap"], 1000)

def MoveSpeedDeedSetup(): # We add the movespeed deed to the inventory via DLC, codewise it's located with the RandomLandmarkCreation code
    CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    BonusMovespeed = 500
    with open("./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 25249:
                row["Name"] = CurrentNameID
                row["Caption"] = CurrentNameID + 1 # Increases running speed by 500%
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Value"] = BonusMovespeed
                row["Type"] = 1
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max movespeed bonus to 750%
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                row["Max"] = 750
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        data["rows"].append({"$id": CurrentNameID, "style": 36, "name": "Movespeed Deed"})
        data["rows"].append({"$id": CurrentNameID + 1, "style": 61, "name": f"Increases running speed by {BonusMovespeed}%."})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def LureRadiusDeedSetup(): # increases lure radius, adds lure radius up deed to starting inventory
    CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    BonusLureDistance = 50
    with open("./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes caption and name
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 25250:
                row["Name"] = CurrentNameID
                row["Caption"] = CurrentNameID + 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonus.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 2:
                row["Value"] = BonusLureDistance
                row["Type"] = 11
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_OwnerBonusParam.json", 'r+', encoding='utf-8') as file: # Changes max lure range to 50(m?)
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 11:
                row["Max"] = 50
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        data["rows"].append({"$id": CurrentNameID, "style": 36, "name": "Lure Range Deed"})
        data["rows"].append({"$id": CurrentNameID + 1, "style": 61, "name": f"Increases lure range by {BonusLureDistance}."})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def OhBoyHereWeGoAgain():
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # Adjusts the levels of the superbosses
        data = json.load(file)
        for i in range(0, len(ChosenSuperbosses)):
            for row in data["rows"]:
                if row["$id"] == ChosenSuperbosses[i]:
                    row["Lv"] = 115 + i*10
                    if row["Scale"] < 35:
                        row["Scale"] = 35
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def WarpManagement(ChosenAreaOrder, PartyMemberstoAdd, EnemySets): # Main function was getting a bit too cluttered
    if ExtraSuperbosses:
        EnemyGroupSetup()
    EventSetup(ChosenAreaOrder, PartyMemberstoAdd)
    EventChangeSetup(ChosenAreaOrder)
    QuestListSetup(ChosenAreaOrder)
    QuestTaskSetup(EnemySets)
    FieldQuestBattleSetup(EnemySets)
    FieldQuestTaskLogSetup(EnemySets)
    AddQuestConditions(ChosenAreaOrder)

def EnemyGroupSetup(): # Makes extra group for superbosses:
    StartingGroupRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_EnemyGroup.json", "$id") + 1
    with open("./XC2/_internal/JsonOutputs/common/FLD_EnemyGroup.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingGroupRow, "EnemyID1": ChosenSuperbosses[0], "EnemyID2": ChosenSuperbosses[1], "EnemyID3": ChosenSuperbosses[2], "EnemyID4": ChosenSuperbosses[3], "EnemyID5": 0, "EnemyID6": 0, "EnemyID7": 0, "EnemyID8": 0, "EnemyID9": 0, "EnemyID10": 0, "EnemyID11": 0, "EnemyID12": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def QuestListSetup(ChosenAreaOrder): # Adjusting the quest list
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        CurrArea = 0
        for row in data["rows"]:
            rowID = row["$id"]
            match rowID:
                case rowID if rowID in range(235, 235 + SetCount - 1): # For all except the last set, do this
                    row["Talker"] = 1001
                    row["FlagCLD"] = 832 + CurrArea
                    row["PurposeID"] = 249 + CurrArea
                    row["CountCancel"] = 1
                    row["NextQuestA"] = row["$id"] + 1
                    row["CallEventA"] = ContinentInfo[ChosenAreaOrder[CurrArea+1]][0]
                    CurrArea += 1
                case rowID if rowID == 235 + SetCount - 1: # for the last quest
                    if not ExtraSuperbosses: # if we don't have extrasuperbosses, warp us to the credits
                        row["Talker"] = 1001
                        row["FlagCLD"] = 832 + CurrArea
                        row["PurposeID"] = 249 + CurrArea
                        row["CountCancel"] = 0
                        row["NextQuestA"] = 236 + CurrArea
                        row["NextQuestA"] = 30000
                        row["CallEventA"] = 10494
                        break
                    else: # otherwise, the set doesn't warp you anywhere, and instead starts the next quest
                        row["Talker"] = 1001
                        row["FlagCLD"] = 832 + CurrArea
                        row["PurposeID"] = 249 + CurrArea
                        row["CountCancel"] = 0
                        row["NextQuestA"] = 236 + CurrArea
                        row["CallEventA"] = 0
                        CurrArea += 1
                case rowID if rowID in range(235 + SetCount, 235 + SetCount + SuperbossCount - 1): # for all except the last quest (superbosses on)
                    row["Talker"] = 1001
                    row["FlagCLD"] = 832 + CurrArea
                    row["PurposeID"] = 249 + CurrArea
                    row["CountCancel"] = 0
                    row["NextQuestA"] = 236 + CurrArea
                    row["CallEventA"] = 0
                    CurrArea += 1
                case rowID if rowID == 235 + SetCount + SuperbossCount - 1: # for the instance where we have superbosses on, the very last quest
                    row["Talker"] = 1001
                    row["FlagCLD"] = 832 + CurrArea
                    row["PurposeID"] = 249 + CurrArea
                    row["CountCancel"] = 1
                    row["NextQuestA"] = 30000
                    row["CallEventA"] = 10494
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def EventSetup(ChosenAreaOrder, PartyMemberstoAdd): # Adjusting the initial area warp events
    with open("./XC2/_internal/JsonOutputs/common/EVT_listBf.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10465:
                row["nextID"] = ContinentInfo[ChosenAreaOrder[0]][0]
                row["nextIDtheater"] = row["nextID"]
                break
        for i in range(0, SetCount):
            for row in data["rows"]:
                if row["$id"] == ContinentInfo[ChosenAreaOrder[i]][0]:
                    row["scenarioFlag"] = 10010 + i
                    row["chapID"] = 10
                    row["linkID"] = 0
                    row["nextID"] = 0
                    row["nextIDtheater"] = 0

                    if PartyMemberstoAdd[i] != 0:
                        row["scriptName"] = PartyMembersAddScripts[PartyMemberstoAdd[i]][0]
                        row["scriptStartId"] = PartyMembersAddScripts[PartyMemberstoAdd[i]][1]
                    else:
                        row["scriptName"] = ""
                        row["scriptStartId"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def EventChangeSetup(ChosenAreaOrder): # Adjusting the warp event endings that change scenario flags
    with open("./XC2/_internal/JsonOutputs/common/EVT_chgBf01.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            for row in data["rows"]:
                if row["$id"] == ContinentInfo[ChosenAreaOrder[i]][1]:
                    row["id"] = 10011 + i
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PartyMemberAddition(): # Adds new party members
    ChosenPartyMemberOrder = []
    FirstPartyMember = []
    ChosenPartyMemberOrder.extend(random.sample(["Tora", "Zeke", "Nia", "Morag"], min(SetCount, 4)))
    FirstPartyMember.append(ChosenPartyMemberOrder[0]) # We want to guarantee getting 1 teammate minimum to start with
    ChosenPartyMemberOrder.pop(0)
    while len(ChosenPartyMemberOrder) < SetCount - 1:
        ChosenPartyMemberOrder.append(0)
    random.shuffle(ChosenPartyMemberOrder)
    FirstPartyMember.extend(ChosenPartyMemberOrder)
    RNGAdjustedChosenPartyMemberOrder = FirstPartyMember
    return RNGAdjustedChosenPartyMemberOrder

def QuestTaskSetup(EnemySets): # Adds the new quest tasks
    StartingQuestTaskRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestBattle.json", "$id") + 1
    StartingQuestLogRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_quest.json", "$id") + 1
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestTask.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            if len(EnemySets[i]) == 4:
                data["rows"].append({"$id": 249 + i, "PreCondition": 0, "TaskType1": 1, "TaskID1": StartingQuestTaskRow, "Branch1": 0, "TaskLog1": StartingQuestLogRow, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 1, "TaskID2": StartingQuestTaskRow + 1, "Branch2": 0, "TaskLog2": StartingQuestLogRow + 1, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 1, "TaskID3": StartingQuestTaskRow + 2, "Branch3": 0, "TaskLog3": StartingQuestLogRow + 2, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 1, "TaskID4": StartingQuestTaskRow + 3, "Branch4": 0, "TaskLog4": StartingQuestLogRow + 3, "TaskUI4": 0, "TaskCondition4": 0}) 
                StartingQuestTaskRow += 4
                StartingQuestLogRow += 4
            else: # if it's not 4, its 3, currently unused
                data["rows"].append({"$id": 249 + i, "PreCondition": 0, "TaskType1": 1, "TaskID1": StartingQuestTaskRow, "Branch1": 0, "TaskLog1": StartingQuestLogRow, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 1, "TaskID2": StartingQuestTaskRow + 1, "Branch2": 0, "TaskLog2": StartingQuestLogRow + 1, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 1, "TaskID3": StartingQuestTaskRow + 2, "Branch3": 0, "TaskLog3": StartingQuestLogRow + 2, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 0, "TaskID4": 0, "Branch4": 0, "TaskLog4": 0, "TaskUI4": 0, "TaskCondition4": 0}) 
                StartingQuestTaskRow += 3
                StartingQuestLogRow += 3
        if ExtraSuperbosses:
            for i in range(0, SuperbossCount):
                data["rows"].append({"$id": 259 + i, "PreCondition": 0, "TaskType1": 1, "TaskID1": StartingQuestTaskRow, "Branch1": 0, "TaskLog1": StartingQuestLogRow, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 0, "TaskID2": 0, "Branch2": 0, "TaskLog2": 0, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 1, "TaskID3": 0, "Branch3": 0, "TaskLog3": 0, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 0, "TaskID4": 0, "Branch4": 0, "TaskLog4": 0, "TaskUI4": 0, "TaskCondition4": 0})
                StartingQuestTaskRow += 1
                StartingQuestLogRow += 1        
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FieldQuestBattleSetup(EnemySets): # Adds new rows in FLD_QuestBattle accordingly
    StartingQuestBattleFlag = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestBattle.json", "CountFlag") + 1
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as file:
        LastRow = 777
        LastFlag = 795
        data = json.load(file)
        for i in range(0, SetCount):
            for j in range(0, len(EnemySets[i])):
                data["rows"].append({"$id": LastRow, "Refer": 1, "EnemyID": EnemySets[i][j], "EnemyGroupID": 0, "EnemySpeciesID": 0, "EnemyRaceID": 0, "Count": 1, "CountFlag": LastFlag, "DeadAll": 0, "TimeCount": 0, "TimeCountFlag": 0, "ReduceEnemyHP": 0, "ReducePCHP": 0, "TargetOff": 0}) 
                LastRow += 1
                LastFlag += 1
        if ExtraSuperbosses:
            for i in range(0, SuperbossCount):
                data["rows"].append({"$id": LastRow, "Refer": 1, "EnemyID": ChosenSuperbosses[i], "EnemyGroupID": 0, "EnemySpeciesID": 0, "EnemyRaceID": 0, "Count": 1, "CountFlag": LastFlag, "DeadAll": 0, "TimeCount": 0, "TimeCountFlag": 0, "ReduceEnemyHP": 0, "ReducePCHP": 0, "TargetOff": 0}) 
                LastRow += 1
                LastFlag += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def FieldQuestTaskLogSetup(EnemySets): # Adds the task logs for the field quests
    AllEnemySetNames = []
    AllEnemySetNameIDs = []
    SuperbossNameIDs = []
    SuperbossNames = []
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            CurrEnemySetNameIDs = []
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == EnemySets[i][j]:
                        CurrEnemySetNameIDs.append(row["Name"])
            AllEnemySetNameIDs.append(CurrEnemySetNameIDs)        
        if ExtraSuperbosses:
            for i in range(0, len(ChosenSuperbosses)):
                for row in data["rows"]:
                    if row["$id"] == ChosenSuperbosses[i]:
                        row["PreciousID"] = 25488 # You get another level 10 bounty token per um defeated
                        SuperbossNameIDs.append(row["Name"])
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            CurrEnemySetNames = []
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == AllEnemySetNameIDs[i][j]:
                        CurrEnemySetNames.append(row["name"])
                        break
            AllEnemySetNames.append(CurrEnemySetNames)
        for i in range(0, len(SuperbossNameIDs)):
            for row in data["rows"]:
                if row["$id"] == SuperbossNameIDs[i]:
                    SuperbossNames.append(row["name"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_quest.json", 'r+', encoding='utf-8') as file:
        StartRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_quest.json", "$id") + 1
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            for j in range(0, len(EnemySets[i])):
                data["rows"].append({"$id": StartRow, "style": 62, "name": f"Defeat [System:Color name=tutorial]{AllEnemySetNames[i][j]}[/System:Color]"})
                StartRow += 1
        if ExtraSuperbosses:
            for i in range(0, SuperbossCount):
                data["rows"].append({"$id": StartRow, "style": 62, "name": f"Defeat [System:Color name=tutorial]{SuperbossNames[0]}[/System:Color] in\n{SuperbossMaps[0].strip()}."})
                StartRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CustomEnemyDrops(EnemySets):
    SecretAccessoryIDs, SecretAuxCoreIDs = UMHuntShopCreation.ExportAccessoryAuxCoreMaxIDs()
    global NewAccessoryID, NewAuxCoreID
    NewAccessoryID = max(SecretAccessoryIDs) + 1
    NewAuxCoreID = max(SecretAuxCoreIDs) + 1
    DropTableDrops = []
    IDDrops = []
    CurrentEnemyDropRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", "$id") + 1
    # Generates Loot
    for i in range(len(EnemySets)):
        SetDropTableDrops = []
        SetIDDrops = []
        for j in range(len(EnemySets[i])):
            LuckyDrop = random.randint(0, 99)
            if LuckyDrop <= 34:
                SetDropTableDrops.append([0,0,0,0])
                SetIDDrops.append(0)
            elif LuckyDrop > 94: # 5% chance for Bounty Token, of any level, and the highest tier of loot
                SetIDDrops.append(CurrentEnemyDropRow)
                CurrentEnemyDropRow += 1
                SetDropTableDrops.append(CreateNewDropTable(2))
            elif LuckyDrop >= 85: # 10% chance for WP Manual of max rank and the middle tier of loot
                SetIDDrops.append(CurrentEnemyDropRow)
                CurrentEnemyDropRow += 1
                SetDropTableDrops.append(CreateNewDropTable(1))
            elif LuckyDrop >= 35: # 10% chance for a doubloon and the lowest tier of loot
                SetIDDrops.append(CurrentEnemyDropRow)
                CurrentEnemyDropRow += 1
                SetDropTableDrops.append(CreateNewDropTable(0))
        DropTableDrops.append(SetDropTableDrops)
        IDDrops.append(SetIDDrops)

    with open("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(IDDrops)):
            for j in range(len(IDDrops[i])):
                if IDDrops[i][j] != 0:
                    newrow = {"$id": IDDrops[i][j], "LimitNum": 0, "SelectType": 0, "ItemID1": 0, "DropProb1": 0, "NoGetByEnh1": 0, "FirstNamed1": 0, "ItemID2": 0, "DropProb2": 0, "NoGetByEnh2": 0, "FirstNamed2": 0, "ItemID3": 0, "DropProb3": 0, "NoGetByEnh3": 0, "FirstNamed3": 0, "ItemID4": 0, "DropProb4": 0, "NoGetByEnh4": 0, "FirstNamed4": 0, "ItemID5": 0, "DropProb5": 0, "NoGetByEnh5": 0, "FirstNamed5": 0, "ItemID6": 0, "DropProb6": 0, "NoGetByEnh6": 0, "FirstNamed6": 0, "ItemID7": 0, "DropProb7": 0, "NoGetByEnh7": 0, "FirstNamed7": 0, "ItemID8": 0, "DropProb8": 0, "NoGetByEnh8": 0, "FirstNamed8": 0}
                    for k in range(len(DropTableDrops[i][j])):
                        newrow[f"ItemID{k+1}"] = DropTableDrops[i][j][k]
                        newrow[f"FirstNamed{k+1}"] = 1
                        newrow[f"DropProb{k+1}"] = 10
                    data["rows"].append(newrow)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)  

    # Applies loot to File
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(EnemySets)):
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == EnemySets[i][j]:
                        LuckyDrop = random.randint(0, 99)
                        if LuckyDrop <= 34:
                            break
                        elif LuckyDrop > 94: # 5% chance for Bounty Token, of any level, and the highest tier of loot
                            row["PreciousID"] = random.choice(Helper.InclRange(25479, 25488))
                            row["DropTableID"] = IDDrops[i][j]
                            break
                        elif LuckyDrop >= 85: # 10% chance for WP Manual of max rank and the middle tier of loot
                            row["PreciousID"] = 25407
                            row["DropTableID"] = IDDrops[i][j]
                            break
                        elif LuckyDrop >= 35: # 50% chance for a doubloon and the lowest tier of loot
                            row["PreciousID"] = 25489
                            row["DropTableID"] = IDDrops[i][j]
                            break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)          

def CreateNewDropTable(Rarity: int = 0):
    ChosenDrops = random.choices(["AuxCore", "Accessory", "Nothing"], weights = [33, 33, 34], k = 4)
    DropIDs = []
    for item in ChosenDrops:
        match item:
            case "Nothing":
                DropIDs.append(0)
            case "Accessory":
                DropIDs.append(CreateMonsterDropAccessory(Rarity))
            case "AuxCore":
                DropIDs.append(CreateMonsterDropAuxCore(Rarity))
    return DropIDs

def CreateMonsterDropAccessory(Rarity: int = 0):
    global NewAccessoryID
    AccessoryEnhancementList = [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp,IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp, BladeSwitchDamageUp, BreakResDown,KaiserZone, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, FlatStrengthBoost, FlatEtherBoost, HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, LowHPRegen, AllDebuffRes, TastySnack, DoomRes, TauntRes, BladeShackRes, DriverShackRes, WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, FlatHPBoost, ArtUseHeal, AgiBoost,GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatAgiBoost, HPBoost, CritHeal, SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat,CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill,RecoverRechargeCrit, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, TakeDamageHeal, DamagePerEvadeUp, PartyHealBladeSwitch, LowHPSpecialUp]

    AccessoryTypesandNames = { # What icon should go with what noun:
            0:["Sandals", "Crocs", "Jordans", "Boots", "Sneakers"], 
            1:["Baseball Cap", "Sweatband", "Beanie", "Earmuffs"], 
            2:["Vest", "Tuxedo", "T-Shirt", "Tank Top", "Jacket"], 
            3:["Choker", "Necklace", "Locket", "Tie"], 
            4:["Belt", "Sash", "Scarf"], 
            5:["Banner", "Loincloth", "Swimsuit", "Thread", "Lamp", "Incense"], 
            6:["Gloves", "Silly Bandz", "Gauntlets", "Bangles", "Watches"],
            7:["Cube", "AirPods", "Headphones", "Hard Drive", "Attachment"],
            8:["Garnet", "Sapphire", "Diamond", "Ruby", "Emerald", "Prismarine"],
            9:["Feather", "Medal", "Bling"]
        }

    with open("./XC2/_internal/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as namefile:
    
            namedata = json.load(namefile) 
            data = json.load(file)

            for row in data["rows"]:
                if row["$id"] == NewAccessoryID:
                    curAccessory:Enhancement = random.choice(AccessoryEnhancementList)
                    curAccessory.RollEnhancement(Rarity, 0.6)
                    row["Enhance1"] = curAccessory.id
                    row["Rarity"] = curAccessory.Rarity
                    ItemType = random.randint(0,9)
                    row["Icon"] = ItemType
                    CurName = row["Name"]
                    NewAccessoryID += 1
                    break
            for namerow in namedata["rows"]:  
                if namerow["$id"] == CurName:
                    lastWord = random.choice(AccessoryTypesandNames[ItemType])
                    namerow["name"] = f"{curAccessory.name} {lastWord}"
                    break

            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return NewAccessoryID

def CreateMonsterDropAuxCore(Rarity: int = 0):
    global NewAuxCoreID
    AuxCoreValidEnhancements = [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, BladeComboDamUp, FusionComboDamUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp, LV1Damage, LV2Damage, LV3Damage, LV4Damage, IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, PartyDamageMaxAffinity, PartyCritMaxAffinity, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp, KaiserZone, AffinityMaxAttack, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, DamageAndCritUpMaxAffinity, FlatCritBoost, HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, AffinityMaxBarrier, AffinityMaxEvade, LowHPRegen, AllDebuffRes, BladeArtsTriggerUp, BladeArtDuration, HunterChem, ShoulderToShoulder, WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, PartyDamageReducMaxAffinity, PhyAndEthDefenseUp, ReduceEnemyChargeMaxAffinity, GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatBlockBoost, SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat, CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill, RecoverRechargeCrit, DealMoreTakeLessMaxAffinity, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, HealingUpMaxAffinity, TakeDamageHeal, StopThinking, ChainAttackPower, DamagePerEvadeUp]
    with open("./XC2/_internal/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./XC2/_internal/JsonOutputs/common_ms/itm_orb.json", 'r+', encoding='utf-8') as namefile:
    
            namedata = json.load(namefile) 
            data = json.load(file)

            for row in data["rows"]:
                if row["$id"] == NewAuxCoreID:
                    curAuxCore:Enhancement = random.choice(AuxCoreValidEnhancements)
                    curAuxCore.RollEnhancement(Rarity, 0.6) # monster accessories should be much weaker than ones in shops
                    row["Enhance"] = curAuxCore.id
                    row["Rarity"] = curAuxCore.Rarity
                    row["EnhanceCategory"] = NewAuxCoreID - 17001
                    NewAuxCoreID += 1
                    CurName = row["Name"]
                    break
            for namerow in namedata["rows"]:  
                if namerow["$id"] == CurName:    
                    namerow["name"] = f"{curAuxCore.name} Core"
                    break
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return NewAuxCoreID

def ChosenEnemySets(AreaUMs): # Figuring out what enemies to turn into a set
    EnemySets = []
    for i in range(0, SetCount):
        if len(AreaUMs[i]) >= 4:
            EnemySets.append(random.sample(AreaUMs[i], 4))
        else: # currently unused
            EnemySets.append(random.sample(AreaUMs[i], len(AreaUMs[i])))
    return EnemySets

def CustomEnemyRando(ChosenAreaOrder): # Custom shuffling of enemies
    AllAreaUMs = []
    AllAreaMonsters = []
    AllAreaSuperbosses = []
    SuperbossMapsFull = []
    AllOriginalAreaEnemies = []
    AllNewAreaEnemies = []
    ChosenSuperbossNumbers = []
    # "Area Name": [Valid Unique Enemies]
    OriginalAreaEnemies = {
        "Gormott": [184, 185, 186, 187, 189, 190, 191, 193, 195, 196, 197, 198, 266, 303, 304, 329, 332, 341, 342, 345, 346, 347, 348, 349, 350, 352, 487, 488, 489, 490, 491, 492, 546, 547, 548, 559, 572, 598, 600, 601, 602, 603, 604, 607, 608, 609, 610, 611, 635, 636, 637, 638, 639, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 699, 701, 703, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 723, 729, 730, 731, 732, 733, 734, 735, 736, 738, 1320, 1321, 1326, 1329, 1386, 1387],
        "Uraya": [199, 201, 202, 203, 204, 206, 208, 210, 212, 214, 267, 268, 305, 307, 308, 309, 310, 356, 365, 367, 369, 372, 373, 374, 375, 407, 409, 411, 451, 479, 481, 483, 485, 496, 506, 508, 510, 512, 536, 538, 567, 577, 578, 579, 581, 583, 588, 591, 593, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 800, 802, 804, 806, 808, 809, 810, 811, 812, 814, 815, 816, 817, 819, 1674],
        "Mor Ardain": [216, 217, 219, 220, 221, 222, 223, 225, 227, 269, 270, 271, 313, 315, 383, 384, 385, 386, 389, 390, 391, 392, 393, 394, 395, 396, 399, 401, 403, 404, 405, 406, 454, 493, 495, 517, 519, 521, 523, 525, 532, 533, 534, 535, 540, 542, 544, 549, 550, 551, 555, 571, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 884, 886, 888, 890, 891, 892, 893, 894, 895, 896, 898, 899, 906, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 922, 924, 926, 928, 929, 1343, 1388, 1418, 1419, 1675, 1676, 1677, 1678, 1679, 1680, 1681],
        "Leftheria": [229, 318, 319, 414, 415, 418, 445, 446, 447, 448, 474, 476, 498, 553, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1254, 1255, 1256, 1258, 1260, 1261, 1262, 1264, 1265, 1344, 1345, 1395, 1397, 1398, 1399, 1415, 1416, 1417, 1684, 1686, 1687, 1688, 1689, 1690],
        "Temperantia": [231, 232, 234, 376, 475, 477, 500, 501, 504, 552, 560, 569, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1019, 1020, 1022, 1023, 1025, 1026, 1027, 1342, 1389, 1391, 1393, 1408, 1410, 1412, 1413, 1414],
        "Tantal": [237, 238, 239, 240, 241, 323, 436, 437, 455, 456, 457, 458, 459, 461, 462, 463, 513, 515, 566, 576, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1104, 1106, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1404, 1405, 1406, 1425, 1682, 1683, 1888],
        "Spirit Crucible": [242, 359, 497, 503, 570, 573, 930, 931, 932, 933, 934, 935, 936, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 957, 958],
        "Cliffs of Morytha": [243, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1131, 1132, 1134, 1135, 1137, 1400, 1402],
        "Land of Morytha": [248, 249, 250, 274, 324, 351, 565, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1423, 1424],
        "World Tree": [251, 252, 253, 254, 325, 326, 557, 558, 564, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1422]
    }
    CopyofUnusedNormalValidEnemyDefaultIDs = UnusedNormalValidEnemyDefaultIDs.copy()
    ShuffledUniqueEnemyIDs = AllUniqueMonsterDefaultIDs.copy()
    ShuffledSuperBossIDs = AllSuperBossDefaultIDs.copy()
    random.shuffle(ShuffledSuperBossIDs)
    random.shuffle(ShuffledUniqueEnemyIDs)
    for k in range(0, len(ChosenAreaOrder)): # 10 loops max
        Chosen4UMs = ShuffledUniqueEnemyIDs[(4*k):(4+4*k)]
        ChosenSuperBoss = ShuffledSuperBossIDs[k]
        CurrentAreaUMs = []
        CurrentAreaMonsters = []
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[k]][2] + "_FLD_EnemyPop.json"
        Helper.ColumnAdjust(enemypopfile, ["battlelockname"], 0)
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            NewAreaEnemies = OriginalAreaEnemies[ChosenAreaOrder[k]].copy() # make a copy of the list
            NewAreaEnemies = [x for x in NewAreaEnemies if x not in AllUniqueMonsterDefaultIDs + AllSuperBossDefaultIDs] # now remove all ums and superbosses
            del NewAreaEnemies[-2:] # remove two slots, this accounts for the land of morytha, where there's only 3 unique monsters, and no superbosses. Everywhere else has 4, and we need at least 5 slots to add 4 ums + 1 superboss to each area
            NewAreaEnemies.extend(Chosen4UMs) # add the 4 UMs back to the pool
            if ExtraSuperbosses:
                NewAreaEnemies.append(ChosenSuperBoss) # add the superboss to the pool
            while len(NewAreaEnemies) < len(OriginalAreaEnemies[ChosenAreaOrder[k]]): # while the new enemy pool is less than the original, we need to add more to make them equal
                ChosenNormalEnemy = random.choice(CopyofUnusedNormalValidEnemyDefaultIDs)
                NewAreaEnemies.append(ChosenNormalEnemy)
                CopyofUnusedNormalValidEnemyDefaultIDs.remove(ChosenNormalEnemy)
            random.shuffle(NewAreaEnemies) # now mix up the enemies
            Old2NewEnemy = {OriginalAreaEnemies[ChosenAreaOrder[k]][i]: NewAreaEnemies[i] for i in range(len(OriginalAreaEnemies[ChosenAreaOrder[k]]))} # dictionary showing how old enemy should get replaced by new enemy
            try:
                while Old2NewEnemy[1137] in Chosen4UMs + ChosenSuperBoss: # if the ophion slot gets chosen for a um or superboss, reroll the list
                    random.shuffle(NewAreaEnemies)
                    Old2NewEnemy = {OriginalAreaEnemies[ChosenAreaOrder[k]][i]: NewAreaEnemies[i] for i in range(len(OriginalAreaEnemies[ChosenAreaOrder[k]]))} # dictionary showing how old enemy should get replaced by new enemy
            except:
                pass
            for row in data["rows"]: # row ~550 loops
                for j in range(1, 5): # column 4 loops
                    OldEnemyID = row[f"ene{j}ID"]
                    if OldEnemyID == 0:
                        break
                    else:
                        try:
                            row[f"ene{j}ID"] = Old2NewEnemy[OldEnemyID]
                            NewEnemyID = row[f"ene{j}ID"]
                            CurrentAreaMonsters.append(NewEnemyID)
                            if NewEnemyID in AllUniqueMonsterDefaultIDs: # if it's a um we want it to always show up
                                row["Condition"] = row["ScenarioFlagMax"] = row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["muteki_QuestFlag"] = row["muteki_QuestFlagMin"] = row["muteki_QuestFlagMax"] = row["muteki_Condition"] = row[f"ene{j}Lv"] = 0
                                row["POP_TIME"] = 256
                                row["popWeather"] = 255
                                CurrentAreaUMs.append(row[f"ene{j}ID"]) # now add it to the list of ums for this area, used in many places, so we need to keep track of this
                            elif NewEnemyID in AllSuperBossDefaultIDs: # if it's a superboss, do the same as for ums, except add it to its' own list
                                row["ScenarioFlagMax"] = row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["muteki_QuestFlag"] = row["muteki_QuestFlagMin"] = row["muteki_QuestFlagMax"] = row["muteki_Condition"] = row[f"ene{j}Lv"] = 0
                                row["Condition"] = 3913 # superbosses should only show up when you're on the last set
                                row["POP_TIME"] = 256
                                row["popWeather"] = 255
                                AllAreaSuperbosses.append(NewEnemyID)
                                SuperbossMapsFull.append(ChosenAreaOrder[k])
                        except:
                            row[f"ene{j}num"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        CurrentAreaUMs = list(dict.fromkeys(CurrentAreaUMs))
        AllAreaUMs.append(CurrentAreaUMs)
        CurrentAreaMonsters = list(dict.fromkeys(CurrentAreaMonsters))
        AllAreaMonsters.append(CurrentAreaMonsters)
        AllOriginalAreaEnemies.extend(OriginalAreaEnemies[ChosenAreaOrder[k]])
        AllNewAreaEnemies.extend(NewAreaEnemies)
    EnemyRandoLogic.FlyingEnemyFix(AllOriginalAreaEnemies, AllNewAreaEnemies)
    EnemyRandoLogic.SwimmingEnemyFix(AllOriginalAreaEnemies, AllNewAreaEnemies)
    EnemyRandoLogic.FishFix()
    # EnemyRandoLogic.BigEnemyCollisionFix() no longer needed, there's no red rings at all.
    global ChosenSuperbosses, SuperbossMaps
    if ExtraSuperbosses:
        UniqueSuperbosses = list(dict.fromkeys(AllAreaSuperbosses))
        ValidSuperBossList = Helper.InclRange(0, 9)
        for i in range(SuperbossCount):
            ChosenSuperbossNumber = random.choice(ValidSuperBossList)
            ChosenSuperbossNumbers.append(ChosenSuperbossNumber)
            ValidSuperBossList.remove(ChosenSuperbossNumber)
        ChosenSuperbosses = []
        for i in range(0, SuperbossCount):
            ChosenSuperbosses.append(UniqueSuperbosses[ChosenSuperbossNumbers[i]])
        SuperbossMaps = []
        for i in range(0, SuperbossCount):
            for j in range(0, len(AllAreaSuperbosses)):
                if AllAreaSuperbosses[j] == ChosenSuperbosses[i]: # if we have a chosen superboss that matches the entire list of superbosses and their maps (both of equal length!)
                    SuperbossMaps.append(SuperbossMapsFull[j]) # add the superboss's map to the list of maps we care about
                    break
    else:
        SuperbossMaps = []
        ChosenSuperbosses = []
    UMEnemyAggro()
    ClearExcessiveUMCounts(ChosenAreaOrder, AllAreaUMs)
    Helper.SubColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_EnParam.json", "Flag", "FldDmgType", 0)
    return AllAreaUMs, AllAreaMonsters
    
def UMEnemyAggro(): # custom enemy aggro
    EnemyAggroSliderOdds = Options.EnemyAggroOption.GetSpinbox()
    if EnemyAggroSliderOdds == 0: #if the slider is 0, turn every enemy passive, except the unique monsters
        with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for row in data["rows"]:
                if (row["$id"] in IDs.ValidEnemies) & (row["$id"] not in AllUniqueMonsterDefaultIDs + AllSuperBossDefaultIDs):
                    row["Flag"]["AlwaysAttack"] = 0
                    row["Flag"]["mBoss"] = 0
                    row["Flag"]["LinkType"] = 0
                    row["SearchRange"] = 0
                    row["SearchRadius"] = 0
                    row["SearchAngle"] = 0
                    row["Detects"] = 0
                    row["BatInterval"] = 50
                    row["BatArea"] = 50
                elif (row["$id"] in AllUniqueMonsterDefaultIDs + AllSuperBossDefaultIDs) & (row["$id"] in IDs.ValidEnemies):
                    row["Flag"]["AlwaysAttack"] = 0
                    row["Flag"]["mBoss"] = 0
                    row["Flag"]["Named"] = 1
                    row["Detects"] = 3
                    row["SearchRange"] = 10
                    row["SearchAngle"] = 360
                    row["SearchRadius"] = 5
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    else: # everything can be aggro or not. ums untouched, since they all aggro by default i believe? nope
        with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for row in data["rows"]:
                if (EnemyAggroSliderOdds != 100) & (row["$id"] not in AllUniqueMonsterDefaultIDs + AllSuperBossDefaultIDs) & (random.randint(0,100) >= EnemyAggroSliderOdds) & (row["$id"] in IDs.ValidEnemies):
                    row["Flag"]["AlwaysAttack"] = 0
                    row["Flag"]["mBoss"] = 0
                    row["Flag"]["LinkType"] = 0
                    row["SearchRange"] = 0
                    row["SearchRadius"] = 0
                    row["SearchAngle"] = 0
                    row["Detects"] = 0
                    row["BatInterval"] = 50
                    row["BatArea"] = 50
                elif (row["$id"] in AllUniqueMonsterDefaultIDs + AllSuperBossDefaultIDs) & (row["$id"] in IDs.ValidEnemies):
                    row["Flag"]["AlwaysAttack"] = 0
                    row["Flag"]["mBoss"] = 0
                    row["Flag"]["Named"] = 1
                    row["Detects"] = 3
                    row["SearchRange"] = 10
                    row["SearchAngle"] = 360
                    row["SearchRadius"] = 5
                elif row["$id"] in AllBossDefaultIDs: # even if a boss doesnt roll non-aggression, we want to nerf it's aggro radius and area
                    row["SearchRange"] = random.randint(5, 25)
                    row["SearchAngle"] = random.randint(45, 75)
                    row["SearchRadius"] = random.randint(1, 10)
                    row["BatInterval"] = 50
                    row["BatArea"] = 50
                    row["Flag"]["mBoss"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def ClearExcessiveUMCounts(ChosenAreaOrder, AllAreaUMs): # if a um gets put in a spot where there's more than 15 enemies on the map, it crashes the game when you try to load into the area.
    CombinedAreaUMs = []
    for area in range(len(AllAreaUMs)):
        CombinedAreaUMs.extend(AllAreaUMs[area])
    try:
        CombinedAreaUMs.extend(ChosenSuperbosses)
    except:
        pass
    enemycountholder = Helper.ExtendListtoLength([0], len(CombinedAreaUMs),"0")
    for i in range(0, len(ChosenAreaOrder)):
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_EnemyPop.json"
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for k in range(1, 5):
                    if row[f"ene{k}ID"] == 0:
                            break
                    else:
                        for j in range(len(CombinedAreaUMs)):
                            if row[f"ene{k}ID"] == CombinedAreaUMs[j]:
                                enemycountholder[j] += row[f"ene{k}num"]
                                if enemycountholder[j] > 15: # if there's already too many of the enemy, then we want to remove that spawn point for the enemy.
                                    enemycountholder[j] -= row[f"ene{k}num"]
                                    row[f"ene{k}ID"] = 0
                                    row[f"ene{k}Per"] = 0
                                    row[f"ene{k}num"] = 0
                                    row[f"ene{k}move"] = 0 
                                    row[f"ene{k}Lv"] = 0                                   
                                break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def CHR_EnArrangeAdjustments(AllAreaMonsters, EnemySets, ChosenAreaOrder): # adjusts aggro + drops of all enemies + levels + stats
    EnemyParamstoNerf = Helper.ExtendListtoLength([], len(EnemySets), "[]") # we want to nerf the early enemies in all their stats, you just don't have much damage or tankiness
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", ["ExpRev", "GoldRev", "WPRev", "SPRev", "DropTableID", "DropTableID2", "DropTableID3"], 0)         
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(AllAreaMonsters)):
            for row in data["rows"]:
                if row["$id"] in AllAreaMonsters[i]:
                    row["Lv"] = 5 + 12*i # Level Formula: Sets level of enemy equal to 5 min, then for each set after, the level goes up by 12 more, so eventually the enemies outscale you
                    row["ZoneID"] = ContinentInfo[ChosenAreaOrder[i]][3] # this fixes pointers not working?
        for i in range(0, len(EnemySets)):
            for j in range(0, len(EnemySets[i])):
                for row in data["rows"]:
                    if row["$id"] == EnemySets[i][j]:
                        EnemyParamstoNerf[i].append(row["ParamID"])
                        if row["Scale"] < 35:
                            row["Scale"] = 35
                        elif row["Scale"] > 750:
                            row["Scale"] = 750
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, min(len(EnemySets),4)):
            NerfRatio = 0.6 + (i+1)*0.1 # 60%->70%->80%->90%->100% after area 4 ends
            for row in data["rows"]:
                if row["$id"] in EnemyParamstoNerf[i]:
                    for stat in ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"]:
                        row[stat] = round(row[stat]*NerfRatio)
        for row in data["rows"]:
            row["HpMaxRev"] = round(row["HpMaxRev"]* 0.5) # nerf the enemy hp harder.         
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    EnemyRandoLogic.SummonsLevelAdjustment()

def LandmarkAdjustments(ChosenAreaOrder): # removes xp and sp gains from landmarks, except for the first one
    for i in range(0, len(ChosenAreaOrder)):
        landmarkpopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_LandmarkPop.json"
        with open(landmarkpopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # removes xp gains from argentum landmarks
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma21a_FLD_LandmarkPop.json", 'r+', encoding='utf-8') as file: # removes xp gains from elysium landmarks
            data = json.load(file)
            for row in data["rows"]:
                row["getEXP"] = 0
                row["getSP"] = 0
                row["developZone"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def RandomLandmarkCreation(): # Creates random landmarks and adds them to the DLC rewards. Also adds movespeed deed here because it's convenient
    CurrentID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", "$id") + 1
    StartingNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    CurrentNameID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    # Map: Landmarks
    LandmarkPool = {
                    "Gormott": [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 539, 540, 541, 542, 543, 554, 555, 556, 557, 559, 560, 576, 577, 578],
                    "Uraya": [701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 739, 740, 741, 750, 751, 752, 753, 754],
                    "Mor Ardain": [801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 832, 833, 834, 835, 836, 837, 838, 839, 849, 850, 851, 852, 853, 854, 855, 856, 870],
                    "Leftheria": [1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1520, 1521, 1522, 1523],
                    "Temperantia": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1023],
                    "Tantal": [1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1327, 1334, 1335, 1336, 1337, 1338, 1339, 1344],
                    "Spirit Crucible": [1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1617],
                    "Cliffs of Morytha": [1701, 1702, 1703, 1704, 1705],
                    "Land of Morytha": [1801, 1802, 1803, 1804, 1805, 1806, 1807],
                    "World Tree": [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]
                    }
    ChangingLandmarkPool = LandmarkPool
    if Options.UMHuntOption_RandomLandmarks.GetState():
        GuaranteedLandmarks = [501, 701, 832, 1501, 1101, 1301, 1601, 1701, 1801, 2001]
        ChosenLandmarks = GuaranteedLandmarks.copy()
        for area in ChangingLandmarkPool:
            for landmark in GuaranteedLandmarks:
                if landmark in ChangingLandmarkPool[area]:
                    ChangingLandmarkPool[area].remove(landmark)
                    break
            AreaLandmarksSelected = random.sample(ChangingLandmarkPool[area], k = 4)
            ChosenLandmarks.extend(AreaLandmarksSelected)
            for i in range(0, 4):
                ChangingLandmarkPool[area].remove(AreaLandmarksSelected[i])
        
        with open("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Movespeed Deed
            data["rows"].append({"$id": CurrentID, "releasecount": 4, "title": CurrentNameID, "condition": UMHuntEnableCondListIDs[0], "category": 1, "item_id": 25249, "value": 1, "disp_item_info": 0, "getflag": 35400})
            CurrentID += 1
            CurrentNameID += 1
            # Landmarks
            for landmark in ChosenLandmarks:
                data["rows"].append({"$id": CurrentID, "releasecount": 4, "title": CurrentNameID, "condition": UMHuntEnableCondListIDs[0], "category": 2, "item_id": 0, "value": 1, "disp_item_info": 0, "getflag": 51161 + landmark})
                CurrentID += 1
                CurrentNameID += 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Movespeed Deed
            data["rows"].append({"$id": StartingNameID, "style": 162, "name": "Movespeed Deed"})
            StartingNameID += 1
            # Landmarks
            for landmark in ChosenLandmarks:
                data["rows"].append({"$id": StartingNameID, "style": 162, "name": "Landmark Receival"})
                StartingNameID += 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    else:
        DefaultLandmarkFlags = [51662, 51667, 51668, 51673, 51700, 51718, 51865, 51867, 51871, 51872, 51900, 51963, 51968, 51998, 52011, 52167, 52170, 52172, 52462, 52468, 52469, 52471, 52500, 52665, 52669, 52681, 52762, 52765, 52766, 52768, 52770, 52862, 52863, 52865, 52962, 52964, 53164, 53165, 53166, 53170]
        with open("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Movespeed Deed
            data["rows"].append({"$id": CurrentID, "releasecount": 4, "title": CurrentNameID, "condition": UMHuntEnableCondListIDs[0], "category": 1, "item_id": 25249, "value": 1, "disp_item_info": 0, "getflag": 35400})
            CurrentID += 1
            CurrentNameID += 1
            # Landmarks
            for flag in DefaultLandmarkFlags:
                data["rows"].append({"$id": CurrentID, "releasecount": 4, "title": CurrentNameID, "condition": UMHuntEnableCondListIDs[0], "category": 2, "item_id": 0, "value": 1, "disp_item_info": 0, "getflag": flag})
                CurrentID += 1
                CurrentNameID += 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./XC2/_internal/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Movespeed Deed
            data["rows"].append({"$id": StartingNameID, "style": 162, "name": "Movespeed Deed"})
            StartingNameID += 1
            # Landmarks
            for flag in DefaultLandmarkFlags:
                data["rows"].append({"$id": StartingNameID, "style": 162, "name": "Landmark Receival"})
                StartingNameID += 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)


def AddQuestConditions(ChosenAreaOrder): # Adding conditions for each area's warp to be unlocked + 1 to allow me to disable all other stuff (salvage points are the big one atm)
    # First, need to replace any conditions
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["ScenarioMax"] > 10009:
                row["ScenarioMax"] = 10009
            if row["NotScenarioMin"] < 10009:
                row["NotScenarioMin"] = 10009
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(0, len(ChosenAreaOrder)):
        eventpopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_EventPop.json"
        with open(eventpopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["ScenarioFlagMax"] > 10009:
                    row["ScenarioFlagMax"] = 10009
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": 322, "ScenarioMin": 1001, "ScenarioMax": 1002, "NotScenarioMin": 0, "NotScenarioMax": 0})
        for i in range(0, SetCount):
            data["rows"].append({"$id": 323 + i, "ScenarioMin": 10011 + i, "ScenarioMax": 10048, "NotScenarioMin": 0, "NotScenarioMax": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": UMHuntDisableCondListID, "Premise": 0, "ConditionType1": 1, "Condition1": 322, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        for i in range(0, SetCount):
            data["rows"].append({"$id": UMHuntEnableCondListIDs[i], "Premise": 0, "ConditionType1": 1, "Condition1": 323 + i, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    # We also want to add some conditions for when we only want an object to exist at one specific scenario flag:
    StartingConditionScenario = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", "$id") + 1
    CurrentConditionScenario = StartingConditionScenario
    StartingConditionList = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    global OneScenarioConditionList # we want to make this global, to capture the known conditions for one scenario flag only
    OneScenarioConditionList = []
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            data["rows"].append({"$id": CurrentConditionScenario, "ScenarioMin": 10011 + i, "ScenarioMax": 10011 + i, "NotScenarioMin": 0, "NotScenarioMax": 0})
            CurrentConditionScenario += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, SetCount):
            data["rows"].append({"$id": StartingConditionList, "Premise": 0, "ConditionType1": 1, "Condition1": StartingConditionScenario, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
            OneScenarioConditionList.append(StartingConditionList)
            StartingConditionList += 1
            StartingConditionScenario += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    OrderedMapIDs = []
    with open("./XC2/_internal/JsonOutputs/common/FLD_maplist.json", 'r+', encoding='utf-8') as file: # pretty sure this is messing up stuff with the maps
        data = json.load(file)
        for i in range(0, len(ChosenAreaOrder)):
            for row in data["rows"]:
                if row["select"] == ContinentInfo[ChosenAreaOrder[i]][2]:
                    if row["select"] == "ma05a" or "ma08a": # these let you do a long rest at an inn
                        row["ebb_ON_cndID"] = 0 
                        row["ebb_inn_cndID"] = 1
                    OrderedMapIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_WorldMapCond.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] <= len(ChosenAreaOrder):
                row["mapId"] = ContinentInfo[ChosenAreaOrder[row["$id"] - 1]][3] # puts the mapIDs in order, so we can assign conditions in order
                row["cond1"] = UMHuntDisableCondListID + row["$id"]
                row["enter"] = 0
            elif row["$id"] == len(ChosenAreaOrder) + 1:
                row["mapId"] = 3
                row["cond1"] = UMHuntEnableCondListIDs[0]
            else:
                row["mapId"] = 0
                row["cond1"] = UMHuntDisableCondListID
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def NoUnintendedRewards(ChosenAreaOrder): # Removes any cheese you can do by doing sidequests, selling Collection Point items
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", ["Gold", "EXP", "Sp", "Coin", "DevelopZone", "DevelopPoint", "TrustPoint", "MercenariesPoint", "IdeaCategory", "IdeaValue", "ItemID1", "ItemNumber1", "ItemID2", "ItemNumber2", "ItemID3", "ItemNumber3", "ItemID4", "ItemNumber4"], 0) # doing quests don't reward you
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/ITM_CollectionList.json", ["Price"], 0) # collectables sell for 0
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_SalvagePointList.json", ["Condition"], UMHuntDisableCondListID) # salvaging is disabled
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2", "EnemyExp"], ['252']) # It costs 252 xp to level up, regardless of level
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_GravePopList.json", ["en_popID"], 0) # Keeps you from respawning a UM.
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", ["Condition"], UMHuntDisableCondListID) # removes drops from chests in argentum
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", ["QuestID"], 0) # removes talking to NPCs in argentum
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/ma21a_FLD_TboxPop.json", ["Condition"], UMHuntDisableCondListID) # removes treasure chests from Elysium
    for area in ChosenAreaOrder:
        Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_TboxPop.json", ["Condition"], UMHuntDisableCondListID) # removes drops from chests
        Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[area][2] + "_FLD_NpcPop.json", ["QuestID"], 0) # removes talking to NPCs in area

def SpiritCrucibleEntranceRemoval(): # Exiting or Entering Spirit Crucible has problems with resetting the quest condition. So we remove that by warping the player back to the original landmark in that area.
    with open("./XC2/_internal/JsonOutputs/common_gmk/FLD_MapJump.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 3: # Leftherian Entrance to Spirit Crucible
                row["MapJumpId"] = 166 # get pranked lmao
            if row["$id"] == 4: # Spirit Crucible Entrance to Leftheria
                row["MapJumpId"] = 167 # get pranked lmao
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def BladeTrustRequirementChanges(): # changes the blade trust/skill unlock requirements to defeating a specific number of UMs
    NumberofUMstoDefeat = [8, 16, 24, 32]
    KeyAchievementIDs = [15, 25, 0, 35, 45, 55, 65, 75, 85, 95, 105, 0, 0, 115, 125, 135, 145, 375, 385, 155, 185, 165, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 195, 355, 365, 395, 0, 415, 425, 465, 455, 445, 435, 405, 175, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 95, 405, 455, 455, 445, 435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 365, 85, 1668, 1678, 1648, 1658, 1739, 1749, 0, 1759, 1739, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 325, 325, 325, 1679, 1689, 1699, 1709, 1719, 1729]
    KeyAchievementIDs = list(set([x for x in KeyAchievementIDs if x != 0]))
    TaskIDs = Helper.ExtendListtoLength([Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestCondition.json", "$id") + 1], 4, "inputlist[i-1]+1")
    TaskLogIDs = [659, 660, 661, 662]
    ValidBladeIDs = [1001, 1002, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1076, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1111, 1112]
    StarterBladeTrustSetAppearance = [16, 11, 12, 13, 14] #rank 1
    Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1
    ArtandSkillCols = ["ArtsAchievement1", "ArtsAchievement2", "ArtsAchievement3", "SkillAchievement1", "SkillAchievement2", "SkillAchievement3", "FskillAchivement1", "FskillAchivement2", "FskillAchivement3"]
    TrustCol = "KeyAchievement"

    ArtandSkillIDs = []
    TrustIDs = []

    for i in range(0, len(ArtandSkillCols)):
        ArtandSkillIDs += Helper.AdjustedFindBadValuesList("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], ValidBladeIDs, ArtandSkillCols[i])
        ArtandSkillIDs = [x for x in ArtandSkillIDs if x != 0]

    TrustIDs.extend(Helper.AdjustedFindBadValuesList("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", ["$id"], ValidBladeIDs, TrustCol))
    TrustIDs = [x for x in TrustIDs if x != 0]

    with open("./XC2/_internal/JsonOutputs/common/FLD_AchievementSet.json", 'r+', encoding='utf-8') as file: # now we need to modify corresponding set ids
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ArtandSkillIDs:
                for j in range(1, 6):
                    if (row[f"AchievementID{j}"] != 0):
                        row[f"AchievementID{j}"] = 16
            if row["$id"] in TrustIDs:
                for j in range(1,6):
                    row[f"AchievementID{j}"] = StarterBladeTrustSetAppearance[j-1]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #we need to change FLD_Achievement ID 1 to walk 1 step total
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                    row["StatsID"] = 60
                    row["Count"] = 1
                    row["DebugName"] = "WALK_TOTAL"
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestTaskAchievement.json", 'r+', encoding='utf-8') as file: #now we need to modify the FLD_QuestTaskAchievement
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] <= 7004:
                    row["TaskType1"] = 10
                    row["TaskID1"] = TaskIDs[row["$id"]-7001]
                    row["TaskCondition1"] = 0
                if row["$id"] == 7005:
                    row["TaskType1"] = 12
                    row["TaskID1"] = 1
                    row["TaskCondition1"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestCondition.json", 'r+', encoding='utf-8') as file: # Adding new Quest Conditions
        data = json.load(file)
        ConditionListRows = Helper.ExtendListtoLength([Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1], 4, "inputlist[i-1]+1")
        for i in range(0, 4):
            data["rows"].append({"$id": TaskIDs[i], "ConditionID": ConditionListRows[i], "MapID": 0, "NpcID": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file: # Adding new ConditionIDs for Quest Condition
        data = json.load(file)
        FlagListRows = Helper.ExtendListtoLength([Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionFlag.json", "$id") + 1], 4, "inputlist[i-1]+1")
        for i in range(0, 4):
           data["rows"].append({"$id": ConditionListRows[i], "Premise": 0, "ConditionType1": 4, "Condition1": FlagListRows[i], "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0 , "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionFlag.json", 'r+', encoding='utf-8') as file: # Adding new checks for the # of UMs defeated flag
        data = json.load(file)
        for i in range(0, 4):
           data["rows"].append({"$id": FlagListRows[i], "FlagType": 8, "FlagID": 2164, "FlagMin": NumberofUMstoDefeat[i], "FlagMax": 256})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common_ms/fld_quest_achievement.json", 'r+', encoding='utf-8') as file: #modifying the text files that describe what you need to do to unlock the node
        data = json.load(file)
        for i in range(0, 4):
            for row in data["rows"]:
                if row["$id"] == TaskLogIDs[i]:
                    row["name"] = f"Defeat {NumberofUMstoDefeat[i]} total Unique Monsters."
                    break
            for row in data["rows"]:
                if row["$id"] == 663:
                    row["name"] = "Unlocked once you unlock the \n corresponding Trust Level."
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def UMHuntMenuTextChanges():
    seedhashcomplete = random.choice(IDs.SeedHashAdj) + " " + random.choice(IDs.SeedHashNoun) 
    with open("./XC2/_internal/JsonOutputs/common_ms/menu_ms.json", 'r+', encoding='utf-8') as file: #puts the seed hash text on the main menu and on the save game screen
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 128:
                row["name"] = f"Seed Hash: [System:Color name=green]{seedhashcomplete}[/System:Color]"
                row["style"] = 166
            if row["$id"] == 129:
                row["name"] = "[System:Color name=tutorial]Unique Monster Hunt[/System:Color]"
            if row["$id"] in [983, 1227]:
                row["name"] = "Bounties"
            if row["$id"] == 1644:
                row["name"] = f"{seedhashcomplete}"
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/menu_main_contents_ms.json", 'r+', encoding='utf-8') as file: # Changes the name of "Expansion Pass"
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 10:
                row["name"] = "Voucher Rewards"
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/menu_sub_contents_ms.json", 'r+', encoding='utf-8') as file: # Changes the name of "Expansion Pass"
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 61:
                row["name"] = "Voucher Rewards"
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_landmark.json", 'r+', encoding='utf-8') as file: # Changes the name of "Expansion Pass"
        data = json.load(file)
        for row in data["rows"]:
            rownum = row["$id"]
            match rownum:
                case 4:
                    row["name"] = "[System:Color name=green]Bounty Token[/System:Color] Exchange"
                    break
                case 3:
                    row["name"] = "[System:Color name=tutorial]Doubloon[/System:Color] Bazaar"
                case _:
                    continue
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)      

def PoppiswapCostChanges(): # Reduces cost of poppiswap stuff
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/ITM_HanaArtsEnh.json","./XC2/_internal/JsonOutputs/common/ITM_HanaAssist.json", "./XC2/_internal/JsonOutputs/common/ITM_HanaAtr.json", "./XC2/_internal/JsonOutputs/common/ITM_HanaNArtsSet.json", "./XC2/_internal/JsonOutputs/common/ITM_HanaRole.json"], ["NeedEther", "DustEther"], ['max(row[key] // 4, 1)'])
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_HanaPower.json"], ["EtherNum1", "EtherNum2", "EtherNum3"], ['max(row[key] // 4, 1)'])
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/BTL_HanaBase.json"], ["Circuit4Num", "Circuit5Num", "Circuit6Num"], ['max(row[key] // 10, 1)'])

def Description():
    UMHuntDesc = PopupDescriptions.Description()
    UMHuntDesc.Header("General Information")
    UMHuntDesc.Tag("Setup")
    UMHuntDesc.Text("Unique Monster Hunt uses a custom starting save file.")
    UMHuntDesc.Text("This save file can be found in the Randomizer download, in the folder titled 'UM Hunt Save'.")
    UMHuntDesc.Text("CONSOLE: Use a homebrew save file manager and place the save file in the correct spot on your SD card.")
    UMHuntDesc.Text(r"EMULATOR: To use this custom starting save file, place it in the emulator file path \nand\user\save\0000000000000000\BF50755B382CCC6AC0A69D441CBBF62C\0100E95004038000")
    UMHuntDesc.Tag("Objective")
    UMHuntDesc.Text(r"Defeat all waves of Unique Monsters to win!")
    UMHuntDesc.Header("Suboptions")
    UMHuntDesc.Tag("Superboss Wave")
    UMHuntDesc.Text(r"If you chose 10 waves in the spinbox, and also selected this suboption, you will also get 5 additional waves of Superbosses, on areas you have previously visited.")
    UMHuntDesc.Text(r"Defeat those waves to warp to the credits!")
    UMHuntDesc.Tag("Random Starting Landmarks")
    UMHuntDesc.Text(r"If you chose the suboption 'Random Starting Landmarks', then the Landmarks you receive through the DLC rewards will be for random locations on the map.")
    UMHuntDesc.Header("Gameplay Information")
    UMHuntDesc.Text(r"Start your run by walking down the stairs to discover your first area!")
    UMHuntDesc.Text(r"At the start of each area, go to the DLC Items slot, renamed 'Voucher Reward'.")
    UMHuntDesc.Image("UMHunt_voucher_reward.png", "XC2", 700)
    UMHuntDesc.Text(r"Collect all rewards available from the DLC by pressing Y.")
    UMHuntDesc.Text(r"This will give you Bounty Tokens, which are traded in at the Argentum Trade Guild, near the Lemour Inn skip travel point.")
    UMHuntDesc.Image("UMHunt_bounty_token_shop.png", "XC2", 700)
    UMHuntDesc.Text(r"Doing so will in turn give you some EXP, SP, and Doubloons.")
    UMHuntDesc.Text(r"These Doubloons are used in the Argentum shops on the first floor to buy items for your characters, and the EXP/SP are crucial to making sure you are keeping up with the growing strength of the Unique Monsters!")
    UMHuntDesc.Image("UMHunt_shops.png", "XC2", 700)
    UMHuntDesc.Text(r"The shops may move between rounds, and the loot in most of them is randomly generated for each round, so if you see something you like, buy it now, as you may not see it again!")
    UMHuntDesc.Text(r"The loot in the shops becomes better as more rounds go on.")
    UMHuntDesc.Text(r"Also received from the DLC rewards are Landmarks, which allow for easier traversal of the maps.")
    UMHuntDesc.Text(r"If you chose the suboption 'Random Starting Landmarks', then the Landmarks you receive through the DLC rewards will be for random locations on the map.")
    UMHuntDesc.Text(r"When you have powered up enough, go defeat the Unique Monsters.")
    UMHuntDesc.Image("UMHunt_enemy.png", "XC2", 700)
    UMHuntDesc.Text(r"When all 4 have been defeated, you will progress to the next area and next set of Unique Monsters.")
    UMHuntDesc.Text(r"Keep an eye out for Secret Shops on the maps with Unique Monsters, denoted by a green dot when you are close enough to see it on the map, but not in the menu.")
    UMHuntDesc.Text(r"These Secret Shops have loot you can't find anywhere else, and so they're very helpful.")
    UMHuntDesc.Text(r"Each map has a 50% chance to spawn a Secret Shop, and it will replace one random NPC on that map if it does spawn in.")
    UMHuntDesc.Text(r"You can tell whether a Secret Shop has spawned on the map by seeing if any regular NPC on that map has any option to talk to them above their head, and if not, then a Secret Shop has spawned.")
    UMHuntDesc.Image("UMHunt_SecretShop.png", "XC2", 700)
    UMHuntDesc.Text(r"Unique Monsters may also drop loot when defeated.")
    UMHuntDesc.Text(r"The loot they drop will be weaker than the loot in shops, but should still allow you to make a viable build with those items.")
    UMHuntDesc.Text(r"Beating all sets of Unique Monsters will warp you to the credits.")
    UMHuntDesc.Text(r"If you chose 10 waves, and also selected the 'Superboss Wave' suboption, you will also get 5 additional waves of Superbosses, on areas you have previously visited.")
    UMHuntDesc.Text(r"Defeat those waves to warp to the credits!")
    UMHuntDesc.Header(r"Ignored Settings")
    UMHuntDesc.Text(r"This mode uses a lot of randomization features already by default, and so it will override the following settings, as the mode was balanced around having some of these on or off:")
    UMHuntDesc.Text(r"• Accessory Shops")
    UMHuntDesc.Text(r"• Collection Points")
    UMHuntDesc.Text(r"• Pouch Item Shops")
    UMHuntDesc.Text(r"• Treasure Chests")
    UMHuntDesc.Text(r"• Weapon Chip Shops")
    UMHuntDesc.Text(r"• Driver Accessories")
    UMHuntDesc.Text(r"• Blade Aux Cores")
    UMHuntDesc.Text(r"• Blade Weapon Chips")
    UMHuntDesc.Text(r"• Enemies")
    UMHuntDesc.Text(r"• Enemy Drops")
    UMHuntDesc.Text(r"• Faster Blade Skill Trees")
    UMHuntDesc.Text(r"• Faster Driver Skill Trees")
    UMHuntDesc.Text(r"• Faster Levels")
    UMHuntDesc.Text(r"• NG+ Blades")
    UMHuntDesc.Text(r"• Race Mode")
    return UMHuntDesc