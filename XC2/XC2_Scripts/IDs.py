import scripts.Helper as Helper


#HELPFUL VARIABLES
AuxCores = Helper.InclRange(15001, 15406)
RefinedAuxCores = Helper.InclRange(17001, 17424)
WeaponChips = Helper.InclRange(10001, 10060)
AllCoreCrystals = Helper.InclRange(45001,45057)
CoreCrystals = [45001,45002,45003,45004,45005,45006,45007,45008,45009,45011,45012,45013,45016,45056,45057]
TornaAccessories = Helper.InclRange(585, 647) + Helper.InclRange(657,680)
Accessories = [x for x in Helper.InclRange(1,687) if x not in ([444,445,446,447,448,449,450,451,452,453,454,455,653] + TornaAccessories)]
PreciousItems = Helper.InclRange(25001, 25499)
PouchItems =  [x for x in Helper.InclRange(40001,40428) if x not in ([40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + Helper.InclRange(40350, 40363) + Helper.InclRange(40389, 40402))]   
AutoAttacks = [1, 2, 3, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 43, 44, 45, 50, 51, 52, 57, 58, 59, 64, 65, 66, 67, 68, 69, 78, 79, 80, 81, 82, 83, 92, 93, 94, 95, 96, 97, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 302, 303, 304, 309, 310, 311, 316, 317, 318, 323, 324, 325, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 582, 583, 584, 592, 593, 594, 602, 603, 604, 612, 613, 614, 622, 623, 624, 632, 633, 634, 642, 643, 644, 652, 653, 654, 662, 663, 664, 672, 673, 674, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726]
Boosters = [50001,50002,50003,50004]


ArtBuffs = [0,1,2,3,4,5,6,7,8,16,17] # 9 is a valid Art Buff, Draw Aggro, but we only use this for randomizing the ArtsDebuff field, not the ArtsBuff field, so it effectively does nothing to the enemy
BladeArts = [0,1,2,3,4,5,6,7,8,9]
ArtDebuffs = [0,11,12,13,14,15,21,23,24,25,30,35]
VanillaEnhancements = Helper.InclRange(1,3894)

DriverSkillTrees = Helper.InclRange(1,270)
HitReactions = Helper.InclRange(0,16)
ButtonCombos = Helper.InclRange(1,5)
BladeBattleSkills = list(set(Helper.InclRange(1,270)) - set([268,267,266,265,144,142,143,141,8,9]))   

MajorAreaIds = ["01","02","03","04","05","07","08","10","11","13","15","17","18","20","21","30","40","41","42","49","50","90"]



BladeSpecials = Helper.InclRange(1,269)
BladeTreeUnlockConditions = Helper.InclRange(1,1768)
BladeNames = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 52, 53, 54, 55, 78, 79, 56, 58, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 59, 75, 76, 77, 45, 46, 47, 48, 49, 50, 51, 45, 57, 45, 49, 50, 51, 76, 102, 103, 104, 105, 106, 107, 108]
Jingles = Helper.InclRange(101,116)
CollectionPointMaterials = [x for x in Helper.InclRange(30001,30445) if x not in [30232, 30233, 30237, 30236, 30243, 30244, 30245, 30246]]
Deeds = Helper.InclRange(25249,25300)
AllMusicIDs = Helper.InclRange(1,180)

