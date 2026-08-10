import os, json

stopPermalinkUpdate = False

class SavedEntry():
    def Save(self):
        pass
    
    def Load(self):
        pass
    
    def GetPermalinkVar(self):
        '''Gets the var object that permalinks save'''
        pass
    
def SaveData(dataList:list[SavedEntry], filename, gameFolder):
    os.makedirs(gameFolder, exist_ok=True)  
    saveFilePath = os.path.join(gameFolder, filename)
    saveFile = open(saveFilePath, 'w')
    saveData = {}
    for savedEntry in dataList:
        try:
            saveData.update(savedEntry.Save())
        except:
            print("Couldn't save an entry")
    json.dump(saveData, saveFile, indent=4, ensure_ascii=True)
    saveFile.close()

def LoadData(dataList:list[SavedEntry], filename, gameFolder):
    global stopPermalinkUpdate
    stopPermalinkUpdate = True
    loadPath = os.path.join(gameFolder, filename)
    if os.path.exists(loadPath):
        try:
            loadFile = open(loadPath, 'r')
            loadData = json.load(loadFile)
            for data in dataList:
                try:
                    data.Load(loadData)
                except:
                    print("Couldnt load state for an option")
            loadFile.close()
        except: 
            print("Couldn't open save file: " + loadPath)
    stopPermalinkUpdate = False
