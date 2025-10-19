from XC2.XC2_Scripts import Options, IDs
import json, random
from scripts import Helper, PopupDescriptions, JSONParser, Values

valTable = Values.ValueTable()

def RandomizeAccessoryShops():
    AccessoryValTable = Values.ValueTable()
    AccessoryValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"))
    # Choose an Accessory of similar value to replace a shop item (With some variance)



def PopulateValueCalcXC2():
    files = [
        Values.ValueFile("ITM_Orb"),
        Values.ValueFile("ITM_OrbEquip"),
        Values.ValueFile("ITM_PcEquip"),
        Values.ValueFile("ITM_PreciousList"),
        Values.ValueFile("ITM_PreciousListIra"),
        Values.ValueFile("ITM_SalvageList"),
        Values.ValueFile("ITM_TresureList"),
        Values.ValueFile("ITM_PcWpnChip", mult=5),
        Values.ValueFile("ITM_CrystalList"),
        Values.ValueFile("ITM_BoosterList"),
        Values.ValueFile("ITM_CollectionList"),
        Values.ValueFile("ITM_FavoriteList"),
        Values.ValueFile("ITM_HanaAssist", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaArtsEnh", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaAtr", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaNArtsSet", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaRole", key="NeedEther", mult=3),
        Values.ValueFile("ITM_InfoList"),  
    ]
    for file in files:
        valTable.PopulateValues(file)

def ItemRando(): # Randomizes everything
    if valTable.isEmpty():
        PopulateValueCalcXC2()
    # Open files
    # Loop through desired things
    # Evaluate them
    # Clear them
    # Put new items in them
    # Close
    
def TreasureBoxRando():

    CreateCTMCDescriptions()
    for area in IDs.ValidTboxMapNames:
        areaBoxes = []
        with open(area, 'r+', encoding='utf-8') as tboxFile:
            tboxData = json.load(tboxFile)
            for box in tboxData["rows"]:
                goldVal = originalGoldVal = EvaluateTboxGoldValue(box)
                ClearTbox(box)
                
                while goldVal > 0: # While the goldVal > 0 
                    chosenItem = valTable.SelectRandomMember()  # Pick an item with less value than the total val of the box to put in the box
                    goldVal -= chosenItem.value # Subtract that from the goldVal
                    # Find empty spot if box is full then ignore
                    for i in range(1,9):
                        if box[f"itm{i}ID"] == 0:
                            box[f"itm{i}ID"] = chosenItem.id
                            break
                        break # If all spots are full break
            
                # areaBoxes.append(goldVal)
                box["RSC_ID"] = GetRarity(originalGoldVal - goldVal) # based on median values of the area
                
            JSONParser.CloseFile(tboxData, tboxFile)
        
class TreasureBox(Values.ValueContainer):

    def ClearContainer(tbox):
        tbox["goldMin"] = 0    
        tbox["goldMax"] = 0    
        tbox["goldPopMin"] = 0    
        tbox["goldPopMax"] = 0  
        
        for i in range(1,9):
            if tbox[f"itm{i}ID"] in IDs.PreciousItems + IDs.TornaPreciousIDs + [0]: # Dont clear precious items
                continue
            tbox[f"itm{i}ID"] = 0

    def GetContainerValue(tbox):
        totalVal = 0
        
        # Gold
        avgGold = (tbox["goldMin"] + tbox["goldMax"])/2
        totalVal += avgGold
        
        # Items
        for i in range(1,9):
            itemID = tbox[f"itm{i}ID"]
            
            if itemID == 0: # Ignore empty slots
                continue
            
            item:Values.ValuedItem = valTable.GetByID(itemID)
            if item:
                amount = tbox[f"itm{i}Num"]
                totalVal += (item.value * amount)

        return int(totalVal)    

class EnemyDrops(Values.ValueContainer):

    def ClearContainer(drops):
        for i in range(1,9):
            if drops[f"ItemID{i}"] in IDs.TornaPreciousIDs + IDs.PreciousItems + [0]:
                continue
            drops[f"ItemID{i}"] = 0

    def GetContainerValue(drops):
        for i in range(1,9):
            itemID = drops[f"ItemID{i}"]
            if itemID == 0: # Ignore empty slots
                continue
            
            item:Values.ValuedItem = valTable.GetByID(itemID)
            if item:
                amount = drops[f"itm{i}Num"]
                totalGold += (item.value * amount)

        return int(totalGold)    


    
