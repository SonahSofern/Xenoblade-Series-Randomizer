import scripts.JSONParser, scripts.XCRandomizer
from XC3.XC3_Scripts import SeedNames, Options
Version = "1.0.0"
Game = "XC3"
Title = "Xenoblade Chronicles 3"

backgrounds = ["aetia.jpg", "desert.jpg", "makna.jpg", "ocean.jpg", "omnia.jpg", "uraya.jpg", "origin.jpg", "sand.jpg", "snow.jpg"]

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["menu/msg_mnu_title.json"],[11], ["name"], f"  Randomizer v{Version}", Game="XC3") # Change Title Version to Randomizer vX.x.x
seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

Exefs = scripts.XCRandomizer.FilePlacer(["Loader/exefs"], "../", game= "XC3")
Skyline = scripts.XCRandomizer.FilePlacer(["Loader/skyline"], "", game= "XC3")

hashFile = "XC3/Loader/xbc3Hashes.txt"
if scripts.XCRandomizer.isOneFile:
    extraArgs = ["--hashes", scripts.XCRandomizer.os.path.join(scripts.XCRandomizer.sys._MEIPASS, hashFile)]
else:  
    extraArgs= ["--hashes", hashFile]
    
extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.Enhancements.EnhancementsList.RefreshCurrentGroup()]
mainFolderNames = ["des", "btl", "evt", "fld", "map", "prg", "qst", "sys", "zzz", "mnu", "dlc"]
subFolderNames = ["autotalk", "battle", "field", "menu", "quest", "system"]
textFolderName= "gb/game"

def XC3Help():
    descData = scripts.XCRandomizer.PopupDescriptions.Description((900,900))
    descData.Header("Info")
    descData.Text(f"This is version {Version} of the randomizer project for Xenoblade Chronicles 3.\ncapable of randomizing: Enemies, Accessories, Characters, Classes, Loot and much more!", anchor="w")
    descData.Text("This program is designed for the 2.2.0 + All DLC English Version of the game. It is recommended you also use that version of the game.\n\nPlease report bugs or suggestions to our discord (link on github) so we can make the randomizer better!", anchor="w")
    descData.Header("Setup")
    descData.Tag("Requirements")
    descData.Text("Homebrewed Switch or Emulator\nLegal Copy of Xenoblade Chronicles 3 with all DLC and update 2.2.0", anchor="w")
    descData.Tag("Step 1")
    descData.Text("Choose your output location for the program. This is where your game will load the randomized files from.", anchor="w")
    descData.Image("outputLocation.png", "XCDE", 800)
    descData.Text("Your path should look similar to this:\n\nYUZU: C:/Users/yourName/AppData/Roaming/yuzu/sdmc/atmosphere/contents/010074F013262000\nRYUJINX: C:/Users/yourName/AppData/Roaming/Ryujinx/sdcard/atmosphere/contents/010074F013262000\nCONSOLE: This PC/Nintendo Switch/SD Card/atmosphere/contents/010074F013262000 (This is on your microsd card)", anchor="w")
    descData.Text("The 010074F013262000 folder might not exist yet in that location, go ahead and create it if so.")
    descData.Tag('Step 2')
    descData.Text("Choose your preferred settings, then click the randomize button.", anchor="w")
    descData.Text("If you want to know more about a setting you can click on its description (not all settings have descriptions).", anchor="w")
    # descData.Text("This will not affect your original game or save data. It can be toggled on or off by deleting/removing the randomized files in the output location.", anchor="w")
    descData.Tag("Step 3")
    descData.Text("Once the randomizer finishes, launch your game and you should see the version somewhere on the title screen.", anchor="w")
    descData.Text("If so, you're ready to start playing!", anchor="w")
    descData.Header("Common Issues")
    descData.Tag("Mods")
    descData.Text("This mod is NOT compatible with other mods that edit the bdats. Ensure that this is the only active one for your game. (60fps and other visual mods should be okay)", anchor="w")
    return descData
