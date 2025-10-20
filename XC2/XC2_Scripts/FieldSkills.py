import json, random
from scripts import JSONParser
from XC2.XC2_Scripts import Options, IDs

def RandomizeFieldSkills(): # Make logic to have all skills in the game
    with open("./XC2/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as bladeFile:
        bladeData = json.load(bladeFile)
        
        # Base 
        BaseSkillPool = [17, 22, 38, 11, 3, 23, 20, 24, 21, 18, 25, 4, 19, 23, 2, 13, 18, 10, 19, 7, 14, 18, 6, 11, 2, 25, 11, 23, 20, 21, 12, 22, 16, 20, 16, 38, 7, 19, 19, 25, 24, 9, 24, 4, 38, 11, 9, 15, 22, 24, 15, 23, 38, 14, 18, 16, 3, 6, 25, 21, 9, 12, 6, 38, 18, 2, 25, 13, 19, 14, 22, 13, 21, 20, 5, 20, 3, 12, 17, 18, 14, 21, 2, 15, 14, 4, 19, 12, 18, 22, 16, 9, 23, 14, 20, 6, 10, 7, 25, 12, 24, 3, 13, 21, 5, 24, 7, 23, 4, 6, 9, 2, 7, 6, 7, 10, 4, 6, 9, 2, 3, 10, 4, 6, 9, 2, 7, 6, 7, 10, 11, 20, 23, 4, 19, 22, 10, 22, 14, 18, 6, 13, 21, 5, 14, 20, 6, 14, 20, 6, 10, 7, 25, 12, 24, 3, 4, 6, 9, 2, 7, 4, 6, 9, 2, 7, 2, 3, 10, 4, 6, 9, 11, 20, 23, 4, 6, 9, 2, 7, 4, 6, 9, 2, 7, 2, 3, 10, 4, 6, 9, 11, 20, 23, 14, 21, 10, 19, 7, 16, 9, 20, 5, 9, 21, 9, 19, 23, 6, 25, 24, 17, 2, 23, 4, 25, 19, 22, 18, 17, 2, 23]
        BaseGameBladeIDs = [1001,1002,1004,1005,1006,1007,1008,1009,1010,1011,1014,1015,1017,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1034,1035,1037,1038,1039,1040,1041,1043,1044,1045,1046,1047,1048,1049,1050,1073,1077,1104,1105,1106,1107,1108,1109,1110,1111]
        
        # Torna
        TornaSkillPool = [72, 58, 66, 68, 59, 65, 67, 60, 73, 70, 63, 69, 64, 71, 62, 61]
        TornaBladeIDs = [1124,1125,1126,1127,1128,1129,1130,1131,1132]
        
        ShuffleQuestSkills = Options.BladeFieldSkillsOption_QuestSkills.GetState()
        QuestSkillPool = [74, 73, 31, 35, 46, 33,37,39,26,43,44,57,34,40,51,29,30,45,47,36,28,32,42,50,48,58,41,49]     

        # Carveouts to make sure the story is completeable
        KeepVanilla = {
            1001: ["FSkill1","FSkill2", "FSkill3"], # Pyra fire mastery and focus, cooking
            1008: ["FSkill2"], # Roc Miasma
            1005: ["FSkill3"], # Poppia superstrength
            1127: ["FSkill2"],  # Jin Swift Swordplay
            1128: ["FSkill2"] # Haze Ether Miasma
        }
        Slots = ["FSkill1","FSkill2", "FSkill3"]
        
        if ShuffleQuestSkills: # Add in our quest skills
            BaseSkillPool.extend(QuestSkillPool) 
        
        for blade in bladeData["rows"]:     
            
            BladeId = blade["$id"]
            
            if BladeId in IDs.InvalidBladeSkillTreeIDs: # Ignore bad blades
                continue
               
            if BladeId in BaseGameBladeIDs: # Decide which pool Torna or Original Game
                Pool = BaseSkillPool
            elif BladeId in TornaBladeIDs:
                Pool = TornaSkillPool
                
            for slot in Slots:
                
                if not ShuffleQuestSkills and (blade[slot] in QuestSkillPool): # Keep unique skills on that blade
                    continue
                
                if ((KeepVanilla.get(BladeId) != None) and slot in KeepVanilla[BladeId]): # Ignore special blades to make sure story is completeable
                    continue
                  
                if blade[slot] == 0: # Only replace skillslots that have one (dagas needs this for his weak form)
                    continue
                  
                Skill = random.choice(Pool) # Choose and Set a skill
                Pool.remove(Skill)
                blade[slot] = Skill
                
        JSONParser.CloseFile(bladeData, bladeFile)
        
        
def RemoveFieldSkills():
    isAllChecks  = Options.RemoveFieldSkillsOption_AllFieldSkills.GetState()
    UMHUNT = Options.UMHuntOption.GetState()
    if isAllChecks or UMHUNT:
        mapGimmickIds = range(1,186)
        npcPopIds = range(1,50000)     
        jumpGimiickIds = range(1,45)
        tBoxIds = range(1,4000)
        diveIds = range(1,12)
    else:
        mapGimmickIds = [
            4, 5,           # Trees in early Gormott
            16, 11,          # Vent/Valve in Gormott Titan Battleship
            36,             # Tardy Gate flood blockade
            7,              # Ether Miasma
            55, 57,         # Old Factory ventilation fans
            111,            # Spider Web
            113,            # Stele of Judgement
            37,             # World Tree Skyport
            129             # The Door
        ]
        npcPopIds = [
            8006,           # Green Barrel
            5267,           # Pyra's Cooking
            5268            # Pyra's Cooking
        ]    
        jumpGimiickIds = [
            34, 33, 38,      # Cliffs of Morytha
            39, 42           # Temperantia wind jump
        ]        
        
        tBoxIds = [] # No required treasure chests
        
        diveIds = [] # No required dive spots

    JSONParser.ChangeJSONLine(["common_gmk/FLD_MapGimmick.json"], mapGimmickIds, ["FSID"], 0)
    JSONParser.ChangeJSONLine(["common_gmk/FLD_JumpGimmick.json"], jumpGimiickIds, ["FSID"], 0)
    JSONParser.ChangeJSONLine(["common_gmk/FLD_WarpGimmick.json"], diveIds, ["FSID"], 0)
    
    JSONParser.ChangeJSONLine(["common/FLD_FieldSkillSetting.json"],[1294,1077],["FieldSkillLevel1", "FieldSkillLevel2"], 0)
    for i in range(51):
        JSONParser.ChangeJSONLine([f"common_gmk/ma{i:02}a_FLD_NpcPop.json"], npcPopIds, ["FSID1", "FSID2", "FSID3"], 0)
        JSONParser.ChangeJSONLine([f"common_gmk/ma{i:02}a_FLD_TboxPop.json"], tBoxIds, ["FSID", "FSID2"], 0)

