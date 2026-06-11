import json
from scripts import JSONParser
from  XCDE.XCDE_Scripts import Options, IDs

def Quickstep(): # Originally wanted to give it to shulks default wep but you couldnt remnove it for some reason
    with open("./XCDE/JsonOutputs/bdat_common/BTL_skilllist.json", 'r+', encoding='utf-8') as gemFile:
        with open("./XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itemFile:
            gemData = json.load(gemFile)
            itemData = json.load(itemFile)
            
            # Find the quickstep gem
            for gem in gemData["rows"]:
                if gem["rvs_status"] == 3:
                    quickstepSkill = gem
                    break
            
            # # If it got randomized and doenst exist in the list add it back??
                
            # Remove the cap
            quickstepSkill["max"] = 10000
            
            # Give it to the gem man
            for item in itemData["rows"]:
                if item["$id"] in [3399,3400]:
                    item["itemType"]= 3
                    item["itemID"]= quickstepSkill["$id"]
                    item["icon"]= 419
                    item["icon_base"]= 328
                    item["rankType"]= 6
                    item["percent"]=  min(Options.MovespeedOption.GetSpinbox(),255)
                    item["item_keep"]=  0
                    item["comment"] = 0   
            

            JSONParser.CloseFile(itemData, itemFile)
            JSONParser.CloseFile(gemData, gemFile)


def QuestAffinity():
    '''Original Idea: Removes the cnd_famous which corresponds the number of stars a quest needs to be allowed to show up
    Didnt work so now: All quests immediately max out your affinity with that area
    '''
    for fileName in IDs.areaListQuestNumbers:
        qstFile = JSONParser.File(f"XCDE/JsonOutputs/bdat_common/JNL_quest{fileName}.json")
        for qst in qstFile.rows:
            # qst["cnd_famous"] = 0 # even set to 0 you still had to do a quest to gain affinity
            for c in ["A", "B"]:
                qst[f"up_famous_{c}"] = 10000 
            # qst["flg_famous"] = 0 # flg_famous controls what area it checks for the cnd_famous
        
        qstFile.Close()