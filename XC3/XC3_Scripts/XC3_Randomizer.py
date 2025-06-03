import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
root = Tk()
import scripts.XCRandomizer, SeedNames, scripts.JSONParser, Options

Version = "BETA"


backgrounds = ["col9.jpg"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["menu/msg_mnu_title.json"],[11], ["name"], f"Randomizer v{Version}", Game="XC3") # Change Title Version to Randomizer vX.x.x

extraArgs= ["--hashes", "./XC3/_internal/Toolset/xbc3Hashes.txt"]
extraCommands = [lambda: ShowTitleScreenText()]
mainFolderNames = ["des", "btl", "evt", "fld", "map", "prg", "qst"]
subFolderNames = ["autotalk", "battle", "field", "menu", "quest", "system"]
textFolderName="gb/game"

scripts.XCRandomizer.CreateMainWindow(root, "XC3", Version, "Xenoblade Chronicles 3 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, textFolderName,extraArgs=extraArgs, backgroundImages=backgrounds)
