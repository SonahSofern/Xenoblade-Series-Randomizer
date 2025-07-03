import scripts.XCRandomizer, scripts.JSONParser
from XC2.XC2_Scripts import SeedNames, Options

Game = "XC2"
Title = "Xenoblade Chronicles 2"
Version = "1.5.0"
backgrounds = ["titlescreen1.png"]
for i in range(1,11):
    backgrounds.append(f"ch{i}.png")
    
seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

TitlescreenSplash = scripts.XCRandomizer.FileReplacer(["Images/Logos/Aegis.wilay"],  "/menu/image", "mnu001_titlelogo_us.wilay", "XC2")

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], f"Randomizer v{Version}") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.Enhancements.AddCustomEnhancements(), lambda: Options.TornaMain.PassAlongSpoilerLogInfo(Version, permalinkVar, seedEntryVar), lambda: Options.ObjectNameCleanup.ReassignAlphabeticalSort()]
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]

def XC2Help():
    descData = scripts.XCRandomizer.PopupDescriptions.Description((900,900))
    descData.Header("Info")
    descData.Text(f"This is version {Version} of the randomizer project for Xenoblade Chronicles 2.\ncapable of randomizing: Enemies, Accessories, Blades, Drivers, Loot and much more!", anchor="w")
    descData.Text("This program is tested on the combined XC2 + DLC (Torna) 2.1.0 English Version of the game. It is recommended you also use that version of the game.\n\nPlease report bugs or suggestions to our discord (link on github) so we can make the randomizer better!", anchor="w")
    descData.Header("Setup")
    descData.Tag("Requirements")
    descData.Text("Homebrewed Switch or Emulator\nLegal Copy of Xenoblade Chronicles 2 with all DLC and update 2.1.0", anchor="w")
    descData.Tag("Step 1")
    descData.Text("Choose your output location for the program. This is where your game will load the randomized files from.", anchor="w")
    descData.Image("outputLocation.png", "XCDE", 800)
    descData.Text("Your path should look similar to this:\n\nYUZU: C:/Users/yourName/AppData/Roaming/yuzu/load/0100E95004039001/Randomizer\nRYUJINX: C:/Users/yourName/AppData/Roaming/Ryujinx/sdcard/atmosphere/contents/0100E95004039001\nCONSOLE: This PC/Nintendo Switch/SD Card/atmosphere/contents/0100E95004039001 (This is on your microsd card)", anchor="w")
    descData.Tag("Step 2")
    descData.Text("Choose your preferred settings, then click the randomize button.", anchor="w")
    descData.Text("If you want to know more about a setting you can click on its description (not all settings have descriptions).", anchor="w")
    # descData.Text("This will not affect your original game or save data. It can be toggled on or off by deleting/removing the randomized files in the output location.", anchor="w")
    descData.Tag("Step 3")
    descData.Text("Once the randomizer finishes, launch your game and you should see the version somewhere on the title screen.", anchor="w")
    descData.Text("If so, you're ready to start playing!", anchor="w")
    descData.Header("Common Issues")
    descData.Tag("Game Modes")
    descData.Text("Race Mode and Unique Monster Hunt do not work with all other settings, they will overwrite the incompatible choices.", anchor="w")
    descData.Tag("Mods")
    descData.Text("This mod is NOT compatible with other mods that edit the bdats. Ensure that this is the only active one for your game. (60fps and other visual mods should be okay)", anchor="w")
    return descData
