# KP_list has the models
import IDs, json, random, Options
from scripts import JSONParser, Helper, PopupDescriptions

def Trades():
    
    types = {
        2 : [], # Weapon
        3 : [], # Gem
        4 : [], # Head
        5 : [], # Body
        6 : [], # Arm
        7 : [], # Waist
        8 : [], # Leg
       10 : [], # Collectable
       11 : []  # Material
    }
    
    isWpn = Options.TradeOption_Weapon.GetState()
    isArmor = Options.TradeOption_Armor.GetState()
    isGem = Options.TradeOption_Gem.GetState()
    isCol = Options.TradeOption_Collectibles.GetState()
    isMat = Options.TradeOption_Materials.GetState()
    
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itemFile:
        itemData = json.load(itemFile)
        for item in itemData["rows"]:
            try:
                types[item["itemType"]].append(item["$id"])
            except:
                pass # Ignore the groups we're not using for trades   
    
    
    
    for file in IDs.areaFileListNumbers:
        try:   
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/exchangelist{file}.json", 'r+', encoding='utf-8') as tradeNPCFile:
                tradeNPCData = json.load(tradeNPCFile)
                
                for trade in tradeNPCData["rows"]:
                    
                    trade["wpn1"] = RandomTradeVerification(types[2], trade["wpn1"], isWpn)

                    trade["head1"] = RandomTradeVerification(types[4], trade["head1"], isArmor)
                    trade["body1"] = RandomTradeVerification(types[5], trade["body1"], isArmor)
                    trade["arm1"] = RandomTradeVerification(types[6], trade["arm1"], isArmor)
                    trade["waist1"] = RandomTradeVerification(types[7], trade["waist1"], isArmor)
                    trade["legg1"] = RandomTradeVerification(types[8], trade["legg1"], isArmor)
                        
                        
                    trade["kessyou1"] = RandomTradeVerification(types[3], trade["kessyou1"], isGem)
                    trade["kessyou2"] = RandomTradeVerification(types[3], trade["kessyou2"], isGem)
                    
                    trade["collect1"] = RandomTradeVerification(types[10], trade["collect1"], isCol)
                    trade["collect2"] = RandomTradeVerification(types[10], trade["collect2"], isCol)
                    
                    trade["materia1"] = RandomTradeVerification(types[11], trade["materia1"], isMat)
                    trade["materia2"] = RandomTradeVerification(types[11], trade["materia2"], isMat)
                        
                
                JSONParser.CloseFile(tradeNPCData, tradeNPCFile)
        except:
            pass


def RandomTradeVerification(typeChoice, trade, isOn):
    if isOn:
        if trade == 0: # Only fill out slots that previously had trades
            return 0
        return random.choice(typeChoice)
    
def NPCTradesDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TradeOption.name)
    myDesc.Text("Randomizes the trades NPCs make. Only the chosen suboptions will be randomized.\nThe categories will stay the same so gems will always be replaced with gems etc.")
    myDesc.Image("rondinecap.png", "XCDE", 800)
    return myDesc