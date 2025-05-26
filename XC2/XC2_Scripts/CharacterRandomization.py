import copy, random, Options
from scripts import JSONParser, Helper

# TODO (blades):
#  - Replace the images in the Pyra/Mythra selection to the blades which replaced them
#  - Figure out how to randomize Torna blades properly (Apparently NoBuildWpn in CHR_Bl is not sufficient)
#  - Blade names should be replaced in all dialogs where possible
#  - Replace driver voice lines when changing blades (Rex will currently shout "Pyra" when switching to Pyra's replacement)
#  - Replace field skill voice lines (Pyra's replacement currently says "I bring upon the power of fire!" in Pyra's voice)
#  - Only do the Pandoria glasses fix if Pandoria is actually randomized
#  - Could Pandoria's glasses overworld model still be used if we apply a condition? Currently a condition isn't used, so I'm not sure how that cosmetic model gets applies
#  - All blade's weapons should scale to who they replace. For example, if a gacha blade replaces Brighid, they should have a coil chip. If Pandoria becomes Gacha, she should have a tier 1 chip.

# TODO: (drivers)
#  - Broadsword arts should only be available at the levels that Rex's broadsword arts are valid. Ensure that none of the arts cause crashes.
#  - Game crashes when Zeke uses Detonation blow with the broadsword (if I can't figure out why, just remove the art)
#  - Voice lines in the menu (such as when spending affinity tokens) is still the original driver's voice
#  - Where weapons are located on the player model is wrong. When Rex becomes Morag for example, the whipswords on Morag's back line up with where Rex puts his weapons (his back) not where Morag puts her weapons (hips)
#    - This is likely tied to the weapon's animations, so that probably cannot be fixed.
#  - swapped drivers are not zoomed in properly when summoning core crystals
#  - "Not to boast, but that was spectacular! Right gramps?" after winning a fight without Rex in the party yet
#  - DefWeapon on each blade is not scaled to the correct damage. Brighid normally starts with a Coil chip for example but when Rex replaced her he has a rank 1 weapon
#  - Text for "Make Nia a Driver" Should say "Turn Nia into Morag" or something
#  - Rex's Master Driver icon is still not fixed for the small icons
#    - It is correct for the big icon
#  -
#  - hard to tell if master driver logic is working properly, since I have the QoL setting for swapping blades. Try another run without that and without NG+ stuff
#  - Driver randomization should be disabled if either of the side modes are selected (driver randomization is kind of fundamentally incompatible with custom save files)
#  -
#  - Replace driver names in all dialog text (nice to have)

# TODO: Can these structures be combined with the ones for blades?
OriginalDrivers = dict()            # Maps Driver ID to the dictionary of the unrandomized driver date. Populated in PopulateDrivers()
DriverNames = dict()                # Maps ID to Driver Name. Populated in PopulateDrivers()
OriginalDriver2Replacement = dict() # Maps Unrandomized Driver ID to Randomized Driver ID. Populated in RandomizeDrivers()
ReplacementDriver2Original = dict() # Maps Randomized Driver ID to Unrandomized Driver ID. Populated in RandomizeDrivers()

OriginalBlades = dict()        # Maps Blade ID to the dictionary of the unrandomized blade date. Populated in PopulateBlades()
BladeNames = dict()            # Maps ID to Blade Name. Populated in PopulateBlades()
OriginalBlade2Replacement = dict()  # Maps Unrandomized Blade ID to Randomized Blade ID. Populated in RandomizeBlades()
ReplacementBlade2Original = dict()  # Maps Randomized Blade ID to Unrandomized Blade ID. Populated in RandomizeBlades()


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
# The guaranteed Healer must belong on the driver who replaced NIA
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

include_printouts = True  # Debugging

def resetGlobals():
    global GuaranteedHealer
    global first_character_randomization

    OriginalDrivers.clear()
    OriginalBlades.clear()
    DriverNames.clear()
    BladeNames.clear()
    OriginalDriver2Replacement.clear()
    OriginalBlade2Replacement.clear()
    ReplacementDriver2Original.clear()
    ReplacementBlade2Original.clear()
    GuaranteedHealer = None
    first_character_randomization = True


