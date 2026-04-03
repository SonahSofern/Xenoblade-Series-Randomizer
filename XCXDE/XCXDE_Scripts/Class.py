from scripts import Helper, JSONParser

class ClassInfo():
    def __init__(self, classData, growData, index):
        self.classData = JSONParser.copy.deepcopy(classData)
        self.growData = JSONParser.copy.deepcopy(growData)
        self.index = index

def ClassTree():    
    validClassIDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
    drifterID = 1
    # invalidClassIDs = Helper.InclRange(17, 38)
    
    dataSets = Helper.RandomGroup()
    
    # Build data sets
    classFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_ClassInfo.json")
    artInfoFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_PcArtsInfo.json")
    skillInfoFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_SkillClass.json")
    
    # Get data
    for i in range(1,17):
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{i:02}Growth.json")
        for cls in classFile.rows:
            if cls["$id"] == i:
                dataSets.AddNewData(ClassInfo(cls, growFile.rows, i))
                break
        growFile.Close()
    
    # Distribute
    for cls in classFile.rows:
        if cls["$id"] not in validClassIDs:
            continue
        chosenCls:ClassInfo = dataSets.SelectRandomMember()
        if cls["$id"] == drifterID: # If we are replacing drifter class we need to rebalance
            if chosenCls.classData["$id"] != drifterID: # Drifter doesnt need to be rebalanced obviously
                FixStartingGear(chosenCls.classData["$id"], classFile.rows)
        Helper.CopyKeys(cls, chosenCls.classData, ["promotion_A", "promotion_B", "promotion_C", "$id", "StartLevel", "Stats"])
        
        # Fix grow files
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{cls["$id"]:02}Growth.json")
        growFile.rows = chosenCls.growData
        growFile.Close()
        
        # Fix arts file
        for art in artInfoFile.rows:
            if art["OpenClass"] == cls["$id"]:
                art["OpenClass"] = chosenCls.index
                
        # Fix skill file
        for skl in skillInfoFile.rows:
            if skl["OpenClass"] == cls["$id"]:
                skl["OpenClass"] = chosenCls.index
                
    artInfoFile.Close()
    classFile.Close()
    skillInfoFile.Close()

def FixStartingGear(classID, classData):
    chrData = JSONParser.File("XCXDE/JsonOutputs/common/DEF_PcList.json")
    
    # Find player char id(23)
    for chr in chrData.rows:
        if chr["$id"] == 23:
            break
    
    # Set the default class
    chr["ClassType"] = classID
    
    # Replace its default weapons for new class
    for cls in classData:
        if cls["$id"] != classID:
            continue
        chr["DefWpnNear"] = cls["NearWeapon"]
        chr["DefWpnFar"] = cls["FarWeapon"]
        break
    
    # Remove the starting arts you get them by levelling
    chr["ArtsNo1"] = 0
    chr["ArtsLv1"] = 0
    chr["ArtsNo8"] = 0
    chr["ArtsLv8"] = 0

    chrData.Close()