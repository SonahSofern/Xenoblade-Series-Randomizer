saveFolderName = "SaveData"
import os, json

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
                if data.get(option.name) == False:
                    continue
                option.checkBoxVal.set(data[option.name])

    except:
        print("Couldn't Load Saved Options")
