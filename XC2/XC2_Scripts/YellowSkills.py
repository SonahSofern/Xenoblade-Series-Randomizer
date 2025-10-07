import json, random
from XC2.XC2_Scripts import Options, IDs
from scripts import Helper
def RandomizeBattleSkills(): # Make logic to have all skills in the game
    with open("./XC2/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as bladeFile:
        bladeData = json.load(bladeFile)
        isDuplicates = Options.BladeBattleSkillsOption_Duplicates.GetState()
        odds = Options.BladeBattleSkillsOption.GetSpinbox()

        SkillPool = list(IDs.BladeBattleSkills)
        
        KeepVanilla = {
            1111: ["BSkill1"] # Elma Overdrive
        }
        Slots = ["BSkill1","BSkill2", "BSkill3"]
        
        for blade in bladeData["rows"]:     
            
            BladeId = blade["$id"]
            
            if BladeId in IDs.InvalidBladeSkillTreeIDs: # Ignore bad blades
                continue
               
                
            for slot in Slots:
                
                if ((KeepVanilla.get(BladeId) != None) and slot in KeepVanilla[BladeId]):
                    continue
                  
                if blade[slot] == 0: # Only replace skillslots that have one (dagas needs this for his weak form)
                    continue
                
                if not Helper.OddsCheck(odds): # Roll odds
                    continue
                
                Skill = random.choice(SkillPool) # Choose and Set a skill
                
                if not isDuplicates:
                    SkillPool.remove(Skill)
                blade[slot] = Skill

        bladeFile.seek(0)
        bladeFile.truncate()
        json.dump(bladeData, bladeFile, indent=2, ensure_ascii=False)