def CharacterRandomization():
    # Make sure this logic is called only once
    global first_character_randomization
    if first_character_randomization:
        first_character_randomization = False
    else:
        return

    if include_printouts:
        print("Character Randomization: ")
        print("\tRandomize Drivers: " + str(Options.DriversOption.GetState()))
        print("\tRandomize Blades: " + str(Options.BladesOption.GetState()))
        print("\t\tRandomize Dromarch: " + str(Options.BladesOption_Dromarch.GetState()))
        print("\t\tGuarantee Healer: " + str(Options.BladesOption_Healer.GetState()))

    InitialSetup()
    BugFixes_PreRandomization()

    # Note: This is explicitly needed before both driver and blade randomization
    #       Drivers need this logic because Zeke does not have any healers, so he cannot replace Nia if healers are guaranteed
    DetermineGuaranteedHealer()

    RandomizeDrivers()
    RandomizeBlades()

    BugFixes_PostRandomization()


def FreeEngage(): # If Blade Rando is on, we want to be able to move blades around freely to avoid bugs
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/MNU_DlcGift.json", ["FreeEngage"], "1")


def InitialSetup():
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], [], PopulateDrivers, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], PopulateBlades, replaceAll=True)


def PopulateDrivers(driver):
    driver_id = driver['$id']
    OriginalDrivers[driver_id] = dict()
    for key, value in driver.items():
        OriginalDrivers[driver_id][key] = copy.deepcopy(driver[key])

    Name = ''
    name_id = driver['Name']

    def getName(row):
        nonlocal Name
        Name = row['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/chr_dr_ms.json"], [name_id], getName)

    DriverNames[driver_id] = Name


def PopulateBlades(blade):
    blade_id = blade['$id']
    OriginalBlades[blade_id] = dict()
    for key, value in blade.items():
        OriginalBlades[blade_id][key] = copy.deepcopy(blade[key])

    Name = ''
    name_id = blade['Name']

    def getName(row):
        nonlocal Name
        Name = row['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/chr_bl_ms.json"], [name_id], getName)

    BladeNames[blade_id] = Name


def DetermineGuaranteedHealer():
    if Options.BladesOption.GetState() and Options.BladesOption_Healer.GetState():
        global GuaranteedHealer

        # If Dromarch isn't randomized, he's the healer by default
        if Options.BladesOption.GetState() and not Options.BladesOption_Dromarch.GetState():
            GuaranteedHealer = 1004
            if include_printouts:
                print("The guaranteed healer is Dromarch (by default).")
        else:
            potential_healers = PossibleHealerBlades.copy()
            random.shuffle(potential_healers)
            GuaranteedHealer = potential_healers[0]
            if include_printouts:
                print("The guaranteed healer is " + BladeNames[GuaranteedHealer])


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
    if Options.BladesOption.GetState():
        # Replace Dagas 1022 with Dagas 1050 in gacha table. Since they are different blades, they could randomize weirdly.
        # For the purposes of this randomizer, 1022 is inaccessible
        JSONParser.ChangeJSONLine(["common/BLD_RareList.json"], [7], ['Blade'], 1050)


def RandomizeDrivers():
    if Options.DriversOption.GetState():
        drivers_left_to_randomize = DriversToRandomize.copy()

        randomized_order = drivers_left_to_randomize.copy()
        random.shuffle(randomized_order)

        # TODO: Testing. Remove this
        #  This makes it so no driver is in their starting position
        if GuaranteedHealer and GuaranteedHealer == 1011:
            randomized_order = [3, 1, 6, 2]
        else:
            randomized_order = [2, 6, 1, 3]

        # If there is a guaranteed healer, make sure they're in Nia's spot (index 1)
        # Keep shuffling until that happens
        if GuaranteedHealer is not None:
            while GuaranteedHealer not in PossibleHealerBladesForEachDriver[randomized_order[1]]:
                if include_printouts:
                    print("The guaranteed healer was %s but Nia was randomized to %s. Reshuffling drivers..." % (BladeNames[GuaranteedHealer], DriverNames[randomized_order[1]]))
                random.shuffle(randomized_order)

        # Determine the randomization prior to randomizing.
        # This way we can populate Original2Replacement and Replacement2Original,
        # which will be needed later on for various reasons
        while drivers_left_to_randomize:
            next_driver = drivers_left_to_randomize[0]
            next_replacement = randomized_order[0]

            OriginalDriver2Replacement[next_driver] = next_replacement
            ReplacementDriver2Original[next_replacement] = next_driver
            if include_printouts:
                print('========================================')
                print(DriverNames[next_driver] + ' was replaced with ' + DriverNames[next_replacement])
                print(str(next_driver) + ' was replaced with ' + str(next_replacement))
            del drivers_left_to_randomize[0]
            del randomized_order[0]

        # Apply Randomizations
        JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], [], ApplyDriverRandomization, replaceAll=True)

    # No randomization, populate the maps with no swaps
    else:
        for driver_id in DriversToRandomize:
            OriginalDriver2Replacement[driver_id] = driver_id
            ReplacementDriver2Original[driver_id] = driver_id


