import json, random, Options, IDs
def RandomizeBattleSkills(): # Make logic to have all skills in the game
    # Drivers
    with open("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as bladeFile:
        bladeData = json.load(bladeFile)
        isDuplicates = Options.BladeBattleSkillsOption_Duplicates.GetState()
        odds = Options.BladeBattleSkillsOption.GetOdds()
        # Base 
        SkillPool = list(IDs.BladeBattleSkills)
        InvalidBladeIDs = [1012, 1013, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1074, 1003, 1103, 1112, 1081, 1102, 1078, 1079, 1076, 1080, 1075, 1042, 1012, 1018, 1033, 1016, 1036, 1072, 1067, 1068, 1065, 1071, 1070, 1066, 1069, 1060, 1061, 1058, 1064, 1063, 1059, 1062, 1053, 1054, 1051, 1057, 1056, 1052, 1055]
        
        # Carveouts to make sure the story is completeable
        KeepVanilla = {
            1003: ["BSkill1", "BSkill2", "BSkill3"], # Pneuma All since you cant view her skills it doesnt make sense to randomize
            1111: ["BSkill1"] # Elma Overdrive
        }
        Slots = ["BSkill1","BSkill2", "BSkill3"]
        
        for blade in bladeData["rows"]:     
            
            BladeId = blade["$id"]
            
            if BladeId in InvalidBladeIDs: # Ignore bad blades
                continue
               
                
            for slot in Slots:
                
                if (KeepVanilla.get(BladeId) and slot in KeepVanilla[BladeId]): # Ignore special blades to make sure story is completeable
                    continue
                  
                if blade[slot] == 0: # Only replace skillslots that have one (dagas needs this for his weak form)
                    continue
                
                
                Skill = random.choice(SkillPool) # Choose and Set a skill
                if not isDuplicates:
                    SkillPool.remove(Skill)
                blade[slot] = Skill

        bladeFile.seek(0)
        bladeFile.truncate()
        json.dump(bladeData, bladeFile, indent=2, ensure_ascii=False)