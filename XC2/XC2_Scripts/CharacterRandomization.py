import copy, random
from XC2.XC2_Scripts import Options
from scripts import JSONParser, Helper, PopupDescriptions

# TODO (blades):
#  - Replace the images in the Pyra/Mythra selection to the blades which replaced them
#  - Figure out how to randomize Torna blades properly (Apparently NoBuildWpn in CHR_Bl is not sufficient)
#  - Blade names should be replaced in all dialogs where possible (nice to have)
#  - Replace driver voice lines when changing blades (Rex will currently shout "Pyra" when switching to Pyra's replacement)
#  - Replace field skill voice lines (Pyra's replacement currently says "I bring upon the power of fire!" in Pyra's voice)
#  - Only do the Pandoria glasses fix if Pandoria is actually randomized
#  - Could Pandoria's glasses overworld model still be used if we apply a condition? Currently a condition isn't used, so I'm not sure how that cosmetic model gets applies

# TODO: (drivers)
#  - Voice lines in the menu (such as when spending affinity tokens) is still the original driver's voice
#  - Voice lines after combat ("Not to boast, but that was spectacular! Right gramps?") is still in the original driver's voice
#  - Replace driver names in all dialog text (nice to have)

OriginalCharacters = dict()            # Maps Driver/Blade ID to the dictionary of the unrandomized driver/blade data. Populated in PopulateDrivers() and PopulateBlades()
CharacterNames = dict()                # Maps ID to Driver/Blade Name. Populated in PopulateDrivers() and PopulateBlades()
OriginalCharacter2Replacement = dict() # Maps Unrandomized Driver/Blade ID to Randomized Driver/Blade ID. Populated in RandomizeDrivers() and PopulateBlades()
ReplacementCharacter2Original = dict() # Maps Randomized Driver/Blade ID to Unrandomized Driver/Blade ID. Populated in RandomizeDrivers() and PopulateBlades()

DriversToRandomize = [1, 2, 3, 6]

DriverToLockedBlades = {
    1: [1001, 1002, 1011], # Rex has Pyra, Mythra, and Nia
    2: [1004], # Nia has Dromarch
    3: [1010], # Zeke has Pandoria
    6: [1009, 1014] # Morag has Brighid and Aegaeon
}

LockedBladeToDriver = {
    1001: 1,
    1002: 1,
    1011: 1,
    1004: 2,
    1010: 3,
    1009: 6,
    1014: 6
}

BladesDriverCantUse = {
    1: [], # Rex can use everyone
    2: [1001, 1002, 1009, 1010, 1011], # Nia can't use Pyra, Mythra, Brighid, Pandoria, and Nia
    3: [1001, 1002, 1009, 1011], # Zeke can't use Pyra, Mythra, Brighid, and Nia
    6: [1001, 1002, 1010, 1011], # Morag can't use Pyra, Mythra, Pandoria, and Nia
}

# Specifically, these are healers which have a healing halo equivalent move.
# The guaranteed Healer must belong to the driver who replaced NIA
GuaranteedHealer = None
PossibleHealerBladesForEachDriver = {
    1: [1011],
    2: [1004, 1021, 1033, 1038, 1041, 1107, 1109, 1111], # + Obrona and Mikhail if we can get NG+ Blades working without the weapon chip quirks
    3: [], # Zeke does not have a healing halo art.
    6: [1004, 1021, 1033, 1038, 1041, 1107, 1109, 1111] # + Obrona and Mikhail if we can get NG+ Blades working without the weapon chip quirks
}
PossibleHealerBlades = list(set(PossibleHealerBladesForEachDriver[1] + PossibleHealerBladesForEachDriver[2] + PossibleHealerBladesForEachDriver[3] + PossibleHealerBladesForEachDriver[6]))

PoppiForms = [1005, 1006, 1007]

# Note: Every Blade besides Roc is randomizable. Roc being randomized would mess up Vandham, and he's exclusive to Rex anyway so may as well keep it that way.
# The NG+ Exclusive blades cannot use weapon chips, so they cannot be randomized in Race Mode (where their chips are defined by the save file). Exclude those blades in Race Mode to account for this
BladesAlwaysRandomized = [1001, 1002, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1050, 1104, 1105, 1106, 1107, 1108, 1109, 1111]
NewGamePlusBlades = [1043, 1044, 1045, 1046, 1047, 1048, 1049] # Currently cannot be randomized, but I would like to figure this out eventually. Will be an option when that works though, because they would be unbalanced if you get them early on

first_character_randomization = True # Both drivers and blade options call this same function. Only run this logic once

randomize_drivers = False
randomize_blades = False

include_printouts = False  # Debugging


def resetGlobals():
    global GuaranteedHealer
    global first_character_randomization
    global randomize_drivers
    global randomize_blades

    OriginalCharacters.clear()
    CharacterNames.clear()
    OriginalCharacter2Replacement.clear()
    ReplacementCharacter2Original.clear()
    GuaranteedHealer = None
    first_character_randomization = True
    randomize_drivers = False
    randomize_blades = False


def CharacterRandomization():
    # Make sure this logic is called only once
    global first_character_randomization
    if first_character_randomization:
        first_character_randomization = False
    else:
        return

    global randomize_drivers
    global randomize_blades
    randomize_drivers = Options.DriversOption.GetState()
    randomize_blades = Options.BladesOption.GetState()

    # Disable driver randomization if custom mode is used
    if Options.RaceModeOption.GetState():
        print("Driver randomization is not supported in Race Mode")
        randomize_drivers = False
    if Options.UMHuntOption.GetState():
        print("Driver randomization is not supported in UM Hunt")
        randomize_drivers = False

    if include_printouts:
        print("Character Randomization: ")
        print("\tRandomize Drivers: " + str(randomize_drivers))
        print("\t\tGuarantee Early Nia: " + str(Options.DriversOption_Nia.GetState()))
        print("\tRandomize Blades: " + str(randomize_blades))
        print("\t\tRandomize Dromarch: " + str(Options.BladesOption_Dromarch.GetState()))
        print("\t\tGuarantee Healer: " + str(Options.BladesOption_Healer.GetState()))

    InitialSetup()

    # Note: This is explicitly needed before both driver and blade randomization
    #       Drivers need this logic because Zeke does not have any healers, so he cannot replace Nia if healers are guaranteed
    DetermineGuaranteedHealer()

    BugFixes_PreRandomization()
    RandomizeDrivers()
    RandomizeBlades()
    BugFixes_PostRandomization()


