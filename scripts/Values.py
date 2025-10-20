import json, random
from scripts import Helper, Interactables

differenceList = []
allowedRange = 0.05
ItemLogicDesciption = "This is done in a balanced way, by replacing the original item with an item of similar value."


def ItemValueStatistics():
    import statistics

    if not differenceList:
        print("No data in differenceList.")
        return

    print(f"For allowed range: {allowedRange*100}%")
    print(f"Mean Difference:  {statistics.mean(differenceList)}")
    print(f"Median Difference: {statistics.median(differenceList)}")
    print(f"Std Deviation:    {statistics.stdev(differenceList)}")


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
        self.valuesList:list[Helper.RandomGroup] = []
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
    
    def SelectValuedMember(self, data, key, dontChangeIDs):
        
        if data[key] in dontChangeIDs + [0]: # dont change some things and empty spots
            return
        
        originalItem = self.GetByID(data[key])
        
        if originalItem == None:
            # print(f"Item could not be found: {data[key]}")
            return
      
        category:Helper.RandomGroup = random.choices(self.valuesList, self.weightList, k=1)[0] # Select a category off weights
    
        indexOfSimilarValueItem = min(range(len(category.originalGroup)), key=lambda i: abs(category.originalGroup[i].value - originalItem.value))
        
        targetRange = max(int(len(category.originalGroup)*allowedRange), 3) # A range depending on the length of the group
        
        lowerBound = max(indexOfSimilarValueItem - targetRange, 0)
        upperBound = min(indexOfSimilarValueItem + targetRange, len(category.originalGroup))
        
        
        categoryRange = category.originalGroup[lowerBound:upperBound]
        
        chosen:ValuedItem = random.choice(categoryRange) # Want to select a random member based on a similar valued item from this category # not using Random Group methods because if you remove choices it could lead to unbalanced things since we are looking at nearby elements in a sorted list by value
        
        # print(f"Original Item Value: {originalItem.value} New Item Value: {chosen.value}")
        
        differenceList.append(originalItem.value - chosen.value)
        
        data[key] = chosen.id # Assign the item
    
    def GetByID(self, id):
        """Given an id, search the valuesList for the ValuedItem."""
        for list in self.valuesList:
            for item in list.originalGroup:
                if item.id == id:
                    return item
        return None

def WeightOptionMethod(option:Interactables.Option):
    ''' Basically just a shortcut so I can pass the option itself and if it is off treat the weight as 0, otherwise look at the spinbox'''
    if not option.GetState():
        return 0
    return option.GetSpinbox()