NonBattleMusicIDs = [1, 2, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 63, 64, 66, 70, 72, 73, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 165, 170, 171, 172, 173, 174, 175, 176, 178]
NonBattleMusicMOVs = ['', 'm47.wav', 'm02.wav', 'm45.wav', 'm50.wav', 'm57.wav', 'm01c.wav', 'm103.wav', 'm91.wav', 'm302.wav', 'm11.wav', 'm17.wav', 'm32.wav', 'm93.wav', 'm69.wav', 'm61.wav', 'm51.wav', 'm48.wav', 'm09.wav', 'event/m100_loop.wav', 'm27.wav', 'm52.wav', 'm46.wav', 'm73.wav', 'm283.wav', 'm22.wav', 'm49.wav', 'event/m18_loop.wav', 'm26.wav', 'm36.wav', 'm89.wav', 'm90.wav', 'm95.wav', 'm99.wav', 'm53.wav', 'm98.wav', 'm97.wav', 'm74.wav', 'm56.wav', 'm70.wav', 'm01.wav', 'm40.wav', 'm43.wav', 'm72.wav', 'm63.wav', 'm28.wav', 'm240.wav', 'm71.wav', 'm15.wav', 'm96.wav', 'm62.wav', 'm18.wav', 'm37.wav', 'm35.wav', 'm33.wav', 'm100.wav', 'm41.wav', 'm01b.wav', 'm03.wav', 'm31.wav', 'm34.wav', 'm252.wav', 'm55.wav', 'm58.wav', 'm01a.wav', 'm248.wav', 'm60.wav', 'm253.wav', 'nodata', 'm92.wav', 'm249.wav', 'event/m14_loop.wav', 'm25.wav', 'm42.wav', 'm24.wav', 'm54.wav', 'm68.wav', 'm04.wav', 'm59.wav', 'event/m97_bf04120110_2.wav', 'm241.wav', 'm30.wav', 'm65.wav', 'm44.wav', 'm39.wav', 'm94.wav', 'm38.wav', 'm23.wav']
EnemyBattleMusicMOVs = ['m67.wav', 'm20.wav', 'm16.wav', 'm14.wav', 'm77.wav', 'm07.wav', 'm281.wav', 'm13.wav', 'm81.wav', 'm82.wav', 'm86.wav', 'm304.wav', 'm78.wav', 'm29.wav', 'm19.wav', 'm76.wav', 'm84.wav', 'm06.wav', 'm282.wav', 'm301.wav', 'm87.wav', 'm21.wav', 'm80.wav', 'm79.wav', 'm64.wav', 'm202.wav', 'm75.wav', 'm72.wav', 'm88.wav', 'm05.wav', 'm203.wav', 'm12.wav', 'm85.wav', 'm66.wav', 'm83.wav', 'm303.wav', 'm10.wav']
ReplacementNonBattleMusicMOVs = ['m47.wav', 'm02.wav', 'm45.wav', 'm50.wav', 'm57.wav', 'm01c.wav', 'm103.wav', 'm91.wav', 'm17.wav', 'm32.wav', 'm93.wav', 'm69.wav', 'm61.wav', 'm51.wav', 'm48.wav', 'm09.wav', 'event/m100_loop.wav', 'm27.wav', 'm52.wav', 'm46.wav', 'm73.wav', 'm283.wav', 'm22.wav', 'm49.wav', 'event/m18_loop.wav', 'm26.wav', 'm36.wav', 'm89.wav', 'm90.wav', 'm95.wav', 'm99.wav', 'm53.wav', 'm97.wav', 'm74.wav', 'm56.wav', 'm70.wav', 'm01.wav', 'm40.wav', 'm43.wav', 'm72.wav', 'm63.wav', 'm28.wav', 'm240.wav', 'm71.wav', 'm15.wav', 'm96.wav', 'm62.wav', 'm18.wav', 'm37.wav', 'm35.wav', 'm33.wav', 'm100.wav', 'm41.wav', 'm01b.wav', 'm03.wav', 'm31.wav', 'm34.wav', 'm252.wav', 'm55.wav', 'm58.wav', 'm01a.wav', 'm248.wav', 'm60.wav', 'm253.wav', 'nodata', 'm92.wav', 'm249.wav', 'event/m14_loop.wav', 'm25.wav', 'm42.wav', 'm24.wav', 'm54.wav', 'm68.wav', 'm04.wav', 'm59.wav', 'event/m97_bf04120110_2.wav', 'm241.wav', 'm30.wav', 'm65.wav', 'm44.wav', 'm39.wav', 'm94.wav', 'm38.wav', 'm23.wav', 'm64.wav']
ValidEnemyMusicIDs = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,49,132,133,157,158,159,160,161,162,163,164,166,167,168,169,177,179,180]
ValidEnemyMusicWAVs = ["m75.wav", "m76.wav", "m77.wav", "m78.wav", "m79.wav", "m80.wav", "m81.wav", "m82.wav", "m83.wav", "m84.wav", "m85.wav", "m86.wav", "m87.wav", "m88.wav", "m202.wav", "m203.wav", "m281.wav", "m282.wav", "m301.wav", "m303.wav", "m304.wav"]
ValidTboxMapNames = ["./XC2/_internal/JsonOutputs/common_gmk/ma02a_FLD_TboxPop.json","./XC2/_internal/JsonOutputs/common_gmk/ma03a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma04a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma05a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma07a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma08a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma10a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma11a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma13a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma15a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma16a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma17a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma18a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma21a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma90a_FLD_TboxPop.json"]
ValidEnemyPopFileNames = ["ma01a_FLD_EnemyPop.json", "ma02a_FLD_EnemyPop.json", "ma04a_FLD_EnemyPop.json", "ma05a_FLD_EnemyPop.json", "ma05c_FLD_EnemyPop.json", "ma07a_FLD_EnemyPop.json", "ma07c_FLD_EnemyPop.json", "ma08a_FLD_EnemyPop.json", "ma08c_FLD_EnemyPop.json", "ma10a_FLD_EnemyPop.json", "ma10c_FLD_EnemyPop.json", "ma11a_FLD_EnemyPop.json", "ma13a_FLD_EnemyPop.json", "ma13c_FLD_EnemyPop.json", "ma15a_FLD_EnemyPop.json", "ma15c_FLD_EnemyPop.json", "ma16a_FLD_EnemyPop.json", "ma17a_FLD_EnemyPop.json", "ma17c_FLD_EnemyPop.json", "ma18a_FLD_EnemyPop.json", "ma18c_FLD_EnemyPop.json", "ma20a_FLD_EnemyPop.json", "ma20c_FLD_EnemyPop.json", "ma21a_FLD_EnemyPop.json", "ma40a_FLD_EnemyPop.json", "ma41a_FLD_EnemyPop.json", "ma42a_FLD_EnemyPop.json"]
InvalidTreasureBoxIDs = [703, 801, 850] # We want to not randomize a broken one inside collision on Mor Ardain, and one in uraya that has a debug item, as well as one in mor ardain with a debug item

BladeDefenseDistribution = [0,0,0,0,5,5,5,5,5,5,5,10,10,10,10,10,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,25,25,25,30,30,35,35,40,40,45,50,55,60,65,70,75,80]
BladeModDistribution = [5,5,5,10,10,10,10,10,15,15,15,20,20,20,25,25,25,25,25,30,30,30,30,35,35,40,40,45,45,50,70,100]
BladeAuxCoreSlotDistribution = [0,1,1,1,2,2,2,2,2,3,3]
BladeWeaponCritDistribution = [0,0,0,0,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,15,15,15,15,15,15,20,20,20,25,30,35,40,45,50,70,100]
BladeWeaponGuardDistribution = [0,0,0,0,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,15,15,15,15,15,15,20,20,20,25,30,35,40,45,50,70,100]