def FreeEngage(): # If Blade Rando is on, we want to be able to move blades around freely to avoid bugs
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_DlcGift.json", ["FreeEngage"], "1")


def InitialSetup():
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], [], PopulateDrivers, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], PopulateBlades, replaceAll=True)


def PopulateDrivers(driver):
    driver_id = driver['$id']
    OriginalCharacters[driver_id] = dict()
    for key, value in driver.items():
        OriginalCharacters[driver_id][key] = copy.deepcopy(driver[key])

    Name = ''
    name_id = driver['Name']

    def getName(row):
        nonlocal Name
        Name = row['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/chr_dr_ms.json"], [name_id], getName)

    CharacterNames[driver_id] = Name


def PopulateBlades(blade):
    blade_id = blade['$id']
    OriginalCharacters[blade_id] = dict()
    for key, value in blade.items():
        OriginalCharacters[blade_id][key] = copy.deepcopy(blade[key])

    Name = ''
    name_id = blade['Name']

    def getName(row):
        nonlocal Name
        Name = row['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/chr_bl_ms.json"], [name_id], getName)

    CharacterNames[blade_id] = Name


def DetermineGuaranteedHealer():
    if randomize_blades and Options.BladesOption_Healer.GetState():
        global GuaranteedHealer

        # If Dromarch isn't randomized, he's the healer by default
        if randomize_blades and not Options.BladesOption_Dromarch.GetState():
            GuaranteedHealer = 1004
            if include_printouts:
                print("The guaranteed healer is Dromarch (by default).")
        else:
            # If Nia isn't randomized, make sure the healer is one of hers
            # Otherwise, pick any of the possible healers for any driver
            if randomize_drivers and Options.DriversOption_Nia.GetState():
                potential_healers = PossibleHealerBladesForEachDriver[2].copy()
            else:
                potential_healers = PossibleHealerBlades.copy()
            random.shuffle(potential_healers)
            GuaranteedHealer = potential_healers[0]
            if include_printouts:
                print("The guaranteed healer is " + CharacterNames[GuaranteedHealer])


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


def BugFixes_PreRandomization():
    if randomize_blades:
        # Replace Dagas 1022 with Dagas 1050 in gacha table. Since they are different blades, they could randomize weirdly.
        # For the purposes of this randomizer, 1022 is inaccessible
        JSONParser.ChangeJSONLine(["common/BLD_RareList.json"], [7], ['Blade'], 1050)


def RandomizeDrivers():
    if randomize_drivers:
        drivers_left_to_randomize = DriversToRandomize.copy()

        randomized_order = drivers_left_to_randomize.copy()
        random.shuffle(randomized_order)

        # Two conditions might be required for the randomized driver order to be valid:
        # 1. If Guarantee Early Nia is set, she must be one of the first two drivers
        # 2. If there is a guaranteed healer, make sure they're in Nia's spot (index 1)
        # Keep shuffling until that happens
        def niaSettingIsSatisfied():
            return (not Options.DriversOption_Nia.GetState()) or (randomized_order[0] == 2 or randomized_order[1] == 2)
        def healerSettingIsSatisfied():
            return (GuaranteedHealer is None) or (GuaranteedHealer in PossibleHealerBladesForEachDriver[randomized_order[1]])
        while not (niaSettingIsSatisfied() and healerSettingIsSatisfied()):
            if include_printouts:
                if not niaSettingIsSatisfied():
                    print("Nia was set to show up early, but the first two drivers were %s and %s. Reshuffling drivers..." % (CharacterNames[randomized_order[0]], CharacterNames[randomized_order[1]]))
                elif not healerSettingIsSatisfied():
                    print("The guaranteed healer was %s but Nia was randomized to %s. Reshuffling drivers..." % (CharacterNames[GuaranteedHealer], CharacterNames[randomized_order[1]]))
            random.shuffle(randomized_order)

        # Determine the randomization prior to randomizing.
        # This way we can populate Original2Replacement and Replacement2Original,
        # which will be needed later on for various reasons
        while drivers_left_to_randomize:
            next_driver = drivers_left_to_randomize[0]
            next_replacement = randomized_order[0]

            OriginalCharacter2Replacement[next_driver] = next_replacement
            ReplacementCharacter2Original[next_replacement] = next_driver
            if include_printouts:
                print('========================================')
                print(CharacterNames[next_driver] + ' was replaced with ' + CharacterNames[next_replacement])
                print(str(next_driver) + ' was replaced with ' + str(next_replacement))
            del drivers_left_to_randomize[0]
            del randomized_order[0]

        # Apply Randomizations
        JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], [], ApplyDriverRandomization, replaceAll=True)

        CreatePneumaReplacement()

    # No randomization, populate the maps with no swaps
    else:
        for driver_id in DriversToRandomize:
            OriginalCharacter2Replacement[driver_id] = driver_id
            ReplacementCharacter2Original[driver_id] = driver_id


def RandomizeBlades():
    if randomize_blades:
        # Note: It is important that BladesLeftToRandomize starts with the default blades,
        # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
        blades_left_to_randomize = BladesAlwaysRandomized.copy()

        # Only add Dromarch to the pool if explicitly randomizing him
        if Options.BladesOption_Dromarch.GetState():
            blades_left_to_randomize = [1004] + blades_left_to_randomize

        # TODO: Re-add this once NG+ blades' weapon chips work properly
        # if not OptionsRunDict["Blades"]["subOptionObjects"]["Include NG+ Blades"]["subOptionTypeVal"]:
        #    blades_left_to_randomize = blades_left_to_randomize + NewGamePlusBlades
        randomized_order = blades_left_to_randomize.copy()
        random.shuffle(randomized_order)

        # Determine the randomization prior to randomizing.
        # This way we can populate Original2Replacement and Replacement2Original,
        # which will be needed later on for various reasons
        while blades_left_to_randomize:
            next_blade = blades_left_to_randomize[0]
            next_replacement = randomized_order[0]
            if bladeCanBeReplaced(next_blade, next_replacement):
                OriginalCharacter2Replacement[next_blade] = next_replacement
                ReplacementCharacter2Original[next_replacement] = next_blade
                if include_printouts:
                    print('========================================')
                    print(CharacterNames[next_blade] + ' was replaced with ' + CharacterNames[next_replacement])
                    print(str(next_blade) + ' was replaced with ' + str(next_replacement))
                del blades_left_to_randomize[0]
                del randomized_order[0]
            else:
                # Next blade doesn't work, randomize again
                random.shuffle(randomized_order)

        # Apply Randomizations
        JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], ApplyBladeRandomization, replaceAll=True)

        RandomizePoppiForms()
    else:
        # Make the default blades compatible if blades are not being randomized
        SwapDefaultBlades()

