import JSONParser

    
def RemoveFieldSkills(Options):
    isAllChecks  = Options["Remove Story Field Skills"]["subOptionObjects"]["Remove All Field Skills"]["subOptionTypeVal"].get()
    
    if isAllChecks:
        mapGimmickIds = range(1,186)
        npcPopIds = range(1,50000)     
        jumpGimiickIds = range(1,45)
    else:
        mapGimmickIds = [
            4, 5,           # Trees in early Gormott
            10,11,          # Vent/Valve in Gormott Titan Battleship
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
            5268            # Pyra's Cooking
        ]    
        jumpGimiickIds = [
            34, 33,38,      # Cliffs of Morytha
            39,42           # Temperantia wind jump
        ]        

    
    JSONParser.ChangeJSONLine(["common_gmk/FLD_MapGimmick.json"], mapGimmickIds, ["FSID"], 0)
    JSONParser.ChangeJSONLine(["common_gmk/FLD_JumpGimmick.json"], jumpGimiickIds, ["FSID"], 0)
    for i in range(51): # Fix 0i its going to be 025 for example at 2 digits
        JSONParser.ChangeJSONLine([f"common_gmk/ma0{i}a_FLD_NpcPop.json"], npcPopIds, ["FSID1", "FSID2", "FSID3"], 0)

