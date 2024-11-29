from tkinter import PhotoImage, ttk
import random, subprocess, shutil, os, threading, types
from tkinter import *
import EnemyRandoLogic, SavedOptions, SeedNames, JSONParser, SkillTreeAdjustments, CoreCrystalAdjustments, TestingStuff, RaceMode, TutorialShortening, IDs
from IDs import *
from Cosmetics import *
from UI_Colors import *

root = Tk()
root.title("Xenoblade Chronicles 2 Randomizer 0.1.0")
root.configure(background=Red)
root.geometry('900x800')
icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

CommonBdatInput = ""
JsonOutput = "./_internal/JsonOutputs"
OptionDictionary = {}
rowIncrement = 0
MaxWidth = 1000

# The Notebook
MainWindow = ttk.Notebook(root, height=5)

def NotebookFocusStyleFix():
    style = ttk.Style()

    style.layout("Tab",
    [('Notebook.tab', {'sticky': 'nswe', 'children':
        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
            #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],
            #})],
        })],
    })]
    )

NotebookFocusStyleFix()
# Frames in the notebook
TabGeneralOuter = Frame(MainWindow) 
TabDriversOuter = Frame(MainWindow) 
TabBladesOuter = Frame(MainWindow) 
TabEnemiesOuter = Frame(MainWindow) 
TabMiscOuter = Frame(MainWindow) 
TabQOLOuter = Frame(MainWindow)
TabCosmeticsOuter = Frame(MainWindow)
TabRaceModeOuter = Frame(MainWindow)
TabSettingsOuter = Frame(MainWindow)

# Canvas 
TabGeneralCanvas = Canvas(TabGeneralOuter) 
TabDriversCanvas = Canvas(TabDriversOuter) 
TabBladesCanvas = Canvas(TabBladesOuter)
TabEnemiesCanvas = Canvas(TabEnemiesOuter) 
TabMiscCanvas = Canvas(TabMiscOuter)
TabQOLCanvas = Canvas(TabQOLOuter)
TabCosmeticsCanvas = Canvas(TabCosmeticsOuter)
TabRaceModeCanvas = Canvas(TabRaceModeOuter)
TabSettingsCanvas = Canvas(TabSettingsOuter)

# Actual Scrollable Content
TabGeneral = Frame(TabGeneralCanvas) 
TabDrivers = Frame(TabDriversCanvas) 
TabBlades = Frame(TabBladesCanvas)
TabEnemies = Frame(TabEnemiesCanvas) 
TabMisc = Frame(TabMiscCanvas)
TabQOL = Frame(TabQOLCanvas)
TabCosmetics = Frame(TabCosmeticsCanvas)
TabRaceMode = Frame(TabRaceModeCanvas)
TabSettings = Frame(TabSettingsOuter)

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

CreateScrollBars([TabGeneralOuter, TabDriversOuter, TabBladesOuter, TabEnemiesOuter, TabMiscOuter, TabQOLOuter, TabCosmeticsOuter, TabRaceModeOuter, TabSettingsOuter],[TabGeneralCanvas, TabDriversCanvas, TabBladesCanvas, TabEnemiesCanvas, TabMiscCanvas, TabQOLCanvas, TabCosmeticsCanvas, TabRaceModeCanvas, TabSettingsCanvas],[TabGeneral, TabDrivers, TabBlades, TabEnemies, TabMisc, TabQOL, TabCosmetics, TabRaceMode, TabSettings])

# Tabs
MainWindow.add(TabGeneralOuter, text ='General') 
MainWindow.add(TabDriversOuter, text ='Drivers') 
MainWindow.add(TabBladesOuter, text ='Blades') 
MainWindow.add(TabEnemiesOuter, text ='Enemies') 
MainWindow.add(TabMiscOuter, text ='Misc.') 
MainWindow.add(TabQOLOuter, text = 'Quality of Life')
MainWindow.add(TabCosmeticsOuter, text='Cosmetics')
MainWindow.add(TabRaceModeOuter, text='Race Mode')
MainWindow.add(TabSettingsOuter, text = 'Game Settings')
MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 

