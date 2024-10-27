import json
import os
from tkinter import filedialog
import tkinter as tk
import JSONParser
import Helper
import random
import time
DriverSkillTrees = Helper.inclRange(1,270)

""" def ArtsCancelBehavior():
    JSONParser.RandomizeBetweenRange("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], Helper.inclRange(0,50000),  [0], InvalidTargetIDs=Helper.inclRange(2,30))
    JSONParser.RandomizeBetweenRange("Randomizing Driver Skill Trees", ["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["NeedSp"], DriverSkillTrees,  [14], InvalidTargetIDs=Helper.inclRange(2,30)) """