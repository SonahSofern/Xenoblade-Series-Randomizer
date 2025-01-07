import json, random




class Attribute:
    name = ""
    mult = 0
    nameColor = ""
    enPar = ""
    enArr = ""
    upgradable = True
    ignoreOriginal = False
    def __init__(self,_name, _baseMult ,_enPar = "", _nameColor = "tutorial", isUp = True, ignoreOriginal = False):
        self.name = _name
        self.mult = _baseMult
        self.nameColor = _nameColor
        self.enPar = _enPar
        self.isUp = isUp
        self.ignoreOriginal = ignoreOriginal
        AttributesList.append(self)
    def RollRank(self):
        rank = random.randrange(1,4)
        return rank

AttributesList = []
# working colors green, red, tutorial(yellow), link(blue)

Speedy = Attribute("Speed", 0.9, "BtlSpeed")
Health = Attribute("Health", 0.4, "HpMaxRev")
Strength = Attribute("Strength", 0.25, "StrengthRev")
Ether = Attribute("Ether", 0.3, "PowEtherRev")
Dex = Attribute("Dex", 0.5, "DexRev")
Agility = Attribute("Agility", 0.3, "AgilityRev")
Luck = Attribute("Luck", 0.5, "LuckRev")
PArmor = Attribute("Defense", 0.2, "RstPower")
EArmor =Attribute("E. Defense", 0.3, "RstEther")
RstFire = Attribute("Fireproof", 0.3, "RstFire")
Crit = Attribute("Critical", 0.3, "CriticalRate")
GuardRate = Attribute("Guard", 0.3, "GuardRate")
Unpottable = Attribute("Potion", 0, "HealPotDrop")



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
                        rank = Att.RollRank()
                    
                        
                        if Att.enPar != "":
                            for par in EnPar["rows"]: # Changes EnParamFile
                                if par["$id"] == Enemy["ParamID"]:
                                    if par[Att.enPar] == 0: # For things like RstElement
                                       par[Att.enPar] += (Att.mult * rank)
                                    else:         
                                        par[Att.enPar] *= (Att.mult + rank)
                                        break
                                
                        for name in Names["rows"]: # Changes Names
                            if name["$id"] == Enemy["Name"]:
                                oldName = name["name"]
                                name["name"] = f"[System:Color name={Att.nameColor}]{Att.name +  ('+'*rank)}[/System:Color] {oldName}"
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