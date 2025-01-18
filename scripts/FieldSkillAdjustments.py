import JSONParser, Helper

    
def DisableRequiredFieldSkills(Options):
    onlyStory  = Options["Disable Story Field Skill Checks"]["subOptionObjects"]["Disable All Field Skill Checks"]["subOptionTypeVal"].get()
    
    if onlyStory:
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
    else:
        mapGimmickIds = range(1,186)
        npcPopIds = []     
        jumpGimiickIds = []

    
    JSONParser.ChangeJSONLine(["common_gmk/FLD_MapGimmick.json"], mapGimmickIds, ["FSID"], 0)
    JSONParser.ChangeJSONLine(["common_gmk/FLD_JumpGimmick.json"], jumpGimiickIds, ["FSID"], 0)
    for item in npcPopIds:
        try:
        JSONParser.ChangeJSONLine([f"common_gmk/ma0{item[0]}"], mapGimmickIds, ["FSID"], 0)

