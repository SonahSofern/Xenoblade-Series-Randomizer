import json
from scripts import Helper

class ValueContainer():
    def __init__(self):
        pass   
    
    def ClearContainer(self):
        ''' Empty the containers contents '''
        pass
    
    def GetContainerValue(self):
        ''' Return a number value for the container '''
        return -1

class ValueFile():
    def __init__(self, filename, key = "Price", mult = 1, path = "XC2/JsonOutputs/common/"):
        self.filename = f"{path}{filename}.json" # file to look at
        self.key = key # Key that indicates a value for the item
        self.mult = mult # multiplier on that keys value

class ValuedItem():
    def __init__(self, id, value):
        self.id = id
        self.value = value

class ValueTable():
    def __init__(self):
        self.valuesList = Helper.RandomGroup()
        
    def PopulateValues(self, file:ValueFile):
        '''
        Adds dictionary items linking every ITM with a gold value
        This value is useful to balance loot drops
        '''
        with open(file.filename, 'r+', encoding='utf-8') as curFile:
            curData = json.load(curFile)
            for data in curData["rows"]:
                self.valuesList.AddNewData(ValuedItem(data["$id"], int(data[file.key] * file.mult)))
    
    def isEmpty(self):        
        if self.valuesList.isEmpty():
            return True
        else:
            return False
    
    def SelectRandomMember(self):
        chosen:ValuedItem = self.valuesList.SelectRandomMember()
        return chosen
    
    def GetByID(self, id):
        """Given an id, search the valuesList for the ValuedItem."""
        for item in self.valuesList.originalGroup:
            if item.id == id:
                return item
        return None