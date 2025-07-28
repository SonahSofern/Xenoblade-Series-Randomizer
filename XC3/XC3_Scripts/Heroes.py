# Randomizes the characters in the story including heroes
import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions

def HeroSwaps():
    with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile: # This method didnt work cant change motion and also icons (probably should just use the quest that unlocks them, swapping it to unlocking another)
        charData = json.load(charFile)
        Chars = []
        Heroes = [7,8,10,11,12]
        ignoreKeys = ["$id"]
        for char in charData["rows"]:            
            if char["$id"] not in Heroes:
                continue
            Chars.append(copy.deepcopy(char))
            
        for char in charData["rows"]:
            if char["$id"] not in Heroes:
                continue
            
            chosenChar = random.choice(Chars)
            
            # Chars.remove(chosenChar)
            for key in char:
                if key in ignoreKeys:
                    continue
                char[key] = chosenChar[key]
        JSONParser.CloseFile(charData, charFile)
    # with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile: # This method didnt work cant change motion and also icons (probably should just use the quest that unlocks them, swapping it to unlocking another)
    #     charData = json.load(charFile)
    #     talents = [18,19,20]
    #     for char in charData["rows"]:
    #         char["DefTalent"] = random.choice(talents)
    #     JSONParser.CloseFile(charData, charFile)

# https://xenobladedata.github.io/xb3_200_dlc4/MNU_HeroList.html#17
        
        
        
        
