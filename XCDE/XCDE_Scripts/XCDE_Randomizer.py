import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
import scripts.XCRandomizer, scripts.JSONParser
from XCDE.XCDE_Scripts import SeedNames, IDs, Options
Version = "1.1.0"

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["bdat_common_ms/MNU_title_ms.json"],[8], ["name"], f"Randomizer v{Version}", Game="XCDE") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.EnemiesScript.OriginalEnemyData.clear()]

backgrounds = ["stars.png", "morning2.png", "stars3.png", "sunset2.png", "day.png"]
TitlescreenSplash = scripts.XCRandomizer.FileReplacer(["Images/Logos/conflict.wilay", "Images/Logos/monado.wilay", "Images/Logos/red.wilay", "Images/Logos/thedivine.wilay"],  "/menu/image", "mnu001_cont02_en.wilay", "XCDE")


# Folder Names 
areaFiles = []
for id in IDs.areaFileListNumbers:
    areaFiles.append(f"bdat_ma{id}")
    
mainFolderNames = ["bdat_common", "bdat_menu_psv", "bdat_menu_ttrl", "bdat_evt", "bdat_menu_map", "bdat_menu_item"] + areaFiles
subFolderNames = ["bdat_common_ms", "bdat_menu_psv_ms", "bdat_menu_mes_ms"]


