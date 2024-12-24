from tkinter import PhotoImage, ttk
import random, subprocess, shutil, os, threading, traceback
from tkinter import *
import EnemyRandoLogic, SavedOptions, SeedNames, JSONParser, SkillTreeAdjustments, CoreCrystalAdjustments, RaceMode, TutorialShortening, IDs, MusicShuffling, DebugLog, PermalinkManagement
import GUISettings
from IDs import *
from Cosmetics import *
from UI_Colors import *
from tkinter.font import Font

Version = "0.1.0"
CommonBdatInput = ""
JsonOutput = "./_internal/JsonOutputs"
OptionDictionary = {}
rowIncrement = 0
MaxWidth = 1000
windowWidth = "1200"
windowHeight = "800"
OptionColorLight = White
OptionColorDark = Gray

root = Tk()
RootsForStyling.append(root)
defaultFont = Font(family=GUIDefaults[0], size=GUIDefaults[1])

root.title(f"Xenoblade Chronicles 2 Randomizer v{Version}")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')
icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

# The Notebook
MainWindow = ttk.Notebook(root, height=5)

# Frames in the notebook
TabGeneralOuter = ttk.Frame(MainWindow) 
TabDriversOuter = ttk.Frame(MainWindow) 
TabBladesOuter = ttk.Frame(MainWindow) 
TabEnemiesOuter = ttk.Frame(MainWindow) 
TabMiscOuter = ttk.Frame(MainWindow) 
TabQOLOuter = ttk.Frame(MainWindow)
TabCosmeticsOuter = ttk.Frame(MainWindow)
TabRaceModeOuter = ttk.Frame(MainWindow)
TabFunnyOuter = ttk.Frame(MainWindow)

# Canvas 
TabGeneralCanvas = Canvas(TabGeneralOuter) 
TabDriversCanvas = Canvas(TabDriversOuter) 
TabBladesCanvas = Canvas(TabBladesOuter)
TabEnemiesCanvas = Canvas(TabEnemiesOuter) 
TabMiscCanvas = Canvas(TabMiscOuter)
TabQOLCanvas = Canvas(TabQOLOuter)
TabCosmeticsCanvas = Canvas(TabCosmeticsOuter)
TabRaceModeCanvas = Canvas(TabRaceModeOuter)
TabFunnyCanvas = Canvas(TabFunnyOuter)

# Actual Scrollable Content
TabGeneral = ttk.Frame(TabGeneralCanvas) 
TabDrivers = ttk.Frame(TabDriversCanvas) 
TabBlades = ttk.Frame(TabBladesCanvas)
TabEnemies = ttk.Frame(TabEnemiesCanvas) 
TabMisc = ttk.Frame(TabMiscCanvas)
TabQOL = ttk.Frame(TabQOLCanvas)
TabCosmetics = ttk.Frame(TabCosmeticsCanvas)
TabRaceMode = ttk.Frame(TabRaceModeCanvas)
TabFunny = ttk.Frame(TabFunnyCanvas)


def CreateScrollBars(OuterFrames, Canvases, InnerFrames): # I never want to touch this code again lol what a nightmare
    for i in range(len(Canvases)):
        scrollbar = ttk.Scrollbar(OuterFrames[i], orient="vertical", command=Canvases[i].yview)
        Canvases[i].config(yscrollcommand=scrollbar.set, borderwidth=0, relief="flat", highlightthickness=0)
        CanvasesForStyling.append(Canvases[i])
        # OuterFrames[i].config(borderwidth=0, relief="flat")
        InnerFrames[i].bind("<Configure>", lambda e, canvas=Canvases[i]: canvas.configure(scrollregion=canvas.bbox("all")))

        OuterFrames[i].pack_propagate(False)
        Canvases[i].create_window((0, 0), window=InnerFrames[i], anchor="nw")
        Canvases[i].pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event, canvas=Canvases[i]):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        Canvases[i].bind("<Enter>", lambda e, canvas=Canvases[i]: canvas.bind_all("<MouseWheel>", lambda event: _on_mousewheel(event, canvas)))
        Canvases[i].bind("<Leave>", lambda e, canvas=Canvases[i]: canvas.unbind_all("<MouseWheel>"))
        OuterFrames[i].pack(expand=True, fill="both")

