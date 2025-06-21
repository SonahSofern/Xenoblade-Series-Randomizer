import scripts.XCRandomizer, scripts.JSONParser
from XC2.XC2_Scripts import SeedNames, Options

Version = "1.5.0"
backgrounds = ["titlescreen1.png"]
for i in range(1,11):
    backgrounds.append(f"ch{i}.png")
    
TitlescreenSplash = scripts.XCRandomizer.FileReplacer(["Images/Logos/Aegis.wilay"],  "/menu/image", "mnu001_titlelogo_us.wilay", "XC2")

def ShowTitleScreenText():
    scripts.JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], f"Randomizer v{Version}") # Change Title Version to Randomizer vX.x.x

extraCommands = [lambda: ShowTitleScreenText(), lambda: Options.Enhancements.AddCustomEnhancements(), lambda: Options.TornaMain.PassAlongSpoilerLogInfo(scripts.XCRandomizer.fileEntryVar, Version, scripts.XCRandomizer.permalinkVar, scripts.XCRandomizer.seedEntryVar), lambda: Options.ObjectNameCleanup.ReassignAlphabeticalSort()]
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]