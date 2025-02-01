import copy

import JSONParser, Helper, random, json, EnemyRandoLogic

from JSONParser import ALL

from IDs import ValidEnemyPopFileNames

#TODO: Things to check
# (✓) Does having blade Nia early break anything?
# (✓) Can I turn Driver Nia into Wulfric?
#     (X) Replace the text "Make Nia a Driver" with "Turn Wulfric into Nia"
#     (X) Replace the text "Make Nia a Blade" with "Turn Nia into Wulfric"
#     - Only do these if blade Nia was actually replaced with something that isn't Blade Nia
# (X) Blade names should be replaced in all dialogs
# (?) Blade quests (does godfrey still do his blade quest or does Pyra now do it? What is desired?)

#TODO: Bugs
# 4. Since it's based on poppiswap, Poppi has no abilities on her specials
# 5. No combination of Godfrey/Wulfric or Pyra/Nia's do the special tier 4.


#TODO: Things to try
# 3. Can I use poppiswap on Crossette to modify Poppi? (cannot be tested until Poppi and Crossette get arts for other characters)

# TODO: ChangeJSONFileWithCallback() could probably be renamed to be clearer.

# TODO: all functions which actually modify the tables should be renamed to start with "apply". This will differentiate between determining the calculations and applying them

# TODO: Shuffle the gacha blades for the Torna blades to make Mikhail accessible

OriginalBlades = dict()       # Maps Blade ID to the dictionary of the unrandomized blade date. Populated in PopulateBlades()
BladeNames = dict()           # Maps ID to Blade Name. Populated in PopulateBlades()
Original2Replacement = dict() # Maps Unrandomized Blade ID to Randomized Blade ID. Populated in RandomizeBlades()
Replacement2Original = dict() # Maps Randomized Blade ID to Unrandomized Blade ID. Populated in RandomizeBlades()
OriginalGacha = dict()        # Maps Gacha ID to Unrandomized Blade ID. Populated in PopulateGacha()

BladesRexCantUse = []
BladesNiaCantUse = [1001, 1002, 1009, 1010, 1011]
BladesMoragCantUse = [1001, 1002, 1010, 1011]
BladesZekeCantUse = [1001, 1002, 1009, 1011]

# Specifically, these are healers which have a healing halo equivalent move. So Twin Rings and Bitballs
# TODO: How does this work when considering randomized art effects?
GuaranteedHealer = None
RexHealerBlades = [1011]
NiaHealerBlades = [1004, 1021, 1033, 1038, 1041, 1107, 1109, 1111] # + Obrona if we can get NG+ Blades working without the weapon chip quirks
PossibleGuaranteedHealerBlades = RexHealerBlades + NiaHealerBlades

# TODO: Is this used?
PoppiForms = [1005, 1006, 1007]

# Note: Every Blade besides Roc is randomizable. Roc being randomized would mess up Vandham, and he's exclusive to Rex anyways so may as well keep it that way.
# The NG+ Exclusive blades cannot use weapon chips, so they cannot be randomized in Race Mode (where their chips are defined by the save file). Exclude those blades in Race Mode to account for this
BladesAlwaysRandomized = [1001, 1002, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1050, 1104, 1105, 1106, 1107, 1108, 1109, 1111]
NewGamePlusBlades = [1043, 1044, 1045, 1046, 1047, 1048, 1049] # Currently cannot be randomized, but I would like to figure this out eventually. Will be an option when that works though, because they would be unbalanced if you get them early on

def ModifyGachaAvailability(gacha):
    if gacha['Condition'] == 1789:  # NG+
        gacha['Condition'] = 0
    elif gacha['Condition'] == 3219:  # T-elos
        gacha['Condition'] = 0

def UnrelatedQolMods():
    # Make T-elos and Torna blades available in NG
    JSONParser.ChangeJSONLineWithCallback(["common/BLD_RareList.json"], ALL, ModifyGachaAvailability)
def InitialSetup():
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], ALL, PopulateBlades)
    JSONParser.ChangeJSONLineWithCallback(["common/BLD_RareList.json"], ALL, PopulateGacha)
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], ALL, MakeAllArtsAccessible)