def RandomizeBlades():
    if Options.BladesOption.GetState():
        # Note: It is important that BladesLeftToRandomize starts with the default blades,
        # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
        blades_left_to_randomize = BladesAlwaysRandomized.copy()

        # Only add Dromarch to the pool if explicitly randomizing him
        if Options.BladesOption.GetState() and Options.BladesOption_Dromarch.GetState():
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
                OriginalBlade2Replacement[next_blade] = next_replacement
                ReplacementBlade2Original[next_replacement] = next_blade
                if include_printouts:
                    print('========================================')
                    print(BladeNames[next_blade] + ' was replaced with ' + BladeNames[next_replacement])
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
    blades_replacement_driver = OriginalDriver2Replacement[blades_original_driver]

    # Handle the case of having the guaranteed healer
    if Options.BladesOption.GetState() and Options.BladesOption_Healer.GetState():
        if original_blade == 1004 and GuaranteedHealer in PossibleHealerBladesForEachDriver[OriginalDriver2Replacement[blades_original_driver]]:
            if replacement_blade != GuaranteedHealer:
                if include_printouts:
                    print("%s cannot be replaced with %s" % (BladeNames[original_blade], BladeNames[replacement_blade]))
                    print("\tRandomized blade is %s. Expected healer blade is %s." % (BladeNames[replacement_blade], BladeNames[GuaranteedHealer]))
                    print("\tDriver is %s (originally %s)" % (blades_replacement_driver, DriverNames[blades_original_driver]))
                return False

    # Handle cases where arts wouldn't be defined for the replacement
    if replacement_blade in BladesDriverCantUse[blades_replacement_driver]:
        if include_printouts:
            print("%s cannot be replaced with %s" % (BladeNames[original_blade], BladeNames[replacement_blade]))
            print("\tDriver is %s (originally %s)" % (DriverNames[blades_replacement_driver], DriverNames[blades_original_driver]))
        return False

    return True


