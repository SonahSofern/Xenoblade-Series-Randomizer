import Options, CharacterRandomization
import copy, random
from scripts import JSONParser, Helper

OriginalDrivers = dict()        # Maps Driver ID to the dictionary of the unrandomized driver date. Populated in PopulateDrivers()
DriverNames = dict()            # Maps ID to Driver Name. Populated in PopulateDrivers()
OriginalDriver2Replacement = dict()  # Maps Unrandomized Driver ID to Randomized Driver ID. Populated in RandomizeDrivers()
ReplacementDriver2Original = dict()  # Maps Randomized Driver ID to Unrandomized Driver ID. Populated in RandomizeDrivers()

PermanentDriversToRandomize = [1, 2, 3, 6]

include_printouts = True  # Debugging

#TODO: Due to conflicts between driver randomization and blade randomization, they may need to be part of the same file. Whoever runs first runs the pre-randomization bug fixes. Whoever runs second handles the post-randomization fixes

OriginalBlades = dict()        # Maps Blade ID to the dictionary of the unrandomized blade date. Populated in PopulateBlades()
BladeNames = dict()            # Maps ID to Blade Name. Populated in PopulateBlades()
OriginalBlade2Replacement = dict()  # Maps Unrandomized Blade ID to Randomized Blade ID. Populated in RandomizeBlades()
ReplacementBlade2Original = dict()  # Maps Randomized Blade ID to Unrandomized Blade ID. Populated in RandomizeBlades()

# TODO:
#  The blade which replaces Pyra still has Pyra's default weapon of Aegis sword. Presumably I fixed this on the blade randomization...
#  - This could be a save file issue. I should try from a fresh save
#  Master driver Rex needs to have his icon replaced (probably similar to Pandoria, I feel like that's hardcoded)
#  Small icons for all drivers need to be fixed (in the blade menu where it shows which driver belongs to the blade)
#  Drivers join the party at different levels. Zeke just joined the party at level 7 (and can Inn to 10) when he replaces Rex

# TODO:
#  Do skill trees on randomized drivers work?
#  - Currently, Nia has Rex's skill tree
#  Can Zeke use eye of shining justice? Can his replacement?
#  Instead of swapping blades, can I just define arts like I do for broadsword (so Nia can use Pyra, for example) Specials might be broken

def Driver():
    # TODO: Move all the logic after this function to CharacterRandomization
    #       Once everything is moved, this file can go away
    #       The option needs to call CharacterRandomization.CharacterRandomization() instead of this function
    CharacterRandomization.CharacterRandomization()

    InitialSetup()

    RandomizeDrivers()
    SwapDefaultBlades()

    BugFixes_PostRandomization() # TODO: This is a dupe from BladeRandomization, and I'm not sure if it conflicts with it

    DefineBroadswordArtsForRexsReplacement()
    FixRexStillAfterHeDies()
    FixRexStillMasterDriver()
    FixArts()

    #JSONParser.PrintTable("common/CHR_Dr.json")
    #JSONParser.PrintTable("common/BTL_Arts_Dr.json")

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


# TODO: This is code duplication with BladeRandomization
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


def RandomizeDrivers():
    drivers_left_to_randomize = PermanentDriversToRandomize.copy()

    randomized_order = drivers_left_to_randomize.copy()
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

# Assigns arts to the correct driver, which has since been swapped
def FixArts():
    def callback(art):
        original_driver_id = art["Driver"]
        if original_driver_id in PermanentDriversToRandomize:
            art["Driver"] = ReplacementDriver2Original[original_driver_id]
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], [], callback, replaceAll=True)

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


