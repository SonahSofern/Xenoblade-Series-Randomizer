import json
import os
from tkinter import filedialog
import tkinter as tk
import JSONParser
import Helper
import random

BossDefaultEnem1Levels = [1, 2, 4, 5, 4, 6, 8, 10, 12, 13, 13, 15, 22, 26, 60, 20, 21, 22, 24, 23, 23, 24, 24, 29, 31, 32, 29, 31, 32, 32, 34, 33, 39, 42, 42, 43, 46, 35, 44, 52, 56, 54, 60, 60, 52, 50, 60, 60, 60, 57, 66, 68, 60, 60, 60, 60, 70, 70, 8, 10, 29, 29, 40, 38, 50, 50, 50, 50, 1, 1, 1, 2, 2, 3, 32, 32, 32, 32, 14, 20, 53]
BossDefaultEnem2Levels = [6, 8, 11, 13, 13, 22, 25, 18, 26, 26, 27, 29, 33, 34, 39, 42, 44, 44, 54, 56, 50, 57, 10, 38, 48, 1, 10, 16]
BossDefaultEnem3Levels = [24, 19, 42, 60, 11, 17]
BossDefaultEnem4Levels = [18]

BossDefaultStageSpecificEnem1IDs = [1001, 4001, 4002, 4003, 4004, 5001, 5500, 5501, 5502, 5503, 5504, 5505, 5506, 5507, 5549, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 11001, 11002, 13001, 13002, 13003, 15001, 16149, 17001, 17002, 17003, 17005, 17006, 18001, 18002, 18003, 18004, 18100, 20001, 20002, 20003, 21001, 21002, 21003, 21004, 21005, 21006, 40001, 40002, 40003, 40004, 40008, 40009, 40010, 40011, 40012, 40013, 40014, 40015, 40016, 40547, 40548, 40549, 40561, 40562, 40563, 40564, 41001, 41002, 42001]
BossDefaultEnem1IDs = [179, 180, 181, 182, 1319, 184, 185, 187, 190, 191, 192, 193, 195, 198, 256, 199, 203, 204, 206, 208, 210, 212, 267, 216, 217, 227, 220, 221, 222, 269, 225, 270, 235, 236, 237, 238, 241, 229, 242, 243, 245, 272, 260, 262, 248, 249, 250, 274, 258, 252, 253, 254, 256, 258, 260, 262, 265, 275, 1431, 1433, 1441, 1442, 1443, 1444, 1446, 1447, 1449, 1450, 1451, 1452, 1453, 1430, 1429, 1454, 1632, 1632, 1632, 1632, 1434, 1437, 1448]

BossDefaultStageSpecificEnem2IDs = [5500, 5501, 5502, 5503, 5504, 5506, 5507, 7001, 7007, 7008, 8002, 8004, 8008, 8009, 11001, 13001, 13002, 16149, 17002, 17003, 18002, 20001, 40002, 40009, 40010, 40548, 41001, 41002]
BossDefaultEnem2IDs = [186, 185, 189, 192, 266, 195, 196, 201, 214, 268, 219, 220, 223, 271, 235, 237, 240, 242, 244, 273, 249, 252, 1432, 1444, 1445, 1428, 1435, 1438]

BossDefaultStageSpecificEnem3IDs = [197, 202, 239, 251, 1436, 1439]
BossDefaultEnem3IDs = [5507, 7001, 13002, 20001, 41001, 41002]

BossDefaultStageSpecificEnem4IDs = [41002]
BossDefaultEnem4IDs = [1440]