def SwapDefaultBlades():
    # Pyra, Dromarch, Brighid, and Pandoria can be handled as simple swaps.
    # Roc needs to stay because of Vandham
    # Blade Nia will stay for convenience. But whoever replaces Rex will not be able to use her #TODO: can blade nia swap blades with the QoL setting enabled?
    # TODO Mythra on the other hand is a strange one. Mythra needs to be replaced with *somebody*
    #  - If Nia replaced Rex, Mythra should become Crossette
    #  - If Morag replaced Rex, Mythra should become Corvin (Or Aegeaon?)
    #  - If Zeke replaced Rex, Mythra should become Herald
    #  - In each of these cases, the core crystals items which contain these blades should also be renamed to "Aegis core crystal"

    original_driver_to_primary_blade = {
        1: 1001, # Rex to Pyra
        2: 1004, # Nia to Dromarch
        3: 1010, # Zeke to Pandoria
        6: 1009, # Morag to Brighid
    }
    original_driver_to_secondary_blades = {
        1: 1002, # Rex to Mythra
        2: 1109, # Nia to Crossette
        3: 1108, # Zeke to Corvin
        6: 1014, # Morag to Aegeaon
    }

    # Swap primary blades for all drivers
    for original_driver_id in DriversToRandomize:
        replacement_driver_id = OriginalDriver2Replacement[original_driver_id]

        original_blade_id = original_driver_to_primary_blade[original_driver_id]
        replacement_blade_id = original_driver_to_primary_blade[replacement_driver_id]

        OriginalBlade2Replacement[original_blade_id] = replacement_blade_id
        ReplacementBlade2Original[replacement_blade_id] = original_blade_id

        if include_printouts:
            print('========================================')
            print(BladeNames[original_blade_id] + ' was replaced with ' + BladeNames[replacement_blade_id])
            print(str(original_blade_id) + ' was replaced with ' + str(replacement_blade_id))

    # Swap Mythra (and only Mythra) with the secondary blades
    # Only bother if Rex was randomized
    if OriginalDriver2Replacement[1] != 1:
        original_driver_id = 1 # Rex
        replacement_driver_id = OriginalDriver2Replacement[original_driver_id]

        original_blade_id = original_driver_to_secondary_blades[original_driver_id] # Mythra
        replacement_blade_id = original_driver_to_secondary_blades[replacement_driver_id]

        OriginalBlade2Replacement[original_blade_id] = replacement_blade_id
        OriginalBlade2Replacement[replacement_blade_id] = original_blade_id
        ReplacementBlade2Original[original_blade_id] = replacement_blade_id
        ReplacementBlade2Original[replacement_blade_id] = original_blade_id

        if include_printouts:
            print('========================================')
            print(BladeNames[original_blade_id] + ' was replaced with ' + BladeNames[replacement_blade_id])
            print(str(original_blade_id) + ' was replaced with ' + str(replacement_blade_id))
            print('========================================')
            print(BladeNames[replacement_blade_id] + ' was replaced with ' + BladeNames[original_blade_id])
            print(str(replacement_blade_id) + ' was replaced with ' + str(original_blade_id))

    # Replace Pneuma with the new character's default blade with an actually strong weapon
    # Note: Pneuma's "Model" and "DefWeapon" fields are explicitly ignored in ApplyBladeSwaps
    # Also rename the core crystal which now contains Mythra (if Mythra was swapped above)
    # TODO: Only if Blades are not randomized
    match OriginalDriver2Replacement[1]:
        case 1: # Rex was not replaced
            if include_printouts:
                print("Rex was not replaced.")
                print("- Pneuma remains unchanged.")
                print("- No core crystals were renamed")
        case 2: # Rex Replaced by Nia
            if include_printouts:
                print("Since Rex was replaced by Nia:")
                print("- Replaced Pneuma with Savage Dromarch with the Meteorite Rings")
                print("- Renamed Crossette's crystal to Aegis Core Crystal (since Crossette and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1004
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100501")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5179) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
            JSONParser.ChangeJSONLine(["common_ms/itm_crystal.json"], [15], ['name'], 'Aegis Core Crystal')
        case 3: # Rex replaced by Zeke
            if include_printouts:
                print("Since Rex was replaced by Zeke:")
                print("- Replaced Pneuma with Mermaid Blue Pandoria with the Meteorite Edge")
                print("- Renamed Corvin's crystal to Aegis Core Crystal (since Corvin and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1010
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100901")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5479) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
        case 6: # Rex Replaced by Morag
            if include_printouts:
                print("Since Rex was replaced by Morag:")
                print("- Replaced Pneuma with Jade Orchid Brighid with the Meteorite Whips")
                print("- Renamed Aegaeon's crystal to Aegis Core Crystal (since Aegeaon and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1009
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl121001")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5419) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma

    # Apply Swaps
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], ApplyBladeRandomization, replaceAll=True)


def ApplyDriverRandomization(driver):
    driver_id = driver['$id']
    if driver_id in OriginalDriver2Replacement:
        replace_with_id = OriginalDriver2Replacement[driver_id]

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
                    driver[key][i] = OriginalDrivers[replace_with_id][key][i]
            else:
                driver[key] = OriginalDrivers[replace_with_id][key]


def ApplyBladeRandomization(blade):
    # Certain fields are not randomized
    # 1. Field skills for progression reasons (TODO: If field skills QoL options are not picked)
    # 2. Pneuma skills, for purposes of Driver randomization without Blade randomization
    excluded_fields = dict()
    excluded_fields[1001] = ['FSkill1', 'FSkill2', 'FSkill3']  # Pyra: Fire Mastery, Focus, Cooking
    excluded_fields[1005] = ['FSkill3']  # Poppi Alpha: Superstrength
    excluded_fields[1008] = ['FSkill2']  # Roc: Miasma Dispersal

    # Pneuma is only randomized when Drivers are randomized but Blades are not
    # 1. Default weapons not randomized, as it is set in SwapDefaultBlades()
    # 2. Model not randomized, as it is set in SwapDefaultBlades()
    # 3. Battle skills, as it is what makes Pneuma...Pneuma
    excluded_fields[1003] = ["DefWeapon", "Model", "BSkill1", "BSkill2", "BSkill3"]

    blade_id = blade['$id']
    if blade_id in OriginalBlade2Replacement:
        replace_with_id = OriginalBlade2Replacement[blade_id]

        # Copy all fields (except ID, ReleaseLock, and the excluded field skills)
        # from the replacement blade to the original blade
        for key, value in blade.items():
            if key in ['$id', 'ReleaseLock']:
                continue
            if blade_id in excluded_fields and key in excluded_fields[blade_id]:
                continue
            if key == 'Flag':
                for flag_key, flag_value in OriginalBlades[replace_with_id]['Flag'].items():
                    if flag_key in ['FreeEngage', 'NoMapRev']:
                        continue

                    blade['Flag'][flag_key] = OriginalBlades[replace_with_id]['Flag'][flag_key]
            else:
                blade[key] = OriginalBlades[replace_with_id][key]


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
        OriginalBlade2Replacement[next_blade] = next_replacement
        ReplacementBlade2Original[next_replacement] = next_blade
        if include_printouts:
            print('========================================')
            print(BladeNames[next_blade] + ' was replaced with ' + BladeNames[next_replacement])
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
        new_image_num = OriginalBlade2Replacement[original_poppi_id] - 1004
        image['filename'] = 'mnu091_hana_img0' + str(new_image_num)
    JSONParser.ChangeJSONLineWithCallback(["common/MNU_Hana_custom.json"], [], ReplacePoppiswapImages, replaceAll=True)

    # Replace Poppi Base (Available Poppiswaps)
    # TODO: I don't think this actually does anything. Unsure if it's even used in the code
    #  It's supposed to change the available Poppiswap slots (Alpha has 1 skill ram, but QTpi has 3)
    def ReplacePoppiBase(base):
       original_poppi_id = base['$id'] + 1004
       new_poppi_id = OriginalBlade2Replacement[original_poppi_id]
       for key, value in OriginalPoppiBase[new_poppi_id - 1004].items():
           if key != '$id':
               base[key] = copy.deepcopy(OriginalPoppiBase[new_poppi_id - 1004][key])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaBase.json"], [], ReplacePoppiBase, replaceAll=True)

    # Replace Poppi Power (Energy Upgrades & Cost)
    def ReplacePoppiPower(power):
        for i in [1, 2, 3]:
            original_poppi_id = i + 1004
            new_poppi_id = OriginalBlade2Replacement[original_poppi_id]
            new_i = new_poppi_id - 1004

            for field in ['PowerNum', 'EtherNum']:
                old_field = field + str(i)
                new_field = field + str(new_i)
                power[old_field] = copy.deepcopy(OriginalPoppiPower[power['$id']][new_field])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaPower.json"], [], ReplacePoppiPower, replaceAll=True)

    # Replace Poppi Chipset (Default Poppiswap Loadout)
    def ReplacePoppiChipset(chipset):
        original_poppi_id = chipset['$id'] + 1004
        new_poppi_id = OriginalBlade2Replacement[original_poppi_id]
        for key, value in OriginalPoppiChipset[new_poppi_id - 1004].items():
            if key != '$id':
                chipset[key] = copy.deepcopy(OriginalPoppiChipset[new_poppi_id - 1004][key])
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_HanaChipset.json"], [], ReplacePoppiChipset, replaceAll=True)


def BugFixes_PostRandomization():
    # TODO: I had the following line commented out when testing driver rando in isolation.
    #  Is this why Dromarch didn't appear in the ghosts fight?
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_EnArrange.json"], [], FixRandomizedEnemyBladeCrashes, replaceAll=True)

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], [], MakeAllArtsAccessible, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/EVT_cutscene_wp.json"], [], FixCutsceneCrashForNotHavingTwoWeapons, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_OrbEquip.json"], [], FixCosmetics, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_HanaAssist.json"], [], FixCosmetics, replaceAll=True)
    FixPandoriaSpriteAfterElpys()
    FixMenuText()

    if Options.BladesOption.GetState():
        FreeEngage()

    if Options.DriversOption.GetState():
        # TODO: FixDriverSkillTrees()
        DefineBroadswordArtsForRexsReplacement()
        FixRexStillAfterHeDies()
        FixRexStillMasterDriver()
        FixDriverArts()