def GenDictionary(optionName, parentTab, description, commandList = [], subOptionName_subCommandList = [], optionType = Checkbutton):   
    global OptionDictionary
    global rowIncrement
    # Create Option Color
    if (rowIncrement %2 == 0):
        OptionColor = White
    else:
        OptionColor = Gray

    optionPanel = Frame(parentTab, padx=10, pady=10, background=OptionColor)
    optionPanel.grid(row = rowIncrement, column= 0, sticky="ew")

    # Create Option Name
    option = Label(optionPanel, text=optionName, background=OptionColor, width=30, anchor="w", wraplength=150)
    option.grid(row=rowIncrement, column=0, sticky="sw")

    # Create Option Interactable
    if (optionType == Checkbutton):
        var = BooleanVar()
        optionTypeObj = Checkbutton(optionPanel, background=OptionColor, highlightthickness=0, variable= var, text=description)
        optionTypeObj.grid(row=rowIncrement, column=1, sticky="e")
        optionType = var    
    elif (optionType == Scale):
        var = IntVar()
        optionTypeObj = Scale(optionPanel, from_=0, to=100, orient= HORIZONTAL, sliderlength=10,variable=var, background=OptionColor, highlightthickness=0)
        optionDesc = Label(optionPanel, text=description, background=OptionColor, anchor='w')
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
    spaceFill = Label(optionPanel, text="", background=OptionColor, width=MaxWidth, anchor='w')
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
        checkBox = Checkbutton(optionPanel, background=OptionColor, text=subOptionName_subCommandList[2*i], variable=var, highlightthickness=0)
        checkBox.grid(row=rowIncrement+i+1, column=0, sticky="sw")
        # print(len(subOptionName_subCommandList[2*i]))

        # Default Command if you dont provide a lambda command for a suboption (made so i dont have to write a million lambda statements)
        if subOptionName_subCommandList[2*i+1] == []:
            autoCommand = []
        elif isinstance(subOptionName_subCommandList[2*i+1][0], types.LambdaType):
            autoCommand = subOptionName_subCommandList[2*i+1]
        else:
            autoCommand = [lambda: IDs.ValidReplacements.extend(subOptionName_subCommandList[2*i+1])]


        OptionDictionary[optionName]["subOptionObjects"][subOptionName_subCommandList[2*i]] = {
        "subName": subOptionName_subCommandList[2*i],
        "subOptionTypeVal": var,
        "subCommandList": autoCommand,
        }


    rowIncrement += 1
    
