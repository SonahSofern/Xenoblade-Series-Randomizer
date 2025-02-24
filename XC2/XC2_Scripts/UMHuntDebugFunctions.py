import json, random, IDs, EnemyRandoLogic, RaceMode, math, Options, time, FieldSkillAdjustments
from Enhancements import *
from BladeRandomization import Replacement2Original
from scripts import Helper
from UMHuntMain import *

AllUniqueMonsterDefaultIDs = [611, 612, 705, 706, 707, 708, 709, 710, 711, 712, 713, 715, 736, 738, 808, 809, 810, 811, 812, 814, 815, 816, 817, 819, 890, 891, 892, 893, 894, 895, 896, 898, 899, 926, 929, 953, 954, 955, 957, 958, 1019, 1020, 1023, 1025, 1026, 1101, 1102, 1104, 1106, 1108, 1109, 1111, 1112, 1113, 1114, 1115, 1131, 1132, 1134, 1155, 1156, 1157, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1255, 1256, 1258, 1260, 1261, 1262, 1264, 1265, 1563, 1564, 1566, 1567, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1670, 1774]
AllSuperBossDefaultIDs = [247, 714, 928, 1022, 1027, 1110, 1135, 1137, 1189, 1559, 1560, 1561, 1562, 1723, 1756, 1758, 1759, 1763, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1775, 1776, 1777, 1778, 1779, 1783, 1784, 1785, 1786, 1792, 1793, 1794, 1795, 1800, 1802, 1803, 1804, 1808, 1809, 1811, 1812, 1813, 1814, 1886]
AllNormalEnemyDefaultIDs = [313, 315, 339, 413, 476, 521, 523, 555, 568, 630, 631, 632, 633, 634, 638, 645, 646, 647, 648, 651, 652, 653, 655, 656, 659, 660, 662, 664, 665, 666, 668, 675, 676, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 691, 692, 694, 695, 699, 701, 703, 716, 717, 718, 719, 720, 721, 722, 723, 729, 730, 731, 732, 734, 749, 756, 757, 758, 762, 763, 764, 766, 771, 772, 773, 774, 794, 795, 796, 798, 800, 802, 804, 806, 825, 835, 843, 844, 847, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 865, 867, 868, 869, 870, 872, 873, 874, 875, 876, 877, 879, 880, 881, 882, 884, 886, 888, 901, 902, 903, 904, 905, 906, 907, 908, 909, 911, 912, 913, 914, 915, 916, 917, 918, 919, 922, 924, 931, 933, 937, 940, 941, 942, 945, 950, 951, 952, 959, 960, 961, 962, 963, 974, 977, 978, 979, 980, 981, 983, 989, 990, 991, 992, 994, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1015, 1016, 1017, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1050, 1051, 1060, 1061, 1063, 1064, 1069, 1070, 1072, 1073, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1098, 1100, 1127, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1171, 1176, 1177, 1178, 1190, 1191, 1192, 1193, 1194, 1195, 1198, 1208, 1209, 1213, 1214, 1217, 1221, 1222, 1228, 1232, 1233, 1235, 1241, 1251, 1254, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1276, 1277, 1279, 1281, 1282, 1283, 1284, 1286, 1287, 1288, 1320, 1321, 1322, 1324, 1326, 1329, 1366, 1380, 1396, 1399, 1421, 1455, 1456, 1459, 1460, 1461, 1462, 1463, 1464, 1466, 1473, 1474, 1476, 1477, 1478, 1479, 1483, 1487, 1488, 1496, 1498, 1500, 1501, 1503, 1507, 1508, 1511, 1513, 1515, 1522, 1529, 1530, 1531, 1532, 1535, 1536, 1539, 1541, 1542, 1543, 1544, 1545, 1547, 1550, 1565, 1570, 1571, 1572, 1573, 1574, 1577, 1578, 1580, 1582, 1583, 1584, 1586, 1587, 1588, 1590, 1591, 1595, 1597, 1600, 1601, 1603, 1606, 1608, 1609, 1611, 1612, 1613, 1617, 1622, 1623, 1624, 1625, 1626, 1627, 1629, 1630, 1631, 1635, 1636, 1637, 1638, 1639, 1640, 1642, 1643, 1645, 1646, 1647, 1649, 1650, 1652, 1656, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1728, 1729, 1730, 1732, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1757, 1760, 1761, 1762, 1764, 1780, 1781, 1782, 1790, 1791, 1796, 1797, 1798, 1799, 1801, 1810, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1882, 1884]
AllQuestDefaultEnemyIDs = [303, 304, 305, 307, 308, 309, 310, 318, 319, 320, 323, 324, 325, 326, 329, 332, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 356, 359, 365, 367, 369, 372, 373, 374, 375, 376, 383, 384, 385, 386, 389, 390, 391, 392, 393, 394, 395, 396, 399, 401, 403, 404, 405, 406, 407, 409, 411, 414, 415, 418, 436, 437, 445, 446, 447, 448, 450, 451, 454, 455, 456, 457, 458, 459, 461, 462, 463, 464, 466, 468, 470, 475, 477, 479, 481, 483, 485, 487, 488, 489, 490, 491, 492, 493, 495, 496, 497, 498, 500, 501, 503, 504, 506, 508, 510, 512, 513, 515, 517, 519, 525, 532, 533, 534, 535, 536, 538, 540, 542, 544, 546, 547, 548, 549, 550, 551, 552, 553, 557, 558, 559, 560, 561, 562, 563, 565, 566, 569, 570, 571, 572, 573, 576, 577, 578, 579, 581, 583, 588, 591, 593, 598, 600, 601, 602, 603, 604, 607, 608, 609, 610, 613, 640, 641, 642, 644, 649, 663, 667, 673, 740, 742, 744, 746, 750, 751, 752, 759, 760, 761, 778, 780, 782, 784, 785, 786, 787, 788, 789, 790, 791, 824, 827, 828, 829, 832, 833, 834, 837, 838, 839, 840, 848, 930, 934, 935, 939, 946, 947, 948, 949, 964, 965, 967, 970, 975, 984, 985, 996, 1035, 1036, 1041, 1053, 1054, 1058, 1059, 1066, 1074, 1075, 1076, 1077, 1078, 1093, 1094, 1095, 1096, 1097, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1128, 1145, 1147, 1148, 1151, 1152, 1153, 1154, 1158, 1159, 1160, 1162, 1164, 1167, 1168, 1169, 1172, 1173, 1174, 1196, 1197, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1212, 1215, 1223, 1226, 1229, 1230, 1231, 1236, 1237, 1238, 1239, 1240, 1242, 1245, 1246, 1248, 1249, 1250, 1343, 1344, 1345, 1348, 1386, 1387, 1388, 1389, 1391, 1393, 1395, 1397, 1398, 1400, 1402, 1404, 1405, 1406, 1407, 1408, 1410, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1422, 1423, 1424, 1425, 1457, 1458, 1465, 1467, 1468, 1469, 1470, 1471, 1472, 1482, 1484, 1485, 1486, 1489, 1490, 1491, 1497, 1499, 1502, 1512, 1516, 1518, 1519, 1526, 1527, 1528, 1534, 1537, 1540, 1546, 1548, 1549, 1551, 1575, 1576, 1579, 1581, 1585, 1589, 1592, 1594, 1596, 1598, 1602, 1604, 1605, 1607, 1610, 1614, 1616, 1618, 1619, 1621, 1628, 1634, 1644, 1648, 1651, 1653, 1655, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1686, 1687, 1688, 1689, 1690, 1888]
AllBossDefaultIDs = [179, 180, 181, 182, 184, 185, 186, 187, 189, 190, 191, 193, 195, 196, 197, 198, 199, 201, 202, 203, 204, 206, 208, 210, 212, 214, 216, 217, 219, 220, 221, 222, 223, 225, 227, 229, 231, 232, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 248, 249, 250, 251, 252, 253, 254, 266, 267, 268, 269, 270, 271, 274, 1342, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1448, 1454, 1632, 1733, 1746, 1747, 1748, 1749, 1754, 1755]
UnusedNormalValidEnemyDefaultIDs = [339, 413, 568, 630, 631, 632, 633, 634, 683, 716, 717, 718, 719, 720, 721, 722, 758, 901, 902, 903, 904, 905, 907, 937, 959, 960, 961, 962, 963, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1190, 1191, 1192, 1193, 1194, 1195, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1276, 1277, 1279, 1281, 1282, 1283, 1284, 1286, 1287, 1288, 1322, 1324, 1366, 1380, 1396, 1421, 1455, 1456, 1459, 1460, 1461, 1462, 1463, 1464, 1466, 1473, 1474, 1476, 1477, 1478, 1479, 1483, 1487, 1488, 1496, 1498, 1500, 1501, 1503, 1507, 1508, 1511, 1513, 1515, 1522, 1529, 1530, 1531, 1532, 1535, 1536, 1539, 1541, 1542, 1543, 1544, 1545, 1547, 1550, 1565, 1570, 1571, 1572, 1573, 1574, 1577, 1578, 1580, 1582, 1583, 1584, 1586, 1587, 1588, 1590, 1591, 1595, 1597, 1600, 1601, 1603, 1606, 1608, 1609, 1611, 1612, 1613, 1617, 1622, 1623, 1624, 1625, 1626, 1627, 1629, 1630, 1631, 1635, 1636, 1637, 1638, 1639, 1640, 1642, 1643, 1645, 1646, 1647, 1649, 1650, 1652, 1656, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1728, 1729, 1730, 1732, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1757, 1760, 1761, 1762, 1764, 1780, 1781, 1782, 1790, 1791, 1796, 1797, 1798, 1799, 1801, 1810, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1882, 1884]
ContinentInfo = {"Gormott": [10043, 10044, "ma05a", 6], "Uraya": [10088, 10079, "ma07a", 9], "Mor Ardain": [10156, 10149, "ma08a", 10], "Leftheria": [10197, 10192, "ma15a", 14], "Temperantia": [10233, 10224, "ma10a", 11], "Tantal": [10272, 10269, "ma13a", 13], "Spirit Crucible": [10325, 10323, "ma16a", 15], "Cliffs of Morytha": [10351, 10345, "ma17a", 16], "Land of Morytha": [10369, 10363, "ma18a", 18], "World Tree": [10399, 10393, "ma20a", 20]}

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