# Unsure why, but it is possible for the game to crash when an enemy blade gets randomized (for example, Pandoria).
# Replace the enemy version of the blade with the blade who that enemy replaced.
# TODO: Investigate the crash and see if it becomes possible to resolve while preserving the randomization. It would be
#       cool to fight against Zeke with Pandoria replaced with something else. But for now, this is not the case.
def FixRandomizedEnemyBladeCrashes(enemy):
    if enemy['BladeID'] in ReplacementBlade2Original:
        if include_printouts:
            print("Enemy: " + BladeNames[enemy['BladeID']] + " (" + str(enemy['BladeID']) + ") was replaced with " + BladeNames[ReplacementBlade2Original[enemy['BladeID']]] + " (" + str(ReplacementBlade2Original[enemy['BladeID']]) + ")")
        enemy['BladeID'] = ReplacementBlade2Original[enemy['BladeID']]


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
    if original not in OriginalBlade2Replacement:
        return

    # Replace resources with weapon type of the blade who replaced the original
    replacement = OriginalBlade2Replacement[original]
    cutscene['resourceL'] = WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'L')
    cutscene['resourceR'] = WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'R')

# TODO: How to fix cosmetics for drivers? Make sure to account for that in the cosmetics settings as well
def FixCosmetics(accessory):
    if accessory['Blade'] in ReplacementBlade2Original:
        accessory['Blade'] = ReplacementBlade2Original[accessory['Blade']]


