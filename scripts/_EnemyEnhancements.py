import json, random
from Enhancements import *

class EnemyEnhancement:
    pass



Nope = [MaxAffinityHeal,ReduceDamageFromNearbyEnemies, DamageUpOnEnemyKill] # Retry these used on armu enemy with dupe

def EnemyStats(spinBox):
    prevNames = []
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as EnParamFile:
            with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
                EnArr = json.load(EnArrangeFile)
                EnPar = json.load(EnParamFile)
                Names = json.load(NamesFile)
                
                
                for Enemy in EnArr["rows"]:
                    if spinBox >= random.randint(0,100):
                           
                        enh = random.choice(ValidSkills)
                        prevNames.append({"myName" :Enemy["Name"], "myEnhance": enh})
                        
                        for pair in prevNames: # Ensures the same name has the same enhancement
                            if pair["myName"] == Enemy["Name"]:
                                enh = pair["myEnhance"]
                                break
                            
                            

                        enh.RollEnhancement()                        
                        Enemy["EnhanceID3"] = enh.id
                        
                        for name in Names["rows"]: # Changes Names
                            if name["$id"] == Enemy["Name"]:
                                oldName = name["name"]
                                enhanceName = enh.name +  ('+'*(enh.Rarity))
                                if len(enhanceName + oldName) > 20:
                                    oldnameList = oldName.split()
                                    oldName = oldnameList[-1]           
                                name["name"] = f"[System:Color name=tutorial]{enhanceName}[/System:Color] {oldName}"
                                break

                
                NamesFile.seek(0)
                NamesFile.truncate()
                json.dump(Names, NamesFile, indent=2, ensure_ascii=False)
            EnParamFile.seek(0)
            EnParamFile.truncate()
            json.dump(EnPar, EnParamFile, indent=2, ensure_ascii=False)
        EnArrangeFile.seek(0)
        EnArrangeFile.truncate()
        json.dump(EnArr, EnArrangeFile, indent=2, ensure_ascii=False)
        
        
Healthy = Enhancement("Health", HPBoost.EnhanceEffect, 0, [50,100,150,200], addToList=False)
Strong = Enhancement("Strength", StrengthBoost.EnhanceEffect, 0, [50,100,150,200], addToList=False)
Etheras = Enhancement("Ether", EtherBoost.EnhanceEffect, 0,[50,100,150,200], addToList=False)
Dextrous = Enhancement("Dex", DexBoost.EnhanceEffect, 0, [75,150,200,300], addToList=False)
Agility = Enhancement("Agility", AgiBoost.EnhanceEffect, 0, [200,400,600,800], addToList=False)
Luck = Enhancement("Luck", LuckBoost.EnhanceEffect, 0 , [100,200,300,400], addToList=False)
EtherBlock = Enhancement("E Def", FlatEthDefBoost.EnhanceEffect, 0, [30,60,90,100], addToList=False)
PhyBlock = Enhancement("P Def", FlatDefBoost.EnhanceEffect, 0, [30,60,90,100], addToList=False)
Spike = Enhancement("Spiky", EtherCounter.EnhanceEffect, 0, [10,20,30,40], addToList=False)
Pursuer = Enhancement("Pursuer", CombatSpeed.EnhanceEffect, 0, [100,200,300,400], addToList=False)
AllReactionNull = Enhancement("Stable", TranquilGuard.EnhanceEffect, 0,[20,40,60,80], addToList=False)
BlowdownSpike = Enhancement("Bouncy", GravityPinwheel.EnhanceEffect, 0, [5,10,15,20], [1,2,3,5], addToList=False)
TasSnack = Enhancement("Devourer", TastySnack.EnhanceEffect, 0, [10,20,30,50], addToList=False)
BladeComboResist = Enhancement("Combo Resist", ReduceEnemyBladeComboDamage.EnhanceEffect,0, [30,50,70,100], addToList=False)
Desperate = Enhancement("Desperate", DamageUpWhenHpDown.EnhanceEffect,0,[10,15,20,25],[300,400,500,600], addToList=False)
Wish = Enhancement("Wish", WhenDiesHealAllies.EnhanceEffect, 0,[20,40,60,80], addToList=False)
FirstStrike = Enhancement("Suprise", FirstArtDamage.EnhanceEffect,0,[300,500,600,700], addToList=False)
Lightning  = Enhancement("Lightning", AutoSpeedArtsSpeed.EnhanceEffect, 0,[300,400,500,600],[200,300,400,500], addToList=False)
# Regen = Enhancement("Regenerate",TakeDamageHeal.EnhanceEffect,0,[1,2,3,4], addToList=False, DisTag="Regen" )
Repeat =Enhancement("Repeat", DidIDoThat.EnhanceEffect, 0,[30,50,70,90], addToList=False) # might use doesnt ring a bell
# Steamroll = Enhancement("Moxie", DamageUpOnEnemyKill.EnhanceEffect, 0, [50,100,150,200], addToList=False, DisTag="Strength Boost")
Enraged = Enhancement("Friendship", AllyDownDamageUp.EnhanceEffect, 0, [50,100,150,200], addToList=False)






ValidSkills = [Healthy, Strong, Etheras, Dextrous, Agility, Luck, EtherBlock, PhyBlock, Spike,Enraged,Repeat,Lightning,FirstStrike,TasSnack,Desperate,Twang,BladeComboResist,Transmigration,AnnulDef,BlowdownSpike,AllReactionNull, Pursuer,Wish] # Phy counter not working weird ill make my own special enhancements for enemies
Testing = []