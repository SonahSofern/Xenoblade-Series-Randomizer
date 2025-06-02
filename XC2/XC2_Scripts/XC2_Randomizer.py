import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
root = Tk()
import scripts.XCRandomizer, SeedNames, scripts.JSONParser, Options

Version = "1.5.0"


Tabs = {
    1: "General",
    2: "Drivers",
    3: "Blades",
    4: "Enemies",
    5: "Misc",
    6: "Quality of Life",
    7: "Funny",
    8: "Cosmetics",
    9: "Game Modes",
    10: "Torna"
}

backgrounds = ["titlescreen1.png"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], f"Randomizer v{Version}") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.Enhancements.AddCustomEnhancements(), lambda: Options.TornaMain.PassAlongSpoilerLogInfo(scripts.XCRandomizer.fileEntryVar, Version, scripts.XCRandomizer.permalinkVar, scripts.XCRandomizer.seedEntryVar), lambda: Options.ObjectNameCleanup.ReassignAlphabeticalSort()]
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]

scripts.XCRandomizer.CreateMainWindow(root, "XC2", Version, "Xenoblade Chronicles 2 Randomizer", Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds)
