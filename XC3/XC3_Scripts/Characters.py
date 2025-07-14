# Randomizes the characters in the story including heroes
import json, random
from scripts import JSONParser, Helper, PopupDescriptions

def CharacterSwaps(): # For some reason visually the game wont load the entire hud until aftyer the first boss in the intro but thats fine
    with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile: # This method didnt work cant change motion and also icons (probably should just use the quest that unlocks them, swapping it to unlocking another)
        charData = json.load(charFile)
        ignoreChar = [1,2,3,4,5,6,30,31,28,14,9,34,35,36,37,38,39,40,41,42,43]
        testchars = [7,8,10,11,12]
        Chars = []
        uncopiedKeys = ['$id', 'ID']
        unusedKeys = ['ObjSlot3', 'IK', 'Effect', 'Still', 'Voice', 'AiID', 'ChestHeight', 'LandingHeight', 'Swim', 'FootStep', 'FootStepEff', 'FootPrintDetection', 'DefLvType', 'DefLv', 'DefTalent', 'DefTalentLv', 'DefAcce1', 'DefAcce2', 'DefAcce3', 'DefGem1', 'DefGem2', 'DefGem3', 'HpMaxLv1', 'StrengthLv1', 'PowHealLv1', 'DexLv1', 'AgilityLv1', 'HpMaxLv99', 'StrengthLv99', 'PowHealLv99', 'DexLv99', 'AgilityLv99', 'UroBody', 'UroPartner', 'UroCondition', 'TalentNPCArts1', 'TalentNPCArts2', 'TalentNPCArts3', 'TalentNPCArts4', 'TalentNPCArts5', 'TalentNPCArtsCond1', 'TalentNPCArtsCond2', 'TalentNPCArtsCond3', 'TalentNPCArtsCond4', 'TalentNPCArtsCond5', 'TalentNPCTalentArts', 'TalentNPCTalentArtsCond', 'TalentNPCSkill1', 'TalentNPCSkill2', 'TalentNPCSkill3', 'TalentNPCSkill4', 'TalentNPCSkill5', 'TalentNPCSkill6', 'TalentNPCSkillCond1', 'TalentNPCSkillCond2', 'TalentNPCSkillCond3', 'TalentNPCSkillCond4', 'TalentNPCSkillCond5', 'TalentNPCSkillCond6', 'OffsetID', 'EffScale', 'MeatType', 'BoneCamera', 'ChainOrder', 'Flag_WpnReinforced', 'TP_Min', 'TP_Max', 'PT_OutTiming', 'HeroChainEff', 'PowAugment', '<9DB71964>', 'UniqueDirection', 'DefPair']
        testKeys = ['Motion']
        copiedKeys = ['Name', 'DebugName', 'Atr', 'Gender', 'Race', 'Force', 'MealMountObj', 'CookMainMountObj', 'CookAssistMountObj', 'DefTalentModel','SpModel1', 'SpModelCond1', 'SpModel2', 'SpModelCond2', 'Type','ObjSlot1', 'ObjSlot2']
        for char in charData["rows"]:            
            if char["$id"] in ignoreChar:
                continue
            Chars.append(char.copy())
        for char in charData["rows"]:
            if char["$id"] in ignoreChar:
                continue
            chosenChar = random.choice(Chars)
            Chars.remove(chosenChar)
            for key in copiedKeys + unusedKeys + testKeys:
                char[key] = chosenChar[key]
        JSONParser.CloseFile(charData, charFile)
    # with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile: # This method didnt work cant change motion and also icons (probably should just use the quest that unlocks them, swapping it to unlocking another)
    #     charData = json.load(charFile)
    #     talents = [18,19,20]
    #     for char in charData["rows"]:
    #         char["DefTalent"] = random.choice(talents)
    #     JSONParser.CloseFile(charData, charFile)

# https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroList.html#17
        
        
        
        
