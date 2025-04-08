import json, Options


def TutorialSkips(): 
    UnskippableTutorials = [1, 6, 18]
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_ttrl/MNU_ttrl.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        for f in tutData["rows"]:
            if f["$id"] not in UnskippableTutorials:
                f["type"] = 0 # Stops tutorials but the tutorial wont set its flags so cant be applied to all
            f["page"] = 1 # Makes the tutorial only 1 page skipping unnesccesary ones
                  
            # f["page"] = 0 # Makes 0 pages but still pulls up the menu
            # f["order"] = 0
            # f["proc_value1"] = 0
            # f["proc_type"] = 0
            # f["type_cat"] = 2 Cant tell what it does
            
                # could this unlock your menu stuff https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_game_option_item.html
        tutFile.seek(0)
        tutFile.truncate()
        json.dump(tutData, tutFile, indent=2, ensure_ascii=False)