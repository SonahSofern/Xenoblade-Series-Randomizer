from scripts import JSONParser, Helper

def ClassTree():    
    plusClassIDs = [1, 17, 18, 20, 23, 24, 29, 30, 31,32, 33]
    Helper.FileShuffle("XCXDE/JsonOutputs/common/CHR_ClassInfo.json", ["promotion_A", "promotion_B", "promotion_C", "$id", ], plusClassIDs, lambda e: e["$id"] not in plusClassIDs)