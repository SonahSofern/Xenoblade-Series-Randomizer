import JSONParser

def BypassStoryFieldSkillChecks():
    print("Removing Story Field Skill Checks")

    ids = [
        1106, 1107, # Kindle Flame, Early Chapter 2
        1077,       # Pyra's Cooking,
        1116, 1117, # Brute Force, Vent/Valve in Gormott Titan Battleship
        # ...
    ]

    JSONParser.ChangeJSONLine(["common/FLD_FieldSkillSetting.json"], ids, ["FieldSkillLevel1", "FieldSkillLevel2"],0)
