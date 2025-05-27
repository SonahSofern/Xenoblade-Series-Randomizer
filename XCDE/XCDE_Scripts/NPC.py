# KP_list has the models
import IDs, json, random, Options
from scripts import JSONParser, Helper, PopupDescriptions

def Trades():
    
    # types = {
    #     4 : IDs.HeadIDs, # Head
    #     5 : IDs.ChestIDs, # Body
    #     6 : IDs.ArmIDs, # Arm
    #     7 : IDs.WaistIDs, # Waist
    #     8 : IDs.LegIDs, # Leg
    # }
    
    isWpn = Options.TradeOption_Weapon.GetState()
    isArmor = Options.TradeOption_Armor.GetState()
    isGem = Options.TradeOption_Gem.GetState()
    isCol = Options.TradeOption_Collectibles.GetState()
    isMat = Options.TradeOption_Materials.GetState()
    
    # with open(f"./XCDE/_internal/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itemFile:
    #     itemData = json.load(itemFile)
    #     for item in itemData["rows"]:
    #         if item["$id"] not in IDs.ArmorIDs:
    #             continue
    #         try:
    #             types[item["itemType"]].append(item["$id"])
    #         except:
    #             pass # Ignore the groups we're not using for trades   
    #     print(f"Head: {types[4]}")
    #     print(f"Chest:  {types[5]}")
    #     print(f"Arm:  {types[6]}")
    #     print(f"Waist:  {types[7]}")
    #     print(f"Leg:  {types[8]}")
    
    #
    for file in IDs.areaFileListNumbers:
        try:   
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/exchangelist{file}.json", 'r+', encoding='utf-8') as tradeNPCFile:
                tradeNPCData = json.load(tradeNPCFile)
                
                for trade in tradeNPCData["rows"]:
                    
                    trade["wpn1"] = RandomTradeVerification(IDs.WeaponIDs, trade["wpn1"], isWpn)

                    trade["head1"] = RandomTradeVerification(IDs.HeadIDs, trade["head1"], isArmor)
                    trade["body1"] = RandomTradeVerification(IDs.ChestIDs, trade["body1"], isArmor)
                    trade["arm1"] = RandomTradeVerification(IDs.ArmIDs, trade["arm1"], isArmor)
                    trade["waist1"] = RandomTradeVerification(IDs.WaistIDs, trade["waist1"], isArmor)
                    trade["legg1"] = RandomTradeVerification(IDs.LegIDs, trade["legg1"], isArmor)
                        
                        
                    trade["kessyou1"] = RandomTradeVerification(IDs.GemIDs, trade["kessyou1"], isGem)
                    trade["kessyou2"] = RandomTradeVerification(IDs.GemIDs, trade["kessyou2"], isGem)
                    
                    trade["collect1"] = RandomTradeVerification(IDs.CollectableIDs, trade["collect1"], isCol)
                    trade["collect2"] = RandomTradeVerification(IDs.CollectableIDs, trade["collect2"], isCol)
                    
                    trade["materia1"] = RandomTradeVerification(IDs.MaterialIDs, trade["materia1"], isMat)
                    trade["materia2"] = RandomTradeVerification(IDs.MaterialIDs, trade["materia2"], isMat)
                        
                
                JSONParser.CloseFile(tradeNPCData, tradeNPCFile)
        except:
            pass

def NPCModelRando():
    odds = Options.NPCModelsOption.GetSpinbox()
    ObjectList = []
    dontReplace = Helper.InclRange(655,680) + [650,651]
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/KP_list.json", 'r+', encoding='utf-8') as lmFile:
        lmData = json.load(lmFile)
        for lm in lmData["rows"]:
            if (lm["$id"] in dontReplace) or (not (lm["model"].startswith("en") or lm["model"].startswith("np"))):
                continue
            ObjectList.append([lm["model"], lm["motion"], lm["action"], lm["effect"], lm["sound"]])

        for lm in lmData["rows"]:
            if lm["$id"] in dontReplace or (not lm["model"].startswith("np")):
                continue
            if not Helper.OddsCheck(odds):
                continue
                
            choice = random.choice(ObjectList)
            lm["model"] = choice[0]
            lm["motion"] = choice[1]
            lm["action"] = choice[2]
            lm["effect"] = choice[3]
            lm["sound"] = choice[4]   
            # lm["model"] = 	"np020201"				
            # lm["motion"] = "mn020101"
            # lm["action"] = "mn020208"
            # lm["effect"] = ""
            # lm["sound"] = "sn302701"               
        JSONParser.CloseFile(lmData, lmFile)


def RandomTradeVerification(typeChoice, trade, isOn):
    if isOn:
        if trade == 0: # Only fill out slots that previously had trades
            return 0
        return random.choice(typeChoice)
    else:
        return trade
    
def NPCTradesDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TradeOption.name)
    myDesc.Text("Randomizes the trades NPCs make. Only the chosen suboptions will be randomized.\nThe categories will stay the same so helms will always replace helms and so on.")
    myDesc.Image("rondinecap.png", "XCDE", 800)
    return myDesc

