saveFolderName = "SaveData"
import os, json


def saveData(DataList, Filename, GamePrefix):
    savePath = os.path.join(GamePrefix, saveFolderName)
    os.makedirs(savePath, exist_ok=True)  
    saveFilePath = os.path.join(savePath, Filename)
    with open(saveFilePath, 'w') as file:
        sav= {}
        for saveData in DataList:
            sav.update({saveData.name: saveData.checkBoxVal.get()})
            if saveData.spinBoxVal != None:
                sav.update({f"{saveData.name} Spinbox: ": saveData.spinBoxVal.get()})
            for sub in saveData.subOptions:
                sav.update({f"{saveData.name}->{sub.name}": sub.checkBoxVal.get()})
        json.dump(sav, file, indent=4, ensure_ascii=True)


            
def loadData(DataList, Filename, GamePrefix):
    try:
        savePath = os.path.join(GamePrefix, saveFolderName)
        saveFilePath = os.path.join(savePath, Filename)
        os.makedirs(savePath, exist_ok=True)
        with open(saveFilePath, 'r') as file:
            data = json.load(file)
            for option in DataList:
                option.checkBoxVal.set(data[option.name])
                try:
                    option.spinBoxVal.set(data[f"{option.name} Spinbox: "])
                except:
                    pass
                for sub in option.subOptions:
                    try:
                        sub.checkBoxVal.set(data[f"{option.name}->{sub.name}"])
                    except:
                        pass
                option.StateUpdate()

    except:
        pass # The file is created upon closing the window so it will error initial launch
    # except Exception as error:
    #             print(f"{traceback.format_exc()}") # shows the full error

class SavedEntry:
    def __init__(self, _name, _val):
        self.name =_name
        self.checkBoxVal = _val # Polymorphism with the Option Class
        self.subOptions = []
        self.spinBoxVal = None
    def StateUpdate(self): # Used so loadData doesnt care
        pass
    