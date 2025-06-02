import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
root = Tk()
import scripts.XCRandomizer, SeedNames, IDs, scripts.JSONParser, Options

Version = "1.1.0"

Tabs = {
    1: '🞛 Items',
    2: '🧍 Characters',
    3: '💀 Enemies',
    4: '🐇 Quality of Life',
    5: '♪ Music',
    6: '😄 Funny',
}
extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.EnemiesScript.OriginalEnemyData.clear()]

backgrounds = ["stars.png", "morning2.png", "stars3.png", "sunset2.png", "day.png"]
# Folder Names 
areaFiles = []
for id in IDs.areaFileListNumbers:
    areaFiles.append(f"bdat_ma{id}")
mainFolderNames = ["bdat_common", "bdat_menu_psv", "bdat_menu_ttrl", "bdat_evt", "bdat_menu_map", "bdat_menu_item"] + areaFiles
subFolderNames = ["bdat_common_ms", "bdat_menu_psv_ms", "bdat_menu_mes_ms"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["bdat_common_ms/MNU_title_ms.json"],[8], ["name"], f"Randomizer v{Version}", Game="XCDE") # Change Title Version to Randomizer vX.x.x




scripts.XCRandomizer.CreateMainWindow(root, "XCDE", Version, "Xenoblade Chronicles DE Randomizer", Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds)
