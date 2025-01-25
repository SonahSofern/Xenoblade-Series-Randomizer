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
# 3. After the scene in Elpys where Pandoria's glasses become transparent, Corvin's sprite in the menu (and only the menu) becomes Pandoria again (with the transparent glasses). Everything else is still Corvin
# 3a. After this scene, Corvin should still appear as Corvin. Pandoria (on Rex) should now appear with transparent glasses
# 4. Since it's based on poppiswap, Poppi has no abilities on her specials
# 5. No combination of Godfrey/Wulfric or Pyra/Nia's do the special tier 4.


#TODO: Things to try
# 3. Can I use poppiswap on Crossette to modify Poppi? (cannot be tested until Poppi and Crossette get arts for other characters)

# TODO: ChangeJSONFileWithCallback() could probably be renamed to be clearer.

# TODO: all functions which actually modify the tables should be renamed to start with "apply". This will differentiate between determining the calculations and applying them

OriginalBlades = dict() # Populated in PopulateBlades()
BladeNames = dict() # Populated in PopulateBlades()
Original2Replacement = dict() # Populated in RandomizeBlades()
Replacement2Original = dict() # Populated in RandomizeBlades()
OriginalGacha = dict() # Populated in PopulateGacha()

# TODO: Is this used? If not, should at least be documented here
BladesWhichCantBeRandomizedAtAll = [1004, 1008]  # Dromarch and Roc cannot be randomized because they are non-human and driver-exclusive

# Keep track of blades which only have arts defined for specific drivers. These blades can appear in gacha, but an overdrive to a compatible driver would be needed to actually use them. They cannot replace the default blade of another driver, as that driver would not be able to use them
RexExclusiveBlades = [1001, 1002, 1011]  # Pyra, Mythra, Nia
MoragExclusiveBlades = [1009]  # Brighid
ZekeExclusiveBlades = [1010]  # Pandoria

# TODO: Is this used?
ToraExclusiveBlades = [1005, 1006, 1007]  # Poppi

AllHumanoidBladesBesidesPoppi = [1001, 1002, 1009, 1010, 1011, 1014, 1015, 1029, 1016, 1017, 1018, 1019, 1020, 1023, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1076, 1104, 1105, 1106, 1107, 1108, 1109, 1111] # Note: Dagas has two entries, 1022 and 1050. The former is his original form, the latter is his true form. We are randomizing the true form into the rotation, NOT the original form.
HumanoidBladesThatArentDriverExclusive = [1014, 1015, 1016, 1017, 1018, 1019, 1020, 1023, 1024, 1025, 1026, 1027, 1028, 1030, 1031, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1076, 1104, 1105, 1106, 1107, 1108, 1109, 1111] # TODO: Is this used?
NonHumanoidBlades = [1021, 1029, 1032, 1040, 1049]  # Boreas, Ursula, Sheba, Herald, Sever (Race is not 1) (Note: There's 2 Severs, 1042 and 1049. I believe the former is enemy and latter is player)

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

# side is either L or R (case doesn't matter). Could also be the words 'left' and 'right', I don't really care
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

    #JSONParser.ChangeJSONLineWithCallback(["common/CHR_Bl.json"], AllHumanoidBlade, ReplaceBlades) # TODO: Replace with actual randomization
    RandomizeBlades(OptionsRunDict)
    RandomizePoppiForms(OptionsRunDict) # TODO
    RandomizeGachaTable(OptionsRunDict)

    # Fix bug with Zeke? Bug is Zeke fight crashes if a randomized Pandoria has a non-default weapon chip
    #    In my case, I swapped Pandoria and Corvin. The Divine Core Crystal gave Pandoria, and I gave her a weapon between Zekes 1 and 2. Zeke 1 didn't crash, and he used Corvin's attacks. Zeke 2 crashes on startup
    #    Note: I thought of locking Pandoria to a side quest crystal which you get after fighting Zeke (Theory or Herald) but that doesn't work because you fight Zeke in chapter 10.
    JSONParser.ChangeJSONFileWithCallback(["common/CHR_EnArrange.json"], ReplaceEnemyBlades)

    BugFixes()

    FinalTouches()

    #search_bdat("R")
    #search_bdat("L")
    #search_bdat("Nia")
    #search_bdat("Pyra")
    #search_bdat("Mythra")
    #search_bdat("Pandoria")
    #search_bdat("wp070101")