# side is either L or R (case doesn't matter).
def WeaponType2Resource(weapon_type, side):
    TwoHandedWeapons = [3, 5, 7, 9, 16, 22, 23, 25, 26, 30, 32, 34, 35]

    base_string = 'wp' + str(weapon_type).zfill(2) + '0101'

    if weapon_type in TwoHandedWeapons:
        return base_string + '_' + side[0].lower()
    else:
        return base_string

def BladeRandomization(OptionsRunDict):
    #TODO: Use suboptions?
    #TODO: Include console messages

    UnrelatedQolMods()
    InitialSetup()

    BugFixes_PreRandomization()

    RandomizeBlades(OptionsRunDict)
    RandomizePoppiForms(OptionsRunDict) # TODO
    #RandomizeGachaTable(OptionsRunDict) # TODO: This is not needed now that all blades can be randomized. HOWEVER we still need to have something which replaces Dagas 1022 with Dagas 1050

    # Fix bug with Zeke? Bug is Zeke fight crashes if a randomized Pandoria has a non-default weapon chip
    #    In my case, I swapped Pandoria and Corvin. The Divine Core Crystal gave Pandoria, and I gave her a weapon between Zekes 1 and 2. Zeke 1 didn't crash, and he used Corvin's attacks. Zeke 2 crashes on startup
    #    Note: I thought of locking Pandoria to a side quest crystal which you get after fighting Zeke (Theory or Herald) but that doesn't work because you fight Zeke in chapter 10.
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_EnArrange.json"], ALL, ReplaceEnemyBlades)

    BugFixes_PostRandomization()

    FinalTouches()

    JSONParser.DebugTable(["common/BLD_RareList.json"])

def BugFixes_PreRandomization():
    # Replace Dagas 1022 with Dagas 1050 in gacha table. Since they are different blades, they could randomize weirdly.
    # For the purposes of this randomizer, 1022 is inaccessible
    JSONParser.ChangeJSONLine(["common/BLD_RareList.json"], [7], ['Blade'], 1050)

def ReplaceBlade(blade, replace_with_id):
    for key, value in blade.items():
        if key in ['$id', 'ReleaseLock']:
            continue
        blade[key] = copy.deepcopy(OriginalBlades[replace_with_id][key])

def ReplaceBlades(blade):
    id = blade['$id']
    if id in Original2Replacement:
        ReplaceBlade(blade, Original2Replacement[id])

def canBeReplaced(original, replacement, OptionsRunDict):
    # Handle the case of having the guaranteed healer
    if OptionsRunDict["Blades"]["subOptionObjects"]["Guarantee a Healer"]["subOptionTypeVal"].get():
        if (original == 1001 and GuaranteedHealer in RexHealerBlades) or \
           (original == 1004 and GuaranteedHealer in NiaHealerBlades):
            return replacement == GuaranteedHealer

    # Handle cases where arts wouldn't be defined for the replacement
    # Note: Rex can be the master driver, so it's fine if his blades get randomized to whoever.
    if original == 1004: # Dromarch
        return replacement not in BladesNiaCantUse
    if original in [1009, 1014]: #Brighid and Aegeaon
        return replacement not in BladesMoragCantUse
    if original == 1010: #Pandoria
        return replacement not in BladesZekeCantUse

    return True