InvalidEnemies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 183, 188, 192, 194, 200, 205, 207, 209, 211, 213, 215, 218, 224, 226, 228, 230, 233, 246, 255, 257, 259, 261, 263, 264, 265, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 306, 311, 312, 314, 316, 317, 321, 322, 327, 328, 330, 331, 333, 334, 335, 336, 337, 338, 340, 343, 344, 353, 354, 355, 357, 358, 360, 361, 362, 363, 364, 366, 368, 370, 371, 377, 378, 379, 380, 381, 382, 387, 388, 397, 398, 400, 402, 408, 410, 412, 416, 417, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 438, 439, 440, 441, 442, 443, 444, 449, 452, 453, 460, 465, 467, 469, 471, 472, 473, 478, 480, 482, 484, 486, 494, 499, 502, 505, 507, 509, 511, 514, 516, 518, 520, 522, 524, 526, 527, 528, 529, 530, 531, 537, 539, 541, 543, 545, 554, 556, 574, 575, 580, 582, 584, 585, 586, 587, 589, 590, 592, 594, 595, 596, 597, 599, 605, 606, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 698, 700, 702, 704, 724, 725, 726, 727, 728, 737, 799, 801, 803, 805, 807, 813, 818, 820, 846, 883, 885, 887, 889, 897, 900, 921, 923, 925, 927, 956, 1012, 1013, 1014, 1018, 1021, 1024, 1103, 1105, 1107, 1129, 1130, 1133, 1136, 1179, 1180, 1252, 1253, 1257, 1259, 1263, 1274, 1275, 1278, 1280, 1285, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1323, 1325, 1327, 1328, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1346, 1347, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1390, 1392, 1394, 1401, 1403, 1409, 1411, 1420, 1426, 1427, 1428, 1446, 1447, 1449, 1450, 1451, 1452, 1453, 1475, 1480, 1481, 1492, 1493, 1494, 1495, 1504, 1505, 1506, 1509, 1510, 1514, 1517, 1520, 1521, 1523, 1524, 1525, 1533, 1538, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1568, 1569, 1593, 1599, 1615, 1620, 1633, 1641, 1654, 1668, 1669, 1671, 1672, 1673, 1685, 1700, 1724, 1725, 1726, 1727, 1731, 1750, 1751, 1752, 1753, 1787, 1788, 1789, 1805, 1806, 1807, 1881, 1883, 1885, 1887]
ValidEnemies =  [x for x in Helper.InclRange(0,1888) if x not in (InvalidEnemies)]

# The Following are IDs corresponding to items I want to shuffle in for race mode, increasing in power level the further in the list they are:
HPUp = [2, 154, 298, 3, 155, 299, 4, 156, 300, 498, 499, 500]
StrUp = [5, 157, 301, 6, 158, 302, 7, 159, 303, 501, 502, 503]
EthUp = [8, 160, 304, 9, 161, 305, 10, 162, 306, 504, 505, 506]
DexUp = [11, 163, 307, 12, 164, 308, 13, 165, 309, 507, 508, 509]
AgiUp = [14, 166, 310, 15, 167, 311, 16, 168, 312, 510, 511, 512]
LucUp = [17, 169, 313, 18, 170, 314, 19, 171, 315, 513, 514, 515]
AutoHeal = [32, 184, 328, 33, 185, 329, 34, 186, 330, 516, 517, 518]
CritHeal = [35, 35, 187, 331, 36, 188, 332, 37, 332, 333, 189, 333]
CritDmg = [38, 190, 334, 39, 191, 335, 40, 192, 336, 519, 520, 521]
AtkTwice = [41, 193, 337, 42, 194, 338, 43, 195, 339, 522, 523, 524]
DmgHigherLv = [53, 205, 349, 54, 206, 350, 55, 207, 351, 534, 535, 536]
BrkLen = [59, 211, 355, 60, 212, 356, 61, 213, 357, 540, 541, 542]
TopLen = [62, 214, 358, 63, 215, 359, 64, 216, 360, 543, 544, 545]
LauLen = [65, 217, 361, 66, 218, 362, 67, 219, 363, 546, 547, 548]
AutoDmg = [68, 220, 364, 69, 221, 365, 70, 222, 366, 549, 550, 551]
AggroDwn = [76, 228, 372, 77, 229, 373, 78, 230, 374, 558, 559, 560]
AggroUp = [79, 231, 375, 80, 232, 376, 81, 233, 377, 561, 562, 563]
AggroStart = [82, 234, 378, 83, 235, 379, 84, 236, 380, 564, 565, 566]
HealArtEff = [91, 243, 387, 92, 244, 388, 93, 245, 389, 567, 568, 569]
CancelHeal = [95, 247, 391, 96, 248, 392, 97, 249, 393, 573, 574, 575]
SpecCDs = [98, 250, 394, 99, 251, 395, 100, 252, 396, 576, 577, 578]
CancelDmg = [101, 253, 397, 102, 254, 398, 103, 255, 399, 579, 580, 581]
PartyGge = [109, 111, 112, 112, 400, 402, 259, 110, 402, 403, 401, 403]
HPPotEff = [141, 285, 429, 142, 286, 430, 143, 287, 431, 431, 431, 431]
BrkResRed = [144, 144, 288, 288, 432, 432, 582, 582, 583, 583, 584, 584]
RiskyDmg = [486, 486, 487, 487, 488, 488, 489, 489, 490, 490, 491, 491]
NoRecoil = [118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118]
BladeCDs = [147, 147, 147, 147, 291, 291, 291, 291, 435, 435, 435, 435]

AllRaceModeItemTypeIDs = [HPUp, StrUp, EthUp, DexUp, AgiUp, LucUp, AutoHeal, CritHeal, CritDmg, AtkTwice, DmgHigherLv, BrkLen, TopLen, LauLen, AutoDmg, AggroDwn, AggroUp, AggroStart, HealArtEff, CancelHeal, SpecCDs, CancelDmg, PartyGge, HPPotEff, BrkResRed, RiskyDmg, NoRecoil, BladeCDs]

