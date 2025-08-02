# Gems, Skills, Arts, Accessories, Archsage Gauntlet ↓

import json, random
from scripts import Helper

# Lists to be populated during randomization
EnhancementsList = Helper.RandomGroup()
ArtsEnhancementList = Helper.RandomGroup()
AccessoryEnhancementList = Helper.RandomGroup()
SkillEnhancementList = Helper.RandomGroup()
GemEnhancementsList = Helper.RandomGroup()

Normal = [10,100]

# Used for skills to choose icons for 
M = 0 #Mixed/Misc
A = 1 #atk
H = 2 #healer
D = 3 #defender

low = 0 
high = 0
defaultSkillIcon = -1

class Enhancement:
    def __init__(self, name, effID, captionID, field3E70C175, roleType = M, param1 = [low,high], param2 = [low,high], skillIcon = defaultSkillIcon, isArts = True, isGem = True, isAccessory = True):
        self.name = name
        self.effID = effID
        self.captionID = captionID
        self.field3E70C175 = field3E70C175
        self.param1 = param1
        self.param2 = param2
        self.roleType = roleType
        self.skillIcon = skillIcon
        if isArts:
            ArtsEnhancementList.AddNewData(self)
        if isAccessory:
            AccessoryEnhancementList.AddNewData(self)
        if skillIcon != defaultSkillIcon:
            SkillEnhancementList.AddNewData(self)
        if isGem:
            GemEnhancementsList.AddNewData(self)
        EnhancementsList.AddNewData(self)
    
    def CreateEffect(self, BTL_EnhanceData, overrideParam1 = None, overrideParam2 = None, powerPercent = 0.5):
        if overrideParam1 == None:
            param1 = self.param1
        else:
            param1 = overrideParam1
        if overrideParam2 == None:
            param2 = self.param2
        else:
            param2 = overrideParam2 
        
        '''Returns the new Enhancements ID'''
        newID = len(BTL_EnhanceData["rows"])+1
        newEffect = {
        "$id": newID,
        "ID": f"{newID}",
        "EnhanceEffect": self.effID,
        "Param1": self.CalculatePower(param1, powerPercent),
        "Param2": self.CalculatePower(param2, powerPercent),
        "Caption": self.captionID,
        "DebugName": "",
        "AcceSetCheck": self.effID,
        "<3E70C175>": self.field3E70C175
        }
        BTL_EnhanceData["rows"].append(newEffect)  
        return newID    

    def CalculatePower(self, param, power):
        '''Calculates the power of the parameter from its low to high value'''
        if param[0] > param[-1]:
            min = param[-1]
            max = param[0]
            power = 1-power # Reverse the power if the parameters are reversed
        else:
            min = param[0]
            max = param[-1]
            
        diff = max - min
        chosen = min + (diff*power)
        newParam = chosen
        return int(newParam)
    
# with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
#     with open(f"XC3/JsonOutputs/btl/BTL_EnhanceEff.json", 'r+', encoding='utf-8') as enhanceEffFile:
#         with open(f"XC3/JsonOutputs/battle/msg_btl_enhance_cap.json", 'r+', encoding='utf-8') as captionFile:
#             with open(f"XC3/JsonOutputs/battle/msg_btl_enhance_name.json", 'r+', encoding='utf-8') as nameFile:
#                 enhanceData = json.load(enhanceFile)
#                 enhanceEffData = json.load(enhanceEffFile)
#                 captionData = json.load(captionFile)
#                 nameData = json.load(nameFile)
#                 TestList = []
#                 PreviousEffects = [0]
#                 for enh in enhanceData["rows"]:
#                     if enh["EnhanceEffect"] not in PreviousEffects:
#                         TestList.append(enh)
#                         PreviousEffects.append(enh["EnhanceEffect"])
#                         for enhEff in enhanceEffData["rows"]:
#                             if enhEff["$id"] == enh["EnhanceEffect"]:
#                                 for name in nameData["rows"]:
#                                     if name["$id"] == enhEff["Name"]:
#                                         enh["ID"] = name["name"]
#                                 break
                            
#                 for enh in TestList:
#                     param1 = ""
#                     param2 = ""
#                     if enh["Param1"] != 0:
#                         param1 = ", []"
#                     if enh["Param2"] != 0:
#                         param2 = ", []"
#                     if enh["Caption"] == 0:
#                         comment = "# "
#                     else:
#                         comment = ""
#                     raw_id = enh["ID"]
#                     # Keep only alphanumeric characters
#                     clean_id = ''.join(c for c in raw_id if c.isalnum())
#                     print(f'{comment}Enhancement("", {enh["EnhanceEffect"]}, {enh["Caption"]}, {enh["<3E70C175>"]}, M{param1}{param2}, skillIcon=0) # {raw_id}')
  
