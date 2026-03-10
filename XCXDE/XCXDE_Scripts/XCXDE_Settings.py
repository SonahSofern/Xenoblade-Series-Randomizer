from XCXDE.XCXDE_Scripts import SeedNames, Options
import scripts.XCRandomizer, scripts.JSONParser
Version = "BETA"
Game = "XCXDE"
Title = "Xenoblade Chronicles X DE"
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

outputRomfsPath = "romfs/mod/bdat"

postCommands = [lambda: ShowTitleScreenText()]

seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

WindowData = scripts.XCRandomizer.GameWindowData(Game, Version, Title, seedEntryVar, permalinkVar, Options.Tabs, postCommands, [], mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, extraArgs=extraArgs, textFolderName=textFolderName, extraFiles=[Exefs, TitlescreenSplash], backgroundImages=backgrounds, outputRomfsSpec=outputRomfsPath)