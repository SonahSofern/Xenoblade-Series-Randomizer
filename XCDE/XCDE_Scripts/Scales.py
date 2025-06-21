import json, random
from XCDE.XCDE_Scripts import Options
from scripts import JSONParser, Helper
from XCDE.XCDE_Scripts.IDs import *

def EnemyScales(): # Try editing the size flag as well since
    scales = [0.2,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1]
    odds = Options.EnemyScaleOption.GetSpinbox()
    for file in areaFileListNumbers:
        try:   
            with open(f"./XCDE/JsonOutputs/bdat_ma{file}/BTL_enelist{file}.json", 'r+', encoding='utf-8') as eneAreaFile:
                eneAreaData = json.load(eneAreaFile)
                for en in eneAreaData["rows"]:
                    if en["$id"] in (BossEnemies + [2504]): # Excluded Mechonis in Egil Fight
                        continue
                    if Helper.OddsCheck(odds):
                        mult = random.choice(scales)
                        en["scale"] = min(int(en["scale"] * mult),255)
                        en["size"] = min(int(en["size"] * mult),8)
                JSONParser.CloseFile(eneAreaData, eneAreaFile)
        except:
            pass
            
def NPCScales():
    odds = Options.NPCScaleOption.GetSpinbox()
    with open(f"./XCDE/JsonOutputs/bdat_common/FLD_npclist.json", 'r+', encoding='utf-8') as npcFile:
        npcData = json.load(npcFile)
        for npc in npcData["rows"]:
            if Helper.OddsCheck(odds):
                npc["scale"] = random.randrange(20,400)
        JSONParser.CloseFile(npcData, npcFile)
        