# The following are Aux Cores to be equipped in Race Mode, increasing in power level, the further along the list they are:
# This is genuinely messed up btw, there"s no fast way to get these
AuxCrit = [17001, 17001, 17002, 17002, 17003, 17003, 17004, 17004, 17005, 17005, 17352, 17352]
PhysDef = [x + 5 for x in AuxCrit[:10]] + [x + 1 for x in AuxCrit[-2:]]
EthDef = [x + 5 for x in PhysDef[:10]] + [x + 1 for x in PhysDef[-2:]]
BlockRate = [x + 5 for x in EthDef[:10]] + [x + 1 for x in EthDef[-2:]]
BeastHnt = [x + 5 for x in BlockRate[:10]] + [x + 1 for x in BlockRate[-2:]]
InsHnt = [x + 5 for x in BeastHnt[:10]] + [x + 1 for x in BeastHnt[-2:]]
AirHnt = [x + 5 for x in InsHnt[:10]] + [x + 1 for x in InsHnt[-2:]]
AquaHnt = [x + 5 for x in AirHnt[:10]] + [x + 1 for x in AirHnt[-2:]]
HumHnt = [x + 5 for x in AquaHnt[:10]] + [x + 1 for x in AquaHnt[-2:]]
MacHnt = [x + 5 for x in HumHnt[:10]] + [x + 1 for x in HumHnt[-2:]]
TitHnt = [x + 5 for x in MacHnt[:10]] + [x + 1 for x in MacHnt[-2:]]
BldCmbBst = [17056, 17056, 17057, 17057, 17058, 17058, 17059, 17059, 17060, 17060, 17061, 17061]
FusCmbBst = [17062, 17062, 17063, 17063, 17064, 17064, 17065, 17065, 17066, 17066, 17363, 17363]
AggAtkUp = [17077, 17077, 17078, 17078, 17079, 17079, 17080, 17080, 17081, 17081, 17365, 17365]
IndAtkUp = [x + 5 for x in AggAtkUp[:10]] + [x + 1 for x in AggAtkUp[-2:]]
OutAtkUp = [x + 5 for x in IndAtkUp[:10]] + [x + 1 for x in IndAtkUp[-2:]]
FirDef = [x + 5 for x in OutAtkUp[:10]] + [x + 1 for x in OutAtkUp[-2:]]
WatDef = [x + 5 for x in FirDef[:10]] + [x + 1 for x in FirDef[-2:]]
EarDef = [x + 5 for x in WatDef[:10]] + [x + 2 for x in WatDef[-2:]]
WindDef = [x + 5 for x in EarDef[:10]] + [x - 1 for x in EarDef[-2:]] 
ElecDef = [x + 5 for x in WindDef[:10]] + [x + 2 for x in WindDef[-2:]]
IceDef = [x + 5 for x in ElecDef[:10]] + [x + 1 for x in ElecDef[-2:]] 
DarkDef = [x + 5 for x in IceDef[:10]] + [x + 2 for x in IceDef[-2:]] 
LigDef = [x + 5 for x in DarkDef[:10]] + [x - 1 for x in DarkDef[-2:]]
EvaFoc = [x + 22 for x in LigDef[:10]] + [x + 2 for x in LigDef[-2:]]
SwiEva = [x + 5 for x in EvaFoc[:10]] + [x + 1 for x in EvaFoc[-2:]]
EmgGuard = [x + 5 for x in SwiEva[:10]] + [x + 1 for x in SwiEva[-2:]]
Endure = [x + 5 for x in EmgGuard[:10]] + [x + 1 for x in EmgGuard[-2:]]
HPAtkUp = [x + 5 for x in Endure[:10]] + [x + 1 for x in Endure[-2:]]
SpkDef = [17174, 17174, 17175, 17175, 17175, 17176, 17176, 17177, 17177, 17177, 17178, 17178]
BrkRes = [x + 10 for x in HPAtkUp[:10]] + [x + 1 for x in HPAtkUp[-2:]]
TopRes = [x + 5 for x in BrkRes[:10]] + [x + 1 for x in BrkRes[-2:]]
LauRes = [x + 5 for x in TopRes[:10]] + [x + 1 for x in TopRes[-2:]]
SmaRes = [x + 5 for x in LauRes[:10]] + [x + 1 for x in LauRes[-2:]]
BlowRes = [x + 5 for x in SmaRes[:10]] + [x + 1 for x in SmaRes[-2:]]
KBRes = [x + 5 for x in BlowRes[:10]] + [x + 1 for x in BlowRes[-2:]]
AnnulRes = [x + 35 for x in SpkDef]
BldShqRes = [x + 5 for x in AnnulRes]
AASneak = [x + 15 for x in KBRes[:10]] + [x + 1 for x in KBRes[-2:]]
AggBoost = [x + 5 for x in AASneak[:10]] + [x + 1 for x in AASneak[-2:]]
ArtSneak = [x + 5 for x in AggBoost[:10]] + [x + 1 for x in AggBoost[-2:]]
ArtAggUp = [x + 5 for x in ArtSneak[:10]] + [x + 1 for x in ArtSneak[-2:]]
ArtHeal = [x + 5 for x in ArtAggUp[:10]] + [x + 1 for x in ArtAggUp[-2:]]
MoveHeal = [x + 5 for x in ArtHeal[:10]] + [x + 1 for x in ArtHeal[-2:]]
DamHeal = [x + 5 for x in MoveHeal[:10]] + [x + 1 for x in MoveHeal[-2:]]
AMSee = [x + 5 for x in DamHeal[:10]] + [x + 1 for x in DamHeal[-2:]]
PMSee = [x + 5 for x in AMSee[:10]] + [x + 1 for x in AMSee[-2:]]
ReflDmg = [x + 5 for x in PMSee[:10]] + [x + 1 for x in PMSee[-2:]]
RngUp = [x + 55 for x in BldShqRes]
OpeArt = [x + 10 for x in ReflDmg[:10]] + [x + 1 for x in ReflDmg[-2:]]
Telepathy = [x + 10 for x in RngUp]
HelpHand = [x + 5 for x in Telepathy]
AffMaxShld = [x + 15 for x in OpeArt[:10]] + [x + 1 for x in OpeArt[-2:]]
AffMaxAtk = [x + 5 for x in AffMaxShld[:10]] + [x + 1 for x in AffMaxShld[-2:]]
AffMaxEvd = [x + 5 for x in AffMaxAtk[:10]] + [x + 1 for x in AffMaxAtk[-2:]]
HntChem = [x + 20 for x in HelpHand]
StS = [x + 5 for x in HntChem]
FstBldSwp = [17314, 17314, 17315, 17315, 17316, 17316, 17317, 17317, 17318, 17318, 17319, 17319]
Lv1SpecUp = [x + 21 for x in AffMaxEvd[:10]] + [x + 1 for x in AffMaxEvd[-2:]]
Lv2SpecUp = [x + 5 for x in Lv1SpecUp[:10]] + [x + 1 for x in Lv1SpecUp[-2:]]
Lv3SpecUp = [x + 5 for x in Lv2SpecUp[:10]] + [x + 1 for x in Lv2SpecUp[-2:]]
Lv4SpecUp = [x + 5 for x in Lv3SpecUp[:10]] + [x + 1 for x in Lv3SpecUp[-2:]]
AffMaxAcc = [x + 5 for x in Lv4SpecUp[:10]] + [x + 1 for x in Lv4SpecUp[-2:]]
Jamming = [x + 5 for x in AffMaxAcc[:10]] + [x + 1 for x in AffMaxAcc[-2:]]

