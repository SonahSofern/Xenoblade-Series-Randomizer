import json
from scripts import JSONParser, Helper

def TutorialSkip():
    '''Makes all tutorials the kind that just appear in the menu and not interrupt gameplay'''
    tipsFile = JSONParser.File("XCXDE/JsonOutputs/common/MNU_TipsList.json")
    for tip in tipsFile.rows:
        tip["operation"] = 2
        tip["type"] = 1
        # tip["flag"] = 28
    tipsFile.Close()
    
    
def InfoRangeIncrease(mult, isMute):
    areaInfoIDs = [1001,1101,1201,1301,1401,1501,1601,1701,2001,2201]
    for info in areaInfoIDs:
        infoFile = JSONParser.File(f"XCXDE/JsonOutputs/common/FLD_TownInfo{info}.json")
        for info in infoFile.rows:
            info["radius"] = info["radius"]*mult
            if isMute:
                for i in range(1,6):
                    info[f"voice{i}"] = ""
        infoFile.Close()
        
def EasyStoryPrerequisites():
    qstFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_questlist.json")
    chapterPrereqIDs = [15, 20, 26, 32, 42, 47, 54, 62, 68, 73, 81, 2465, 2477, 2503]
    for qst in qstFile.rows:
        if qst["$id"] in chapterPrereqIDs:
            qst["HexCondition"] = 1
    qstFile.Close()

def SkellExamSkip():
    # Reduce the required count of certificates
    colFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_QuestCollect.json")
    for col in colFile.rows:
        if col["$id"] == 175:
            col["count"] = 0
            break
    colFile.Close()        
    
    
    qstFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_questlist.json")
    for qst in qstFile.rows: # Next quest to the actual scene of getting a skell so you just go directly to it
        if qst["$id"] == 1143:
            qst["next_quest_a"] = 1662
            break
    qstFile.Close()
    

# def TTRLSkip(): # Didnt work
#     tutFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_EventPopList.json")
#     for tut in tutFile.rows:
#         tut["script_name"] = ""
#         # tut["script_start_id"] = 0
#     tutFile.Close()    

def FasterClassRanks(spin):
    # might be breaking since you learn multiple ranks at once
    for i in range(1, 39):
        clsFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{i:02}Growth.json")
        for cls in clsFile.rows:
            cls["Exp"] = max(cls["Exp"] // spin, 1)       
        
        # AdjustLevelsDifferently(clsFile, "Exp")
            
        clsFile.Close()

def AdjustLevelsDifferently(file:JSONParser.File, key):
    '''Ensures each level up is a higher amount of XP (didnt help)'''
    lastrow = 0
    for cls in file.rows:
        while cls[key] <= lastrow:
            cls[key] += 1
        lastrow = cls[key]

def FasterLevels(mult):
    ''''''
    growFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_Growlist.json")
    for lv in growFile.rows:
        for key in ["LevelExp", "LevelExpRental"]:
            lv[key] = max(lv[key] // mult, 1)
    
    growFile.Close()

 
def EarlyFlight():
    '''Unlocks skell flight as soon as you get skells'''
    sklFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_DlList.json")
    for skl in sklFile.rows:
        skl["FlgSky"] = 1
    sklFile.Close()
    
  
def OpWep():
    with open("XCXDE/JsonOutputs/common/WPN_PcList.json", 'r+', encoding='utf-8') as wpFile:
        wpData = json.load(wpFile)
        for wep in wpData["rows"]:
            if wep["$id"] in [1583, 543]:
                wep["Damage"] = 3500
                wep["Magazine"] = 100
                wep["DMRatio"] = 3500
                wep["Recast"] = 1
                
                
        JSONParser.CloseFile(wpData, wpFile)
        
def ClearEnemyWeatherCondition():
    '''Enemies show up in all weather conditions'''
    popFile = JSONParser.File("XCXDE/JsonOutputs/common/CHR_EnPopParam.json")
    for pop in popFile.rows:
        pop["DePopWeather"] = 0 # Does not disappear in any weather
        pop["PopWeather"] = 4294967295 # THe bit mask for showing up in all weathers
    popFile.Close()

def EarlyVandahmQuest():
    # Just let them get skell whenever they want
    # Make that vandahm always show up (unless condition 2 which is the quest being complete so he goes away)
    vandahmCH6Condition = 3083
    condFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_GameCondition.json")
    for cond in condFile.rows:
        if cond["$id"] == vandahmCH6Condition: 
            cond["cond1"] = 115
    condFile.Close()            
    
    # Make him ready to give the quest
    talkFile = JSONParser.File("XCXDE/JsonOutputs/common/NPC_talk5000.json")
    for talk in talkFile.rows:
        if talk["$id"] in [4,5]: # YOu have to edit 4 AND 5 I do not know why
            talk["script"] = "qev096101"
            talk["check"] = 0
            talk["uid"] = 24
            talk["id"] = 1143
    talkFile.Close()    
    
    # Make the submissions not show up to avoid clicking through them 
    proficiencyExamIDs = [1146, 1148, 1150, 1152, 1154, 1156, 1158, 1160]
    qstFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_questlist.json")
    for qst in qstFile.rows:
        if qst["$id"] in proficiencyExamIDs:
            qst["window_disp"] = 0
    qstFile.Close()
    # category 4 # Didnt matter for displaying just changed the background
    # windowdisplay 0
    # flagtype = 0

# # Didnt work menu wouldnt allow you to outfit, refuel reassign skells
# def EarlySkell(chosenChapter):
#     '''Users can choose what chapter they want to get the level 15 skell at and unlock skells in general'''
#     getSkellQuestID = 1662
#     # talkToWalter = 1145 (he requires the skell liscenses can probably remove that)
#     # getSkell
#     chapterDict = {
#         2: 15,
#         3: 20,
#         4: 26,
#         5: 32,
#         6: 42
#     }
#     qstFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_questlist.json")
#     for qst in qstFile.rows:
#         if qst["$id"] == chapterDict[chosenChapter]:
#             qst["next_quest_a"] = getSkellQuestID
#     for qst in qstFile.rows:
#         if qst["$id"] == getSkellQuestID:
#             qst["next_quest_a"] = chapterDict[chosenChapter] + 1
#             qst["prt_quest_id"] = chapterDict[chosenChapter]
#     qstFile.Close()
    
# Cant just zero out the fields it breaks. It requires one material and one rarersc minimum. Not worth it.
# def EasyGemCrafting():
#     import random
#     from 
#     gemFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_ItemSkill_inner.json")
#     for gem in gemFile.rows:
#         for i in range(0,3):
#             # RareRsc
#             gem[f"materialST[{i}]"] = random.choice(IDs.) # Material
#             gem[f"mctST[{i}]"] = 1 # Material Count
#             # Material
#             gem[f"materialMA[{i}]"] = random.choice(IDs.MaterialIDs) # Material
#             gem[f"mctMA[{i}]"] = 1 # Material Count
#     gemFile.Close()
    
# FLD_ConditionList_Scenario -> FLD_GameCondition -> FLD_NpcPopGimmick (CONDITION1 parameter)
# So setting condition1 = 682 allows npc to show up all the time since 682 in FLD_GameCondition is during the whole game

# FLD_Condition are just what a quest requires
# ballooncond -> FLD_GameCondition