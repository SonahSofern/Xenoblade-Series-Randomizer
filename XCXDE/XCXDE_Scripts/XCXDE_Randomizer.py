import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
root = Tk()
import scripts.XCRandomizer, SeedNames, Options

Version = "BETA"

backgrounds = ["flower.jpg", "sunset.jpg", "purple.jpg"]


extraCommands = []
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]

scripts.XCRandomizer.CreateMainWindow(root, "XCXDE", Version, "Xenoblade Chronicles X DE Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds)
