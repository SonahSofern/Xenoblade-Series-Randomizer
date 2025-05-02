from scripts.GUISettings import fontNameVar as TestVar
from scripts import Helper
areaFileListNumbers = ["0101", "0201", "0301", "0401", "0402", "0501", "0601", "0701", "0801", "0901", "1001", "1101", "1201","1202", "1301", "1401", "1501", "1601", "1701", "1901", "2001", "2101", "2201", "2301", "2401", "2501", "2601", "5001", "5101", "5201", "5301", "5401", "5501", "5601", "5701", "5801", "5901", "6001"]
CollectableIDs = Helper.InclRange(1852,2151)
MaterialIDs = Helper.InclRange(2152,2587)
ArmorIDs = Helper.InclRange(3766, 3945, [3936, 3941])
WeaponIDs = Helper.InclRange(1,625) # Come back to filter
GemIDs = Helper.InclRange(3104, 3747) + Helper.InclRange(4264, 4550) + Helper.InclRange(4579,4585)
CrystalIDs = Helper.InclRange(1252,1851)
ArtBookIDs = Helper.InclRange(2864, 3103, Helper.InclRange(2912,2919) + Helper.InclRange(3008,3015))