def DefineBroadswordArtsForRexsReplacement():
    rexs_replacement = OriginalDriver2Replacement[1]

    # If Rex was not replaced, bail
    if rexs_replacement == 1:
        return

    # TODO: Instead of Monado, copy shield hammer and increase the speed
    #       I don't want words like "Monado" in the art names is all
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
    for original_driver_id in PermanentDriversToRandomize:
        replacement_driver_id = OriginalDriver2Replacement[original_driver_id]

        original_blade_id = original_driver_to_primary_blade[original_driver_id]
        replacement_blade_id = original_driver_to_primary_blade[replacement_driver_id]

        OriginalBlade2Replacement[original_blade_id] = replacement_blade_id
        ReplacementBlade2Original[replacement_blade_id] = original_blade_id

        if include_printouts:
            print('========================================')
            print(BladeNames[original_blade_id] + ' was replaced with ' + BladeNames[replacement_blade_id])
            print(str(original_blade_id) + ' was replaced with ' + str(replacement_blade_id))

    # Swap Mythra (and only mythra) with the secondary blades
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
            print("Rex was not replaced.")
            print("- Pneuma remains unchanged.")
            print("- No core crystals were renamed")
        case 2: # Rex Replaced by Nia
            print("Rex replaced by Nia.")
            print("- Replaced Pneuma with Savage Dromarch with the Meteorite Rings")
            print("- Renamed Crossette's crystal to Aegis Core Crystal (since Crossette and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1004
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100501")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5179) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
            JSONParser.ChangeJSONLine(["common_ms/itm_crystal.json"], [15], ['name'], 'Aegis Core Crystal')
        case 3: # Rex replaced by Zeke
            print("Rex replaced by Zeke.")
            print("- Replaced Pneuma with Mermaid Blue Pandoria with the Meteorite Edge")
            print("- Renamed Corvin's crystal to Aegis Core Crystal (since Corvin and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1010
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl100901")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5479) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma
        case 6: # Rex Replaced by Morag
            print("Rex replaced by Morag.")
            print("- Replaced Pneuma with Jade Orchid Brighid with the Meteorite Whips")
            print("- Renamed Aegaeon's crystal to Aegis Core Crystal (since Aegeaon and Mythra swapped)")
            OriginalBlade2Replacement[1003] = 1009
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['Model'], "bl/bl121001")
            JSONParser.ChangeJSONLine(["common/CHR_Bl.json"], [1003], ['DefWeapon'], 5419) #TODO: Custom weapon? The strongest weapons are much weaker than base Pneuma


    # Apply Swaps
    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], [], ApplyBladeSwaps, replaceAll=True)

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


# TODO: Unsure if this works, I think it needs a full playthough. Save right before jalos to confirm
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













# TODO: This is code duplication with BladeRandomization
def ApplyBladeSwaps(blade):
    # Certain field skills are not randomized for progression reasons
    excluded_field_skills = dict()
    excluded_field_skills[1001] = ['FSkill1', 'FSkill2', 'FSkill3']  # Pyra: Fire Mastery, Focus, Cooking
    excluded_field_skills[1005] = ['FSkill3']  # Poppi Alpha: Superstrength
    excluded_field_skills[1008] = ['FSkill2']  # Roc: Miasma Dispersal

    blade_id = blade['$id']
    if blade_id in OriginalBlade2Replacement:
        replace_with_id = OriginalBlade2Replacement[blade_id]

        # Copy all fields (except ID, ReleaseLock, and the excluded field skills)
        # from the replacement blade to the original blade
        for key, value in blade.items():
            # Pneuma should not have default weapons replaced (they are explicitly set before calling this function
            if blade_id == 1003 and key in ["DefWeapon", "Model"]:
                continue
            if key in ['$id', 'ReleaseLock']:
                continue
            if blade_id in excluded_field_skills and key in excluded_field_skills[blade_id]:
                continue
            if key == 'Flag':
                for flag_key, flag_value in OriginalBlades[replace_with_id]['Flag'].items():
                    if flag_key in ['FreeEngage', 'NoMapRev']:
                        continue

                    blade['Flag'][flag_key] = OriginalBlades[replace_with_id]['Flag'][flag_key]
            else:
                blade[key] = OriginalBlades[replace_with_id][key]

# TODO: This is code duplication with BladeRandomization
def BugFixes_PostRandomization():
    #JSONParser.ChangeJSONLineWithCallback(["common/CHR_EnArrange.json"], [], FixRandomizedEnemyBladeCrashes, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/EVT_cutscene_wp.json"], [],  FixCutsceneCrashForNotHavingTwoWeapons, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_OrbEquip.json"], [], FixCosmetics, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common/ITM_HanaAssist.json"], [], FixCosmetics, replaceAll=True)
    FixPandoriaSpriteAfterElpys()
    FixMenuText()