RaceModeAuxCoreIDs = [AuxCrit, PhysDef, EthDef, BlockRate, BeastHnt, InsHnt, AirHnt, AquaHnt, HumHnt, MacHnt, TitHnt, BldCmbBst, FusCmbBst, AggAtkUp, IndAtkUp, OutAtkUp, FirDef, WatDef, EarDef, WindDef, ElecDef, IceDef, DarkDef, LigDef, EvaFoc, SwiEva, EmgGuard, Endure, HPAtkUp, SpkDef, BrkRes, TopRes, LauRes, SmaRes, BlowRes, KBRes, AnnulRes, BldShqRes, AASneak, AggBoost, ArtSneak, ArtAggUp, ArtHeal, MoveHeal, DamHeal, AMSee, PMSee, ReflDmg, RngUp, OpeArt, Telepathy, HelpHand, AffMaxShld, AffMaxAtk, AffMaxEvd, HntChem, StS, FstBldSwp, Lv1SpecUp, Lv2SpecUp, Lv3SpecUp, Lv4SpecUp, AffMaxAcc, Jamming]

A1RaceModeCoreChipIDs = [10002, 10009, 10010, 10003, 10011, 10017, 10018, 10019, 10005, 10006, 10007]
A2RaceModeCoreChipIDs = [10025, 10026, 10027, 10013, 10014, 10015, 10033, 10034, 10035, 10029, 10030, 10031, 10041, 10042, 10043]
A3RaceModeCoreChipIDs = [10021, 10022, 10023, 10037, 10038, 10039, 10045, 10046, 10047, 10049, 10050, 10051, 10055, 10056, 10057]
A4RaceModeCoreChipIDs = [10004, 10008, 10012, 10016, 10020, 10024, 10028, 10032, 10036, 10040, 10044, 10048, 10052, 10053, 10054, 10058, 10059, 10060]  

SeedHashAdj = ["Spellbinder", "Vagrant", "Howitzer", "Muscley", "Enlightened", "Vampire Bride", "Implacable", "Man-Eating", "Reeking", "Spring-Shower", "Epicurean", "Immovable", "Sniping", "Relentless", "Jadeite", "Gladiator", "Remorseful", "Parasite", "Praetorian", "Heroic", "Malicious", "Rapturous", "Acute", "Mk. VI", "Walker", "Impassable", "Hard-Bitten", "Insectivore", "Incandescent", "Excavator", "Nitpicking", "Tyrannotitan", "Autumn-Shower", "Azure", "Soul-Eater", "Sad", "Confiscator", "Machine-Gun", "Glamorous", "Artifice", "Martial", "Deep-Green", "Ravenwing", "Slasher", "Judicial", "Antecedent", "Haywire", "Leonine", "Grievous", "Pernicious", "Moonlighting", "Decapitator", "Territorial", "Climactic", "Supercharged", "Cunning", "Beast-Hunter", "Myrmidon", "Tattooed", "Runaway Train", "Atrocious", "Evileye", "Dedicated", "Skyfist", "Vile", "Unflinching", "Cloud Sea King", "Perplexed", "Venal", "Demon-Shell", "Crimson", "Demon King", "Peerless", "Mk. VII", "Blue-Eyed", "Holy Lancer", "Chickenheart", "Soothsayer", "Armored", "Anguished"]
SeedHashNoun = ["William", "Orion", "Edgar", "Oscar", "Howard", "Hermes", "Sadie", "Darius", "Stanley", "Phoebus", "Melvyn", "Alfonso", "Gonzalez", "Ligia", "Marion", "Arek", "Margot", "Polly", "Dimitri", "Vaclav", "Kamron", "Douglas", "Saxton", "Hugo", "Leon", "Saggie", "Alfred", "Xiaxia", "Elwyn", "Derrick", "Kurodil", "Medea", "Brennan", "Solomon", "Elliott", "Stoyan", "Kollin", "Clive", "Trap", "Beaufort", "Eugene", "Dagmara", "Malcom", "Gerald", "Honnold", "Bool", "Mambor", "Benf", "Bernard", "Jacob", "Buffon", "Arduran", "Marcus", "Xavier", "Gilbert", "Reginald", "Edwin", "Dylan", "Glenn", "Ophion", "Beru", "Efrain", "Ken", "Damian", "Baldr", "Rotbart", "Montgomery", "Kustal", "Jimmy", "Familion", "Aplacus", "Morris", "Julio", "Melvin", "Skull", "Gerolf", "Marvin", "Radclyffe", "Brent", "Scandia", "Billy", "Argus", "Remington", "Conroy", "Korbin"]

