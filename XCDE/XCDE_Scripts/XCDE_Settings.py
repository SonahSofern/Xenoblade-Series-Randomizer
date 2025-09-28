import scripts.XCRandomizer, scripts.JSONParser
from XCDE.XCDE_Scripts import SeedNames, IDs, Options

Title = "Xenoblade Chronicles DE"
Game = "XCDE"
Version = "1.1.1"
def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["bdat_common_ms/MNU_title_ms.json"],[8], ["name"], f"Randomizer v{Version}", Game="XCDE") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.EnemiesScript.OriginalEnemyData.clear()]

seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()


backgrounds = ["stars.png", "morning2.png", "stars3.png", "sunset2.png", "day.png"]
TitlescreenSplash = scripts.XCRandomizer.FilePlacer(["Images/Logos/conflict.wilay", "Images/Logos/monado.wilay", "Images/Logos/red.wilay", "Images/Logos/thedivine.wilay"],  "../menu/image", "mnu001_cont02_en.wilay", "XCDE")


# Folder Names 
areaFiles = []
for id in IDs.areaFileListNumbers:
    areaFiles.append(f"bdat_ma{id}")
    
mainFolderNames = ["bdat_common", "bdat_menu_psv", "bdat_menu_ttrl", "bdat_evt", "bdat_menu_map", "bdat_menu_item"] + areaFiles
subFolderNames = ["bdat_common_ms", "bdat_menu_psv_ms", "bdat_menu_mes_ms"]

def XCDEHelp():
    descData = scripts.XCRandomizer.PopupDescriptions.Description((900,900))
    descData.Header("Info")
    descData.Text(f"This is version {Version} of the randomizer project for Xenoblade Chronicles 1 DE.\nCapable of randomizing: Enemies, Armors, Music, Loot and much more!", anchor="w")
    descData.Text("This program is tested on the 1.1.2 English Version of the game. It is recommended you also use that version of the game.\n\nPlease report bugs or suggestions to our discord (link on github) so we can make the randomizer better!", anchor="w")
    descData.Header("Setup")
    descData.Tag("Requirements")
    descData.Text("Homebrewed Switch or Emulator\nLegal Copy of Xenoblade Chronicles DE with update 1.1.2", anchor="w")
    descData.Tag("Step 1")
    descData.Text("Choose your output location for the program. This is where your game will load the randomized files from.", anchor="w")
    descData.Image("outputLocation.png", Game, 800)
    descData.Text("Your path should look similar to this:\n\nYUZU: C:/Users/yourName/AppData/Roaming/yuzu/load/0100FF500E34A000/Randomizer\nRYUJINX: C:/Users/yourName/AppData/Roaming/Ryujinx/sdcard/atmosphere/contents/0100FF500E34A000\nCONSOLE: This PC/Nintendo Switch/SD Card/atmosphere/contents/0100FF500E34A000 (This is on your microsd card)", anchor="w")
    descData.Text("The 0100FF500E34A000 folder might not exist yet in that location, go ahead and create it if so.")
    descData.Tag("Step 2")
    descData.Text("Choose your preferred settings, then click the randomize button.", anchor="w")
    descData.Text("If you want to know more about a setting you can click on its description (not all settings have descriptions).", anchor="w")
    # descData.Text("This will not affect your original game or save data. It can be toggled on or off by deleting/removing the randomized files in the output location.", anchor="w")
    descData.Tag("Step 3")
    descData.Text("Once the randomizer finishes, launch your game and you should see the version somewhere on the title screen.", anchor="w")
    descData.Text("If so, you're ready to start playing!", anchor="w")
    descData.Header("Common Issues")
    descData.Tag("Future Connected")
    descData.Text("The story expansion Future Connected has not been tested at all, it may or may not work.", anchor="w")
    descData.Tag("Mods")
    descData.Text("This mod is NOT compatible with other mods that edit the bdats. Ensure that this is the only active one for your game. (60fps and other visual mods should be okay)", anchor="w")
    return descData

