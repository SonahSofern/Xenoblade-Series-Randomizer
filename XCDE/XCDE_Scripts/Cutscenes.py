import json, random
from XCDE.XCDE_Scripts import Options
from scripts import JSONParser, Helper

def CutsceneSkipper():
    with open("./XCDE/_internal/JsonOutputs/bdat_evt/EVT_sev.json", 'r+', encoding='utf-8') as eventFile:
        evData = json.load(eventFile)
            
        for ev in evData["rows"]: # remonving event and script on both the files didnt work sev and cs
            # ev["event"] = "" # Didnt do anythin
            # ev["scenario_flag"] = 0
            # ev["map"] = ""
            # ev["set_scenario_flag"] = 388
            ev["script"] = ""
            ev["scenario_flag"] = 0
                
        JSONParser.CloseFile(evData, eventFile)