CreateScrollBars([TabGeneralOuter, TabDriversOuter, TabBladesOuter, TabEnemiesOuter, TabMiscOuter, TabQOLOuter, TabCosmeticsOuter, TabRaceModeOuter, TabFunnyOuter],[TabGeneralCanvas, TabDriversCanvas, TabBladesCanvas, TabEnemiesCanvas, TabMiscCanvas, TabQOLCanvas, TabCosmeticsCanvas, TabRaceModeCanvas, TabFunnyCanvas],[TabGeneral, TabDrivers, TabBlades, TabEnemies, TabMisc, TabQOL, TabCosmetics, TabRaceMode, TabFunny])

# Tabs
MainWindow.add(TabGeneralOuter, text ='General') 
MainWindow.add(TabDriversOuter, text ='Drivers') 
MainWindow.add(TabBladesOuter, text ='Blades') 
MainWindow.add(TabEnemiesOuter, text ='Enemies') 
MainWindow.add(TabCosmeticsOuter, text='Cosmetics')
MainWindow.add(TabQOLOuter, text = 'Quality of Life')
MainWindow.add(TabRaceModeOuter, text='Race Mode')
MainWindow.add(TabFunnyOuter, text='Funny')
MainWindow.add(TabMiscOuter, text ='Misc.') 
MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 

def ShowTitleScreenText():
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], [f"Randomizer v{Version}"]) # Change Title Version to Randomizer v0.1.0

def GenHeader(headerName, parentTab, backgroundColor):
    global rowIncrement
    
    Header = ttk.Label(parentTab, text=headerName, padx=10, pady=10, background=backgroundColor, font=(defaultFont), width=MaxWidth, anchor="w")
    Header.grid(row=rowIncrement, column=0, sticky="w")

    rowIncrement += 1


stateSetList = []    

def StateUpdate(button, textList):
    if button.get():
        for item in textList:
            item.state(["!disabled"])       
    else:
        for item in textList:
            item.state(["disabled"])


def InteractableStateSet():
    for item in stateSetList:
        item()
        
        