def bladeCanBeReplaced(original_blade, replacement_blade):
    # If blade isn't originally locked to a driver, anyone can replace them
    if original_blade not in LockedBladeToDriver:
        return True

    blades_original_driver = LockedBladeToDriver[original_blade]
    blades_replacement_driver = OriginalCharacter2Replacement[blades_original_driver]

    # Handle the case of having the guaranteed healer
    if randomize_blades and Options.BladesOption_Healer.GetState():
        if original_blade == 1004 and GuaranteedHealer in PossibleHealerBladesForEachDriver[OriginalCharacter2Replacement[blades_original_driver]]:
            if replacement_blade != GuaranteedHealer:
                if include_printouts:
                    print("%s cannot be replaced with %s" % (CharacterNames[original_blade], CharacterNames[replacement_blade]))
                    print("\tRandomized blade is %s. Expected healer blade is %s." % (CharacterNames[replacement_blade], CharacterNames[GuaranteedHealer]))
                    print("\tDriver is %s (originally %s)" % (blades_replacement_driver, CharacterNames[blades_original_driver]))
                return False

    # Handle cases where arts wouldn't be defined for the replacement
    if replacement_blade in BladesDriverCantUse[blades_replacement_driver]:
        if include_printouts:
            print("%s cannot be replaced with %s" % (CharacterNames[original_blade], CharacterNames[replacement_blade]))
            print("\tDriver is %s (originally %s)" % (CharacterNames[blades_replacement_driver], CharacterNames[blades_original_driver]))
        return False

    return True


def CreatePneumaReplacement():
    # Replace Pneuma with the new character's default blade with an actually strong weapon
    # Note: Pneuma's "Model" and "DefWeapon" fields are explicitly ignored in ApplyBladeRandomization()
    match OriginalCharacter2Replacement[1]:
        case 1: # Rex was not replaced
            if include_printouts:
                print("Since Rex was not replaced:")
                print("- Pneuma remains unchanged.")
                print("- No core crystals were renamed")
        case 2: # Rex Replaced by Nia
            if include_printouts:
                print("Since Rex was replaced by Nia:")
                print("- Replaced Pneuma with Savage Dromarch with the Meteorite Rings")
            OriginalCharacter2Replacement[1003] = 1004
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100501")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5179) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
        case 3: # Rex replaced by Zeke
            if include_printouts:
                print("Since Rex was replaced by Zeke:")
                print("- Replaced Pneuma with Mermaid Blue Pandoria with the Meteorite Edge")
            OriginalCharacter2Replacement[1003] = 1010
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100901")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5479) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
        case 6: # Rex Replaced by Morag
            if include_printouts:
                print("Since Rex was replaced by Morag:")
                print("- Replaced Pneuma with Jade Orchid Brighid with the Meteorite Whips")
            OriginalCharacter2Replacement[1003] = 1009
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl121001")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5419) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma


def SwapDefaultBlades():
    # Pyra, Dromarch, Brighid, and Pandoria can be handled as simple swaps.
    # Roc needs to stay because of Vandham
    # Blade Nia will stay for convenience. But whoever replaces Rex will not be able to use her
    # Mythra's replacement is as follows:
    #  - If Nia replaced Rex, Mythra should become Crossette
    #  - If Morag replaced Rex, Mythra should become Corvin
    #  - If Zeke replaced Rex, Mythra should become Wulfric
    #  - In each of these cases, the core crystals items which contain these blades should also be renamed to "Aegis core crystal", as they now contain Mythra
    # Pneuma is replaced with a "custom" blade, which is an "Ascended" version of either Dromarch, Brighid, or Pandoria.

    original_driver_to_primary_blade = {
        1: 1001, # Rex to Pyra
        2: 1004, # Nia to Dromarch
        3: 1010, # Zeke to Pandoria
        6: 1009, # Morag to Brighid
    }
    original_driver_to_secondary_blades = {
        1: 1002, # Rex to Mythra
        2: 1109, # Nia to Crossette
        3: 1016, # Zeke to Wulfric
        6: 1108, # Morag to Corvin
    }

    # Swap primary blades for all drivers
    for original_driver_id in DriversToRandomize:
        replacement_driver_id = OriginalCharacter2Replacement[original_driver_id]

        original_blade_id = original_driver_to_primary_blade[original_driver_id]
        replacement_blade_id = original_driver_to_primary_blade[replacement_driver_id]

        OriginalCharacter2Replacement[original_blade_id] = replacement_blade_id
        ReplacementCharacter2Original[replacement_blade_id] = original_blade_id

        if include_printouts:
            print('========================================')
            print(CharacterNames[original_blade_id] + ' was replaced with ' + CharacterNames[replacement_blade_id])
            print(str(original_blade_id) + ' was replaced with ' + str(replacement_blade_id))

    # Swap Mythra (and only Mythra) with the secondary blades
    # Only bother if Rex was randomized
    if OriginalCharacter2Replacement[1] != 1:
        original_driver_id = 1 # Rex
        replacement_driver_id = OriginalCharacter2Replacement[original_driver_id]

        original_blade_id = original_driver_to_secondary_blades[original_driver_id] # Mythra
        replacement_blade_id = original_driver_to_secondary_blades[replacement_driver_id]

        OriginalCharacter2Replacement[original_blade_id] = replacement_blade_id
        OriginalCharacter2Replacement[replacement_blade_id] = original_blade_id
        ReplacementCharacter2Original[original_blade_id] = replacement_blade_id
        ReplacementCharacter2Original[replacement_blade_id] = original_blade_id

        if include_printouts:
            print('========================================')
            print(CharacterNames[original_blade_id] + ' was replaced with ' + CharacterNames[replacement_blade_id])
            print(str(original_blade_id) + ' was replaced with ' + str(replacement_blade_id))
            print('========================================')
            print(CharacterNames[replacement_blade_id] + ' was replaced with ' + CharacterNames[original_blade_id])
            print(str(replacement_blade_id) + ' was replaced with ' + str(original_blade_id))

    # Also Rename the core crystal which now contains Mythra (if Mythra was swapped above)
    match OriginalCharacter2Replacement[1]:
        case 1: # Rex was not replaced
            if include_printouts:
                print("Since Rex was not replaced:")
                print("- No core crystals were renamed")
        case 2: # Rex Replaced by Nia
            if include_printouts:
                print("Since Rex was replaced by Nia:")
                print("- Renamed Crossette's crystal to Aegis Core Crystal (since Crossette and Mythra swapped)")
            JSONParser.ChangeJSONLine(["common_ms/itm_crystal.json"], [15], ['name'], 'Aegis Core Crystal')
        case 3: # Rex replaced by Zeke
            if include_printouts:
                print("Since Rex was replaced by Zeke:")
                print("- Renamed Wulfric's crystal to Aegis Core Crystal (since Wulfric and Mythra swapped)")
            JSONParser.ChangeJSONLine(["common_ms/itm_crystal.json"], [13], ['name'], 'Aegis Core Crystal')
        case 6: # Rex Replaced by Morag
            if include_printouts:
                print("Since Rex was replaced by Morag:")
                print("- Renamed Corvin's crystal to Aegis Core Crystal (since Corvin and Mythra swapped)")
            JSONParser.ChangeJSONLine(["common_ms/itm_crystal.json"], [14], ['name'], 'Aegis Core Crystal')

    # Apply Swaps
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], ApplyBladeRandomization, replaceAll=True)


