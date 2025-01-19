import json, random
from Enhancements import *


Nope = [MaxAffinityHeal,ReduceDamageFromNearbyEnemies, DamageUpOnEnemyKill] # Retry these used on armu enemy with dupe
ValidSkills = []   


def EnemyStats(spinBox):
    prevNames = []
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as EnParamFile:
            with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
                EnArr = json.load(EnArrangeFile)
                EnPar = json.load(EnParamFile)
                Names = json.load(NamesFile)
                
                
                for Enemy in EnArr["rows"]:
                    if spinBox > random.randrange(0,100):
                           
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
        
class EnemyEnhancement(Enhancement):
    def __init__(self, name, enhancement, para1 = [0,0,0,0],para2 = [0,0,0,0]):
        self.name = name
        self.EnhanceEffect = enhancement.EnhanceEffect
        self.Caption = 0
        self.addToList = False
        self.Param1 = para1
        self.Param2 = para2
        ValidSkills.append(self)
   
Healthy = EnemyEnhancement("Health", HPBoost, [50,100,150,200])
Strong = EnemyEnhancement("Strength", StrengthBoost, [50,100,150,200])
Etheras = EnemyEnhancement("Ether", EtherBoost, [50,100,150,200])
Dextrous = EnemyEnhancement("Dex", DexBoost, [75,150,200,300])
Agility = EnemyEnhancement("Agility", AgiBoost, [200,400,600,800])
Luck = EnemyEnhancement("Luck", LuckBoost, [100,200,300,400])
EtherBlock = EnemyEnhancement("E Def", FlatEthDefBoost, [30,60,90,100])
PhyBlock = EnemyEnhancement("P Def", FlatDefBoost, [30,60,90,100])
Spike = EnemyEnhancement("Spiky", EtherCounter, [10,20,30,40])
Pursuer = EnemyEnhancement("Pursuer", CombatSpeed, [100,200,300,400])
AllReactionNull = EnemyEnhancement("Stable", TranquilGuard,[20,40,60,80])
BlowdownSpike = EnemyEnhancement("Bouncy", GravityPinwheel, [10,20,30,40], [1,2,3,5])
TasSnack = EnemyEnhancement("Devourer", TastySnack, [10,20,30,50])
BladeComboResist = EnemyEnhancement("Combo Resist", ReduceEnemyBladeComboDamage, [30,50,70,100])
Desperate = EnemyEnhancement("Desperate", DamageUpWhenHpDown,[10,15,20,25],[300,400,500,600])
Wish = EnemyEnhancement("Wish", WhenDiesHealAllies,[20,40,60,80])
FirstStrike = EnemyEnhancement("Suprise", FirstArtDamage,[300,500,600,700])
Lightning  = EnemyEnhancement("Lightning", AutoSpeedArtsSpeed,[300,400,500,600],[200,300,400,500])
Repeat = EnemyEnhancement("Repeat", DidIDoThat,[30,50,70,90])
Enraged = EnemyEnhancement("Friendship", AllyDownDamageUp,[30,60,90,120])









