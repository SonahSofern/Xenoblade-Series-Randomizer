saveFolderName = "SaveData"
import os, json, Options, traceback

def saveData(DataList, Filename):
    with open(f"{saveFolderName}/{Filename}", 'w') as file:
        sav= {}
        for saveData in DataList:
            sav.update({saveData.name: saveData.checkBoxVal.get()})
            for sub in saveData.subOptions:
                sav.update({f"{saveData.name}->{sub.name}": sub.checkBoxVal.get()})
        json.dump(sav, file, indent=4)


            
def loadData(DataList, Filename):
    try:
        os.makedirs(saveFolderName, exist_ok=True)
        with open(f"{saveFolderName}/{Filename}", 'r') as file:
            data = json.load(file)
            for option in DataList:
                option.checkBoxVal.set(data[option.name])
                for sub in option.subOptions:
                    sub.checkBoxVal.set(data[f"{option.name}->{sub.name}"])
                option.StateUpdate()
    except Exception as error:
                print(f"{traceback.format_exc()}") # shows the full error

class SavedEntry:
    def __init__(self, _name, _val):
        self.name =_name
        self.checkBoxVal = _val # Polymorphism with the Option Class
        self.subOptions = []
    def StateUpdate(self): # Used so loadData doesnt care
        pass