# side is either 'L' or 'R' (case doesn't matter).
def WeaponType2Resource(weapon_type, side):

    base_string = 'wp' + str(weapon_type).zfill(2) + '0101'

    two_handed_weapons = [3, 5, 7, 9, 16, 22, 23, 25, 26, 30, 32, 34, 35]
    if weapon_type in two_handed_weapons:
        return base_string + '_' + side[0].lower()
    else:
        return base_string

# Pandoria's menu icon and portrait changes at some point in chapter 7. Her glasses go from opaque to transparent.
# When this happens, the icon and portrait would replace whichever blade replaced her.
# This function replaces the transparent glasses images with images for whoever replaced Pandoria
def FixPandoriaSpriteAfterElpys():
    # Get the still of the blade which replaced Pandoria
    pandoria_replacement_still = OriginalBlades[OriginalBlade2Replacement[1010]]['Still']

    # Use the still to find the icon index of the blade which replaced Pandoria
    icon_index = JSONParser.QueryJSONLine("common/MNU_IconList.json", "$id", pandoria_replacement_still)["icon_index"]

    # Fix the small icon for Pandoria's replacement. Row 261 corresponds to Pandoria's icon with transparent glasses
    JSONParser.ChangeJSONLine(["common/MNU_IconList.json"], [261], ['icon_index'], icon_index)

    # Get the blade image for Pandoria's replacement
    # This includes both the File ID and scaling/cropping information of the image
    PandoriaReplacementImageRow = JSONParser.QueryJSONLine("common/MNU_BlImageID.json", "icon_id", pandoria_replacement_still)

    # Grab the file name from the File ID
    fileName = JSONParser.QueryJSONLine("common/MNU_Stream_full_bl.json", "$id", PandoriaReplacementImageRow['$id'])['filename']
    # TODO fix the glow as well?

    # Replace the image for Pandoria with her replacement's image. Row 50 corresponds to Pandoria's portrait with transparent glasses
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_bl.json"], [50], ['filename'], fileName)

    # Fix the cropping of the image of Pandoria's replacement. Row 50 corresponds to Pandoria's portrait with transparent glasses
    for field in ['offs_x', 'offs_y', 'scale', 'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine(["common/MNU_BlImageID.json"], [50], [field], PandoriaReplacementImageRow[field])

def FixMenuText():
    # TODO: How do I figure out default blades if both Drivers and Blades have been randomized?
    #  This matters for Pandoria at least, perhaps others.


    # Zeke's Eye of Shining Justice Skill
    # TODO Also, does this skill even work if Zeke gets swapped?
    JSONParser.ChangeJSONLine(["common_ms/btl_enhance_cap.json"], [294], ['name'], 'At max Affinity w/ ' + BladeNames[OriginalBlade2Replacement[1010]] + ': R and +\nto awaken for a time (once per battle).')

    # Switch between Driver/Blade Nia text
    if 1011 in OriginalBlade2Replacement and OriginalBlade2Replacement[1011] != 1011:
        # TODO: Test this change
        #JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [261], ['name'], 'Turn Nia into ' + BladeNames[OriginalBlade2Replacement[1011]] + '?''')
        #JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [262], ['name'], 'Turn ' + BladeNames[OriginalBlade2Replacement[1011]] + ' into Nia?')
        #JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [297], ['name'], 'You cannot turn ' + BladeNames[OriginalBlade2Replacement[1011]] + ' into Nia because\nno other Blades are engaged.')
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [261], ['name'], "Turn %s into %s?" % (DriverNames[OriginalDriver2Replacement[2]], BladeNames[OriginalBlade2Replacement[1011]]))
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [262], ['name'], "Turn %s into %s?" % (BladeNames[OriginalBlade2Replacement[1011]], DriverNames[OriginalDriver2Replacement[2]]))
        JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [297], ['name'], "You cannot turn %s into %s because\nno other Blades are engaged." % (BladeNames[OriginalBlade2Replacement[1011]], DriverNames[OriginalDriver2Replacement[2]]))

    # Swap to between Pyra/Mythra text
    # Note: The words "Swap to" have been intentionally dropped because any blade which a name longer than 6 letters gets cut off
    # TODO: Test this change
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [260], ['name'], "Changing to %s. Is this OK?" % (BladeNames[OriginalBlade2Replacement[1001]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [259], ['name'], "Changing to %s. Is this OK?" % (BladeNames[OriginalBlade2Replacement[1002]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [89], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # "Swap to" Text
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [90], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # "Swap to" Text

    # Pyra/Mythra choice text
    # TODO: Test this change
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [1], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # Pneuma's name when "Pyra" is selected
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [2], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # Pneuma's name when "Mythra" is selected
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1736], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1737], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [257], ['name'], "The name will be set to %s. Is this OK?" % (BladeNames[OriginalBlade2Replacement[1001]]))
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [258], ['name'], "The name will be set to %s. Is this OK?" % (BladeNames[OriginalBlade2Replacement[1002]]))

    # Pyra/Mythra choice images
    # TODO


