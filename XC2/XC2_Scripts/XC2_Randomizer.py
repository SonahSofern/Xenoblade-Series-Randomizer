import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
import scripts.XCRandomizer, scripts.JSONParser
from XC2.XC2_Scripts import SeedNames, Options
Version = "1.5.0"



backgrounds = ["titlescreen1.png"]

TitlescreenSplash = scripts.XCRandomizer.FileReplacer(["Images/Logos/Aegis.wilay"],  "/menu/image", "mnu001_titlelogo_us.wilay", "XC2")

for i in range(1,11):
    backgrounds.append(f"ch{i}.png")

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], f"Randomizer v{Version}") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.Enhancements.AddCustomEnhancements(), lambda: Options.ObjectNameCleanup.ReassignAlphabeticalSort()]
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]