def ApplyDriverRandomization(driver):
    driver_id = driver['$id']
    if driver_id in OriginalCharacter2Replacement:
        replace_with_id = OriginalCharacter2Replacement[driver_id]

        # Copy all fields (except ID) from the replacement driver to the original driver
        for key, value in driver.items():
            # Skip a few fields
            if key in ['$id', 'DefBlade1', 'DefBlade2', 'DefBlade3', 'DefLvType', 'DefLv', 'DefWPType', 'DefWP', 'DefSPType', 'DefSP', 'DefAcce' ]:
                continue
            # For the keys which are lists, update every value except for Broadsword
            if key in ['WpnType', 'WpRate']:
                for i in range(0,len(driver[key])):
                    if i == 16: # Skip Broadsword, which should remain on Rex's replacement
                        continue
                    driver[key][i] = OriginalCharacters[replace_with_id][key][i]
            else:
                driver[key] = OriginalCharacters[replace_with_id][key]


def ApplyBladeRandomization(blade):
    # Certain skills are not randomized
    # 1. Field skills for progression reasons
    # 2. Pneuma skills, for purposes of Driver randomization without Blade randomization
    excluded_skills = dict()
    if not Options.RemoveFieldSkillsOption.GetState():
        excluded_skills[1001] = ['FSkill1', 'FSkill2', 'FSkill3']  # Pyra: Fire Mastery, Focus, Cooking
        excluded_skills[1005] = ['FSkill3']  # Poppi Alpha: Superstrength
        excluded_skills[1008] = ['FSkill2']  # Roc: Miasma Dispersal

    # Pneuma is only randomized when Drivers are randomized
    # 1. Default weapons not randomized, as it is set in SwapDefaultBlades()
    # 2. Model not randomized, as it is set in SwapDefaultBlades()
    # 3. Battle skills, as it is what makes Pneuma...Pneuma
    excluded_skills[1003] = ["Name", "DefWeapon", "Model", "BSkill1", "BSkill2", "BSkill3"]

    blade_id = blade['$id']
    if blade_id in OriginalCharacter2Replacement:
        replace_with_id = OriginalCharacter2Replacement[blade_id]

        # Copy all fields (except ID, ReleaseLock, and the excluded field skills)
        # from the replacement blade to the original blade
        for key, value in blade.items():
            if key in ['$id', 'ReleaseLock']:
                continue
            if blade_id in excluded_skills and key in excluded_skills[blade_id]:
                continue
            if key == 'Flag':
                for flag_key, flag_value in OriginalCharacters[replace_with_id]['Flag'].items():
                    if flag_key in ['FreeEngage', 'NoMapRev']:
                        continue

                    blade['Flag'][flag_key] = OriginalCharacters[replace_with_id]['Flag'][flag_key]
            else:
                blade[key] = OriginalCharacters[replace_with_id][key]


