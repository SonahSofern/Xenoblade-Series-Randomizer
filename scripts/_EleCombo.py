import JSONParser, Helper, Options, copy, random

Name2Elem = dict()
OriginalID2Name = dict()

# First key is ComboStage. Second key is name. Content is dictionary of original bdat
OriginalCombos = {
    1: dict(),
    2: dict(),
    3: dict()
}

# Key is ID. This is used to look up the entire route when randomizing combos 2 and 3
ReplacedCombos = dict()
ReplacedComboRoutes = list()

CustomLevel2s = list()
CustomLevel3Templates = dict()

class Level2Combo:
    def __init__(self, name, elemRoute, baseName, tier3adjectives):
        random.shuffle(tier3adjectives)
        self.elemRoute = list()
        for elem in elemRoute:
            self.elemRoute.append(Name2Elem[elem])
        self.name = name
        self.base = copy.deepcopy(OriginalCombos[2][baseName])
        self.tier3adjectives = tier3adjectives

        CustomLevel2s.append(self)

class Level3ComboTemplate:
    def __init__(self, elem, nameNouns, baseNames):
        # Shuffle the names and bases while making sure the indices still correspond with each other
        combined = list(zip(nameNouns, baseNames))
        random.shuffle(combined)
        nameNouns_shuffled, baseNames_shuffled = zip(*combined)
        nameNouns = list(nameNouns_shuffled)
        baseNames = list(baseNames_shuffled)

        self.elem = Name2Elem[elem]
        self.nameNouns = nameNouns
        self.bases = list()
        for baseName in baseNames:
            self.bases.append(copy.deepcopy(OriginalCombos[3][baseName]))

        CustomLevel3Templates[self.elem] = self