# Unsure why, but it is possible for the game to crash when an enemy blade gets randomized (for example, Pandoria).
# Replace the enemy version of the blade with the blade who that enemy replaced.
# TODO: Investigate the crash and see if it becomes possible to resolve while preserving the randomization. It would be
#       cool to fight against Zeke with Pandoria replaced with something else. But for now, this is not the case.
#def FixRandomizedEnemyBladeCrashes(enemy):
#    if enemy['BladeID'] in Replacement2Original:
#        if include_printouts:
#            print("Enemy: " + BladeNames[enemy['BladeID']] + " (" + str(enemy['BladeID']) + ") was replaced with " + BladeNames[Replacement2Original[enemy['BladeID']]] + " (" + str(Replacement2Original[enemy['BladeID']]) + ")")
#        enemy['BladeID'] = Replacement2Original[enemy['BladeID']]

# When randomizing blades, there is a bug where cutscenes will crash when attempting to load. This is caused because in 2 ways
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

    # Replace the image for Pandoria with her replacement's image. Row 50 corresponds to Pandoria's portrait with transparent glasses
    JSONParser.ChangeJSONLine(["common/MNU_Stream_full_bl.json"], [50], ['filename'], fileName)

    # Fix the cropping of the image of Pandoria's replacement. Row 50 corresponds to Pandoria's portrait with transparent glasses
    for field in ['offs_x', 'offs_y', 'scale', 'offs_x2', 'offs_y2', 'scale2', 'offs_x3', 'offs_y3', 'scale3', 'offs_x4', 'offs_y4', 'scale4', 'offs_x5', 'offs_y5', 'scale5']:
        JSONParser.ChangeJSONLine(["common/MNU_BlImageID.json"], [50], [field], PandoriaReplacementImageRow[field])

def FixMenuText():
    # Zeke's Eye of Shining Justice Skill
    #JSONParser.ChangeJSONLine(["common_ms/btl_enhance_cap.json"], [294], ['name'], 'At max Affinity w/ ' + BladeNames[Original2Replacement[1010]] + ': R and +\nto awaken for a time (once per battle).')

    # Switch between Driver/Blade Nia text
    #if Original2Replacement[1011] != 1011:
    #    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [261], ['name'], 'Turn Nia into ' + BladeNames[Original2Replacement[1011]] + '?''')
    #    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [262], ['name'], 'Turn ' + BladeNames[Original2Replacement[1011]] + ' into Nia?')
    #    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [297], ['name'], 'You cannot turn ' + BladeNames[Original2Replacement[1011]] + ' into Nia because\nno other Blades are engaged.')

    # Swap to between Pyra/Mythra text
    # Note: The words "Swap to" have been intentionally dropped because any blade which a name longer than 6 letters gets cut off
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [260], ['name'], 'Changing to ' + BladeNames[OriginalBlade2Replacement[1001]] + '. Is this OK?')
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [259], ['name'], 'Changing to ' + BladeNames[OriginalBlade2Replacement[1002]] + '. Is this OK?')
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [89], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # "Swap to" Text
    JSONParser.ChangeJSONLine(["common_ms/menu_operation_info_ms.json"], [90], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # "Swap to" Text

    # Pyra/Mythra choice text
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [1], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # Pneuma's name when "Pyra" is selected
    JSONParser.ChangeJSONLine(["common_ms/cmm_homuri_name_ms.json"], [2], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # Pneuma's name when "Mythra" is selected
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1736], ['name'], BladeNames[OriginalBlade2Replacement[1001]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"], [1737], ['name'], BladeNames[OriginalBlade2Replacement[1002]]) # The choice selection
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [257], ['name'], 'The name will be set to "' + BladeNames[OriginalBlade2Replacement[1001]] + '". Is this OK?')
    JSONParser.ChangeJSONLine(["common_ms/menu_cmnwindow.json"], [258], ['name'], 'The name will be set to "' + BladeNames[OriginalBlade2Replacement[1002]] + '". Is this OK?')
