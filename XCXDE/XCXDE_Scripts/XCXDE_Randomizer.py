import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
from XCXDE.XCXDE_Scripts import SeedNames, Options
Version = "BETA"

backgrounds = ["flower.jpg", "sunset.jpg", "purple.jpg"]


extraCommands = []
mainFolderNames = ["common", "common_gmk"]
subFolderNames = ["common_ms"]

