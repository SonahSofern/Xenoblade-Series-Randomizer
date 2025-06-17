# KP_list has the models
import json, random
from scripts import JSONParser, Helper, PopupDescriptions
from  XCDE.XCDE_Scripts import Options, IDs

def NPCModelRando():
    odds = Options.NPCModelsOption.GetSpinbox()
    ObjectList = []
    dontReplace = Helper.InclRange(654,680) + [650,651]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/KP_list.json", 'r+', encoding='utf-8') as lmFile:
        lmData = json.load(lmFile)
        for lm in lmData["rows"]:
            if (lm["$id"] in dontReplace) or (not (lm["model"].startswith("en") or lm["model"].startswith("np"))):
                continue
            ObjectList.append([lm["model"], lm["motion"], lm["action"], lm["effect"], lm["sound"]])

        for lm in lmData["rows"]:
            if lm["$id"] in dontReplace or (not lm["model"].startswith("np")):
                continue
            if not Helper.OddsCheck(odds):
                continue
                
            choice = random.choice(ObjectList)
            lm["model"] = choice[0]
            lm["motion"] = choice[1]
            lm["action"] = choice[2]
            lm["effect"] = choice[3]
            lm["sound"] = choice[4]   
            # lm["model"] = 	"np020201"				
            # lm["motion"] = "mn020101"
            # lm["action"] = "mn020208"
            # lm["effect"] = ""
            # lm["sound"] = "sn302701"               
        JSONParser.CloseFile(lmData, lmFile)


