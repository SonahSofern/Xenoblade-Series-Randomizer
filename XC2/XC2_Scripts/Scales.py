import json, random, Options
from scripts import Helper


def BladeScales():
    BladeScales = [20,30,40,50,60,70,80,90,110,120,130,140,160,180,200,400]

    with open(f"./XC2/_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as bladeFile:
        bladeData = json.load(bladeFile)
        odds = Options.BladeSizeOption.GetSpinbox()
        for blade in bladeData["rows"]:
            if not Helper.OddsCheck(odds): # Check spinbox
                continue
            scale = random.choice(BladeScales)  # Make our selection
            blade["Scale"] =  scale
            blade["WpnScale"] = scale
        bladeFile.seek(0)
        bladeFile.truncate()
        json.dump(bladeData, bladeFile, indent=2, ensure_ascii=False)

def NPCScales():
    NPCScales = [20,30,40,50,60,70,80,90,110,120,130,140,160,180,200,400,600]
    
    with open(f"./XC2/_internal/JsonOutputs/common/RSC_NpcList.json", 'r+', encoding='utf-8') as npcFile:
        npcData = json.load(npcFile)
        odds = Options.NPCSizeOption.GetSpinbox()
        for npc in npcData["rows"]:
            if not Helper.OddsCheck(odds): # Check spinbox
                continue
            npc["Scale"] = random.choice(NPCScales)  # Make our selection
        npcFile.seek(0)
        npcFile.truncate()
        json.dump(npcData, npcFile, indent=2, ensure_ascii=False)


def EnemyScales():
    EnemyScales= [10,20,30,40,50,60,70,80,90,110,120,130,140,160,180,200,400,600]
    
    with open(f"./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as enFile:
        enData = json.load(enFile)
        odds = Options.EnemySizeOption.GetSpinbox()
        for en in enData["rows"]:
            if not Helper.OddsCheck(odds): # Check spinbox
                continue
            en["Scale"] = random.choice(EnemyScales)  # Make our selection
        enFile.seek(0)
        enFile.truncate()
        json.dump(enData, enFile, indent=2, ensure_ascii=False)
