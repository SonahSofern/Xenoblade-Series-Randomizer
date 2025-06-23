import json, random
from scripts import JSONParser, Helper, PopupDescriptions


def SkillRando():
    copiedStats = ["Name", "Enhance1","Enhance2","Enhance3","Enhance4","Enhance5", "Icon"]
    with open("XC3/JsonOutputs/btl/BTL_Skill_PC.json", 'r+', encoding='utf-8') as skillFile:
        skillData = json.load(skillFile)
        TalentList = []
        for skill in skillData["rows"]: # Build the list from the original data
            if skill["Name"] == 0:
                continue
            testDict = {}
            for stat in copiedStats:
                testDict[stat] =  skill[stat]
            TalentList.append(testDict)

        for skill in skillData["rows"]: # Replace the list
            if skill["Name"] == 0:
                continue
            chosen = random.choice(TalentList)
            for stat in copiedStats:
                skill[stat] = chosen[stat]
            TalentList.remove(chosen)

        JSONParser.CloseFile(skillData, skillFile)
