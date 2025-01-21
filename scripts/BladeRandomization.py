import JSONParser, Helper, random, json, EnemyRandoLogic

from IDs import ValidEnemyPopFileNames

#TODO: Things to check
# (✓) Blades should be swapped in cutscenes
# (✓) Blades should be swapped in overworld (IE Fan's ship after chapter 4)
# (✓) Affinity Trees are swapped
# (✓) Rex starts with Godfrey (chapter 1)
# (✓) Kasandra can swap with Godfrey in the menu after chapter 4
#     (X) The text says "Switch to Godfrey" instead of "Switch to Pyra"
# (✓) Divine Core Crystal gives Pandoria (Of note, this is the one with glasses in the menu. It's the one with the hood ingame)
# (✓) Kassandra replaces Mythra vs Makhos
#     (✓) Kassandra gets the Mythra buff for this fight
# (✓) Zeke uses Corvin instead of Pandoria as an enemy? (this would be cool)
# (✓) Zeke starts with Corvin (Chapter 5)
# (✓) Ebullient Core Crystal gives Poppi Alpha
# (✓) Tora starts with Crossette (Chapter 2)
# (✓) Heart to Hearts use the new blades
# (✓) Favorite Pouch Items are preserved between blades (Pyra still likes Jenerosi Tea)
# (✓) Number of aux core slots are preserved between blades
# (✓) Does having blade Nia early break anything?
# (✓) Can I turn Driver Nia into Wulfric?
#     (X) Replace the text "Make Nia a Driver" with "Turn Wulfric into Nia"
#     (X) Replace the text "Make Nia a Blade" with "Turn Nia into Wulfric"
#     - Only do these if blade Nia was actually replaced with something that isn't Blade Nia
# (✓) Can you properly release the gacha blades but not the main party blades?
# (X) Do cosmetics still work correctly
# (✓) Merc group names
# (X) Blade names should be replaced in all dialogs
# (✓) Blade art gallery should show modified blades with their correct VAs
# (?) Blade quests (does godfrey still do his blade quest or does Pyra now do it? What is desired?)
# (✓) Can Zeke use Eye of Shining Justice with Corvin?
#     (X) Description of the skill should say "Corvin" instead of "Pandoria"
# (✓) Crossette can get full affinity in Elpys (instead of Poppi)
# (✓) Godfrey/Kasandra should be able to turn into Pneuma
# (✓) When viewing an Awakening cutscene, the "flash" before summoning should be the correctly summoned blade


#TODO: Bugs
# 1. Rex cannot use Poppi arts (obviously)
# 1a. When switching off of Poppi, Rex still can not attack (even with Godfrey)
# 2. Using an unsupported blade (Crossette on Tora for example) during a chain attack causes a softlock
# 3. After the scene in Elpys where Pandoria's glasses become transparent, Corvin's sprite in the menu (and only the menu) becomes Pandoria again (with the transparent glasses). Everything else is still Corvin
# 3a. After this scene, Corvin should still appear as Corvin. Pandoria (on Rex) should now appear with transparent glasses
# 4. Since it's based on poppiswap, Poppi has no abilities on her specials
# 4a. Special description should say something like "Set Crossette's Poppiswap". Reference the original wording
# 5. No combination of Godfrey/Wulfric or Pyra/Nia's do the special tier 4.


#TODO: Things to try
# 1. Add a cosmetic item for Pandoria's hooded form
# 2. If Pyra was not randomized to a tank, make sure Poppi gets randomized to a tank. Otherwise, Poppi can be whatever. Basically, make sure there is at least one tank.
# 3. Can I use poppiswap on Crossette to modify Poppi? (cannot be tested until Poppi and Crossette get arts for other characters)
# 4a. Can I modify the menu to put Poppiswap on Poppi so Tora doesn't have the poppiswap anymore?
# 5. Rename items which summon blades. For example, if Kasandra becomes Mythra, then rename "Lucky Core Crystal" to "Aegis Core Crystal" or something
# 6. Can Pneuma be randomized? I think she's too broken to have normally, but we could nerf her and buff whoever replaces her


# Hardcode a few swaps for now for initial testing
Pyra = 1001
Godfrey = 1015

Mythra = 1002
Kasandra = 1023

Pandoria = 1010 # There is another Pandoria (1076) which appears to be hooded Pandoria from that one cutscene
Corvin = 1108

Crossette = 1109
PoppiAlpha = 1005

Wulfric = 1016
BladeNia = 1011

OriginalBlades = dict()