def ReplaceBlade(blade, replace_with_id):
    # Note: DefWeapon changes their initial arts. However, it is needed because cutscenes can crash if the wrong weapon is loaded
    # I do not know if this affects every weapon or not, but I suspect it has something to do with Brighid's
    for key, value in blade.items():
        #if key in ['$id', 'ReleaseLock', 'DefWeapon']:
        if key in ['$id', 'ReleaseLock']:
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
        #return replacement == 1027 # Force Brighid to be Kora, for testing (Works)
        #return replacement == 1045 # Force Brighid to be Mikhail, for testing (Works)
        #return replacement == 1029 # Force Brighid to be Ursula, for testing (Works)
        return replacement == 1016 # Force Brighid to be Wulfric, for testing (Crashes in cutscene)
        #return not (replacement in RexExclusiveBlades or replacement in ZekeExclusiveBlades)
        #return replacement == 1009 # Don't randomize brighid, for now
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
    print('TODO: RandomizePoppiForms()')
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
        if next_replacement == 7: # TODO: Is this check still needed? I think he's swapped already when populating OriginalGacha
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
    x = 5
    #if enemy['BladeID'] in Original2Replacement:
    #    enemy['BladeID'] = Original2Replacement[enemy['BladeID']]

    # TODO: Do this with all blades
    #if enemy['BladeID'] == Pandoria:
    #    enemy['BladeID'] = Corvin

def MakeAllArtsAccessible(art):
    # Cap level requirements at level 10
    # In a normal playthrough, these arts only really matter for Aegis Sword, as that affects the
    # Junk Sword arts. However, a handful of arts have high enough requirements that Rex can't use
    # it if randomization gives him Brighid or Pandoria early on. For simplicity and potential
    # future-proofing, just cap all arts at 3. This is Rex's minimum level when he gets his first blade.
    # This is chosen instead of 1 just so the Junk Sword still behaves as intended prior to getting Pyra
    for i in Helper.InclRange(1,5):
        if art['ReleaseLv' + str(i)] > 3:
            art['ReleaseLv' + str(i)] = 3

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

def BugFixes():
    def FixCutsceneCrashForNotHavingTwoWeapons(weapon):
        # TODO: This doesn't seem to work.
        #  Instead, try hardcoding a valid weapon instead of using the offhand one
        #  (I'm wondering if there's something specific where a left handed weapon
        #  just simply cannot be used in the right hand and vice versa)
        print('')
        #weapon['RscR'] = 121
        #weapon['RscL'] = 120
        #if weapon['RscR'] == 0:
        #    weapon['RscR'] = weapon['RscL']
        #if weapon['RscL'] == 0:
        #    weapon['RscL'] = weapon['RscR']

    def FixCutsceneCrashForNotHavingTwoWeapons2(cutscene):
        # TODO: This doesn't seem to work.
        #  Instead, try hardcoding a valid weapon instead of using the offhand one
        #  (I'm wondering if there's something specific where a left handed weapon
        #  just simply cannot be used in the right hand and vice versa)
        print(cutscene)

        # TODO: Doesn't crash
        #if (cutscene['$id'] == 13):
        #    cutscene['resourceL'] = 'wp090101_l' # Dual Scythes, I believe
        #    cutscene['resourceR'] = 'wp090101_r' # Dual Scythes, I believe

        original = cutscene['blade']

        # Bail if this blade was not randomized
        if original not in Original2Replacement:
            return

        replacement = Original2Replacement[original]

        print("======================= Resource Modifications")
        print("Original Blade: " + BladeNames[original])
        print("Original Weapon Type" + str(OriginalBlades[original]['WeaponType']))
        print("Original resource (R): " + cutscene['resourceR'])
        print("Original resource (L): " + cutscene['resourceL'])
        print("----")
        print("New Blade: " + BladeNames[replacement])
        print("New Weapon Type" + str(OriginalBlades[replacement]['WeaponType']))
        print("New Resource (R): " + WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'R'))
        print("New resource (L): " + WeaponType2Resource(OriginalBlades[replacement]['WeaponType'], 'L'))
        print("=======================")

        # TODO: Works
        if (cutscene['$id'] == 13):
            cutscene['resourceL'] = 'wp110101' # Megalance, I believe
            cutscene['resourceR'] = 'wp110101' # Megalance, I believe

        # TODO: Crashes
        #if (cutscene['$id'] == 12):
        #    cutscene['resourceL'] = 'wp090101_l' # Dual Scythes, I believe
        #    cutscene['resourceR'] = 'wp090101_r' # Dual Scythes, I believe

        # If there is a weapon not defined, just replace it with a known, valid resource (whipsword in this case)
        # This can happen in cases of dual wielded weapons being replaced with single-hand weapons,
        # as the cutscene will try to load the off-hand weapon, which is not defined
        #if cutscene['resourceR'] == '':
        #    cutscene['resourceR'] = 'wp090101_r'
        #if cutscene['resourceL'] == '':
        #    cutscene['resourceL'] = 'wp090101_l'

        #if cutscene['resourceR'] == '':
        #    cutscene['resourceR'] = weapon['resourceL']
        #if cutscene['resourceL'] == '':
        #    cutscene['resourceL'] = weapon['resourceR']


    JSONParser.ChangeJSONFileWithCallback(["common/ITM_PcWpn.json"], FixCutsceneCrashForNotHavingTwoWeapons)
    #JSONParser.ChangeJSONFileWithCallback(["common/BTL_Wpn_En.json"], FixCutsceneCrashForNotHavingTwoWeapons)
    JSONParser.ChangeJSONFileWithCallback(["common/EVT_cutscene_wp.json"], FixCutsceneCrashForNotHavingTwoWeapons2)

