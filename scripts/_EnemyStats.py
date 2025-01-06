import json, random




class Attribute:
    name = ""
    mult = 0
    nameColor = ""
    enPar = ""
    enArr = ""
    def __init__(self,_name, _mult, _nameColor, _enPar = "", _enArr = ""):
        self.name = _name
        self.mult = _mult
        self.nameColor = _nameColor
        self.enPar = _enPar
        self.enArr = _enArr
        AttributesList.append(self)

AttributesList = [Attribute]
Lucky = Attribute("Lucky" ,3, "yellow", _enArr = "ExpRev")


def EnemyStats():
    with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as EnArrangeFile:
        with open("./_internal/JsonOutputs/common_ms/CHR_EnParam.json", 'r+', encoding='utf-8') as EnParamFile:
            with open("./_internal/JsonOutputs/common_ms/fld_enemyname.json", 'r+', encoding='utf-8') as NamesFile:      
                EnArr = json.load(EnArrangeFile)
                EnPar = json.load(EnParamFile)
                Names = json.load(NamesFile)
                for Enemy in EnArr:
                    Att = random.choice(AttributesList)
                    
                    if Att.enArr != "":
                        Enemy[Att.enArr] *= Att.mult # Changes EnArrangeFile
                    
                    if Att.enPar != "":
                        for par in EnPar: # Changes EnParamFile
                            if par["$id"] == Enemy["ParamID"]:
                                par[Att.enPar] *= Att.mult
                            
                    for name in Names: # Changes Names
                        if name["$id"] == Enemy["Name"]:
                            oldName = name["name"]
                            name["name"] = f"[System:Color name={Att.nameColor}]{Att.name} {oldName}[/System:Color]"

                
                NamesFile.seek(0)
                NamesFile.truncate()
                json.dump(Names, NamesFile, indent=2, ensure_ascii=False)
            EnArrangeFile.seek(0)
            EnArrangeFile.truncate()
            json.dump(EnPar, EnParamFile, indent=2, ensure_ascii=False)
        EnArrangeFile.seek(0)
        EnArrangeFile.truncate()
        json.dump(EnArr, EnArrangeFile, indent=2, ensure_ascii=False)