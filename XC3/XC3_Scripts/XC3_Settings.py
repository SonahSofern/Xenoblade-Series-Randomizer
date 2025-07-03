import scripts.JSONParser, scripts.XCRandomizer
from XC3.XC3_Scripts import SeedNames, Options
Version = "BETA"
Game = "XC3"
Title = "Xenoblade Chronicles 3"

backgrounds = ["col9.jpg"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["menu/msg_mnu_title.json"],[11], ["name"], f"Randomizer v{Version}", Game="XC3") # Change Title Version to Randomizer vX.x.x
seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

extraArgs= ["--hashes", "Toolset/xbc3Hashes.txt"]
extraCommands = [lambda: ShowTitleScreenText()]
mainFolderNames = ["des", "btl", "evt", "fld", "map", "prg", "qst", "sys", "zzz"] # "mnu"
subFolderNames = ["autotalk", "battle", "field", "menu", "quest", "system"]
textFolderName="gb/game"