Arts = [4, 5, 6, 7, 11, 12, 13, 14, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 46, 47, 48, 49, 53, 54, 55, 56, 60, 61, 62, 63, 70, 71, 72, 73, 74, 75, 76, 77, 84, 85, 86, 87, 88, 89, 90, 91, 98, 99, 100, 101, 102, 103, 104, 105, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 215, 216, 217, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 312, 314, 320, 321, 322, 326, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 585, 586, 587, 589, 591, 595, 596, 597, 600, 601, 605, 606, 607, 609, 611, 615, 616, 617, 621, 625, 626, 627, 629, 631, 635, 636, 637, 639, 641, 645, 646, 647, 649, 651, 655, 656, 657, 659, 661, 665, 666, 667, 669, 671, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742]
WeaponTypeRoles = [2,3,3,1,1,1,1,2,2,2,2,2,1,1,3,3,2,2,1,3,2,1,2,2,1,1,2,2,2,1,3,2,2,3,2,1]
EvasionEnhancementIDs = [2825, 2866, 2872]
SpecialEffectArtIDs = [49, 202, 217, 538, 550, 646, 315, 329, 675]
OriginalAOECaptionIDs = [3, 8, 13, 15, 16, 17, 19, 20, 21, 25, 27, 33, 36, 37, 39, 41, 43, 52, 56, 61, 63, 65, 68, 69, 71, 72, 77, 81, 84, 85, 88, 93, 97, 101, 104, 107, 108, 113, 117, 119, 120, 123, 136, 140, 141, 144, 145, 147, 148, 149, 151, 153, 156, 157, 159, 162, 164, 165, 167, 169, 172, 173, 176, 177, 183, 185, 191, 195, 199, 202, 203, 206, 210, 215, 217, 219, 222, 226, 230, 231, 234, 235, 238, 239, 243, 247, 250, 254, 257, 258, 262, 266, 269, 270, 271, 273, 275, 278, 279, 282, 283, 286, 287, 290, 291, 294, 295, 297, 299, 301, 302, 305, 309, 315, 318, 322, 326, 327, 329, 336, 343, 350, 355, 356, 357, 358, 372, 377, 384, 392, 401, 424, 427, 431, 436, 438, 444, 449, 451, 452]
OriginalHealPartyCaptionIDs = [7, 57, 79, 105, 131, 223, 227, 251, 255, 319, 323, 344, 428, 432]
ArtRandoCompleteness = 0

FlyingEnArrangeIDs = [195, 247, 251, 313, 315, 319, 350, 359, 384, 413, 414, 415, 418, 447, 448, 450, 476, 498, 535, 547, 548, 551, 558, 564, 566, 567, 568, 569, 571, 577, 578, 613, 632, 660, 669, 670, 671, 672, 673, 674, 694, 695, 711, 712, 723, 730, 731, 765, 766, 767, 768, 769, 770, 771, 772, 815, 832, 844, 845, 847, 867, 875, 892, 893, 902, 905, 906, 907, 915, 929, 943, 944, 945, 946, 947, 958, 961, 962, 963, 978, 985, 986, 987, 988, 989, 990, 994, 1017, 1030, 1032, 1033, 1034, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1070, 1073, 1110, 1114, 1115, 1118, 1121, 1122, 1123, 1124, 1131, 1134, 1137, 1141, 1142, 1143, 1144, 1158, 1159, 1160, 1165, 1172, 1174, 1184, 1186, 1189, 1191, 1192, 1193, 1194, 1195, 1205, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1233, 1254, 1260, 1264, 1270, 1271, 1272, 1273, 1343, 1395, 1399, 1416, 1417, 1460, 1472, 1479, 1486, 1519, 1528, 1529, 1530, 1531, 1532, 1550, 1551, 1560, 1567, 1589, 1603, 1604, 1605, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1618, 1639, 1640, 1643, 1650, 1655, 1660, 1666, 1667, 1678, 1710, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1741, 1744, 1745, 1759, 1786, 1797, 1802, 1813, 1817, 1818, 1821, 1829, 1886]
OriginalFlyingHeights = [0, -3000, 100, 80, 80, 10, 250, 250, 150, 250, 250, 10, 250, 0, 100, 10, 150, 50, 0, 0, 0, 0, 120, 10, 0, 0, 0, 0, 0, 150, 150, 10, 50, 0, 150, 10, 10, 80, 80, 80, 80, 80, 150, 80, 10, 50, 0, 150, 80, 130, 80, 80, 0, 250, 0, 250, 0, 150, 80, 250, 0, 0, 150, 0, 50, 250, 10, 250, 80, 10, 80, 0, 250, 50, 10, 10, 50, 250, 10, 0, 150, 10, 10, 80, 0, 250, 10, 0, 0, 250, 250, 10, 0, 150, 80, 0, 0, 250, 0, 0, 10, 10, 10, 0, 0, 0, 150, 80, 80, 250, 150, 0, -3000, 10, 250, 10, 10, 0, 150, 250, 120, 10, 100, 120, 100, 120, 250, 10, 250, 10, 10, 0, 150, 10, 130, 80, 0, 250, 250, 250, 50, 0, 0, 10, 10, 10, 0, 250, 250, 10, 10, 10, 10, 50, 0, 250, 80, 0, 80, 0, 0, 150, 10, 10, 80, 80, 10, 10, 150, 0, 0, 0, 150, 150, 80, 80, 80, 0, 250, 50, 0, 10, 10, 10, 150, 10, 0, 10, 10, 0, 100, 0, 80, 80, 0, 0, 10, 0, 250, 10, 10, 50, 10, 10, 0, 10, 150, 120, 0, 80, 80, 0, 0, -100]
OriginalWalkSpeeds = [8, 35, 8, 8, 8, 14, 24, 24, 25, 24, 24, 14, 24, 18, 8, 20, 25, 6, 18, 22, 22, 18, 8, 8, 18, 18, 18, 18, 22, 25, 25, 20, 6, 22, 20, 14, 14, 8, 8, 8, 8, 8, 25, 8, 20, 6, 18, 25, 8, 8, 8, 8, 18, 24, 8, 24, 22, 25, 8, 24, 18, 18, 25, 18, 6, 24, 20, 24, 8, 8, 8, 18, 24, 6, 20, 20, 6, 24, 20, 22, 25, 14, 14, 8, 18, 24, 20, 18, 18, 24, 24, 25, 24, 25, 8, 18, 18, 24, 8, 8, 20, 25, 25, 14, 8, 22, 25, 8, 8, 24, 25, 22, 35, 20, 24, 20, 25, 22, 25, 24, 8, 12, 35, 8, 35, 8, 24, 20, 24, 20, 25, 22, 25, 14, 8, 8, 18, 24, 24, 24, 6, 8, 18, 20, 14, 20, 22, 24, 24, 20, 25, 8, 25, 6, 22, 24, 8, 18, 8, 22, 22, 25, 14, 14, 8, 8, 14, 14, 25, 22, 22, 14, 25, 25, 8, 8, 8, 14, 24, 6, 8, 20, 14, 14, 25, 14, 14, 20, 14, 10, 8, 18, 8, 8, 14, 8, 14, 18, 24, 20, 25, 6, 20, 25, 22, 25, 25, 8, 18, 8, 8, 14, 18, 6]
OriginalRunSpeeds = [28, 50, 28, 20, 28, 35, 35, 35, 60, 35, 35, 35, 35, 35, 28, 35, 60, 12, 35, 40, 40, 35, 20, 28, 30, 30, 30, 30, 40, 60, 60, 35, 12, 40, 45, 35, 35, 28, 20, 20, 28, 20, 60, 28, 35, 12, 35, 60, 28, 28, 20, 20, 30, 35, 28, 35, 40, 60, 28, 35, 35, 35, 60, 35, 12, 35, 35, 35, 28, 28, 28, 30, 35, 12, 35, 35, 12, 35, 35, 40, 60, 35, 35, 20, 30, 35, 35, 30, 30, 35, 35, 45, 34, 60, 28, 30, 30, 35, 28, 28, 35, 45, 45, 36, 28, 40, 60, 28, 20, 35, 60, 40, 50, 35, 35, 35, 45, 40, 60, 35, 20, 30, 55, 20, 55, 20, 35, 35, 35, 35, 45, 40, 60, 35, 28, 20, 30, 35, 35, 35, 12, 28, 35, 35, 35, 35, 40, 35, 35, 35, 45, 28, 45, 12, 40, 35, 20, 30, 20, 40, 40, 60, 35, 35, 28, 20, 35, 35, 60, 40, 40, 36, 60, 60, 28, 20, 20, 26, 35, 12, 28, 35, 35, 35, 60, 35, 36, 35, 35, 20, 28, 35, 20, 20, 36, 28, 35, 30, 35, 35, 45, 12, 35, 45, 40, 45, 60, 20, 35, 20, 20, 36, 35, 12]
OriginalBtlSpeeds = [24, 50, 28, 20, 24, 24, 30, 26, 40, 30, 30, 24, 30, 28, 28, 30, 40, 18, 28, 28, 28, 28, 20, 28, 24, 24, 24, 24, 28, 40, 40, 30, 18, 28, 40, 24, 24, 24, 20, 18, 24, 18, 40, 24, 30, 18, 28, 40, 24, 24, 18, 18, 24, 30, 24, 30, 28, 40, 24, 30, 28, 28, 40, 28, 18, 30, 30, 30, 24, 28, 24, 24, 30, 18, 30, 30, 18, 30, 30, 28, 40, 24, 24, 18, 24, 30, 30, 24, 24, 30, 30, 28, 36, 40, 24, 24, 24, 30, 24, 24, 30, 28, 28, 36, 24, 28, 40, 24, 20, 30, 40, 28, 50, 30, 30, 30, 28, 28, 40, 30, 20, 28, 28, 15, 28, 10, 30, 30, 30, 30, 28, 28, 40, 24, 24, 18, 24, 30, 30, 30, 18, 24, 28, 30, 24, 30, 28, 30, 30, 30, 28, 28, 28, 18, 28, 30, 18, 24, 18, 28, 28, 40, 24, 24, 24, 20, 24, 24, 40, 28, 28, 36, 40, 40, 24, 18, 18, 24, 30, 18, 24, 30, 24, 24, 40, 24, 36, 30, 24, 24, 28, 28, 18, 20, 36, 24, 24, 24, 30, 30, 28, 18, 30, 28, 28, 28, 40, 20, 28, 20, 18, 36, 28, 18]

