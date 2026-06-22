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
    isAllowDupes = not Options.CharacterOption_Duplicates.GetState()
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
    amrFile.Close()

def GetArmorFlags(armor):
    flags = 0
    parts = ["Head", "Body", "Arm_R", "Arm_L", "Legs"]
    for part in parts:
        flags = flags << 1 
        flags = flags | armor[f"PartsBit({part})"]
    return flags

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
            if wep["$id"] not in IDs.MeleeWeaponIDs + IDs.RangedWeaponIDs:
                continue
            if wep["TypeWpn"] != weaponType: # matches weapon type
                continue
            if wep["EquLv"] > maxLv or wep["EquLv"] < minLv: # if within the level range
                continue
            allowedWeapons.append(wep["$id"])
            
        return Helper.random.choice(allowedWeapons) # Return a random choice's id
                
    def GetBalancedArmor(targetGearID, armorPiecemeal, armorType):
        female = 2
        male = 1
        
        # Generate Allowed Armors
        allowedArmors = []
        for amr in amrFile.rows: 
            # Only use valid armors
            if amr["$id"] not in IDs.ArmorIDs:
                continue
            # Use the same type of armor
            if amr["TypeAmr"] != armorType:
                continue
            # stay within the level range
            if amr["EquLv"] > maxLv or amr["EquLv"] < minLv: 
                continue
            # Remove armors that cannot be chosen with the current armor flags already set
            if (armorPiecemeal & GetArmorFlags(amr)) != 0:
                continue
            # Keep armors to allowed genders
            if amr["EquPc02"] == 0 and newChar["Sex"] == female: 
                continue
            if amr["EquPc01"] == 0 and newChar["Sex"] == male:
                continue
            allowedArmors.append(amr)
        
        if len(allowedArmors) == 0:
            return 0, armorPiecemeal
        
        # Choose valid armor
        chosenArmor = Helper.random.choice(allowedArmors)
        
        # Set flags that the armor takes spots
        return chosenArmor["$id"], armorPiecemeal | GetArmorFlags(chosenArmor) # add with bitwise or
               
    armorPiecemeal = 0 # Updated when a slot is filled, needed to handle equipment that takes multiple slots
    for i in range(1,6):
        newChar[f"DefAmr{i}"] = 0 # Clear the original piece
        if (armorPiecemeal & pow(5-i, 2)): continue # Bitwise & on armorPiecemeal and the slot we are currently trying to fill to check if it is already filled. [Head, Body, Arm R, Arm L, Leg]
        newChar[f"DefAmr{i}"], armorPiecemeal = GetBalancedArmor(newChar[f"DefAmr{i}"], armorPiecemeal, i)
    newChar["DefWpnFar"] = GetBalancedWeapon(newChar["DefWpnFar"])
    newChar["DefWpnNear"] = GetBalancedWeapon(newChar["DefWpnNear"])


def PartyMemDesc(name, allowDupeName):
    from scripts import PopupDescriptions
    partyMemDesc = PopupDescriptions.Description()
    partyMemDesc.Header(name)
    partyMemDesc.Text("This randomizes the party members in the game. For example, In this picture Al has replaced Elma.")
    partyMemDesc.Image("charRando.png", "XCXDE", 500)
    partyMemDesc.Header(allowDupeName)
    partyMemDesc.Text("This allows copies of the party members, you could have a full team of Elma's.")
    return partyMemDesc