def DefineBroadswordArtsForRexsReplacement():
    rexs_replacement = OriginalDriver2Replacement[1]

    # If Rex was not replaced, bail
    if rexs_replacement == 1:
        return

    match rexs_replacement:
        case 2: # Nia
            # Define Broadsword arts for Nia, using Monado arts as a base
            NiaHammerAA1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 193)
            NiaHammerAA2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 194)
            NiaHammerAA3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 195)
            NiaHammerArt1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 206)
            NiaHammerArt2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 207)
            NiaHammerArt3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 208)
            NiaHammerArt4 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 209)

            new_auto_attacks = [NiaHammerAA1, NiaHammerAA2, NiaHammerAA3]
            new_arts = [NiaHammerArt1, NiaHammerArt2, NiaHammerArt3, NiaHammerArt4]
        case 3: # Zeke
            # TODO: One of these crashes the game. Need to figure out which and just remove it
            # TODO: Figure out if there are any other arts for other characters which need arts removed
            # Define Broadsword arts for Zeke, using Monado arts as a base
            ZekeHammerAA1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 199)
            ZekeHammerAA2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 200)
            ZekeHammerAA3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 201)
            ZekeHammerArt1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 214)
            ZekeHammerArt2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 215)
            ZekeHammerArt3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 216)
            ZekeHammerArt4 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 217)

            new_auto_attacks = [ZekeHammerAA1, ZekeHammerAA2, ZekeHammerAA3]
            new_arts = [ZekeHammerArt1, ZekeHammerArt2, ZekeHammerArt3, ZekeHammerArt4]
        case 6: # Morag
            # Define Broadsword arts for Zeke, using Hammer arts as a base
            MoragHammerAA1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 196)
            MoragHammerAA2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 197)
            MoragHammerAA3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 198)
            MoragHammerArt1 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 210)
            MoragHammerArt2 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 211)
            MoragHammerArt3 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 212)
            MoragHammerArt4 = JSONParser.QueryJSONLine("common/BTL_Arts_Dr.json", "$id", 213)

            new_auto_attacks = [MoragHammerAA1, MoragHammerAA2, MoragHammerAA3]
            new_arts = [MoragHammerArt1, MoragHammerArt2, MoragHammerArt3, MoragHammerArt4]
        case _: # Invalid
            print("Invalid Rex replacement...this should never happen")
            return

    next_art_ID = 743 # The last art in the table by default is 742
    last_AA_ID = next_art_ID + len(new_auto_attacks) - 1

    # Iterate over each new art to make the required modifications
    new_auto_attacks_and_arts = new_auto_attacks + new_arts
    for art in new_auto_attacks_and_arts:
        art['$id'] = next_art_ID                  # Set the art ID
        art['WpnType'] = 17                       # Assign the art to Broadswords
        art['ActSpeed'] = 120                      # Change Speed to match Monado TODO: Multiple speed by 1.2 instead of hardcoding, since the art speed may have been randomized earlier)
        for i in Helper.InclRange(1,5): # Make arts accessible at level 1
            art['ReleaseLv' + str(i)] = 1         # TODO: Levels shouldn't be 1. They should match Rex's Broadsword art levels
        if next_art_ID < last_AA_ID:              # This is a non-final auto attack, chain them together
            art["NextArts"] = next_art_ID + 1
        next_art_ID = next_art_ID + 1 # Increment counter
    JSONParser.ExtendJSONFile("common/BTL_Arts_Dr.json", [new_auto_attacks_and_arts])

    # Replace Broadsword animations with Shield Hammer
    JSONParser.ChangeJSONLine(["common/ITM_PcWpnType.json"], [17], ['Motion'], 13)



