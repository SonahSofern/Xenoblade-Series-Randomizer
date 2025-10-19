import json, random
from scripts import Helper

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
        self.valuesList = []
        self.weightList = []
        
    def PopulateValues(self, file:ValueFile, validIDs, weight = 1):
        '''
        List of RandomGroups linking every ITM with a gold value
        This value is useful to balance loot drops
        args:
        file: name of the file 
        validIDs: list of ids that are allowed to be populated
        weight: weight of this category
        '''
        with open(file.filename, 'r+', encoding='utf-8') as curFile:
            curData = json.load(curFile)
            newList = Helper.RandomGroup()
            self.valuesList.append(newList)
            self.weightList.append(weight)
            for data in curData["rows"]:
                if data["$id"] in validIDs:
                    newList.AddNewData(ValuedItem(data["$id"], int(data[file.key] * file.mult)))
            newList.currentGroup.sort(key=lambda x: x.value)
            newList.originalGroup.sort(key=lambda x: x.value)
    
    def isEmpty(self):        
        if len(self.valuesList) == 0:
            return True
        else:
            return False
    
    def SelectValuedMember(self, data, key, dontChangeIDs, range = 10):
        
        if data[key] in dontChangeIDs + [0]: # dont change some things and empty spots
            return
        
        originalItem = self.GetByID(data[key])
        
        category:Helper.RandomGroup = random.choices(self.valuesList, self.weightList, k=1) # Select a category off weights
        
        indexOfOriginalItem = category.originalGroup.index(originalItem)
        
        lowerBound = max(indexOfOriginalItem - range, 0)
        upperBound = min(indexOfOriginalItem + range, len(category.originalGroup))
        
        
        categoryRange = category.originalGroup[lowerBound, upperBound]
        
        chosen:ValuedItem = random.choice(categoryRange) # Want to select a random member based on a similar valued item from this category # not using Random Group methods because if you remove choices it could lead to unbalanced things since we are looking at nearby elements in a sorted list by value
        
        
        data[key] = chosen.id # Assign the item
    
    def GetByID(self, id):
        """Given an id, search the valuesList for the ValuedItem."""
        for list in self.valuesList:
            for item in list:
                if item.id == id:
                    return item
        return None