SwimmingEnArrangeIDs = [677, 678, 690, 715, 775, 776, 777, 1228, 1229, 1230, 1255, 1536, 1537, 1616, 1617]

# Used as reference
# ShopID: [ShopType: EventID, Name]
FullShopEventNameDict = {'Normal': {36: [40321, 30], 37: [40322, 31], 38: [40323, 32], 39: [40324, 33], 40: [40325, 34], 41: [40326, 35], 42: [40327, 36], 43: [40328, 37], 44: [40329, 38], 45: [40330, 39], 46: [40332, 40], 47: [40331, 41], 48: [41000, 42], 49: [40333, 43], 64: [40438, 50], 65: [40338, 66], 66: [40441, 51], 67: [40339, 72], 68: [40442, 52], 69: [40340, 68], 70: [40443, 53], 71: [40444, 54], 72: [40445, 55], 73: [40446, 56], 75: [40341, 69], 76: [40342, 70], 77: [40447, 58], 78: [40448, 59], 80: [40449, 60], 81: [40450, 61], 82: [40343, 71], 83: [40451, 62], 84: [41001, 45], 85: [41002, 46], 92: [40663, 91], 93: [40664, 92], 94: [40665, 93], 95: [40666, 94], 96: [40667, 95], 97: [40668, 96], 98: [40669, 97], 99: [40670, 98], 100: [40671, 99], 102: [40672, 100], 103: [40673, 101], 104: [41003, 102], 105: [40674, 103], 113: [40675, 112], 115: [40758, 114], 116: [40760, 115], 117: [40676, 116], 118: [40723, 117], 119: [40757, 118], 120: [40684, 119], 121: [40756, 120], 122: [40685, 122], 123: [41004, 121], 145: [41040, 143], 146: [41041, 144], 147: [40810, 145], 148: [40806, 146], 149: [40808, 147], 150: [40805, 148], 151: [40811, 149], 152: [40807, 150], 153: [41005, 151], 174: [20262, 167], 201: [41556, 117], 203: [21256, 42], 249: [42020, 228], 250: [42019, 229], 251: [42022, 230], 252: [42021, 231], 253: [41628, 232], 254: [41678, 233], 255: [42023, 234]},
                     'Exchange': {16: [40058, 245], 17: [40054, 239], 18: [40045, 238], 21: [40048, 241], 23: [40050, 244], 24: [40051, 240], 26: [40052, 242], 27: [40053, 246], 33: [40320, 23], 54: [40439, 49], 55: [40337, 65], 60: [20805, 82], 61: [20806, 83], 62: [20807, 84], 74: [41042, 57], 89: [40662, 88], 90: [20441, 89], 91: [20444, 90], 109: [40724, 108], 110: [40761, 109], 114: [40731, 243], 144: [40809, 142], 154: [41039, 152], 156: [40982, 155], 161: [20121, 165], 162: [20119, 166], 164: [20124, 73], 165: [20125, 74], 166: [20126, 75], 176: [20265, 25], 177: [20268, 26], 186: [41564, 183], 189: [40980, 154], 202: [41044, 191], 213: [21383, 193], 214: [21393, 194], 215: [21394, 195], 217: [21470, 197], 219: [21448, 200], 226: [21623, 205], 227: [21660, 206], 228: [21694, 207], 230: [21727, 209], 231: [21729, 210], 234: [21740, 213], 235: [21741, 214], 237: [21760, 216], 257: [42027, 236]},
                    'Inn': {12: [40057, 2], 31: [40318, 21], 50: [40436, 47], 51: [40335, 63], 87: [40660, 86], 106: [40762, 105], 107: [40952, 106], 143: [41053, 141], 225: [41578, 204]},
                    'AuxCore': {32: [40319, 22], 52: [40440, 48], 53: [40336, 64], 88: [40661, 87], 108: [40759, 107]}
}


