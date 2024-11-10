import JSONParser

def FixDescriptionText():
    JSONParser.ChangeJSON("", ["common_ms/menu_ms.json"], ["name"], ["Auto-Attack"], 100, ["Strength"], []) # Changes Auto-Attack to Strength

def FixOptionText():
    JSONParser.ChangeJSON("", ["common_ms/menu_option_name_ms.json"], ["name"], ["Battle Narration volume"], 100, ["Narrator volume"], [])
    JSONParser.ChangeJSON("", ["common_ms/menu_option_cap_ms.json"], ["name"], ["Adjust volume of narration heard\nduring battle."], 100, ["Adjust volume of the battle narrator"], [])
    
FixOptionText()
FixDescriptionText()