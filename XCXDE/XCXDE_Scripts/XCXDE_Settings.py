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

outputRomfsPath = "romfs/mod/bdat"

Exefs = scripts.XCRandomizer.FilePlacer(["Loader/exefs"], "../../../", game=Game)

postCommands = [lambda: ShowTitleScreenText()]

seedEntryVar = scripts.XCRandomizer.StringVar()
permalinkVar = scripts.XCRandomizer.StringVar()