def RandomizeBlades(OptionsRunDict):
    # Determine the guaranteed healer, if specified
    if OptionsRunDict["Blades"]["subOptionObjects"]["Guarantee a Healer"]["subOptionTypeVal"].get():
        global GuaranteedHealer

        # If Dromarch isn't randomized, he's the healer by default
        if not OptionsRunDict["Blades"]["subOptionObjects"]["Randomize Dromarch"]["subOptionTypeVal"].get():
            GuaranteedHealer = 1004
            print("The guaranteed healer is Dromarch (by default).")
        else:
            potential_healers = PossibleGuaranteedHealerBlades.copy()
            random.shuffle(potential_healers)
            GuaranteedHealer = potential_healers[0]
            print("The guaranteed healer is " + BladeNames[GuaranteedHealer])

    # Note: It is important that BladesLeftToRandomize starts with the default blades,
    # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
    blades_left_to_randomize = BladesAlwaysRandomized.copy()

    # Only add Dromarch to the pool if explicitly randomizing him
    if OptionsRunDict["Blades"]["subOptionObjects"]["Randomize Dromarch"]["subOptionTypeVal"].get():
        blades_left_to_randomize = [1004] + blades_left_to_randomize

    # TODO: Re-add this once NG+ blades' weapon chips work properly
    #if not OptionsRunDict["Blades"]["subOptionObjects"]["Include NG+ Blades"]["subOptionTypeVal"]:
    #    blades_left_to_randomize = blades_left_to_randomize + NewGamePlusBlades
    randomized_order = blades_left_to_randomize.copy()
    random.shuffle(randomized_order)

    # Determine the randomization prior to randomizing.
    # This way we can populate Original2Replacement and Replacement2Original,
    # which will be needed later on for various reasons
    while blades_left_to_randomize:
        next_blade = blades_left_to_randomize[0]
        next_replacement = randomized_order[0]
        if canBeReplaced(next_blade, next_replacement, OptionsRunDict):
            Original2Replacement[next_blade] = next_replacement
            Replacement2Original[next_replacement] = next_blade
            print('========================================')
            print(BladeNames[next_blade] + ' was replaced with ' + BladeNames[next_replacement])
            print(str(next_blade) + ' was replaced with ' + str(next_replacement))
            del blades_left_to_randomize[0]
            del randomized_order[0]
        else:
            # Next blade doesn't work, randomize again
            random.shuffle(randomized_order)

    # Apply Randomizations
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], ALL, ReplaceBlades)

def RandomizePoppiForms(OptionsRunDict):
    print('TODO: RandomizePoppiForms()')
    # TODO: Randomize Poppi
    # TODO: How do I make it so the poppiswaps are in the right spot

OriginalGacha2ReplacementBlade = dict()
def RandomizeGachaTable(OptionsRunDict):
    # TODO: repurpose this section to randomize Mikhail into the the gacha table. Or just add him to the table outright, that's also fine.
    # This Function exists to randomize gacha rows. Both the random gacha (Godfrey, Perceval, Vale, ...)
    # as well as predetermined gacha (Kasandra, Sheba, Herald, ...)
    # While it's true that blades like Corvin will already be randomized, this will further shuffle the
    # table so that blades can be received at different times.

    # Note: It is important that gacha_left_to_randomize starts with Aegeaon's row,
    # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
    gacha_left_to_randomize = [30] + [x for x in Helper.InclRange(1,29)] + [x for x in Helper.InclRange(31,37)]
    randomized_order = gacha_left_to_randomize.copy()
    random.shuffle(randomized_order)

    while gacha_left_to_randomize:
        this_gacha_row_id = gacha_left_to_randomize[0]
        replacement_gacha_row_id = randomized_order[0]

        # This row, the one being replaced
        this_row_unrandomized_gacha_blade = OriginalGacha[this_gacha_row_id]
        this_row_unrandomized_gacha_blade_name = BladeNames[this_row_unrandomized_gacha_blade]
        this_row_randomized_gacha_blade = Original2Replacement[this_row_unrandomized_gacha_blade]
        this_row_randomized_gacha_blade_name = BladeNames[this_row_randomized_gacha_blade]

        # The replacement row, which will overwrite this row
        replacement_row_unrandomized_gacha_blade = OriginalGacha[replacement_gacha_row_id]
        replacement_row_unrandomized_gacha_blade_name = BladeNames[replacement_row_unrandomized_gacha_blade]
        replacement_row_randomized_gacha_blade = Original2Replacement[replacement_row_unrandomized_gacha_blade]
        replacement_row_randomized_gacha_blade_name = BladeNames[replacement_row_randomized_gacha_blade]

        # Note: original replacement blade is used to set the blade ID in the table
        #       the randomized version of that blade is needed to check for valid replacements
        #       The only case where this matters is when the original unrandomized blade is Aegeaon.
        #       He is forced to Morag, so the replacement must be compatible with Morag
        if canBeReplaced(this_row_unrandomized_gacha_blade, replacement_row_randomized_gacha_blade, OptionsRunDict):
            OriginalGacha2ReplacementBlade[this_gacha_row_id] = replacement_row_unrandomized_gacha_blade
            print('===========================================')
            print('gacha blade ' + this_row_randomized_gacha_blade_name + ' (originally ' + this_row_unrandomized_gacha_blade_name + ') was replaced with ' + replacement_row_randomized_gacha_blade_name + ' (originally ' + replacement_row_unrandomized_gacha_blade_name + ')')
            print('gacha blade ' + str(this_row_randomized_gacha_blade) + ' (originally ' + str(this_row_unrandomized_gacha_blade) + ') was replaced with ' + str(replacement_row_randomized_gacha_blade) + ' (originally ' + str(replacement_row_unrandomized_gacha_blade) + ')')
            print('===========================================')
            del gacha_left_to_randomize[0]
            del randomized_order[0]
        else:
            # Next blade doesn't work, randomize again
            random.shuffle(randomized_order)

    JSONParser.ChangeJSONLineWithCallback(["common/BLD_RareList.json"], ALL, ReplaceGacha)