def Options():

    # General
    GenDictionary("Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops", [lambda: JSONParser.ChangeJSON(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(PouchItems)-set([40007])), PouchItems)])
    GenDictionary("Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops", [lambda: JSONParser.ChangeJSON(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(Accessories)-set([1])), Accessories + Helper.InclRange(448,455))])
    GenDictionary("Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Weapon Chip Shops", [lambda: JSONParser.ChangeJSON(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)])
    GenDictionary("Treasure Chests Contents", TabGeneral, "Randomizes the contents of Treasure Chests", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID","itm5ID","itm6ID","itm7ID","itm8ID"], Accessories + WeaponChips + AuxCores + CoreCrystals,[])], ["Accessories", Accessories ,"Weapon Chips", WeaponChips, "Aux Cores", AuxCores, "Core Crystals", CoreCrystals, "Deeds", Deeds, "Collection Point Materials", CollectionPointMaterials])
    GenDictionary("Collection Points", TabGeneral, "Randomizes the contents of Collection Points", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2,1,90, "maa_FLD_CollectionPopList.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID"], list(set(CollectionPointMaterials) - set([30019])), [])], ["Accessories", Accessories,"Weapon Chips", WeaponChips, "Aux Cores", AuxCores, "Core Crystals", CoreCrystals, "Deeds", Deeds, "Collection Point Materials", CollectionPointMaterials])

    # Drivers
    GenDictionary("Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", [lambda: JSONParser.ChangeJSON(["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], ArtDebuffs, ArtDebuffs + ArtBuffs, InvalidTargetIDs=AutoAttacks)], ["Doom", [21]], Scale)
    # GenOption("Driver Art Distances", TabDrivers, "Randomizes how far away you can cast an art", ["common/BTL_Arts_Dr.json"], ["Distance"], Helper.inclRange(0, 20), Helper.inclRange(1,20)) Nothing wrong with this just kinda niche/silly
    GenDictionary("Driver Skill Trees", TabDrivers, "Randomizes all driver's skill trees", [lambda: JSONParser.ChangeJSON(["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], DriverSkillTrees, DriverSkillTrees)])
    GenDictionary("Balanced Skill Trees", TabDrivers, "Balances and randomizes the driver skill trees", [lambda: SkillTreeAdjustments.BalancingSkillTreeRando(OptionDictionary)])
    GenDictionary("Arts Cancel on Tier 1", TabDrivers, "Puts the Driver Skill that allows you to cancel Driver Arts into each other on the left-most Tier 1 Driver Skill Tree slot.", [lambda: SkillTreeAdjustments.Tier1ArtsCancel(OptionDictionary)])
    GenDictionary("Driver Art Reactions", TabDrivers, "Randomizes each hit of an art to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSON(["common/BTL_Arts_Dr.json"], Helper.StartsWith("ReAct", 1,16), HitReactions, HitReactions, InvalidTargetIDs=AutoAttacks)], optionType=Scale) # we want id numbers no edit the 1/6 react stuff
    GenDictionary("Driver Animation Speed", TabDrivers, "Randomizes animation speeds", [lambda: JSONParser.ChangeJSON(["common/BTL_Arts_Dr.json"], ["ActSpeed"], Helper.InclRange(0,255), Helper.InclRange(50,255), InvalidTargetIDs=AutoAttacks)])
    GenDictionary("Driver Starting Accessory", TabDrivers, "Randomizes what accessory your drivers begin the game with", [lambda: JSONParser.ChangeJSON(["common/CHR_Dr.json"], ["DefAcce"], AllValues, Accessories)], ["Remove All Starting Accessories", Accessories])
    
    # Blades
    GenDictionary("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSON(["common/BTL_Arts_Bl.json"], Helper.StartsWith("ReAct", 1, 16), HitReactions, HitReactions)], optionType=Scale)
    GenDictionary("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage", [lambda: JSONParser.ChangeJSON(["common/BTL_Arts_Bl.json"], ["ArtsType"], [1, 2], [1,2])])
    GenDictionary("Blade Special Buttons", TabBlades, "Randomizes what button a special uses for its button challenge", [lambda: JSONParser.ChangeJSON(["common/MNU_BtnChallenge2.json"], Helper.StartsWith("BtnType", 1, 3), ButtonCombos, ButtonCombos)])
    GenDictionary("Blade Elements", TabBlades, "Randomizes what element a blade is", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))])
    GenDictionary("Blade Battle Skills", TabBlades, "Randomizes blades battle (yellow) skill tree", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("BSkill", 1, 3), BladeBattleSkills, BladeBattleSkills)])
    GenDictionary("Blade Green Skills", TabBlades, "Randomizes blades field (green) skill tree", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("FSkill", 1, 3), BladeFieldSkills, BladeFieldSkills, InvalidTargetIDs=[1135])])
    # GenOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials, BladeSpecials)]) Commenting out for initial launch I think this setting will put people off it sounds fun but animations no longer connect well on specials
    GenDictionary("Blade Cooldowns", TabBlades, "Randomizes a blades cooldown", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
    GenDictionary("Blade Arts", TabBlades, "Randomizes your blade's arts", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), ArtBuffs, ArtBuffs)])
    GenDictionary("Blade Aux Core Slots", TabBlades, "Randomizes how many Aux Core slots a Blade gets", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), Helper.InclRange(0,3))])
    GenDictionary("Blade Names", TabBlades, "Randomizes the names of blades", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
    GenDictionary("Blade Defenses", TabBlades, "Randomizes Blade Physical and Ether Defense", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)])
    GenDictionary("Blade Mods", TabBlades, "Randomizes Blade Stat Modifiers", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(0,100), BladeModDistribution)])
    GenDictionary("Blade Scale", TabBlades, "Randomizes the size of Blades", [lambda: JSONParser.ChangeJSON(["common/CHR_Bl.json"], ["Scale", "WpnScale"], AllValues, Helper.InclRange(1,250) + [1000,16000])]) # Make sure these work for common blades
    
    # Enemies
    GenDictionary("Enemy Drops", TabEnemies, "Randomizes enemy drop tables", [lambda: JSONParser.ChangeJSON(["common/BTL_EnDropItem.json"], Helper.StartsWith("ItemID", 1, 8), AuxCores + Accessories + WeaponChips, AuxCores + Accessories + WeaponChips)])
    GenDictionary("Enemy Size", TabEnemies, "Randomizes the size of enemies", [lambda: JSONParser.ChangeJSON(["common/CHR_EnArrange.json"], ["Scale"], Helper.InclRange(0, 1000), Helper.InclRange(1, 200) + Helper.InclRange(990,1000))])
    GenDictionary("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [lambda: EnemyRandoLogic.EnemyLogic(OptionDictionary)],["Story Bosses", [], "Quest Enemies", [], "Unique Monsters", [], "Superbosses", [], "Normal Enemies", [], "Mix Enemies Between Types", [], "Keep All Enemy Levels", [], "Keep Quest Enemy Levels", [], "Keep Story Boss Levels", []])
    GenDictionary("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSON(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))])
    #GenOption("Enemy Level Ranges", TabEnemies, "Randomizes enemy level ranges", Helper.InsertHelper(2, 1,90,"maa_FLD_EnemyPop.json", "common_gmk/"), ["ene1Lv", "ene2Lv", "ene3Lv", "ene4Lv"], Helper.inclRange(-100,100), Helper.inclRange(-30,30)) Defunct with alex's enemy rando
    
    # Misc
    GenDictionary("Music", TabMisc, "Randomizes what music plays where", [lambda: JSONParser.ChangeJSON(["common/RSC_BgmCondition.json"], ["BgmIDA", "BgmIDB", "BgmIDC", "BgmIDD"], BackgroundMusic, BackgroundMusic)]) # need to change title screen music
    GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
    GenDictionary("NPCs Size", TabMisc, "Randomizes the size of NPCs", [lambda: JSONParser.ChangeJSON(["common/RSC_NpcList.json"], ["Scale"], Helper.InclRange(1,100), Helper.InclRange(1,250))])
    #GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
    GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
    GenDictionary("Beta Stuff", TabMisc, "Stuff still in testing", [lambda: TestingStuff.Beta()])

    # QOL
    GenDictionary("Fix Bad Descriptions", TabQOL, "Fixes some of the bad descriptions in the game") #common_ms/menu_ms
    GenDictionary("Running Speed", TabQOL, "Max out your starting Run Speed")
    GenDictionary("Shortened Tutorial", TabQOL, "Shortens/removes all tutorials", [lambda: TutorialShortening.ShortenedTutorial(OptionDictionary)])
    GenDictionary("Blade Skill Tree Changes", TabQOL, "Makes all blades' field skills maxed by default", [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()])
    GenDictionary("Core Crystal Changes", TabQOL, "Removes the Gacha system in favor of custom Core Crystals", [lambda: CoreCrystalAdjustments.CoreCrystalChanges()])
    #GenOption("Freely Engage All Blades", TabQOL, "Allows all blades to be freely engaged", ["common/CHR_Bl.json"], []) # common/CHR_Bl Set Free Engage to true NEED TO FIGURE OUT ACCESS TO FLAGS
    
    # Cosmetics
    # GenOption("Rex's Cosmetics", TabCosmetics, "Randomizes Rex's Outfits", ["common/CHR_Dr.json"], ["Model"], [DefaultRex], [], RexCosmetics, optionType=[Checkbutton])
    # GenOption("Pyra's Cosmetics", TabCosmetics, "Randomizes Pyra's Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultPyra], [], PyraCosmetics, optionType=[Checkbutton])
    # GenOption("Mythra's Cosmetics", TabCosmetics, "Randomizes Mythra's Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultMythra], [], MythraCosmetics, optionType=[Checkbutton])
    # GenOption("Nia's Cosmetics (Driver)", TabCosmetics, "Randomizes Nia's Driver Outfits", ["common/CHR_Dr.json"], ["Model"], [DefaultDriverNia], [], NiaDriverCosmetics, optionType=[Checkbutton])
    # GenOption("Nia's Cosmetics (Blade)", TabCosmetics, "Randomizes Nia's Blade Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultBladeNia], [], NiaBladeCosmetics, optionType=[Checkbutton])
    # GenOption("Dromarch's Cosmetics", TabCosmetics, "Randomizes Dromarch's Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultDromarch], [], DromarchCosmetics, optionType=[Checkbutton])
    # GenOption("Tora's Cosmetics", TabCosmetics, "Randomizes Tora's Outfits", ["common/CHR_Dr.json"], ["Model"], [DefaultTora], [], ToraCosmetics, optionType=[Checkbutton])
    # GenOption("Morag's Cosmetics", TabCosmetics, "Randomizes Morag's Outfits", ["common/CHR_Dr.json"], ["Model"], [DefaultMorag], [], MoragCosmetics, optionType=[Checkbutton])
    # GenOption("Brighid's Cosmetics", TabCosmetics, "Randomizes Brighid's Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultBrighid], [], BrighidCosmetics, optionType=[Checkbutton])
    # GenOption("Zeke's Cosmetics", TabCosmetics, "Randomizes Zeke's Outfits", ["common/CHR_Dr.json"], ["Model"], [DefaultZeke], [], ZekeCosmetics, optionType=[Checkbutton])
    # GenOption("Pandoria's Cosmetics", TabCosmetics, "Randomizes Pandoria's Outfits", ["common/CHR_Bl.json"], ["Model"], [DefaultPandoria], [], PandoriaCosmetics, optionType=[Checkbutton])
    
    # Race Mode
    GenDictionary("Race Mode", TabRaceMode, "Enables Race Mode", [lambda: RaceMode.RaceModeChanging(OptionDictionary)], ["Mysterious Part Hunt", [], "Less Grinding", [], "Shop Changes", [], "Enemy Drop Changes", [], "DLC Item Removal", [], "Custom Loot", []])

def Randomize():
    def ThreadedRandomize():
        global OptionDictionary
        RandomizeButton.config(state=DISABLED)

        randoProgressDisplay.pack()
        randoProgressDisplay.config(text="Unpacking BDATs")

        random.seed(randoSeedEntry.get())
        print("Seed: " + randoSeedEntry.get())

        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common_gmk.bdat -o {JsonOutput} -f json --pretty")
        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/gb/common_ms.bdat -o {JsonOutput} -f json --pretty")

        # Runs all randomization
        RunOptions()


        randoProgressDisplay.config(text="Packing BDATs")

        subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

        # Outputs common_ms in the correct file structure
        os.makedirs(f"{outDirEntry.get()}/gb", exist_ok=True)
        shutil.move(f"{outDirEntry.get()}/common_ms.bdat", f"{outDirEntry.get()}/gb/common_ms.bdat")

        import time
        randoProgressDisplay.config(text="Done")
        time.sleep(1)
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
                except:
                    pass
 
def GenRandomSeed():
    randoSeedEntry.delete(0, END)
    randoSeedEntry.insert(0,SeedNames.RandomSeedName())

Options()


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
RandomizeButton.pack(pady=10) 
randoProgressDisplay = Label(text="", background=Red, anchor="e", foreground=White)

EveryObjectToSaveAndLoad = ([bdatFilePathEntry, outDirEntry, randoSeedEntry] + [option["optionTypeVal"] for option in OptionDictionary.values()] + [subOption["subOptionTypeVal"] for option in OptionDictionary.values() for subOption in option["subOptionObjects"].values()])
SavedOptions.loadData(EveryObjectToSaveAndLoad)

root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EveryObjectToSaveAndLoad), root.destroy()))
root.mainloop()