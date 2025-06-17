import scripts.JSONParser
from XC3.XC3_Scripts import SeedNames, Options
Version = "BETA"


backgrounds = ["col9.jpg"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["menu/msg_mnu_title.json"],[11], ["name"], f"Randomizer v{Version}", Game="XC3") # Change Title Version to Randomizer vX.x.x

extraArgs= ["--hashes", "./XC3/_internal/Toolset/xbc3Hashes.txt"]
extraCommands = [lambda: ShowTitleScreenText()]
mainFolderNames = ["des", "btl", "evt", "fld", "map", "prg", "qst"]
subFolderNames = ["autotalk", "battle", "field", "menu", "quest", "system"]
textFolderName="gb/game"

