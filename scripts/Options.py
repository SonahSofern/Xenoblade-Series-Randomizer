from tkinter import ttk
import JSONParser, Helper, SavedOptions
from IDs import *
from tkinter import *



class SubOption():
    def __init__(self, _name, _commands = [], _defState = True, _prio = 0):
        self.name = _name
        self.checkBoxVal = None
        self.checkBox:ttk.Checkbutton = None
        self.commands = _commands    
        self.defState = _defState
        self.prio = _prio

class Option():
    def __init__(self, _name:str, _tab, _desc:str, _commands:list, _subOptions: list, _defState = False, _prio = 0):
        # Objects
        self.descObj = None
        self.spinBoxObj = None
        self.spinBoxVal = None
        self.checkBox = None
        self.checkBoxVal = None

        # Initial Data
        self.name =  _name
        self.tab = _tab
        self.desc = _desc
        self.hasSpinBox = False
        self.commands:list = _commands
        self.subDefState = _defState
        self.subOptions:list[SubOption] = _subOptions
        self.prio = _prio
        OptionList.append(self)
        
    def DisplayOption(self, tab):
        self.GenStandardOption(tab)
        # Load Saved Option
        self.StateUpdate()
    
    def GenStandardOption(self, parentTab):   
        # Variables
        global rowIncrement
        spinBoxVar = IntVar(value=100)
        var = BooleanVar()
        self.spinBoxObj = ttk.Label()
        self.spinBoxObj = ttk.Spinbox()

        # Parent Frame
        optionPanel = ttk.Frame(parentTab)
        optionPanel.grid(row = rowIncrement, column= 0, sticky="ew")
        
        # Major Option Checkbox
        checkButtonObj = ttk.Checkbutton(optionPanel, variable= var, text=self.name, width=40, style="midColor.TCheckbutton", command=lambda: self.StateUpdate())
        self.checkBoxVal = var
        checkButtonObj.grid(row=rowIncrement, column=0, sticky="w")
        
        # Description Label
        self.descObj = ttk.Label(optionPanel, text=self.desc, anchor="w", width=60, wraplength=400)
        self.descObj.grid(row=rowIncrement, column=1, sticky="w", padx=0)
        
        # % Boxes
        if self.hasSpinBox:
            self.spinBoxObj = ttk.Spinbox(optionPanel, from_=0, to=100, textvariable=spinBoxVar, wrap=True, width=3, increment=10)
            self.spinBoxObj.grid(row=rowIncrement, column=2, padx=(15,0))
            self.spinBoxObj = ttk.Label(optionPanel, text="% randomized", anchor="w")
            self.spinBoxObj.grid(row=rowIncrement, column=3, sticky="w", padx=0)

        for sub in self.subOptions:
            rowIncrement += 1
            sub.checkBoxVal = BooleanVar(value=sub.defState)
            self.checkBox = ttk.Checkbutton(optionPanel, text=sub.name, variable=sub.checkBoxVal, width=30)
            sub.checkBox = self.checkBox
            self.checkBox.grid(row=rowIncrement, column=0, sticky="sw")
        rowIncrement += 1

    def StateUpdate(self):
        if self.checkBoxVal.get():
            for sub in self.subOptions:
                sub.checkBox.state(["!disabled"])
            self.descObj.state(["!disabled"])
            self.spinBoxObj.state(["!disabled"])
            for sub in self.subOptions: # Handles Dropdown
                sub.checkBox.grid()     
        else:
            for sub in self.subOptions:
                sub.checkBox.state(["disabled"])
            self.descObj.state(["disabled"])
            self.spinBoxObj.state(["disabled"])
            for sub in self.subOptions: # Handles Dropdown
                sub.checkBox.grid_remove()
    
    def GetSpinBox(self):
        return self.spinBoxVal.get()
    
    def GetCheckBox(self):
        return self.checkBoxVal.get()
    


rowIncrement = 0   
OptionList:list[Option] = []
General = 1
Driver  = 2