# Torna IDS
ValidRecipeInfoIDs = Helper.InclRange(26139, 26163) + [26166] + Helper.InclRange(26171, 26191)
TornaCollectibleIDs = [30340, 30341, 30342, 30343, 30344, 30345, 30346, 30347, 30348, 30349, 30350, 30351, 30352, 30353, 30354, 30355, 30356, 30357, 30358, 30359, 30360, 30361, 30362, 30363, 30364, 30365, 30366, 30367, 30368, 30369, 30370, 30371, 30372, 30373, 30374, 30375, 30376, 30377, 30378, 30380, 30384, 30386, 30387, 30388, 30389, 30390, 30391, 30392, 30393, 30394, 30395, 30396, 30397, 30398, 30399, 30400, 30401, 30402, 30403, 30404, 30405, 30406, 30407, 30408, 30409, 30410, 30411, 30412, 30413, 30414, 30415, 30416, 30417, 30418, 30419, 30420, 30421, 30422, 30423, 30424, 30425, 30426, 30427, 30428, 30429, 30430, 30432, 30433, 30434, 30435, 30436, 30437, 30438, 30439, 30442, 30443, 30444, 25457, 25458, 25463, 25473, 25536]
TornaAuxCores = Helper.InclRange(17001, 17406) + [17425]
TornaWeaponChips = WeaponChips
CombinedTornaAccessories = list(set(TornaAccessories + Accessories))
TornaPreciousIDs = Helper.InclRange(25457, 25466) + Helper.InclRange(25469, 25494) + Helper.InclRange(25501, 25528)
TornaUMIDs = [1563, 1564, 1566, 1567, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1670, 1559, 1560, 1561, 1562]
TornaRegularEnemyIDs = [1536, 1537, 1539, 1540, 1542, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1570, 1571, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1585, 1587, 1588, 1589, 1590, 1591, 1592, 1594, 1595, 1596, 1598, 1600, 1601, 1602, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1616, 1617, 1618, 1619, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1634, 1635, 1636, 1637, 1639, 1640, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1655, 1656, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1507, 1512, 1515, 1516, 1518, 1519, 1522, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1534, 1535]
TornaSlatePieceIDs = [25479, 25480, 25481, 25482, 25483, 25484, 25485, 25486, 25487, 25488, 25489, 25490, 25491, 25492, 25493, 25494]
# Custom Randomizer Item IDs for Torna

# Field Skill Unlocks
MineralogyKey = Helper.InclRange(25544,25546)
SwordplayKey = Helper.InclRange(25547,25549)
FortitudeKey = Helper.InclRange(25550,25551)
ForestryKey = Helper.InclRange(25552,25554)
ManipEtherKey = Helper.InclRange(25555,25557)
KeenEyeKey = Helper.InclRange(25558,25560)
FocusKey = Helper.InclRange(25561,25563)
LightKey = Helper.InclRange(25564,25566)
GirlsTalkKey = [25567]
EntomologyKey = Helper.InclRange(25568,25570)
MiningKey = Helper.InclRange(25571,25573)
BotanyKey = Helper.InclRange(25574,25576)
LockpickKey = Helper.InclRange(25577,25579)
IcthyologyKey = Helper.InclRange(25580,25582)
ComWaterKey = Helper.InclRange(25583,25585)
SuperstrKey = Helper.InclRange(25586,25588)

# Campsite Unlocks
HHC_Key = [25589]
LC_Key = [25590]
CLC_Key = [25591]
HWC_Key = [25592]
PVC_Key = [25593]
FVC_Key = [25594]
AGC_Key = [25595]
OTC_Key = [25596]
DDC_Key = [25597]
HGC_Key = [25598]

# Affinity Level Unlocks
JinAff = Helper.InclRange(25599,25602)
HazeAff = Helper.InclRange(25603,25606)
MythraAff = Helper.InclRange(25607,25610)
MinothAff = Helper.InclRange(25611,25614)
BrighidAff = Helper.InclRange(25615,25618)
AegaeonAff = Helper.InclRange(25619,25622)

# Character Unlocks
HazeKey = [25623]
AddamKey = [25624]
MythraKey = [25625]
MinothKey = [25626]
HugoKey = [25627]
BrighidKey = [25628]
AegaeonKey = [25629]

# Level Up Unlocks
LevelUpTokens = Helper.InclRange(25630,25725) # 96 tokens, we assume we get 2 levels from intro fight (stats required to beat fight?), and start at lv 1.