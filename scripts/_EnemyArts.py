import json, random
from Enhancements import *

common = 0
rare = 1
legendary = 2

def EnemyStats(spinBox):
    with open("./_internal/JsonOutputs/common/BTL_Arts_En.json", 'r+', encoding='utf-8') as EnArtsFile:
        with open("./_internal/JsonOutputs/common_ms/btl_arts_en_ms.json", 'r+', encoding='utf-8') as NamesFile:      
            enArtsData = json.load(EnArtsFile)
            nameData = json.load(NamesFile)
            newNameID = 457 # Starting id to add new names to old names file
            for art in enArtsData["rows"]:
                if spinBox < random.randrange(0,100): # Spinbox value check
                    continue
                if art["Name"] == 0: # Avoid changing autoattacks and things with no name
                    continue
                
                newNameID += 1
                rarity = random.choice(common,common,common,rare,rare,legendary) # choose rarity
                validChanges = FindValidChanges(art, rarity)  # i dont want to overwrite previous behaviour so check what i can change on an art
                myChange = random.choice(validChanges) # choose a change to apply
                changeName = myChange()
                
                for name in nameData["rows"]: # Get the old name
                    if name == art["Name"]:
                        oldName = name["name"]
                        break
                        
                
                art["Name"] =  newNameID # Set new name id
                newName = {
                    "$id" : newNameID,
                    "style" : 15,
                    "name" : f"{changeName} {oldName}"
                }
                nameData.extend
                


                # AOE
                # Buff
                # Debuff
                # Damage Type
                # Reaction
                # Cooldown
                # Enhancement
                # Name (Make new name id)
                
                    
                    
                
                # for name in nameData["rows"]: # Changes Names
                #     if name["$id"] == art["Name"]:
                #         oldName = name["name"]
                #         enhanceName = enh.name +  ('+'*(enh.Rarity))
                #         if len(enhanceName + oldName) > 20:
                #             oldnameList = oldName.split()
                #             oldName = oldnameList[-1]           
                #         name["name"] = f"[System:Color name=tutorial]{enhanceName}[/System:Color] {oldName}"
                #         break

            
            NamesFile.seek(0)
            NamesFile.truncate()
            json.dump(nameData, NamesFile, indent=2, ensure_ascii=False)
        EnArtsFile.seek(0)
        EnArtsFile.truncate()
        json.dump(enArtsData, EnArtsFile, indent=2, ensure_ascii=False)
        
# class EnemyArtEnhancement(Enhancement):
#     def __init__(self, name, enhancement, para1 = [0,0,0,0],para2 = [0,0,0,0]):
#         self.name = name
#         self.EnhanceEffect = enhancement.EnhanceEffect
#         self.Caption = 0
#         self.addToList = False
#         self.Param1 = para1
#         self.Param2 = para2
#         ValidSkills.append(self)
   
   
def FindValidChanges(art, rarity):
    ValidChanges = []
    if art["Recast"] not in [0]:
        ValidChanges.append(lambda: Cooldown(art, rarity))
    return ValidChanges


def Cooldown(art, rarity): 
    if rarity == common:
        div = 2
    elif rarity == rare:
        div = 4
    elif rarity == legendary:
        div = 6
    
    art["Recast"] //= div
    return [f"CD{"↓" * rarity + 1}"]






