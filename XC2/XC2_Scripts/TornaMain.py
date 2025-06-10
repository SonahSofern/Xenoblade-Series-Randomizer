from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests, TornaEnemies, TornaAreas, TornaShops, TornaRedBagItems, TornaMiscItems, TornaChests, TornaCollectionPoints, Options
import copy
import os
import math
from scripts.Interactables import OptionList
import _WeaponChips

# TO DO
# look into options for pre-completed quests or EZ-complete quests?
# required items for a given quest would need to be zeroed out for said quest, besides the pre-req items.

# option to remove specific quests or locations from list

# there's probably a few enemies that are hard to get to aggro.

# need to turn pre-req quests golden/red
# need to turn npcs that give quests golden/red

# need to add the quests that are required for their rewards to the spoiler log as well
# re-evaluate whether or not quest enemies can have progression, I disabled them for now

class ItemInfo:
    def __init__(self, inputid, category, addtolist):
        self.id = inputid
        self.type = category
        addtolist.append(self)

class LocationCategory:
    def __init__(self, cat, progbool, fulllocs):
        self.category = cat # what is the category's name
        self.isprogresscategory = progbool # can the category have progression
        self.fullloclist = fulllocs # what is the full list of locations that belong in this category
        self.remlocations = fulllocs.copy() # what is the remaining list of locations that haven't been used yet

class KeyItemParams:
    def __init__(self, name, caption, nameid, captionid, preciousid, addtolist):
        self.name = name
        self.nameid = nameid
        self.caption = caption
        self.captionid = captionid
        self.preciousid = preciousid
        addtolist.append(self)

class BladeInfo:
    def __init__(self, name, FSkillID, unlockkeyids):
        self.name = name
        self.fskillid = FSkillID
        self.unlockkeyids = unlockkeyids

LocTypetoSpoilerLogHeader = {
    "sidequest": "Side Quests",
    "uniquemonster": "Unique Monsters",
    "boss": "Bosses",
    "normalenemy": "Normal Enemies",
    "redbag": "Ground Item Spots",
    "misc": "Miscellaneous",
    "chest": "Chests",
    "shop": "Shops",
    "tornacollectionpoint": "Collection Points (Torna)",
    "gormottcollectionpoint": "Collection Points (Gormott)",
    "questenemy": "Quest Enemies"
}

