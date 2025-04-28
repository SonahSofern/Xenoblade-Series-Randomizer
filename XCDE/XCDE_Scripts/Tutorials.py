import json, Options


def TutorialSkips(): 
    UnskippableTutorials = [1, 6, 18]
    MechonTutorials = [29] # Ids for tutorials relating to fights with mechon it wont load for some reason if the proc_type is default
    with open("./XCDE/_internal/JsonOutputs/bdat_menu_ttrl/MNU_ttrl.json", 'r+', encoding='utf-8') as tutFile:
        tutData = json.load(tutFile)
        dupeFlags = []
        for f in tutData["rows"]:
            # if f["$id"] not in UnskippableTutorials:
            #     f["type"] = 0 # Stops tutorials but the tutorial wont set its flags so cant be applied to all
            
            if f["$id"] in MechonTutorials:
                f["proc_type"] = 0
                
            if f["scenario_flag"] in dupeFlags:
                f["type"] = 0
                f["proc_type"] = 0 # Set these for fights with tutorials seem to crash wthiout it
                f["proc_value1"] = 0
                f["proc_value2"] = 0
            else:
                dupeFlags.append(f["scenario_flag"])
                
            f["page"] = 1 # Makes the tutorial only 1 page skipping unnesccesary ones
            
            
                # could this unlock your menu stuff https://xenobladedata.github.io/xb1de/bdat/bdat_common/MNU_game_option_item.html
        tutFile.seek(0)
        tutFile.truncate()
        json.dump(tutData, tutFile, indent=2, ensure_ascii=False)