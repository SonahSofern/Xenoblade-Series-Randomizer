from scripts import JSONParser, Helper, PopupDescriptions

# More flags in here? https://xenobladedata.github.io/xb3_200_dlc4/331C38A9.html

def TutorialSkips(): # For some reason visually the game wont load the entire hud until aftyer the first boss in the intro but thats fine
    tutFile = JSONParser.File("XC3/JsonOutputs/prg/SYS_Tutorial.json")
    allTutorialIDs = Helper.InclRange(1,185)
    TutorialRemoval(tutFile, allTutorialIDs)
    TutorialShorten(tutFile, allTutorialIDs)
    tutFile.Close()
    UnlockAllSystemsTutorialsLocked()
    SetTipNotificationsOff()
        
def TutorialRemoval(tutFile:JSONParser.File, targetIDs):  
    for tut in tutFile.rows:
        if tut["$id"] not in targetIDs: continue
        tut["EnemyInfo"] = 0
        tut["Repeat"] = 0
        tut["<CA1A7DB1>"] = 0

def TutorialShorten(tutFile:JSONParser.File, targetIDs):
    '''For tutorials that cannot be skipped shorten then to one page'''
    for tut in tutFile.rows:
        if tut["$id"] not in targetIDs: continue
        for i in range(2,6):
            tut[f"Tips{i}"] = 0
       
def UnlockAllSystemsTutorialsLocked():
    '''Because we skip tutorials we have to unlock the players systems manually instead of through the normal tutorials'''
    tutFile = JSONParser.File("XC3/JsonOutputs/sys/SYS_SystemOpen.json")

    # Unlock right from the start
    startingUnlocks = [
        3, # Skip time
        4, # Skip travel
        5, # Shop release
        6, # Character Customization
        7, # Talent Customization
        9, # Party status
        10, # Information Piece (Yellow info bubbles?)
        11, # Quest
        12, # Collectepedia Cards
        13, # Kizunagram (Affinity chart?)
        14, # Photo Mode (L+R? or unused photo mode)
        15, # Colony (Colony affinity?)
        16, # Supplies (Supply Drops?)
        17, # Ether Absorber
        18, # Memory Space (??)
        20, # Respect (??)
        23, # Communication Spot (Campfires/ Food Spots to discuss info)
        26, # Level Up Campfire
        27, # Level Down Campfire 
        29, # Sendoff Soul
        30, # Arts
        31, # Talent Arts
        32, # Role Act (Build up a talent art I guess)
        33, # Revive/Help up
        34, # Instruct Allies
        35, # Quick Move
        42, # Change Character
        43, # Gold Drop (??)
        44, # Hero Accessories Editing
        70, # Menu Shortcuts
        71, # Fashion Equipment
        76, # Training
    ]
    
    # Unlocks later
    laterUnlocks = [
        19, # Moebius Alert
        21, # Eyepatch
        22, # Flame clock 
        24, # Gem Craft
        25, # Cook Food
        28, # Boundary Ship 
        37, # Chain Attack
        38, # Master Arts
        39, # Master Skills
        40, # Master Art Slots
        41, # Master Skill Slots
        45, # Class Learning
        46, # Class Growth (Class Points)
        52, # Upgraded Boundary Ship
        36, # Interlink
        53, # Mio Interlink
        54, # Lanz Interlink
        55, # Senna Interlink
        56, # Eunie Interlink
        57, # Taion Interlink
        74, # Ouroborous Switch
        60, # Rope Sliding
        61, # Wall Climbing
        62, # Quicksand
        63, # Poison Immunity
        75, # Soul Link (Special slots in ouros)
        78, 79, 80, 81, 82, 83 # Soul Link Slot 2
    ]
    # Unrelated to tutorials
    noTutorialUnlocks = [
        47, # PC White Gear (???)
        48, # Mio Tattoo Swap
        49, # Mio Expression Swap
        50, # Ouroborous Version of Weapon
        51, # Flute exchange
        58, # Gray's Mask
        59, # Triton's Mask
        64, # Mio's Hair
        65, # Noah Eyes
        66,
        67,
        68,
        69,
        72,
        73,
        77, # Temporary Blockage Before Fusion Arts (???)
        84
    ]
    
    # HD Ether Cylinders
    # Empowering Ino
    # Land of Challenge
    # Masha Accessory Crafting

    # Future Redeemed
    # Swap Char
    # Gem Craft
    # Affinity Growth
    # Unity Combo
    # Chain Attack
    # Unity Menu
    # Strengthen Weapons
    # Lure
    # Ladder building
    # X reader
    
    DLC4Systems = [87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102]
    
    # 8 Ouroborous Soul Tree

    for tut in tutFile.rows:
        if tut["$id"] in startingUnlocks:
            tut["Flag"] = 21022 # Flag set very early instantly unlocks 
    tutFile.Close()

def SetTipNotificationsOff(): # Barrage of notifications should be off by default if you unlock the systems
    notiFile = JSONParser.File("XC3/JsonOutputs/mnu/MNU_option_notice.json")
    notiFile.Alter(44, "default_value", 1)
    notiFile.Close()