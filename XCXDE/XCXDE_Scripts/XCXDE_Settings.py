from XCXDE.XCXDE_Scripts import SeedNames, Options
import scripts.XCRandomizer, scripts.JSONParser
Version = "1.1.0"
Game = "XCXDE"
Title = "Xenoblade Chronicles X DE"
outputPath = "contents/0100453019AA8000/romfs/mod/bdat"
backgrounds = ["flower.jpg", "sunset.jpg", "purple.jpg"]
postCommands = []
mainFolderNames = ["common"]
subFolderNames = ["common_ms"]
textFolderName = "us"

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["common_ms/menu_program_ms.json"],  [5237], ["name"], f"  Randomizer v{Version}", Game=Game) # Change Title Version to Randomizer vX.x.x

extraArgs = ["--hashes", scripts.XCRandomizer.Onefile.Directory("XCXDE/Loader/hashes.txt")] # Hash Table

TitlescreenSplash = scripts.XCRandomizer.FilePlacer(["Images/Logos/mainmen.wilay"],  "../ui/stream/us", "strm_title_thumb001.wilay", "XCXDE")
Exefs = scripts.XCRandomizer.FilePlacer(["Loader/exefs"], "../../../", game=Game)

postCommands = [lambda: ShowTitleScreenText()]

seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

def XCXDEHelp():
    descData = scripts.XCRandomizer.PopupDescriptions.Description((900,900))
    descData.Header("Info")
    descData.Text(f"This is version {Version} of the randomizer project for Xenoblade Chronicles X DE.\nCapable of randomizing: Enemies, Characters, Loot and much more!", anchor="w")
    descData.Text("Please report bugs or suggestions to our discord, so we can make the randomizer better!", anchor="w")
    descData.Header("Setup")
    descData.Tag("Requirements")
    descData.Text("Homebrewed Switch or Emulator\nLegal Copy of Xenoblade Chronicles X DE", anchor="w")
    descData.Tag("Step 1")
    descData.Text("Choose your output location for the program. This is where your game will load the randomized files from.", anchor="w")
    descData.Image("outputLocation.png", "XCDE", 800)
    descData.Text("Your output path should be the '"'atmosphere'"' folder of whatever platform you are playing on (emulators and console have this).\n\n e.g. C:/Users/your_name/AppData/Roaming/Ryujinx/sdcard/atmosphere", anchor="w")
    descData.Tag("Step 2")
    descData.Text("Choose your preferred settings, then click the randomize button.", anchor="w")
    descData.Text(f"If you want to know more about a setting you can click on its description marked by {Options.scripts.Interactables.DescriptionIndicator} (not all settings have descriptions).", anchor="w")
    descData.Tag("Step 3")
    descData.Text("Once the randomizer finishes, launch your game and you should see the version somewhere on the title screen.", anchor="w")
    descData.Text("If so, you're ready to start playing!", anchor="w")
    descData.Header("Common Issues")
    descData.Tag("Mods")
    descData.Text("This mod is NOT compatible with other mods that edit the bdats. Ensure that this is the only active one for your game. (60fps and other visual mods are okay)", anchor="w")
    return descData


WindowData = scripts.XCRandomizer.GameWindowData(Game, Version, Title, seedEntryVar, permalinkVar, Options.Tabs, postCommands, [], mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, extraArgs=extraArgs, textFolderName=textFolderName, extraFiles=[Exefs, TitlescreenSplash], backgroundImages=backgrounds, outputRomfsSpec=outputPath, setupHelpDesc=lambda: XCXDEHelp())