def RandomizePoppiForms():
    blades_left_to_randomize = PoppiForms.copy()
    randomized_order = blades_left_to_randomize.copy()
    random.shuffle(randomized_order)

    # Determine the randomization prior to randomizing.
    # This way we can populate Original2Replacement and Replacement2Original,
    # which will be needed later on for various reasons
    while blades_left_to_randomize:
        next_blade = blades_left_to_randomize[0]
        next_replacement = randomized_order[0]
        OriginalCharacter2Replacement[next_blade] = next_replacement
        ReplacementCharacter2Original[next_replacement] = next_blade
        if include_printouts:
            print('========================================')
            print(CharacterNames[next_blade] + ' was replaced with ' + CharacterNames[next_replacement])
            print(str(next_blade) + ' was replaced with ' + str(next_replacement))
        del blades_left_to_randomize[0]
        del randomized_order[0]

    # Apply Randomizations
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], PoppiForms, ApplyBladeRandomization)

    # Copy original poppi-related tables so we can swap things below
    OriginalPoppiBase = JSONParser.CopyJSONFile("common/BTL_HanaBase.json")
    OriginalPoppiChipset = JSONParser.CopyJSONFile("common/BTL_HanaChipset.json")
    OriginalPoppiPower = JSONParser.CopyJSONFile("common/BTL_HanaPower.json")

    # In most of the following tables, rows for the Poppi forms are 1-3.
    # Poppi alpha's blade ID is 1005, so I just add/subtract 1004 to convert between row and blade ID

    # Replace Poppiswap images (background of Poppiswap menu)
    def ReplacePoppiswapImages(image):
        original_poppi_id = image['$id'] + 1004
        new_image_num = OriginalCharacter2Replacement[original_poppi_id] - 1004
        image['filename'] = 'mnu091_hana_img0' + str(new_image_num)
    JSONParser.ChangeJSONLineWithCallback(["common/MNU_Hana_custom.json"], [], ReplacePoppiswapImages, replaceAll=True)

    # Replace Poppi Base (Available Poppiswaps)
    # TODO: I don't think this actually does anything. Unsure if it's even used in the code
    #  It's supposed to change the available Poppiswap slots (Alpha has 1 skill ram, but QTpi has 3)
    def ReplacePoppiBase(base):
       original_poppi_id = base['$id'] + 1004
       new_poppi_id = OriginalCharacter2Replacement[original_poppi_id]
       for key, value in OriginalPoppiBase[new_poppi_id - 1004].items():
           if key != '$id':
               base[key] = copy.deepcopy(OriginalPoppiBase[new_poppi_id - 1004][key])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaBase.json"], [], ReplacePoppiBase, replaceAll=True)

    # Replace Poppi Power (Energy Upgrades & Cost)
    def ReplacePoppiPower(power):
        for i in [1, 2, 3]:
            original_poppi_id = i + 1004
            new_poppi_id = OriginalCharacter2Replacement[original_poppi_id]
            new_i = new_poppi_id - 1004

            for field in ['PowerNum', 'EtherNum']:
                old_field = field + str(i)
                new_field = field + str(new_i)
                power[old_field] = copy.deepcopy(OriginalPoppiPower[power['$id']][new_field])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaPower.json"], [], ReplacePoppiPower, replaceAll=True)

    # Replace Poppi Chipset (Default Poppiswap Loadout)
    def ReplacePoppiChipset(chipset):
        original_poppi_id = chipset['$id'] + 1004
        new_poppi_id = OriginalCharacter2Replacement[original_poppi_id]
        for key, value in OriginalPoppiChipset[new_poppi_id - 1004].items():
            if key != '$id':
                chipset[key] = copy.deepcopy(OriginalPoppiChipset[new_poppi_id - 1004][key])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaChipset.json"], [], ReplacePoppiChipset, replaceAll=True)


def BugFixes_PostRandomization():
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_EnArrange.json"], [], FixRandomizedEnemyBladeCrashes, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], [], MakeAllArtsAccessible, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/EVT_cutscene_wp.json"], [], FixCutsceneCrashForNotHavingTwoWeapons, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_PcEquip.json"], [], FixDriverCosmetics, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_OrbEquip.json"], [], FixBladeCosmetics, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_HanaAssist.json"], [], FixBladeCosmetics, replaceAll=True)
    FixMenuText()
    RebalanceDefaultWeapons()
    FreeEngage()

    if OriginalCharacter2Replacement[1010] != 1010: # Pandoria was randomized
        FixCharacterMenuIcon(1010, 261, 50, "BL") # Pandoria with transparent glasses

    if randomize_drivers:
        DefineBroadswordArtsForRexsReplacement()
        FixDriverArts()
        FixDriverSkillTrees()
        FixWeaponMounts()
        if OriginalCharacter2Replacement[1] != 1: # Rex was randomized
            FixCharacterMenuIcon(1, 262, 9, "DR") # Rex after he gets Pyra's core crystal
            FixCharacterMenuIcon(1, 264, 10, "DR") # Rex with the Master Driver outfit


# Unsure why, but it is possible for the game to crash when an enemy blade gets randomized (for example, Pandoria).
# Replace the enemy version of the blade with the blade who that enemy replaced.
# TODO: Investigate the crash and see if it becomes possible to resolve while preserving the randomization. It would be
#       cool to fight against Zeke with Pandoria replaced with something else. But for now, this is not the case.
def FixRandomizedEnemyBladeCrashes(enemy):
    if enemy['BladeID'] in ReplacementCharacter2Original:
        if include_printouts:
            print("Enemy: " + CharacterNames[enemy['BladeID']] + " (" + str(enemy['BladeID']) + ") was replaced with " + CharacterNames[ReplacementCharacter2Original[enemy['BladeID']]] + " (" + str(ReplacementCharacter2Original[enemy['BladeID']]) + ")")
        enemy['BladeID'] = ReplacementCharacter2Original[enemy['BladeID']]


# When swapping blades, there is a bug where cutscenes will crash when attempting to load. This is caused because in 2 ways
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
    if original not in OriginalCharacter2Replacement:
        return

    # Replace resources with weapon type of the blade who replaced the original
    replacement = OriginalCharacter2Replacement[original]
    cutscene['resourceL'] = WeaponType2Resource(OriginalCharacters[replacement]['WeaponType'], 'L')
    cutscene['resourceR'] = WeaponType2Resource(OriginalCharacters[replacement]['WeaponType'], 'R')

def FixDriverCosmetics(accessory):
    if accessory['Driver'] in ReplacementCharacter2Original:
        accessory['Driver'] = ReplacementCharacter2Original[accessory['Driver']]


def FixBladeCosmetics(accessory):
    if accessory['Blade'] in ReplacementCharacter2Original:
        accessory['Blade'] = ReplacementCharacter2Original[accessory['Blade']]


# side is either 'L' or 'R' (case doesn't matter).
def WeaponType2Resource(weapon_type, side):

    base_string = 'wp' + str(weapon_type).zfill(2) + '0101'

    two_handed_weapons = [3, 5, 7, 9, 16, 22, 23, 25, 26, 30, 32, 34, 35]
    if weapon_type in two_handed_weapons:
        return base_string + '_' + side[0].lower()
    else:
        return base_string