def CreateCustomCombos():
    # Every combination of first 2 stages are defined with a custom name.
    # Some of these already exist in the base game and are duplicated here for convenience
    # Each custom combo has a "base" of an existing blade combo. It copies all damage, animations, etc. of that base
    # Each custom combo also contains 2 adjectives which become the beginning of the following stage 3's names
    Level2Combo('Burnout', ['Fire', 'Fire'], 'Burnout', ['Scorching', 'Searing'])
    Level2Combo('Steam Bomb', ['Fire', 'Water'], 'Steam Bomb', ['Steamy', 'Vaporous'])
    Level2Combo('Ember Quake', ['Fire', 'Earth'], 'Volcano', ['Smoldering', 'Techtonic'])
    Level2Combo('Plasma Flare', ['Fire', 'Electric'], 'Flame Bolt', ['Electrified', 'Plasmatic'])
    Level2Combo('Frostfire', ['Fire', 'Ice'], 'Burnout', ['Pyrofrigid', 'Frostburning'])
    Level2Combo('Blazing Zephyr', ['Fire', 'Wind'], 'Cyclone', ['Fervent', 'Blistering'])
    Level2Combo('Hellfire', ['Fire', 'Dark'], 'Volcano', ['Infernal', 'Malevolent'])
    Level2Combo('Solar Flare', ['Fire', 'Light'], 'Gamma Ray', ['Incandescent', 'Brilliant'])
    Level2Combo('Boiling Point', ['Water', 'Fire'], 'Steam Bomb', ['Scalding', 'Simmering'])
    Level2Combo('Venom Water', ['Water', 'Water'], 'Venom Water', ['Venomous', 'Toxic'])
    Level2Combo('Pandemic', ['Water', 'Earth'], 'Pandemic', ['Infectious', 'Virulent'])
    Level2Combo('Conductivity', ['Water', 'Electric'], '1,000,000 Volt', ['Voltaic', 'Cascading'])
    Level2Combo('Glacier Surge', ['Water', 'Ice'], 'Freeze', ['Glacial', 'Raging'])
    Level2Combo('Maelstrom Gale', ['Water', 'Wind'], 'Ice Wind', ['Turbulent', 'Whirling'])
    Level2Combo('Abyssal Tide', ['Water', 'Dark'], 'Black Abyss', ['Abyssal', 'Dismal'])
    Level2Combo('Holy Rain', ['Water', 'Light'], 'Steam Bomb', ['Sacred', 'Celestial'])
    Level2Combo('Volcano', ['Earth', 'Fire'], 'Volcano', ['Volcanic', 'Eruptive'])
    Level2Combo('Mudslide', ['Earth', 'Water'], 'Venom Water', ['Raging', 'Corrosive'])
    Level2Combo('Gaia Crash', ['Earth', 'Earth'], 'Gaia Crash', ['Primordial', 'Terrestrial'])
    Level2Combo('Aftershock', ['Earth', 'Electric'], 'Flame Bolt', ['Seismic', 'Jolting'])
    Level2Combo('Glacial Rift', ['Earth', 'Ice'], 'Freeze', ['Glacial', 'Fractured'])
    Level2Combo('Dust Devil', ['Earth', 'Wind'], 'Cyclone', ['Arid', 'Gritty'])
    Level2Combo('Tombstone', ['Earth', 'Dark'], 'Gaia Crash', ['Undead', 'Necromantic'])
    Level2Combo('Earthlight', ['Earth', 'Light'], 'Gamma Ray', ['Resplendent', 'Luminous'])
    Level2Combo('Flame Bolt', ['Electric', 'Fire'], 'Flame Bolt', ['Pyrocharged', 'Sparking'])
    Level2Combo('Shockwave', ['Electric', 'Water'], 'Pandemic', ['Thunderous', 'Surging'])
    Level2Combo('Voltquake', ['Electric', 'Earth'], 'Gaia Crash', ['Voltanic', 'Quaking'])
    Level2Combo('1,000,000 Volt', ['Electric', 'Electric'], '1,000,000 Volt', ['Dynamic', 'Overcharged'])
    Level2Combo('Cryocharge', ['Electric', 'Ice'], 'Lightning Bolt', ['Cryogenic', 'Frigid'])
    Level2Combo('Cumulonimbus ', ['Electric', 'Wind'], 'Lightning Bolt', ['Galvanic', 'Turbulent'])
    Level2Combo('Shadow Spark', ['Electric', 'Dark'], 'Pandemic', ['Umbral', 'Flickering'])
    Level2Combo('Radiant Charge', ['Electric', 'Light'], 'Gamma Ray', ['Incandescent', 'Vibrant'])
    Level2Combo('Scorched Frost', ['Ice', 'Fire'], 'Burnout', ['Frostburned', 'Chillscorched'])
    Level2Combo('Cold Snap', ['Ice', 'Water'], 'Cold Snap', ['Brisk', 'Frigid'])
    Level2Combo('Permafrost', ['Ice', 'Earth'], 'Freeze', ['Cryolithic', 'Icelocked'])
    Level2Combo('Frozen Current', ['Ice', 'Electric'], 'Lightning Bolt', ['Icy', 'Surging'])
    Level2Combo('Freeze', ['Ice', 'Ice'], 'Freeze', ['Glacial', 'Frosty'])
    Level2Combo('Hailstorm', ['Ice', 'Wind'], 'Cold Snap', ['Wintry', 'Blustery'])
    Level2Combo('Frostbite', ['Ice', 'Dark'], 'Ice Wind', ['Numbing', 'Absolute'])
    Level2Combo('Diamond Flash', ['Ice', 'Light'], '1,000,000 Volt', ['Brilliant', 'Prismatic'])
    Level2Combo('Firestorm', ['Wind', 'Fire'], 'Volcano', ['Roaring', 'Incendiary'])
    Level2Combo('Rainstorm', ['Wind', 'Water'], 'Steam Bomb', ['Torrential', 'Pluvial'])
    Level2Combo('Sand Strike', ['Wind', 'Earth'], 'Gaia Crash', ['Swirling', 'Gritty'])
    Level2Combo('Thunderstorm', ['Wind', 'Electric'], '1,000,000 Volt', ['Thunderous', 'Electrified'])
    Level2Combo('Ice Wind', ['Wind', 'Ice'], 'Ice Wind', ['Chilly', 'Gusty'])
    Level2Combo('Cyclone', ['Wind', 'Wind'], 'Cyclone', ['Cyclonic', 'Whirling'])
    Level2Combo('Twilight Tempest', ['Wind', 'Dark'], 'Ray of Light', ['Dusky', 'Brooding'])
    Level2Combo('Aurora Gale', ['Wind', 'Light'], 'Cold Snap', ['Ethereal', 'Radiant'])
    Level2Combo('Campfire ', ['Dark', 'Fire'], 'Burnout', ['Dire', 'Incendiary'])
    Level2Combo('Deep Ocean', ['Dark', 'Water'], 'Venom Water', ['Nocturnal', 'Torrential'])
    Level2Combo('Obsidian Rift', ['Dark', 'Earth'], 'Black Abyss', ['Obsidian', 'Craggy'])
    Level2Combo('Nocturnal Surge', ['Dark', 'Electric'], 'Ray of Light', ['Quantum', 'Electrified'])
    Level2Combo('Black Ice', ['Dark', 'Ice'], 'Venom Water', ['Chilling', 'Sinister'])
    Level2Combo('Midnight Gale', ['Dark', 'Wind'], 'Black Abyss', ['Howling', 'Nocturnal'])
    Level2Combo('Black Abyss', ['Dark', 'Dark'], 'Black Abyss', ['Abyssal', 'Pitchblack'])
    Level2Combo('Ray of Light', ['Dark', 'Light'], 'Ray of Light', ['Radiant', 'Contrasting'])
    Level2Combo('Solar Wrath', ['Light', 'Fire'], 'Flame Bolt', ['Incandescent', 'Furious'])
    Level2Combo('Atlantis', ['Light', 'Water'], 'Cold Snap', ['Iridescent', 'Neptunian'])
    Level2Combo('Shooting Star', ['Light', 'Earth'], 'Ray of Light', ['Terrestrial', 'Gaian'])
    Level2Combo('Lightning Bolt', ['Light', 'Electric'], 'Lightning Bolt', ['Electrifying', 'Swift'])
    Level2Combo('Glacial Gleam', ['Light', 'Ice'], 'Ice Wind', ['Lustrous', 'Crystalline'])
    Level2Combo('Solar Wind', ['Light', 'Wind'], 'Cyclone', ['Radiant', 'Aerial'])
    Level2Combo('Luminous Dusk', ['Light', 'Dark'], 'Pandemic', ['Ethereal', 'Interstellar'])
    Level2Combo('Gamma Ray', ['Light', 'Light'], 'Gamma Ray', ['Brilliant', 'Spectral'])

    # Since there are 512 possible combinations, I'm not creating names for all of them
    # Instead, the first 2 stages determine an adjective. The element types determine possible nouns. Combine the 2 to form a new combo name
    Level3ComboTemplate('Fire', ['Inferno', 'Blaze', 'Explosion', 'Combustion', 'Conflagration'],['Volcanic Storm', 'Mega Explosion', 'Mega Explosion', 'Nuclear Blast', 'Mega Eruption'])
    Level3ComboTemplate('Water', ['Tsunami', 'Torrent', 'Maelstrom', 'Riptide', 'Undertow'],['Steam Explosion', 'Electrolysis', 'Electrolysis', 'Steam Explosion', 'Splash Hazard'])
    Level3ComboTemplate('Earth', ['Landslide', 'Fissure', 'Fracture', 'Ragnarök', 'Earthquake '],['Splash Hazard', 'Mega Eruption', 'Nuclear Blast', 'Meteorite', 'Lightning Quake'])
    Level3ComboTemplate('Electric', ['Electrocution', 'Voltage', 'Surge', 'Lightning', 'Fulmination'],['Lightning Quake', 'Heaven\'s Bolt', 'Ruinous Weather', 'Heaven\'s Bolt', 'Ultimate Aurora'])
    Level3ComboTemplate('Ice', ['Avalanche', 'Blizzard', 'Fimbulvetr', 'Glacier', 'Cryofreeze'],['Frost Typhoon', 'Diamond Mist', 'Dead of Winter', 'Permafrost Crash', 'Gravity Blizzard'])
    Level3ComboTemplate('Wind', ['Whirlwind', 'Hurricane', 'Twister', 'Zephyr', 'Tornado'],['Final Disaster', 'Thunder Gale', 'Electrofire Storm', 'Dead of Winter', 'Sandstorm'])
    Level3ComboTemplate('Dark', ['Eclipse', 'Nightfall', 'Void', 'Poltergeist', 'Nosferatu'],['Hyper Graviton', 'Dark Tide', 'Dark Tide', 'Hyper Graviton', 'Gravity Blizzard'])
    Level3ComboTemplate('Light', ['Corona', 'Beacon', 'Nova', 'Flash', 'Quazar'],['Second Sun', 'Supernova', 'Second Sun', 'Ultimate Aurora', 'Supernova'])


