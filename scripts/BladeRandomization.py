import copy

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

#TODO: Figure out the two different Dagas forms? My randomization creates Dagas 1 I believe


OriginalBlades = dict() # Populated in PopulateBlades()
BladeNames = dict() # Populated in PopulateBlades()
Original2Replacement = dict() # Populated in RandomizeBlades()
Replacement2Original = dict() # Populated in RandomizeBlades()
OriginalGacha = dict() # Populated in PopulateGacha()

BladesWhichCantBeRandomizedAtAll = [1004, 1008]  # Dromarch and Roc cannot be randomized because they are non-human and driver-exclusive

# Keep track of blades which only have arts defined for specific drivers. These blades can appear in gacha, but an overdrive to a compatible driver would be needed to actually use them. They cannot replace the default blade of another driver, as that driver would not be able to use them
RexExclusiveBlades = [1001, 1002, 1011]  # Pyra, Mythra, Nia
MoragExclusiveBlades = [1009]  # Brighid
ZekeExclusiveBlades = [1010]  # Pandoria

ToraExclusiveBlades = [1005, 1006, 1007]  # Poppi

AllHumanoidBladesBesidesPoppi = [1001, 1002, 1009, 1010, 1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1023, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1076, 1104, 1105, 1106, 1107, 1108, 1109, 1111] # Note: Dagas has two entries, 1022 and 1050. The former is his original form, the latter is his true form. We are randomizing the true form into the rotation, NOT the original form.
HumanoidBladesThatArentDriverExclusive = [1014, 1015, 1016, 1017, 1018, 1019, 1020, 1023, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1076, 1104, 1105, 1106, 1107, 1108, 1109, 1111]
NonHumanoidBlades = [1021, 1029, 1032, 1040, 1049]  # Boreas, Ursula, Sheba, Herald, Sever (Race is not 1) (Note: There's 2 Severs, 1042 and 1049. I believe the former is enemy and latter is player)

# TODO: Handle the randomization for Boreas, Ursula, Sheba, Herald, and Sever separetely. They cannot be default blades, but they can remain as either Gacha or item summons. The gacha tables and item summons can be randomized.

def ModifyGachaAvailability(gacha):
    if gacha['Condition'] == 1789:  # NG+
        gacha['Condition'] = 0
    elif gacha['Condition'] == 3219:  # T-elos
        gacha['Condition'] = 0

def UnrelatedQolMods():
    # Speed boost TODO (not part of this feature, but is useful for testing.
    JSONParser.ChangeJSONLineWithCallback(["common/FLD_OwnerBonus.json"], [24], FullSpeedAhead)
    JSONParser.ChangeJSONLineWithCallback(["common/FLD_QuestReward.json"], [151], GimmeThatSpeed)

    # Guaranteed rare blades from gacha
    JSONParser.ChangeJSONFileWithCallback(["common/BLD_RareList.json"], ModifyGachaProbabilityToMakeGuaranteed) # TODO: So I can get everyone from the gacha for testing

    # Make T-elos and Torna blades available in NG
    JSONParser.ChangeJSONFileWithCallback(["common/BLD_RareList.json"], ModifyGachaAvailability)
def InitialSetup():
    JSONParser.ChangeJSONFileWithCallback(["common/CHR_Bl.json"], PopulateBlades)
    JSONParser.ChangeJSONFileWithCallback(["common/BLD_RareList.json"], PopulateGacha)
    JSONParser.ChangeJSONFileWithCallback(["common/BTL_Arts_Dr.json"], MakeAllArtsAccessible)

def BladeRandomization(OptionsRunDict):
    #TODO: Use suboptions?
    #TODO: Include console messages

    UnrelatedQolMods()
    InitialSetup()

    #JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], AllHumanoidBlade, ReplaceBlades) # TODO: Replace with actual randomization
    RandomizeBlades(OptionsRunDict)
    RandomizePoppiForms(OptionsRunDict) # TODO
    RandomizeGachaTable(OptionsRunDict)

    # Fix bug with Zeke? Bug is Zeke fight crashes if a randomized Pandoria has a non-default weapon chip
    #    In my case, I swapped Pandoria and Corvin. The Divine Core Crystal gave Pandoria, and I gave her a weapon between Zekes 1 and 2. Zeke 1 didn't crash, and he used Corvin's attacks. Zeke 2 crashes on startup
    #    Note: I thought of locking Pandoria to a side quest crystal which you get after fighting Zeke (Theory or Herald) but that doesn't work because you fight Zeke in chapter 10.
    JSONParser.ChangeJSONFileWithCallback(["common/CHR_EnArrange.json"], ReplaceEnemyBlades)

def ReplaceBlade(blade, replace_with_id):
    for key, value in blade.items():
        if key in ['$id', 'ReleaseLock', 'CreateEventId']:
            continue
        blade[key] = OriginalBlades[replace_with_id][key]

def ReplaceBlades(blade):
    id = blade['$id']
    if id in Original2Replacement:
        ReplaceBlade(blade, Original2Replacement[id])
    else: # TODO: Most of these are fine, but some of these are duplicates? For example, Pyra, Cressidus, and Herald (amongst others)
        print(BladeNames[id] + '(' + str(id) + ') was not randomized')

