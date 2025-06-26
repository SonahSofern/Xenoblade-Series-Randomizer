# Randomizes the characters in the story including heroes
import json, random
from scripts import JSONParser, Helper, PopupDescriptions

def CharacterSwaps(): # For some reason visually the game wont load the entire hud until aftyer the first boss in the intro but thats fine
    with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile:
        charData = json.load(charFile)
        Chars = list((h.copy for h in charData["rows"] if h not in [1,2,3,4,5,6]))
        
        
        for char in charData["rows"]:
            if char["$id"] in [1,2,3,4,5,6]:
                continue
        for i in range(0,len(Chars)):
            pass
        JSONParser.CloseFile(charData, charFile)

        
        
        
        
        