subAccessoryShopsOption_Accessories = SubOption("Accessories")
AccessoryShopsOption = Option("Accessory Shops", General, "Randomizes the contents of Accessory Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(Accessories)-set([1])),[])],[subAccessoryShopsOption_Accessories], _defState=True)



        




# def Options():
    
#     # General
#     GenStandardOption("Accessory Shops", TabGeneral, "Randomizes the contents of Accessory Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(IDs.Accessories)-set([1])),[])],LootOptions + PouchItemOption, defState=True)
#     GenStandardOption("Collection Points", TabGeneral, "Randomizes the contents of Collection Points", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_CollectionPopList.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID"], list(set(CollectionPointMaterials) - set([30019])), [])], LootOptions + PouchItemOption, defState=True)
#     GenStandardOption("Pouch Item Shops", TabGeneral, "Randomizes the contents of Pouch Item Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), list(set(PouchItems)-set([40007])), [])], LootOptions + PouchItemOption, defState=True)
#     GenStandardOption("Treasure Chests Contents", TabGeneral, "Randomizes the contents of Treasure Chests", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["itm1ID", "itm2ID", "itm3ID", "itm4ID","itm5ID","itm6ID","itm7ID","itm8ID"], Accessories + Boosters + WeaponChips + AuxCores + CoreCrystals + RefinedAuxCores,[])], LootOptions, defState=True)
#     GenStandardOption("Weapon Chip Shops", TabGeneral, "Randomizes Weapon Chips in Weapon Chip Shops", [lambda: JSONParser.ChangeJSONFile(["common/MNU_ShopNormal.json"], Helper.StartsWith("DefItem", 1, 10), WeaponChips, WeaponChips)])

#     # Drivers
#     GenStandardOption("Driver Accessories", TabDrivers, "Randomizes effects of Accessories", [lambda: Accs.RandomizeAccessoryEnhancements()])
#     GenStandardOption("Driver Arts", TabDrivers, "Randomizes effects of all driver arts", [lambda: _DriverArts.DriverArtRandomizer(OptionDictionary), lambda: _DriverArts.GenCustomArtDescriptions()], ["Auto Attacks", [],"Single Reaction", [], "Multiple Reactions", [] ,"Debuffs",[],"Buffs",[],"Cooldown", [], "Damage", [], "Enhancements", [], "Animation Speed", [], "AOE", []], optionType = Spinbox, defState=True)
#     GenStandardOption("Driver Skill Trees", TabDrivers, "Randomizes driver's skill trees",[lambda: SkillTrees.RandomizeSkillEnhancements(OptionDictionary)],["Nonstandard Skills", [], "Early Arts Cancel", [], "Early XYB Attack", []])
       
#     # Blades
#     GenStandardOption("Blades", TabBlades, "Randomizes when blades appear in the story", [lambda: BladeRandomization.BladeRandomization(OptionDictionary)], ["Randomize Dromarch", [], "Guarantee a Healer", []], optionType=Spinbox)
#     GenStandardOption("Blade Aux Cores", TabBlades, "Randomizes the effects of Aux Cores", [lambda: AuxCr.RandomizeAuxCoreEnhancements()])
#     GenStandardOption("Blade Aux Core Slots", TabBlades, "Randomizes a Blade's maximum Aux Core Slots", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["OrbNum"], Helper.InclRange(0,3), IDs.BladeAuxCoreSlotDistribution)])
#     GenStandardOption("Blade Arts", TabBlades, "Randomizes a Blade's arts", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("NArts",1,3), BladeArts, BladeArts)])
#     GenStandardOption("Blade Battle Skills", TabBlades, "Randomizes a Blade's battle (yellow) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BSkill", 1, 3), list(set(BladeBattleSkills) - set([268, 8, 9])), list(set(BladeBattleSkills) - set([268, 267,266,265,144,142,143, 8, 9])) )])
#     GenStandardOption("Blade Field Skills", TabBlades, "Randomizes a Blade's field (green) skill tree",[lambda: _GreenSkills.RandomizeFieldSkills(OptionDictionary)], ["Quest Skills", []])
#     GenStandardOption("Blade Cooldowns", TabBlades, "Randomizes a Blade's swap cooldown", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["CoolTime"], Helper.InclRange(1,1000), Helper.InclRange(1,1000))])
#     GenStandardOption("Blade Defenses", TabBlades, "Randomizes a Blade's Physical and Ether Defense", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["PArmor", "EArmor"], Helper.InclRange(0,100), BladeDefenseDistribution)],optionType=Spinbox)
#     GenStandardOption("Blade Elements", TabBlades, "Randomizes a Blade's element", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"],["Atr"], Helper.InclRange(1,8), Helper.InclRange(1,8))],optionType=Spinbox)
#     GenStandardOption("Blade Mods", TabBlades, "Randomizes a Blade's Stat Modifiers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["HpMaxRev", "StrengthRev", "PowEtherRev", "DexRev", "AgilityRev", "LuckRev"], Helper.InclRange(1,100), BladeModDistribution)])
#     GenStandardOption("Blade Special Buttons", TabBlades, "Randomizes what button a special uses for its button challenge", [lambda: JSONParser.ChangeJSONFile(["common/MNU_BtnChallenge2.json"], Helper.StartsWith("BtnType", 1, 3), ButtonCombos, [])], ["A", [lambda: ValidReplacements.append(1)] ,"B", [lambda: ValidReplacements.append(2)], "X", [lambda: ValidReplacements.append(3)], "Y", [lambda: ValidReplacements.append(4)], "?", [lambda: ValidReplacements.append(5)]], defState=True)
#     GenStandardOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], Helper.StartsWith("ReAct", 1, 16), HitReactions, HitReactions)], optionType=Spinbox)
#     GenStandardOption("Blade Weapon Chips", TabBlades, "Randomizes the effects of weapon chips", [],["Auto Attack",[lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["Damage"],Helper.InclRange(0,1298), Helper.InclRange(1,900) + Helper.InclRange(1000,1100) + Helper.InclRange(1250,1300))],"Crit Rate",[lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["CriRate"],Helper.InclRange(0,100), BladeWeaponCritDistribution)],"Guard Rate",[lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpn.json"],["GuardRate"],Helper.InclRange(0,100), BladeWeaponGuardDistribution)],"Enhancements",[lambda: WPChips.RandomizeWeaponEnhancements(OptionDictionary["Blade Weapon Chips"]["spinBoxVal"])]], optionType= Spinbox, defState=True)
#     GenStandardOption("Blade Weapon Class", TabBlades, "Randomizes weapon roles (ATK, TNK, HLR)", [lambda: JSONParser.ChangeJSONFile(["common/ITM_PcWpnType.json"], ["Role"], Helper.InclRange(1,3), WeaponTypeRoles)])
  
#     # Enemies
#     GenStandardOption("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [lambda: EnemyRandoLogic.EnemyLogic(OptionDictionary)],["Story Bosses", [], "Quest Enemies", [], "Unique Monsters", [], "Superbosses", [], "Normal Enemies", [], "Mix Enemies Between Types", [], "Use All Original Encounter Levels", [], "Use Original Boss Encounter Levels", [], "Use Original Quest Encounter Levels", []], defState=True)
#     GenStandardOption("Enemy Enhancements", TabEnemies, "Gives enemies a random enhancement; displayed by their name", [lambda: _EnemyEnhancements.EnemyStats(OptionDictionary["Enemy Enhancements"]["spinBoxVal"].get())],optionType=Spinbox)
#     GenStandardOption("Enemy Arts Effects", TabEnemies, "Gives enemies a random bonus effect to their arts; displayed by their art's name", [lambda: _EnemyArts.EnemyArtAttributes(OptionDictionary)], ["AOE", [], "Debuffs", [], "Buffs", [], "Reactions", [], "Enhancements", []],optionType=Spinbox, defState=True)
#     GenStandardOption("Enemy Drops", TabEnemies, "Randomizes enemy drops", [lambda: JSONParser.ChangeJSONFile(["common/BTL_EnDropItem.json"], Helper.StartsWith("ItemID", 1, 8), AuxCores+ RefinedAuxCores + IDs.Accessories + WeaponChips, [])], LootOptions, optionType=Spinbox, defState=True)
#     GenStandardOption("Enemy Aggro", TabEnemies, "The percentage of all non-boss and non-quest enemies that will aggro the player", [lambda: EnemyRandoLogic.EnemyAggroProportion(OptionDictionary)],optionType=Spinbox)
#     GenStandardOption("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], Helper.InclRange(0,100), Helper.InclRange(0,100) + Helper.InclRange(250,255))],optionType=Spinbox)

#     # Misc
#     GenStandardOption("Music", TabMisc, "Randomizes Music", [lambda: MusicShuffling.MusicShuffle(OptionDictionary)], ["Mix Battle and \nEnvironment Themes", []]) # need to change title screen music
#     GenStandardOption("Trust Lines", TabMisc, "Randomizes blade trust lines in battle (colors, power, etc.)", [lambda: TrustBeam.BeamRandomizer()])
#     GenStandardOption("Custom Core Crystals", TabMisc, "Adds Core Crystals with guaranteed Rare Blades to Treasure Chests.", [lambda: CoreCrystalAdjustments.CoreCrystalChanges(OptionDictionary)], optionType=Spinbox) # The slider shouldnt do anything tbh the other things have sliders like enemy drop rando, chest rando etc. All this should do is add custom crystals to the crystal file. 
#     GenStandardOption("Difficulty", TabMisc, "Forces this difficulty, regardless of what is chosen in the options menu", [], ["Easy", [], "Normal", [], "Bringer of Chaos", [], "Ultimate", []])

#     # QOL
#     GenStandardOption("Shortened Tutorial", TabQOL, "Shortens/removes tutorials", [lambda: TutorialShortening.ShortenedTutorial(OptionDictionary)])
#     GenStandardOption("Unlock NG+ Blades", TabQOL, "Allows all blades to be accessible in a fresh playthrough",[lambda: GachaModifications.UnlockNGPlusBlades()])
#     GenStandardOption("Freely Engage Blades", TabQOL, "Allows blades to be freely engaged by all valid drivers", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["FreeEngage"], [0], [1], [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1075, 1076, 1103])])
#     GenStandardOption("Treasure Chest Visibility", TabQOL, "Increases the range you can see treasure chests from", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"), ["msgVisible", "msgdigVisible"], Helper.InclRange(0,200), [255])])
#     GenStandardOption("Remove Story Field Skills", TabQOL, "Removes field skill checks",  [lambda: FieldSkillAdjustments.RemoveFieldSkills(OptionDictionary)], ["Remove All Field Skills", []])
#     GenStandardOption("Everlasting Pouch Items", TabQOL, "Makes Pouch Items last forever", [lambda: JSONParser.ChangeJSONFile(["common/ITM_FavoriteList.json"],["Time"], Helper.InclRange(0,255), [6099])])
#     GenStandardOption("Condense Gold Loot", TabQOL, "Condenses gold in chests so you can see other items", [lambda: JSONParser.ChangeJSONFile(Helper.InsertHelper(2,1,90, "maa_FLD_TboxPop.json", "common_gmk/"),["goldPopMin", "goldPopMax"], Helper.InclRange(0,100000), [1])])
#     GenStandardOption("Mute Popups", TabQOL, "Stops blade skill and pouch item refill popups", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[89], ["sheet06"], [""])],["Landmarks", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[85], ["sheet04"], [""])]])
#     GenStandardOption("Enhancement Display", TabQOL, "Shows when enhancements activate in battle", [lambda: Enhancements.SearchAndSetDisplayIDs()])
#     GenStandardOption("Easy Blade Skill Trees", TabQOL, "Makes trust the only condition for levelling up a blade's skill tree", [lambda: SkillTrees.BladeSkillTreeShortening()])
#     GenStandardOption("Faster Levels", TabQOL, "Decreases EXP required for each levelup",[],["2x", [lambda: Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 2'])], "4x", [lambda: Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 4'])], "8x", [lambda: Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 8'])], "16x", [lambda: Helper.MathmaticalColumnAdjust(["./_internal/JsonOutputs/common/BTL_Grow.json"], ["LevelExp", "LevelExp2"], ['row[key] // 16'])]])
    
#     # Funny
#     GenStandardOption("Projectile Treasure Chests", TabFunny, "Launches your items from chests", [lambda: JSONParser.ChangeJSONFile(["common/RSC_TboxList.json"], ["box_distance"], [0,0.5,1], [15])])
#     GenStandardOption("Blade Size", TabFunny, "Randomizes the size of Blades", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Scale", "WpnScale"], [], BladeScales)], optionType= Spinbox) # Make sure these work for common blades
#     GenStandardOption("NPCs Size", TabFunny, "Randomizes the size of NPCs", [lambda: JSONParser.ChangeJSONFile(["common/RSC_NpcList.json"], ["Scale"],[], NPCScales)], optionType=Spinbox)
#     GenStandardOption("Enemy Size", TabFunny, "Randomizes the size of enemies", [lambda: JSONParser.ChangeJSONFile(["common/CHR_EnArrange.json"], ["Scale"], [], EnemyScales)], optionType=Spinbox)
#     GenStandardOption("Field Items", TabFunny, "Randomizes the size and spin rate of items from chests and collection points", [lambda: BigItems.BigItemsRando()])

#     # Cosmetics
#     GenStandardOption("Character Outfits", TabCosmetics, "Randomizes Cosmetics on Accessories and Aux Cores", [lambda: Cosmetics(OptionDictionary)], CosmeticsList, Spinbox, defState=True)
#     GenStandardOption("Blade Weapon Cosmetics", TabCosmetics, "Keeps all default weapon models regardless of chips", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["OnlyWpn"], [0], [1])])
    
#     # Race Mode
#     GenStandardOption("Race Mode", TabGameMode, "Enables Race Mode (see the Race Mode README)", [lambda: RaceMode.RaceModeChanging(OptionDictionary), RaceMode.SeedHash], ["Zohar Fragment Hunt", [], "Less Grinding", [], "Shop Changes", [], "Enemy Drop Changes", [], "DLC Item Removal", [], "Custom Loot", [], "Field Skill Trees", [lambda: CoreCrystalAdjustments.FieldSkillLevelAdjustment()]], defState=True)
#     GenStandardOption("Unique Monster Hunt", TabGameMode, "Experimental Mode", [lambda: UniqueMonsterHunt.UMHunt()], optionType=Spinbox)

#     GenStandardOption("Chest Type Matches Contents", TabQOL, "Chest model and label changes depending on tier of loot", [lambda: RaceMode.ChestTypeMatching(OptionDictionary)])

#     # Currently Disabled for Various Reasons
#     # Blade Names (moved so that blade name rando doesn't mess up Race Mode getting blade IDs)
#     # GenStandardOption("Blade Names", TabBlades, "Randomizes a Blade's name", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], ["Name"], Helper.InclRange(0,1000), BladeNames)])
#     # GenStandardOption("Less UI", TabQOL, "Removes some of the unneccessary on screen UI (Blade Swap and Current Objective)", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03"], [""])])
#     # GenStandardOption("Screenshot Mode", TabQOL, "Removes most UI for screenshots", [lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[88], ["sheet05", "sheet03", "sheet04"], ""), lambda: JSONParser.ChangeJSONLine(["common/MNU_Layer.json"],[86], ["sheet02", "sheet03"], "")])
#     # CTMC (has to run after Race Mode in current iteration, needs to know what chests have what loot)
#     # GenDictionary("NPCs", TabMisc, "Randomizes what NPCs appear in the world (still testing)", [lambda: JSONParser.ChangeJSON(Helper.InsertHelper(2, 1,90,"maa_FLD_NpcPop.json", "common_gmk/"), ["NpcID"], Helper.InclRange(0,3721), Helper.InclRange(2001,3721))])
#     # GenOption("Funny Faces", TabMisc, "Randomizes Facial Expressions", ["common/EVT_eyetype.json"], ["$id"], Helper.inclRange(0,15), Helper.inclRange(0,15)) # doesnt work yet
#     # GenDictionary("Menu Colors", TabMisc, "Randomizes Colors in the UI", [lambda: JSONParser.ChangeJSON(["common/MNU_ColorList.json"], ["col_r", "col_g", "col_b"], Helper.InclRange(0,255), Helper.InclRange(0,0))])
#     # GenStandardOption("Blade Weapons", TabBlades, "Randomizes a Blade Weapon type, for example Pyra can now be a Knuckle Claws user", [lambda: _BladeWeapons.WepRando()])
#     # GenStandardOption("Blade Specials", TabBlades, "Randomizes blades special (red) skill tree", [lambda: JSONParser.ChangeJSONFile(["common/CHR_Bl.json"], Helper.StartsWith("BArts", 1, 3) + ["BartsEx", "BartsEx2"], BladeSpecials,  list(set(BladeSpecials) - set([215])))]) works okay, but animations dont connect feels mid
#     # DebugLog.CreateDebugLog(OptionDictionary, Version, randoSeedEntry.get())
#     # GenStandardOption("Enemy Arts", TabEnemies, "Gives enemies new arts", [lambda: _EnemyArts.EnemyArts(OptionDictionary["Enemy Arts"]["spinBoxVal"].get())],optionType=Spinbox)
#     # GenStandardOption("Enemy Rage", TabEnemies, "Randomizes the effects of enemy enraged states", ["common/BTL_Aura"])   

def UpdateAllStates():
    for opt in OptionList:
        opt.StateUpdate()