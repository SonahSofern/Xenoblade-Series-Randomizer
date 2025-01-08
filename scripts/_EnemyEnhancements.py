import json, random




class Attribute:
    name = ""
    max = 0
    mult = 0
    nameColor = ""
    enPar = ""
    enArr = ""
    upgradable = True
    ignoreOriginal = False
    def __init__(self,_name, _baseMult ,_enPar = "", _nameColor = "tutorial", isUp = True, ignoreOriginal = False, _maxVal = 65000):
        self.name = _name
        self.mult = _baseMult
        self.nameColor = _nameColor
        self.enPar = _enPar
        self.isUp = isUp
        self.ignoreOriginal = ignoreOriginal
        self.max = _maxVal
        AttributesList.append(self)
    def RollRank(self):
        rank = random.choice(1,1,1,1,2,2,3)
        return rank

AttributesList = []
# working colors green, red, tutorial(yellow), link(blue)

Speedy = Attribute("Speed", 4, "BtlSpeed", _maxVal = 255)
Health = Attribute("Health", 0.8, "HpMaxRev")
Strength = Attribute("Strength", 0.8, "StrengthRev")
Ether = Attribute("Ether", 0.4, "PowEtherRev")
Dex = Attribute("Dex", 0.5, "DexRev")
Agility = Attribute("Agility", 2, "AgilityRev")
Luck = Attribute("Luck", 3, "LuckRev")
PArmor = Attribute("Defense", 40, "RstPower", _maxVal=100)
EArmor =Attribute("E. Defense", 40, "RstEther", _maxVal=100)
Crit = Attribute("Critical", 45, "CriticalRate", _maxVal=100)

# Use Enrage states, Arts and Enhance123 to make more enemy types
# RstFire = Attribute("Fireproof", 100, "RstFire", _maxVal=100) # Doesnt work even if i give pyra nova fire attribute

# GuardRate = Attribute("Guard", 40, "GuardRate", _maxVal=100) # Only works for enemies with blades so i dont really need this
# Unpottable = Attribute("Potion", 0, "HealPotDrop", _maxVal=0, isUp=False) # Setting to 0 doesnt seem to do anything to potions



def EnemyStats(spinBox):
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./_internal/JsonOutputs/common/CHR_EnParam.json", 'r+', encoding='utf-8') as EnParamFile:
            with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
                EnArr = json.load(EnArrangeFile)
                EnPar = json.load(EnParamFile)
                Names = json.load(NamesFile)
                for Enemy in EnArr["rows"]:
                    if spinBox >= random.randrange(0,101):
                        Att = random.choice(AttributesList)
                        
                        if Att.isUp:
                            rank = Att.RollRank()
                        else:
                            rank = 1
                        
                        if Att.enPar != "":
                            for par in EnPar["rows"]: # Changes EnParamFile
                                if par["$id"] == Enemy["ParamID"]:
                                    if Att.max <= 100:
                                       par[Att.enPar] += int((Att.mult * rank))
                                    else:         
                                        newVal = par[Att.enPar] * ((1+ Att.mult) * rank)
                                        par[Att.enPar] = int(newVal)
                                        
                                    if par[Att.enPar] > Att.max: # sets max if above
                                        par[Att.enPar] = Att.max
                                        
                                    break
                                
                        for name in Names["rows"]: # Changes Names
                            if name["$id"] == Enemy["Name"]:
                                oldName = name["name"]
                                enhanceName = Att.name +  ('+'*(rank-1))
                                if len(enhanceName + oldName) > 20:
                                    oldnameList = oldName.split()
                                    oldName = oldnameList[-1]           
                                name["name"] = f"[System:Color name={Att.nameColor}]{enhanceName}[/System:Color] {oldName}"
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