def getCustomLevel2Combo(elemRoute):
    for combo in CustomLevel2s:
        if combo.elemRoute == elemRoute:
            return combo
    return None


def BladeComboRandomization():
    PopulateMaps()

    if Options.BladeCombosOption_ElementRoutes.GetState():
        CreateCustomCombos()
        RandomizeElementRoutes()
    if Options.BladeCombosOption_AOE.GetState():
        RandomizeAOE()
    if Options.BladeCombosOption_DOT.GetState():
        RandomizeDOT()
    if Options.BladeCombosOption_Animations.GetState():
        RandomizeAnimations()

    JSONParser.PrintTable("common/BTL_ElementalCombo.json")
    JSONParser.PrintTable("common_ms/BTL_ElementalCombo_ms.json")


def PopulateMaps():
    def getNames(combo):
        OriginalID2Name[combo['$id']] = combo['name']
    JSONParser.ChangeJSONLineWithCallback(["common_ms/BTL_ElementalCombo_ms.json"], [], getNames, replaceAll=True)

    def getCombos(combo):
        name = OriginalID2Name[combo['$id']]
        OriginalCombos[combo['ComboStage']][name] = combo
    JSONParser.ChangeJSONLineWithCallback(["common/BTL_ElementalCombo.json"], [], getCombos, replaceAll=True)

    def getElems(elem):
        # Note: -1 because the blade combo elements are offset by 1 for some reason (presumably as there is no "None")
        Name2Elem[elem['name']] = elem['$id']-1
    JSONParser.ChangeJSONLineWithCallback(["common_ms/menu_attr_ms.json"], Helper.InclRange(2,9), getElems)

