import json, random
from Enhancements import *
import Options

Nope = [MaxAffinityHeal,ReduceDamageFromNearbyEnemies, DamageUpOnEnemyKill] # Retry these used on armu enemy with dupe
ValidSkills = []   


def EnemyEnhances():
    prevNames = []
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./XC2/_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
            EnArr = json.load(EnArrangeFile)
            Names = json.load(NamesFile)
            spinbox  = Options.EnemyEnhancementsOption.GetOdds()
            for Enemy in EnArr["rows"]:
                if spinbox < random.randrange(0,100):
                    continue
                        
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
        EnArrangeFile.seek(0)
        EnArrangeFile.truncate()
        json.dump(EnArr, EnArrangeFile, indent=2, ensure_ascii=False)
        
class EnemyEnhancement(Enhancement):
    def __init__(self, name, enhancement, para1 = [0,0,0,0],para2 = [0,0,0,0], revP1 = False, revp2 = False):
        self.name = name
        self.EnhanceEffect = enhancement.EnhanceEffect
        self.Caption = 0
        self.addToList = False
        self.Param1 = para1
        self.Param2 = para2
        self.ReversePar1 = revP1
        self.ReversePar2 = revp2
        ValidSkills.append(self)
   
Healthy = EnemyEnhancement("Healthy", HPBoost, [100,150,200,300])
Strong = EnemyEnhancement("Strong", StrengthBoost, [50,100,150,200])
Etheras = EnemyEnhancement("Etherite", EtherBoost, [50,100,150,200])
EtherBlock = EnemyEnhancement("E. Def", FlatEthDefBoost, [60,70,80,100])
PhyBlock = EnemyEnhancement("P. Def", FlatDefBoost, [60,70,80,100])
Spike = EnemyEnhancement("Spiky", EtherCounter, [30,40,50,60])
Pursuer = EnemyEnhancement("Pursuer", CombatMoveSpeed, [100,200,300,400])
AllReactionNull = EnemyEnhancement("Stable", TranquilGuard,[40,60,80,100])
BlowdownSpike = EnemyEnhancement("Bouncy", GravityPinwheel, [10,15,20,25], [1,2,3,5])
TasSnack = EnemyEnhancement("Devourer", TastySnack, [30,50,70,100])
Desperate = EnemyEnhancement("Desperate", HpDownDamageUp,[10,15,20,25])
Wish = EnemyEnhancement("Sacrificial", WhenDiesHealAllies,[50,70,80,100])
FirstStrike = EnemyEnhancement("Supriser", FirstArtDamage,[300,500,600,700])
Lightning  = EnemyEnhancement("Lightning", AutoSpeedArtsSpeed,[300,400,500,600],[200,300,400,500])
Repeat = EnemyEnhancement("Repeat", DidIDoThat,[20,40,60,80])
Enraged = EnemyEnhancement("Avenger", AllyDownDamageUp,[60,80,100,120])
Regen = EnemyEnhancement("Regen", PermaRegen,[30,60,90,120], [1,2,3,4], revP1=True)
CloseArmor = EnemyEnhancement("Guardian", ReduceDamageFromNearbyEnemies, [30,50,70,90])
Swarm = EnemyEnhancement("Swarming", PerAllyDamageUp, [20,40,60,80])
Sealing = EnemyEnhancement("Sealing", ChainAttackSeal, [1,1,2,3])

#New testing

# Not including
# BladeComboResist = EnemyEnhancement("Combo Resist", ReduceEnemyBladeComboDamage, [60,70,90,100])
# ChainHeal = EnemyEnhancement("Chain Heal", ChainAttackHeal, [50,60,70,80]) didnt work
# Warmup = EnemyEnhancement("Warmup", BattleDurationDamageUp, [70,100,120,150])
# Agility = EnemyEnhancement("Agile", AgiBoost, [100,200,300,400])








