# KP_list has the models
import IDs, json, random, Options
from scripts import JSONParser, Helper

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
                pass # Ignore the groups were not using for trades   
    
    
    
    for file in IDs.areaFileListNumbers:
        try:   
            with open(f"./XCDE/_internal/JsonOutputs/bdat_ma{file}/exchangelist{file}.json", 'r+', encoding='utf-8') as tradeNPCFile:
                tradeNPCData = json.load(tradeNPCFile)
                
                for trade in tradeNPCData["rows"]:
                    
                    if isWpn:
                        trade["wpn1"] = random.choice(types[2])
                        
                    if isArmor:
                        trade["head1"] = random.choice(types[4])
                        trade["body1"] = random.choice(types[5])
                        trade["arm1"] = random.choice(types[6])
                        trade["waist1"] = random.choice(types[7])
                        trade["legg1"] = random.choice(types[8])
                    
                    if isGem:
                        trade["kessyou1"] = random.choice(types[3])
                        trade["kessyou2"] = random.choice(types[3])
                        
                    if isCol:
                        trade["collect1"] = random.choice(types[10]) 
                        trade["collect2"] = random.choice(types[10]) 
                        
                    if isMat:
                        trade["material1"] = random.choice(types[11])
                        trade["material2"] = random.choice(types[11])
                        
                
                JSONParser.CloseFile(tradeNPCData, tradeNPCFile)
        except:
            pass
            