def CreateEnhancements():                 
    Enhancement('Healthy', 1, 1, 1, D, [10,100], skillIcon=1) # Max HP Up
    Enhancement('Strong', 2, 3, 1, A, [10,100], skillIcon=2) # Attack Up
    Enhancement('Medic', 3, 4, 1, H, [10,100], skillIcon=1) # Healing Up
    Enhancement('Dextrous', 4, 5, 1, A, [10,100], skillIcon=8) # Dexterity Up
    Enhancement('Agile', 5, 6, 1, D, [10,100], skillIcon=9) # Agility Up
    Enhancement('Critical', 6, 7, 1, A, [10,100], skillIcon=10) # Critical Rate Up
    Enhancement('Iron', 7, 8, 1, D, [10,50], skillIcon=6) # Physical Defense Up
    Enhancement('Ether', 8, 9, 1, D, [10,50], skillIcon=7) # Ether Defense Up
    Enhancement('Deflection', 9, 10, 1, D, [10,50], skillIcon=4) # Block Rate Up
    Enhancement("Hearty", 10, 11, 1, D, [100,2000], skillIcon=38) # Max HP Plus
    Enhancement("Strength", 11, 12, 1, A, [50,200], skillIcon=2) # Attack Plus
    Enhancement("Medical", 12, 13, 1, H, [50,200], skillIcon=1) # Healing Plus
    Enhancement("Dextrous", 13, 14, 1, A, [50,200], skillIcon=8) # Dexterity Plus
    Enhancement("Agile", 14, 15, 1, D, [20,100], skillIcon=9) # Agility Plus
    Enhancement("Critical", 15, 16, 1, A, [10,60], skillIcon=10) # Critical Rate Plus
    Enhancement("Iron", 16, 17, 1, D, [10,50], skillIcon=6) # Physical Defense Plus
    Enhancement("Ether", 17, 18, 1, D, [10,50], skillIcon=7) # Ether Defense Plus
    Enhancement("Blocker", 18, 19, 1, D, [10,40], skillIcon=4) # Block Rate Plus
    Enhancement("Terrestrial", 19, 20, 1, A, [0], [50,200], skillIcon=37) # Species Expert
    Enhancement("Aquatic", 19, 21, 1, A, [1], [50,200], skillIcon=37) # Species Expert
    Enhancement("Aerial", 19, 23, 1, A, [2], [50,200], skillIcon=37) # Species Expert
    Enhancement("Agnus", 19, 27, 1, A, [3], [50,200], skillIcon=37) # Species Expert
    Enhancement("Machine", 19, 29, 1, A, [6], [50,300], skillIcon=37) # Species Expert
    Enhancement("Keves", 19, 26, 1, A, [4], [50,200], skillIcon=37) # Species Expert
    # Enhancement("", 20, 0, 1, M, [], [], skillIcon=0) # <CAE39FB6>
    Enhancement("Counter", 21, 30, 1, D, [50,500], skillIcon=27) # Damage Counter
    Enhancement("Reversal", 22, 31, 1, D, [50,500], skillIcon=27) # Evasion Counter
    Enhancement("Absorber", 23, 32, 1, H, [50,100], skillIcon=44) # Auto-Attack Heal: Self
    Enhancement("Absorber", 24, 36, 1, H, [50,100], [5,10], skillIcon=44) # Auto-Attack Heal Allies
    Enhancement("Exploit", 25, 38, 1, A, [20,150], skillIcon=10) # Critical Hit Plus
    Enhancement("Doublestrike", 26, 39, 1, A, [20,100], skillIcon=35) # Double Attack
    Enhancement("Frontal", 27, 40, 1, A, [50,100], skillIcon=8) # Front Attack↑
    Enhancement("Blindside", 28, 42, 1, A, [50,200], skillIcon=8) # Side Attack↑
    Enhancement("Backstab", 29, 43, 1, A, [30,100], skillIcon=8) # Back Attack↑
    Enhancement("Toppler", 30, 44, 1, A, [50,200], skillIcon=14) # Toppled↑
    Enhancement("Volley", 31, 45, 1, A, [50,200], skillIcon=14) # Launched↑
    Enhancement("Gravity", 32, 47, 1, A, [100,500], skillIcon=28) # Smash Effect Up
    Enhancement("Dazy", 33, 48, 1, A, [50,200], skillIcon=29) # Dazed↑
    Enhancement("Burst", 34, 49, 1, M, [100,500], skillIcon=49) # Burst Effect Up
    Enhancement("Bravery", 35, 50, 1, A, [50,150], skillIcon=42) # Challenger
    Enhancement("Avenger", 36, 51, 1, A, [50,200], skillIcon=2) # Avenger
    Enhancement("Piercing", 37, 52, 1, A, [30,100], skillIcon=5) # Unblockable
    Enhancement("Desperation", 38, 54, 1, A, [30,60], [50,200], skillIcon=44) # Damage Up (HP Low)
    Enhancement("Overwhelm", 39, 55, 1, A, [90,60], [50,150], skillIcon=13) # Damage Up (HP High) 
    Enhancement("Rush", 40, 57, 1, A, [30,90], [25,120], skillIcon=17) # Kick-Starter
    Enhancement("Bloodbath", 41, 58, 1, A, [20,60], [250,500], skillIcon=42) # Enemy KO Damage Up
    Enhancement("Breaker", 42, 59, 1, M, [100,300], skillIcon=39) # Break Duration Up
    Enhancement("Toppler", 43, 60, 1, M, [50,150], skillIcon=39) # Topple Duration Up
    Enhancement("Airborne", 44, 61, 1, M, [50,150], skillIcon=39) # Launch Duration Up
    Enhancement("Concussive", 45, 62, 1, M, [50,150], skillIcon=39) # Daze Duration Up
    Enhancement("Auto", 46, 63, 1, A, [100,500], skillIcon=13) # Auto-Attack Up
    Enhancement("Critical", 47, 64, 1, A, [100,500], skillIcon=13) # Auto-Attack Critical Rate Up
    Enhancement("Honed", 48, 65, 1, A, [100,500], skillIcon=8) # Auto-Attack Accuracy Up
    Enhancement("Clash", 49, 66, 1, M, [50,200], skillIcon=37) # Aggroed↑
    Enhancement("Indoor", 50, 67, 1, A, [50,200], skillIcon=2) # Indoors↑
    Enhancement("Outdoor", 51, 68, 1, A, [50,150], skillIcon=2) # Outdoors↑
    Enhancement("Breaker", 52, 69, 1, M, [20,100], skillIcon=14) # Break Resist Down 
    #Enhancement("", 53, 70, 1, M, [], skillIcon=0) # SanguineFire 
    #Enhancement("", 54, 71, 1, M, [], skillIcon=0) # 64C914AD 
    #Enhancement("", 55, 72, 1, M, [], skillIcon=0) # 52EE5A17 
    Enhancement("Dream", 56, 73, 1, D, [20,60], skillIcon=46) # Perfect Shield
    Enhancement("Absorber", 57, 74, 1, D, [20,60], skillIcon=46) # Physical Absorb
    Enhancement("Absorber", 58, 75, 1, D, [20,80], skillIcon=46) # Ether Absorb
    Enhancement("Awaken", 59, 76, 1, D, [20,80], [4,10], isAccessory=False) # Absorb Awaken
    Enhancement("Spiked", 60, 77, 1, D, [100,600], [5,15], skillIcon=27) # Shield Spike
    Enhancement("Reflector", 61, 78, 1, D, [20,60], skillIcon=27) # Reflector Shield
    Enhancement("Sway", 62, 79, 1, D, [20,60], [100,300], skillIcon=44) # Evasion Up (Low HP)  
    Enhancement("Nimble", 63, 80, 1, D, [50,150], skillIcon=9) # Evasion Up (Mobile)      
    Enhancement("Phantom", 64, 81, 1, D, [100,200], skillIcon=9) # Evasion Up (Stationary)  
    Enhancement("Acrobat", 65, 82, 1, D, [50,150], skillIcon=9) # Evasion Up (Art)
    Enhancement("Posture", 66, 83, 1, D, [20,50], [40,100], skillIcon=44) # Block Rate Plus (Low HP)
    Enhancement("Fortitude", 67, 85, 1, D, [20,50], [20,80], skillIcon=44) # Fortitude (Low HP)   
    # Enhancement("", 68, 86, 1, M, [], skillIcon=0) # <C3E35259>
    Enhancement("Steady", 69, 87, 1, M, Normal, skillIcon=40) # Break Resist
    Enhancement("Steady", 70, 88, 1, M, Normal, skillIcon=40) # Topple Resist
    Enhancement("Steady", 71, 89, 1, M, Normal, skillIcon=40) # Launch Resist
    Enhancement("Steady", 72, 90, 1, M, Normal, skillIcon=40) # Smash Resist
    Enhancement("Steady", 73, 91, 1, M, Normal, skillIcon=40) # Daze Resist
    # Enhancement("", 74, 92, 1, M, [], skillIcon=0) # <A7C9AAD4>
    Enhancement("Steady", 75, 93, 1, M, Normal, skillIcon=40) # Blowdown Resist
    Enhancement("Steady", 76, 94, 1, M, Normal, skillIcon=40) # Knockback Resist
    Enhancement("Whisper", 77, 95, 1, A, [70,100], skillIcon=12) # Slower Auto-Attack Aggro 
    Enhancement("Flourish", 78, 96, 1, D, [100,250], skillIcon=12) # Faster Auto-Attack Aggro 
    Enhancement("Whisper", 79, 97, 1, A, [20,60], skillIcon=12) # Slower Arts Aggro        
    Enhancement("Flourish", 80, 98, 1, D, [60,120], skillIcon=12) # Faster Arts Aggro        
    Enhancement("Shadowed", 81, 101, 1, A, [50,150], skillIcon=12) # Aggro Reduction Up      
    Enhancement("Garish", 82, 102, 1, D, [50,150], skillIcon=12) # Auto Aggro Up
    Enhancement("Battlecry", 83, 107, 1, D, [1000,2000], skillIcon=12) # Aggro Starter
    Enhancement("Flourish", 84, 108, 1, D, [100,500], skillIcon=12) # Faster Damage Aggro     
    # Enhancement("", 85, 0, 1, M, [], skillIcon=0) # <D18934AB>
    Enhancement("Angelic", 86, 109, 1, H, [50,100], skillIcon=32) # Rescue HP Up: Other     
    Enhancement("Vamp", 87, 111, 1, H, [100,200], [3,10], skillIcon=16) # Arts Heal
    Enhancement("Support", 88, 112, 1, H, [50,150], skillIcon=16) # Healing Arts Up
    Enhancement("Whisper", 89, 113, 1, H, [50,150], skillIcon=16) # Slower Healing Aggro    
    Enhancement("Self Care", 90, 114, 1, M, [20,150], skillIcon=1) # HP Recovery Up
    Enhancement("Mending", 91, 115, 1, H, [20,90], [50,250], skillIcon=52) # Damage Heal: Self   
    Enhancement("Mending", 92, 116, 1, H, [20,90], [50,150], skillIcon=52) # Damage Heal: Allies 
    Enhancement("Perfect", 93, 117, 1, A, [50,100], skillIcon=36) # Cancel Up
    Enhancement("Unbeatable", 94, 119, 1, M, [20,70], skillIcon=32) # Unbeatable
    Enhancement("Diurnal", 95, 120, 1, A, [20,150], skillIcon=12) # Night Vision
    Enhancement("Nocturnal", 96, 121, 1, M, [20,150], skillIcon=12) # Sunlight Eye
    # Enhancement("", 97, 0, 1, M, [], skillIcon=0) # <4943A920>
    # Enhancement("", 98, 0, 1, M, [], skillIcon=0) # <09F52558>
    Enhancement("Potent", 99, 122, 1, H, [50,100], skillIcon=23) # Buff Effect Up
    Enhancement("Adept", 100, 123, 1, H, [50,150], skillIcon=39) # Longer Buff Timers     
    Enhancement("Bane", 101, 124, 1, M, [50,150], skillIcon=23) # Debuff Effect Up       
    Enhancement("Torturer", 102, 125, 1, M, [50,100], skillIcon=39) # Longer Debuff Timers   
    Enhancement("Bane", 103, 126, 1, M, [50,100], skillIcon=23) # Debuff Success Rate Plus
    Enhancement("Sampler", 104, 127, 1, A, [20,100], skillIcon=18) # Art extends debuff timers give em a sampler
    Enhancement("Party", 105, 128, 1, M, [10,50], skillIcon=47) # Chain Gauge Up (Critical)
    Enhancement("Disco", 106, 129, 1, M, [20,80], skillIcon=47) # Chain Gauge Up (Art)   
    Enhancement("Heroic", 107, 130, 1, A, [20,60], [300,600], skillIcon=42) # Enemy Count Damage Up
    Enhancement("Sniper", 108, 131, 1, A, [5,40], skillIcon=8) # Ranged Attack Range Up 
    Enhancement("Wish", 109, 132, 1, M, [20,70], skillIcon=32) # KO Heal: Allies
    Enhancement("Enthrall", 110, 134, 1, M, [20,60], skillIcon=51) # % chance of arts to stop enemy recharge
    Enhancement("Balanced", 111, 135, 1, A, skillIcon=33) # Anti-Deflection
    # Enhancement("", 112, 0, 1, M, [], skillIcon=0) # <AEE52010>
    # Enhancement("", 113, 0, 1, M, [], skillIcon=0) # <B05AB2EB>
    Enhancement("Executioner", 114, 136, 1, M, [10,30], [10,30], skillIcon=26) # <C4D784E6> Instant kill below hp%
    Enhancement("Tailwind", 115, 138, 1, M, [10,40], [5,25], skillIcon=9) # Accuracy/Evasion Up: Allies
    # Enhancement("", 116, 0, 1, M, [], [], skillIcon=0) # <554E9057>
    Enhancement("Whisper", 117, 139, 1, A, [20,80], skillIcon=12) # Slower Attack Aggro
    Enhancement("Dream", 118, 140, 1, D, [10,40], skillIcon=52) # All Defenses Plus
    Enhancement("Godspeed", 119, 141, 1, M, [10,25], skillIcon=29) # Perfect Hit/Evasion
    Enhancement("Reflector", 120, 142, 1, D, [5,15], skillIcon=27) # Reflection
    Enhancement("Combo", 121, 143, 1, A, [50,200], skillIcon=35) # Toppled/Launched↑
    # Enhancement("", 122, 0, 1, M, [], skillIcon=0) # <1902ADDB>
    Enhancement("KO Vamp", 123, 144, 1, M, [10,80], skillIcon=38) # Enemy KO Heal: Allies
    # Enhancement("", 124, 0, 1, M, [], [], skillIcon=0) # <E48EE6DF>
    # Enhancement("Challenger", 125, 145, 1, M, [], [], skillIcon=0) # Power Up (Dire Battle) Wrong Caption and effect idk why this is here
    # Enhancement("", 126, 0, 1, M, [], skillIcon=0) # <2B78D893>
    Enhancement("Nimble", 127, 149, 1, M, [10,80], skillIcon=40) # Resist Combo Reaction
    Enhancement("Challenger", 128, 150, 1, A, [50,150], skillIcon=42) # Unique/Boss↑
    Enhancement("Mashing", 129, 151, 1, M, [20,50], skillIcon=20) # Continuous Arts
    Enhancement("Pierce", 130, 152, 1, A, [30,100], skillIcon=33) # Piercing Attacks
    Enhancement("Lightning", 131, 154, 1, M, [50,250], skillIcon=29) # Auto-Attack Speed Up
    Enhancement("Reckless", 132, 156, 1, A, [10,40], isGem=False, isAccessory=False) # Lose % of HP on Art
    Enhancement("Concussive", 133, 159, 1, M, [20,60], isGem=False, isAccessory=False) # Art hit lose aggro
    Enhancement("Pinpoint", 134, 160, 1, A, [20,50], skillIcon=31) # Recover Recharge (Critical)
    Enhancement("Regen", 135, 161, 1, M, [5,25], [5,10], skillIcon=1) # Regeneration (Low HP)
    Enhancement("Talented", 136, 162, 1, A, [50,100], [250,500], skillIcon=35) # Damage Up (Talent Art)
    Enhancement("Bouncy", 137, 163, 1, D, [20,50], [1,3], skillIcon=41) # Damage Counter: Reaction
    # Enhancement("", 138, 0, 1, M, skillIcon=0) # <8220967D>
    Enhancement("Beginner", 139, 164, 1, M, [50,200], skillIcon=21) # Bigger Cancel Window
    Enhancement("Vamp", 140, 165, 1, H, [60,200], isAccessory=False, isGem=False) # <3F363F42> Art hit heal allies
    Enhancement("Art Mend", 141, 167, 1, M, [3,15], isAccessory=False, isGem=False) # <0C909AAE> While art performed recover % hp
    Enhancement("Jamming", 142, 168, 1, M, [20,90], skillIcon=40) # Ranged Evasion
    Enhancement("Retainer", 143, 169, 1, D, [50,100], skillIcon=26) # Hold Aggro (Self KO)
    Enhancement("Martyr", 144, 170, 1, A, [50,100], skillIcon=26) # Damage Up (Ally KO)
    # Enhancement("", 145, 0, 1, M, [], [], skillIcon=0) # <4724B11C>
    Enhancement("Ascendancy", 146, 171, 1, A, [1,10], [1,10], skillIcon=0) # <1DDE9148> Crit strikes increase damage dealt and crit rate
    Enhancement("Reckless", 147, 172, 1, A, [20,120], [10,60], skillIcon=19) # Attack Shift
    Enhancement("Sheltered", 148, 173, 1, D, [10,60], [10,60], skillIcon=4) # Defense Shift
    Enhancement("Immunity", 149, 174, 1, M, [25,85], skillIcon=52) # Debuff Resist: All
    Enhancement("Resistance", 150, 175, 1, M, [25,75], skillIcon=52) # Shorter Debuff Timers
    Enhancement("Precision", 151, 176, 1, A, [10,30], skillIcon=8) # Damage Up (Cancel)
    # Enhancement("", 152, 0, 1, M, [], skillIcon=0) # <CE6DB1B1>
    Enhancement("Hacker", 153, 177, 1, M, skillIcon=19) # Soul Hacking
    Enhancement("Chained", 154, 178, 1, M, [20,50], skillIcon=5) # <1DD0CB32> During chain attack reduces enemy ether defense
    # Enhancement("", 155, 0, 1, M, [], skillIcon=0) # <0D99005B>
    # Enhancement("", 156, 0, 1, M, [], skillIcon=0) # <EA4FE79F>
    # Enhancement("", 157, 0, 1, M, [], skillIcon=0) # <7F54F93E>
    Enhancement("Plague", 158, 179, 1, M, [5,20], skillIcon=23) # <C719FE0D> Spread debuffs to other enemies when you hit them
    Enhancement("Rejuvenate", 159, 180, 1, M, [50,100], skillIcon=39) # <1C89FC37> Restore all art cooldowns for team except self
    Enhancement("Disrupter", 160, 181, 1, M, [1,3], skillIcon=27) # <621F1009> Enemys using arts will be knocked back
    Enhancement("Viper", 161, 182, 1, A, [50,300], skillIcon=8) # Damage Up (Enemy Arts)
    Enhancement("Sniper", 162, 183, 1, A, [10,100], skillIcon=8) # <3C2BDC90> Crit Up (Enemy Arts)
    Enhancement("Seeking", 163, 184, 1, M, [50,200], skillIcon=8) # Accuracy Up (Enemy Arts)
    Enhancement("Finale", 164, 185, 1, A, [500,1500], isGem=False, isAccessory=False) # <0282C4D5> Uses all arts and increases damage of art used for that
    Enhancement("Bloodlust", 165, 186, 1, A, [10,50], [30,250], skillIcon=44) # Wounded Enemy↑
    Enhancement("Strikeout", 166, 189, 1, M, [5,10], skillIcon=8) # Accuracy Up (Miss)
    Enhancement("Debuffer", 167, 190, 1, A, [30,45], [100,200], skillIcon=24) # Debuffed Enemy↑
    # Enhancement("", 168, 0, 1, M, [], skillIcon=0) # <ED6CBA7D>
    Enhancement("Devils", 169, 193, 1, M, [1,5], isGem=False, isAccessory=False) # <3F91CECC> Apply param1 random debuffs on art
    Enhancement("Blessed", 170, 194, 1, M, [1,5], skillIcon=22) # <E7C12D95> # Wonder if this works as a passive
    # Enhancement("", 171, 0, 1, M, [], skillIcon=0) # <C29024C3>
    Enhancement("Explosive", 172, 197, 1, M, [5,15], [300,800], skillIcon=49) # Damage Bomb (Self KO)
    Enhancement("Spirit", 173, 198, 1, M, [20,80], skillIcon=26) # Party Recharge (Self KO)
    # Enhancement("", 174, 0, 1, M, [], [], skillIcon=0) # <48F464E4>
    Enhancement("Perfect", 175, 199, 1, M, skillIcon=22) # Perfect Hit (Cancel)
    # Enhancement("", 176, 0, 1, M, [], [], skillIcon=0) # <A8B4FF50>
    Enhancement("Fortitude", 177, 200, 1, M, [20,60], skillIcon=6) # Fortitude (Art Duration)
    Enhancement("Hoarding", 178, 202, 1, A, [50,200], skillIcon=39) # Damage Up (Full Recharge)
    Enhancement("Depleted", 179, 203, 1, A, [25,150], skillIcon=17) # <0007E213> Damage Up (Less Recharge)
    # Enhancement("", 180, 0, 1, M, [], [], skillIcon=0) # Persistent Damage Up
    Enhancement("Flurry", 181, 206, 1, A, [25,100], [25,100], skillIcon=18) # Sequential Auto-Attack Up
    Enhancement("Stance", 182, 210, 1, M, [50,250], skillIcon=0) # Stance Duration Up
    Enhancement("Buffer", 183, 211, 1, M, [5,20], skillIcon=38) # Buff Heal
    # Enhancement("", 184, 0, 1, M, [], [], skillIcon=0) # <CF9BFB20>
    Enhancement("Tender", 185, 215, 1, M, [100,100], skillIcon=24) # Tender Auto-Attack
    Enhancement("Tender", 186, 216, 1, M, [100,100], skillIcon=24) # Tender Arts
    Enhancement("Fusion", 187, 217, 1, A, [50,150], skillIcon=13) # Fusion Arts Up
    # Enhancement("", 188, 218, 1, M, [], [], skillIcon=0) # <27C116CB>
    Enhancement("Pacifist", 189, 219, 1, M, [100,400], skillIcon=12) # Aggro Reduce Up (Targeted)
    Enhancement("Mocking", 190, 220, 1, D, [50,200], skillIcon=9) # Draw Aggro (Evasion)
    Enhancement("Surefire", 191, 223, 1, A, [20,80], skillIcon=37) # Incremental Damage Up
    # Enhancement("", 192, 0, 1, M, [], [], skillIcon=0) # Preemptive Buff
    Enhancement("Share buffs", 193, 225, 1, M, isGem=False, isAccessory=False) # <5EA32440>
    Enhancement("Buffed", 194, 226, 1, A, [50,150], skillIcon=16) # Damage Up (Buff No.)
    Enhancement("Acrobat", 195, 227, 1, M, [30,70], [2,4], skillIcon=40) # Aerial Recovery
    Enhancement("Panic", 196, 229, 1, M, [100,300], skillIcon=17) # Risky Recharge Up
    Enhancement("Antiqua", 197, 230, 1, A, [50,200], skillIcon=51, isGem=False, isAccessory=False) # Damage Up (Elem. Discharge)
    Enhancement("Extra", 198, 231, 1, A, [20,60], [100,300], skillIcon=35) # EX Damage (Base Attack)
    Enhancement("Extra", 199, 232, 1, H, [40,100], [500,1000], skillIcon=35) # EX Damage (Base Healing)
    Enhancement("Flatten", 200, 233, 1, M, [50,100], [100,500], skillIcon=10) # <59C16213> Inflicting blowdown and knockback deals damage
    # Enhancement("", 201, 0, 1, M, [], [], skillIcon=0) # <3BFA4DC7>
    # Enhancement("", 202, 0, 1, M, [], skillIcon=0) # Damage Up (Ally Heal)
    Enhancement("Guardian", 203, 235, 1, D, [5,10], [25,50], skillIcon=41) # Prevent Attack: Nearby Allies       
    Enhancement("Everlasting", 204, 236, 1, M, [100,400], skillIcon=21) # Field Duration Up
    Enhancement("Aggressive", 205, 237, 1, A, [100,300], skillIcon=30) # Field Damage Up
    Enhancement("Dissolution", 206, 238, 1, A, [100,300], skillIcon=30) # Field Dissolution Dmg. Up
    # Enhancement("", 207, 239, 1, M, [], skillIcon=0) # <3C8F6C0E>
    Enhancement("Rescuer", 208, 241, 1, M, skillIcon=25) # Enable Rescue
    Enhancement("Ghostwalker", 209, 242, 1, M, [10,50], skillIcon=9) # Evasion Chance
    Enhancement("Batter", 210, 243, 1, A, [50,200], skillIcon=2) # Physical Damage Up
    Enhancement("Magician", 211, 244, 1, A, [50,200], skillIcon=29) # Ether Damage Up
    Enhancement("Destabilizer", 212, 245, 1, M, [50,90], skillIcon=31) # Reaction Success Up
    Enhancement("Talented", 213, 246, 1, M, [50,100], skillIcon=31) # Talent Art Starter
    Enhancement("Solid", 214, 248, 1, D, [20,60], skillIcon=41) # Guard Efficiency Up
    # Enhancement("", 215, 0, 1, M, [], skillIcon=0) # <6B7B5B21>
    Enhancement("Bursting", 216, 249, 1, H, [1], [100,400], skillIcon=45) # Combo HP Heal: Allies
    Enhancement("Qigong", 217, 250, 1, A, [20,50], skillIcon=33) # Pierce Physical Defense
    Enhancement("Qigong", 218, 251, 1, A, [20,50], skillIcon=33) # Pierce Ether Defense
    Enhancement("Hone", 219, 252, 1, A, [10,20], skillIcon=8) # Critical Rate Up (Hit)
    Enhancement("Cleansing", 220, 253, 1, H, [25,50], skillIcon=16) # Healing Up (Debuff Clear)
    Enhancement("Buffer", 221, 254, 1, A, [50,100], skillIcon=18) # Damage Up (Buff)
    Enhancement("Debuffer", 222, 255, 1, A, [50,100], skillIcon=24) # Damage Up (Debuff)
    # # Enhancement("", 223, 0, 1, M, [], skillIcon=0) # <29AEFFA8>
    # # Enhancement("", 224, 0, 1, M, [], skillIcon=0) # <745DD649>
    # # Enhancement("", 225, 0, 1, M, [], skillIcon=0) # <4B82A9D2>
    # Enhancement("", 226, 256, 1, M, [], skillIcon=0) # <F1A4DB56>
    # # Enhancement("", 227, 0, 1, M, [], skillIcon=0) # <7F104DB2>
    # # Enhancement("", 228, 0, 1, M, [], skillIcon=0) # <55351493>
    # # Enhancement("", 229, 0, 1, M, [], [], skillIcon=0) # <0147B3BB>
    # # Enhancement("", 230, 0, 1, M, [], [], skillIcon=0) # <4E126891>
    # Enhancement("", 231, 259, 1, M, [], skillIcon=0) # <224D3D2A>
    # Enhancement("", 232, 260, 1, M, [], skillIcon=0) # <E0D09216>
    # Enhancement("", 233, 261, 1, M, [], [], skillIcon=0) # Nearby Ally Fortitude
    # # Enhancement("", 234, 0, 1, M, [], [], skillIcon=0) # <1E3DEC99>
    # Enhancement("", 235, 264, 1, M, [], [], skillIcon=0) # Awaken (Damage Stack)
    # Enhancement("", 236, 265, 1, M, [], [], skillIcon=0) # <0662DEEF>
    # Enhancement("", 237, 266, 1, M, [], [], skillIcon=0) # Attack Up: All Allies
    # Enhancement("", 238, 267, 1, M, [], [], skillIcon=0) # Elemental Up
    # Enhancement("", 239, 269, 1, M, [], [], skillIcon=0) # Def./Recovery Up: All Allies        
    # # Enhancement("", 240, 0, 1, M, [], skillIcon=0) # <8A98413D>
    # # Enhancement("", 241, 0, 1, M, [], skillIcon=0) # Rescue Buff
    # # Enhancement("", 242, 0, 1, M, [], [], skillIcon=0) # <2D37CF4F>
    # Enhancement("", 243, 271, 1, M, [], skillIcon=0) # Pierce Defense (Critical)
    # Enhancement("", 244, 272, 1, M, [], skillIcon=0) # <4078B801>
    # Enhancement("", 245, 274, 1, M, [], skillIcon=0) # Extend Combo Time (Art Hit)
    # Enhancement("", 246, 275, 1, M, [], [], skillIcon=0) # <54F2F7D0>
    # Enhancement("", 247, 276, 1, M, [], skillIcon=0) # Evasion Up (Targeted)
    # Enhancement("", 248, 277, 1, M, [], [], skillIcon=0) # <E599A89B>
    # Enhancement("", 249, 278, 1, M, [], skillIcon=0) # <183D62F0>
    # Enhancement("", 250, 280, 1, M, [], [], skillIcon=0) # <6E886F68>
    # Enhancement("", 251, 281, 1, M, [], skillIcon=0) # <5DA2D73A>
    # Enhancement("", 252, 283, 1, M, [], skillIcon=0) # <747EC061>
    # Enhancement("", 253, 284, 1, M, [], skillIcon=0) # Slower Debuff Expiry
    # Enhancement("", 254, 287, 1, M, [], skillIcon=0) # Slower Buff Expiry
    # Enhancement("", 255, 290, 1, M, [], skillIcon=0) # <7B2E3FC1>
    # Enhancement("", 256, 292, 1, M, [], [], skillIcon=0) # <3C65A37E>
    # Enhancement("", 257, 293, 1, M, [], skillIcon=0) # Negate Combo Reaction (Art)
    # Enhancement("", 258, 294, 1, M, [], skillIcon=0) # Damage Up (Targeted No.)
    # Enhancement("", 259, 297, 1, M, [], skillIcon=0) # <A9068BC4>
    # Enhancement("", 260, 298, 1, M, [], skillIcon=0) # <E0A5E317>
    # Enhancement("", 261, 299, 1, M, [], skillIcon=0) # <96E9BE64>
    # # Enhancement("", 262, 0, 1, M, [], [], skillIcon=0) # Debuff Resist
    # # Enhancement("", 263, 0, 1, M, [], [], skillIcon=0) # <71289EF7>
    # # Enhancement("", 264, 0, 1, M, [], [], skillIcon=0) # <C427566B>
    # # Enhancement("", 265, 0, 1, M, [], [], skillIcon=0) # <32D6A4FD>
    # Enhancement("", 266, 307, 1, M, [], skillIcon=0) # Arts Link
    # # Enhancement("", 267, 0, 1, M, [], skillIcon=0) # Recover Recharge (Ene. KO)
    # Enhancement("", 268, 309, 1, M, [], skillIcon=0) # Damage Up (Critical)
    # Enhancement("", 269, 310, 1, M, [], skillIcon=0) # Critical Up (Launched)
    # Enhancement("", 270, 311, 1, M, [], skillIcon=0) # Recharge Rec. Up (Danger)
    # Enhancement("", 271, 312, 1, M, [], skillIcon=0) # Reduce Aggro (Ally KO)
    # # Enhancement("", 272, 0, 1, M, [], [], skillIcon=0) # Evasion Buff
    # Enhancement("", 273, 315, 1, M, [], [], skillIcon=0) # Target Lock (Danger)
    # Enhancement("", 274, 316, 1, M, [], skillIcon=0) # Damage Up (Time)
    # Enhancement("", 275, 317, 1, M, [], skillIcon=0) # Reduce Aggro (Auto-Attack)
    # Enhancement("", 276, 318, 1, M, [], [], skillIcon=0) # Critical Rate + Damage Up
    # Enhancement("", 277, 319, 1, M, [], skillIcon=0) # Emergency Rescue
    # Enhancement("", 278, 320, 1, M, [], skillIcon=0) # Damage Up (Unharmed)
    # # Enhancement("", 279, 0, 1, M, [], [], skillIcon=0) # Enemy KO Buff
    # Enhancement("", 280, 322, 1, M, [], skillIcon=0) # Extreme Attack Shift
    # Enhancement("", 281, 323, 1, M, [], skillIcon=0) # Auto-Atk Spd Up (Same Role)
    # Enhancement("", 282, 324, 1, M, [], skillIcon=0) # Attacker Mastery
    # Enhancement("", 283, 325, 1, M, [], skillIcon=0) # Defender Mastery
    # Enhancement("", 284, 326, 1, M, [], skillIcon=0) # Healer Mastery
    # Enhancement("", 285, 327, 1, M, [], [], skillIcon=0) # Rushed Healing Arts
    # Enhancement("", 286, 328, 1, M, [], [], skillIcon=0) # Ally KO Buff
    # Enhancement("", 287, 329, 1, M, [], skillIcon=0) # Fortitude (No Arts Ready)
    # Enhancement("", 288, 330, 1, M, [], skillIcon=0) # Recover Recharge (Ally KO)
    # Enhancement("", 289, 331, 1, M, [], skillIcon=0) # Block Recharge
    # Enhancement("", 290, 332, 1, M, [], [], skillIcon=0) # Recover HP (Low HP)
    # Enhancement("", 291, 333, 1, M, [], skillIcon=0) # Target Lock (Revival)
    # Enhancement("", 292, 334, 1, M, [], [], skillIcon=0) # Power Up (Revival)
    # Enhancement("", 293, 335, 1, M, [], skillIcon=0) # Damage Transfer
    # # Enhancement("", 294, 0, 1, M, [], skillIcon=0) # <D33620B5>
    # Enhancement("", 295, 337, 1, M, [], skillIcon=0) # <3A8B75DC>
    # # Enhancement("", 296, 0, 1, M, [], [], skillIcon=0) # <108C6BDC>
    # # Enhancement("", 297, 0, 1, M, [], skillIcon=0) # <3DC91AB4>
    # # Enhancement("", 298, 0, 1, M, [], skillIcon=0) # <B45078E8>
    # Enhancement("", 299, 372, 1, M, [], skillIcon=0) # <5D432F9D>
    # Enhancement("", 300, 373, 1, M, [], skillIcon=0) # <699CD98E>
    # Enhancement("", 301, 374, 1, M, [], skillIcon=0) # <01DFEBDE>
    # Enhancement("", 302, 375, 1, M, [], skillIcon=0) # <6A7AE143>
    # Enhancement("", 303, 376, 1, M, [], skillIcon=0) # <3B070EC3>
    # # Enhancement("", 304, 0, 1, M, [], skillIcon=0) # <ADD9368C>
    # Enhancement("", 305, 377, 1, M, [], [], skillIcon=0) # <170EE93C>
    # Enhancement("", 306, 378, 1, M, [], skillIcon=0) # <F62D628F>
    # # Enhancement("", 307, 0, 1, M, [], [], skillIcon=0) # <6C84E6C5>
    # # Enhancement("", 308, 0, 1, M, [], [], skillIcon=0) # <1CC5A345>
    # Enhancement("", 309, 382, 1, M, [], [], skillIcon=0) # <A34DB1D7>
    # Enhancement("", 310, 383, 1, M, [], skillIcon=0) # <665C44C7>
    # Enhancement("", 311, 384, 1, M, [], skillIcon=0) # <42203200>
    # # Enhancement("", 312, 0, 1, M, [], skillIcon=0) # <44DED265>
    # # Enhancement("", 313, 0, 1, M, [], [], skillIcon=0) # <697730B7>
    # Enhancement("", 314, 386, 1, M, [], skillIcon=0) # <A8EEF413>
    # # Enhancement("", 315, 0, 1, M, [], [], skillIcon=0) # <D30612A6>
    # Enhancement("", 316, 397, 1, M, [], skillIcon=0) # <C42DC4C1>
    # # Enhancement("", 317, 0, 1, M, [], skillIcon=0) # <E371CADF>
    # Enhancement("", 318, 398, 1, M, [], skillIcon=0) # Attack AOE Range Up
    # Enhancement("", 319, 400, 1, M, [], skillIcon=0) # Reaction Recharge
    # Enhancement("", 320, 401, 1, M, [], skillIcon=0) # Damage Up (In Water)
    # Enhancement("", 321, 402, 1, M, [], skillIcon=0) # Recharge Up (In Water)
    # Enhancement("", 322, 403, 1, M, [], skillIcon=0) # Damage Up (On Land)
    # Enhancement("", 323, 404, 1, M, [], skillIcon=0) # Recharge Up (On Land)
    # Enhancement("", 324, 405, 1, M, [], skillIcon=0) # Damage Up (Self Debuff)
    # Enhancement("", 325, 406, 1, M, [], skillIcon=0) # Fortitude (Enemy KO)
    # Enhancement("", 326, 324, 1, M, [], skillIcon=0) # <81E4C3B5>
    # # Enhancement("", 327, 0, 1, M, [], skillIcon=0) # <69CE51B7>
    # # Enhancement("", 328, 0, 1, M, [], skillIcon=0) # <EE1FAEA1>
    # # Enhancement("", 329, 0, 1, M, [], skillIcon=0) # <DF068DFA>
    # # Enhancement("", 330, 0, 1, M, [], skillIcon=0) # <1ABA7C2B>
    # # Enhancement("", 331, 0, 1, M, [], skillIcon=0) # <D450C258>
    # # Enhancement("", 332, 0, 1, M, [], skillIcon=0) # <2661B30A>
    # # Enhancement("", 333, 0, 1, M, [], [], skillIcon=0) # <78B0628E>
    # Enhancement("", 334, 412, 1, M, [], [], skillIcon=0) # <94556EFC>
    # # Enhancement("", 335, 0, 1, M, [], [], skillIcon=0) # <2F1CE75E>
    # # Enhancement("", 336, 0, 1, M, [], skillIcon=0) # <03522C97>
    # Enhancement("", 337, 415, 1, M, [], [], skillIcon=0) # Cover Low HP Allies
    # Enhancement("", 338, 416, 1, M, [], [], skillIcon=0) # Ranged Counter
    # Enhancement("", 339, 417, 1, M, [], skillIcon=0) # <2307272B>
    # # Enhancement("", 340, 0, 1, M, [], skillIcon=0) # <13E86D62>
    # Enhancement("", 341, 422, 1, M, skillIcon=0) # <5AA8EF8D>
    # Enhancement("", 342, 423, 1, M, skillIcon=0) # <8321536A>
    # Enhancement("", 343, 424, 1, M, skillIcon=0) # <12290987>
    # Enhancement("", 344, 425, 1, M, skillIcon=0) # <AE3060F1>
    # Enhancement("", 345, 426, 1, M, skillIcon=0) # <DABAB9B0>
    # Enhancement("", 346, 427, 1, M, skillIcon=0) # <635B23F8>
    # # Enhancement("", 347, 0, 1, M, [], [], skillIcon=0) # <FBF26980>
    # # Enhancement("", 348, 0, 1, M, [], [], skillIcon=0) # <BDD4CC17>
    # # Enhancement("", 349, 0, 1, M, [], skillIcon=0) # <3868CBC6>
    # # Enhancement("", 350, 0, 1, M, [], skillIcon=0) # <299669B7>
    # # Enhancement("", 351, 0, 1, M, [], skillIcon=0) # <B469390D>
    # # Enhancement("", 352, 0, 1, M, [], [], skillIcon=0) # <D021D9EE>
    # # Enhancement("", 353, 0, 1, M, [], [], skillIcon=0) # <FF3CFA6B>
    # # Enhancement("", 354, 0, 1, M, [], [], skillIcon=0) # <3DFBD363>
    # # Enhancement("", 355, 0, 1, M, [], [], skillIcon=0) # <B7DE0EBC>
    # Enhancement("", 356, 428, 1, M, [], [], skillIcon=0) # Quick Move Evasion Up
    # Enhancement("", 357, 429, 1, M, [], [], skillIcon=0) # Quick Move Damage Up
    # Enhancement("", 358, 430, 1, M, [], [], skillIcon=0) # Quick Move AOE Damage
    # Enhancement("", 359, 431, 1, M, [], [], skillIcon=0) # Faster Interlink Level Gain
    # Enhancement("", 360, 432, 1, M, [], [], skillIcon=0) # Recover Recharge (Rescue)
    # Enhancement("", 361, 433, 1, M, [], [], skillIcon=0) # Starting Master Arts
    # Enhancement("", 362, 441, 1, M, [], skillIcon=0) # Class Aptitude Up
    # Enhancement("", 363, 442, 1, M, [], skillIcon=0) # Extra Positional Arts
    # Enhancement("", 364, 443, 1, M, [], skillIcon=0) # Extra Field Arts
    # Enhancement("", 365, 444, 1, M, [], skillIcon=0) # <FC852C14>
    # # Enhancement("", 366, 0, 1, M, [], skillIcon=0) # <0A83170C>
    # # Enhancement("", 367, 0, 1, M, [], skillIcon=0) # <5E206C1B>
    # # Enhancement("", 368, 0, 1, M, [], skillIcon=0) # <85F2BABF>
    # Enhancement("", 369, 447, 1, M, [], [], skillIcon=0) # Absorb Attacks in Range
    # Enhancement("", 370, 448, 1, M, [], skillIcon=0) # <6AED9FC9>
    # Enhancement("", 371, 450, 1, M, [], skillIcon=0) # Starter TP Plus
    # Enhancement("", 372, 240, 1, M, [], [], skillIcon=0) # Fast Rescue & Healing Plus
    # Enhancement("", 373, 110, 1, M, [], [], skillIcon=0) # Rescue HP & Healing Plus
    # Enhancement("", 374, 451, 1, M, skillIcon=0) #
    # Enhancement("", 375, 452, 1, M, skillIcon=0) #
    # Enhancement("", 376, 453, 1, M, [], skillIcon=0) # <D90DECBD>
    # Enhancement("", 377, 455, 1, M, [], skillIcon=0) # <887EC595>
    # Enhancement("", 378, 457, 1, M, skillIcon=0) # <5228990D>
    # Enhancement("", 379, 459, 1, M, [], skillIcon=0) # <C006052B>
    # Enhancement("", 380, 460, 1, M, [], skillIcon=0) # <9E09B0E3>
    # Enhancement("", 381, 462, 1, M, [], skillIcon=0) # <C682C0B2>
    # Enhancement("", 382, 464, 1, M, skillIcon=0) # <ACEEE2B3>
    # Enhancement("", 383, 466, 1, M, skillIcon=0) # <F5A970B0>
    # Enhancement("", 384, 468, 1, M, [], [], skillIcon=0) # <1C953DC1>
    # Enhancement("", 385, 470, 1, M, [], skillIcon=0) # <119C145F>
    # Enhancement("", 386, 472, 1, M, [], skillIcon=0) # <819DAB29>
    # Enhancement("", 387, 474, 1, M, [], skillIcon=0) # <8166DDA7>
    # Enhancement("", 388, 476, 1, M, [], skillIcon=0) # <727B2C77>
    # Enhancement("", 389, 478, 1, M, skillIcon=0) # <9BE9B1DB>
    # Enhancement("", 390, 480, 1, M, [], [], skillIcon=0) # <67C12EA7>
    # Enhancement("", 391, 482, 1, M, [], skillIcon=0) # <BD2FFC2C>
    # Enhancement("", 392, 484, 1, M, [], skillIcon=0) # <44DD9F9C>
    # Enhancement("", 393, 486, 1, M, skillIcon=0) # <BBA3F2C3>
    # Enhancement("", 394, 488, 1, M, [], skillIcon=0) # <8B5865D2>
    # # Enhancement("", 395, 0, 1, M, [], [], skillIcon=0) # <CBAEDB1D>
    # Enhancement("", 396, 490, 1, M, [], skillIcon=0) # Recover HP: Self (Evasion)
    # Enhancement("", 397, 491, 1, M, [], skillIcon=0) # Recover Recharge (Evasion)
    # Enhancement("", 398, 492, 1, M, [], skillIcon=0) # <7BA9A48D>
    # Enhancement("", 399, 494, 1, M, [], skillIcon=0) # Recharge Up (Self KO)
    # Enhancement("", 400, 495, 1, M, [], skillIcon=0) # <FB5146DB>
    # Enhancement("", 401, 499, 1, M, [], [], skillIcon=0) # Recharge (Nearby Ally Hit)
    # Enhancement("", 402, 500, 1, M, [], skillIcon=0) # Ranged Heal (Critical)
    # Enhancement("", 403, 501, 1, M, [], [], skillIcon=0) #
    # Enhancement("", 404, 502, 1, M, [], [], skillIcon=0) # Critical Hit Plus: All Allies       
    # Enhancement("", 405, 503, 1, M, [], [], skillIcon=0) # Power Up (In Field)
    # Enhancement("", 406, 504, 1, M, skillIcon=0) # Max Fields Up
    # Enhancement("", 407, 505, 1, M, [], [], skillIcon=0) # <D8498101>
    # Enhancement("", 408, 507, 1, M, [], skillIcon=0) # Several Stats Up
    # Enhancement("", 409, 508, 1, M, [], [], skillIcon=0) # Weaken Party
    # Enhancement("", 410, 173, 0, M, [], [], skillIcon=0) # <554E813F>
    # # Enhancement("", 419, 0, 1, M, [], skillIcon=0) # <83D1DC60>
    # # Enhancement("", 411, 0, 1, M, [], skillIcon=0) # <03956403>
    # Enhancement("", 412, 509, 1, M, [], skillIcon=0) # Unity Combo Damage Up
    # Enhancement("", 413, 525, 1, M, [], [], skillIcon=0) # <D3A726C0>
    # Enhancement("", 414, 529, 1, M, [], skillIcon=0) # <EF72174A>
    # Enhancement("", 415, 530, 1, M, [], [], skillIcon=0) # <E110F3CA>
    # Enhancement("", 416, 430, 1, M, [], [], skillIcon=0) # Quick Move AOE Damage
    # Enhancement("", 417, 532, 1, M, [], skillIcon=0) # Weakness Damage Up
    # Enhancement("", 418, 316, 1, M, [], skillIcon=0) # Damage Up (Time)
    # # Enhancement("", 421, 0, 1, M, [], [], skillIcon=0) # <B665A1F1>
    # Enhancement("", 424, 399, 1, M, [], [], skillIcon=0) # Attack AOE Range + Dmg Up
    # Enhancement("", 425, 534, 1, M, [], skillIcon=0) # Unity Special Starter
    # # Enhancement("", 426, 0, 1, M, [], skillIcon=0) # <11BB435A>
    # # Enhancement("", 428, 0, 1, M, [], [], skillIcon=0) # Auto-Attack Twofold Haste
    # Enhancement("", 427, 434, 0, M, [], skillIcon=0) # Starting Ouroboros Powers
    # # Enhancement("", 422, 0, 0, M, [], [], skillIcon=0) # <C7118AF0>
    # # Enhancement("", 423, 0, 0, M, [], skillIcon=0) # <EBFBFD29>
    # # Enhancement("", 420, 0, 0, M, [], skillIcon=0) # <378C7FD9>

CreateEnhancements()