def DefaultBladeRandomization(OptionsRunDict):
    #TODO: Use the suboptions
    #TODO: Rename this functions (and others) accordingly
    #TODO: Include console messages

    #TODO: Modify ChangeJSONLineWithCallback() to make the list of IDs optional. If empty, process the callback on all items

    # Speed boost TODO (not part of this feature, but is useful for testing.
    JSONParser.ChangeJSONLineWithCallback(["common/FLD_OwnerBonus.json"], [24], FullSpeedAhead)
    JSONParser.ChangeJSONLineWithCallback(["common/FLD_QuestReward.json"], [151], GimmeThatSpeed)

    # Note: Includes Poppi forms (1005, 1006, and 1007)
    # Note: Blades can only be swapped with other blades of the same Race. Some blades with weird shapes (Dromarch, Roc, Boreas, Ursula, Sheba, Herald, and Sever) cannot be randomized
    AllHumanoidBlade = [1001, 1002, 1005, 1006, 1007, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1076, 1104, 1105, 1106, 1107, 1108, 1109, 1111]

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], Helper.InclRange(1, 1000), MakeAllArtsAccessible)

    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], AllHumanoidBlade, PopulateBlades)
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], AllHumanoidBlade, ReplaceBlades) # TODO: Replace with actual randomization

    JSONParser.ChangeJSONLineWithCallback(["common/BLD_RareList.json"], [1], ModifyGachaProbabilityToMakeGuaranteed) # TODO: So I can get Pyra from the gacha for testing


    # Fix bug with Zeke? Bug is Zeke fight crashes if a randomized Pandoria has a non-default weapon chip
    #    In my case, I swapped Pandoria and Corvin. The Divine Core Crystal gave Pandoria, and I gave her a weapon between Zekes 1 and 2. Zeke 1 didn't crash, and he used Corvin's attacks. Zeke 2 crashes on startup
    #    Note: I thought of locking Pandoria to a side quest crystal which you get after fighting Zeke (Theory or Herald) but that doesn't work because you fight Zeke in chapter 10.
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_EnArrange.json"], Helper.InclRange(1,2000), ReplaceEnemyBlades)

def ReplaceEnemyBlades(enemy):
    # TODO: Do this with all blades
    if enemy['BladeID'] == Pandoria:
        enemy['BladeID'] = Corvin

def MakeAllArtsAccessible(art):
    art['ReleaseLv1'] = 1
    art['ReleaseLv2'] = 1
    art['ReleaseLv3'] = 1
    art['ReleaseLv4'] = 1
    art['ReleaseLv5'] = 1

def FullSpeedAhead(deed): # increases movement speed from the deed
    deed['Value'] = 10000

def GimmeThatSpeed(rewards): # rewards the movement deed in the tutorial
    rewards['ItemID1'] = 25272
    rewards['ItemNumber1'] = 5

def ModifyGachaProbabilityToMakeGuaranteed(gacha):
    gacha['Prob1'] = 100
    gacha['Prob2'] = 100
    gacha['Prob3'] = 100
    gacha['Prob4'] = 100
    gacha['Prob5'] = 100

def PopulateBlades(blade):
    id = blade['$id']
    OriginalBlades[id] = dict()
    for key, value in blade.items():
        OriginalBlades[id][key] = blade[key]

def ReplaceBlade(blade, replace_with_id):
    for key, value in blade.items():
        if key in ['$id', 'ReleaseLock', 'CreateEventId']:
            continue
        blade[key] = OriginalBlades[replace_with_id][key]

def MoveMythrasCosmeticsToKassandra(accessory):
    # TODO: Do this for all cosmetics
    # TODO: Find the ID for Melee Mythra. Perhaps replace all aux core names with their ID so we can find it easier
    accessory['Blade'] = Kasandra

def ReplaceBlades(blade):
    # TODO: Replace with randomness

    # Swap Pyra and Godfrey
    if blade['$id'] == Pyra:
        ReplaceBlade(blade, Godfrey)
    elif blade['$id'] == Godfrey:
        ReplaceBlade(blade, Pyra)

    # Swap Mythra and Kassandra
    # Note: The blades which replace Pyra/Mythra should have the same weapons because arts are shared between them
    elif blade['$id'] == Mythra:
        ReplaceBlade(blade, Kasandra)
    elif blade['$id'] == Kasandra:
        ReplaceBlade(blade, Mythra)
        mythra_cosmetics = [17409, 17414, 17419]  # TODO: Need to find Massive Melee Mythra, not in the bdats
        JSONParser.ChangeJSONLineWithCallback(["common/ITM_OrbEquip.json"], mythra_cosmetics, MoveMythrasCosmeticsToKassandra)

    # Swap Pandoria and Corvin
    elif blade['$id'] == Pandoria:
        ReplaceBlade(blade, Corvin)
    elif blade['$id'] == Corvin:
        ReplaceBlade(blade, Pandoria)

    # Swap Crossette and Poppi Alpha
    elif blade['$id'] == Crossette:
        ReplaceBlade(blade, PoppiAlpha)
    elif blade['$id'] == PoppiAlpha:
        ReplaceBlade(blade, Crossette)

    # Swap Wulfric and Blade Nia
    elif blade['$id'] == Wulfric:
        ReplaceBlade(blade, BladeNia)
    elif blade['$id'] == BladeNia:
        ReplaceBlade(blade, Wulfric)