QuestDefaultEnemyIDs = [1, 1, 179, 180, 181, 182, 184, 0, 0, 0, 0, 0, 190, 191, 266, 193, 0, 201, 202, 203, 204, 206, 208, 210, 0, 214, 0, 214, 216, 0, 227, 220, 221, 222, 269, 0, 225, 0, 225, 195, 196, 197, 0, 229, 1342, 231, 237, 237, 0, 239, 240, 241, 235, 236, 242, 243, 0, 245, 0, 245, 248, 249, 250, 274, 0, 253, 254, 256, 258, 0, 262, 264, 265, 264, 275, 604, 80, 80, 296, 298, 0, 303, 304, 305, 307, 0, 310, 311, 0, 318, 276, 276, 276, 320, 323, 324, 325, 326, 329, 330, 595, 0, 332, 276, 334, 0, 395, 0, 338, 0, 481, 481, 496, 496, 503, 497, 497, 503, 498, 498, 503, 508, 0, 0, 340, 341, 342, 347, 348, 348, 349, 350, 352, 354, 276, 797, 356, 948, 930, 359, 360, 364, 365, 367, 369, 371, 0, 0, 376, 377, 276, 276, 276, 383, 384, 385, 0, 389, 0, 393, 398, 0, 0, 0, 0, 276, 414, 415, 416, 418, 968, 419, 422, 423, 436, 437, 438, 443, 0, 448, 439, 440, 441, 442, 450, 451, 454, 455, 458, 459, 461, 462, 462, 461, 0, 461, 463, 0, 466, 0, 470, 472, 473, 475, 477, 0, 481, 481, 0, 479, 479, 479, 0, 0, 0, 0, 0, 496, 497, 498, 0, 0, 512, 0, 0, 0, 0, 0, 546, 547, 548, 0, 552, 553, 0, 559, 560, 560, 0, 0, 564, 564, 564, 565, 566, 567, 0, 0, 570, 571, 572, 573, 0, 576, 577, 0, 588, 0, 598, 0, 0, 0, 0, 0, 0, 0, 0, 613, 0, 0, 0, 1118, 1131, 932, 1146, 0, 957, 751, 1200, 1119, 752, 1116, 830, 1132, 767, 0, 0, 0, 1175, 827, 0, 1199, 1025, 779, 1224, 949, 1160, 0, 775, 0, 0, 0, 0, 1229, 0, 0, 0, 965, 0, 0, 0, 1121, 809, 0, 936, 0, 1155, 0, 1227, 0, 1146, 1174, 948, 1113, 930, 0, 755, 1020, 1219, 775, 938, 1156, 1229, 1146, 0, 1230, 1119, 0, 0, 0, 1175, 1224, 0, 1260, 1203, 1157, 1218, 1159, 1227, 946, 0, 1201, 932, 0, 1165, 1182, 1210, 1264, 1160, 1119, 1185, 1226, 1230, 0, 1261, 747, 1202, 0, 1159, 970, 1116, 967, 1117, 1234, 1134, 996, 0, 1181, 779, 842, 949, 1265, 1234, 1174, 748, 985, 0, 748, 1126, 810, 1256, 1131, 1134, 812, 1258, 1132, 893, 890, 815, 1155, 1157, 709, 1255, 1156, 1186, 713, 895, 957, 1187, 808, 896, 958, 1023, 711, 894, 1020, 1025, 705, 891, 1261, 706, 892, 1113, 0, 1023, 1201, 1186, 636, 0, 822, 0, 0, 822, 760, 1159, 840, 0, 1165, 0, 0, 975, 1264, 0, 944, 958, 0, 957, 1262, 975, 930, 778, 938, 1174, 0, 944, 0, 1158, 841, 1205, 1041, 1125, 1134, 1200, 0, 1218, 1260, 0, 1231, 1187, 0, 827, 1131, 1042, 755, 0, 0, 0, 1183, 0, 0, 1146, 0, 1174, 967, 1118, 1210, 1262, 0, 1160, 1261, 1119, 0, 0, 1173, 932, 0, 930, 1225, 1131, 778, 946, 1126, 748, 0, 0, 743, 1132, 1234, 0, 743, 1117, 1118, 1216, 1158, 748, 0, 1120, 1025, 1242, 0, 1165, 1159, 0, 1184, 1125, 1165, 1104, 649, 650, 669, 0, 739, 740, 741, 744, 746, 0, 765, 759, 753, 775, 767, 821, 824, 834, 0, 826, 827, 831, 830, 0, 713, 0, 0, 0, 1196, 0, 1116, 1199, 939, 1122, 1203, 946, 1126, 1229, 930, 1125, 1225, 936, 0, 1216, 948, 1119, 1219, 943, 1121, 1204, 938, 1145, 1158, 1146, 1159, 1147, 1160, 1148, 1165, 0, 0, 0, 0, 0, 0, 1152, 1173, 1153, 1174, 1154, 0, 0, 0, 1169, 0, 219, 234, 251, 0, 0, 456, 457, 319, 564, 564, 1343, 1343, 564, 0, 1388, 1393, 1391, 1389, 1395, 0, 1404, 0, 1412, 1417, 1422, 1418, 0, 1415, 1416, 1417, 0, 1431, 0, 0, 0, 1441, 1442, 1632, 1443, 1444, 0, 1447, 1448, 1405, 1406, 1457, 1458, 0, 0, 0, 0, 1468, 1468, 1482, 1469, 1465, 1674, 0, 0, 1681, 1197, 1109, 1188, 708, 899, 736, 814, 671, 775, 1046, 1122, 0, 663, 1223, 947, 1167, 828, 984, 1119, 1147, 1491, 0, 635, 1470, 1471, 1472, 1467, 1486, 1484, 1581, 1527, 1489, 1489, 1490, 1485, 1632, 1632, 1502, 1616, 1579, 1499, 1592, 1593, 1497, 1596, 1607, 1634, 1576, 1548, 1653, 1537, 1512, 1628, 1516, 1549, 1546, 1614, 1618, 1604, 1605, 1644, 1518, 1551, 1594, 1621, 1585, 1602, 1648, 1528, 1610, 1540, 1534, 1655, 1619, 1651, 1598, 1575, 1533, 1526, 1589, 1519, 0, 0, 1682, 1683, 792, 1196, 1042, 829, 752, 1207, 1047, 833, 744, 1216, 1049, 739, 1218, 832, 753, 1071, 848, 1225, 1043, 837, 1425, 1682, 1468, 661, 761, 964, 938, 1159, 1468]
QuestDefaultEnemyGroupIDs = [0, 0, 0, 0, 0, 0, 0, 75, 0, 76, 0, 77, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 79, 0, 89, 0, 0, 81, 0, 0, 0, 0, 0, 82, 0, 90, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 83, 0, 0, 0, 0, 0, 0, 0, 84, 0, 91, 0, 0, 0, 0, 0, 85, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 103, 0, 0, 0, 0, 93, 0, 0, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 94, 0, 0, 0, 13, 0, 14, 0, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 62, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 11, 0, 0, 15, 16, 17, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 0, 68, 0, 69, 0, 0, 0, 0, 0, 72, 0, 0, 73, 0, 0, 0, 1, 2, 98, 98, 3, 0, 0, 0, 4, 70, 0, 5, 6, 7, 66, 67, 0, 0, 0, 8, 0, 0, 74, 0, 0, 0, 99, 9, 0, 0, 0, 0, 0, 0, 106, 106, 0, 0, 0, 0, 0, 0, 0, 96, 0, 97, 0, 64, 65, 22, 22, 22, 22, 22, 22, 0, 0, 23, 110, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 25, 42, 0, 0, 115, 0, 0, 0, 0, 0, 0, 122, 0, 44, 36, 39, 123, 0, 44, 36, 39, 0, 49, 43, 111, 0, 0, 38, 0, 44, 0, 39, 0, 110, 0, 0, 0, 0, 0, 116, 0, 0, 0, 0, 0, 0, 0, 0, 26, 0, 0, 25, 45, 48, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 108, 0, 0, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 0, 0, 119, 0, 119, 50, 0, 0, 0, 0, 115, 0, 119, 115, 0, 0, 27, 0, 0, 121, 0, 0, 0, 0, 0, 0, 0, 108, 0, 28, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 29, 0, 0, 24, 0, 0, 0, 0, 116, 120, 30, 0, 30, 33, 0, 109, 0, 0, 0, 0, 0, 104, 0, 0, 0, 37, 105, 0, 0, 116, 0, 0, 0, 0, 0, 0, 0, 46, 50, 0, 0, 0, 49, 0, 0, 0, 0, 0, 0, 46, 0, 0, 0, 120, 0, 0, 115, 0, 0, 0, 0, 0, 0, 0, 102, 0, 0, 0, 0, 0, 108, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 0, 0, 0, 105, 0, 51, 53, 54, 0, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 114, 118, 124, 119, 113, 120, 0, 0, 0, 0, 0, 115, 116, 117, 0, 63, 0, 0, 0, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 125, 0, 0, 0, 0, 0, 127, 0, 128, 0, 0, 0, 0, 136, 0, 0, 0, 139, 0, 135, 130, 131, 0, 0, 0, 0, 0, 132, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 137, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 140, 142, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

EnemyGroupDefaultID1s = [487, 487, 493, 500, 513, 517, 532, 549, 561, 385, 390, 393, 394, 396, 399, 403, 403, 407, 445, 487, 487, 606, 640, 639, 780, 739, 838, 641, 741, 1145, 828, 934, 677, 1118, 930, 1120, 1037, 1035, 1052, 1065, 1039, 1074, 1196, 1210, 1236, 1206, 1151, 1244, 1163, 1166, 1255, 953, 1131, 1155, 390, 393, 399, 403, 403, 407, 374, 372, 487, 600, 602, 536, 540, 464, 464, 506, 479, 479, 479, 557, 185, 187, 190, 199, 212, 198, 217, 223, 238, 244, 252, 260, 455, 823, 267, 270, 272, 296, 309, 345, 577, 579, 591, 491, 1344, 1151, 461, 673, 297, 1052, 1123, 569, 838, 750, 768, 1048, 1055, 934, 1151, 1149, 1161, 1162, 1163, 1166, 1168, 1172, 667, 1052, 1052, 1150, 1386, 1389, 1397, 1408, 1412, 1434, 1437, 1446, 0, 1406, 1432, 1419, 1675, 1678, 1430, 1686, 639, 1684]
EnemyGroupDefaultID2s = [488, 488, 495, 501, 515, 519, 533, 550, 562, 386, 391, 397, 390, 390, 400, 404, 406, 408, 446, 488, 488, 607, 642, 640, 781, 740, 839, 642, 742, 1146, 829, 935, 690, 1121, 948, 1123, 1038, 1036, 1053, 1066, 1040, 1075, 1197, 1211, 1237, 1207, 1152, 1245, 1164, 1167, 1256, 954, 1132, 1156, 391, 397, 400, 404, 406, 409, 375, 373, 488, 601, 603, 538, 542, 466, 466, 508, 481, 481, 481, 558, 186, 185, 189, 201, 214, 196, 219, 225, 239, 245, 251, 262, 456, 846, 268, 271, 273, 297, 308, 346, 578, 581, 593, 492, 1345, 1152, 462, 1347, 296, 1365, 1370, 567, 1354, 1351, 1353, 1358, 1359, 1368, 1371, 1372, 1373, 1374, 1375, 1376, 1380, 1381, 724, 1365, 1365, 1372, 1387, 1391, 1398, 1410, 1413, 1435, 1438, 1445, 0, 1407, 1433, 1420, 1676, 1679, 1429, 1687, 641, 1687]
EnemyGroupDefaultID3s = [0, 489, 0, 504, 0, 525, 534, 551, 563, 0, 392, 0, 0, 0, 401, 405, 0, 409, 447, 489, 489, 608, 644, 0, 782, 0, 1354, 697, 0, 1147, 0, 1368, 0, 1122, 949, 1128, 0, 0, 1054, 0, 0, 1076, 0, 1212, 1238, 0, 1153, 1246, 1375, 1376, 1258, 955, 1134, 1157, 392, 0, 401, 405, 0, 411, 0, 0, 489, 0, 0, 0, 544, 468, 468, 510, 0, 483, 483, 0, 0, 0, 0, 202, 0, 197, 0, 0, 240, 0, 0, 0, 457, 0, 0, 0, 0, 0, 0, 0, 0, 583, 0, 0, 0, 1153, 463, 0, 0, 0, 0, 0, 0, 0, 0, 1362, 0, 1369, 0, 0, 0, 0, 0, 1377, 0, 0, 725, 0, 0, 0, 0, 1393, 0, 0, 1414, 1436, 1439, 0, 0, 0, 0, 0, 1677, 1680, 1428, 1690, 0, 1688]
EnemyGroupDefaultID4s = [0, 490, 0, 0, 0, 0, 535, 0, 0, 0, 0, 0, 0, 0, 402, 0, 0, 410, 0, 0, 0, 609, 0, 0, 783, 0, 0, 0, 0, 1148, 0, 1369, 0, 1123, 0, 1370, 0, 0, 1055, 0, 0, 1077, 0, 1215, 1239, 0, 1154, 0, 0, 1377, 1260, 957, 1135, 0, 0, 0, 402, 0, 0, 408, 0, 0, 490, 0, 0, 0, 0, 0, 470, 0, 0, 0, 485, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1378, 0, 0, 1348, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1440, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1689]
EnemyGroupDefaultID5s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 411, 0, 0, 0, 610, 0, 0, 784, 0, 0, 0, 0, 0, 0, 0, 0, 1124, 0, 0, 0, 0, 1058, 0, 0, 1078, 0, 1219, 1240, 0, 1371, 0, 0, 1378, 1261, 958, 1137, 0, 0, 0, 0, 0, 0, 410, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1379, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID6s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 412, 0, 0, 0, 611, 0, 0, 785, 0, 0, 0, 0, 0, 0, 0, 0, 1370, 0, 0, 0, 0, 1059, 0, 0, 1093, 0, 1384, 1248, 0, 0, 0, 0, 1379, 1262, 0, 0, 0, 0, 0, 0, 0, 0, 412, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID7s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 786, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1359, 0, 0, 1094, 0, 318, 1249, 0, 0, 0, 0, 0, 1264, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID8s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 787, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1365, 0, 0, 1095, 0, 0, 1250, 0, 0, 0, 0, 0, 1265, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID9s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 788, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID10s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 789, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1097, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID11s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 790, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EnemyGroupDefaultID12s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 791, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def FindMatchingInfo(file1path, file2path, keyword0, keyword1, keyword2, keyword3): # file 1 path, file 2 path, file 1 header to search through, file 1 header to return data from, file 2 header to search through (same values as keyword1, maybe different header name), file 2 header to return data from
    namemat = []
    IDMat = [] 
    LevelMat = []
    mapspecID = []
    if file1path == "":
        mapname = ""
        i = 1
        j = 1
        for i in range(1,90):
            if i > 10:
                mapnum = str(i)
            if i <= 10:
                mapnum = "0" + str(i)
            for j in range(1,3):
                if j == 1:
                    mapname = "a"
                if j == 2:
                    mapname = "b"
                if j == 3:
                    mapname = "c"
                combinedmapname = "./_internal/JsonOutputs/common_gmk/ma" + mapnum + mapname + "_FLD_EnemyPop.json"
                file1path = combinedmapname
                try:
                    with open(combinedmapname, 'r+', encoding='utf-8') as file:
                        data = json.load(file)
                        for row in data['rows']:
                            if "boss" in row.get(keyword0):
                                if row.get(keyword1) != 0 and row.get(keyword1) != "":
                                    namemat.append(row[keyword1])
                                    mapspecID.append(row["$id"]) 
                except:
                    pass
    else:
        with open(file1path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if "boss" in row.get(keyword0):
                    if row.get(keyword1) != 0 and row.get(keyword1) != "":
                        namemat.append(row[keyword1])
                        mapspecID.append(row["$id"])   
    if file2path == "":
        chrenname = "./_internal/JsonOutputs/common/CHR_EnArrange.json"
        file2path = chrenname
    with open(chrenname, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for k in range(0, len(namemat)):
            idsearch = namemat[k]
            for row in data["rows"]:
                for key, value in row.items():
                    if key in keyword2 and value == idsearch: 
                            IDMat.append(row[keyword2])
                            LevelMat.append(row[keyword3])
    print(namemat)
    print(mapspecID)                    
    print(IDMat)
    print(LevelMat)

def ReverseSpecificChanges(file1path, file2path, keyword0, keyword1, keyword2, keyword3, keyword4, keyword5, inputmatrix, checkcondition): # file 1 path, file 2 path, file 1 header to search through, file 1 header to return data from, file 2 header to search through (same values as keyword1, maybe different header name), file 2 header to return data from, file 2 header for column to revert changes to, file 2 header that the randomized values get reverted to
    namemat = []
    IDMat = []
    LevelMat = []
    mapspecID = []
    BossPostRandomizationEnemIDs = []
    if file1path == "":
        mapname = ""
        i = 1
        j = 1
        for i in range(1,90):
            if i > 10:
                mapnum = str(i)
            if i <= 10:
                mapnum = "0" + str(i)
            for j in range(1,3):
                if j == 1:
                    mapname = "a"
                if j == 2:
                    mapname = "b"
                if j == 3:
                    mapname = "c"
                combinedmapname = "./_internal/JsonOutputs/common_gmk/ma" + mapnum + mapname + "_FLD_EnemyPop.json"
                file1path = combinedmapname
                try:
                    with open(combinedmapname, 'r+', encoding='utf-8') as file:
                        data = json.load(file)
                        for row in data['rows']:
                            if "boss" in row.get(keyword0):
                                if row.get(keyword1) != 0 and row.get(keyword1) != "":
                                    if row.get(checkcondition) != 0:
                                        namemat.append(row[keyword1])
                                        mapspecID.append(row["$id"]) 
                except:
                    pass
    else:
        with open(file1path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if "boss" in row.get(keyword0):
                    if row.get(keyword1) != 0 and row.get(keyword1) != "":
                        if row.get(checkcondition) != 0:
                            namemat.append(row[keyword1])
                            mapspecID.append(row["$id"])   
    if file2path == "":
        chrenname = "./_internal/JsonOutputs/common/CHR_EnArrange.json"
        file2path = chrenname
    with open(chrenname, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for k in range(0, len(namemat)):
            idsearch = namemat[k]
            for row in data["rows"]:
                for key, value in row.items():
                    if key in keyword2 and value == idsearch:
                        IDMat.append(row[keyword2])
                        LevelMat.append(row[keyword3])
        BossPostRandomizationEnemIDs = IDMat
        for k in range(0, len(BossPostRandomizationEnemIDs)):
            for row in data["rows"]:
                for key, value in row.items():
                    if key in keyword4 and value == BossPostRandomizationEnemIDs[k]:
                        row[keyword5] = inputmatrix[k]

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

def ReadPostRandomizationChanges(filepath, keyword1): # file to read after randomization, keyword1 column header
    retIDmatrix = []
    retkey1matrix = []
    with open(filepath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            for key in row.items():
                if key == keyword1:
                    retIDmatrix.append(row["$id"])
                    retkey1matrix.append(row[keyword1])
    return retIDmatrix, retkey1matrix

def ReworkedEnemyRando (DefaultEnemyIDs, RandomizedEnemyIDs):
    for i in range(1,90):
        if i > 10:
            mapnum = str(i)
        if i <= 10:
            mapnum = "0" + str(i)
        for j in range(1,3):
            if j == 1:
                mapname = "a"
            if j == 2:
                mapname = "b"
            if j == 3:
                mapname = "c"
            enemypopfile = "./_internal/JsonOutputs/common_gmk/ma" + mapnum + mapname + "_FLD_EnemyPop.json"
            try:
                with open(enemypopfile, 'r+', encoding='utf-8') as file:
                    data = json.load(file)
                    for row in data['rows']:
                        for k in range(0, len(DefaultEnemyIDs)):
                            for key, value in row.items():
                                if key == "ene1ID" and value == DefaultEnemyIDs[k]:
                                    row[key] = RandomizedEnemyIDs[k]
                                if key == "ene2ID" and value == DefaultEnemyIDs[k]:
                                    if row.get(key) != 0 and row.get(key) != "":
                                        row[key] = RandomizedEnemyIDs[k]
                                if key == "ene3ID" and value == DefaultEnemyIDs[k]:
                                    if row.get(key) != 0 and row.get(key) != "":
                                        row[key] = RandomizedEnemyIDs[k]
                                if key == "ene4ID" and value == DefaultEnemyIDs[k]:
                                    if row.get(key) != 0 and row.get(key) != "":
                                        row[key] = RandomizedEnemyIDs[k]
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)                                               
            except:
                pass
    with open("./_internal/JsonOutputs/common/FLD_QuestBattle.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            for k in range(0, len(DefaultEnemyIDs)):
                for key, value in row.items(): 
                    if key == "EnemyID" and value == DefaultEnemyIDs[k]:
                        if row.get(key) != 0 and row.get(key) != "":
                            row[key] = RandomizedEnemyIDs[k]

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
    with open("./_internal/JsonOutputs/common/FLD_EnemyGroup.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            for k in range(0, len(DefaultEnemyIDs)):
                for key, value in row.items():
                    for l in range (1,13):
                        keymatchval = "EnemyID" + str(l)
                        if key == keymatchval and value == DefaultEnemyIDs[k]:
                            if row.get(key) != 0 and row.get(key) != "":
                                row[key] = RandomizedEnemyIDs[k]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)

    with open("./_internal/JsonOutputs/common/FLD_SalvageEnemySet.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            for k in range(0, len(DefaultEnemyIDs)):
                for key, value in row.items():
                    if key == "ene1ID" and value == DefaultEnemyIDs[k]:
                        row[key] = RandomizedEnemyIDs[k]
                    if key == "ene2ID" and value == DefaultEnemyIDs[k]:
                        if row.get(key) != 0 and row.get(key) != "":
                            row[key] = RandomizedEnemyIDs[k]
                    if key == "ene3ID" and value == DefaultEnemyIDs[k]:
                        if row.get(key) != 0 and row.get(key) != "":
                            row[key] = RandomizedEnemyIDs[k]
                    if key == "ene4ID" and value == DefaultEnemyIDs[k]:
                        if row.get(key) != 0 and row.get(key) != "":
                            row[key] = RandomizedEnemyIDs[k]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)   

def RemoveLevelRanges(Filename):
    with open(Filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            for key, value in row.items():
                if key == "LvRand" and value >= 0:
                    row[key] = 0

def EnemyLogic(CheckboxList, CheckboxStates):
    RandomizedEnemyIDs = []
    ValidEnemies =  [x for x in Helper.inclRange(0,1888) if x not in ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 183, 185, 186, 188, 189, 190, 192, 194, 200, 201, 205, 207, 209, 211, 213, 215, 218, 219, 220, 224, 226, 228, 230, 237, 238, 240, 246, 251, 255, 257, 259, 261, 263, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 306, 311, 312, 314, 316, 317, 321, 322, 327, 328, 330, 331, 333, 334, 335, 336, 337, 338, 340, 343, 344, 353, 354, 355, 357, 358, 360, 361, 362, 363, 364, 366, 368, 370, 371, 377, 378, 379, 380, 381, 382, 387, 388, 397, 398, 400, 402, 408, 410, 412, 416, 417, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 438, 439, 440, 441, 442, 443, 444, 449, 452, 453, 460, 465, 467, 469, 471, 472, 473, 478, 480, 482, 484, 486, 494, 499, 502, 505, 507, 509, 511, 514, 516, 518, 520, 522, 524, 526, 527, 528, 529, 530, 531, 537, 539, 541, 543, 545, 554, 556, 574, 575, 580, 582, 584, 585, 586, 587, 589, 590, 592, 594, 595, 596, 597, 599, 605, 606, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 633, 698, 700, 702, 704, 737, 799, 801, 803, 805, 807, 813, 818, 820, 883, 885, 887, 889, 897, 900, 921, 923, 925, 927, 956, 1012, 1013, 1014, 1021, 1024, 1103, 1105, 1107, 1129, 1130, 1133, 1136, 1179, 1180, 1252, 1253, 1257, 1259, 1263, 1274, 1275, 1278, 1280, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1305, 1306, 1307, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1323, 1325, 1327, 1328, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1346, 1390, 1392, 1394, 1401, 1403, 1409, 1411, 1426, 1427, 1428, 1451, 1452, 1453, 1475, 1480, 1481, 1492, 1493, 1494, 1495, 1504, 1505, 1506, 1509, 1510, 1514, 1517, 1520, 1523, 1524, 1525, 1538, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1615, 1620, 1654, 1668, 1669, 1671, 1672, 1673, 1685, 1750, 1751, 1752, 1753, 1887])]
    DefaultEnemyIDs = ValidEnemies
    RandomizedEnemyIDs = DefaultEnemyIDs
    random.shuffle(RandomizedEnemyIDs)

    for n in range(0, len(CheckboxList)):
        print(CheckboxStates[n].get())
        if CheckboxList[n] == "Randomize Enemies Box" and CheckboxStates[n].get() == True:
            ReworkedEnemyRando(DefaultEnemyIDs, RandomizedEnemyIDs)
            for k in range(0, len(CheckboxList)):
                if CheckboxList[k] == "Story Boss Levels Box" and CheckboxStates[k].get() == True:
                    ReverseSpecificChanges("", "", "name", "ene1ID", "$id", "Lv", "$id", "Lv", BossDefaultEnem1Levels, "ene1num")
                    ReverseSpecificChanges("", "", "name", "ene2ID", "$id", "Lv", "$id", "Lv", BossDefaultEnem2Levels, "ene2num")
                    ReverseSpecificChanges("", "", "name", "ene3ID", "$id", "Lv", "$id", "Lv", BossDefaultEnem3Levels, "ene3num")
                    ReverseSpecificChanges("", "", "name", "ene4ID", "$id", "Lv", "$id", "Lv", BossDefaultEnem4Levels, "ene4num")

            
    RemoveLevelRanges("./_internal/JsonOutputs/common/CHR_EnArrange.json")
