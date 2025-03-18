import json, Options

def TutorialSkips(): 
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_ttrl/MNU_ttrl.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for f in tutData["rows"]:
            f["page"] = 0 # Makes 0 pages but still pulls up the menu
            # f["type"] = 0 # Stops tutorials but the tutorial wont set its flags
            # f["order"] = 0
            # f["proc_value1"] = 0
                
        tutFile.seek(0)
        tutFile.truncate()
        json.dump(tutData, tutFile, indent=2, ensure_ascii=False)