ItemIDtoItemName = {30340: "Cotton Branch",25302: "???",105: "0-Battle Course",106: "0-Battle Course+",26006: "3003用情報(内容未定)",25144: "50 Volt Battery",25163: "500年前の記録書",25498: "A Boy of Two Swords",25499: "A Firecracker of a Gal",26062: "A Gormotti Recipe",25421: "A Hat Fit for a Lady",25423: "A Mercenary's Honor",25420: "A Smith's Pastime",26061: "A Tantalese Recipe",25195: "Absorp Quartz",489: "Abyss Masque 1",490: "Abyss Masque 2",491: "Abyss Masque 3",1: "Abyss Vest",25451: "Access Code 1",26137: "Access Code 1",25452: "Access Code 2",26138: "Access Code 2",25450: "Accessory Expander Kit",26076: "Acquiring Skills",141: "Activity Amulet",285: "Activity Amulet",429: "Activity Amulet",25282: "Adelno Deeds",25313: "Adventures Contract",17031: "Aerial Hunter I",17032: "Aerial Hunter II",17033: "Aerial Hunter III",17034: "Aerial Hunter IV",17035: "Aerial Hunter V",17358: "Aerial Hunter VI",612: "Aero Greatsword 1",613: "Aero Greatsword 2",614: "Aero Greatsword 3",244: "Affection Necklace",388: "Affection Necklace",92: "Affection Necklace",241: "Affection Ring",385: "Affection Ring",89: "Affection Ring",26072: "Affinity Benefits",17340: "Affinity MAX Acc I",17341: "Affinity MAX Acc II",17342: "Affinity MAX Acc III",17343: "Affinity MAX Acc IV",17344: "Affinity MAX Acc V",17405: "Affinity MAX Acc VI",17294: "Affinity MAX Atk I",17295: "Affinity MAX Atk II",17296: "Affinity MAX Atk III",17297: "Affinity MAX Atk IV",17298: "Affinity MAX Atk V",17399: "Affinity MAX Atk VI",17289: "Affinity MAX Barrier I",17290: "Affinity MAX Barrier II",17291: "Affinity MAX Barrier III",17292: "Affinity MAX Barrier IV",17293: "Affinity MAX Barrier V",17398: "Affinity MAX Barrier VI",17299: "Affinity MAX Evade I",17300: "Affinity MAX Evade II",17301: "Affinity MAX Evade III",17302: "Affinity MAX Evade IV",17303: "Affinity MAX Evade V",17400: "Affinity MAX Evade VI",25198: "Agate",17077: "Aggro Attack Up I",17078: "Aggro Attack Up II",17079: "Aggro Attack Up III",17080: "Aggro Attack Up IV",17081: "Aggro Attack Up V",17365: "Aggro Attack Up VI",17224: "Aggro Boost I",17225: "Aggro Boost II",17226: "Aggro Boost III",17227: "Aggro Boost IV",17228: "Aggro Boost V",17388: "Aggro Boost VI",26028: "Akatsuki's Hideout",25092: "Alban's Painting",25271: "Aldomar Deeds",516: "Alexandrite 1",517: "Alexandrite 2",518: "Alexandrite 3",30427: "Alloy Sheeting",226: "Alpha Scope",370: "Alpha Scope",74: "Alpha Scope",107: "Alphabet Course",108: "Alphabet Course+",25472: "Alrest Linkring",30366: "Amber Sweetfish",17067: "Ambush Boost I",17068: "Ambush Boost II",17069: "Ambush Boost III",17070: "Ambush Boost IV",17071: "Ambush Boost V",17364: "Ambush Boost VI",26103: "Ambushing Enemies",10019: "Amethyst Chip",26060: "An Ardainian Recipe",25234: "Anangham Gate Key",201: "Ancient Banner",345: "Ancient Banner",49: "Ancient Banner",25053: "Ancient Nopon Key",30348: "Angel's Sage",10048: "Angrite Chip",26193: "Anise's Location",17209: "Annul Resist I",17210: "Annul Resist II",17211: "Annul Resist III",17212: "Annul Resist IV",17213: "Annul Resist V",25112: "Antidesiccant",146: "Appealing Lamp",290: "Appealing Lamp",434: "Appealing Lamp",30426: "Apple Lamp",205: "Apprentice Vambraces",349: "Apprentice Vambraces",53: "Apprentice Vambraces",609: "Aqua Greatsword 1",610: "Aqua Greatsword 2",611: "Aqua Greatsword 3",10022: "Aquamarine Chip",25273: "Aquaneze Deeds",17036: "Aquatic Hunter I",17037: "Aquatic Hunter II",17038: "Aquatic Hunter III",17039: "Aquatic Hunter IV",17040: "Aquatic Hunter V",17359: "Aquatic Hunter VI",25434: "Arbitrary Fish",642: "Arctic Sword 1",643: "Arctic Sword 2",644: "Arctic Sword 3",26175: "Armored Rucksack",123: "Arms Attachment",268: "Arms Attachment",412: "Arms Attachment",25461: "Armu Carcass",25362: "Armu Meat Contract",25382: "Armu Milk Contract",25219: "Artificial Blade Report",25427: "Artisanal Accessories",17234: "Arts Aggro Boost I",17235: "Arts Aggro Boost II",17236: "Arts Aggro Boost III",17237: "Arts Aggro Boost IV",17238: "Arts Aggro Boost V",17390: "Arts Aggro Boost VI",17239: "Arts Heal I",17240: "Arts Heal II",17241: "Arts Heal III",17242: "Arts Heal IV",17243: "Arts Heal V",17391: "Arts Heal VI",17229: "Arts Stealth I",17230: "Arts Stealth II",17231: "Arts Stealth III",17232: "Arts Stealth IV",17233: "Arts Stealth V",17389: "Arts Stealth VI",30431: "Aspar Snakemeat",15: "Assassin Shoes",167: "Assassin Shoes",311: "Assassin Shoes",221: "Assault Stone",365: "Assault Stone",69: "Assault Stone",25396: "Astrology Contract",26159: "Astronomer's Pot",220: "Attack Stone",364: "Attack Stone",68: "Attack Stone",10047: "Aubrite Chip",465: "Augmented Vision Kit 1",466: "Augmented Vision Kit 2",467: "Augmented Vision Kit 3",17219: "Auto-Attack Stealth I",17220: "Auto-Attack Stealth II",17221: "Auto-Attack Stealth III",17222: "Auto-Attack Stealth IV",17223: "Auto-Attack Stealth V",17387: "Auto-Attack Stealth VI",118: "Auto-Balancer",189: "Avant-Garde Medal",333: "Avant-Garde Medal",37: "Avant-Garde Medal",443: "Avian Totem Carving",128: "Axe Attachment",273: "Axe Attachment",417: "Axe Attachment",10050: "Axion Chip",26127: "Back Attack",25391: "Bagna Contract",25437: "Baked Redfish",133: "Ball Attachment",278: "Ball Attachment",422: "Ball Attachment",25330: "Bana Etching Contract",26016: "Band of Assassins",30408: "Barbed Tomato",26015: "Barrels' Destination",25232: "Basement Key",26100: "Basics of Tiger! Tiger! 1",26101: "Basics of Tiger! Tiger! 2",26102: "Basics of Tiger! Tiger! 3",25279: "Bassani Deeds",30425: "Bat Hinge",10029: "Battery Chip",17421: "Beach Date Pandoria",228: "Beast Hood",372: "Beast Hood",76: "Beast Hood",17021: "Beast Hunter I",17022: "Beast Hunter II",17023: "Beast Hunter III",17024: "Beast Hunter IV",17025: "Beast Hunter V",17356: "Beast Hunter VI",501: "Beast-Hide Vest 1",502: "Beast-Hide Vest 2",503: "Beast-Hide Vest 3",25320: "Beat Paste Contract",573: "Beatific Medal 1",574: "Beatific Medal 2",575: "Beatific Medal 3",25433: "Beautiful Bowl",25355: "Beautiful Contract",471: "Belemnite Bangle 1",472: "Belemnite Bangle 2",473: "Belemnite Bangle 3",26158: "Bell of Idyll",25417: "Beneath the Aurora",26107: "Benefits of Smashing",25032: "Benoît Nut",30358: "Berryhopper",218: "Berserk Ring",362: "Berserk Ring",66: "Berserk Ring",683: "Best Girl Fan Tora",144: "Beta Scope",288: "Beta Scope",432: "Beta Scope",25398: "Billiard Contract",30393: "Binding Roots",251: "Bio Gauntlet",395: "Bio Gauntlet",99: "Bio Gauntlet",25325: "Bipedal Crab Contract",30372: "Bismuth Slab",25431: "Bizarre Soup",215: "Black Belt",359: "Black Belt",63: "Black Belt",522: "Black Cube 1",523: "Black Cube 2",524: "Black Cube 3",25020: "Black Steel Circler",26066: "Blade Affinity",26068: "Blade Combat",17056: "Blade Combo Boost I",17057: "Blade Combo Boost II",17058: "Blade Combo Boost III",17059: "Blade Combo Boost IV",17060: "Blade Combo Boost V",17061: "Blade Combo Boost VI",26117: "Blade Switch",26105: "Blade's Personality",30350: "Bladed Holly",26116: "Blades and Ideas",585: "Blazing Braid 1",586: "Blazing Braid 2",587: "Blazing Braid 3",26161: "Blinding-Fast Wing",600: "Blizzard Braid 1",601: "Blizzard Braid 2",602: "Blizzard Braid 3",25395: "Blizzard Contract",17016: "Block Rate Up I",17017: "Block Rate Up II",17018: "Block Rate Up III",17019: "Block Rate Up IV",17020: "Block Rate Up V",17355: "Block Rate Up VI",655: "Blood Witch Nia",210: "Bloody Orb",354: "Bloody Orb",58: "Bloody Orb",25201: "Bloomshroom",17199: "Blowdown Resist I",17200: "Blowdown Resist II",17201: "Blowdown Resist III",17202: "Blowdown Resist IV",17203: "Blowdown Resist V",17385: "Blowdown Resist VI",17413: "Blue Sky Pyra",25342: "Bluegill Contract",25294: "Boldarde Deeds",160: "Bolt Hat",304: "Bolt Hat",8: "Bolt Hat",26188: "Bonytongue Casserole",30419: "Bonytongue Shark",25105: "Book of Knowledge",10032: "Booster Chip",26075: "Boosting Arts",206: "Boxer Vambraces",350: "Boxer Vambraces",54: "Boxer Vambraces",10042: "Brachinite Chip",25266: "Brad Deeds",17179: "Break Resist I",17180: "Break Resist II",17181: "Break Resist III",17182: "Break Resist IV",17183: "Break Resist V",17381: "Break Resist VI",222: "Break Stone",366: "Break Stone",70: "Break Stone",26125: "Breaking Element Orbs",25093: "Brief History of Alrest",25306: "Bright Contract",26003: "Broken Crane 1",26004: "Broken Crane 2",26005: "Broken Crane 3",25012: "Broken Knife",30434: "Broken Tirkin Spear",10003: "Bronze Chip",25252: "Brothersisterpon Deeds",25317: "Bubbly Contract",25462: "Bug Catcher Turbotron",30382: "Buloofo Beastmeat",30386: "Bunnit Bunnymeat",182: "Bunnit Choker",30: "Bunnit Choker",326: "Bunnit Choker",26147: "Bunnit-Stuffed Peppers",25008: "Buoyweed",30418: "Burred Clam",113: "Burst Symbol",260: "Burst Symbol",404: "Burst Symbol",650: "Buster-Mode Tora",25441: "Buzzing Bouillabaisse",25082: "Calamity Puzzle",30443: "Camill Mane",229: "Camo Hood",373: "Camo Hood",77: "Camo Hood",649: "Candy Stripe Nia",130: "Cannon Attachment",275: "Cannon Attachment",419: "Cannon Attachment",25471: "Cap with Casual Trim",576: "Carbon Gauntlet 1",577: "Carbon Gauntlet 2",578: "Carbon Gauntlet 3",13: "Carbon Gloves",165: "Carbon Gloves",309: "Carbon Gloves",17414: "Carbon Mythra",26069: "Careful When Exploring",26195: "Carpathia's Location",25010: "Carved Stone Turtle",159: "Ceramic Belt",303: "Ceramic Belt",7: "Ceramic Belt",25363: "Ceviche Contract",26132: "Chain Attack Secrets",10026: "Chain Chip",175: "Champion Belt",23: "Champion Belt",319: "Champion Belt",25341: "Char-Grilling Contract",30378: "Charged Shaft",468: "Charm Bangle 1",469: "Charm Bangle 2",470: "Charm Bangle 3",225: "Charming Swimsuit",369: "Charming Swimsuit",73: "Charming Swimsuit",137: "Cheer Treat",281: "Cheer Treat",425: "Cheer Treat",25489: "Cherry Slate Piece",25484: "Chestnut Slate Piece",26149: "Chilsainian Kascha",26191: "Chilsainian Kascha DX",247: "Chivalric Medal",391: "Chivalric Medal",95: "Chivalric Medal",211: "Chrome Scarf",355: "Chrome Scarf",59: "Chrome Scarf",645: "Cimmerian Sword 1",646: "Cimmerian Sword 2",647: "Cimmerian Sword 3",25485: "Cinnabar Slate Piece",30390: "Clarity Moss",187: "Classic Medal",331: "Classic Medal",35: "Classic Medal",25416: "Cleared of All Charges",25256: "Cleo Deeds",25312: "Clicky-Clacks Contract",25372: "Cloud Love Contract",25162: "Cloud Sea Compass EX",25043: "Cloud Sea Halite",654: "Cloud Sea King Rex",681: "Cloud Sea Shark Rex",25348: "Cloudsnail Contract",25263: "Cmalaf Deeds",10006: "Cobalt Chip",26184: "Coeian-Style Fry-Up",10025: "Coil Chip",25063: "Colla Carrot",234: "Colorful Feather",378: "Colorful Feather",82: "Colorful Feather",26106: "Combo Request",171: "Comet Choker",19: "Comet Choker",315: "Comet Choker",26163: "Community Spirit",25332: "Conch Contract",30391: "Confusion Ivy",456: "Consul Greaves 1",457: "Consul Greaves 2",458: "Consul Greaves 3",531: "Consul Pauldrons 1",532: "Consul Pauldrons 2",533: "Consul Pauldrons 3",25236: "Control Room Key",25301: "Control Room Key",25354: "Coral Casino Contract",25315: "Coral Contract",25297: "Coral Leaf Deeds",25329: "Coralline Contract",25295: "Corcaja Deeds",26111: "Core Chips",26018: "Core Crystal Hunters",26065: "Corinne's Recipe",30341: "Corkscrew Creeper",25264: "Cosmetipolitan Deeds",30405: "Cranberry Bell",30407: "Creeping Starpepper",519: "Crimson Headband 1",520: "Crimson Headband 2",521: "Crimson Headband 3",17411: "Crimson Orchid Brighid",25481: "Crimson Slate Piece",25359: "Crispy Veg Contract",114: "Critical Symbol",261: "Critical Symbol",405: "Critical Symbol",17001: "Critical Up I",17002: "Critical Up II",17003: "Critical Up III",17004: "Critical Up IV",17005: "Critical Up V",17352: "Critical Up VI",25190: "Crystal Dome",110: "Crystal Earrings",257: "Crystal Earrings",401: "Crystal Earrings",26115: "Crystal Fortunes",197: "Crystal Greaves",341: "Crystal Greaves",45: "Crystal Greaves",10038: "Cube Chip",30343: "Curious Rotting Leaves",17249: "Damage Heal I",17250: "Damage Heal II",17251: "Damage Heal III",17252: "Damage Heal IV",17253: "Damage Heal V",17393: "Damage Heal VI",30442: "Dannagh Weta",17139: "Dark Absorb",17122: "Dark Def Up I",17123: "Dark Def Up II",17124: "Dark Def Up III",17125: "Dark Def Up IV",17126: "Dark Def Up V",17375: "Dark Def Up VI",10049: "Dark Matter Chip",208: "Dark Orb",352: "Dark Orb",56: "Dark Orb",17147: "Dark Reflect",25491: "Dark-Gray Slate Piece",25194: "Darkcyte",510: "Dauntless Boots 1",511: "Dauntless Boots 2",512: "Dauntless Boots 3",30397: "Dawn Hydrangea",25480: "Dawning Slate Piece",25145: "Dead Man's Message",30392: "Deer Wood",25031: "Delivery for Feyla",537: "Demon Orb 1",538: "Demon Orb 2",539: "Demon Orb 3",25535: "Desert Medicine",30352: "Deviled Onion",17424: "Devoted Marigold Nia",30361: "Dharma Cricket",186: "Diamond",330: "Diamond",34: "Diamond",25007: "Diamond Oak",25180: "Diamond Tablet Piece",30421: "Dicy Stone",10058: "Dilaton Chip",30422: "Dilemma Rock",17407: "Disguised Pyra",534: "Divine Vambraces 1",535: "Divine Vambraces 2",536: "Divine Vambraces 3",25477: "Dragon Incense",651: "Dress Uniform Mòrag",26083: "Driver Class",26079: "Driver Combat 1",26104: "Driver Combat 2",26082: "Driver Combos",25394: "Dumplings Contract",25197: "Dusky Pearl",17135: "Earth Absorb",17102: "Earth Def Up I",17103: "Earth Def Up II",17104: "Earth Def Up III",17105: "Earth Def Up IV",17106: "Earth Def Up V",17371: "Earth Def Up VI",17143: "Earth Reflect",126: "Edge Attachment",271: "Edge Attachment",415: "Edge Attachment",30437: "Eks Tail",25442: "Elaborate Carving",17137: "Electric Absorb",17112: "Electric Def Up I",17113: "Electric Def Up II",17114: "Electric Def Up III",17115: "Electric Def Up IV",17116: "Electric Def Up V",17372: "Electric Def Up VI",17145: "Electric Reflect",618: "Electro Greatsword 1",619: "Electro Greatsword 2",620: "Electro Greatsword 3",17350: "Element Orb Ender",17351: "Element Orb Prioritizer",26124: "Element Orbs",25285: "Elgeschel Deeds",25448: "Ellook Horn",30441: "Ellook Horn",652: "Embercake Zeke",17159: "Emergency Guard I",17160: "Emergency Guard II",17161: "Emergency Guard III",17162: "Emergency Guard IV",17163: "Emergency Guard V",17378: "Emergency Guard VI",17164: "Endurance I",17165: "Endurance II",17166: "Endurance III",17167: "Endurance IV",17168: "Endurance V",17379: "Endurance VI",26080: "Enemy Detection",26130: "Enemy Reinforcements",26144: "Energy Stir-Fry",10030: "Engine Chip",552: "Enlightened Loincloth 1",553: "Enlightened Loincloth 2",554: "Enlightened Loincloth 3",492: "Envoy's Footgear 1",493: "Envoy's Footgear 2",494: "Envoy's Footgear 3",209: "Eraser Orb",353: "Eraser Orb",57: "Eraser Orb",16: "Ester Shoes",168: "Ester Shoes",312: "Ester Shoes",25361: "Estral Contract",25536: "Eternity Loam",26183: "Eternity Perfume",25024: "Ether Bottle",25003: "Ether Cylinder",25006: "Ether Cylinder",17011: "Ether Defense Up I",17012: "Ether Defense Up II",17013: "Ether Defense Up III",17014: "Ether Defense Up IV",17015: "Ether Defense Up V",17354: "Ether Defense Up VI",25220: "Ether R&D Revolution",25227: "Ether Tank Key",17149: "Evasion Focus I",17150: "Evasion Focus II",17151: "Evasion Focus III",17152: "Evasion Focus IV",17153: "Evasion Focus V",17376: "Evasion Focus VI",30409: "Everyman Cicada",25435: "Exotic Chips",26181: "Exquisite Perfume",25495: "Extra Game Options",101: "Eyepatch",253: "Eyepatch",397: "Eyepatch",177: "Fabulous Hat",25: "Fabulous Hat",321: "Fabulous Hat",25453: "Fabulously Fierce Hat",25277: "Fallone Deeds",30376: "Fancy Seam",682: "Fancy Sundress Nia",10009: "Fang Chip",26152: "Farsighted Talisman",17314: "Fast Blade Switch I",17315: "Fast Blade Switch II",17316: "Fast Blade Switch III",17317: "Fast Blade Switch IV",17318: "Fast Blade Switch V",17319: "Fast Blade Switch VI",25104: "Favored Hammer",25369: "Felmeri Contract",30380: "Feris Beastmeat",10: "Fiber Hat",162: "Fiber Hat",306: "Fiber Hat",26151: "Fierce Talisman",477: "Fighter's Circlet 1",478: "Fighter's Circlet 2",479: "Fighter's Circlet 3",25025: "Filament Globe",17133: "Fire Absorb",17092: "Fire Def Up I",17093: "Fire Def Up II",17094: "Fire Def Up III",17095: "Fire Def Up IV",17096: "Fire Def Up V",17368: "Fire Def Up VI",26135: "Fire Dragons Recipe",17141: "Fire Reflect",25364: "Fish Contract",26190: "Fisherman's Feast",25250: "Fishy Fishy Deeds",25345: "Fizz Contract",30433: "Flier Stinger",30423: "Floral Soil",10014: "Flower Chip",25073: "Flowers of Ice",176: "Fluffy Hat",24: "Fluffy Hat",320: "Fluffy Hat",10020: "Fluorite Chip",25447: "Flutterheart Grass",25356: "Fonsett-Rouge Contract",10016: "Forest Chip",30420: "Forrestone",26148: "Fried Tartari à la Jin",240: "Friendship Ring",384: "Friendship Ring",88: "Friendship Ring",25309: "Fruity Rice Contract",25318: "Full Moon Contract",639: "Fulmen Sword 1",640: "Fulmen Sword 2",641: "Fulmen Sword 3",25111: "Fungicide",25449: "Fused Valve",17062: "Fusion Combo Up I",17063: "Fusion Combo Up II",17064: "Fusion Combo Up III",17065: "Fusion Combo Up IV",17066: "Fusion Combo Up V",17363: "Fusion Combo Up VI",26098: "Fusion Combos 1",26099: "Fusion Combos 2",25299: "Future Deeds",26143: "Galaxy Charm",195: "Galaxy Cube",339: "Galaxy Cube",43: "Galaxy Cube",591: "Gale Braid 1",592: "Gale Braid 2",593: "Gale Braid 3",227: "Gamma Scope",371: "Gamma Scope",75: "Gamma Scope",564: "Gargantuan Feather 1",565: "Gargantuan Feather 2",566: "Gargantuan Feather 3",184: "Garnet",32: "Garnet",328: "Garnet",10021: "Garnet Chip",250: "Gauntlet",394: "Gauntlet",98: "Gauntlet",26007: "Gavyth the Merc's Info",154: "Gear Vest",2: "Gear Vest",298: "Gear Vest",25365: "Gelée Tart Contract",615: "Geo Greatsword 1",616: "Geo Greatsword 2",617: "Geo Greatsword 3",30430: "Geometric Gear",26112: "Getting Core Chips",26192: "Gibson's Location",25474: "Gideon Goldamatron",621: "Glacio Greatsword 1",622: "Glacio Greatsword 2",623: "Glacio Greatsword 3",555: "Glamorous Swimsuit 1",556: "Glamorous Swimsuit 2",557: "Glamorous Swimsuit 3",25378: "Glarna Contract",10015: "Glass Chip",25455: "Glassmaker's Tome",25336: "Glitterspud Contract",603: "Gloom Braid 1",604: "Gloom Braid 2",605: "Gloom Braid 3",25042: "Gloomwood Root",30349: "Glossy Chamomile",25170: "Glowing Tablet",200: "Goddess Banner",344: "Goddess Banner",48: "Goddess Banner",170: "Goddess Choker",18: "Goddess Choker",314: "Goddess Choker",10008: "Gold Chip",183: "Gold Gear Choker",31: "Gold Gear Choker",327: "Gold Gear Choker",233: "Gold Nopon Mask",377: "Gold Nopon Mask",81: "Gold Nopon Mask",666: "Golden Greaves 1",667: "Golden Greaves 2",668: "Golden Greaves 3",678: "Golden Headband 1",679: "Golden Headband 2",680: "Golden Headband 3",26155: "Golden Land Talisman",26176: "Golden Mug",25473: "Golden Sand Cocoon",660: "Golden Sash 1",661: "Golden Sash 2",662: "Golden Sash 3",25475: "Golden Scorpion",25080: "Golden Sunstone",672: "Golden Vambraces 1",673: "Golden Vambraces 2",674: "Golden Vambraces 3",546: "Goliath Ring 1",547: "Goliath Ring 2",548: "Goliath Ring 3",25196: "Gong Crystal",25124: "Gormotti Firewood",25029: "Gormotti Walnut",25304: "Graduation Certificate",30381: "Grady Beastmeat",25173: "Grand Ancient Tome",237: "Grandarbor Ward",381: "Grandarbor Ward",85: "Grandarbor Ward",198: "Graphite Greaves",342: "Graphite Greaves",46: "Graphite Greaves",25465: "Gravitonic Clutch",25171: "Great Ancient Tome",26019: "Greedy Monster",25233: "Green Pollen Orb",25186: "Greenmarine",30411: "Gregarious Scorpion",30365: "Grimdark Crab",25278: "Griogair Deeds",25388: "Grumbird Contract",25259: "Gryff Deeds",10057: "Hadron Chip",131: "Hammer Attachment",276: "Hammer Attachment",420: "Hammer Attachment",25081: "Hammershead",25228: "Hangar Division Key",25280: "Hanoon Deeds",25439: "Haphazard Pie",26056: "Harghal's Location",243: "Harvest Necklace",387: "Harvest Necklace",91: "Harvest Necklace",25284: "Haskefell Deeds",142: "Healing Amulet",286: "Healing Amulet",430: "Healing Amulet",25028: "Healing Herb",25182: "Healing Teak",26171: "Heart Compass",25217: "Heart Cookies",26118: "Heart-to-Heart Hints",26119: "Heart-to-Hearts",25337: "Hearty Contract",17284: "Helping Hand I",17285: "Helping Hand II",17286: "Helping Hand III",17287: "Helping Hand IV",17288: "Helping Hand V",12: "Hero Gloves",164: "Hero Gloves",308: "Hero Gloves",203: "Hero Pauldrons",347: "Hero Pauldrons",51: "Hero Pauldrons",207: "Hero Vambraces",351: "Hero Vambraces",55: "Hero Vambraces",10036: "Hexagon Chip",103: "Hi-Tech Eyepatch",255: "Hi-Tech Eyepatch",399: "Hi-Tech Eyepatch",30375: "Hi-vis Wire",26108: "Hidden Landmarks",25055: "Hideout Key",25185: "Himahistone",25094: "History of Gormott",26142: "Hollow Charm",25494: "Hollyhock Slate Piece",245: "Holy Necklace",389: "Holy Necklace",93: "Holy Necklace",25251: "Honeycomb Deeds",10012: "Horn Chip",30364: "Horned Sculpin",30402: "Hot Orange",25366: "Hot Ruby Contract",25428: "Hot Spring Bonanza",25340: "Hotplate Contract",10046: "Howardite Chip",17169: "HP Attack Boost I",17170: "HP Attack Boost II",17171: "HP Attack Boost III",17172: "HP Attack Boost IV",17173: "HP Attack Boost V",17380: "HP Attack Boost VI",25476: "Hugo's Gold Detector",26178: "Hugo's Gold Detector",17041: "Humanoid Hunter I",17042: "Humanoid Hunter II",17043: "Humanoid Hunter III",17044: "Humanoid Hunter IV",17045: "Humanoid Hunter V",17360: "Humanoid Hunter VI",17304: "Hunter's Chemistry I",17305: "Hunter's Chemistry II",17306: "Hunter's Chemistry III",17307: "Hunter's Chemistry IV",17308: "Hunter's Chemistry V",30403: "Hustle Hyacinth",26187: "Hustle Marinade",25338: "Hyacinth Contract",26186: "Hyber Meatball Stew",25222: "Hypertech Made Easy",17138: "Ice Absorb",25389: "Ice Cabbage Contract",17117: "Ice Def Up I",17118: "Ice Def Up II",17119: "Ice Def Up III",17120: "Ice Def Up IV",17121: "Ice Def Up V",17373: "Ice Def Up VI",191: "Ice Headband",335: "Ice Headband",39: "Ice Headband",17146: "Ice Reflect",25368: "Icicle Contract",25268: "Ikthus Deeds",152: "Incense of Calm",296: "Incense of Calm",440: "Incense of Calm",153: "Incense of Insight",297: "Incense of Insight",441: "Incense of Insight",26074: "Increasing Affinity",25479: "Indigo Slate Piece",26031: "Indoline Murals",17082: "Indoor Attack Up I",17083: "Indoor Attack Up II",17084: "Indoor Attack Up III",17085: "Indoor Attack Up IV",17086: "Indoor Attack Up V",17366: "Indoor Attack Up VI",25412: "Industrial Sort of Tour",173: "Infantry Vest",21: "Infantry Vest",317: "Infantry Vest",627: "Inferno Sword 1",628: "Inferno Sword 2",629: "Inferno Sword 3",459: "Infinity Greaves 1",460: "Infinity Greaves 2",461: "Infinity Greaves 3",117: "Infinity Symbol",263: "Infinity Symbol",407: "Infinity Symbol",25488: "Inky Slate Piece",26109: "Inns",17026: "Insect Hunter I",17027: "Insect Hunter II",17028: "Insect Hunter III",17029: "Insect Hunter IV",17030: "Insect Hunter V",17357: "Insect Hunter VI",25406: "Intermediate Weaponry",30373: "Inverse Bearing",10005: "Iron Chip",190: "Iron Headband",334: "Iron Headband",38: "Iron Headband",25054: "Jac's Family Gifts",17416: "Jade Orchid Brighid",155: "Jade Vest",299: "Jade Vest",3: "Jade Vest",25208: "Jammie's Mud Balls",17345: "Jamming I",17346: "Jamming II",17347: "Jamming III",17348: "Jamming IV",26174: "Jamming Megaphone",17349: "Jamming V",17406: "Jamming VI",25344: "Jelly Contract",25018: "Jellyfish Balsam Bunch",204: "Jet Pauldrons",348: "Jet Pauldrons",52: "Jet Pauldrons",25088: "Jeweled Signet",132: "Katana Attachment",277: "Katana Attachment",421: "Katana Attachment",25149: "Keepsake Necklace",25158: "Key to Something",25023: "Key-Shaped Lever",25229: "Keycode",25123: "Kiara's Torigonda",25379: "Killifish Contract",25373: "Kingdom Contract",26017: "Kingdom Destroyer",25272: "Knick-Knacks Deeds",25470: "Knit Hat with Cute Trim",17204: "Knockback Resist I",17205: "Knockback Resist II",17206: "Knockback Resist III",17207: "Knockback Resist IV",17208: "Knockback Resist V",17386: "Knockback Resist VI",134: "Knuckle Attachment",279: "Knuckle Attachment",423: "Knuckle Attachment",26157: "Koto of Self-Interest",26020: "Kountess Search Brief",26092: "Kountess Search Brief",26093: "Kountess Search Brief",26094: "Kountess Search Brief",30444: "Krabble Carapace",30438: "Lactonut",25409: "Ladder Key",129: "Lance Attachment",274: "Lance Attachment",418: "Lance Attachment",17189: "Launch Resist I",17190: "Launch Resist II",17191: "Launch Resist III",17192: "Launch Resist IV",17193: "Launch Resist V",17383: "Launch Resist VI",149: "Lavender Potpourri",293: "Lavender Potpourri",437: "Lavender Potpourri",663: "Lazure Greaves 1",664: "Lazure Greaves 2",665: "Lazure Greaves 3",675: "Lazure Headband 1",676: "Lazure Headband 2",677: "Lazure Headband 3",657: "Lazure Sash 1",658: "Lazure Sash 2",659: "Lazure Sash 3",30412: "Lazure Swallowtail",669: "Lazure Vambraces 1",670: "Lazure Vambraces 2",671: "Lazure Vambraces 3",10001: "Lead Chip",25492: "Leaden Slate Piece",102: "Leader's Eyepatch",254: "Leader's Eyepatch",398: "Leader's Eyepatch",25334: "Leaf-Weave Contract",26077: "Learning New Ideas",178: "Leather Gloves",26: "Leather Gloves",322: "Leather Gloves",25287: "Lectica Deeds",25125: "Left Golden Bracer",26085: "Leftheria Collecting 1",26086: "Leftheria Collecting 2",26087: "Leftheria Collecting 3",25316: "Leftheria Contract",26097: "Leftherian Murals",25323: "Lentil Contract",25303: "Letter to Melvin",25224: "Level 1 Access Key",25225: "Level 2 Access Key",26136: "Lhagen's Hat Pattern",17140: "Light Absorb",17127: "Light Def Up I",17128: "Light Def Up II",17129: "Light Def Up III",17130: "Light Def Up IV",17131: "Light Def Up V",17374: "Light Def Up VI",17148: "Light Reflect",25192: "Lightning Pearl",26156: "Lightning-Speed Flag",25187: "Lightocyte",30345: "Lily of the Sunny Valley",26166: "Literally Killer Tart",25314: "Littlepon Contract",25258: "Llysiau Deeds",10041: "Lodranite Chip",25176: "Looks Stamp",25095: "Lost People's Tablet",25352: "Love and War Contract",139: "Love Thread",283: "Love Thread",427: "Love Thread",17422: "Loyal Bellflower Nia",30354: "Lucky Lettuce",25300: "Lutino Deeds",25411: "M.I.A. Nopon",17046: "Machine Hunter I",17047: "Machine Hunter II",17048: "Machine Hunter III",17049: "Machine Hunter IV",17050: "Machine Hunter V",17361: "Machine Hunter VI",17417: "Magical Pink Pandoria",10027: "Magnet Chip",25349: "Maiden Statue Contract",25422: "Making Love Source",224: "Male Loincloth",368: "Male Loincloth",72: "Male Loincloth",25270: "Maluria Deeds",570: "Marble Cameo 1",571: "Marble Cameo 2",572: "Marble Cameo 3",25308: "Marine Contract",30385: "Marrin Fishmeat",17425: "Massive Melee Mythra",135: "Master Attachment",280: "Master Attachment",424: "Master Attachment",582: "Master Scope 1",583: "Master Scope 2",584: "Master Scope 3",25351: "Masterpiece Contract",26078: "Max Affinity",26070: "Maximum Affinity",30404: "Meaty Carrot",26140: "Mechanical Charm",196: "Mechanized Greaves",340: "Mechanized Greaves",44: "Mechanized Greaves",30398: "Melosian Honey",30394: "Memento Bark",25290: "Memoria Deeds",136: "Memory Locket",26121: "Merc Mission Tip",26122: "Merc Rewards 1",26123: "Merc Rewards 2",25424: "Merclibay's Mightiest",17412: "Mermaid-Blue Pandoria",25068: "Metal Brooch",232: "Metal Nopon Mask",376: "Metal Nopon Mask",80: "Metal Nopon Mask",25413: "Midnight Feasting",248: "Military Medal",392: "Military Medal",96: "Military Medal",25346: "Milkshake Contract",30416: "Mint Fish",148: "Mint Potpourri",292: "Mint Potpourri",436: "Mint Potpourri",10051: "Mirror Matter Chip",188: "Modern Medal",332: "Modern Medal",36: "Modern Medal",25147: "Mokmo Onion",193: "Moon Cube",337: "Moon Cube",41: "Moon Cube",10053: "Moon Matter Chip",30401: "Moonbeam Banana",25384: "Moonbeam Contract",26030: "Mor Ardain Murals",30436: "Moramora Pearl",26009: "Morythan Tablet 1",26010: "Morythan Tablet 2",26011: "Morythan Tablet 3",25493: "Moss-Green Slate Piece",25419: "Most Awful News?!",30413: "Motley Cobra",10031: "Motor Chip",17244: "Movement Heal I",17245: "Movement Heal II",17246: "Movement Heal III",17247: "Movement Heal IV",17248: "Movement Heal V",17392: "Movement Heal VI",30362: "Munchygrub",30439: "Murakmor's Flashstone",174: "Muscle Belt",22: "Muscle Belt",318: "Muscle Belt",30388: "Muscle Branch",25370: "Music Box Contract",25401: "Musical Contract",25324: "Mustard Contract",25034: "Mysterious Part A",25035: "Mysterious Part B",25036: "Mysterious Part C",25037: "Mysterious Part D",25038: "Mysterious Part E",25084: "Mysterious Part F",25429: "Mystery Launch Codes",17408: "Mythra-Style Pyra",169: "Nacre Choker",17: "Nacre Choker",313: "Nacre Choker",10045: "Nakhlite Chip",100: "Nano-Metal Gauntlet",252: "Nano-Metal Gauntlet",396: "Nano-Metal Gauntlet",25310: "Narcipear Contract",25487: "Navy-Blue Slate Piece",30383: "Nest Extract",25265: "Neuromin Deeds",25496: "New Difficulty Levels",25207: "Niall's Underwear",17254: "Night Vision I",17255: "Night Vision II",17256: "Night Vision III",17257: "Night Vision IV",17258: "Night Vision V",17394: "Night Vision VI",462: "Night-vision Kit 1",463: "Night-vision Kit 2",464: "Night-vision Kit 3",25009: "Nils's Medicine",25218: "Nimble Nopon Get Girls",579: "Noise Dampener 1",580: "Noise Dampener 2",581: "Noise Dampener 3",25397: "Nopon Contract",442: "Nopon Doll",25027: "Nopon Doubloon",231: "Nopon Mask",375: "Nopon Mask",79: "Nopon Mask",25415: "Nopon of Good Tastes",25443: "Nopon Summons",25497: "Nopon Summons, Pt. 2",25403: "Nopon Thank-You Note",25140: "Nopon Trade Guild ID",25385: "Noponcho Contract",25399: "Noponic Contract",25353: "Nopopomouli Contract",25030: "Nopopon's Journal",25255: "Nopox Deeds",25468: "Not-safe-for-work Folio",25011: "Note Fragment",25119: "Note on Lance",25121: "Note on Lance 2",25122: "Note on Lance 3",26008: "Noted Ardainian Doctor",26110: "Number of Arts",684: "Obligatory Leave Mòrag",17415: "Obsidian Dromarch",480: "Ocean Earring 1",481: "Ocean Earring 2",482: "Ocean Earring 3",30371: "Ocean Eye",25393: "Odifa Punch Contract",25237: "Old Town Gate Key",111: "Omega Drive",258: "Omega Drive",402: "Omega Drive",10023: "Opal Chip",17274: "Opening Art I",17275: "Opening Art II",17276: "Opening Art III",17277: "Opening Art IV",17278: "Opening Art V",17397: "Opening Art VI",25404: "Ophion's Data Terminal",192: "Optical Headband",336: "Optical Headband",40: "Optical Headband",25079: "Orbital Skyreader",17087: "Outdoor Attack Up I",17088: "Outdoor Attack Up II",17089: "Outdoor Attack Up III",17090: "Outdoor Attack Up IV",17091: "Outdoor Attack Up V",17367: "Outdoor Attack Up VI",147: "Overclocking Bangle",291: "Overclocking Bangle",435: "Overclocking Bangle",25408: "Overdrive Protocol",25457: "Panacellin",30395: "Panda Pansy",25326: "Passion Fruit Contract",25410: "Passion of the Artisan",140: "Passion Thread",284: "Passion Thread",428: "Passion Thread",25291: "Paulio Deeds",25490: "Peach Slate Piece",161: "Pearl Hat",305: "Pearl Hat",9: "Pearl Hat",10035: "Pentagon Chip",25002: "Perfect Range Sensor",25005: "Perfect Range Sensor",26173: "Perpetual Music Box",25463: "Pestronella",26182: "Pestronella Oil",236: "Phantom Feather",380: "Phantom Feather",84: "Phantom Feather",10055: "Photon Chip",17006: "Physical Defense Up I",17007: "Physical Defense Up II",17008: "Physical Defense Up III",17009: "Physical Defense Up IV",17010: "Physical Defense Up V",17353: "Physical Defense Up VI",25339: "Pickling Contract",25026: "Pile of Letters",25381: "Pipestraw Contract",25289: "Placks Deeds",30424: "Planetary Crystal",25286: "Platini Deeds",216: "Platinum Belt",360: "Platinum Belt",64: "Platinum Belt",25019: "Platinum Music Box",561: "Platinum Nopon Mask 1",562: "Platinum Nopon Mask 2",563: "Platinum Nopon Mask 3",30357: "Platinum Shroom",25374: "Plumber Contract",30368: "Polar Pearl",25089: "Pollen Orb",10039: "Polygon Chip",10056: "Positron Chip",25444: "Posystone",25305: "Pouch Expansion Kit",504: "Prairie Cap 1",505: "Prairie Cap 2",506: "Prairie Cap 3",25293: "Praximo Deeds",10059: "Preon Chip",25168: "Pretty Seashell",25390: "Prickly Contract",150: "Priestess's Auspices",294: "Priestess's Auspices",438: "Priestess's Auspices",25386: "Prismatic Contract",17418: "Pro Swimmer Pyra",25371: "Profiteering Contract",242: "Promise Ring",386: "Promise Ring",90: "Promise Ring",25022: "Promotional Leaflets",25230: "Proof of Akatsuki's Fall",648: "Prototype Suit Rex",25458: "Purestone",25321: "Puri Leaf Contract",25483: "Purple Slate Piece",30387: "Puzzletree Wood",17409: "Pyra-Style Mythra",606: "Pyro Greatsword 1",607: "Pyro Greatsword 2",608: "Pyro Greatsword 3",213: "Quantum Scarf",357: "Quantum Scarf",61: "Quantum Scarf",17419: "Radiant Beach Mythra",543: "Rainbow Belt 1",544: "Rainbow Belt 2",545: "Rainbow Belt 3",25466: "Rainbow Blossom",11: "Rainbow Gloves",163: "Rainbow Gloves",307: "Rainbow Gloves",30342: "Rainbow Resin",26084: "Raising Trust",17269: "Range Boost Up I",17270: "Range Boost Up II",17271: "Range Boost Up III",17272: "Range Boost Up IV",17273: "Range Boost Up V",30367: "Rarestone",143: "Rebirth Amulet",287: "Rebirth Amulet",431: "Rebirth Amulet",115: "Recovery Symbol",262: "Recovery Symbol",406: "Recovery Symbol",25017: "Red Collar",30445: "Red Pollen Orbs",138: "Red Thread",282: "Red Thread",426: "Red Thread",25254: "Reedirait Deeds",17264: "Reflect Damage Up I",17265: "Reflect Damage Up II",17266: "Reflect Damage Up III",17267: "Reflect Damage Up IV",17268: "Reflect Damage Up V",17396: "Reflect Damage Up VI",17072: "Reflect Immunity",17073: "Reflect Immunity",17074: "Reflect Immunity",17075: "Reflect Immunity",17076: "Reflect Immunity",25097: "Regiderian Tablet",25464: "Reinforced Glass",26179: "Resurrection Perfume",116: "Resurrection Symbol",104: "Revival Pod",26073: "Reviving Teammates",30384: "Rhogul Birdmeat",10034: "Rhombus Chip",25126: "Right Golden Bracer",172: "Rigid Vest",20: "Rigid Vest",316: "Rigid Vest",121: "Ring Attachment",266: "Ring Attachment",410: "Ring Attachment",30429: "Ripple Lens",25221: "Robolab Club Quarterly",249: "Round Table Medal",393: "Round Table Medal",97: "Round Table Medal",30356: "Ruby Pineapple",25347: "Rumble Contract",25249: "Rumbletum Deeds",26057: "Rumors of a Battleship",26058: "Rumors of Execution",145: "Rush Hour",289: "Rush Hour",433: "Rush Hour",30400: "Ruska Flour",25319: "Ruska Noodle Contract",25153: "Rusted Old Watch",25482: "Rusty Slate Piece",26141: "Rynea's Charm",124: "Saber Attachment",269: "Saber Attachment",413: "Saber Attachment",25274: "Sadecott Deeds",25165: "Saffran's Key",151: "Sage's Auspices",295: "Sage's Auspices",439: "Sage's Auspices",567: "Saint's Necklace 1",568: "Saint's Necklace 2",569: "Saint's Necklace 3",25281: "Salter Deeds",25216: "Salvager Rank A Cert.",25215: "Salvager Rank B Cert.",25214: "Salvager Rank C Cert.",25213: "Salvager Rank D Cert.",25212: "Salvager Rank E Cert.",25146: "Salvager's Diary",26133: "Salvaging Wisdom 1",26134: "Salvaging Wisdom 2",25387: "Samod Contract",25358: "Sanar-Knit Contract",30360: "Sand Upa",185: "Sapphire",329: "Sapphire",33: "Sapphire",17410: "Savage Dromarch",25261: "Savvy Deeds",10011: "Scale Chip",30428: "Scarlet Coil",656: "Scarlet Inquisitor Mòrag",26177: "Scarlet Rocket",25486: "Scarlet Slate Piece",120: "Scimitar Attachment",265: "Scimitar Attachment",409: "Scimitar Attachment",127: "Scythe Attachment",272: "Scythe Attachment",416: "Scythe Attachment",25438: "Seafood Chowder",26081: "Sealing Effects",25380: "Searing Contract",25532: "Secret Bell Blueprint",25531: "Secret Flag Blueprint",25533: "Secret Pot Blueprint",25534: "Secret Wing Blueprint",25343: "Seed-Grill Contract",636: "Seismic Sword 1",637: "Seismic Sword 2",638: "Seismic Sword 3",25226: "Senior Officer's Key",25155: "Sensitive Documents",25021: "Serenade",25151: "Serenade?",26180: "Serenity Perfume",474: "Seven-League Circlet 1",475: "Seven-League Circlet 2",476: "Seven-League Circlet 3",483: "Seven-Seas Earring 1",484: "Seven-Seas Earring 2",485: "Seven-Seas Earring 3",17214: "Shackle Blade Resist I",17215: "Shackle Blade Resist II",17216: "Shackle Blade Resist III",17217: "Shackle Blade Resist IV",17218: "Shackle Blade Resist V",26129: "Shackling Blades",26128: "Shackling Drivers",10028: "Shaft Chip",25178: "Sharp Tablet Piece",246: "Shell Cameo",390: "Shell Cameo",94: "Shell Cameo",14: "Shell Shoes",166: "Shell Shoes",310: "Shell Shoes",30351: "Shepherd's Coronet",30396: "Shepherd's Purse",122: "Shield Attachment",267: "Shield Attachment",411: "Shield Attachment",25206: "Shimmering Feather",687: "Shining Justice Zeke",25156: "Shining Stalactite",10052: "Shining Star Chip",25467: "Shiny New Power",17309: "Shoulder to Shoulder I",17310: "Shoulder to Shoulder II",17311: "Shoulder to Shoulder III",17312: "Shoulder to Shoulder IV",17313: "Shoulder to Shoulder V",26026: "Shrine of Journeys 1",26027: "Shrine of Journeys 2",26024: "Shrine of Light 1",26025: "Shrine of Light 2",26022: "Shrine of Offering 1",26023: "Shrine of Offering 2",112: "Sigma Drive",259: "Sigma Drive",403: "Sigma Drive",25311: "Silent Contract",158: "Silver Belt",302: "Silver Belt",6: "Silver Belt",10004: "Silver Chip",109: "Silver Earrings",256: "Silver Earrings",400: "Silver Earrings",235: "Silver Feather",379: "Silver Feather",83: "Silver Feather",25109: "Silver Pendant",30370: "Silverwing Quartz",17423: "Sincere Primrose Nia",230: "Skeleton Hood",374: "Skeleton Hood",78: "Skeleton Hood",686: "Skullface Punk Tora",25350: "Skywards Contract",17194: "Smash Resist I",17195: "Smash Resist II",17196: "Smash Resist III",17197: "Smash Resist IV",17198: "Smash Resist V",17384: "Smash Resist VI",30369: "Smellactite",179: "Smithy Gloves",27: "Smithy Gloves",323: "Smithy Gloves",25235: "Smùide Plant Key",25013: "Snow-White Rhino",25376: "Snowbaby Contract",25335: "Snowflake Contract",25322: "Snowy Dudleya Contract",217: "Soldier Ring",361: "Soldier Ring",65: "Soldier Ring",25200: "Solemn Statue",25262: "Soniarus Deeds",25177: "Soul Stamp",30353: "Sour Avocado",25333: "Sparkly Snow Contract",25045: "Special Blade Medicine",17320: "Specials Lv 1 Plus I",17321: "Specials Lv 1 Plus II",17322: "Specials Lv 1 Plus III",17323: "Specials Lv 1 Plus IV",17324: "Specials Lv 1 Plus V",17401: "Specials Lv 1 Plus VI",17325: "Specials Lv 2 Plus I",17326: "Specials Lv 2 Plus II",17327: "Specials Lv 2 Plus III",17328: "Specials Lv 2 Plus IV",17329: "Specials Lv 2 Plus V",17402: "Specials Lv 2 Plus VI",17330: "Specials Lv 3 Plus I",17331: "Specials Lv 3 Plus II",17332: "Specials Lv 3 Plus III",17333: "Specials Lv 3 Plus IV",17334: "Specials Lv 3 Plus V",17403: "Specials Lv 3 Plus VI",17335: "Specials Lv 4 Plus I",17336: "Specials Lv 4 Plus II",17337: "Specials Lv 4 Plus III",17338: "Specials Lv 4 Plus IV",17339: "Specials Lv 4 Plus V",17404: "Specials Lv 4 Plus VI",25296: "Speck Deeds",30359: "Speckled Monarch",10037: "Sphere Chip",17174: "Spike Defense I",17175: "Spike Defense II",17176: "Spike Defense III",17177: "Spike Defense IV",17178: "Spike Defense V",202: "Spiked Pauldrons",346: "Spiked Pauldrons",50: "Spiked Pauldrons",10018: "Spinel Chip",10040: "Spiral Chip",30344: "Spiral Mistletoe",238: "Spirit Tree Ward",382: "Spirit Tree Ward",86: "Spirit Tree Ward",25172: "Splendid Ancient Tome",181: "Spring Shoes",29: "Spring Shoes",325: "Spring Shoes",25269: "Sprintsy Deeds",25179: "Square Tablet Piece",194: "Star Cube",338: "Star Cube",42: "Star Cube",30346: "Star Maple",525: "Staunch Boots 1",526: "Staunch Boots 2",527: "Staunch Boots 3",157: "Steam Belt",301: "Steam Belt",5: "Steam Belt",25400: "Steam Contract",25360: "Steamflake Contract",10007: "Steel Chip",25383: "Steel Pipe Contract",30414: "Steel Salmon",26189: "Steel Salmon Tempura",26126: "Stench",30410: "Sticky Stick Insect",25167: "Stolen Parcel",25074: "Storied Band",25189: "Stormstone",25377: "Stralu Contract",25060: "Strange Mineral",25061: "Strange Mineral",25076: "Strange Mineral",25096: "Strange Mineral",25098: "Strange Mineral",25099: "Strange Mineral",25100: "Strange Mineral",25118: "Strange Mineral",25142: "Strange Mineral",25143: "Strange Mineral",25174: "Strange Mineral",25183: "Strange Mineral",25184: "Strange Mineral",25202: "Strange Mineral",25253: "Strummer Deeds",25469: "Subjugation Report",30406: "Sumpkin",26185: "Sumpkin Griddle Cakes",30377: "Suncog",30399: "Sunflower Rogue",25425: "Sunken Boosters",10054: "Sunlight Chip",513: "Sunlight Choker 1",514: "Sunlight Choker 2",515: "Sunlight Choker 3",17259: "Sunlight Eye I",17260: "Sunlight Eye II",17261: "Sunlight Eye III",17262: "Sunlight Eye IV",17263: "Sunlight Eye V",17395: "Sunlight Eye VI",30374: "Sunset Bracket",25211: "Sunshine Pie Recipe",685: "Surfinator Zeke",495: "Survivor's Footgear 1",496: "Survivor's Footgear 2",497: "Survivor's Footgear 3",25459: "Sweet Nothings",26164: "Sweet Nothings",17154: "Swift Evasion I",17155: "Swift Evasion II",17156: "Swift Evasion III",17157: "Swift Evasion IV",17158: "Swift Evasion V",17377: "Swift Evasion VI",26002: "Switch Parts 1",26095: "Switch Parts 2",26096: "Switch Parts 3",119: "Sword Attachment",264: "Sword Attachment",408: "Sword Attachment",26139: "Sword Charm",199: "Swordfighting Banner",343: "Swordfighting Banner",47: "Swordfighting Banner",26153: "Swordstrike Talisman",10060: "Tachyon Chip",540: "Tachyon Scarf 1",541: "Tachyon Scarf 2",542: "Tachyon Scarf 3",25298: "Talmye Deeds",26088: "Tantal Collecting 1",26089: "Tantal Collecting 2",26090: "Tantal Collecting 3",26091: "Tantal Collecting 4",26032: "Tantalese Murals",25445: "Tantalese Records",25454: "Tarres's Notes",25307: "Tasty Contract",25288: "Tatraty Deeds",26131: "Taunt",30355: "Tawny Carrot",26160: "Telepathic Bell",17279: "Telepathy I",17280: "Telepathy II",17281: "Telepathy III",17282: "Telepathy IV",17283: "Telepathy V",630: "Tempest Sword 1",631: "Tempest Sword 2",632: "Tempest Sword 3",594: "Terra Braid 1",595: "Terra Braid 2",596: "Terra Braid 3",486: "Terror Masque 1",487: "Terror Masque 2",488: "Terror Masque 3",26067: "The Basics of Battle",25414: "The Lone Watchman",25199: "The Mystery Continent",26059: "The Name of a Tornan",25426: "The Trendy Patissier",25150: "Thick Notepad",597: "Thunder Braid 1",598: "Thunder Braid 2",599: "Thunder Braid 3",25120: "Thunder Crystal",25181: "Ticket to Mor Ardain",26162: "Tiger-Winged Helmet",25257: "Tilly Deeds",10002: "Tin Chip",30435: "Tirkin Arrowhead",25430: "Tirkin Crab",25440: "Tirkin Curry",25436: "Tirkin Sushi",17051: "Titan Hunter I",17052: "Titan Hunter II",17053: "Titan Hunter III",17054: "Titan Hunter IV",17055: "Titan Hunter V",17362: "Titan Hunter VI",156: "Titanium Vest",300: "Titanium Vest",4: "Titanium Vest",26194: "Tlaloc's Location",25127: "Tome of Morytha #1",25128: "Tome of Morytha #2",25129: "Tome of Morytha #3",25130: "Tome of Morytha #4",25260: "Tomi Deeds",26021: "Top Secret Papers",17184: "Topple Resist I",17185: "Topple Resist II",17186: "Topple Resist III",17187: "Topple Resist IV",17188: "Topple Resist V",17382: "Topple Resist VI",25402: "Torigoth Contract",26029: "Torigoth Murals",30363: "Tornan Trout",588: "Torrent Braid 1",589: "Torrent Braid 2",590: "Torrent Braid 3",25292: "Trappers Deeds",25113: "Tree Brace",30415: "Tree Crab",10033: "Tri-Chip",25240: "Trial Blood Cookies",25244: "Trial Flumbleflan",25248: "Trial Glitterspud Cake",25239: "Trial Hot Cookies",25242: "Trial Laughcaf Flan",25245: "Trial Lovemerry Cake",25238: "Trial Neon Cookies",25243: "Trial Romello Flan",25241: "Trial Snipe Flan",25246: "Trial Starlit Tart",25247: "Trial Starry Waffle",25432: "Trident Fish",25188: "Trollenite",25044: "True Dragon Incense",25478: "True Dragon Incense",10017: "Turquoise Chip",26064: "Twaina's Recipe",498: "Twin Trunks Vest 1",499: "Twin Trunks Vest 2",500: "Twin Trunks Vest 3",26114: "Types of Core Crystal",26120: "Types of Merc Mission",219: "Tyrant Ring",363: "Tyrant Ring",67: "Tyrant Ring",17132: "Ultimate Shield",25407: "Ultimate Weaponry",624: "Umbra Greatsword 1",625: "Umbra Greatsword 2",626: "Umbra Greatsword 3",26154: "Unbreakable Talisman",212: "Unicorn Scarf",356: "Unicorn Scarf",60: "Unicorn Scarf",26113: "Unique Monsters R.I.P.",25418: "Upgrades and Tinkering",10043: "Ureilite Chip",26071: "Utilizing the Elements",558: "Vanish Hood 1",559: "Vanish Hood 2",560: "Vanish Hood 3",25275: "Vargel Deeds",26063: "Vasq's Recipe",25460: "Vault Key",25375: "Veg Contract",25191: "Verdi Crystal",30432: "Vibrant Flamii Wing",25276: "Vibrattio Deeds",25327: "Victory Contract",30389: "Vinegar Leaf",549: "Violent Stone 1",550: "Violent Stone 2",551: "Violent Stone 3",507: "Vivid Mitts 1",508: "Vivid Mitts 2",509: "Vivid Mitts 3",25175: "Vocals Stamp",30379: "Volff Beastmeat",25446: "Volff Fang",30440: "Volff Fang",25267: "Volty Deeds",633: "Vortex Sword 1",634: "Vortex Sword 2",635: "Vortex Sword 3",528: "War God Banner 1",529: "War God Banner 2",530: "War God Banner 3",26033: "Washed-Up Titans",17134: "Water Absorb",17097: "Water Def Up I",17098: "Water Def Up II",17099: "Water Def Up III",17100: "Water Def Up IV",17101: "Water Def Up V",17369: "Water Def Up VI",17420: "Water Lily Brighid",17142: "Water Reflect",25405: "Weaponry for Noobs",30347: "Weeping Flour",25209: "Whelzaman Cookie",26001: "Where's Falala's Son?",125: "Whip Attachment",270: "Whip Attachment",414: "Whip Attachment",214: "White Belt",358: "White Belt",62: "White Belt",25392: "Whitebait Contract",26145: "Wildflower Salad",17136: "Wind Absorb",17107: "Wind Def Up I",17108: "Wind Def Up II",17109: "Wind Def Up III",17110: "Wind Def Up IV",17111: "Wind Def Up V",17370: "Wind Def Up VI",17144: "Wind Reflect",30417: "Windyfish",26172: "Wing Booster",10010: "Wing Chip",26150: "Wingberry Cake",10044: "Winonaite Chip",180: "Wolf Shoes",28: "Wolf Shoes",324: "Wolf Shoes",10013: "Wood Chip",25331: "Wood-Carving Contract",25328: "Woodboard Contract",25357: "Woodwing Contract",223: "World Tree Drop",367: "World Tree Drop",71: "World Tree Drop",239: "World Tree Ward",383: "World Tree Ward",87: "World Tree Ward",25041: "Wraithwood Root",26146: "XL Magma Sauté",25367: "Xylophone Contract",25283: "Yafush Deeds",25193: "Yawn Lazuli",10024: "Zircon Chip",25544: "Mineralogy Lv. 1 Unlock",25545: "Mineralogy Lv. 2 Unlock",25546: "Mineralogy Lv. 3 Unlock",25547: "Swordplay Lv. 1 Unlock",25548: "Swordplay Lv. 2 Unlock",25549: "Swordplay Lv. 3 Unlock",25550: "Fortitude Lv. 1 Unlock",25551: "Fortitude Lv. 2 Unlock",25552: "Fortitude Lv. 3 Unlock",25553: "Forestry Lv. 1 Unlock",25554: "Forestry Lv. 2 Unlock",25555: "Forestry Lv. 3 Unlock",25556: "Manipulate Ether Lv. 1 Unlock",25557: "Manipulate Ether Lv. 2 Unlock",25558: "Manipulate Ether Lv. 3 Unlock",25559: "Keen Eye Lv. 1 Unlock",25560: "Keen Eye Lv. 2 Unlock",25561: "Keen Eye Lv. 3 Unlock",25562: "Focus Lv. 1 Unlock",25563: "Focus Lv. 2 Unlock",25564: "Focus Lv. 3 Unlock",25565: "Power of Light Lv. 1 Unlock",25566: "Power of Light Lv. 2 Unlock",25567: "Power of Light Lv. 3 Unlock",25568: "Girls' Talk Unlock",25569: "Entomology Lv. 1 Unlock",25570: "Entomology Lv. 2 Unlock",25571: "Entomology Lv. 3 Unlock",25572: "Mining Lv. 1 Unlock",25573: "Mining Lv. 2 Unlock",25574: "Mining Lv. 3 Unlock",25575: "Botany Lv. 1 Unlock",25576: "Botany Lv. 2 Unlock",25577: "Botany Lv. 3 Unlock",25578: "Lockpicking Lv. 1 Unlock",25579: "Lockpicking Lv. 2 Unlock",25580: "Lockpicking Lv. 3 Unlock",25581: "Icthyology Lv. 1 Unlock",25582: "Icthyology Lv. 2 Unlock",25583: "Icthyology Lv. 3 Unlock",25584: "Command Water Lv. 1 Unlock",25585: "Command Water Lv. 2 Unlock",25586: "Command Water Lv. 3 Unlock",25587: "Superstrength Lv. 1 Unlock",25588: "Superstrength Lv. 2 Unlock",25589: "Superstrength Lv. 3 Unlock",25590: "Hidden Hunting Camp Unlock",25591: "Lakeshore Campsite Unlock",25592: "Coolley Lake Camp Unlock",25593: "Hoary Weald Camp Unlock",25594: "Porton Village Camp Unlock",25595: "Feltley Village Camp Unlock",25596: "Aletta Garrison Camp Unlock", 25597: "Olnard's Trail Campsite Unlock",25598: "Dannagh Desert Camp Unlock",25599: "Holy Gate Camp Unlock",25600: "Jin Affinity Lv. 2 Unlock",25601: "Jin Affinity Lv. 3 Unlock",25602: "Jin Affinity Lv. 4 Unlock",25603: "Jin Affinity Lv. 5 Unlock",25604: "Haze Affinity Lv. 2 Unlock",25605: "Haze Affinity Lv. 3 Unlock",25606: "Haze Affinity Lv. 4 Unlock",25607: "Haze Affinity Lv. 5 Unlock",25608: "Mythra Affinity Lv. 2 Unlock",25609: "Mythra Affinity Lv. 3 Unlock",25610: "Mythra Affinity Lv. 4 Unlock",25611: "Mythra Affinity Lv. 5 Unlock",25612: "Minoth Affinity Lv. 2 Unlock",25613: "Minoth Affinity Lv. 3 Unlock",25614: "Minoth Affinity Lv. 4 Unlock",25615: "Minoth Affinity Lv. 5 Unlock",25616: "Brighid Affinity Lv. 2 Unlock",25617: "Brighid Affinity Lv. 3 Unlock",25618: "Brighid Affinity Lv. 4 Unlock",25619: "Brighid Affinity Lv. 5 Unlock",25620: "Aegaeon Affinity Lv. 2 Unlock",25621: "Aegaeon Affinity Lv. 3 Unlock",25622: "Aegaeon Affinity Lv. 4 Unlock",25623: "Aegaeon Affinity Lv. 5 Unlock",25624: "Haze Unlock Key",25625: "Addam Unlock Key",25626: "Mythra Unlock Key",25627: "Minoth Unlock Key",25628: "Hugo Unlock Key",25629: "Brighid Unlock Key",25630: "Aegaeon Unlock Key",25631: "Level Up Token"}

