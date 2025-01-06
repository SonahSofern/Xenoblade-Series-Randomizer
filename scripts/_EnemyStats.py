import json, random




class Attribute:
    name = ""
    mult = 0
    nameColor = ""
    enPar = ""
    enArr = ""
    def __init__(self,_name, _baseMult, _nameColor, _enPar = "", _enArr = ""):
        self.name = _name
        self.mult = _baseMult
        self.nameColor = _nameColor
        self.enPar = _enPar
        self.enArr = _enArr
        AttributesList.append(self)
    def RollRank(self):
        rank = random.randrange(0,3)
        return rank

AttributesList = []

Golden = Attribute("Golden" ,5, "tutorial", _enArr = "GoldRev")


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
                        
                        if Att.enArr != "":
                            Enemy[Att.enArr] *= (Att.mult * rank+1) # Changes EnArrangeFile
                        
                        if Att.enPar != "":
                            for par in EnPar["rows"]: # Changes EnParamFile
                                if par["$id"] == Enemy["ParamID"]:
                                    par[Att.enPar] *= (Att.mult * rank+1)
                                    break
                                
                        for name in Names["rows"]: # Changes Names
                            if name["$id"] == Enemy["Name"]:
                                oldName = name["name"]
                                name["name"] = f"[System:Color name={Att.nameColor}]{Att.name +  ("+"*rank)}[/System:Color] {oldName}"
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