def FixMenuText():
    # Zeke's Eye of Shining Justice Skill
    JSONParser.ChangeJSONLine(["common_ms/btl_enhance_cap.json"], [294], ['name'], 'At max Affinity w/ ' + CharacterNames[OriginalCharacter2Replacement[1010]] + ': R and +\nto awaken for a time (once per battle).')

    # Switch between Driver/Blade Nia text
    if 1011 in OriginalCharacter2Replacement and OriginalCharacter2Replacement[1011] != 1011:
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [261], ['name'], "Turn %s into %s?" % (CharacterNames[OriginalCharacter2Replacement[2]], CharacterNames[OriginalCharacter2Replacement[1011]]))
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [262], ['name'], "Turn %s into %s?" % (CharacterNames[OriginalCharacter2Replacement[1011]], CharacterNames[OriginalCharacter2Replacement[2]]))
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [297], ['name'], "You cannot turn %s into %s because\nno other Blades are engaged." % (CharacterNames[OriginalCharacter2Replacement[1011]], CharacterNames[OriginalCharacter2Replacement[2]]))

    # Swap to between Pyra/Mythra text
    # Note: The words "Swap to" have been intentionally dropped because any blade which a name longer than 6 letters gets cut off
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [260], ['name'], "Changing to %s. Is this OK?" % (CharacterNames[OriginalCharacter2Replacement[1001]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [259], ['name'], "Changing to %s. Is this OK?" % (CharacterNames[OriginalCharacter2Replacement[1002]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [89], ['name'], CharacterNames[OriginalCharacter2Replacement[1002]]) # "Swap to" Text
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [90], ['name'], CharacterNames[OriginalCharacter2Replacement[1001]]) # "Swap to" Text

    # Pyra/Mythra choice text
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [1], ['name'], CharacterNames[OriginalCharacter2Replacement[1001]]) # Pneuma's name when "Pyra" is selected
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [2], ['name'], CharacterNames[OriginalCharacter2Replacement[1002]]) # Pneuma's name when "Mythra" is selected
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1736], ['name'], CharacterNames[OriginalCharacter2Replacement[1001]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1737], ['name'], CharacterNames[OriginalCharacter2Replacement[1002]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [257], ['name'], "The name will be set to %s.\nIs this OK?" % (CharacterNames[OriginalCharacter2Replacement[1001]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [258], ['name'], "The name will be set to %s.\nIs this OK?" % (CharacterNames[OriginalCharacter2Replacement[1002]]))

    # Pyra/Mythra choice images
    # TODO


def DefineBroadswordArtsForRexsReplacement():
    rexs_replacement = OriginalCharacter2Replacement[1]

    # If Rex was not replaced, bail
    if rexs_replacement == 1:
        return

    existing_arts = JSONParser.CopyJSONFile("common/BTL_Arts_Dr.json")

    match rexs_replacement:
        case 2: # Nia
            # Define Broadsword arts for Nia, using Shield Hammer arts as a base
            NiaHammerAA1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 193)
            NiaHammerAA2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 194)
            NiaHammerAA3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 195)
            NiaHammerArt1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 206)
            NiaHammerArt2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 207)
            NiaHammerArt3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 208)
            #NiaHammerArt4 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 209) # Crashes the game

            new_auto_attacks = [NiaHammerAA1, NiaHammerAA2, NiaHammerAA3]
            #new_arts = [NiaHammerArt1, NiaHammerArt2, NiaHammerArt3, NiaHammerArt4]
            new_arts = [NiaHammerArt1, NiaHammerArt2, NiaHammerArt3]
        case 3: # Zeke
            # Define Broadsword arts for Zeke, using Shield Hammer arts as a base
            ZekeHammerAA1 = existing_arts[199].copy()
            ZekeHammerAA2 = existing_arts[200].copy()
            ZekeHammerAA3 = existing_arts[201].copy()
            ZekeHammerArt1 = existing_arts[214].copy()
            ZekeHammerArt2 = existing_arts[215].copy()
            #ZekeHammerArt3 = existing_arts[216].copy() # Crashes the game
            ZekeHammerArt4 = existing_arts[217].copy()

            new_auto_attacks = [ZekeHammerAA1, ZekeHammerAA2, ZekeHammerAA3]
            #new_arts = [ZekeHammerArt1, ZekeHammerArt2, ZekeHammerArt3, ZekeHammerArt4]
            new_arts = [ZekeHammerArt1, ZekeHammerArt2, ZekeHammerArt4]
        case 6: # Morag
            # Define Broadsword arts for Morag, using Shield Hammer arts as a base
            MoragHammerAA1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 196)
            MoragHammerAA2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 197)
            MoragHammerAA3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 198)
            MoragHammerArt1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 210)
            MoragHammerArt2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 211)
            MoragHammerArt3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 212)
            #MoragHammerArt4 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 213) # Crashes the game

            new_auto_attacks = [MoragHammerAA1, MoragHammerAA2, MoragHammerAA3]
            #new_arts = [MoragHammerArt1, MoragHammerArt2, MoragHammerArt3, MoragHammerArt4]
            new_arts = [MoragHammerArt1, MoragHammerArt2, MoragHammerArt3]
        case _: # Invalid
            print("Invalid Rex replacement...this should never happen")
            return

    next_art_ID = list(existing_arts)[-1] + 1
    last_AA_ID = next_art_ID + len(new_auto_attacks) - 1

    # Match unlock levels to Rex's Broadsword arts
    art_unlock_levels = [1, 1, 1, 1, 3, 5, 7] # First 3 are the AAs
    art_unlock_level_idx = 0

    # Iterate over each new art to make the required modifications
    new_auto_attacks_and_arts = new_auto_attacks + new_arts
    for art in new_auto_attacks_and_arts:
        art['$id'] = next_art_ID                  # Set the art ID
        art['WpnType'] = 17                       # Assign the art to Broadswords
        art['ActSpeed'] = int(art['ActSpeed'] * 1.2)   # Shield hammer arts art slow, make them Monado speed instead
        for i in Helper.InclRange(1,5): # Make arts accessible at the desired levels
            art['ReleaseLv' + str(i)] = art_unlock_levels[art_unlock_level_idx]
        art_unlock_level_idx = art_unlock_level_idx + 1
        if next_art_ID < last_AA_ID:              # This is a non-final auto attack, chain them together
            art["NextArts"] = next_art_ID + 1
        next_art_ID = next_art_ID + 1 # Increment counter
    JSONParser.ExtendJSONFile("common/BTL_Arts_Dr.json", [new_auto_attacks_and_arts])

    # Replace Broadsword animations with Shield Hammer
    JSONParser.ChangeJSONLine(["common/ITM_PcWpnType.json"], [17], ['Motion'], 13)


# Assigns arts to the correct driver, which has since been swapped
def FixDriverArts():
    def callback(art):
        original_driver_id = art["Driver"]
        if original_driver_id in DriversToRandomize:
            art["Driver"] = ReplacementCharacter2Original[original_driver_id]
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], [], callback, replaceAll=True)

