saveFolderName = "SaveData"
import os, json

def saveData(DataList, Filename):
    with open(f"{saveFolderName}/{Filename}", 'w') as file:
        sav= {}
        for saveData in DataList:
            sav.update({saveData.name: saveData.checkBoxVal.get()})
        json.dump(sav, file, indent=4)


            
def loadData(DataList, Filename):
    try:
        os.makedirs(saveFolderName, exist_ok=True)
        with open(f"{saveFolderName}/{Filename}", 'r') as file:
            data = json.load(file)
            for option in DataList:
                try:
                    option.checkBoxVal.set(data[option.name])
                except:
                    pass
    except:
        print("Couldn't Load Saved Options")