def DebugEnemyLevels(ChosenAreaOrder):
    AllAreasEnemies = []
    TotalAreasEnemies = []
    for k in range(0, len(ChosenAreaOrder)):
        CurrentAreasEnemies = []
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[k]][2] + "_FLD_EnemyPop.json"
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for k in range(1, 5):
                    if row[f"ene{k}ID"] == 0:
                        break
                    elif row[f"ene{k}num"] != 0:
                        CurrentAreasEnemies.append(row[f"ene{k}ID"])
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        AllAreasEnemies.append(CurrentAreasEnemies)
        TotalAreasEnemies.extend(list(set(CurrentAreasEnemies)))
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(ChosenAreaOrder)):
            for row in data["rows"]:
                if (row["$id"] in AllAreasEnemies[i]) & (row["Lv"] not in [5+12*i, 115, 125, 135, 145, 155]): #if the enemy level doesnt match what it should
                    print(f"{row['$id']} is not the correct level for {ChosenAreaOrder[i]}! It should be level {5+12*i}.")
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(len(TotalAreasEnemies)):
        numofenemy = TotalAreasEnemies.count(TotalAreasEnemies[i])
        if numofenemy > 1:
            print(f"{TotalAreasEnemies[i]} appears {numofenemy} times!")

def DebugFindMonsters(ChosenAreaOrder): # was used to debug and find enemies that spawned in too often. If the objective pointer points towards defeating an enemy of which there are 16 or more on the map you're on, the game will freeze upon loading.
    enemycountholder = Helper.ExtendListtoLength([0], len(AllNormalEnemyDefaultIDs),"0")
    for i in range(0, len(ChosenAreaOrder)):
        enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_EnemyPop.json"
        with open(enemypopfile, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for k in range(1, 5):
                    if row[f"ene{k}ID"] == 0:
                            break
                    else:
                        for j in range(0, len(AllNormalEnemyDefaultIDs)):
                            if row[f"ene{k}ID"] == AllNormalEnemyDefaultIDs[j]:
                                enemycountholder[j] += row[f"ene{k}num"]
                                break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    toolargepool = {
        "IDs": [],
        "Counts": []
    }
    for i in range(0, len(enemycountholder)):
        if enemycountholder[i] >= 10: # I chose 10 as an arbitrary number under 16. 
            toolargepool["IDs"].append(AllNormalEnemyDefaultIDs[i])
            toolargepool["Counts"].append(enemycountholder[i])
    print(toolargepool)

def DebugItemsPlace(): #need to place some tokens to play around with them in the shops
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 209:
                row["itm1ID"] = 25488
                row["itm1Num"] = 1
                row["itm2ID"] = 25487
                row["itm2Num"] = 1
                row["itm3ID"] = 25489
                row["itm3Num"] = 1
                row["itm4ID"] = 25485
                row["itm4Num"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DebugEasyMode(): # if this is on, enemies will be lv 1, makes it easier to playtest
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # Adjusted their levels
        data = json.load(file)
        for row in data["rows"]:
            row["Lv"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def DebugSpawnCountPrint(EnemySets, ChosenAreaOrder): # Prints how many times an enemy spawns, think it's causing a crash
    debugfilename = "D:/XC2 Rando Debug Logs/EnemyCounting.txt"
    debugfile = open(debugfilename, "w", encoding= "utf-8")
    for k in range(0, len(ChosenAreaOrder)):
        for i in range(0, len(IDs.ValidEnemyPopFileNames)):
            if ContinentInfo[ChosenAreaOrder[k]][2] in IDs.ValidEnemyPopFileNames[i]:
                enemypopfile = "./XC2/_internal/JsonOutputs/common_gmk/" + IDs.ValidEnemyPopFileNames[i]
                AreaUMCount = [0,0,0,0]
                with open(enemypopfile, 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data["rows"]:
                        for j in range(0, len(EnemySets[k])):
                            for l in range(1, 5):
                                if row[f"ene{l}ID"] == EnemySets[k][j]:
                                    AreaUMCount[j] += row[f"ene{l}num"]
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2, ensure_ascii=False)
                debugfile.write(f"{ChosenAreaOrder[k]}\n\n")
                for j in range(0, 4):
                    debugfile.write(f"ID:{EnemySets[k][j]} Count:{AreaUMCount[j]}\n")  
    debugfile.close()

def DebugGetNPCIDs(): # was used to figure out how many instances of an npc show up in the argentum bazaar. Checked by running around there myself
    TargetedNPCIDs = []
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        CurNPC = 0
        NPCCount = 0
        CurCount = 3 # change this to change what version of an npc shows up (zero-indexed)
        for row in data["rows"]:
            CurNPC = row["NpcID"]
            NPCCount = 0
            for row2 in data["rows"]:
                if row2["NpcID"] == CurNPC:
                    CurNPC2 = row2["$id"]
                    if NPCCount < CurCount:
                        NPCCount += 1
                        row2["ShopID"] = 0
                        row2["flag"]["Talkable"] = 0
                        row2["EventID"] = 0
                        row2["QuestFlag"] = 0
                        row2["ScenarioFlagMin"] = 10047
                        row2["ScenarioFlagMax"] = 10048
                        row2["QuestID"] = 0
                    elif NPCCount == CurCount:
                        row2["flag"]["Talkable"] = 1
                        row2["QuestFlag"] = 0
                        row2["ScenarioFlagMin"] = 1001
                        row2["ScenarioFlagMax"] = 10048
                        row2["Condition"] = 0
                        row2["Mot"] = 0
                        row2["TimeRange"] = 0
                        row2["QuestID"] = 0
                        row2["ShopID"] = 0
                        row2["EventID"] = 41123
                        row2["Visible_XZ"] = 100
                        row2["Visible_Y"] = 10
                        row2["Invisible_XZ"] = 105
                        row2["Invisible_Y"] = 15
                        TargetedNPCIDs.append(row2["$id"])
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
pass

def DebugFindIDForName():
    Instance1NPCNames = ["Shoon", "Hiyaya", "Melolo", "Pupunin", "Lhagen", "Hatatat", "Mitutu", "Motata", "Kynon", "Amumu", "Temimi", "Neyaya", "Pelala", "Mamalu", "Nunana", "Bonbon", "Momoni", "Denden", "Zuzu"]
    Instance2NPCNames = ["Helehele", "Pupunin", "Shynini", "Pelala", "Motata", "Mitutu", "Kynon", "Lutie", "Kux", "Ysolde", "Melolo", "Lhagen", "Hatatat", "Max", "Momoni", "Tonadon", "Garram", "Kokoi", "Pilopilo", "Shoon"]
    Instance3NPCNames = ["Melolo", "Lutie", "Kux", "Garram", "Kokoi", "Pilopilo", "Shoon", "Lhagen", "Kynon", "Helehele", "Pupunin", "Krujah", "Rurui", "Max"]
    Instance4NPCNames = ["Melolo", "Kynon", "Garram", "Pilopilo", "Shoon", "Lhagen", "Rurui", "Max", "Helehele", "Krujah"]

    NPCNames = Instance4NPCNames
    fldnpcnameIDs = []
    RSCNPCIDs = []
    MATWOIDs = []

    with open("./XC2/_internal/JsonOutputs/common_ms/fld_npcname.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(NPCNames)):
            for row in data["rows"]:
                if row["name"] == NPCNames[i]:
                    fldnpcnameIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/RSC_NpcList.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(fldnpcnameIDs)):
            for row in data["rows"]:
                if row["Name"] == fldnpcnameIDs[i]:
                    RSCNPCIDs.append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
        data = json.load(file)
        for i in range(0, len(RSCNPCIDs)):
            FoundInstance = 0
            for row in data["rows"]:
                if row["NpcID"] == RSCNPCIDs[i]:
                    if FoundInstance == 3: # change this to change the instance
                        MATWOIDs.append(row["$id"])
                        break
                    else:
                        FoundInstance += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(MATWOIDs)
    pass