GormottNametoLocID = {
    "Coolley Lake": 2416,
    "Coolley Lake Camp": 2428,
    "Depths of Ignorance": 2419,
    "Duelists' Bridge": 2410,
    "Grandarbor's Embrace": 2420,
    "Hidden Hunting Camp": 2403,
    "Hoary Weald": 2417,
    "Hoary Weald Camp": 2423,
    "Lakeshore Campsite": 2402,
    "Lascham Cove": 2401,
    "Lascham Peninsula": 2407,
    "Lyanne Meadow": 2413,
    "Nebley Wind Cave": 2421,
    "Nox Promontory": 2424,
    "Ordia Great Plains": 2408,
    "Outlook Knoll": 2412,
    "Saints' Practice Grounds": 2422,
    "Seigle Fell": 2418,
    "Serene Springside": 2409,
    "Singbreeze Bough": 2404,
    "Strategy Room": 2426,
    "Titan's Roar": 2406,
    "Torigoth Arch": 2405,
    "Torigoth Cemetery": 2415,
    "Torigoth Village": 2414,
    "Valafum Hill": 2425,
    "Wayside Respite": 2411
}

def PassAlongSpoilerLogInfo(fileEntryVar2, Version2, permalinkVar2, seedEntryVar2):
    global fileEntryVar, Version, permalinkVar, seedEntryVar
    fileEntryVar = fileEntryVar2
    Version = Version2
    permalinkVar = permalinkVar2
    seedEntryVar = seedEntryVar2
    if Options.TornaCreateSpoilerLog.GetState():
        CreateSpoilerLog()

