import json, random
from XC2.XC2_Scripts.Enhancements import *
from XC2.XC2_Scripts import Options 
import scripts.PopupDescriptions


Nope = [MaxAffinityHeal,ReduceDamageFromNearbyEnemies, DamageUpOnEnemyKill] # Retry these used on armu enemy with dupe
ValidSkills = []   
MaxLettersInNameTag = 23


def EnemyEnhances():
    prevNames = []
    with open("./XC2/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./XC2/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
            EnArr = json.load(EnArrangeFile)
            Names = json.load(NamesFile)
            spinbox  = Options.EnemyEnhancementsOption.GetSpinbox()
            for Enemy in EnArr["rows"]:
                if spinbox < random.randrange(0,100):
                    continue
                        
                enh:Enhancement = random.choice(ValidSkills)
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
                        if len(enhanceName + oldName) > MaxLettersInNameTag:
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
    def __init__(self, name, enhancement, para1 = [0,0,0,0],para2 = [0,0,0,0], revP1 = False, revp2 = False, isRounded = True):
        self.name = name
        self.EnhanceEffect = enhancement.EnhanceEffect
        self.Caption = 0
        self.addToList = False
        self.Param1 = para1
        self.Param2 = para2
        self.ReversePar1 = revP1
        self.ReversePar2 = revp2
        self.isRounded = isRounded
        ValidSkills.append(self)
   
Healthy = EnemyEnhancement("Healthy", HPBoost, [100,150,200,300])
Strong = EnemyEnhancement("Strong", StrengthBoost, [50,100,150,200])
Etheras = EnemyEnhancement("Ether", EtherBoost, [50,100,150,200])
EtherBlock = EnemyEnhancement("E.Def", FlatEthDefBoost, [60,70,80,100])
PhyBlock = EnemyEnhancement("P.Def", FlatDefBoost, [60,70,80,100])
Spike = EnemyEnhancement("Spiky", EtherCounter, [30,40,50,60])
Pursuer = EnemyEnhancement("Pursuer", CombatMoveSpeed, [100,200,300,400])
AllReactionNull = EnemyEnhancement("Stable", TranquilGuard,[40,60,80,100])
BlowdownSpike = EnemyEnhancement("Bouncy", GravityPinwheel, [3,6,9,12], [1,2,3,5])
TasSnack = EnemyEnhancement("Devour", TastySnack, [30,50,70,100])
Desperate = EnemyEnhancement("Frenzy", HpDownDamageUp,[10,15,20,25])
Wish = EnemyEnhancement("Wish", WhenDiesHealAllies,[50,70,80,100])
FirstStrike = EnemyEnhancement("Ambush", FirstArtDamage,[300,500,600,700])
Lightning  = EnemyEnhancement("Fleet", AutoSpeedArtsSpeed,[300,400,500,600],[200,300,400,500])
Repeat = EnemyEnhancement("Repeat", DidIDoThat,[20,40,60,80])
Enraged = EnemyEnhancement("Avenge", AllyDownDamageUp,[60,80,100,120])
Regen = EnemyEnhancement("Regen", PermaRegen,[60,90,120,150], [0.01,0.015,0.02,0.03], revP1=True, isRounded=False)
CloseArmor = EnemyEnhancement("Solid", ReduceDamageFromNearbyEnemies, [30,50,70,90])
Swarm = EnemyEnhancement("Swarm", PerAllyDamageUp, [20,40,60,80])
Sealing = EnemyEnhancement("Seal", ChainAttackSeal, [2,2,2,3], revP1=True)

#New testing
TestSkills = [Regen]

# Not including
# BladeComboResist = EnemyEnhancement("Combo Resist", ReduceEnemyBladeComboDamage, [60,70,90,100])
# ChainHeal = EnemyEnhancement("Chain Heal", ChainAttackHeal, [50,60,70,80]) didnt work
# Warmup = EnemyEnhancement("Warmup", BattleDurationDamageUp, [70,100,120,150])
# Agility = EnemyEnhancement("Agile", AgiBoost, [100,200,300,400])

def EnemyEnhancementDescriptions():
    myDesc = scripts.PopupDescriptions.Description()
    myDesc.Header("Enemy Enhancements")
    myDesc.Text(f"Adds {len(ValidSkills)} possible enhancements to enemies, displayed like this.")
    myDesc.Image("NameTagEnhancement.png","XC2", 400)
    myDesc.Text("Each enhancement has 3 different strengths indicated by a +/++ after the enhancement name.")
    
    myDesc.Tag(Healthy.name, padx=0)
    myDesc.Text(f"Gives a % HP boost between {Healthy.Param1[0]}-{Healthy.Param1[3]}%")

    myDesc.Tag(Strong.name, padx=0)
    myDesc.Text(f"Gives a % Strength boost between {Strong.Param1[0]}-{Strong.Param1[3]}%")

    myDesc.Tag(Etheras.name, padx=0)
    myDesc.Text(f"Gives a % Ether boost between {Etheras.Param1[0]}-{Etheras.Param1[3]}%")

    myDesc.Tag(EtherBlock.name, padx=0)
    myDesc.Text(f"Gives a flat ether resist boost between {EtherBlock.Param1[0]}-{EtherBlock.Param1[3]}%")

    myDesc.Tag(PhyBlock.name, padx=0)
    myDesc.Text(f"Gives a flat physical resist boost between {PhyBlock.Param1[0]}-{PhyBlock.Param1[3]}%")

    myDesc.Tag(Spike.name, padx=0)
    myDesc.Text(f"Gives a spike for {Spike.Param1[0]}-{Spike.Param1[3]}% of ether stat (This is known to not work for some enemies)")

    myDesc.Tag(Pursuer.name, padx=0)
    myDesc.Text(f"Gives a movement speed boost in combat between {Pursuer.Param1[0]}-{Pursuer.Param1[3]}%")

    myDesc.Tag(AllReactionNull.name, padx=0)
    myDesc.Text(f"Gives a {AllReactionNull.Param1[0]}-{AllReactionNull.Param1[3]}% chance to negate incoming reactions (break, topple, launch, smash)")

    myDesc.Tag(BlowdownSpike.name, padx=0)
    myDesc.Text(f"Gives a lv {BlowdownSpike.Param2[0]}-{BlowdownSpike.Param2[3]} blowdown spike with odds of activating between {BlowdownSpike.Param1[0]}-{BlowdownSpike.Param1[3]}%")

    myDesc.Tag(TasSnack.name, padx=0)
    myDesc.Text(f"When this enemy defeats a driver it will heal {TasSnack.Param1[0]}-{TasSnack.Param1[3]}% of its max health.")

    myDesc.Tag(Desperate.name, padx=0)
    myDesc.Text(f"As their HP goes down they deal {Desperate.Param1[0]}-{Desperate.Param1[3]}% more damage linearly")

    myDesc.Tag(Wish.name, padx=0)
    myDesc.Text(f"Upon death heals all allies in the battle by {Wish.Param1[0]}-{Wish.Param1[3]}% of their max health")

    myDesc.Tag(FirstStrike.name, padx=0)
    myDesc.Text(f"Enemies' first attack of the battle deals {FirstStrike.Param1[0]}-{FirstStrike.Param1[3]}% bonus damage")

    myDesc.Tag(Lightning.name, padx=0)
    myDesc.Text(f"Enemy animations are sped up by {Lightning.Param1[0]}-{Lightning.Param1[3]}%")

    myDesc.Tag(Repeat.name, padx=0)
    myDesc.Text(f"Gives a {Repeat.Param1[0]}-{Repeat.Param1[3]}% chance to not put arts and attacks on cooldown when used.")

    myDesc.Tag(Enraged.name, padx=0)
    myDesc.Text(f"Each enemy that dies increases this enemy's damage by {Enraged.Param1[0]}-{Enraged.Param1[3]}%")

    myDesc.Tag(Regen.name, padx=0)
    myDesc.Text(f"Permanently regens {Regen.Param2[0]*100}-{Regen.Param2[3]*100}% of their max health every {Regen.Param1[0]//30}-{Regen.Param1[3]//30} seconds.")

    myDesc.Tag(CloseArmor.name, padx=0)
    myDesc.Text(f"Reduces damage by {CloseArmor.Param1[0]}-{CloseArmor.Param1[3]}% to all allies and user within 5 meters")

    myDesc.Tag(Swarm.name, padx=0)
    myDesc.Text(f"Each ally the enemy has increases their own damage by {Swarm.Param1[0]}-{Swarm.Param1[3]}%")

    myDesc.Tag(Sealing.name, padx=0)
    myDesc.Text(f"Locks the first, second, and/or third block of the party gauge.")

    return myDesc





