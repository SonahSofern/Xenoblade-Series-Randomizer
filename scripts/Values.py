import json, random
from scripts import Helper, Interactables
import statistics

differenceList = []
allowedRange = 0.1
ItemLogicDesciption = "This is done in a balanced way, by replacing the original item with an item of similar value."


def ItemValueStatistics():

    if len(differenceList) == 0:
        return

    print(f"For allowed range: {allowedRange*100}%")
    print(f"Mean Difference:  {statistics.mean(differenceList)}")
    print(f"Median Difference: {statistics.median(differenceList)}")
    print(f"Std Deviation:    {statistics.stdev(differenceList)}")

class RandomValuedGroup(Helper.RandomGroup):
    def __init__(self):
        super().__init__()
        self.stDev = None
    
    def SetStDevOverMean(self):
        pricesList = [x.value for x in self.originalGroup]
        mean = statistics.mean(pricesList)
        if mean == 0:
            self.stDev = 0
        else:
            self.stDev = abs(statistics.stdev(pricesList)/mean) 

class ValueFile():
    '''mult - Multiplier on the keys value, higher mult means this item will cost more to place'''
    def __init__(self, filename, key = "Price", mult = 1):
        self.filename = filename # file to look at
        self.key = key # Key that indicates a value for the item
        self.mult = mult # multiplier on that keys value

class ValuedItem():
    def __init__(self, id, value, category = 0):
        self.id = id
        self.value = value
        self.category = category # Only XCXDE uses this rn

class ValueTable():
    '''Holds data of all items and their categories to allow randomizing them to items of similar value'''
    def __init__(self, path = "XC2/JsonOutputs/common"):
        self.valuesList:list[RandomValuedGroup] = []
        self.weightList = []
        self.path = path
        
    def PopulateValues(self, file:ValueFile, validIDs, weight = 1, category = 0):
        '''
        List of RandomGroups linking every ITM with a gold value
        This value is useful to balance loot drops
        args:
        file: name of the file 
        validIDs: list of ids that are allowed to be populated
        weight: weight of this category
        '''
        with open(f"{self.path}/{file.filename}.json", 'r+', encoding='utf-8') as curFile:
            curData = json.load(curFile)
            newList = RandomValuedGroup()
            self.valuesList.append(newList)
            self.weightList.append(weight)
            for data in curData["rows"]:
                if data["$id"] in validIDs:
                    newList.AddNewData(ValuedItem(data["$id"], int(data[file.key] * file.mult), category))
            newList.currentGroup.sort(key=lambda x: x.value)
            newList.originalGroup.sort(key=lambda x: x.value)
            newList.SetStDevOverMean()
    
    def isEmpty(self):        
        if len(self.valuesList) == 0:
            return True
        else:
            return False
    
    def SelectValuedMember(self, data, key, dontChangeIDs = [], catKey = None, dontChangeCat = [29]):
        minRange = 5 # The minimum steps you can take in either direction choosing an item from the list so minRange = 10 means +- 10 items from the target value
        minStandardDeviationOverMean = 0.5
        
        if catKey != None:
            if (data[catKey] in dontChangeCat) and (data[key] in dontChangeIDs + [0]): # dont change some things and empty spots
                return
        elif data[key] in dontChangeIDs + [0]: # dont change some things and empty spots
            return
        
        if catKey == None:
            originalItem = self.GetByIDCat(data[key])
        else:
            originalItem = self.GetByIDCat(data[key], data[catKey])
        
        if originalItem == None:
            # print(f"Item could not be found: {data[key]}")
            return
        
        if not any(self.weightList):
            raise Exception("Not enough item categories chosen")
        
        category:Helper.RandomGroup = random.choices(self.valuesList, self.weightList, k=1)[0] # Select a category off weights
                
        indexOfSimilarValueItem = min(range(len(category.originalGroup)), key=lambda i: abs(category.originalGroup[i].value - originalItem.value))
        
        if category.stDev < minStandardDeviationOverMean:
            targetRange = len(category.originalGroup) # Forced full range when the St Dev of the data is low to keep randomness
        else:
            targetRange = max(int(len(category.originalGroup)*allowedRange), minRange) # A range depending on the length of the group
        
        lowerBound = max(indexOfSimilarValueItem - targetRange, 0)
        upperBound = min(indexOfSimilarValueItem + targetRange, len(category.originalGroup))
        categoryGroupRange = category.originalGroup[lowerBound:upperBound]
        
        chosen:ValuedItem = random.choice(categoryGroupRange) # Want to select a random member based on a similar valued item from this category # not using Random Group methods because if you remove choices it could lead to unbalanced things since we are looking at nearby elements in a sorted list by value
        
        # print(f"Original Item Value: {originalItem.value} New Item Value: {chosen.value}")
        
        differenceList.append(originalItem.value - chosen.value)
        
        data[key] = chosen.id # Assign the item
        
        if catKey != None: # If it has a category requirement assign it
            data[catKey] = chosen.category
        
        return chosen
    
    def GetByIDCat(self, id, cat = None):
        """Given an id and optionally a category, search the valuesList for the ValuedItem."""
        for list in self.valuesList:
            for item in list.originalGroup:
                if item.id == id:
                    if cat == None: # If no category given return the match
                        return item
                    elif item.category == cat: # If category given also check category
                        return item
        return None

def WeightOptionMethod(option:Interactables.MainOption):
    ''' Basically just a shortcut so I can pass the option itself and if it is off treat the weight as 0, otherwise look at the spinbox'''
    if not option.GetState():
        return 0
    return option.GetSpinbox()