def AllTornaRando():
    CheckforIncompatibleSettings()
    DetermineSettings()
    if ProgressionLocTypes[:6] == [0,0,0,0,0,0]:
        raise Exception("There are no progression locations enabled, cannot generate seed!")
    #Recipes = TornaRecipes.CreateTornaRecipeList()
    TornaQuests.SelectRandomPointGoal()
    ChosenSupporterAmounts = [1,16,32,48,64] # have a few sliders going forwards to let the player change this amount
    global ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, AreaIDtoNameDict, MaxDropTableID, Enemies, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList, FullItemList, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, AllSidequestProgressionItems
    ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, AllSidequestProgressionItems = TornaQuests.SelectCommunityQuests(ChosenSupporterAmounts, ProgressionLocTypes[0], ProgressionLocTypes[6], ProgressionLocTypes[7])
    Areas, AreaIDtoNameDict = TornaAreas.CreateAreaInfo(Sidequests, Mainquests)
    Enemies, MaxDropTableID = TornaEnemies.AdjustEnemyRequirements(Sidequests, Mainquests, Areas, ProgressionLocTypes[2])
    Shops = TornaShops.CreateShopInfo(Mainquests, Areas, ProgressionLocTypes[4])
    RedBags = TornaRedBagItems.CreateRedBagInfo(Mainquests, Areas, ProgressionLocTypes[5])
    MiscItems = TornaMiscItems.CreateMiscItems(Mainquests, Areas, ProgressionLocTypes[4]) # for now, is on if shops are on
    Chests = TornaChests.CreateChestInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[3])
    TornaCollectionPointList, GormottCollectionPointList = TornaCollectionPoints.CreateCollectionPointInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[1])
    FullItemList = CreateItemLists()
    NormalEnemies, QuestEnemies, Bosses, UniqueMonsters = SplitEnemyTypes(Enemies)
    DetermineRemovedGormottLocs()
    PlaceItems(FullItemList, ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList)
    AddMissingKeyItems()
    CreateLevelCaps()
    HugoComeBack()
    AdjustSlateValue()
    EternityLoamChange()
    SkillTreeSetup()
    CampfireUnlocks()
    CharacterUnlocks()
    GenerateHints()
    if Options.TornaObjectColorMatchesContents.GetState():
        GildedCheckNames()
        ChangeReqItemRarities()

def CheckforIncompatibleSettings():
    AllowableOptions = ['Blade Button Combos', 'Blade Defenses', 'Blade Elements', 'Community Level Story Requirements', 'Condense Gold Loot', 'Create Torna Spoiler Log', 'Enemy Movespeed', 'Enhancement Display', 'Everlasting Pouch Items', 'Field Item Size', 'Gilded Required Check Names', 'Increased Movespeed', 'Music', 'Mute Popups', 'NPC Size', 'Remove Certain Gormott Checks', 'Shortcuts', 'Torna In-Game Hints', 'Torna Randomization', 'Treasure Chest Visibility', 'Trust Lines']
    ConflictingOptions = []
    ConflictingOptionNames = []
    ConflictingSubOptions = []
    exceptionmsg = ""
    for opt in OptionList:
        if opt.GetState() and opt.name not in AllowableOptions:
            ConflictingOptions.append(opt)
            ConflictingOptionNames.append(opt.name)
    for opt in OptionList:
        if opt.name == 'Shortcuts':
            if opt.GetState():
                for sub in opt.subOptions:
                    if sub.GetState() and sub.name != 'Tutorials Skip':
                        ConflictingSubOptions.append(sub.name)
    if ConflictingOptions != []:
        exceptionmsg += f"Torna Randomization did not complete due to the following conflicting options:\n{ConflictingOptionNames}.\n\n"
    if ConflictingSubOptions != []:
        exceptionmsg += f"Torna Randomization did not complete due to the following conflicting suboptions:\nShortcuts: {ConflictingSubOptions}."
    if exceptionmsg != "":
        raise Exception(exceptionmsg)

def DetermineSettings():
    global ProgressionLocTypes
    SidequestRewardQty, CollectionPointQty, EnemyDropQty, TreasureChestQty, ShopQty, GroundItemQty, Gate1CommReq, Gate2CommReq = 0,0,0,0,0,0,2,4
    
    if Options.TornaMainOption_SideQuests.GetState(): # if Sidequest Rewards are randomized
        SidequestRewardQty = Options.TornaMainOption_SideQuests.GetSpinbox()
    
    if Options.TornaMainOption_CollectionPoints.GetState(): # if Collection Points are randomized
        CollectionPointQty = Options.TornaMainOption_CollectionPoints.GetSpinbox()
    
    if Options.TornaMainOption_EnemyDrops.GetState(): # if Enemy Drops are randomized
        EnemyDropQty = Options.TornaMainOption_EnemyDrops.GetSpinbox()
    
    if Options.TornaMainOption_TreasureChests.GetState(): # if Treasure Chests are randomized
        TreasureChestQty = Options.TornaMainOption_TreasureChests.GetSpinbox()
    
    if Options.TornaMainOption_Shops.GetState(): # if Shops are randomized
        ShopQty = Options.TornaMainOption_Shops.GetSpinbox()
    
    if Options.TornaMainOption_GroundItems.GetState(): # if Ground Items are randomized
        GroundItemQty = 1

    if Options.TornaChooseCommunityReqs_Gate1Req.GetState(): # if we are changing the first community gate requirement
        Gate1CommReq = Options.TornaChooseCommunityReqs_Gate1Req.GetSpinbox()
        AddNewFlagPointers(Gate1CommReq, 1)

    if Options.TornaChooseCommunityReqs_Gate2Req.GetState(): # if we are changing the second community gate requirement
        Gate2CommReq = Options.TornaChooseCommunityReqs_Gate2Req.GetSpinbox()
        AddNewFlagPointers(Gate2CommReq, 2)

    ProgressionLocTypes = [SidequestRewardQty, CollectionPointQty, EnemyDropQty, TreasureChestQty, ShopQty, GroundItemQty, Gate1CommReq, Gate2CommReq]

def DetermineRemovedGormottLocs():
    global RemovedGormottLocs
    RemovedGormottLocs = []
    if Options.TornaRemoveGormottChecks.GetState():
        for subopt in Options.TornaRemoveGormottChecks.subOptions:
            if subopt.GetState():
                RemovedGormottLocs.append(GormottNametoLocID[subopt.name])

def CreateItemLists():
    CollectionMaterialList, AuxCoreList, WeaponChipList, AccessoryList, WeaponAccessoryList, KeyItemList = [], [], [], [], [], []
    for item in Helper.InclRange(30340, 30445):
        ItemInfo(item, "CollectionMat", CollectionMaterialList)
    for item in TornaAuxCores:
        ItemInfo(item, "AuxCore", AuxCoreList)
    for item in TornaWeaponChips:
        ItemInfo(item, "WeaponChip", WeaponChipList)
    for item in Accessories + Helper.InclRange(657,680):
        ItemInfo(item, "Accessory", AccessoryList)
    for item in Helper.InclRange(585, 647):
        ItemInfo(item, "WeaponAccessory", WeaponAccessoryList)
    UncleanKeyItemList = [25455, Helper.InclRange(25457, 25466), Helper.InclRange(25479, 25494), Helper.InclRange(25531, 25535),MineralogyKey,SwordplayKey,FortitudeKey,ForestryKey,ManipEtherKey,KeenEyeKey,FocusKey,LightKey,GirlsTalkKey,EntomologyKey,MiningKey,BotanyKey,LockpickKey,IcthyologyKey,ComWaterKey,SuperstrKey,HHC_Key,LC_Key,CLC_Key,HWC_Key,PVC_Key,FVC_Key,AGC_Key,OTC_Key,DDC_Key,HGC_Key,JinAff,HazeAff,MythraAff,MinothAff,BrighidAff,AegaeonAff,HazeKey,AddamKey,MythraKey,MinothKey,HugoKey,BrighidKey,AegaeonKey, ValidRecipeInfoIDs, 26164, 26192, 26193, 26194, 26195, 25473, 25536]
    UncleanKeyItemList = Helper.MultiLevelListToSingleLevelList(UncleanKeyItemList)
    for item in UncleanKeyItemList:
        ItemInfo(item, "KeyItem", KeyItemList)
    FullItemList = [AccessoryList, WeaponAccessoryList, WeaponChipList, AuxCoreList, CollectionMaterialList, KeyItemList]
    return FullItemList

def SplitEnemyTypes(Enemies):
    NormalEnemies, QuestEnemies, BossEnemies, UniqueMonsters = [], [], [], []
    for enemy in Enemies:
        match enemy.type:
            case "uniquemonster":
                UniqueMonsters.append(enemy)
            case "boss":
                BossEnemies.append(enemy)
            case "questenemy":
                QuestEnemies.append(enemy)
            case "normalenemy":
                NormalEnemies.append(enemy)
    return NormalEnemies, QuestEnemies, BossEnemies, UniqueMonsters

def PlaceItems(FullItemList, ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList):
    # loop through main quest reqs, when you get to a story step with a quest, stop, see what requirements there are, and then place those items in valid spots
    #if an item gets placed in a spot with additional requirements, add those requirements to every single type of check that has a corresponding story step above that one
    # Also add those reqs to the current story step's requirements, and add those items to the list of items being placed in this sphere.
    # repeat
    # once done, fill remainder with misc items
    global PlacedItems
    PlacedItems = []
    global KeyItemtoLocDict
    KeyItemtoLocDict = {}
    Locs = [Sidequests, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList]
    CatList = [] # list of location categories
    global FilledLocations
    FilledLocations = []
    AllProgressLocations = []
    AllNonProgressLocations = []
    for loc in Locs:
        if loc[0].hasprogression == True:
            CatList.append(LocationCategory(loc[0].type, 1, loc))
            AllProgressLocations.extend(loc)
        else:
            CatList.append(LocationCategory(loc[0].type, 0, loc))
            AllNonProgressLocations.extend(loc)
    global AllLocations
    AllLocations = AllProgressLocations + AllNonProgressLocations
    if Options.StartwithIncreasedMovespeedOption.GetState():
        for loc in AllLocations:
            if loc.type == "boss":
                if loc.id == 1430:
                    loc.randomizeditems[8] = 25249
                    break
    for MQ in Mainquests:
        if MQ.itemreqs != []:
            CurrentStepReqs = MQ.itemreqs.copy()
            random.shuffle(CurrentStepReqs)
            CurrentStepReqs = [x for x in CurrentStepReqs if x not in PlacedItems]
            while len(CurrentStepReqs) > 0:
                ChosenItem = CurrentStepReqs[0]
                if ChosenItem not in PlacedItems:
                    ChosenItemCat = 0
                    for index in range(len(FullItemList)):
                        if ChosenItemCat != 0:
                            break
                        else:
                            for subitem in FullItemList[index]:
                                if ChosenItem == subitem.id:
                                    ChosenItemCat = subitem.type
                                    break
                    ValidLocations = DetermineValidItemSpots(ChosenItem, ChosenItemCat, CatList, MQ.id)
                    ValidLocations = [loc for loc in ValidLocations if loc not in FilledLocations]
                    decidedonlocation = False
                    stucknotice = 0
                    while decidedonlocation == False:
                        try:
                            ChosenLocation = random.choices(ValidLocations, weights=[loc.randomizeditems.count(-1)*loc.mainreq + len(loc.itemreqs) for loc in ValidLocations])[0]
                            for cat in CatList:
                                for loc in cat.fullloclist:
                                    if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                        ChosenLocation = loc
                        except:
                            raise Exception(f"Generation failed during location selection: No valid locations available for {ChosenItem}: ({ItemIDtoItemName[ChosenItem]})!")
                        if ChosenItemCat == "KeyItem" and ChosenLocation.type in ["uniquemonster", "boss", "normalenemy"]: # enemy drops need to be handled differently, there's a set spot for key items, only 1 spot is open, not 3, so we need to account for that
                            if ChosenLocation.randomizeditems[8] == -1: # if there's a spot open for a precious item, and there's no spots for other items left, the location needs to be removed from the list of remaining progress locations
                                ChosenLocation.randomizeditems[8] = ChosenItem
                                decidedonlocation = True
                            else:
                                ValidLocations.remove(ChosenLocation)
                                continue
                        elif ChosenLocation.type in ["uniquemonster", "boss", "normalenemy"]: #if the location the item is being placed is an enemy, but the item is not a key item, there's 3 slots open for it, so check those for an opening
                            if -1 not in ChosenLocation.randomizeditems[:8]:
                                ValidLocations.remove(ChosenLocation)
                                continue
                            else:
                                for itemspot in range(len(ChosenLocation.randomizeditems[:8])):
                                    if ChosenLocation.randomizeditems[itemspot] == -1: # if we find a progression spot
                                        ChosenLocation.randomizeditems[itemspot] = ChosenItem # put the chosen item into that spot
                                        decidedonlocation = True
                                        break # immediately leave loop, we don't want to replace all important drops
                        else:
                            for itemspot in range(len(ChosenLocation.randomizeditems)):
                                if ChosenLocation.randomizeditems[itemspot] == -1: # if we find a progression spot
                                    ChosenLocation.randomizeditems[itemspot] = ChosenItem # put the chosen item into that spot
                                    decidedonlocation = True
                                    break # immediately leave loop, we don't want to replace all important drops
                        stucknotice += 1
                        if stucknotice > 1000:
                            raise Exception(f"Generation got stuck trying to place {ChosenItem}: ({ItemIDtoItemName[ChosenItem]}!")
                    CurrentStepReqs.extend(ChosenLocation.itemreqs)
                    CurrentStepReqs = list(set(CurrentStepReqs))
                    CurrentStepReqs = [x for x in CurrentStepReqs if x not in PlacedItems]
                    UpdateAllItemReqs(CurrentStepReqs, Locs, ChosenLocation, ChosenItem, AllLocations, MQ.id)
                    for MQ2 in Mainquests:
                        if MQ2.id >= MQ.id:
                            MQ2.itemreqs.extend(CurrentStepReqs)
                            MQ2.itemreqs = list(set(MQ2.itemreqs))
                    CurrentStepReqs.remove(ChosenItem)               
                    PlacedItems.append(ChosenItem)
                    KeyItemtoLocDict[ChosenItem] = ChosenLocation
                    PlacedItems.sort()
                    if ChosenLocation.type in ["uniquemonster", "boss", "normalenemy"] and ChosenLocation.randomizeditems.count(-1) == 1:
                        for cat in CatList:
                            for loc in cat.remlocations:
                                if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                    ChosenLocation = loc
                            if ChosenLocation in cat.remlocations:
                                cat.remlocations.remove(ChosenLocation)
                                FilledLocations.append(ChosenLocation)
                                break
                    else:
                        if ChosenLocation.randomizeditems.count(-1) == 0:
                            for cat in CatList:
                                for loc in cat.remlocations:
                                    if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                        ChosenLocation = loc
                                if ChosenLocation in cat.remlocations:
                                    cat.remlocations.remove(ChosenLocation)
                                    FilledLocations.append(ChosenLocation)
                                    break
    # for now, I'm not placing progress items that unlock checks that aren't required for the playthrough
    FullItemReqList = []
    for loc in Locs:
        for check in loc:
            FullItemReqList.extend(check.itemreqs)
    FullItemReqList.extend(ValidRecipeInfoIDs)
    FullItemReqList = list(set(FullItemReqList))
    FullItemReqList.sort()
    UnplacedProgressionItems = [x for x in FullItemReqList if x not in PlacedItems] # this holds the items that unlock stuff but don't logically contribute to the playthrough

    # place filler items in all remaining checks, regardless of if it has progression enabled.

    global HelpfulUpgrades
    HelpfulUpgrades = [MineralogyKey,SwordplayKey,FortitudeKey,ForestryKey,ManipEtherKey,KeenEyeKey,FocusKey,LightKey,GirlsTalkKey,EntomologyKey,MiningKey,BotanyKey,LockpickKey,IcthyologyKey,ComWaterKey,SuperstrKey,HHC_Key,LC_Key,CLC_Key,HWC_Key,PVC_Key,FVC_Key,AGC_Key,OTC_Key,DDC_Key,HGC_Key,JinAff,HazeAff,MythraAff,MinothAff,BrighidAff,AegaeonAff,HazeKey,AddamKey,MythraKey,MinothKey,HugoKey,BrighidKey,AegaeonKey]
    HelpfulUpgrades = Helper.MultiLevelListToSingleLevelList(HelpfulUpgrades)
    HelpfulUnplacedUpgrades = []
    for item in FullItemList[5]:
        if item.id in HelpfulUpgrades and item.id not in PlacedItems:
            HelpfulUnplacedUpgrades.append(item)
    PoolMaxItemsPerCategory = 200
    AccessoryList = FullItemList[0]
    WeaponAccessoryList = FullItemList[1]
    WeaponChipList = [chip for chip in FullItemList[2] if chip not in FullItemReqList]
    AuxCoreList = FullItemList[3]
    CollectionMaterialList = FullItemList[4]
    CollectionMaterialList = [item for item in CollectionMaterialList if item.id not in FullItemReqList]
    NewItemList = [AccessoryList, WeaponAccessoryList, WeaponChipList, AuxCoreList]
    NewItemList.append(CollectionMaterialList)
    NewItemList.append(HelpfulUnplacedUpgrades)
    SelectiveItemPool = []
    for cat in NewItemList:
        SelectiveItemPool.append(random.choices(cat, k = PoolMaxItemsPerCategory))
    SelAccList, SelWAccList, SelChipList, SelXCoreList, SelMatList, SelUpgradeList = SelectiveItemPool[0], SelectiveItemPool[1], SelectiveItemPool[2], SelectiveItemPool[3], SelectiveItemPool[4], SelectiveItemPool[5]
    SelFull = SelAccList + SelWAccList + SelChipList + SelXCoreList + SelMatList + SelUpgradeList
    ValidItemtoLoc = {
        'sidequest': [x for x in SelFull if x not in SelMatList],
        'normalenemy': [x for x in SelFull if x not in SelUpgradeList],
        'questenemy': [x for x in SelFull if x not in SelMatList + SelUpgradeList],
        'boss': [x for x in SelFull if x not in SelMatList + SelUpgradeList],
        'uniquemonster': [x for x in SelFull if x not in SelUpgradeList],
        'shop': SelFull,
        'redbag': [x for x in SelFull if x not in SelMatList],
        'misc': [x for x in SelFull if x not in SelMatList],
        'chest': [x for x in SelFull if x not in SelMatList],
        'tornacollectionpoint': [x for x in SelFull if x not in SelUpgradeList],
        'gormottcollectionpoint': [x for x in SelFull if x not in SelUpgradeList],
    }
    for cat in CatList:
        ValidItems = ValidItemtoLoc[cat.category]
        if cat.category not in ["uniquemonster", "normalenemy", "boss", "questenemy"]:
            for remloc in cat.fullloclist:
                for item in range(len(remloc.randomizeditems)):
                    if remloc.randomizeditems[item] in [0, -1]:
                        if Helper.OddsCheck(15):
                            ChosenValidItem = random.choice(ValidItems)
                            remloc.randomizeditems[item] = ChosenValidItem.id
                            if ChosenValidItem in SelUpgradeList:
                                for cat in ValidItemtoLoc:
                                    if ChosenValidItem in ValidItemtoLoc[cat]:
                                        ValidItemtoLoc[cat].remove(ChosenValidItem)
                        else:
                            remloc.randomizeditems[item] = 0
                FilledLocations.append(remloc)
        else:
            for remloc in cat.fullloclist:
                for item in range(8):
                    if remloc.randomizeditems[item] in [0, -1]:
                        if Helper.OddsCheck(15):
                            ChosenValidItem = random.choice(ValidItems)
                            remloc.randomizeditems[item] = ChosenValidItem.id
                            if ChosenValidItem in SelUpgradeList:
                                for cat in ValidItemtoLoc:
                                    if ChosenValidItem in ValidItemtoLoc[cat]:
                                        ValidItemtoLoc[cat].remove(ChosenValidItem)
                        else:
                            remloc.randomizeditems[item] = 0
                if remloc.randomizeditems[8] in [0, -1]:
                    if Helper.OddsCheck(35):
                        try:
                            ChosenValidItem = random.choice(SelUpgradeList)
                            remloc.randomizeditems[8] = ChosenValidItem.id
                            if ChosenValidItem in SelUpgradeList:
                                for cat in ValidItemtoLoc:
                                    if ChosenValidItem in ValidItemtoLoc[cat]:
                                        ValidItemtoLoc[cat].remove(ChosenValidItem)
                        except: # in case we run out of upgrade items to place
                            remloc.randomizeditems[item] = 0
                    else:
                        remloc.randomizeditems[8] = 0
                FilledLocations.append(remloc)
    for cat in CatList:
        for loc in cat.fullloclist:
            if -1 in loc.randomizeditems:
                for item in range(len(loc.randomizeditems)):
                    if loc.randomizeditems[item] == -1:
                        loc.randomizeditems[item] = 0
                        print(f"name: {loc.name}, type: {loc.type}")
    PutItemsInSpots(Locs)

