import JSONParser

def BypassStoryFieldSkillChecks():
    print("Removing Story Field Skill Checks")

    ids = [
        1106, 1107,         # Trees in early Gormott
        1077,               # Pyra's Cooking,
        1116, 1117,         # Vent/Valve in Gormott Titan Battleship
        1399,               # Tardy Gate flood blockade
        1109,               # Ether Miasma
        1294,               # Green Barrel
        1226, 1447,         # Old Factory ventilation fans
        1443,               # Temperantia wind jump
        1302,               # Spider Web
        1304,               # Stele of Judgement
        1312, 1313, 1442,   # Cliffs of Morytha
        1324,               # World Tree Skyport
        1327,               # The Door
    ]

    JSONParser.ChangeJSONLine(["common/FLD_FieldSkillSetting.json"], ids, ["FieldSkillLevel1", "FieldSkillLevel2"],0)

    # TODO: Add suboption to remove all skill checks, not just the main story ones