def RandomizeElementRoutes():
    print('RandomizeElementRoutes()')

    # Note: Debug names are set for 2 reasons:
    # 1. So I can understand the randomization as it's happening
    # 2. So we can iterate over ReplacedCombos once done to apply all the names at once

    RemainingTier1s = list(OriginalCombos[1].values())
    RemainingTier2Elements = [i for i in Helper.InclRange(1,8) for _ in range(3)] # 3 chances to appear
    RemainingTier3Elements = [i for i in Helper.InclRange(1, 8) for _ in range(4)]  # 4 chances to appear
    random.shuffle(RemainingTier1s)
    random.shuffle(RemainingTier2Elements)
    random.shuffle(RemainingTier3Elements)

    def randomize(combo):
        # Skip Torna combos such as Heat II, Stone II, etc. (they should still work after randomization)
        if combo['ComboStage'] != 1 and combo['PreCombo'] == 0:
            return

        # For tier 1s, we just shuffle the list of tier 1s and reassign them
        if combo['ComboStage'] == 1:
            combo['DebugName'] = OriginalID2Name[RemainingTier1s[0]['$id']]
            for key, value in combo.items():
                if key not in ['$id', 'DebugName', 'Name']:  # Note: Name is excluded because we handle that ourselves down below
                    combo[key] = RemainingTier1s[0][key]
            del RemainingTier1s[0]

        # For tier 2s, we start by randomizing an element. Once we have the element,
        # we determine the custom combo based on the first and second stages.
        elif combo['ComboStage'] == 2:
            # Determine the next combo based on randomized tier 2 elements
            stage1Element = ReplacedCombos[combo['PreCombo']]['Atr']
            stage2Element = RemainingTier2Elements[0]
            comboRoute = [stage1Element, stage2Element]
            newCombo = getCustomLevel2Combo(comboRoute)

            # If this combo has happened previously, shuffle the elements again
            while any(previousCombo == comboRoute for previousCombo in ReplacedComboRoutes):
                random.shuffle(RemainingTier2Elements)
                stage2Element = RemainingTier2Elements[0]
                comboRoute = [stage1Element, stage2Element]
                newCombo = getCustomLevel2Combo(comboRoute)

            # Replace the combo
            combo['DebugName'] = newCombo.name
            combo['Atr'] = stage2Element
            for key, value in combo.items():
                if key not in ['$id', 'DebugName', 'Atr', 'PreCombo', 'Name']: # Note: Name is excluded because we handle that ourselves down below
                    combo[key] = newCombo.base[key]

            del RemainingTier2Elements[0]
            ReplacedComboRoutes.append(comboRoute)

        # For tier 3s, we start by randomizing an element. Once we have the element,
        # we determine the final combo based on the 5 combos possible for that element.
        # This final combo corresponds to the noun in the combo name. The prior 2 stages
        # of the combo determine the adjective which comes before this noun.
        elif combo['ComboStage'] == 3:
            # Determine the next combo based on randomized tier 2 elements
            stage2Combo = ReplacedCombos[combo['PreCombo']]
            stage1Combo = ReplacedCombos[stage2Combo['PreCombo']]
            stage1Element = stage1Combo['Atr']
            stage2Element = stage2Combo['Atr']
            stage2Combo = getCustomLevel2Combo([stage1Element, stage2Element])
            stage3Element = RemainingTier3Elements[0]
            comboRoute = [stage1Element, stage2Element, stage3Element]

            # If this combo has happened previously, shuffle the elements again
            while any(previousCombo == comboRoute for previousCombo in ReplacedComboRoutes):
                random.shuffle(RemainingTier3Elements)
                stage3Element = RemainingTier3Elements[0]
                comboRoute = [stage1Element, stage2Element, stage3Element]

            # Create the new combo
            stage3ComboTemplate = CustomLevel3Templates[stage3Element]
            newComboName = stage2Combo.tier3adjectives[0] + " " + stage3ComboTemplate.nameNouns[0]
            newComboBase = stage3ComboTemplate.bases[0]

            # Replace the combo
            combo['DebugName'] = newComboName
            combo['Atr'] = stage3Element
            for key, value in combo.items():
                if key not in ['$id', 'DebugName', 'Atr', 'PreCombo', 'Name']:  # Note: Name is excluded because we handle that ourselves down below
                    combo[key] = newComboBase[key]

            del RemainingTier3Elements[0]
            del stage2Combo.tier3adjectives[0]
            del stage3ComboTemplate.nameNouns[0]
            del stage3ComboTemplate.bases[0]
            ReplacedComboRoutes.append(comboRoute)

        ReplacedCombos[combo['$id']] = combo

    def updateNames(combo):
        if combo['$id'] in ReplacedCombos:
            combo['name'] = ReplacedCombos[combo['$id']]['DebugName']

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_ElementalCombo.json"], [], randomize, replaceAll=True)
    JSONParser.ChangeJSONLineWithCallback(["common_ms/BTL_ElementalCombo_ms.json"], [], updateNames, replaceAll=True)


def RandomizeAOE():
    print('TODO: RandomizeAOE()')


def RandomizeDOT():
    print('TODO: RandomizeDOT')


def RandomizeAnimations():
    print('TODO: RandomizeAnimations()')