def DetermineValidItemSpots(ChosenItem, ChosenItemCat, CatList, CurrentStoryStep = -1): # certain item types cannot coexist with certain location types. collectible items cannot be put as quest rewards, since there is no renewable source of them in case the player uses them all up, for instance.
    ValidItemSpots = []
    match ChosenItemCat:
        case "CollectionMat":
            for cat in CatList:
                if cat.isprogresscategory == 1 and cat.category in ["uniquemonster", "normalenemy", "shop", "tornacollectionpoint", "gormottcollectionpoint"]:
                    ValidItemSpots.extend(cat.remlocations)
        case "KeyItem":
            for cat in CatList:
                if cat.isprogresscategory == 1 and cat.category in ["sidequest", "uniquemonster", "boss", "normalenemy", "redbag", "misc", "chest", "shop", "tornacollectionpoint", "gormottcollectionpoint"]:
                    ValidItemSpots.extend(cat.remlocations)
        case _:
            for cat in CatList:
                if cat.isprogresscategory == 1 and cat.category not in ["questenemy"]:
                    ValidItemSpots.extend(cat.remlocations)
    TempValidItemSpots = [loc for loc in ValidItemSpots if ChosenItem not in loc.itemreqs] # make sure the item isn't put in a spot locked by itself
    if TempValidItemSpots == []:
        raise Exception(f"Ran out of valid locations when trying to ensure {ChosenItem}: ({ItemIDtoItemName[ChosenItem]} was not locked by itself!")
    else:
        ValidItemSpots = TempValidItemSpots
    if CurrentStoryStep != -1:
        TempValidItemSpots = [loc for loc in ValidItemSpots if loc.mainreq < CurrentStoryStep + 1] # make sure the item isn't past the spot in the story where it can be accessed
        if TempValidItemSpots == []:
            raise Exception(f"Ran out of valid locations when trying to ensure {ChosenItem}: ({ItemIDtoItemName[ChosenItem]} was not placed further ahead in the story than the player can reach!")
        else:
            ValidItemSpots = TempValidItemSpots
    InvalidNonSidequestLocs = []
    for loc in ValidItemSpots:
        if loc.type != "sidequest":
            if loc.nearloc in RemovedGormottLocs:
                InvalidNonSidequestLocs.append(loc)
    TempValidItemSpots = [loc for loc in ValidItemSpots if loc not in InvalidNonSidequestLocs]
    if TempValidItemSpots == []:
        raise Exception(f"Ran out of valid locations when trying to ensure {ChosenItem}: ({ItemIDtoItemName[ChosenItem]} was not locked by itself!")
    else:
        ValidItemSpots = TempValidItemSpots
    
    return ValidItemSpots

def UpdateAllItemReqs(CurrentStepReqs, Locations, ChosenLocation, ChosenItem, AllLocations, CurrentStepNumber = -1):
    for loc in AllLocations:
        if ChosenItem in loc.itemreqs:
            loc.itemreqs += ChosenLocation.itemreqs
            loc.itemreqs = list(set(loc.itemreqs))
    if CurrentStepNumber != -1:
        if CurrentStepReqs != []:
            for loctype in Locations:
                for subloc in loctype:
                    if subloc.mainreq > CurrentStepNumber:
                        try:
                            subloc.itemreqs.extend(CurrentStepReqs)
                            subloc.itemreqs = list(set(subloc.itemreqs))
                        except:
                            raise Exception(f"Generation failed to update item requirements: Invalid item placed at {subloc}!")