def FixDriverSkillTrees():
    # Populate original skill trees
    original_skill_trees = dict()
    for driver_id in DriversToRandomize:
        original_skill_trees[driver_id] = JSONParser.CopyJSONFile(f"common/BTL_Skill_Dr_Table{driver_id:02d}.json")

    # Move the skill trees to the correct driver after randomization
    for original_driver_id in DriversToRandomize:
        replacement_driver_id = OriginalCharacter2Replacement[original_driver_id]

        # Convert dict to list
        new_skill_tree = []
        for key, value in original_skill_trees[replacement_driver_id].items():
            item = {"$id": key}
            # Zeke's Eye of Shining Justice sadly doesn't work with randomized drivers
            # The functionality exists on Zeke's replacement, but the game softlocks when you try to activate it
            # Replace Zeke's Shining Justice Skill with Rex's Combo Enhance skill (arbitrarily selected, but it's
            # one of the few skills not common between drivers)
            # This only happens if Zeke was actually randomized
            if (OriginalCharacter2Replacement[3] != [3]) and (replacement_driver_id == 3 and key == 24):
                item.update(original_skill_trees[1][8])
            else:
                item.update(value)

            new_skill_tree.append(item)

        JSONParser.ReplaceJSONFile(f"common/BTL_Skill_Dr_Table{original_driver_id:02d}.json", new_skill_tree)


def RebalanceDefaultWeapons():
    weapon_table = JSONParser.CopyJSONFile("common/ITM_PcWpn.json")
    chip_table = JSONParser.CopyJSONFile("common/ITM_PcWpnChip.json")

    def callback(blade):
        # Skip Pneuma, we handle her chip differently
        if blade['$id'] == 1003:
            return

        # Skip blades which were never randomized in the first place
        if blade['$id'] not in OriginalCharacter2Replacement:
            return

        original_blade_id = blade['$id']
        original_blade = OriginalCharacters[original_blade_id]
        original_weapon_type_id = original_blade['WeaponType']
        original_default_weapon_id = original_blade['DefWeapon']
        original_default_weapon = weapon_table[original_default_weapon_id]

        replacement_blade_id = OriginalCharacter2Replacement[original_blade_id]
        replacement_blade = blade
        replacement_weapon_type_id = replacement_blade['WeaponType']

        # Search for the original blade's default weapon in the weapon chip table
        original_chip = None
        for chip_id, chip in chip_table.items():
            if chip["CreateWpn" + str(original_weapon_type_id)] == original_default_weapon_id:
                original_chip = chip_id
                break
        # Unable to find the exact chip (not all weapons are in there), just find one with the same rank
        if original_chip is None:
            for chip_id, chip in chip_table.items():
                if chip["Rank"] == original_default_weapon["Rank"]:
                    original_chip = chip_id
                    break

        # Find the weapon that this chip becomes for the replacement blade's weapon type
        new_replacement_weapon_id = chip_table[original_chip]["CreateWpn" + str(replacement_weapon_type_id)]
        blade["DefWeapon"] = new_replacement_weapon_id
        if include_printouts:
            print("%s's new default weapon is: %s" % (CharacterNames[replacement_blade_id], new_replacement_weapon_id))

    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], callback, replaceAll=True)


def FixWeaponMounts():
    weapon_mount_table = JSONParser.CopyJSONFile("common/RSC_PcWpnMount.json")

    def callback(wpn_mount):
        for i in Helper.InclRange(1,36):
            fields = [f"Wpn{i:02d}rIn", f"Wpn{i:02d}rOut", f"Wpn{i:02d}lIn", f"Wpn{i:02d}lOut"]
            for field in fields:
                if field in wpn_mount.keys():
                    nonlocal weapon_mount_table
                    original_driver_id = wpn_mount['$id']
                    replacement_driver_id = OriginalCharacter2Replacement[original_driver_id]
                    wpn_mount[field] = weapon_mount_table[replacement_driver_id][field]

    JSONParser.ChangeJSONLineWithCallback(["common/RSC_PcWpnMount.json"], DriversToRandomize, callback)


