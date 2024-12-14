from tkinter import PhotoImage, ttk
import random, subprocess, shutil, os, threading
from tkinter import *
import EnemyRandoLogic, SavedOptions, SeedNames, JSONParser, SkillTreeAdjustments, CoreCrystalAdjustments, RaceMode, TutorialShortening, IDs, MusicShuffling
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


OptionColorLight = White
OptionColorDark = Gray

root = Tk()
fontNameSizeDefault = ["", 12]
SavedOptions.loadData(fontNameSizeDefault, "GUISavedOptions.txt")
defaultFont = Font(family=fontNameSizeDefault[0], size=fontNameSizeDefault[1])

root.title(f"Xenoblade Chronicles 2 Randomizer v{Version}")
root.option_add("*Font", defaultFont)
root.configure(background=Red)
root.geometry('1000x900')
icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

# The Notebook
MainWindow = ttk.Notebook(root, height=5)

# Frames in the notebook
TabGeneralOuter = Frame(MainWindow) 
TabDriversOuter = Frame(MainWindow) 
TabBladesOuter = Frame(MainWindow) 
TabEnemiesOuter = Frame(MainWindow) 
TabMiscOuter = Frame(MainWindow) 
TabQOLOuter = Frame(MainWindow)
TabCosmeticsOuter = Frame(MainWindow)
TabRaceModeOuter = Frame(MainWindow)
TabFunnyOuter = Frame(MainWindow)

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
TabGeneral = Frame(TabGeneralCanvas) 
TabDrivers = Frame(TabDriversCanvas) 
TabBlades = Frame(TabBladesCanvas)
TabEnemies = Frame(TabEnemiesCanvas) 
TabMisc = Frame(TabMiscCanvas)
TabQOL = Frame(TabQOLCanvas)
TabCosmetics = Frame(TabCosmeticsCanvas)
TabRaceMode = Frame(TabRaceModeCanvas)
TabFunny = Frame(TabFunnyCanvas)


def CreateScrollBars(OuterFrames, Canvases, InnerFrames): # I never want to touch this code again lol what a nightmare
    for i in range(len(Canvases)):
        scrollbar = ttk.Scrollbar(OuterFrames[i], orient="vertical", command=Canvases[i].yview)
        Canvases[i].config(yscrollcommand=scrollbar.set, highlightthickness=0)
        OuterFrames[i].config(highlightthickness=0)
        InnerFrames[i].config(highlightthickness=0)
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
MainWindow.add(TabMiscOuter, text ='Misc.') 
MainWindow.add(TabQOLOuter, text = 'Quality of Life')
MainWindow.add(TabCosmeticsOuter, text='Cosmetics')
MainWindow.add(TabRaceModeOuter, text='Race Mode')
MainWindow.add(TabFunnyOuter, text='Funny')
MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 

def ShowTitleScreenText():
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], [f"Randomizer v{Version}"]) # Change Title Version to Randomizer v0.1.0

def GenHeader(headerName, parentTab, backgroundColor):
    global rowIncrement
    
    Header = Label(parentTab, text=headerName, padx=10, pady=10, background=backgroundColor, font=(defaultFont), width=MaxWidth, anchor="w")
    Header.grid(row=rowIncrement, column=0, sticky="w")

    rowIncrement += 1

