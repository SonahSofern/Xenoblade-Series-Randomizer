import json
from XCXDE.XCXDE_Scripts import IDs, Options

from scripts import JSONParser, Helper

# Starting Gear
# 

def Members():
    charFile = JSONParser.File("XCXDE/JsonOutputs/common/DEF_PcList.json")
    wpnFile = JSONParser.File("XCXDE/JsonOutputs/common/WPN_PcList.json")
    amrFile = JSONParser.File("XCXDE/JsonOutputs/common/AMR_PcList.json")
    
    testGroup = Helper.RandomGroup()
    testGroup.GenData(charFile.rows, lambda e: e["$id"] in IDs.PartyMembersIDs)
    isAllowDupes = Options.CharacterOption_Duplicates.GetState()
    isBalanceGear = Options.CharacterOption_BalanceGear.GetState()
    for char in charFile.rows:
        if char["$id"] not in IDs.PartyMembersIDs:
            continue
        newChar = testGroup.SelectRandomMember(isAllowDupes)
        if isBalanceGear:
            BalanceStartingGear(char["Lv"], newChar, wpnFile, amrFile)
        Helper.CopyKeys(char, newChar, ["$id", "Lv", "InitBp"]) # Keep original Level and Bp for balancing
        
    charFile.Close()
    wpnFile.Close()


def BalanceStartingGear(targetLv, newChar, wpnFile:JSONParser.File, amrFile:JSONParser.File):
    '''Balance the starting gear since high level characters would be very strong and have gear they were underleveled for'''
    # Find all weapons within 10 levels below users level capped at 60
    minLv = min(targetLv - 10, 60)
    maxLv = targetLv
    
    # Get weaponType
    def GetBalancedWeapon(targetWepID):
        # Get Weapon Type
        for wep in wpnFile.rows: 
            if wep["$id"] == targetWepID:
                weaponType = wep["TypeWpn"]
                break
        
        allowedWeapons = []
        for wep in wpnFile.rows: # get similar weapons
            if wep["TypeWpn"] != weaponType: # matches weapon type
                continue
            if wep["EquLv"] > maxLv or wep["EquLv"] < minLv: # if within the level range
                continue
            allowedWeapons.append(wep["$id"])
            
        return Helper.random.choice(allowedWeapons)["$id"] # Return a random choice's id
            
    armorPiecemeal = [0,0,0,0,0] # Updated when a slot is filled, needed to handle equipment that takes multiple slots
    
    # Equip Level at the level of the member, grab the same type of weapon / gear and ensure gender can equip it
    def GetBalancedArmor(targetGearID):
        
        # Account for bodysuits need to look at flags
        female = 2
        male = 1
        
        # Get Gear Type
        for amr in amrFile.rows: 
            if amr["$id"] == targetGearID:
                armorType = amr["TypeAmr"]
                break
            
        
        allowedArmors = []
        for amr in amrFile.rows: 
            # Keep armors to allowed genders
            if amr["EquPc02"] == 0 and newChar["Sex"] == female: 
                continue
            if amr["EquPc01"] == 0 and newChar["Sex"] == male:
                continue
            # Keep the same type of armor
            if amr["TypeAmr"] != armorType:
                continue
            allowedArmors.append(amr)
            
        chosenArmor = Helper.random.choice(allowedArmors)
        
        # Set flags that the armor takes spots
            
        return 
               

    # "PartsBit(Head)": 0,
    #   "PartsBit(Body)": 0,
    #   "PartsBit(Arm_R)": 1,
    #   "PartsBit(Arm_L)": 0,
    #   "PartsBit(Legs)": 0,
    for i in range(1,6):
        newChar[f"DefAmr{i}"] = GetBalancedArmor(newChar[f"DefAmr{i}"])["$id"]
    newChar["DefWpnFar"] = GetBalancedWeapon(newChar["DefWpnFar"])
    newChar["DefWpnNear"] = GetBalancedWeapon(newChar["DefWpnNear"])