def ReplaceGacha(gacha):
    gacha['Blade'] = OriginalGacha2ReplacementBlade[gacha['$id']]

def ReplaceEnemyBlades(enemy):
    if enemy['BladeID'] in Replacement2Original:
        print("Enemy: " + BladeNames[enemy['BladeID']] + " (" + str(enemy['BladeID']) + ") was replaced with " + BladeNames[Replacement2Original[enemy['BladeID']]] + " (" + str(Replacement2Original[enemy['BladeID']]) + ")")
        enemy['BladeID'] = Replacement2Original[enemy['BladeID']]

def MakeAllArtsAccessible(art):
    # Sets all arts to be unlocked at level 1.
    # In a normal playthrough, these arts only really matter for Broadsword and Aegis Sword, as those
    # are the only weapons can possibly use this early. However, a handful of arts have high enough
    # requirements that Rex can't use it if randomization gives him something like Brighid or Pandoria
    # early on. For simplicity and potential future-proofing, just set all arts to level 1 besides the
    # Broadsword. It is desirable that the Junk Sword still behaves as intended prior to Rex getting
    # his first blade.
    if art['WpnType'] not in [17]: # Broadsword
        for i in Helper.InclRange(1,5):
           art['ReleaseLv' + str(i)] = 1



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

    Name = ''
    name_id = blade['Name']
    def getName(row):
        nonlocal Name
        Name = row['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/chr_bl_ms.json"], [name_id], getName)

    BladeNames[id] = Name

def PopulateGacha(gacha):
    if gacha['Blade'] == 1022: # Replace Original Dagas with True Dagas in the table
        OriginalGacha[gacha['$id']] = 1050
    else:
        OriginalGacha[gacha['$id']] = gacha['Blade']

def BugFixes_PostRandomization():
    JSONParser.ChangeJSONLineWithCallback(["common/EVT_cutscene_wp.json"], ALL, FixCutsceneCrashForNotHavingTwoWeapons)
    FixPandoriaSpriteAfterElpys()

# When swapping blade, there is a bug where cutscenes will crash when attempting to load. This is caused because in two ways
# 1. A blade which uses dual-wield weapons is replaced with a blade which does not. The cutscene tries to load the offhand
#    weapon, which does not exist, and so the game crashes
# 2. A blade's weapon has a special animation or model which the replaced weapon does not support. For example, Brighid's
#    whipsword has special properties due to how it extends. Replacing this with a different weapon can cause crashes.
# To fix these bugs, this cutscene replaces all weapon resources with the weapons of the original blade who was supposed
# to appear in that cutscene. For safety, all single-hand weapons are written to both the left and right hand resource
# slots to ensure things are always defined.
def FixCutsceneCrashForNotHavingTwoWeapons(cutscene):
    original = cutscene['blade']

    # Bail if this blade was not randomized
    if original not in Original2Replacement:
        return

    # Replace resources with weapon type of the blade who replaced the original
    replacement = Original2Replacement[original]
    cutscene['resourceL'] = WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'L')
    cutscene['resourceR'] = WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'R')