def canBeReplaced(original, replacement):
    # Note: Rex can be the master driver, so it's fine if his blades get randomized to whoever

    if original == 1009: #Brighid
        return not (replacement in RexExclusiveBlades or replacement in ZekeExclusiveBlades)
    if original == 1014: #Aegeaon
        return not (replacement in RexExclusiveBlades or replacement in ZekeExclusiveBlades)
    if original == 1010: #Pandoria
        return not (replacement in RexExclusiveBlades or replacement in MoragExclusiveBlades)

    # Are there any other exceptions?
    return True

def RandomizeBlades(OptionsRunDict):
    # Note: It is important that BladesLeftToRandomize starts with the default blades,
    # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
    blades_left_to_randomize = AllHumanoidBladesBesidesPoppi.copy()
    randomized_order = blades_left_to_randomize.copy()
    random.shuffle(randomized_order)

    # Determine the randomization prior to randomizing.
    # This way we can populate Original2Replacement and Replacement2Original,
    # which will be needed later on for various reasons
    while blades_left_to_randomize:
        next_blade = blades_left_to_randomize[0]
        next_replacement = randomized_order[0]
        if canBeReplaced(next_blade, next_replacement):
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

    # Populate non-randomized blades into the same map, so we can look it up later if needed
    for blade in NonHumanoidBlades:
        Original2Replacement[blade] = blade
        Replacement2Original[blade] = blade

    # Apply Randomizations
    JSONParser.ChangeJSONFileWithCallback(["common/CHR_Bl.json"], ReplaceBlades)

def RandomizePoppiForms(OptionsRunDict):
    print('RandomizePoppiForms()')
    # TODO: Randomize Poppi
    # TODO: How do I make it so the poppiswaps are in the right spot

OriginalGacha2ReplacementBlade = dict()
def RandomizeGachaTable(OptionsRunDict):
    # This Function exists to randomize gacha rows. Both the random gacha (Godfrey, Perceval, Vale, ...)
    # as well as predetermined gacha (Kasandra, Sheba, Herald, ...)
    # While it's true that blades like Corvin will already be randomized, some of these blades
    # (Ursula, Boreas, Herald, etc) can only be randomized like this. At least it's something...

    # Note: It is important that gacha_left_to_randomize starts with Aegeaon's row,
    # as otherwise the below loop could be stuck indefinitely if the last replacement is incompatible
    gacha_left_to_randomize = [30] + [x for x in Helper.InclRange(1,29)] + [x for x in Helper.InclRange(31,37)]
    randomized_order = gacha_left_to_randomize.copy()
    random.shuffle(randomized_order)

    while gacha_left_to_randomize:
        next_gacha = gacha_left_to_randomize[0]
        next_replacement = randomized_order[0]

        original_gacha_blade = OriginalGacha[next_gacha]

        next_gacha_blade = Original2Replacement[OriginalGacha[next_gacha]]

        # Replace original Dagas with true form Dagas in the gacha table
        if next_replacement == 7:
            next_replacement_blade = 1050
        else:
            next_replacement_blade = Original2Replacement[OriginalGacha[next_replacement]]

        # Note: original gacha blade is checked just because of Aegeon (forced to Morag, so must be compatable with Morag)
        if canBeReplaced(original_gacha_blade, next_replacement_blade):
            OriginalGacha2ReplacementBlade[next_gacha] = next_replacement_blade
            print('===========================================')
            print('gacha blade ' + BladeNames[next_gacha_blade] + ' (originally ' + BladeNames[original_gacha_blade] + ') was replaced with ' + BladeNames[next_replacement_blade])
            print('gacha blade ' + str(next_gacha_blade) + ' (originally ' + str(original_gacha_blade) + ') was replaced with ' + str(next_replacement_blade))
            del gacha_left_to_randomize[0]
            del randomized_order[0]
        else:
            # Next blade doesn't work, randomize again
            random.shuffle(randomized_order)

    JSONParser.ChangeJSONFileWithCallback(["common/BLD_RareList.json"], ReplaceGacha)

def ReplaceGacha(gacha):
    gacha['Blade'] = OriginalGacha2ReplacementBlade[gacha['$id']]

def ReplaceEnemyBlades(enemy):
    if enemy['BladeID'] in Original2Replacement:
        enemy['BladeID'] = Original2Replacement[enemy['BladeID']]

    # TODO: Do this with all blades
    #if enemy['BladeID'] == Pandoria:
    #    enemy['BladeID'] = Corvin

def MakeAllArtsAccessible(art):
    # Cap level requirements at level 10
    # In a normal playthrough, these arts only really matter for Aegis Sword, as that affects the
    # Junk Sword arts. However, a handful of arts have high enough requirements that Rex can't use
    # it if randomization gives him Brighid or Pandoria early on. For simplicity and potential
    # future-proofing, just cap all arts at 4. This is Rex's minimum level when he gets his first blade.
    # This is chosen instead of 1 just so the Junk Sword still behaves as intended
    for i in Helper.InclRange(1,5):
        if art['ReleaseLv' + str(i)] > 4:
            art['ReleaseLv' + str(i)] = 4

def FullSpeedAhead(deed):  # increases movement speed from the deed
    deed['Value'] = 10000

def GimmeThatSpeed(rewards):  # rewards the movement deed in the tutorial
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

# def MoveMythrasCosmeticsToKassandra(accessory):
#     # TODO: Do this for all cosmetics
#     # TODO: Find the ID for Melee Mythra. Perhaps replace all aux core names with their ID so we can find it easier
#     #accessory['Blade'] = Kasandra
#     print(accessory)

