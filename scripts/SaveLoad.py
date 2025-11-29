saveFolderName = "SaveData"
import os, json

class SavedEntry: # Kinda hacky ):
    def __init__(self, _name, _val):
        self.name =_name
        self.checkBoxVal = _val 
        self.subOptions = []
        self.spinBoxVal = None
        self.hasSpinBox = False
    def StateUpdate(self): # Used so loadData doesnt care
        pass
    
stopPermalinkUpdate = False
seperator = " -> "

def saveData(DataList, Filename, gameFolder):
    os.makedirs(gameFolder, exist_ok=True)  
    saveFilePath = os.path.join(gameFolder, Filename)
    with open(saveFilePath, 'w') as file:
        sav = {}
        for saveData in DataList:
            sav.update({saveData.name: saveData.checkBoxVal.get()})
            if saveData.spinBoxVal != None:
                sav.update({f"{saveData.name} Spinbox: ": saveData.spinBoxVal.get()})
            for sub in saveData.subOptions:
                sav.update({f"{saveData.name}{seperator}{sub.name}": sub.checkBoxVal.get()})
                if sub.hasSpinBox:
                    sav.update({f"{saveData.name}{seperator}{sub.name} Spinbox: ": sub.spinBoxVal.get()})
        json.dump(sav, file, indent=4, ensure_ascii=True)


def loadData(DataList, Filename, gameFolder):
    global stopPermalinkUpdate
    stopPermalinkUpdate = True
    loadPath = os.path.join(gameFolder, Filename)
    if not os.path.exists(loadPath):
        return
    with open(loadPath, 'r') as file:
        data = json.load(file)
        for option in DataList:
            try:
                option.checkBoxVal.set(data[option.name])
                
                if option.hasSpinBox:
                    option.spinBoxVal.set(data[f"{option.name} Spinbox: "])
                    
                for sub in option.subOptions:
                    
                    sub.checkBoxVal.set(data[f"{option.name}{seperator}{sub.name}"])
                    
                    if sub.hasSpinBox:
                        sub.spinBoxVal.set(data[f"{option.name}{seperator}{sub.name} Spinbox: "])
                        
                option.StateUpdate()
            except:
                continue
    stopPermalinkUpdate = False