def GenStandardOption(optionName, parentTab, description, commandList = [], subOptionName_subCommandList = [], optionType = Checkbutton):   
    # Variables
    global OptionDictionary
    global rowIncrement
    spinBoxVar = IntVar(value=100)
    var = BooleanVar()
    spinDesc = ttk.Label()
    spinBoxObj = ttk.Spinbox()
    StateSet = lambda: StateUpdate(checkButtonVar, [optionDesc, spinDesc, spinBoxObj] + checkBoxList)

    # Parent Frame
    optionPanel = ttk.Frame(parentTab)
    optionPanel.grid(row = rowIncrement, column= 0, sticky="ew")
    
    # Major Option Checkbox

    checkButtonObj = ttk.Checkbutton(optionPanel, variable= var, text=optionName, width=40, style="midColor.TCheckbutton",command= StateSet)
    checkButtonObj.grid(row=rowIncrement, column=0, sticky="e")
    checkButtonVar = var
    
    # Description Label
    optionDesc = ttk.Label(optionPanel, text=description, anchor="w", width=55, wraplength=500)
    optionDesc.grid(row=rowIncrement, column=1, sticky="w", padx=0)
    
    # % Boxes
    if (optionType == Spinbox):
        spinBoxObj = ttk.Spinbox(optionPanel, from_=0, to=100, textvariable=spinBoxVar, wrap=True, width=3, increment=10)
        spinBoxObj.delete(0, END)
        spinBoxObj.insert(0,"0")
        spinBoxObj.grid(row=rowIncrement, column=2, padx=(15,0))
        spinDesc = ttk.Label(optionPanel, text="% randomized", anchor="w")
        spinDesc.grid(row=rowIncrement, column=3, sticky="w", padx=0)


    # Create Main Option Dictionary Entry
    OptionDictionary[optionName]={
        "name": optionName,
        "optionTypeVal": checkButtonVar,
        "spinBoxVal": spinBoxVar,
        "commandList": commandList,
        "subOptionObjects": {},
    }
    checkBoxList = []
    # Create Suboptions Dictionary Entry
    for i in range((len(subOptionName_subCommandList))//2):
        var = BooleanVar()
        checkBox = ttk.Checkbutton(optionPanel, text=subOptionName_subCommandList[2*i], variable=var, width=35)
        checkBox.grid(row=rowIncrement+i+1, column=0, sticky="sw")
        checkBoxList.append(checkBox)
        OptionDictionary[optionName]["subOptionObjects"][subOptionName_subCommandList[2*i]] = {
        "subName": subOptionName_subCommandList[2*i],
        "subOptionTypeVal": var,
        "subCommandList": subOptionName_subCommandList[2*i+1],
        }
    rowIncrement += 1
    # Variable to help set initial states of interactables
    stateSetList.append(StateSet)
    
def Options():
    # DebugLog.CreateDebugLog(OptionDictionary, Version, randoSeedEntry.get())
    # General
    GenStandardOption("Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(PouchItems)-set([40007])), PouchItems)])
    GenStandardOption("Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(Accessories)-set([1])), Accessories + Helper.InclRange(448,455))])
    GenStandardOption("Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Weapon Chip Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)])
    GenStandardOption("Treasure Chests Contents", TabGeneral, "Randomizes the contents of Treasure Chests", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID","itm5ID","itm6ID","itm7ID","itm8ID"], Accessories + WeaponChips + AuxCores + CoreCrystals,[])], ["Accessories", [lambda: IDs.ValidReplacements.extend(Accessories)] ,"Weapon Chips", [lambda: IDs.ValidReplacements.extend(WeaponChips)], "Aux Cores", [lambda: IDs.ValidReplacements.extend(AuxCores)], "Core Crystals", [lambda: IDs.ValidReplacements.extend(CoreCrystals)], "Deeds", [lambda: IDs.ValidReplacements.extend(Deeds)], "Collection Point Materials", [lambda: IDs.ValidReplacements.extend(CollectionPointMaterials)]])
    GenStandardOption("Collection Points", TabGeneral, "Randomizes the contents of Collection Points", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_CollectionPopList.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID"], list(set(CollectionPointMaterials) - set([30019])), [])], ["Accessories", [lambda: IDs.ValidReplacements.extend(Accessories)] ,"Weapon Chips", [lambda: IDs.ValidReplacements.extend(WeaponChips)], "Aux Cores", [lambda: IDs.ValidReplacements.extend(AuxCores)], "Core Crystals", [lambda: IDs.ValidReplacements.extend(CoreCrystals)], "Deeds", [lambda: IDs.ValidReplacements.extend(Deeds)], "Collection Point Materials", [lambda: IDs.ValidReplacements.extend(CollectionPointMaterials)]])

    # Drivers
    GenStandardOption("Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, [], InvalidTargetIDs=AutoAttacks)],["Debuffs", [lambda: IDs.ValidReplacements.extend(list(set(ArtDebuffs)-set([21])))],"Buffs",[lambda: IDs.ValidReplacements.extend(ArtBuffs)], "Doom", [lambda: IDs.ValidReplacements.extend([21])]], Spinbox)
    # GenOption("Driver Art Distances", TabDrivers, "Randomizes how far away you can cast an art", ["common/BTL_Arts_Dr.json"], ["Distance"], Helper.inclRange(0, 20), Helper.inclRange(1,20)) Nothing wrong with this just kinda niche/silly
    # GenStandardOption("Driver Skill Trees", TabDrivers, "Randomizes all driver's skill trees", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], DriverSkillTrees, DriverSkillTrees)]) Commenting out for first release dont want to bother making mutually exclusive widgets
    GenStandardOption("Balanced Skill Trees", TabDrivers, "Balances and randomizes the driver skill trees", [lambda: SkillTreeAdjustments.BalancingSkillTreeRando(OptionDictionary)])
    GenStandardOption("Driver Art Reactions", TabDrivers, "Randomizes each hit of an art to have a reaction", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactionDistribution, InvalidTargetIDs=AutoAttacks)],["Clear Default Reactions", [Helper.ColumnAdjust("./_internal/JsonOutputs/common/BTL_Arts_Dr.json", [Helper.StartsWith("ReAct", 1,16)], 0)]], optionType=Spinbox) # we want id numbers no edit the 1/6 react stuff
    GenStandardOption("Driver Art Animation Speeds", TabDrivers, "Randomizes a Driver's art animation speeds", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], ["ActSpeed"], Helper.InclRange(0,255), Helper.InclRange(50,255), InvalidTargetIDs=AutoAttacks)], optionType=Spinbox)
    # GenStandardOption("Driver Starting Accessory", TabDrivers, "Randomizes what accessory your drivers begin the game with", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Dr.json"], ["DefAcce"], Accessories + [0], Accessories + [0])], ["Remove All Starting Accessories", [lambda: IDs.InvalidReplacements.extend(Accessories)]])
    
    # Blades
    GenStandardOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], Helper.StartsWith("ReAct", 1, 16), HitReactions, HitReactions)], optionType=Spinbox)
    # GenStandardOption("Blade Special Damage Types", TabBlades, "Randomizes whether a Blade's special deals Physical Damage or Ether Damage", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], ["ArtsType"], [1, 2], [1,2])])
    GenStandardOption("Blade Special Buttons", TabBlades, "Randomizes what button a special uses for its button challenge", [lambda: JSONParser.ChangeJSONFile(["common/MNU_BtnChallenge2.json"], Helper.StartsWith("BtnType", 1, 3), ButtonCombos, ButtonCombos)])
    GenStandardOption("Blade Elements", TabBlades, "Randomizes a Blade's element", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))],optionType=Spinbox)
    GenStandardOption("Blade Battle Skills", TabBlades, "Randomizes a Blade's battle (yellow) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BSkill", 1, 3), list(set(BladeBattleSkills) - set([268])), list(set(BladeBattleSkills) - set([268])) )])
    GenStandardOption("Blade Field Skills", TabBlades, "Randomizes a Blade's field (green) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("FSkill", 1, 3), BladeFieldSkills, BladeFieldSkills, InvalidTargetIDs=[1135])])
    # GenOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials, BladeSpecials)]) Commenting out for initial launch I think this setting will put people off it sounds fun but animations no longer connect well on specials
    GenStandardOption("Blade Cooldowns", TabBlades, "Randomizes a Blade's swap cooldown", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
    GenStandardOption("Blade Arts", TabBlades, "Randomizes a Blade's arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), ArtBuffs, ArtBuffs)])
    GenStandardOption("Blade Aux Core Slots", TabBlades, "Randomizes a Blade's maximum Aux Core Slots", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), IDs.BladeAuxCoreSlotDistribution)])
    GenStandardOption("Blade Names", TabBlades, "Randomizes a Blade's name", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
    GenStandardOption("Blade Defenses", TabBlades, "Randomizes a Blade's Physical and Ether Defense", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)],optionType=Spinbox)
    GenStandardOption("Blade Mods", TabBlades, "Randomizes a Blade's Stat Modifiers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(1,100), BladeModDistribution)])
    
    # Enemies
    GenStandardOption("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [lambda: EnemyRandoLogic.EnemyLogic(OptionDictionary)],["Story Bosses", [], "Quest Enemies", [], "Unique Monsters", [], "Superbosses", [], "Normal Enemies", [], "Mix Enemies Between Types", [], "Keep All Enemy Levels", [], "Keep Story Boss Levels", [], "Keep Quest Enemy Levels", []])
    GenStandardOption("Enemy Drops", TabEnemies, "Randomizes enemy drops", [lambda: JSONParser.ChangeJSONFile(["common/BTL_EnDropItem.json"], Helper.StartsWith("ItemID", 1, 8), AuxCores + Accessories + WeaponChips, [])], ["Accessories", [lambda: IDs.ValidReplacements.extend(Accessories)] ,"Weapon Chips", [lambda: IDs.ValidReplacements.extend(WeaponChips)], "Aux Cores", [lambda: IDs.ValidReplacements.extend(AuxCores)], "Core Crystals", [lambda: IDs.ValidReplacements.extend(CoreCrystals)], "Deeds", [lambda: IDs.ValidReplacements.extend(Deeds)], "Collection Point Materials", [lambda: IDs.ValidReplacements.extend(CollectionPointMaterials)]], optionType=Spinbox)
    GenStandardOption("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))],optionType=Spinbox)
    #GenOption("Enemy Level Ranges", TabEnemies, "Randomizes enemy level ranges", Helper.InsertHelper(2, 1,90,"maa_FLD_EnemyPop.json", "common_gmk/"), ["ene1Lv", "ene2Lv", "ene3Lv", "ene4Lv"], Helper.inclRange(-100,100), Helper.inclRange(-30,30)) Defunct with alex's enemy rando
    
    # Misc
    GenStandardOption("Music", TabMisc, "Randomizes Music", [lambda: MusicShuffling.MusicShuffle(OptionDictionary)], ["Seperate Battle and \nEnvironment Themes", []]) # need to change title screen music
    # GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
    # GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
    # GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
    #GenStandardOption("Beta Stuff", TabMisc, "Stuff still in testing", [lambda: TestingStuff.Beta(OptionDictionary)])

    # QOL
    # GenStandardOption("Deed Max Values", TabQOL, "Increases the maximum value of deed effects")
    GenStandardOption("Shortened Tutorial", TabQOL, "Shortens/removes tutorials", [lambda: TutorialShortening.ShortenedTutorial(OptionDictionary)])
    # GenStandardOption("Fast Skill Trees", TabQOL, "Makes Blade Skill Trees easy to complete", [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()])
    # GenStandardOption("Guaranteed Rare Blades", TabQOL, "Puts Rare Blades in chests instead of the Gacha system", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()])
    GenStandardOption("Early Arts Cancel", TabQOL, "Puts Arts Cancel skills into the first Driver Skill Tree slot", [lambda: SkillTreeAdjustments.Tier1ArtsCancel(OptionDictionary)])
    GenStandardOption("Treasure Chest Visibility", TabQOL, "Increases the range you can see treasure chests from", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
    GenStandardOption("Freely Engage Blades", TabQOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])
    GenStandardOption("Easy Field Skill Trees", TabQOL, "Maxes out all Blade field skills",  [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()])

    # Funny
    GenStandardOption("Projectile Treasure Chests", TabFunny, "Launches your items from chests", [lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [12])])
    GenStandardOption("Blade Size", TabFunny, "Randomizes the size of Blades", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Scale", "WpnScale"], [], Helper.InclRange(1,250) + [1000,16000])], optionType= Spinbox) # Make sure these work for common blades
    GenStandardOption("NPCs Size", TabFunny, "Randomizes the size of NPCs", [lambda: JSONParser.ChangeJSONFile(["common/RSC_NpcList.json"], ["Scale"], Helper.InclRange(1,100), Helper.InclRange(1,250))], optionType=Spinbox)
    GenStandardOption("Enemy Size", TabFunny, "Randomizes the size of enemies", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnArrange.json"], ["Scale"], Helper.InclRange(0, 1000), Helper.InclRange(1, 200) + Helper.InclRange(990,1000))], optionType=Spinbox)

    # Cosmetics
    GenStandardOption("Cosmetics", TabCosmetics, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics(OptionDictionary)], RexCosmetics + NiaDriverCosmetics + ToraCosmetics + MoragCosmetics + ZekeCosmetics + PyraCosmetics + MythraCosmetics + DromarchCosmetics + BrighidCosmetics + PandoriaCosmetics + NiaBladeCosmetics + PoppiαCosmetics + PoppiQTCosmetics + PoppiQTπCosmetics, Spinbox)
    
    # Race Mode
    GenStandardOption("Race Mode", TabRaceMode, "Enables Race Mode", [lambda: RaceMode.RaceModeChanging(OptionDictionary)], ["Xohar Fragment Hunt", [], "Less Grinding", [], "Shop Changes", [], "Enemy Drop Changes", [], "DLC Item Removal", [], "Custom Loot", [], "Guaranteed Rare Blades", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()]])

    # # In-Game Settings
    # GenHeader("Camera Settings",TabSettings, None)
    # GenStandardOption("Invert up/down", TabSettings, "Toggle inversion of up/down for camera controls", [],[])
    # GenStandardOption("Invert left/right", TabSettings, "Toggle inversion of left/right for camera controls", [],[])
    # GenStandardOption("Auto camera response speed", TabSettings, "Adjust the response times for the automatically controlled camera", [],[],Spinbox)
    # GenStandardOption("Camera reset response speed", TabSettings, "Adjust the length of time it takes to reset the camera's position", [],[],Spinbox)
    # GenStandardOption("Turn speed", TabSettings, "Adjust the turning speed of the manual camera", [],[],Spinbox)
    # GenStandardOption("Zoom speed", TabSettings, "Adjust the speed of the camera's zoom", [],[],Spinbox)
    # GenStandardOption("Gradient Correction", TabSettings, "Adjust the automatic behavior of the camera when traversing gradients", [],[])
    # GenHeader("Sound Settings",TabSettings, None)    
    # GenStandardOption("Subtitles", TabSettings, "Toggle subtitles on or off", [],[])
    # GenStandardOption("Cutscene voice volume", TabSettings, "Adjust voice volume during cutscenes", [],[], Spinbox)
    # GenStandardOption("Game BGM volume", TabSettings, "Adjust background music volume during the game", [],[], Spinbox)
    # GenStandardOption("Game SE volume", TabSettings, "Adjust volume of sound effects heard during the game", [],[], Spinbox)
    # GenStandardOption("Game voice volume", TabSettings, "Adjust volume of voices heard during the game", [],[], Spinbox)
    # GenStandardOption("Battle Narrator volume", TabSettings, "Adjust volume of the battle Narrator (not character battle voices)", [],[], Spinbox)
    # GenStandardOption("Environment volume", TabSettings, "Adjust volume of environmental sounds (such as rain) heard during the game", [],[], Spinbox)
    # GenStandardOption("System volume", TabSettings, "Adjust volume of system sounds heard during the game", [],[], Spinbox)
    # GenHeader("Screen Settings",TabSettings, None)        
    # GenStandardOption("Screen brightness", TabSettings, "Adjust screen brightness", [],[], Spinbox)
    # GenHeader("Game Settings",TabSettings, None)
    # GenStandardOption("Difficulty level", TabSettings, "Default Difficulty", [],["Easy",[],"Normal",[],"Bringer of Chaos",[], "Custom",[]])
    # GenStandardOption("Auto-battle", TabSettings, "Toggle auto-battle", [],[])
    # GenStandardOption("Automate Special Button Challenges", TabSettings, "Toggle automatic success for button challenge inputs during Specials", [],[])
    # GenStandardOption("Enemy Aggression", TabSettings, "Toggle whether foes pick a fight (exc.salvage, unique, boss, and quest foes)", [],[])
    # GenStandardOption("Special BGM", TabSettings, "When enabled, special battle music will play with certain Blades in the party", [],[])

def Randomize():
    def ThreadedRandomize():
        # Variables
        global OptionDictionary
        
        # Disable Repeated Button Click
        RandomizeButton.config(state=DISABLED)

        # Showing Progress Diplay 
        randoProgressDisplay.pack(side='left', anchor='w', pady=10, padx=10)
        randoProgressDisplay.config(text="Unpacking BDATs")

        random.seed(CompressedPermalink)
        print("Seed: " + randoSeedEntry.get())
        print("Permalink: "+  CompressedPermalink)

        # Unpacks BDATs
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common_gmk.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/gb/common_ms.bdat -o {JsonOutput} -f json --pretty")

        # Runs all randomization
        RunOptions()
        randoProgressDisplay.config(text="Packing BDATs")

        # Packs BDATs
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

        # Outputs common_ms in the correct file structure
        os.makedirs(f"{outDirEntry.get()}/gb", exist_ok=True)
        shutil.move(f"{outDirEntry.get()}/common_ms.bdat", f"{outDirEntry.get()}/gb/common_ms.bdat")

        # Displays Done and Clears Text
        import time
        randoProgressDisplay.config(text="Done")
        time.sleep(0.5)
        randoProgressDisplay.config(text="")
        randoProgressDisplay.pack_forget()

        # ReEnables Randomize Button
        RandomizeButton.config(state=NORMAL)
        
        print("Done")

    threading.Thread(target=ThreadedRandomize).start()

def RunOptions():
    for option in OptionDictionary.values():
        if (option["optionTypeVal"].get()): # checks main option input
            IDs.CurrentSliderOdds = option["spinBoxVal"].get()
            for subOption in option["subOptionObjects"].values():
                if (subOption["subOptionTypeVal"].get()): # checks subOption input
                    for subCommand in subOption["subCommandList"]:
                        try:
                            subCommand()
                        except Exception as error:
                            print(f"ERROR: {command['name']}: {subCommand['subName']} | {error}")
                            print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text=f"Randomizing {option['name']}")
            for command in option["commandList"]:
                try:
                    command()
                except Exception as error:
                    print(f"ERROR: {option['name']} | {error}")
                    print(f"{traceback.format_exc()}") # shows the full error
    
    # Nonstandard Options
    ShowTitleScreenText()
    RaceMode.SeedHash()
 
def GenRandomSeed():
    randoSeedEntry.delete(0, END)
    randoSeedEntry.insert(0,SeedNames.RandomSeedName())

Options()

bdatcommonFrame = ttk.Frame(root)
bdatcommonFrame.pack(anchor="w", padx=10)
bdatButton = ttk.Button(bdatcommonFrame, width=20, text="Choose Input Folder", command= lambda: Helper.DirectoryChoice("Choose your folder containing common.bdat, common_ms.bdat and common_gmk.bdat", bdatFilePathEntry))
bdatButton.pack(side="left", padx=2, pady=2)
bdatFilePathEntry = ttk.Entry(bdatcommonFrame, width=MaxWidth)
bdatFilePathEntry.pack(side="left", padx=2)
OutputDirectoryFrame = ttk.Frame(root)
OutputDirectoryFrame.pack(anchor="w", padx=10)
outputDirButton = ttk.Button(OutputDirectoryFrame, width = 20, text='Choose Output Folder', command= lambda: Helper.DirectoryChoice("Choose an output folder", outDirEntry))
outputDirButton.pack(side="left", padx=2, pady=2)
outDirEntry = ttk.Entry(OutputDirectoryFrame, width=MaxWidth)
outDirEntry.pack(side="left", padx=2)
SeedFrame = ttk.Frame(root)
SeedFrame.pack(anchor="w", padx=10)
seedDesc = ttk.Button(SeedFrame, text="Seed", command=GenRandomSeed)
seedDesc.pack(side='left', padx=2, pady=2)

# Seed entry box
randoSeedEntry = ttk.Entry(SeedFrame, width=30)
randoSeedEntry.pack(side='left', padx=2)





# Save and Load Last Options
EveryObjectToSaveAndLoad = ([bdatFilePathEntry, outDirEntry, randoSeedEntry] + [option["optionTypeVal"] for option in OptionDictionary.values()] + [subOption["subOptionTypeVal"] for option in OptionDictionary.values() for subOption in option["subOptionObjects"].values()] + [option["spinBoxVal"] for option in OptionDictionary.values()])
SavedOptions.loadData(EveryObjectToSaveAndLoad, "SavedOptions.txt")
InteractableStateSet()


# Permalink Options/Variables
permalinkVar = StringVar()
CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
# SeedName, SettingsValues = PermalinkManagement.GenerateSettingsFromPermalink(CompressedPermalink, EveryObjectToSaveAndLoad)
permalinkFrame = ttk.Frame(root)
permalinkEntry = ttk.Entry(permalinkFrame, width=MaxWidth, textvariable=permalinkVar)
permalinkButton = ttk.Button(permalinkFrame, text="Copy Permalink")
permalinkFrame.pack(padx=10, pady=(0,30), anchor="w")
permalinkButton.pack(side="left", padx=2)
permalinkEntry.pack(side='left', padx=2)

def LoadByPermalink(objects, permaLinkObjects):
    
    pass
# permalinkVar.trace_add("write", LoadByPermalink(EveryObjectToSaveAndLoad, PermalinkManagement.GenerateSettingsFromPermalink()))


# Bottom Left Progress Display Text
randoProgressDisplay = ttk.Label(text="", anchor="e", padding=2, style="BorderlessLabel.TLabel")

# Randomize Button
RandomizeButton = ttk.Button(text='Randomize', command=Randomize)
RandomizeButton.place(relx=0.5, rely=1, y= -10, anchor="s")
RandomizeButton.config(padding=5)

# Options Cog
Cog = PhotoImage(file="./_internal/Images/SmallSettingsCog.png")
SettingsButton = ttk.Button(image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont))
SettingsButton.pack(pady=10, padx=10, side='right', anchor='e') 



root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EveryObjectToSaveAndLoad, "SavedOptions.txt"), root.destroy()))
GUISettings.LoadTheme(defaultFont, GUIDefaults[2])
root.mainloop()