def FixRexStillAfterHeDies(): # Mostly duplicate with the pandoria bugfix, but with different ids, and using the driver table instead of the blade table
    # Get the still of the driver which replaced Rex
    rex_replacement_still = OriginalDrivers[OriginalDriver2Replacement[1]]['Still']

    # Use the still to find the icon index of the driver which replaced Rex
    icon_index = JSONParser.QueryJSONLine("common/MNU_IconList.json", "$id", rex_replacement_still)["icon_index"]

    # Fix the small icon for Rex's replacement. Row 262 corresponds to Rex with Pyra's core crystal
    JSONParser.ChangeJSONLine(["common/MNU_IconList.json"], [262], ['icon_index'], icon_index)

    # Get the driver image for Rex's replacement
    # This includes both the File ID and scaling/cropping information of the image
    RexReplacementImageRow = JSONParser.QueryJSONLine("common/MNU_DrImageID.json", "icon_id", rex_replacement_still)

    # Grab the file name from the File ID
    fileName = JSONParser.QueryJSONLine("common/MNU_Stream_full_dr.json", "$id", RexReplacementImageRow['$id'])['filename']
    fileName_glow = JSONParser.QueryJSONLine("common/MNU_Stream_full_glow_dr.json", "$id", RexReplacementImageRow['$id'])['filename']
    # TODO: Add the glow logic to Pandoria bugfix

    # Replace the image for Rex with his replacement's image. Row 9 corresponds to Rex's portrait with Pyra's core crystal
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_dr.json"], [9], ['filename'], fileName)
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_glow_dr.json"], [9], ['filename'], fileName_glow)

    # Fix the cropping of the image of Rex's replacement. Row 9 corresponds to Rex's portrait with Pyra's core crystal
    for field in ['offs_x', 'offs_y', 'scale', 'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine(["common/MNU_DrImageID.json"], [9], [field], RexReplacementImageRow[field])


# TODO: Unsure if this works, I think it needs a full playthrough. Save right before Jalos to confirm
def FixRexStillMasterDriver(): # Mostly duplicate with the pandoria bugfix, but with different ids, and using the driver table instead of the blade table
    # Get the still of the driver which replaced Rex
    rex_replacement_still = OriginalDrivers[OriginalDriver2Replacement[1]]['Still']

    # Use the still to find the icon index of the driver which replaced Rex
    icon_index = JSONParser.QueryJSONLine("common/MNU_IconList.json", "$id", rex_replacement_still)["icon_index"]

    # Fix the small icon for Rex's replacement. Row 265 corresponds to Rex Master Driver
    JSONParser.ChangeJSONLine(["common/MNU_IconList.json"], [265], ['icon_index'], icon_index)

    # Get the driver image for Rex's replacement
    # This includes both the File ID and scaling/cropping information of the image
    RexReplacementImageRow = JSONParser.QueryJSONLine("common/MNU_DrImageID.json", "icon_id", rex_replacement_still)

    # Grab the file name from the File ID
    fileName = JSONParser.QueryJSONLine("common/MNU_Stream_full_dr.json", "$id", RexReplacementImageRow['$id'])['filename']
    fileName_glow = JSONParser.QueryJSONLine("common/MNU_Stream_full_glow_dr.json", "$id", RexReplacementImageRow['$id'])['filename']
    # TODO: Add the glow logic to Pandoria bugfix

    # Replace the image for Rex with his replacement's image. Row 10 corresponds to Rex's portrait with Master Driver
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_dr.json"], [10], ['filename'], fileName)
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_glow_dr.json"], [10], ['filename'], fileName_glow)

    # Fix the cropping of the image of Rex's replacement. Row 10 corresponds to Rex's portrait with Master Driver
    for field in ['offs_x', 'offs_y', 'scale', 'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine(["common/MNU_DrImageID.json"], [10], [field], RexReplacementImageRow[field])


# Assigns arts to the correct driver, which has since been swapped
def FixDriverArts():
    def callback(art):
        original_driver_id = art["Driver"]
        if original_driver_id in DriversToRandomize:
            art["Driver"] = ReplacementDriver2Original[original_driver_id]
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], [], callback, replaceAll=True)