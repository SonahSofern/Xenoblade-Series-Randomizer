import json, random
from Enhancements import *

class EnemyEnhancement:
    pass


Spike = Enhancement("Spiky", EtherCounter.EnhanceEffect, 0, [10,20,30,40], addToList=False)
Pursuer = Enhancement("Pursuer", CombatSpeed.EnhanceEffect, 0, [100,200,300,400], addToList=False, DisTag="Pursue")
AllReactionNull = Enhancement("Stable", TranquilGuard.EnhanceEffect, 0,[20,40,60,80], addToList=False, DisTag="Null React")
BlowdownSpike = Enhancement("Bouncy", GravityPinwheel.EnhanceEffect, 0, [5,10,15,20], [1,2,3,5], addToList=False,DisTag="Bounce")
TasSnack = Enhancement("Devourer", TastySnack.EnhanceEffect, 0, [10,20,30,50], addToList=False, DisTag="Devourer")
BladeComboResist = Enhancement("Combo Resist", ReduceEnemyBladeComboDamage.EnhanceEffect,0, [30,50,70,100], addToList=False, DisTag="Blade Combo Resist")
Desperate = Enhancement("Desperate", DamageUpWhenHpDown.EnhanceEffect,0,[10,15,20,25],[300,400,500,600], addToList=False, DisTag="Desperation Attack" )
Wish = Enhancement("Wish", WhenDiesHealAllies.EnhanceEffect, 0,[20,40,60,80], addToList=False, DisTag="Heal Allies")
FirstStrike = Enhancement("Suprise", FirstArtDamage.EnhanceEffect,0,[300,500,600,700], addToList=False, DisTag="Suprise Strike")
Lightning  = Enhancement("Lightning", AutoSpeedArtsSpeed.EnhanceEffect, 0,[300,400,500,600],[200,300,400,500], addToList=False)
# Regen = Enhancement("Regenerate",TakeDamageHeal.EnhanceEffect,0,[1,2,3,4], addToList=False, DisTag="Regen" )
Repeat =Enhancement("Repeat", DidIDoThat.EnhanceEffect, 0,[30,50,70,90], addToList=False, DisTag="Free Cooldown") # might use doesnt ring a bell
# Steamroll = Enhancement("Moxie", DamageUpOnEnemyKill.EnhanceEffect, 0, [50,100,150,200], addToList=False, DisTag="Strength Boost")
Enraged = Enhancement("Friendship", AllyDownDamageUp.EnhanceEffect, 0, [50,100,150,200], addToList=False, DisTag="Strength Boost")

ValidSkills = [Spike,Enraged,Repeat,Lightning,FirstStrike,TasSnack,Desperate,Twang,BladeComboResist,Transmigration, ReduceEnemyBladeComboDamage,AnnulDef,BlowdownSpike,AllReactionNull, Pursuer,Wish] # Phy counter not working weird ill make my own special enhancements for enemies
Testing = []

Nope = [MaxAffinityHeal,ReduceDamageFromNearbyEnemies, DamageUpOnEnemyKill] # These have been tried and dont work as far as I can tell

def EnemyStats(spinBox):
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as EnParamFile:
            with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
                EnArr = json.load(EnArrangeFile)
                EnPar = json.load(EnParamFile)
                Names = json.load(NamesFile)
                
                
                for Enemy in EnArr["rows"]:
                    if spinBox >= random.randrange(0,101):
                        enh = random.choice(ValidSkills)
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