def AdjustLevelUpReqs(MinLogicalLevel):
    with open("./XC2/_internal/JsonOutputs/common/BTL_Grow.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [2,3]:
                row["LevelExp2"] == 1
            if 4 <= row["$id"] <= MinLogicalLevel:
                row["LevelExp2"] == 9999
            if row["$id"] > MinLogicalLevel - 1:
                row["LevelExp2"] = 1
            if row["$id"] > 99:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PutItemsInSpots(Locs2): # now we actually feed the items into their corresponding pipelines in the bdats
    # Locs = ConsolidateLevelUpTokens(Locs2) no longer need to consolidate levelup tokens, since we use level cap now
    Locs = Locs2
    # sidequests
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] not in Helper.InclRange(1088, 1202):
                row["EXP"] = row["ItemID1"] = row["ItemNumber1"] = row["ItemID2"] = row["ItemNumber2"] = row["ItemID3"] = row["ItemNumber3"] = row["ItemID4"] = row["ItemNumber4"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for sidequest in Locs[0]:
            for rewardid in sidequest.rewardids: # currently only one quest has multiple reward ids, but they all need to have the same ending rewards.
                for row in data["rows"]:
                    if row["$id"] == rewardid:
                        for i in range(4):
                            row[f"ItemID{i+1}"] = sidequest.randomizeditems[i]
                            if row[f"ItemID{i+1}"] != 0:
                                row[f"ItemNumber{i+1}"] = 1
                            else:
                                row[f"ItemNumber{i+1}"] = 0
                        break      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # enemy drops
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", Helper.ExtendListtoLength(["ItemID1", "DropProb1", "NoGetByEnh1", "FirstNamed1"], 32, "inputlist[i-4][:-1] +  str(int(inputlist[i-4][-1:])+1)"), 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", ["DropProb1", "DropProb2", "DropProb3", "DropProb4", "DropProb5", "DropProb6", "DropProb7", "DropProb8"], 1000) # the first loot item in each row has a 100% chance to drop every time.
    MaxEnemyLootID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", "$id")
    if MaxDropTableID > MaxEnemyLootID: # need to add a row to BTL_EnDropItem for each enemy past the max # of rows 
        NewLootIDRows = []
        for tableid in range(MaxEnemyLootID + 1, MaxDropTableID + 1):
            NewLootIDRows.append([{"$id": tableid, "LimitNum": 0, "SelectType": 0, "ItemID1": 0, "DropProb1": 0, "NoGetByEnh1": 0, "FirstNamed1": 0, "ItemID2": 0, "DropProb2": 0, "NoGetByEnh2": 0, "FirstNamed2": 0, "ItemID3": 0, "DropProb3": 0, "NoGetByEnh3": 0, "FirstNamed3": 0, "ItemID4": 0, "DropProb4": 0, "NoGetByEnh4": 0, "FirstNamed4": 0, "ItemID5": 0, "DropProb5": 0, "NoGetByEnh5": 0, "FirstNamed5": 0, "ItemID6": 0, "DropProb6": 0, "NoGetByEnh6": 0, "FirstNamed6": 0, "ItemID7": 0, "DropProb7": 0, "NoGetByEnh7": 0, "FirstNamed7": 0, "ItemID8": 0, "DropProb8": 0, "NoGetByEnh8": 0, "FirstNamed8": 0}])
        JSONParser.ExtendJSONFile("common/BTL_EnDropItem.json", NewLootIDRows)
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for enemytype in range(1, 5):
            for enemy in Locs[enemytype]:
                for row in data["rows"]:
                    if row["$id"] == enemy.id:
                        row["DropTableID"] = enemy.droptableids[0]
                        row["PreciousID"] = enemy.randomizeditems[8] # the precious id just gets the id itself plugged in here
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False) 
    with open("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for enemytype in range(1, 5):
            for enemy in Locs[enemytype]:
                for row in data["rows"]:
                    if row["$id"] == enemy.droptableids[0]:
                        for i in range(1, 9):
                            row[f"ItemID{i}"] = enemy.randomizeditems[i - 1]
                            if row[f"ItemID{i}"] == 0:
                                row[f"DropProb{i}"] = 0
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # shops
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # alters the NpcPop file to make the bards call different Event IDs and different Shop IDs
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 40660:
                row["Condition"] = 0
                row["EventID"] = 40339
                row["ShopID"] = 67
            if row["$id"] == 40662:
                row["Condition"] = 0
                row["EventID"] = 40442
                row["ShopID"] = 68      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: # Changing ShopList
        data = json.load(file)
        for shop in Locs[5]:
            for row in data["rows"]:
                if row["$id"] == shop.shoplistid:
                    row["ShopType"] = 0 # need to convert all shops to Normal shops if they aren't already
                    row["TableID"] = shop.shopnormalid
                    for i in range(1,6):
                        row[f"Discount{i}"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: # Adding items to ShopNormal
        data = json.load(file)
        for shop in Locs[5]:
            for row in data["rows"]:
                if row["$id"] == shop.shopnormalid:
                    for key, value in row.items(): # clear out the other stuff in the row
                        if key != "$id":
                            row[key] = 0
                    for defnum in range(0, 10):
                        row[f"DefItem{defnum + 1}"] = shop.randomizeditems[defnum]
                    for addtemnum in range(10, 15):
                        row[f"Addtem{addtemnum - 9}"] = shop.randomizeditems[addtemnum]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # redbags
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_PreciousPopList.json", 'r+', encoding='utf-8') as file: # adding the redbag items
        data = json.load(file)
        for redbag in Locs[6]:
            for row in data["rows"]:
                if row["$id"] == redbag.id:
                    row["QuestFlag"], row["QuestFlagMin"], row["QuestFlagMax"] = 0, 0, 0
                    row["itmID"] = redbag.randomizeditems[0]
                    if row["itmID"] == 0: # if there's no item, we just disappear the bag.
                        row["Condition"] = 2112
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # misc
    with open("./XC2/_internal/JsonOutputs/common/FLD_AddItem.json", 'r+', encoding='utf-8') as file: # adding the misc items
        data = json.load(file)
        for miscitem in Locs[7]:
            for row in data["rows"]:
                if row["$id"] == miscitem.fldadditemid:
                    row["ItemID1"] = miscitem.randomizeditems[0]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # chests
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_TboxPop.json", 'r+', encoding='utf-8') as fileT: # Torna chests
        dataT = json.load(fileT)
        with open("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_TboxPop.json", 'r+', encoding='utf-8') as fileG: # Gormott chests
            dataG = json.load(fileG)
            for chest in Locs[8]:
                if chest.continent == "Torna":
                    for rowT in dataT["rows"]:
                        if rowT["$id"] == chest.id:
                            for i in range(1, 9):
                                rowT[f"itm{i}ID"] = chest.randomizeditems[i-1]
                                if rowT[f"itm{i}ID"] != 0:
                                    rowT[f"itm{i}Num"] = 1
                                    rowT[f"itm{i}Per"] = 100
                                else:
                                    rowT[f"itm{i}Num"] = 0
                                    rowT[f"itm{i}Per"] = 0
                            break
                else:
                    for rowG in dataG["rows"]:
                        if rowG["$id"] == chest.id:
                            for i in range(1, 9):
                                rowG[f"itm{i}ID"] = chest.randomizeditems[i-1]
                                if rowG[f"itm{i}ID"] != 0:
                                    rowG[f"itm{i}Num"] = 1
                                    rowG[f"itm{i}Per"] = 100
                                else:
                                    rowG[f"itm{i}Num"] = 0
                                    rowG[f"itm{i}Per"] = 0
                            break
            fileG.seek(0)
            fileG.truncate()
            json.dump(dataG, fileG, indent=2, ensure_ascii=False)
        fileT.seek(0)
        fileT.truncate()
        json.dump(dataT, fileT, indent=2, ensure_ascii=False)
    
    # collectionpoints
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as file: # Torna collection points
        data = json.load(file)
        for collectionpoint in Locs[9]:
            for row in data["rows"]:
                if str(row["$id"]) == collectionpoint.id:
                    row["POP_TIME"] = 256
                    row["popWeather"] = 0
                    row["CollectionTable"] = collectionpoint.collectiontableid
                    if row["Condition"] not in [3230, 3231]: # we only care about the gold and silver seeker conditions
                        row["Condition"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
       
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as file: # Gormott collection points
        data = json.load(file)
        for collectionpoint in Locs[10]:
            for row in data["rows"]:
                if str(row["$id"]) == collectionpoint.id:
                    row["POP_TIME"] = 256
                    row["popWeather"] = 0
                    row["CollectionTable"] = collectionpoint.collectiontableid
                    if row["Condition"] not in [3230, 3231]: # we only care about the gold and silver seeker conditions
                        row["Condition"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    DesiredMaxCollectionTableID = 501 # known, will always be the case, 1 collection point -> 1 collection table
    CurMaxCollectionTableID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", "$id")
    NewCollectionTableRows = []
    for i in range(CurMaxCollectionTableID + 1, DesiredMaxCollectionTableID + 1):
        NewCollectionTableRows.append([{"$id": i, "FSID": 0, "randitmPopMin": 0, "randitmPopMax": 0, "itm1ID": 0, "itm1Per": 0, "itm2ID": 0, "itm2Per": 0, "itm3ID": 0, "itm3Per": 0, "itm4ID": 0, "itm4Per": 0, "goldMin": 0, "goldMax": 0, "goldPopMin": 0, "goldPopMax": 0, "rsc_paramID": 0, "categoryName": 0, "ZoneID": 0}])
    JSONParser.ExtendJSONFile("common/FLD_CollectionTable.json", NewCollectionTableRows)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", ["itm1Per", "itm2Per", "itm3Per", "itm4Per"], 100)
    with open("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", 'r+', encoding='utf-8') as file: # collection table file
        data = json.load(file)
        for i in range(9, 11):
            for collectionpoint in Locs[i]:
                for row in data["rows"]:
                    itemcount = 0
                    if row["$id"] == collectionpoint.collectiontableid:
                        row["FSID"] = random.choice(Helper.InclRange(68, 72)) # add a bonus for a random field skill
                        for item in range(1, 5):
                            row[f"itm{item}ID"] = collectionpoint.randomizeditems[item-1]
                            itemcount += 1
                            if row[f"itm{item}ID"] == 0:
                                row[f"itm{item}Per"] = 0
                                itemcount -= 1
                        row["randitmPopMax"] = itemcount + 2 # we add 2 more just to make it so you dont need to farm the collectables as much
                        row["randitmPopMin"] = itemcount + 2
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ConsolidateLevelUpTokens(Locs): # need to now remove all level up tokens and replace them with 1 singular level up token, so the shop will only require 1 input trade.
    for cat in Locs:
        for loc in cat:
            for req in range(len(loc.itemreqs)):
                if loc.itemreqs[req] in LevelUpTokens:
                    loc.itemreqs[req] = 25631
    return Locs

def AddMissingKeyItems():
    NewDescID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    KeyItemNames = ["Mineralogy Lv. 1", "Mineralogy Lv. 2", "Mineralogy Lv. 3", "Swordplay Lv. 1", "Swordplay Lv. 2", "Swordplay Lv. 3", "Fortitude Lv. 1", "Fortitude Lv. 2", "Fortitude Lv. 3", "Forestry Lv. 1", "Forestry Lv. 2", "Forestry Lv. 3", "Manipulate Ether Lv. 1", "Manipulate Ether Lv. 2", "Manipulate Ether Lv. 3", "Keen Eye Lv. 1", "Keen Eye Lv. 2", "Keen Eye Lv. 3", "Focus Lv. 1", "Focus Lv. 2", "Focus Lv. 3", "Power of Light Lv. 1", "Power of Light Lv. 2", "Power of Light Lv. 3", "Girls' Talk", "Entomology Lv. 1", "Entomology Lv. 2", "Entomology Lv. 3", "Mining Lv. 1", "Mining Lv. 2", "Mining Lv. 3", "Botany Lv. 1", "Botany Lv. 2", "Botany Lv. 3", "Lockpicking Lv. 1", "Lockpicking Lv. 2", "Lockpicking Lv. 3", "Icthyology Lv. 1", "Icthyology Lv. 2", "Icthyology Lv. 3", "Command Water Lv. 1", "Command Water Lv. 2", "Command Water Lv. 3", "Superstrength Lv. 1", "Superstrength Lv. 2", "Superstrength Lv. 3", "Hidden Hunting Camp","Lakeshore Campsite","Coolley Lake Camp","Hoary Weald Camp","Porton Village Camp","Feltley Village Camp","Aletta Garrison Camp","Olnard's Trail Campsite","Dannagh Desert Camp","Holy Gate Camp","Jin Affinity Lv. 2", "Jin Affinity Lv. 3", "Jin Affinity Lv. 4", "Jin Affinity Lv. 5", "Haze Affinity Lv. 2", "Haze Affinity Lv. 3", "Haze Affinity Lv. 4", "Haze Affinity Lv. 5", "Mythra Affinity Lv. 2", "Mythra Affinity Lv. 3", "Mythra Affinity Lv. 4", "Mythra Affinity Lv. 5", "Minoth Affinity Lv. 2", "Minoth Affinity Lv. 3", "Minoth Affinity Lv. 4", "Minoth Affinity Lv. 5", "Brighid Affinity Lv. 2", "Brighid Affinity Lv. 3", "Brighid Affinity Lv. 4", "Brighid Affinity Lv. 5", "Aegaeon Affinity Lv. 2", "Aegaeon Affinity Lv. 3", "Aegaeon Affinity Lv. 4", "Aegaeon Affinity Lv. 5", "Haze Key", "Addam Key", "Mythra Key", "Minoth Key", "Hugo Key", "Brighid Key", "Aegaeon Key", "Level Up Token"]
    KeyItemDescriptions = ["Unlocks the Mineralogy\nLv. 1 Field Skill.", "Unlocks the Mineralogy\nLv. 2 Field Skill.", "Unlocks the Mineralogy\nLv. 3 Field Skill.", "Unlocks the Swordplay\nLv. 1 Field Skill.", "Unlocks the Swordplay\nLv. 2 Field Skill.", "Unlocks the Swordplay\nLv. 3 Field Skill.", "Unlocks the Fortitude\nLv. 1 Field Skill.", "Unlocks the Fortitude\nLv. 2 Field Skill.", "Unlocks the Fortitude\nLv. 3 Field Skill.", "Unlocks the Forestry\nLv. 1 Field Skill.", "Unlocks the Forestry\nLv. 2 Field Skill.", "Unlocks the Forestry\nLv. 3 Field Skill.", "Unlocks the Manipulate Ether\nLv. 1 Field Skill.", "Unlocks the Manipulate Ether\nLv. 2 Field Skill.", "Unlocks the Manipulate Ether\nLv. 3 Field Skill.", "Unlocks the Keen Eye\nLv. 1 Field Skill.", "Unlocks the Keen Eye\nLv. 2 Field Skill.", "Unlocks the Keen Eye\nLv. 3 Field Skill.", "Unlocks the Focus\nLv. 1 Field Skill.", "Unlocks the Focus\nLv. 2 Field Skill.", "Unlocks the Focus\nLv. 3 Field Skill.", "Unlocks the Power of Light\nLv. 1 Field Skill.", "Unlocks the Power of Light\nLv. 2 Field Skill.", "Unlocks the Power of Light\nLv. 3 Field Skill.", "Unlocks the Girls' Talk Field Skill.", "Unlocks the Entomology\nLv. 1 Field Skill.", "Unlocks the Entomology\nLv. 2 Field Skill.", "Unlocks the Entomology\nLv. 3 Field Skill.", "Unlocks the Mining\nLv. 1 Field Skill.", "Unlocks the Mining\nLv. 2 Field Skill.", "Unlocks the Mining\nLv. 3 Field Skill.", "Unlocks the Botany\nLv. 1 Field Skill.", "Unlocks the Botany\nLv. 2 Field Skill.", "Unlocks the Botany\nLv. 3 Field Skill.", "Unlocks the Lockpicking\nLv. 1 Field Skill.", "Unlocks the Lockpicking\nLv. 2 Field Skill.", "Unlocks the Lockpicking\nLv. 3 Field Skill.", "Unlocks the Icthyology\nLv. 1 Field Skill.", "Unlocks the Icthyology\nLv. 2 Field Skill.", "Unlocks the Icthyology\nLv. 3 Field Skill.", "Unlocks the Command Water\nLv. 1 Field Skill.", "Unlocks the Command Water\nLv. 2 Field Skill.", "Unlocks the Command Water\nLv. 3 Field Skill.", "Unlocks the Superstrength\nLv. 1 Field Skill.", "Unlocks the Superstrength\nLv. 2 Field Skill.", "Unlocks the Superstrength\nLv. 3 Field Skill.", "Unlocks the ability to rest at\nthe Hidden Hunting Campsite.", "Unlocks the ability to rest at\nthe Lakeshore Campsite.", "Unlocks the ability to rest at\nthe Coolley Lake Campsite.", "Unlocks the ability to rest at\nthe Hoary Weald Campsite.", "Unlocks the ability to rest at\nthe Porton Village Campsite.", "Unlocks the ability to rest at\nthe Feltley Village Campsite.", "Unlocks the ability to rest at\nthe Aletta Garrison Campsite.", "Unlocks the ability to rest at\nthe Olnard's Trail Campsite.", "Unlocks the ability to rest at\nthe Dannagh Desert Campsite.", "Unlocks the ability to rest at\nthe Holy Gate Campsite.","Unlocks Level 2 of \nJin's Affinity Chart.", "Unlocks Level 3 of \nJin's Affinity Chart.", "Unlocks Level 4 of \nJin's Affinity Chart.", "Unlocks Level 5 of \nJin's Affinity Chart.", "Unlocks Level 2 of \nHaze's Affinity Chart.", "Unlocks Level 3 of \nHaze's Affinity Chart.", "Unlocks Level 4 of \nHaze's Affinity Chart.", "Unlocks Level 5 of \nHaze's Affinity Chart.", "Unlocks Level 2 of\nMythra's Affinity Chart.", "Unlocks Level 3 of\nMythra's Affinity Chart.", "Unlocks Level 4 of\nMythra's Affinity Chart.", "Unlocks Level 5 of\nMythra's Affinity Chart.", "Unlocks Level 2 of\nMinoth's Affinity Chart.", "Unlocks Level 3 of\nMinoth's Affinity Chart.", "Unlocks Level 4 of\nMinoth's Affinity Chart.", "Unlocks Level 5 of\nMinoth's Affinity Chart.", "Unlocks Level 2 of \nBrighid's Affinity Chart.", "Unlocks Level 3 of \nBrighid's Affinity Chart.", "Unlocks Level 4 of \nBrighid's Affinity Chart.", "Unlocks Level 5 of \nBrighid's Affinity Chart.", "Unlocks Level 2 of \nAegaeon's Affinity Chart.", "Unlocks Level 3 of \nAegaeon's Affinity Chart.", "Unlocks Level 4 of \nAegaeon's Affinity Chart.", "Unlocks Level 5 of \nAegaeon's Affinity Chart.", 'Unlocks the ability to add\nHaze to your party.', 'Unlocks the ability to add\nAddam to your party.', 'Unlocks the ability to add\nMythra to your party.', 'Unlocks the ability to add\nMinoth to your party.', 'Unlocks the ability to add\nHugo to your party.', 'Unlocks the ability to add\nBrighid to your party.', 'Unlocks the ability to add\nAegaeon to your party.', "Can be exchanged for 1 level's worth of EXP at the Token Exchange."]
    KeyItemPreciousIDs = [25544, 25545, 25546, 25547, 25548, 25549, 25550, 25551, 25552, 25553, 25554, 25555, 25556, 25557, 25558, 25559, 25560, 25561, 25562, 25563, 25564, 25565, 25566, 25567, 25568, 25569, 25570, 25571, 25572, 25573, 25574, 25575, 25576, 25577, 25578, 25579, 25580, 25581, 25582, 25583, 25584, 25585, 25586, 25587, 25588, 25589, 25590, 25591, 25592, 25593, 25594, 25595, 25596, 25597, 25598, 25599, 25600, 25601, 25602, 25603, 25604, 25605, 25606, 25607, 25608, 25609, 25610, 25611, 25612, 25613, 25614, 25615, 25616, 25617, 25618, 25619, 25620, 25621, 25622, 25623, 25624, 25625, 25626, 25627, 25628, 25629, 25630, 25631]
    KeyItemList = []
    for name in range(len(KeyItemNames)):
        KeyItemParams(f"{KeyItemNames[name]}",f"{KeyItemDescriptions[name]}", NewDescID, NewDescID + 1, KeyItemPreciousIDs[name], KeyItemList)
        NewDescID += 2
    NewPreciousListItems, NewDescList = [], []
    for item in KeyItemList:
        NewPreciousListItems.append([{"$id": item.preciousid, "Name": item.nameid, "Caption": item.captionid, "Category": 29, "Type": 0, "Price": 1, "ValueMax": 1, "ClearNewGame": 1, "NoMultiple": 0, "sortJP": item.preciousid, "sortGE": item.preciousid, "sortFR": item.preciousid, "sortSP": item.preciousid, "sortIT": item.preciousid, "sortGB": item.preciousid, "sortCN": item.preciousid, "sortTW": item.preciousid, "sortKR": item.preciousid}])
        NewDescList.append([{"$id": item.nameid, "style": 36, "name": item.name}])
        NewDescList.append([{"$id": item.captionid, "style": 61, "name": item.caption}])
    JSONParser.ExtendJSONFile("common/ITM_PreciousListIra.json", NewPreciousListItems)
    JSONParser.ExtendJSONFile("common_ms/itm_precious.json", NewDescList)

def CreateLevelCaps(): 
    # makes the level caps in the files, removing all other xp sources than the story bosses, which give max xp possible. all other sources will give 1 xp.
    # it takes max xp to level up past a level cap, and 1 xp otherwise.
    # technically this is cheeseable with fights where there are multiple enemies, if you defeat the one that lets you pass the level cap, then die to another, you can get that same xp again, I believe.
    # unless you do ExpRevLow, set that to 0 when you're over .
    with open("./XC2/_internal/JsonOutputs/common/BTL_Grow.json", 'r+', encoding='utf-8') as file: # xp requirements file
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case 2 | 12 | 25 | 34 | 46:
                    row["LevelExp2"] = 99999
                case 18:
                    row["LevelExp2"] = 10
                case 38:
                    row["LevelExp2"] = 1000
                case _ if row["$id"] >= 56:
                    row["LevelExp2"] = 99999
                case _:
                    row["LevelExp2"] = 0
            row["EnemyExp"] = 1000 # believe this is the base xp gained by defeating an enemy of this level, before accounting for level differences
            row["EnemyWP"] = row["EnemyWP"] * 10
            row["EnemySP"] = row["EnemySP"] * 10
            row["EnemyGold"] = row["EnemyGold"] * 10
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_Lv_Rev.json", ["ExpRevHigh", "ExpRevLow", "ExpRevLow2"], 100) # make it so you always get 100% of the exp you earn, regardless of level difference.
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # enemy file
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case 1434:
                    row["ExpRev"] = 1
                case 1632:
                    row["ExpRev"] = 100
                case 1430 | 1433 | 1437 | 1442 | 1443: # all enemies that raise level cap upon defeat
                    row["ExpRev"] = 10000 # 10000% of 1000
                case _:
                    row["ExpRev"] = 0 # all other enemies get 0*99999 = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    LandmarkFiles = ["./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_LandmarkPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_LandmarkPop.json"]
    for map in LandmarkFiles:
        with open(map, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    row["getEXP"] = 10
                    row["getSP"] = row["getSP"] * 10 # amp the SP gains by 10, to reduce grinding
                    row["developZone"] = 0
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", ["EXP"], 0) # doing quests doesn't reward any xp
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json"], ["Gold", "SP"], ['row[key] * 10']) # quests reward 10x gold and sp
    
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # needed to make enemies over level 55 not impossible to kill while still being logically available. Setting the level cap to 100 makes the final boss a joke when you insta level up to that.
        data = json.load(file)
        for row in data["rows"]:
            if row["Lv"] > 55:
                row["Lv"] = 55
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/BTL_Lv_Rev.json", 'r+', encoding='utf-8') as file: # needed to make enemies over level 55 not impossible to kill while still being logically available. Setting the level cap to 100 makes the final boss a joke when you insta level up to that.
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 6:
                row["ExpRevLow"] = 0
                row["ExpRevLow2"] = 0
            row["ExpRevHigh"] = 100
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def HugoComeBack(): # Hugo is scripted to leave the party with Aegaeon whenever you receive the quest "Feeding an Army". We don't want this, it messes with logic (at least right now).
    with open("./XC2/_internal/JsonOutputs/common/EVT_listFev01.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [30185, 30187]:
                row["scriptName"] = ""
                row["scriptStartId"] = 0
            if row["$id"] > 30187:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AdjustSlateValue(): # changes the slate pieces to be worth 1 point apiece, and make the requirements for the different sections 5, 10, and 16 points.
    with open("./XC2/_internal/JsonOutputs/common/FLD_ConditionFlag.json", 'r+', encoding='utf-8') as file: # various conditions related to how many pieces you've inserted
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case 1401:
                    row["FlagMin"] = 16
                    row["FlagMax"] = 16
                case 1445:
                    row["FlagMin"] = 5
                    row["FlagMax"] = 5
                case 1446:
                    row["FlagMin"] = 10
                    row["FlagMax"] = 10
                case 1447:
                    row["FlagMin"] = 16
                    row["FlagMax"] = 16
                case 1448:
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    SlateRows = Helper.InclRange(723, 738)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case item if item in SlateRows: # these rows contain the slate pieces, provided there's no randomization done on where a shop item needs to be inserted.
                    row["AddFlagValue"] = 1
                case 739:
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def EternityLoamChange(): # need to make eternity loam only require 1 of for the quest "Unforgotten Promise".
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestCollect.json", 'r+', encoding='utf-8') as file: # not sure which row is actually used by the quest, but both 274 and 316 have the same item id, so do it to both
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [274, 316]:
                row["Count"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SkillTreeSetup(): # sets up the blade skill tree nodes for each blade.
    Blades = ["Jin", "Haze", "Mythra", "Minoth", "Brighid", "Aegaeon"]
    FSkill1Names = ["Mineralogy", "Forestry", "Focus", "Entomology", "Botany", "Ichthyology"]
    FSkill2Names = ["Swift Swordplay", "Manipulate Ether", "Power of Light", "Mining", "Lockpicking", "Command Water"]
    FSkill3Names = ["Fortitude", "Keen Eye", "Girls' Talk", 0, 0, "Superstrength"]
    BladeInfoList = []
    FSkill1IDs = [1686, 1696, 1706, 1716, 1726, 1736]
    FSkill2IDs = [1687, 1697, 1707, 1717, 1727, 1737]
    FSkill3IDs = [1688, 1698, 1708, 1718, 1728, 1738]
    AffinityIDs = [1679, 1689, 1699, 1709, 1719, 1729]
    FSkill1UnlockKeyIDs = [MineralogyKey, ForestryKey, FocusKey, EntomologyKey, BotanyKey, IcthyologyKey]
    FSkill2UnlockKeyIDs = [SwordplayKey, ManipEtherKey, LightKey, MiningKey, LockpickKey, ComWaterKey]
    FSkill3UnlockKeyIDs = [FortitudeKey, KeenEyeKey, GirlsTalkKey, 0, 0, SuperstrKey]
    AffinityUnlockKeys = [JinAff, HazeAff, MythraAff, MinothAff, BrighidAff, AegaeonAff]
    AllBladeIDs = FSkill1IDs + FSkill2IDs + FSkill3IDs + AffinityIDs
    AllNameValues = FSkill1Names + FSkill2Names + FSkill3Names + Blades
    AllUnlockKeyIDs = FSkill1UnlockKeyIDs + FSkill2UnlockKeyIDs + FSkill3UnlockKeyIDs + AffinityUnlockKeys
    for skillid in range(len(AllBladeIDs)):
        BladeInfoList.append(BladeInfo(AllNameValues[skillid], AllBladeIDs[skillid], AllUnlockKeyIDs[skillid]))
    # PurposeIDs will get spat out in the following order: [AffinityRank1, FieldSkill1Rank1, FieldSkill2Rank1, FieldSkill3Rank1, AffinityRank2, ...]
    CurMaxPurposeID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestTaskAchievement.json", "$id") + 1
    CurMaxQuestListAchievementID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestListAchievement.json", "$id") + 1
    CurMaxQuestCollectID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestCollect.json", "$id") + 1
    CurMaxTaskLogID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_quest_achievement.json", "$id") + 1
    CurMaxFLDAchievementListID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_AchievementList.json", "$id") + 1
    FLDAchievementListNewRows, FLDQuestListAchievementNewRows, FLDQuestTaskAchievementNewRows, FLDQuestCollectNewRows, fldquestachievementtextfilenewrows = [], [], [], [], []
    with open("./XC2/_internal/JsonOutputs/common/FLD_AchievementSet.json", 'r+', encoding='utf-8') as file: # hook up the new questlistachievementid to the "Task" column
        data = json.load(file)
        for blade in BladeInfoList:
            for row in data["rows"]:
                if row["$id"] == blade.fskillid:
                    CurRank = 0 # holds the current location of the skill unlock key in the blade.unlockkeyids property
                    for i in range(1,6):
                        if row[f"AchievementID{i}"] != 0:
                            row[f"AchievementID{i}"] = CurMaxFLDAchievementListID
                            if blade.fskillid in AffinityIDs and i == 1:
                                FLDAchievementListNewRows.append({"$id": CurMaxFLDAchievementListID, "Title": 0, "Category": 0, "Icon": 0, "Task": 0, "VoiceCategory": 0, "AfterVoice": 0, "Difficulty": 0, "IdeaCategory": 0, "IdeaValue": 0})
                            else:
                                FLDAchievementListNewRows.append({"$id": CurMaxFLDAchievementListID, "Title": 0, "Category": 0, "Icon": 0, "Task": CurMaxQuestListAchievementID, "VoiceCategory": 0, "AfterVoice": 0, "Difficulty": 0, "IdeaCategory": 0, "IdeaValue": 0})
                                FLDQuestListAchievementNewRows.append({"$id": CurMaxQuestListAchievementID, "QuestTitle": 0, "QuestCategory": 6, "Visible": 0, "Talker": 0, "Summary": 0, "ResultA": 5131, "ResultB": 0, "SortNo": 0, "RewardDisp": 0, "RewardSetA": 0, "RewardSetB": 0, "PRTQuestID": 0, "FlagPRT": 0, "FlagCLD": 0, "PurposeID": 0, "CountCancel": 0, "NextQuestA": CurMaxQuestListAchievementID + 1, "CallEventA": 0, "NextQuestB": 0, "CallEventB": 0, "HintsID": 0, "ClearVoice": 0, "AutoStart": 0, "ItemLost": 0, "CancelCondition": 0, "QuestIcon": 0, "LinkedQuestID": 0})
                                FLDQuestListAchievementNewRows.append({"$id": CurMaxQuestListAchievementID + 1, "QuestTitle": 0, "QuestCategory": 6, "Visible": 0, "Talker": 0, "Summary": 0, "ResultA": 0, "ResultB": 0, "SortNo": 0, "RewardDisp": 0, "RewardSetA": 0, "RewardSetB": 0, "PRTQuestID": CurMaxQuestListAchievementID, "FlagPRT": 0, "FlagCLD": 0, "PurposeID": CurMaxPurposeID, "CountCancel": 0, "NextQuestA": 30000, "CallEventA": 0, "NextQuestB": 0, "CallEventB": 0, "HintsID": 0, "ClearVoice": 0, "AutoStart": 0, "ItemLost": 0, "CancelCondition": 0, "QuestIcon": 0, "LinkedQuestID": 0})
                                FLDQuestTaskAchievementNewRows.append({"$id": CurMaxPurposeID, "PreCondition": 0, "TaskType1": 3, "TaskID1": CurMaxQuestCollectID, "Branch1": 0, "TaskLog1": CurMaxTaskLogID, "TaskUI1": 0, "TaskCondition1": 0, "TaskType2": 0, "TaskID2": 0, "Branch2": 0, "TaskLog2": 0, "TaskUI2": 0, "TaskCondition2": 0, "TaskType3": 0, "TaskID3": 0, "Branch3": 0, "TaskLog3": 0, "TaskUI3": 0, "TaskCondition3": 0, "TaskType4": 0, "TaskID4": 0, "Branch4": 0, "TaskLog4": 0, "TaskUI4": 0, "TaskCondition4": 0})
                                FLDQuestCollectNewRows.append({"$id": CurMaxQuestCollectID, "Refer": 4, "ItemID": blade.unlockkeyids[CurRank], "Category": 0, "Count": 1, "Deduct": 0, "TresureID": 0, "EnemyID": 0, "MapID": 0, "NpcID": 0, "CollectionID": 0})
                                fldquestachievementtextfilenewrows.append({"$id": CurMaxTaskLogID, "style": 62, "name": "Unlocked by the respective unlock key\nitem found in locations across Alrest."})
                                CurMaxQuestListAchievementID += 2
                                CurMaxPurposeID += 1
                                CurMaxQuestCollectID += 1
                                CurMaxTaskLogID += 1
                                CurRank += 1
                            CurMaxFLDAchievementListID += 1
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    JSONParser.ExtendJSONFile("common/FLD_AchievementList.json", [FLDAchievementListNewRows])
    JSONParser.ExtendJSONFile("common/FLD_QuestListAchievement.json", [FLDQuestListAchievementNewRows])
    JSONParser.ExtendJSONFile("common/FLD_QuestTaskAchievement.json", [FLDQuestTaskAchievementNewRows])
    JSONParser.ExtendJSONFile("common/FLD_QuestCollect.json", [FLDQuestCollectNewRows])
    JSONParser.ExtendJSONFile("common_ms/fld_quest_achievement.json", [fldquestachievementtextfilenewrows])
    RegularNodeSetup()

def RegularNodeSetup(): # split for readability, this basically makes all non-field skill and non-affinity rank blade tree unlocks get unlocked when the corresponding blade affinity rank is unlocked.
    RegularNodeIDs = [1680, 1681, 1682, 1683, 1684, 1685, 1690, 1691, 1692, 1693, 1694, 1695, 1700, 1701, 1702, 1703, 1704, 1705, 1710, 1711, 1712, 1713, 1714, 1715, 1720, 1721, 1722, 1723, 1724, 1725, 1730, 1731, 1732, 1733, 1734, 1735]
    with open("./XC2/_internal/JsonOutputs/common/FLD_AchievementSet.json", 'r+', encoding='utf-8') as file: # now we need to modify corresponding set ids
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RegularNodeIDs:
                for j in range(1, 6):
                    if (row[f"AchievementID{j}"] != 0):
                        row[f"AchievementID{j}"] = 16
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_Achievement.json", 'r+', encoding='utf-8') as file: #we need to change FLD_Achievement ID 1 to walk 1 step total
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 1:
                    row["StatsID"] = 60
                    row["Count"] = 1
                    row["DebugName"] = "WALK_TOTAL"
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestTaskAchievement.json", 'r+', encoding='utf-8') as file: #now we need to modify the FLD_QuestTaskAchievement
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 7005:
                row["TaskType1"] = 12
                row["TaskID1"] = 1
                row["TaskCondition1"] = 0
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common_ms/fld_quest_achievement.json", 'r+', encoding='utf-8') as file: #modifying the text files that describe what you need to do to unlock the node
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 663:
                row["name"] = "Unlocked once you unlock the \n corresponding Trust Level."
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CampfireUnlocks(): # adds conditions to the campfire unlocks
    CurMaxFLDConditionListID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    CurMaxFLDConditionItemID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionItem.json", "$id") + 1
    StartingFLDConditionListID = CurMaxFLDConditionListID
    #Helper.MathmaticalColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/FLD_CampPop.json", ["ConditionID"], ['row["$id"] + 25589'])
    AllCampsiteKeys = Helper.MultiLevelListToSingleLevelList([HHC_Key, LC_Key, CLC_Key, HWC_Key, PVC_Key, FVC_Key, AGC_Key, OTC_Key, DDC_Key, HGC_Key])
    NewFLDConditionListRows, NewFLDConditionItemRows = [], []
    for key in AllCampsiteKeys:
        if key == PVC_Key[0]: # if we access the camp without the means to create the recipe, you get softlocked.
            NewFLDConditionListRows.append({"$id": CurMaxFLDConditionListID, "Premise": 0, "ConditionType1": 5, "Condition1": CurMaxFLDConditionItemID, "ConditionType2": 2, "Condition2": 862, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        else:
            NewFLDConditionListRows.append({"$id": CurMaxFLDConditionListID, "Premise": 0, "ConditionType1": 5, "Condition1": CurMaxFLDConditionItemID, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        NewFLDConditionItemRows.append({"$id": CurMaxFLDConditionItemID, "ItemCategory": 0, "ItemID": key, "Number": 1})
        CurMaxFLDConditionListID += 1
        CurMaxFLDConditionItemID += 1
    JSONParser.ExtendJSONFile("common/FLD_ConditionList.json", [NewFLDConditionListRows])
    JSONParser.ExtendJSONFile("common/FLD_ConditionItem.json", [NewFLDConditionItemRows])
    with open("./XC2/_internal/JsonOutputs/common_gmk/FLD_CampPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row["ConditionID"] = StartingFLDConditionListID + row["$id"] - 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CharacterUnlocks(): # sets up the character unlock keys
    # FLD_QuestTaskIra row 5 should have 3 additional Tasks, of type Collect (3), that mention each individual extra key, AddamKey, MythraKey, HazeKey
    # FLD_QuestTaskIra row 12 should have 3 additional Tasks, of type Collect (3), that mention each individual extra key, HugoKey, BrighidKey, AegaeonKey
    # FLD_QuestTaskIra row 25 should have 1 additional Task, of type Collect (3), that mentions the extra key, MinothKey
    AllCharUnlockKeys = Helper.MultiLevelListToSingleLevelList([AddamKey, MythraKey, HazeKey, HugoKey, BrighidKey, AegaeonKey, MinothKey])
    KeyNames = ["Addam", "Mythra", "Haze", "Hugo", "Brighid", "Aegaeon", "Minoth"]
    FLDQuestCollectNewRows, fldquestnewrows = [], []
    CurMaxFLDQuestCollectID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_QuestCollect.json", "$id") + 1
    CurMaxfldquestid = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_quest.json", "$id") + 1
    CurKeyCount = 0
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestTaskIra.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case 5 | 12:
                    for i in range(2, 5):
                        row[f"TaskType{i}"] = 3
                        row[f"TaskID{i}"] = CurMaxFLDQuestCollectID
                        row[f"TaskLog{i}"] = CurMaxfldquestid
                        FLDQuestCollectNewRows.append({"$id": CurMaxFLDQuestCollectID, "Refer": 4, "ItemID": AllCharUnlockKeys[CurKeyCount], "Category": 0, "Count": 1, "Deduct": 0, "TresureID": 0, "EnemyID": 0, "MapID": 0, "NpcID": 0, "CollectionID": 0})
                        fldquestnewrows.append({"$id": CurMaxfldquestid, "style": 62, "name": f"Obtain the {KeyNames[CurKeyCount]} unlock key\nfound in progression locations across Alrest."})
                        CurKeyCount += 1
                        CurMaxFLDQuestCollectID += 1
                        CurMaxfldquestid += 1
                case 25:
                    row["TaskType2"] = 3
                    row["TaskID2"] = CurMaxFLDQuestCollectID
                    row["TaskLog2"] = CurMaxfldquestid
                    FLDQuestCollectNewRows.append({"$id": CurMaxFLDQuestCollectID, "Refer": 4, "ItemID": AllCharUnlockKeys[CurKeyCount], "Category": 0, "Count": 1, "Deduct": 0, "TresureID": 0, "EnemyID": 0, "MapID": 0, "NpcID": 0, "CollectionID": 0})
                    fldquestnewrows.append({"$id": CurMaxfldquestid, "style": 62, "name": f"Obtain the {KeyNames[CurKeyCount]} unlock key\nfound in progression locations across Alrest."})
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/CHR_Dr.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] > 17:
                row["DefLvType"] = 2
                row["DefLv"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    JSONParser.ExtendJSONFile("common/FLD_QuestCollect.json", [FLDQuestCollectNewRows])
    JSONParser.ExtendJSONFile("common_ms/fld_quest.json", [fldquestnewrows])

def ChangeReqItemRarities(): # we want the useful items that get dropped from chests and enemies to have a golden glow, so that people know to pick them up.
    RequiredItems = KeyItemtoLocDict.keys()
    MinWeaponChipID = Helper.GetMinValue("./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json", "$id") # should be 10001, but just in case
    MaxWeaponChipID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json", "$id")
    MinCollectionMatID = Helper.GetMinValue("./XC2/_internal/JsonOutputs/common/ITM_CollectionList.json", "$id") # should be 30001
    MaxCollectionMatID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/ITM_CollectionList.json", "$id")
    MinPreciousMainID = Helper.GetMinValue("./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", "$id") # should be 25001
    MaxPreciousMainID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", "$id")
    MinPreciousTornaID = Helper.GetMinValue("./XC2/_internal/JsonOutputs/common/ITM_PreciousListIra.json", "$id") # should be 25001
    MaxPreciousTornaID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/ITM_PreciousListIra.json", "$id")
    MinInfoID = Helper.GetMinValue("./XC2/_internal/JsonOutputs/common/ITM_InfoList.json", "$id") # should be 25501
    MaxInfoID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/ITM_InfoList.json", "$id")
    WeaponChipIDRange = Helper.InclRange(MinWeaponChipID, MaxWeaponChipID)
    CollectionMatIDRange = Helper.InclRange(MinCollectionMatID, MaxCollectionMatID)
    PreciousMainIDRange = Helper.InclRange(MinPreciousMainID, MaxPreciousMainID)
    PreciousTornaIDRange = Helper.InclRange(MinPreciousTornaID, MaxPreciousTornaID)
    InfoIDRange = Helper.InclRange(MinInfoID, MaxInfoID)
    WeaponChipRegularIDs, CollectionMatRegularIDs, PreciousRegularMainIDs, PreciousRegularTornaIDs, InfoRegularIDs = [], [], [], [], []
    WeaponChipTextIDs, CollectionMatTextIDs, PreciousMainTextIDs, PreciousTornaTextIDs, InfoTextIDs = [], [], [], [], []
    AllRegularIDs = [WeaponChipRegularIDs, CollectionMatRegularIDs, PreciousRegularMainIDs, PreciousRegularTornaIDs, InfoRegularIDs]
    AllTextIDs = [WeaponChipTextIDs, CollectionMatTextIDs, PreciousMainTextIDs, PreciousTornaTextIDs, InfoTextIDs]
    AllRegularTargetFiles = ["./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json", "./XC2/_internal/JsonOutputs/common/ITM_CollectionList.json", "./XC2/_internal/JsonOutputs/common/ITM_PreciousList.json", "./XC2/_internal/JsonOutputs/common/ITM_PreciousListIra.json", "./XC2/_internal/JsonOutputs/common/ITM_InfoList.json"]
    AllTextTargetFiles = ["./XC2/_internal/JsonOutputs/common_ms/itm_pcwpnchip_ms.json", "./XC2/_internal/JsonOutputs/common_ms/itm_collection.json", "./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "./XC2/_internal/JsonOutputs/common_ms/itm_info.json"]

    for item in RequiredItems:
        if item in WeaponChipIDRange:
            WeaponChipRegularIDs.append(item)
        elif item in CollectionMatIDRange:
            CollectionMatRegularIDs.append(item)
        elif item in PreciousMainIDRange:
            PreciousRegularMainIDs.append(item)
        elif item in PreciousTornaIDRange:
            PreciousRegularTornaIDs.append(item)
        elif item in InfoIDRange:
            InfoRegularIDs.append(item)

    for file in ["./XC2/_internal/JsonOutputs/common/ITM_BoosterList.json", "./XC2/_internal/JsonOutputs/common/ITM_CollectionList.json", "./XC2/_internal/JsonOutputs/common/ITM_CrystalList.json", "./XC2/_internal/JsonOutputs/common/ITM_FavoriteList.json", "./XC2/_internal/JsonOutputs/common/ITM_Orb.json",  "./XC2/_internal/JsonOutputs/common/ITM_OrbEquip.json",  "./XC2/_internal/JsonOutputs/common/ITM_OrbRecipe.json", "./XC2/_internal/JsonOutputs/common/ITM_PcEquip.json", "./XC2/_internal/JsonOutputs/common/ITM_PcWpnChip.json",  "./XC2/_internal/JsonOutputs/common/ITM_SalvageList.json",  "./XC2/_internal/JsonOutputs/common/ITM_TresureList.json"]:
        Helper.ColumnAdjust(file, ["Rarity"], 1)

    for reqitemtype in range(len(AllRegularIDs)):
        if reqitemtype < 2:
            with open(AllRegularTargetFiles[reqitemtype], 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    if row["$id"] in AllRegularIDs[reqitemtype]:
                        row["Rarity"] = 2 # this row is the only reason I need to check the reqitem type. Computationally fastest to put it here, but does require repeating most of the code again below.
                        AllTextIDs[reqitemtype].append(row["Name"])
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            with open(AllRegularTargetFiles[reqitemtype], 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    if row["$id"] in AllRegularIDs[reqitemtype]:
                        AllTextIDs[reqitemtype].append(row["Name"])
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)
        with open(AllTextTargetFiles[reqitemtype], 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] in AllTextIDs[reqitemtype]:
                    row["name"] = f"[System:Color name=tutorial]{row["name"]}[/System:Color]"
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    
    _WeaponChips.ChangeWeaponRankNames() # we want to make the weapon chip names have their ranks too

def GildedCheckNames():
    # current problems:
    # cannot change anything about the red bag items in the field, they display no text, and I'm not sure where their model info is in the bdats, or if it even exists. probably tied to the map itself?
    RequiredItems = KeyItemtoLocDict.keys()
    RequiredLocations = list(KeyItemtoLocDict.values())
    RequiredCollectionPoints = [x.collectiontableid for x in RequiredLocations if x.type in ["tornacollectionpoint", "gormottcollectionpoint"]]
    RequiredChestIDs = [x.id for x in RequiredLocations if x.type == "chest"]
    RequiredEnemies = [x.id for x in RequiredLocations if x.type in ["normalenemy", "uniquemonster", "boss", "questenemy"]]
    RequiredMisc = [x.name for x in RequiredLocations if x.type == "misc"]
    RequiredShops = [x.shoplistid for x in RequiredLocations if x.type == "shop"]
    RequiredQuests = [x.rewardids[0] for x in RequiredLocations + ChosenLevel2Quests + ChosenLevel4Quests if x.type == "sidequest" and x.rewardids != []]
    CurGmkNameMax = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_gmkname.json", "$id")
    ProgressID = CurGmkNameMax + 1
    NonProgressID = CurGmkNameMax + 2
    NewGmkNameRows = [{"$id": ProgressID, "style": 36, "name": "[System:Color name=tutorial ]Progression[/System:Color]"}, {"$id": NonProgressID, "style": 36, "name": "[System:Color name=red ]Unrequired[/System:Color]"}]
    JSONParser.ExtendJSONFile("common_ms/fld_gmkname.json", [NewGmkNameRows])

    # collection points
    with open("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RequiredCollectionPoints:
                row["categoryName"] = ProgressID
            else:
                row["categoryName"] = NonProgressID
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_CollectionPopList.json", ["nameRadius"], 255) # makes it easier to see from far away
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_CollectionPopList.json", ["nameRadius"], 255) # makes it easier to see from far away

    # chests
    with open("./XC2/_internal/JsonOutputs/common/RSC_TboxList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            row["initWaitTimeRand"] = 0 # why would you add a random wait time before items start popping out??? get that out of here
            row["initWaitTime"] = 0
            match row["$id"]:
                case 10 | 3:
                    row["MSG_ID"] = ProgressID
                case 7 | 1:
                    row["MSG_ID"] = NonProgressID
                case _:
                    pass
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    ChestIDToUnearthFieldSkillID = {2205:1509, 2223:1549, 2243:1550, 2244:1551, 2257:1561, 2259:1552, 2260:1557, 2261:1554, 2263:1553, 2264:1562, 2324:1594, 2501:1497, 2502:1496, 2520:1577, 2523:1578, 2526:1580, 2540:1581, 2542:1583, 2544:1579, 2547:1582}
    AllUnearthIDs = [1509, 1549, 1550, 1551, 1561, 1552, 1557, 1554, 1553, 1562, 1594, 1497, 1496, 1577, 1578, 1580, 1581, 1583, 1579, 1582]
    RequiredUnearthIDs = [ChestIDToUnearthFieldSkillID[x] for x in RequiredChestIDs if x in AllUnearthIDs]

    FileList = ["./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_TboxPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_TboxPop.json"]
    for curfile in FileList:
        with open(curfile, 'r+', encoding='utf-8') as file: 
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] in RequiredChestIDs:
                    if row["RSC_ID"] in [7, 10]: # all barrels with progression get turned into a barrel of model type 10
                        row["RSC_ID"] = 10
                    else: # all chests with progression get turned into a chest of model type 3
                        row["RSC_ID"] = 3
                else:
                    if row["RSC_ID"] in [7, 10]: # all barrels without progression get turned into barrels of model type 7
                        row["RSC_ID"] = 7
                    else: # all chests without progression get turned into a chest of model type 1
                        row["RSC_ID"] = 1
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        Helper.ColumnAdjust(curfile, ["msgVisible", "msgdigVisible"], 255) # makes it easier to see from far away    
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_fieldskillplace.json", 'r+', encoding='utf-8') as file: # need to deal with the "Unearth" chest locations
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case 12:
                    row["name"] = "[System:Color name=tutorial]Unearth[/System:Color]"
                case 71:
                    row["name"] = "[System:Color name=red]Unearth[/System:Color]"
                case _:
                    pass
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    JSONParser.ChangeJSONLine(["common/FLD_FieldSkillSetting.json"], AllUnearthIDs, ["Name"], 71)
    if RequiredUnearthIDs != []:
        JSONParser.ChangeJSONLine(["common/FLD_FieldSkillSetting.json"], RequiredUnearthIDs, ["Name"], 12)

    # enemies
    # we're just going to turn the name yellow if it is required, red if not required, it's a bit more work than just setting the name to "Progression" or "Unrequired", but worth it
    RequiredEnemyNameList = []

    # first, we give enemies with duplicate names unique name ids.
    # we need to do this because they reuse enemy name ids for enemies with the same name but different chr_enarrange ids, so an unrequired cursed buloofo (id 1430) and a required cursed buloofo (id 1454) share the same name id, which screws up the whole concept. So we need to give them new name ids.
    MaxEnemyNameRow = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/fld_enemyname.json", "$id") + 1
    EnemiesWithDuplicateNames = [1436, 1442, 1444, 1446, 1447, 1448, 1450, 1454, 1526, 1606, 1632, 1633, 1651, 1653, 1655, 1656]
    DuplicateEnemyNames = ["Ardainian Scout", "Slithe Jagron", "Gargoyle", "Malos", "Malos", "Gort", "Artifice Siren", "Cursed Buloofo", "Dread Caterpile", "Urbs Armu", "Gargoyle", "Gargoyle", "Sable Volff", "Dormine Brog", "Grohl Plambus", "Chelta Caterpile"]
    AdditionalEnemyNameRows = []
    for enemy in range(len(DuplicateEnemyNames)):
        AdditionalEnemyNameRows.append({"$id": MaxEnemyNameRow + enemy, "style": 15, "name": DuplicateEnemyNames[enemy]})
    JSONParser.ExtendJSONFile("common_ms/fld_enemyname.json", [AdditionalEnemyNameRows])
    CurDupeEnemy = 0
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in EnemiesWithDuplicateNames:
                row["Name"] = MaxEnemyNameRow + CurDupeEnemy
                CurDupeEnemy += 1
            if row["$id"] in RequiredEnemies:
                RequiredEnemyNameList.append(row["Name"])
                row["Flag"]["mBoss"] = 1
            else:
                row["Flag"]["mBoss"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RequiredEnemyNameList:
                row["name"] = "[System:Color name=tutorial ]" + row["name"] + "[/System:Color]"
            else:
                row["name"] = "[System:Color name=red ]" + row["name"] + "[/System:Color]"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # misc
    # each of the misc ones has to be hardcoded, since the idea is that it is a rarely used bucket for a bunch of one-off checks.
    if 'Nameless Wanderpon Gift Item' in RequiredMisc:
        ReplacementName = "[System:Color name=tutorial ]Nameless Wanderpon[/System:Color]"
    else:
        ReplacementName = "[System:Color name=red ]Nameless Wanderpon[/System:Color]"
    JSONParser.ChangeJSONLine(["common_ms/fld_npcname.json"],[1258],["name"], ReplacementName)

    # shops
    # again, coloring the existing shop name yellow or red if it has progression or doesnt
    RequiredShopNameList = []
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RequiredShops:
                RequiredShopNameList.append(row["Name"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_shopname.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RequiredShopNameList:
                row["name"] = "[System:Color name=tutorial ]" + row["name"] + "[/System:Color]"
            elif row["$id"] >= 226:
                row["name"] = "[System:Color name=red ]" + row["name"] + "[/System:Color]"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # sidequests
    # yellow name if progression, red name if it doesn't
    RequiredSidequestNameList = []
    NonRequiredSidequestNameList = []
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestListNormalIra.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["RewardSetA"] in RequiredQuests:
                RequiredSidequestNameList.append(row["QuestTitle"])
            elif row["RewardSetA"] != 0 and row["QuestTitle"] != 0:
                NonRequiredSidequestNameList.append(row["QuestTitle"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common_ms/fld_quest_normal.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in RequiredSidequestNameList:
                row["name"] = "[System:Color name=tutorial ]" + row["name"] + "[/System:Color]"
            elif row["$id"] in NonRequiredSidequestNameList:
                row["name"] = "[System:Color name=red ]" + row["name"] + "[/System:Color]"
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    # needs to account for npc giver name probably. not sure how fully to implement this. are there npcs that give multiple quests? I guess those are separate instances.


def GenerateHints():
    global HintedItemText, HintedLocText, ItemHintNames, LocHintNames, LocHintCount, ItemHintCheckLoc, ItemHintCheckNear
    HintedItemText, HintedLocText, ItemHintNames, ItemHintCheckLoc, ItemHintCheckNear, LocHintNames, LocHintCount = [], [], [], [], [], [], []
    if Options.TornaAddHints_ItemHints.GetState():
        HintedItemKeys = random.sample(list(KeyItemtoLocDict.keys()), Options.TornaAddHints_ItemHints.GetSpinbox())
        for item in HintedItemKeys:
            match KeyItemtoLocDict[item].type:
                case "normalenemy" | "uniquemonster" | "boss" | "questenemy":
                    HintedItemText.append(f"{ItemIDtoItemName[item]} can be found by defeating {KeyItemtoLocDict[item].name} near {AreaIDtoNameDict[KeyItemtoLocDict[item].nearloc].name}.")
                case "sidequest":
                    HintedItemText.append(f"{ItemIDtoItemName[item]} can be found by completing \"{KeyItemtoLocDict[item].name}\".")
                case _:
                    HintedItemText.append(f"{ItemIDtoItemName[item]} can be found at {KeyItemtoLocDict[item].name} near {AreaIDtoNameDict[KeyItemtoLocDict[item].nearloc].name}.")
            ItemHintNames.append(f"{ItemIDtoItemName[item]}")
            ItemHintCheckLoc.append(f"{KeyItemtoLocDict[item].name}")
            try:
                ItemHintCheckNear.append(f"{AreaIDtoNameDict[KeyItemtoLocDict[item].nearloc].name}")
            except:
                ItemHintCheckNear.append("null")
    if Options.TornaAddHints_LocProgHints.GetState():
        HintedLocs = random.sample(list(AreaIDtoNameDict.keys()), Options.TornaAddHints_LocProgHints.GetSpinbox())
        for loc in HintedLocs:
            LocProgCount = 0
            for item in KeyItemtoLocDict.keys():
                if KeyItemtoLocDict[item].type != "sidequest":
                    if KeyItemtoLocDict[item].nearloc == loc:
                        LocProgCount += 1
            HintedLocText.append(f"There are {LocProgCount} required progression item(s) found near {AreaIDtoNameDict[loc].name}.")
            LocHintNames.append(f"{AreaIDtoNameDict[loc].name}")
            LocHintCount.append(f"{LocProgCount}")
    if HintedLocs != [] or HintedItemKeys != []:
        AddHintstoBdats()

def AddHintstoBdats():
    numitempages = math.ceil(len(HintedItemText) / 3)
    numlocpages = math.ceil(len(HintedLocText) / 3)
    CurMessage = 85
    CurHintedItemNum = 0 
    CurHintedLocNum = 0
    NewLineHintedItemTexts = HintedItemText.copy()
    NewLineHintedLocTexts = HintedLocText.copy()
    for hint in range(len(NewLineHintedItemTexts)): # adding newlines and yellow text to the hints.
        NewLineHintedItemTexts[hint] = NewLineHintedItemTexts[hint].replace(" found ", " found\n")
        NewLineHintedItemTexts[hint] = NewLineHintedItemTexts[hint].replace(" near ", " near\n")
        NewLineHintedItemTexts[hint] = NewLineHintedItemTexts[hint].replace(f"{ItemHintNames[hint]}", f"[System:Color name=tutorial ]{ItemHintNames[hint]}[/System:Color]")
        NewLineHintedItemTexts[hint] = NewLineHintedItemTexts[hint].replace(f"{ItemHintCheckLoc[hint]}", f"[System:Color name=tutorial ]{ItemHintCheckLoc[hint]}[/System:Color]")
        NewLineHintedItemTexts[hint] = NewLineHintedItemTexts[hint].replace(f"{ItemHintCheckNear[hint]}", f"[System:Color name=tutorial ]{ItemHintCheckNear[hint]}[/System:Color]")
    for hint in range(len(NewLineHintedLocTexts)):
        NewLineHintedLocTexts[hint] = NewLineHintedLocTexts[hint].replace(" near ", " near\n")
        NewLineHintedLocTexts[hint] = NewLineHintedLocTexts[hint].replace(f"{LocHintNames[hint]}", f"[System:Color name=tutorial ]{LocHintNames[hint]}[/System:Color]")
        NewLineHintedLocTexts[hint] = NewLineHintedLocTexts[hint].replace(f"{LocHintCount[hint]}", f"[System:Color name=tutorial ]{LocHintCount[hint]}[/System:Color]", 1) # replacing only the first instance accounts for areas like "Balaur, Dark Zone #1, if it were to have only 1 progressive item"
    
    with open("./XC2/_internal/JsonOutputs/common/MNU_Tutorial_Tips.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)

        with open("./XC2/_internal/JsonOutputs/common_ms/menu_tutorial_chbtl.json", 'r+', encoding='utf-8') as filet:
            datat = json.load(filet)
            
            rowscopy = [row for row in data["rows"] if row.get("$id") <= 99 + numitempages + numlocpages]
            data["rows"] = rowscopy
            
            for row in data["rows"]:
                row["page"] = row["$id"] - 99
                row["bg_type"] = 1
                for i in range(1, 4):
                    row[f"window_y{i}"] = -50 + 150*i
                    row[f"message{i}"] = 0
                
            for ipage in range(numitempages):
                for row in data["rows"]:
                    if row["$id"] == 100 + ipage:
                        CurRowTitle = row["title"]
                        for i in range(1, 4):
                            try:
                                row[f"message{i}"] = CurMessage
                                for rowt in datat["rows"]:
                                    if rowt["$id"] == CurRowTitle:
                                        rowt["name"] = f"Item Hints (Page {ipage + 1})"
                                    if rowt["$id"] == CurMessage:
                                        rowt["name"] = NewLineHintedItemTexts[CurHintedItemNum]
                                CurMessage += 1
                                CurHintedItemNum += 1
                            except:
                                row[f"message{i}"] = 0
                                break

            for lpage in range(numlocpages):
                for row in data["rows"]:
                    if row["$id"] == 100 + numitempages + lpage:
                        CurRowTitle = row["title"]
                        for i in range(1, 4):
                            try:
                                row[f"message{i}"] = CurMessage
                                for rowt in datat["rows"]:
                                    if rowt["$id"] == CurRowTitle:
                                        rowt["name"] = f"Location Hints (Page {lpage + 1})"
                                    if rowt["$id"] == CurMessage:
                                        rowt["name"] = NewLineHintedLocTexts[CurHintedLocNum]
                                CurMessage += 1
                                CurHintedLocNum += 1
                            except:
                                row[f"message{i}"] = 0
                                break

            filet.seek(0)
            filet.truncate()
            json.dump(datat, filet, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AddNewFlagPointers(GateCommReq, GateNumber): # if we reduce the required community level, we want to make a separate FLD_ConditionList row, with a different Condition1 value, to avoid screwing up any other events relying on that Flag Condition ()
    NewCondFlagRowID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_ConditionFlag.json","$id") + 1
    if GateNumber == 1:
        JSONParser.ChangeJSONLine(["common/FLD_ConditionList.json"], [2918], ["Condition1"], NewCondFlagRowID)
        JSONParser.ExtendJSONFile("common/FLD_ConditionFlag.json", [[{"$id": NewCondFlagRowID, "FlagType": 4, "FlagID": 652, "FlagMin": GateCommReq, "FlagMax": 6}]])
    else:
        JSONParser.ChangeJSONLine(["common/FLD_ConditionList.json"], [2919], ["Condition1"], NewCondFlagRowID)
        JSONParser.ExtendJSONFile("common/FLD_ConditionFlag.json", [[{"$id": NewCondFlagRowID, "FlagType": 4, "FlagID": 652, "FlagMin": GateCommReq, "FlagMax": 6}]])

def CreateSpoilerLog():
    IDstoAdd = []
    try: 
        if HintedItemText != []:
            pass
    except:
        HintedItemText = []
    try: 
        if HintedLocText != []:
            pass
    except:
        HintedLocText = []
    DesiredSpoilerLogDirectory = os.path.dirname(fileEntryVar.get()) + "/Torna_Spoiler_Logs"
    if not os.path.exists(DesiredSpoilerLogDirectory):
        os.makedirs(DesiredSpoilerLogDirectory)
    DesiredSpoilerLogLocation = os.path.dirname(fileEntryVar.get()) + f"/Torna_Spoiler_Logs/{seedEntryVar.get()}.txt"
    if not os.path.exists(DesiredSpoilerLogLocation):
        with open(DesiredSpoilerLogLocation, "w", encoding= "utf-8") as debugfile:
            pass
    debugfile = open(DesiredSpoilerLogLocation, "w", encoding= "utf-8")
    debugfile.write(f"Xenoblade 2 Randomizer Version {Version}\n\n")
    debugfile.write(f"Permalink: {permalinkVar.get()}\n\n")
    debugfile.write(f"Seed Name: {seedEntryVar.get()}\n\n")
    debugfile.write("Options Selected:\n")
    for option in OptionList: # for each option
        OptionName = option.name   
        OptionVal = option.GetState()
        if OptionVal: # if the option is checked
            if option.hasSpinBox:
                OptionOdds = option.GetSpinbox()
                debugfile.write(f" {OptionName}: {OptionOdds};")
            else:
                debugfile.write(f" {OptionName};")
    debugfile.write("\n\n")
    debugfile.write("Suboptions Selected:\n")
    for option in OptionList:
        OptionName = option.name
        OptionVal = option.GetState()
        if OptionVal:
            for subOption in option.subOptions: # looping through all suboptions
                SubOptionName = subOption.name
                SubOptionVal = subOption.GetState()
                if SubOptionVal: # if the suboption is a checkbox and checked
                    if subOption.hasSpinBox:
                        subOptionOdds = subOption.GetSpinbox()
                        debugfile.write(f" {OptionName}: {SubOptionName}: [{subOptionOdds}];")
                    else:
                        debugfile.write(f" {OptionName}: {SubOptionName};")
    debugfile.write("\n")   
    debugfile.close()
    debugfileread = open(DesiredSpoilerLogLocation, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines[7] = alllines[7][1:]
    alllines[7] = alllines[7][:-2]
    alllines[7] += "\n"
    alllines[10] = alllines[10][1:]
    alllines[10] = alllines[10][:-2]
    alllines[10] += "\n"
    debugfilewrite = open(DesiredSpoilerLogLocation, "w", encoding= "utf-8")
    debugfilewrite.writelines(alllines)
    debugfilewrite.close()
    debugfileread = open(DesiredSpoilerLogLocation, "r", encoding= "utf-8")
    alllines = debugfileread.readlines()
    alllines.append("\n")
    if HintedItemText != [] or HintedLocText != []:
        alllines.append("Hints:")
        alllines.append("\n\n")
        if HintedItemText != []:
            alllines.append("     Item Hints:\n\n")
            for hint in HintedItemText:
                alllines.append(f"          {hint}\n")
            alllines.append("\n")
        if HintedLocText != []:
            alllines.append("     Location Progression Count Hints:\n\n")
            for hint in HintedLocText:
                alllines.append(f"          {hint}\n")
            alllines.append("\n")
        alllines.append("\n")
    alllines.append("Chosen Required Quests and NPC Conversations by Community Level Requirement:\n")
    alllines.append("\n")
    QuestListByCommReq = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for sq in ChosenLevel4Quests:
        QuestListByCommReq[sq.comreq].append(sq)
    for commlevel in range(0, 6):
        if commlevel == 0:
            alllines.append(f"     No Community Level Requirement:\n\n")
        else:
            alllines.append(f"     Community Level {commlevel} Required:\n\n")
        for quest in QuestListByCommReq[commlevel]:
            alllines.append(f"          {quest.name}\n")
        alllines.append("\n")
    alllines.append("\n")
    alllines.append("Logical Playthrough:\n")
    alllines.append("\n")
    #StoryStepList = []
    for MQ in range(len(Mainquests)):
        alllines.append(f"     Step {Mainquests[MQ].id}: {Mainquests[MQ].summary}\n")
        alllines.append("\n")
        CurStepLocList = []
        if MQ != 0:
            NewStepReqs = [item for item in Mainquests[MQ].itemreqs if item not in Mainquests[MQ - 1].itemreqs]
            for item in NewStepReqs:
                CurStepLocList.append(KeyItemtoLocDict.get(item))
            CurStepLocList = list(set(CurStepLocList))
            
            # logic for determining sphere in step
            SpheretoLoc = {}
            NonSphere0s = []
            CurStepLocListCopy = copy.deepcopy(CurStepLocList)
            LoctoLocCopy = {}
            for index in range(len(CurStepLocList)):
                LoctoLocCopy[CurStepLocListCopy[index]] = CurStepLocList[index] # this ties the old and new locs together
            for loc in CurStepLocListCopy:
                for item in NewStepReqs:
                    if item in loc.itemreqs: # if this location requires an item that was logically added this step, it can't be sphere 0 for the step
                        NonSphere0s.append(loc)
                        break
            Sphere0s = [loc for loc in CurStepLocListCopy if loc not in NonSphere0s]
            CurrSphere0Items = list(set(Helper.MultiLevelListToSingleLevelList([loc.randomizeditems for loc in Sphere0s])))
            CurrSphere0Items = [item for item in CurrSphere0Items if item in NewStepReqs]
            SpheretoLoc[0] = []
            CurrSphere = 0
            for loc in Sphere0s:
                SpheretoLoc[0].append(LoctoLocCopy[loc])
            CurStepLocListCopy = [loc for loc in CurStepLocListCopy if loc not in Sphere0s]
            while sum(len(item) for item in SpheretoLoc.values()) < len(CurStepLocList):
                if LastSphereItems == False: # if LastSphereItems is False, it has to be the first loop, so we do some setup
                    CurrSphere = 1
                    for loc in CurStepLocListCopy:
                        loc.itemreqs = [item for item in loc.itemreqs if item in NewStepReqs and item not in CurrSphere0Items]
                    LastSphereItems = CurrSphere0Items
                    LastSphereLocs = Sphere0s
                else:
                    CurrSphereItems = list(set([item for item in CurrSphereItems if item in NewStepReqs]))
                    LastSphereItems = CurrSphereItems
                    LastSphereLocs = CurrSphereLocs
                    CurStepLocListCopy = [loc for loc in CurStepLocListCopy if loc not in LastSphereLocs]
                    for loc in CurStepLocListCopy:
                        loc.itemreqs = [item for item in loc.itemreqs if item in NewStepReqs and item not in LastSphereItems] # basically removing the previous sphere's item requirements from the remaining locations
                    CurrSphere += 1
                CurrSphereLocs = []
                CurrSphereItems = []
                SpheretoLoc[CurrSphere] = []
                for loc in CurStepLocListCopy:
                    if loc.itemreqs == []:
                        CurrSphereLocs.append(loc)
                        SpheretoLoc[CurrSphere].append(LoctoLocCopy[loc])
                    CurrSphereItems.extend(loc.randomizeditems)
            if SpheretoLoc[CurrSphere] == []:
                del SpheretoLoc[CurrSphere]
            LastSphereItems = False

            if CurStepLocList != []:
                for sphere in range(0, max(SpheretoLoc.keys()) + 1):
                    alllines.append(f"          Sphere {sphere}:\n\n")                
                    for loc in CurStepLocList:
                        if loc in SpheretoLoc[sphere]:
                            if loc.type != "sidequest":
                                alllines.append(f"               {AreaIDtoNameDict[loc.nearloc].name}: {loc.name} (Story Step {loc.mainreq})\n")
                                #StoryStepList.append(loc.mainreq)
                            else:
                                alllines.append(f"               Sidequest: {loc.name} (Story Step {loc.mainreq})\n")
                            for reward in range(len(loc.randomizeditems)):
                                if loc.randomizeditems[reward] in NewStepReqs:
                                    alllines.append(f"                    Item {reward + 1}: {ItemIDtoItemName.get(loc.randomizeditems[reward])}\n")
                            alllines.append("\n")
    alllines.append("\n")
    alllines.append("Items per Check (by Category):\n")
    alllines.append("\n")
    alllines.append(f"     {LocTypetoSpoilerLogHeader[AllLocations[0].type]}:")
    alllines.append("\n\n")
    for loc in range(len(AllLocations)):
        CurLocType = LocTypetoSpoilerLogHeader[AllLocations[loc].type]
        if loc != 0 and CurLocType != LocTypetoSpoilerLogHeader[AllLocations[loc - 1].type]:
            alllines.append("\n")
            alllines.append(f"     {LocTypetoSpoilerLogHeader[AllLocations[loc].type]}:")
            alllines.append("\n")
            alllines.append("\n")
        alllines.append(f"          {AllLocations[loc].name}:\n")
        for reward in range(len(AllLocations[loc].randomizeditems)):
            if ItemIDtoItemName.get(AllLocations[loc].randomizeditems[reward]) == None and AllLocations[loc].randomizeditems[reward] != 0:
                IDstoAdd.append(AllLocations[loc].randomizeditems[reward])
            alllines.append(f"               Item {reward + 1}: {ItemIDtoItemName.get(AllLocations[loc].randomizeditems[reward])}\n")
    alllines.append("\n\n")
    alllines.append("Items per Check (by Location (Excludes Sidequests!)):\n\n")
    for loc in AreaIDtoNameDict.keys():
        alllines.append(f"     {AreaIDtoNameDict[loc].name}\n\n")
        for check in range(len(AllLocations)):
            if AllLocations[check].type != "sidequest":
                if AllLocations[check].nearloc == loc:
                    alllines.append(f"          {AllLocations[check].name}:\n")
                    for reward in range(len(AllLocations[check].randomizeditems)):
                        if ItemIDtoItemName.get(AllLocations[check].randomizeditems[reward]) == None and AllLocations[check].randomizeditems[reward] != 0:
                            IDstoAdd.append(AllLocations[check].randomizeditems[reward])
                        alllines.append(f"               Item {reward + 1}: {ItemIDtoItemName.get(AllLocations[check].randomizeditems[reward])}\n")
        alllines.append("\n")
    alllines.append("\n\n")
    debugfilewrite = open(DesiredSpoilerLogLocation, "w", encoding= "utf-8")
    debugfilewrite.writelines(alllines)
    debugfilewrite.close()
    #IDstoAdd = list(set(IDstoAdd))
    #print(IDstoAdd)
    #print(f"Average Story Step: {round(sum(StoryStepList)/len(StoryStepList), 2)}")

    
def TornaMainDescription():
    TornaMainDesc = PopupDescriptions.Description()
    TornaMainDesc.Header("Option Description")
    TornaMainDesc.Text(r"Randomizes the Torna DLC, in a logic-based method, requiring Progression Items to be found at Checks to progress in the story. For  When enabled, each of the following Categories of Checks can have Progression Items. ")
    TornaMainDesc.Tag("Definitions")
    TornaMainDesc.Text(r"Category: A group of Checks. Usually this refers to all Checks of a specific type, like 'Treasure Chests' or 'Quest Rewards'.")
    TornaMainDesc.Text(r"Check: Each individual spot in-game where items can be found, i.e. a specific Treasure Chest, or a specific Enemy's drops.")
    TornaMainDesc.Text(r"Progression Item: An in-game item that is required to beat the main story.")
    TornaMainDesc.Header("Suboptions")
    TornaMainDesc.Tag("Collection Points")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by interacting with Collection Points. Each Collection Point can have a maximum number of Progression Items placed there equal to the number in the Spinbox.")
    TornaMainDesc.Tag("Enemy Drops")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by defeating Enemies. Each Enemy can have a maximum number of Progression Items placed there equal to the number in the Spinbox. Quest Enemies will never have Progression Items due to the possibility of some of them being permanently missable.")
    TornaMainDesc.Tag("Ground Items")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by running into Ground Item spots on the ground. Each Ground Item can only have 1 item inside it.")
    TornaMainDesc.Image("httpswwwxenoserieswikiorgwikiFileDawning_Slate_Piece_Locationjpg.jpg", "XC2", 700)
    TornaMainDesc.Tag("Shops")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by purchasing items from Shops and Traveling Bards, and by receiving the gift item from the Nameless Wanderpon. Each Shop Check (excluding the Nameless Wanderpon) can have a maximum number of Progression Items placed there equal to the number in the Spinbox. The Nameless Wanderpon only gives 1 item when talked to.")
    TornaMainDesc.Tag("Side Quests")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by completing Side Quests. Each Side Quest can have a maximum number of Progression Items placed there equal to the number in the Spinbox.")
    TornaMainDesc.Tag("Treasure Chests")
    TornaMainDesc.Text(r"If enabled, Progression Items can be found by opening Treasure Chests. Each Treasure Chest can have a maximum number of Progression Items placed there equal to the number in the Spinbox.")
    return TornaMainDesc

def TornaHintDescription():
    TornaHintDesc = PopupDescriptions.Description()
    TornaHintDesc.Header("Item Hints")
    TornaHintDesc.Text("Item Hints are hints that tell the player at which Check a specific Progression Item can be found.")
    TornaHintDesc.Image("Torna_Item_Hints.png", "XC2", 700)
    TornaHintDesc.Header("Location Hints")
    TornaHintDesc.Text("Location Hints are hints that tell the player exactly how many Progression Items can be found in Checks around the Location listed.")
    TornaHintDesc.Image("Torna_Location_Hints.png", "XC2", 700)
    return TornaHintDesc

def TornaCCMCDescription():
    TornaCCMCDesc = PopupDescriptions.Description()
    TornaCCMCDesc.Header("Explanation")
    TornaCCMCDesc.Text("If this setting is enabled, all Progression Items will be of yellow rarity. The check that each Progression Item is located at will also have yellow names, in some capacity. In the case of Ground Item Checks, the bag they would normally spawn in will not show up. All enemies with Progression Items will also have a special icon above their heads. All Non-Progression Items will be of red rarity and the checks they are located at will have red names, unless there is a Progression Item there as well.")
    TornaCCMCDesc.Image("object type matches contents.png", "XC2", 700)
    TornaCCMCDesc.Tag("Progression Enemy Tag")
    TornaCCMCDesc.Image("special enemy tag.png", "XC2", 700)
    return TornaCCMCDesc

def TornaStoryReqChangeDescription():
    TornaStoryDesc = PopupDescriptions.Description()
    TornaStoryDesc.Header("Suboptions")
    TornaStoryDesc.Tag("Community Gate 1 Required Level")
    TornaStoryDesc.Text("When enabled, changes the community level requirement that prevents you from talking with the Tornan King for the first time.")
    TornaStoryDesc.Tag("Community Gate 2 Required Level")
    TornaStoryDesc.Text("When enabled, changes the community level requirement that prevents you from heading out to the Titan's Interior.")
    return TornaStoryDesc