def FixPandoriaSpriteAfterElpys():
    # Get the still of the blade which replaced Pandoria
    pandoria_replacement_still = OriginalBlades[Original2Replacement[1010]]['Still']

    # Use the still to find the icon index of the blade which replaced Pandoria
    icon_index = JSONParser.QuerySingleRow("common/MNU_IconList.json", "$id", pandoria_replacement_still)["icon_index"]

    # Fix the small icon for Pandoria's replacement
    # Note: Row 261 corresponds to Pandoria's icon with transparent glasses
    #def PandoriaGlassesFixIcon(icon):
    #    icon['icon_index'] = icon_index
    #JSONParser.ChangeJSONLineWithCallback(["common/MNU_IconList.json"], [261], PandoriaGlassesFixIcon)
    JSONParser.ChangeJSONLine(["common/MNU_IconList.json"], [261], ['icon_index'], icon_index)

    # Get the blade image for Pandoria's replacement
    # This includes both the File ID and scaling/cropping information of the image
    PandoriaReplacementImageRow = JSONParser.QuerySingleRow("common/MNU_BlImageID.json", "icon_id", pandoria_replacement_still)

    # Grab the file name from the File ID
    fileName = JSONParser.QuerySingleRow("common/MNU_Stream_full_bl.json", "$id", PandoriaReplacementImageRow['$id'])['filename']

    # Replace the image for Pandoria with her replacement's image
    # Note: Row 50 corresponds to Pandoria's portrait with transparent glasses
    #def PandoriaGlassesFixPortraitFile(image):
    #    image['filename'] = fileName  # 'fim_bl_053' # Okay for sure this one is Vale
    #JSONParser.ChangeJSONLineWithCallback(["common/MNU_Stream_full_bl.json"], [50], PandoriaGlassesFixPortraitFile)
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_bl.json"], [50], ['filename'], fileName)


    # Fix the cropping of the image of Pandoria's replacement
    # Note: Row 50 corresponds to Pandoria's portrait with transparent glasses
    #def PandoriaGlassesFixPortraitCropping(image):
    #    for field in ['offs_x', 'offs_y', 'scale',
    #                  'offs_x2', 'offs_y2', 'scale2',
    #                  'offs_x3', 'offs_y3', 'scale3',
    #                  'offs_x4', 'offs_y4', 'scale4',
    #                  'offs_x5', 'offs_y5', 'scale5']:
    #        image[field] = PandoriaReplacementImageRow[field]
    #JSONParser.ChangeJSONLineWithCallback(["common/MNU_BlImageID.json"], [50], PandoriaGlassesFixPortraitCropping)
    for field in ['offs_x', 'offs_y', 'scale',  'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine(["common/MNU_BlImageID.json"], [50], [field], PandoriaReplacementImageRow[field])



def FinalTouches():
    print('FinalTouches')
    # common_ms/menu_tutorial.html:
    # ID 320 name is "Nia has unleashed her true power! Now Rex can [System:Color name=tutorial ]engage Nia as a Blade[/System:Color]."
    # ID 344 name is "When you want to engage Nia as a Blade, go to [System:Color name=tutorial ]Main Menu[/System:Color] > [System:Color name=tutorial ]Characters[/System:Color], [System:Color name=tutorial ]then select the Driver Nia and press [ML:icon icon=Y ][/System:Color]."
    # ID 345 name is "When you want to travel with Nia in her Driver form, go to [System:Color name=tutorial ]Main Menu[/System:Color] > [System:Color name=tutorial ]Characters[/System:Color], [System:Color name=tutorial ]then select the Blade Nia and press [ML:icon icon=Y ][/System:Color]."
    # IDs 401-403 talks about the Pyra/Nia special. Replace this with something saying that it doesn't work
    # Various IDs mention other blades such as Poppibuster, Shulk, Fiora, and Elma
    # 497: "Players who use Nia in her Blade form may have to return her to Driver form to be able to use Fiora as a Blade."
    # Honestly, just comb this whole file searching for the name of any blade

    # common/MNU_CmnWindow.html
    # 183-188 are pyra/mythra/nia things
    #223 has Nia

    #TODO: Can I just loop over each table of interest, search for each blade name, and replace that string if it exists?