# Several characters' menu icon and portrait change at some point in the story
# When this happens, the base game icon and portrait would replace whichever character replaced them.
# This function replaces the original image with images for whoever replaced that character
# We cannot modify who gets their image replaced, since that's tied to the executable.
def FixCharacterMenuIcon(character_id, icon_id, full_image_id, suffix):
    suffix_low = suffix.lower()
    suffix_cap = suffix_low.capitalize()

    # Get the still of the character which replaced this character
    replacement_still = OriginalCharacters[OriginalCharacter2Replacement[character_id]]['Still']

    # Use the still to find the icon index of the blade which replaced this character
    icon_index = JSONParser.QueryJSONLine("common/MNU_IconList.json", "$id", replacement_still)["icon_index"]

    # Fix the small icon for this character's replacement.
    JSONParser.ChangeJSONLine(["common/MNU_IconList.json"], [icon_id], ['icon_index'], icon_index)

    # Get the image for this character's replacement
    # This includes both the File ID and scaling/cropping information of the image
    replacement_image_row = JSONParser.QueryJSONLine(f"common/MNU_{suffix_cap}ImageID.json", "icon_id", replacement_still)

    # Grab the file name from the File ID
    file_name = JSONParser.QueryJSONLine(f"common/MNU_Stream_full_{suffix_low}.json", "$id", replacement_image_row['$id'])['filename']
    file_name_glow = JSONParser.QueryJSONLine(f"common/MNU_Stream_full_glow_{suffix_low}.json", "$id", replacement_image_row['$id'])['filename']

    # Replace the image for this character with their replacement's image.
    JSONParser.ChangeJSONLine([f"common/MNU_Stream_full_{suffix_low}.json"], [full_image_id], ['filename'], file_name)
    JSONParser.ChangeJSONLine([f"common/MNU_Stream_full_glow_{suffix_low}.json"], [full_image_id], ['filename'], file_name_glow)

    # Fix the cropping of the image of this character's replacement.
    for field in ['offs_x', 'offs_y', 'scale', 'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine([f"common/MNU_{suffix_cap}ImageID.json"], [full_image_id], [field], replacement_image_row[field])


def BladesDescriptions():
    BladesDesc = PopupDescriptions.Description()
    BladesDesc.Header(Options.BladesOption.name)
    BladesDesc.Image("BladeRandomization.png", "XC2", 700)
    BladesDesc.Text("This option randomizes when blades join the party throughout the story. This includes a driver's default blade, blades obtained through gacha, and blades obtained through side quests.")
    BladesDesc.Text("A few notes:")
    BladesDesc.Text("- Not every driver can use every blade. For example, Nia cannot use Pyra. Because of this, all blades can be freely engaged on any driver. An incompatible blade cannot appear as a driver's default blade.", anchor="w")
    BladesDesc.Text("- The blades who replace Pyra and Mythra will be able to swap between each other, as well as ascend into Pneuma. ", anchor="w")
    BladesDesc.Text("- The blade which replaces Nia will be able to swap between blade form and Nia's driver form.", anchor="w")
    BladesDesc.Text("- Roc is not randomized, as that would break Vandham.", anchor="w")
    BladesDesc.Text("- Dagas's base form is inaccessible. His true form appears when blades are randomized. Admittedly, I have no idea what happens if you decide to complete his side quest.", anchor="w")
    BladesDesc.Text("- The NG+ exclusive blades (Akhos, Obrona, Patroka, Perdido, Mikhail, Cressidus, and Sever) are not randomized. This is due to issues caused by their lack of unique weapon chips.", anchor="w")
    BladesDesc.Text("- A handful of voice lines do not work correctly, such as when using field skills.", anchor="w")

    BladesDesc.Header(Options.BladesOption_Dromarch.name)
    BladesDesc.Text("This suboption allows Dromarch to be randomized. This is generally recommended, however it introduces a weird glitch you should know about. Randomizing Dromarch may cause a player to teleport to a location specific to the current map, often out of bounds. This teleportation is known as \"Niaporting\" and can sometimes be burdensome but also sometimes be useful.")
    BladesDesc.Text("In the base game, playing as Nia with Dromarch causes Nia to ride Dromarch's back. In actuality, you are controlling Dromarch, and Nia just happens to be anchored to him. When Dromarch gets replaced, you are instead controlling the replaced blade. However, Nia is NOT anchored to this replacement blade. She is instead floating at the world's (0,0,0) coordinate. This is easiest to see in Argentum, where she is floating in the air at the Central Exchange.")
    BladesDesc.Image("FloatingNia.png", "XC2", 600)
    BladesDesc.Text("When changing the party in any form (drivers or blades), the game tries to reload the party at the active driver's location. If the active driver is Nia at the (0,0,0) location, that causes your party to reload at the (0,0,0) location, thus causing you to teleport there.")
    BladesDesc.Text("In order to avoid this behavior while using this suboption, make sure that  Nia's primary blade is not the blade who replaced Dromarch when controlling Nia and changing your party.")
    BladesDesc.Text("Controlling a blade directly has some interesting behavior. For example, they cannot interact with NPCs (only drivers can). Some blades do not have climbing animations and are unable to climb ladders (interestingly though, some blades actually can climb ladders). Blades also have some voice clips which are normally inaccessible, such as jumping and taking fall damage.")

    BladesDesc.Header(Options.BladesOption_Healer.name)
    BladesDesc.Text(f"This suboption only has an effect if {Options.BladesOption_Dromarch.name} is also selected. With this suboption, it ensures that the blade which replaces Dromarch has a Healing Halo equivalent art. This is used to ensure that there is a healer in the party. This includes any blade which is a Bitball or Twin Rings (or a clone of Twin Rings) weapon. This blade is is not always a Healer class, as some blades like Elma have healing arts as Attackers.")
    BladesDesc.Text("If drivers are also randomized, this suboption ensures that whichever driver replaces Nia gets paired with a blade who has a Healing Halo equivalent art. Nia and Morag have the same healing weapons, listed above. Rex's only healing weapon is the Catalyst Scimitar. If Rex replaces Nia, Nia will be his default blade. Zeke has no Healing Halo arts on any weapon, and so he cannot replace Nia if this suboption is selected.")
    return BladesDesc


def DriversDescriptions():
    DriversDesc = PopupDescriptions.Description()
    DriversDesc.Header(Options.DriversOption.name)
    DriversDesc.Image("DriverRandomization.png", "XC2", 700)
    DriversDesc.Text("This option randomizes when the drivers join the party throughout the story. Specifically: Rex, Nia, Morag, and Zeke are randomized.")
    DriversDesc.Text("Since weapons are not compatible between these drivers (for example, Nia cannot use the Aegis Sword) their default blades get swapped as well. So if Morag replaces Rex, that means that Brighid will replace Pyra as well.")
    DriversDesc.Text("Mythra also gets swapped out when Rex gets randomized. Mythra gets replaced with either Crossette, Corvin, or Wulfric, depending on which driver replaced Rex (Nia, Morag, and Zeke respectively). These blades were selected because they are the 3 blades which are guaranteed the earliest in the game, while also matching the classes (HLR/TNK/ATK) of the driver's default blade. The Pyra/Mythra replacements can swap between each other freely during combat. The core crystal which normally summons this blade is replaced with an Aegis Core Crystal, which summons Mythra. This should be used on Rex.")
    DriversDesc.Text("Pneuma gets a full replacement if Rex gets randomized. This replacement will be an \"ascended\" version of either Dromarch, Brighid, or Pandoria. This is a more powerful version of this blade which gets Pneuma's ability to perform any blade combo.")
    # TODO: Custom Pneuma image
    DriversDesc.Text("A few notes:")
    DriversDesc.Text(f"- This option is incompatible with {Options.RaceModeOption.name} and {Options.UMHuntOption.name}. If those game modes are selected, drivers will not be randomized.", anchor="w")
    DriversDesc.Text("- Zeke's Eye of Shining Justice skill does not work properly when Zeke gets randomized. This skill is replaced by Rex's Combo Breaker in this case.", anchor="w")
    DriversDesc.Text("- A handful of voice lines do not work correctly, such as when unlocking affinity nodes.", anchor="w")

    DriversDesc.Header(Options.DriversOption_Nia.name)
    DriversDesc.Text("This suboption ensures that Nia is one of the first two drivers that join the party (either replacing Rex or herself). This is recommended when not randomizing blades, as this guarantees a healer.")

    return DriversDesc