# TODO: Having all ITM_PcWpn be 121 and 120 while also having all EVT_cutscene_wp set to wp090101_r and wp090101_l seems to work.
# TODO: Having all ITM_PcWpn be 121 and 120 while NOT having all EVT_cutscene_wp set to wp090101_r and wp090101_l causes a crash
# TODO: NOT having ITM_PcWpn be 121 and 120 while having all EVT_cutscene_wp set to wp090101_r and wp090101_l seems to work




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














import requests
from bs4 import BeautifulSoup

def fetch_hyperlinks(base_url):
    """Fetch all hyperlinks from the base webpage."""
    response = requests.get(base_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch base URL: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'].replace('\\', '/'))  # Correct backslashes to forward slashes

    return links

def search_tables_in_pages(base_url, links, search_string):
    """Search for the given string in the tables of each linked webpage."""
    matching_pages = []

    for link in links:
        full_url = base_url.rstrip('/') + '/' + link
        response = requests.get(full_url)

        if response.status_code != 200:
            print(f"Failed to fetch {full_url}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        for table in tables:
            # Get all hyperlinks in the table
            hyperlinks = [a.get_text().lower() for a in table.find_all('a')]

            # Check if search_string is in table text but not in any hyperlink text
            table_text = table.get_text().lower()
            if search_string.lower() in table_text and all(search_string.lower() not in link for link in hyperlinks):
                matching_pages.append(full_url)
                print(full_url)
                break  # No need to check more tables on this page

    return matching_pages

def search_table_headers_in_pages_ends_with(base_url, links, search_string):
    """Search for the given string in the tables of each linked webpage."""
    matching_pages = []

    for link in links:
        full_url = base_url.rstrip('/') + '/' + link
        response = requests.get(full_url)

        if response.status_code != 200:
            print(f"Failed to fetch {full_url}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all('th')

        for header in headers:
           # Check if header text ends with the search string
            if header.get_text().endswith(search_string):
                matching_pages.append(full_url)
                break  # No need to check more tables on this page

    return matching_pages

def search_bdat(search_string):
    base_url = "https://xenoblade.github.io/xb2/bdat/index.html"

    print('Search String: ' + search_string)

    try:
        print("Fetching hyperlinks...")
        links = fetch_hyperlinks(base_url)
        print(f"Found {len(links)} links.")

        #matching_pages = search_tables_in_pages(base_url.rsplit('/', 1)[0], links, search_string)
        matching_pages = search_table_headers_in_pages_ends_with(base_url.rsplit('/', 1)[0], links, search_string)

        if matching_pages:
            print(f"Found the string on the following pages:")
            for page in matching_pages:
                print(page)
        else:
            print("No pages contain the given search string outside hyperlinks.")

    except Exception as e:
        print(f"An error occurred: {e}")