def GenStandardOption(optionName, parentTab, description, commandList = [], subOptionName_subCommandList = [], optionType = Checkbutton, optionColor = ""):   
    global OptionDictionary
    global rowIncrement
    # Create Option Color
    if (optionColor == ""):
        if (rowIncrement %2 == 0):
            optionColor = OptionColorLight
        else:
            optionColor = OptionColorDark

    optionPanel = Frame(parentTab, padx=10, pady=10, background=optionColor)
    optionPanel.grid(row = rowIncrement, column= 0, sticky="ew")

    # Create Option Name
    option = Label(optionPanel, text=optionName, background=optionColor, width=30, anchor="w", wraplength=350)
    option.grid(row=rowIncrement, column=0, sticky="sw")

    # Create Option Interactable
    if (optionType == Checkbutton):
        var = BooleanVar()
        optionTypeObj = Checkbutton(optionPanel, background=optionColor, highlightthickness=0, variable= var, text=description)
        optionTypeObj.grid(row=rowIncrement, column=1, sticky="e")
        optionType = var
    elif (optionType == Scale):
        var = IntVar()
        optionTypeObj = Scale(optionPanel, from_=0, to=100, orient= HORIZONTAL, sliderlength=10, variable=var, background=optionColor, highlightthickness=0)
        optionDesc = Label(optionPanel, text=description, background=optionColor, anchor='w')
        optionTypeObj.grid(row=rowIncrement, column=1, sticky="e")
        optionDesc.grid(row=rowIncrement, column=2, sticky="sw")
        optionType = var
    # elif (optionType == Entry):
    #     optionTypeMin = Entry(optionPanel, background=OptionColor, highlightthickness=0, width=5)
    #     optionTypeMax = Entry(optionPanel, background=OptionColor, highlightthickness=0, width=5)
    #     optionDesc = Label(optionPanel, text="| Range", background=OptionColor, anchor='w')
    #     optionDesc.grid(row=rowIncrement, column=4)
    #     optionTypeMin.grid(row=rowIncrement, column=5)
    #     optionTypeMax.grid(row=rowIncrement, column=6, padx=5)
    #     optionType = [optionTypeMin, optionTypeMax]

    # I hate this but the parent wont fill "sticky="ew" doesnt work. Its probably due to so many nested parents but I dont wanna go fix all of them
    spaceFill = Label(optionPanel, text="", background=optionColor, width=MaxWidth, anchor='w')
    spaceFill.grid(row=rowIncrement, column=100, sticky="sw")

    # Create Main Option Dictionary Entry
    OptionDictionary[optionName]={
        "name": optionName,
        "optionTypeVal": optionType,
        "commandList": commandList,
        "subOptionObjects": {},
    }    
    # Create Suboptions Dictionary Entry
    for i in range((len(subOptionName_subCommandList))//2):
        var = BooleanVar()
        checkBox = Checkbutton(optionPanel, background=optionColor, text=subOptionName_subCommandList[2*i], variable=var, highlightthickness=0)
        checkBox.grid(row=rowIncrement+i+1, column=0, sticky="sw")

        OptionDictionary[optionName]["subOptionObjects"][subOptionName_subCommandList[2*i]] = {
        "subName": subOptionName_subCommandList[2*i],
        "subOptionTypeVal": var,
        "subCommandList": subOptionName_subCommandList[2*i+1],
        }

    rowIncrement += 1
    
def Options():
    # General
    GenStandardOption("Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(PouchItems)-set([40007])), PouchItems)])
    GenStandardOption("Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(Accessories)-set([1])), Accessories + Helper.InclRange(448,455))])
    GenStandardOption("Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Weapon Chip Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)])
    GenStandardOption("Treasure Chests Contents", TabGeneral, "Randomizes the contents of Treasure Chests", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID","itm5ID","itm6ID","itm7ID","itm8ID"], Accessories + WeaponChips + AuxCores + CoreCrystals,[])], ["Accessories", [lambda: IDs.ValidReplacements.extend(Accessories)] ,"Weapon Chips", [lambda: IDs.ValidReplacements.extend(WeaponChips)], "Aux Cores", [lambda: IDs.ValidReplacements.extend(AuxCores)], "Core Crystals", [lambda: IDs.ValidReplacements.extend(CoreCrystals)], "Deeds", [lambda: IDs.ValidReplacements.extend(Deeds)], "Collection Point Materials", [lambda: IDs.ValidReplacements.extend(CollectionPointMaterials)]])
    GenStandardOption("Collection Points", TabGeneral, "Randomizes the contents of Collection Points", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_CollectionPopList.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID"], list(set(CollectionPointMaterials) - set([30019])), [])], ["Accessories", [lambda: IDs.ValidReplacements.extend(Accessories)] ,"Weapon Chips", [lambda: IDs.ValidReplacements.extend(WeaponChips)], "Aux Cores", [lambda: IDs.ValidReplacements.extend(AuxCores)], "Core Crystals", [lambda: IDs.ValidReplacements.extend(CoreCrystals)], "Deeds", [lambda: IDs.ValidReplacements.extend(Deeds)], "Collection Point Materials", [lambda: IDs.ValidReplacements.extend(CollectionPointMaterials)]])

    # Drivers
    GenStandardOption("Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, [], InvalidTargetIDs=AutoAttacks)],["Debuffs", [lambda: IDs.ValidReplacements.extend(ArtDebuffs)],"Buffs",[lambda: IDs.ValidReplacements.extend(ArtBuffs)], "Doom", [lambda: IDs.ValidReplacements.extend([21])]], Scale)
    # GenOption("Driver Art Distances", TabDrivers, "Randomizes how far away you can cast an art", ["common/BTL_Arts_Dr.json"], ["Distance"], Helper.inclRange(0, 20), Helper.inclRange(1,20)) Nothing wrong with this just kinda niche/silly
    GenStandardOption("Driver Skill Trees", TabDrivers, "Randomizes all driver's skill trees", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], DriverSkillTrees, DriverSkillTrees)])
    GenStandardOption("Balanced Skill Trees", TabDrivers, "Balances and randomizes the driver skill trees", [lambda: SkillTreeAdjustments.BalancingSkillTreeRando(OptionDictionary)])
    GenStandardOption("Driver Art Reactions", TabDrivers, "Randomizes each hit of an art to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactionDistribution, InvalidTargetIDs=AutoAttacks)], optionType=Scale) # we want id numbers no edit the 1/6 react stuff
    GenStandardOption("Driver Animation Speed", TabDrivers, "Randomizes animation speeds", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Dr.json"], ["ActSpeed"], Helper.InclRange(0,255), Helper.InclRange(50,255), InvalidTargetIDs=AutoAttacks)])
    # GenStandardOption("Driver Starting Accessory", TabDrivers, "Randomizes what accessory your drivers begin the game with", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Dr.json"], ["DefAcce"], Accessories + [0], Accessories + [0])], ["Remove All Starting Accessories", [lambda: IDs.InvalidReplacements.extend(Accessories)]])
    
    # Blades
    GenStandardOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], Helper.StartsWith("ReAct", 1, 16), HitReactions, HitReactions)], optionType=Scale)
    GenStandardOption("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], ["ArtsType"], [1, 2], [1,2])])
    GenStandardOption("Blade Special Buttons", TabBlades, "Randomizes what button a special uses for its button challenge", [lambda: JSONParser.ChangeJSONFile(["common/MNU_BtnChallenge2.json"], Helper.StartsWith("BtnType", 1, 3), ButtonCombos, ButtonCombos)])
    GenStandardOption("Blade Elements", TabBlades, "Randomizes what element a blade is", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))])
    GenStandardOption("Blade Battle Skills", TabBlades, "Randomizes blades battle (yellow) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BSkill", 1, 3), BladeBattleSkills, BladeBattleSkills)])
    GenStandardOption("Blade Green Skills", TabBlades, "Randomizes blades field (green) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("FSkill", 1, 3), BladeFieldSkills, BladeFieldSkills, InvalidTargetIDs=[1135])])
    # GenOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials, BladeSpecials)]) Commenting out for initial launch I think this setting will put people off it sounds fun but animations no longer connect well on specials
    GenStandardOption("Blade Cooldowns", TabBlades, "Randomizes a blades cooldown", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
    GenStandardOption("Blade Arts", TabBlades, "Randomizes your blade's arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), ArtBuffs, ArtBuffs)])
    GenStandardOption("Blade Aux Core Slots", TabBlades, "Randomizes how many Aux Core slots a Blade gets", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), IDs.BladeAuxCoreSlotDistribution)])
    GenStandardOption("Blade Names", TabBlades, "Randomizes the names of blades", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
    GenStandardOption("Blade Defenses", TabBlades, "Randomizes Blade Physical and Ether Defense", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)])
    GenStandardOption("Blade Mods", TabBlades, "Randomizes Blade Stat Modifiers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(0,100), BladeModDistribution)])
    
    # Enemies
    GenStandardOption("Enemy Drops", TabEnemies, "Randomizes enemy drops", [lambda: JSONParser.ChangeJSONFile(["common/BTL_EnDropItem.json"], Helper.StartsWith("ItemID", 1, 8), AuxCores + Accessories + WeaponChips, AuxCores + Accessories + WeaponChips)])
    GenStandardOption("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [lambda: EnemyRandoLogic.EnemyLogic(OptionDictionary)],["Story Bosses", [], "Quest Enemies", [], "Unique Monsters", [], "Superbosses", [], "Normal Enemies", [], "Mix Enemies Between Types", [], "Keep Enemy Levels", []])
    GenStandardOption("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))])
    #GenOption("Enemy Level Ranges", TabEnemies, "Randomizes enemy level ranges", Helper.InsertHelper(2, 1,90,"maa_FLD_EnemyPop.json", "common_gmk/"), ["ene1Lv", "ene2Lv", "ene3Lv", "ene4Lv"], Helper.inclRange(-100,100), Helper.inclRange(-30,30)) Defunct with alex's enemy rando
    
    # Misc
    GenStandardOption("Music", TabMisc, "Randomizes what music plays where", [lambda: MusicShuffling.SeparateBGMandBattle(OptionDictionary)], ["Seperate Battle and Environment Themes", []]) # need to change title screen music
    # GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
    # GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
    # GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
    #GenStandardOption("Beta Stuff", TabMisc, "Stuff still in testing", [lambda: TestingStuff.Beta(OptionDictionary)])

    # QOL
    # GenStandardOption("Deed Max Values", TabQOL, "Increases the maximum value of deed effects")
    GenStandardOption("Shortened Tutorial", TabQOL, "Shortens/removes tutorials", [lambda: TutorialShortening.ShortenedTutorial(OptionDictionary)])
    # GenStandardOption("Fast Skill Trees", TabQOL, "Makes Blade Skill Trees easy to complete", [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()])
    GenStandardOption("Guaranteed Rare Blades", TabQOL, "Puts Rare Blades in chests instead of the Gacha system", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()])
    GenStandardOption("Early Arts Cancel", TabQOL, "Puts Driver arts cancel skills into the first Driver Skill Tree slot", [lambda: SkillTreeAdjustments.Tier1ArtsCancel(OptionDictionary)])
    GenStandardOption("Treasure Chest Visibility", TabQOL, "Increases the range you can see treasure chests from", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
    GenStandardOption("Freely Engage Blades", TabQOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])


    GenStandardOption("Projectile Treasure Chests", TabFunny, "Launches your items from chests", [lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [12])])
    GenStandardOption("Blade Size", TabFunny, "Randomizes the size of Blades", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Scale", "WpnScale"], AllValues, Helper.InclRange(1,250) + [1000,16000])], optionType= Scale) # Make sure these work for common blades
    GenStandardOption("NPCs Size", TabFunny, "Randomizes the size of NPCs", [lambda: JSONParser.ChangeJSONFile(["common/RSC_NpcList.json"], ["Scale"], Helper.InclRange(1,100), Helper.InclRange(1,250))], optionType=Scale)
    GenStandardOption("Enemy Size", TabFunny, "Randomizes the size of enemies", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnArrange.json"], ["Scale"], Helper.InclRange(0, 1000), Helper.InclRange(1, 200) + Helper.InclRange(990,1000))], optionType=Scale)


    # Cosmetics
    GenStandardOption("Cosmetics", TabCosmetics, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics(OptionDictionary)], RexCosmetics + NiaDriverCosmetics + ToraCosmetics + MoragCosmetics + ZekeCosmetics + PyraCosmetics + MythraCosmetics + DromarchCosmetics + BrighidCosmetics + PandoriaCosmetics + NiaBladeCosmetics + PoppiαCosmetics + PoppiQTCosmetics + PoppiQTπCosmetics, Scale, OptionColorLight)
    
    # Race Mode
    GenStandardOption("Race Mode", TabRaceMode, "Enables Race Mode", [lambda: RaceMode.RaceModeChanging(OptionDictionary)], ["Xohar Fragment Hunt", [], "Less Grinding", [], "Shop Changes", [], "Enemy Drop Changes", [], "DLC Item Removal", [], "Custom Loot", [], "Easy Field Skill Trees", [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()]])

    # # In-Game Settings
    # GenHeader("Camera Settings",TabSettings, None)
    # GenStandardOption("Invert up/down", TabSettings, "Toggle inversion of up/down for camera controls", [],[])
    # GenStandardOption("Invert left/right", TabSettings, "Toggle inversion of left/right for camera controls", [],[])
    # GenStandardOption("Auto camera response speed", TabSettings, "Adjust the response times for the automatically controlled camera", [],[],Scale)
    # GenStandardOption("Camera reset response speed", TabSettings, "Adjust the length of time it takes to reset the camera's position", [],[],Scale)
    # GenStandardOption("Turn speed", TabSettings, "Adjust the turning speed of the manual camera", [],[],Scale)
    # GenStandardOption("Zoom speed", TabSettings, "Adjust the speed of the camera's zoom", [],[],Scale)
    # GenStandardOption("Gradient Correction", TabSettings, "Adjust the automatic behavior of the camera when traversing gradients", [],[])
    # GenHeader("Sound Settings",TabSettings, None)    
    # GenStandardOption("Subtitles", TabSettings, "Toggle subtitles on or off", [],[])
    # GenStandardOption("Cutscene voice volume", TabSettings, "Adjust voice volume during cutscenes", [],[], Scale)
    # GenStandardOption("Game BGM volume", TabSettings, "Adjust background music volume during the game", [],[], Scale)
    # GenStandardOption("Game SE volume", TabSettings, "Adjust volume of sound effects heard during the game", [],[], Scale)
    # GenStandardOption("Game voice volume", TabSettings, "Adjust volume of voices heard during the game", [],[], Scale)
    # GenStandardOption("Battle Narrator volume", TabSettings, "Adjust volume of the battle Narrator (not character battle voices)", [],[], Scale)
    # GenStandardOption("Environment volume", TabSettings, "Adjust volume of environmental sounds (such as rain) heard during the game", [],[], Scale)
    # GenStandardOption("System volume", TabSettings, "Adjust volume of system sounds heard during the game", [],[], Scale)
    # GenHeader("Screen Settings",TabSettings, None)        
    # GenStandardOption("Screen brightness", TabSettings, "Adjust screen brightness", [],[], Scale)
    # GenHeader("Game Settings",TabSettings, None)
    # GenStandardOption("Difficulty level", TabSettings, "Default Difficulty", [],["Easy",[],"Normal",[],"Bringer of Chaos",[], "Custom",[]])
    # GenStandardOption("Auto-battle", TabSettings, "Toggle auto-battle", [],[])
    # GenStandardOption("Automate Special Button Challenges", TabSettings, "Toggle automatic success for button challenge inputs during Specials", [],[])
    # GenStandardOption("Enemy Aggression", TabSettings, "Toggle whether foes pick a fight (exc.salvage, unique, boss, and quest foes)", [],[])
    # GenStandardOption("Special BGM", TabSettings, "When enabled, special battle music will play with certain Blades in the party", [],[])


def Randomize():
    def ThreadedRandomize():
        global OptionDictionary
        RandomizeButton.config(state=DISABLED)

        randoProgressDisplay.pack(side='left', anchor='w', pady=10, padx=10)
        randoProgressDisplay.config(text="Unpacking BDATs")

        random.seed(randoSeedEntry.get())
        print("Seed: " + randoSeedEntry.get())

        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common_gmk.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/gb/common_ms.bdat -o {JsonOutput} -f json --pretty")

        ShowTitleScreenText()

        # Runs all randomization
        RunOptions()
        RaceMode.SeedHash()
        randoProgressDisplay.config(text="Packing BDATs")

        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

        # Outputs common_ms in the correct file structure
        os.makedirs(f"{outDirEntry.get()}/gb", exist_ok=True)
        shutil.move(f"{outDirEntry.get()}/common_ms.bdat", f"{outDirEntry.get()}/gb/common_ms.bdat")

        import time
        randoProgressDisplay.config(text="Done")
        time.sleep(0.5)
        randoProgressDisplay.config(text="")
        randoProgressDisplay.pack_forget()

        RandomizeButton.config(state=NORMAL)
        print("Done")

    threading.Thread(target=ThreadedRandomize).start()

def RunOptions():
    for option in OptionDictionary.values():
        # For Sliders
        if (type(option["optionTypeVal"].get()) == int):
            IDs.CurrentSliderOdds = option["optionTypeVal"].get()
        if (option["optionTypeVal"].get() != 0): # checks main option input
            for subOption in option["subOptionObjects"].values():
                if (subOption["subOptionTypeVal"].get()): # checks subOption input
                    for subCommand in subOption["subCommandList"]:
                        try:
                            subCommand()
                        except:
                            pass
            randoProgressDisplay.config(text=f"Randomizing {option['name']}")
            for command in option["commandList"]:
                try:
                    command()
                except Exception as error:
                    print(f"ERROR: {option['name']} | {error}")
                    import traceback
                    print(f"{traceback.format_exc()}")
 
def GenRandomSeed():
    randoSeedEntry.delete(0, END)
    randoSeedEntry.insert(0,SeedNames.RandomSeedName())

Options()
GUISettings.NotebookFocusStyleFix(defaultFont)
GUISettings.CheckbuttonFocusStyleFix()

bdatcommonFrame = Frame(root, background=Red)
bdatcommonFrame.pack(anchor="w", padx=10)
bdatButton = Button(bdatcommonFrame, width=20, text="Choose Input Folder", command= lambda: Helper.DirectoryChoice("Choose your folder containing common.bdat, common_ms.bdat and common_gmk.bdat", bdatFilePathEntry))
bdatButton.pack(side="left", padx=2, pady=2)
bdatFilePathEntry = Entry(bdatcommonFrame, width=MaxWidth)
bdatFilePathEntry.pack(side="left", padx=2)
OutputDirectoryFrame = Frame(root, background=Red)
OutputDirectoryFrame.pack(anchor="w", padx=10)
outputDirButton = Button(OutputDirectoryFrame, width = 20, text='Choose Output Folder', command= lambda: Helper.DirectoryChoice("Choose an output folder", outDirEntry))
outputDirButton.pack(side="left", padx=2, pady=2)
outDirEntry = Entry(OutputDirectoryFrame, width=MaxWidth)
outDirEntry.pack(side="left", padx=2)
SeedFrame = Frame(root, background=Red)
SeedFrame.pack(anchor="w", padx=10)
seedDesc = Button(SeedFrame, text="Seed", command=GenRandomSeed)
seedDesc.pack(side='left', padx=2, pady=2)

randoSeedEntry = Entry(SeedFrame, width=30)
randoSeedEntry.pack(side='left', padx=2)
RandomizeButton = Button(text='Randomize', command=Randomize)
RandomizeButton.place(relx=0.5, rely=1, y= -10, anchor="s")

Cog = PhotoImage(file="./_internal/Images/SmallSettingsCog.png")
SettingsButton = Button(image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont))
SettingsButton.pack(pady=10, padx=10, side='right', anchor='e') 

randoProgressDisplay = Label(text="", background=Red, anchor="e", foreground=OptionColorLight)

EveryObjectToSaveAndLoad = ([bdatFilePathEntry, outDirEntry, randoSeedEntry] + [option["optionTypeVal"] for option in OptionDictionary.values()] + [subOption["subOptionTypeVal"] for option in OptionDictionary.values() for subOption in option["subOptionObjects"].values()])
SavedOptions.loadData(EveryObjectToSaveAndLoad, "SavedOptions.txt")



root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EveryObjectToSaveAndLoad, "SavedOptions.txt"), root.destroy()))
root.mainloop()