def CreateCTMCDescriptions(): # Hardcoded New Boxes and descriptions
    class CreditRarityRelation():
        def __init__(self, name, rscId, credits, msId):
            self.name = name
            self.rscId = rscId # RSC ID of the chest
            self.credits = credits # credits to belong to this category
            self.msId = msId
    
    Common = CreditRarityRelation("Common", 1, 100, 154)
    Rare = CreditRarityRelation("Rare", 2, 200, 155)
    Legendary = CreditRarityRelation("Legendary", 3, 300, 156)
    
    with open("XC2/JsonOutputs/common_ms/fld_gmkname.json", 'r+', encoding='utf-8') as nameFile:
        nameData = json.load(nameFile)
        nameData["rows"].append({"$id": Common.msId, "style": 36, "name": Common.name})
        nameData["rows"].append({"$id": Rare.msId, "style": 36, "name": Rare.name})
        nameData["rows"].append({"$id": Legendary.msId, "style": 36, "name": Legendary.name})
        JSONParser.CloseFile(nameData, nameFile)
            
    with open("XC2/JsonOutputs/common/RSC_TboxList.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            box["initWaitTimeRand"] = 0.1 # reduces wait time for chest down to 0.1 sec
            if box["$id"] == Common.rscId:
                box["MSG_ID"] = Common.msId
            elif box["$id"] == Rare.rscId:
                box["MSG_ID"] = Rare.msId
            elif box["$id"] == Legendary.rscId:
                box["MSG_ID"] = Legendary.rscId
            else:
                break
        JSONParser.CloseFile(tboxData, tboxFile)

def GetRarity(gold):
    if gold < 5000:
        return 1
    elif gold < 10000:
        return 2
    else:
        return 3

def RandoTreasureBoxes():
    ValidReplacements = []
    if not Options.RaceModeOption.GetState(): # if race mode is on, we don't want to do any of this
        if Options.TreasureChestOption_Accessories.GetState():
            ValidReplacements.extend(IDs.AccessoryIDs)
        if Options.TreasureChestOption_TornaAccessories.GetState():
            ValidReplacements.extend(IDs.TornaAccessories)
        if Options.TreasureChestOption_WeaponChips.GetState():
            ValidReplacements.extend(IDs.WeaponChipIDs)
        if Options.TreasureChestOption_AuxCores.GetState():
            ValidReplacements.extend(IDs.AuxCoreIDs)
        if Options.TreasureChestOption_RefinedAuxCores.GetState():
            ValidReplacements.extend(IDs.RefinedAuxCores)
        if Options.TreasureChestOption_CoreCrystals.GetState() and not Options.CustomCoreCrystalOption.GetState():
                ValidReplacements.extend(IDs.CoreCrystals)
        if Options.TreasureChestOption_Deeds.GetState():
            if not Options.StartwithIncreasedMovespeedOption.GetState(): # if we have the bonus movespeed starting deed on, we want to exclude it from the deeds found in chests.
                ValidReplacements.extend(IDs.Deeds)
            else:
                ValidReplacements.extend(Helper.InclRange(25250, 25300))
        if Options.TreasureChestOption_CollectionPointMaterials.GetState():
            ValidReplacements.extend(IDs.CollectionPointMaterials)
    odds = Options.TreasureChestOption.GetSpinbox()

    if ValidReplacements == []: # In case they dont select anything
        return
    
    for area in IDs.MajorAreaIds:
        try:
            with open(f"./XC2/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as tboxFile:
                boxData = json.load(tboxFile)
                for box in boxData["rows"]:
                    for i in range(1,9):
                        if not Helper.OddsCheck(odds): # Check spinbox
                            continue
                        if box[f"itm{i}ID"] in [0] + IDs.PreciousItems: # Ignore empty spots in points
                            continue
                        box[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
                tboxFile.seek(0)
                tboxFile.truncate()
                json.dump(boxData, tboxFile, indent=2, ensure_ascii=False)
        except:
            pass # Ignores wrong files


def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option randomizes a % of all non-key items in Treasure Chests into the types of items chosen from suboptions.")
    myDesc.Text("If no sub-options are selected this will do nothing.")
    myDesc.Image("TreasureChest.png", "XC2")
    return myDesc