from scripts import Helper

def ClassTree():    
    validClassIDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
    invalidClassIDs = Helper.InclRange(17, 38)
    # change default weapons
    Helper.FileShuffle("XCXDE/JsonOutputs/common/CHR_ClassInfo.json", ["promotion_A", "promotion_B", "promotion_C", "$id", "StartLevel", "Stats", "Rank"], invalidClassIDs, lambda e: e["$id"] in validClassIDs)