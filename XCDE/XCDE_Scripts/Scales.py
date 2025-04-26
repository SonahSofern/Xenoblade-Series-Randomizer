import IDs, json, random, Options
from scripts import JSONParser, Helper


def EnemyScales():
    scales = [0.2,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1,2.5,3.0,4,5,6,7,8]
    for file in IDs.areaFileListNumbers:
        try:   
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                eneAreaData = json.load(eneAreaFile)
                odds = Options.EnemyScaleOption.GetSpinbox()
                for en in eneAreaData["rows"]:
                    if Helper.OddsCheck(odds):
                        en["scale"] = min(int(en["scale"] * random.choice(scales)),255)
                JSONParser.CloseFile(eneAreaData, eneAreaFile)
        except:
            pass
            