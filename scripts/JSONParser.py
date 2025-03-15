import copy
import json, random, os


def ChangeJSONFile(Filename: list, keyWords: list, rangeofValuesToReplace:list = [], rangeValidReplacements:list = [], InvalidTargetIDs:list = [], IgnoreID_AND_Key = [["",""]]): # make this a function to reuse, check the settings ot see if we even do this

    # print(f"Valid Replacements: {Replacements}")
    for name in Filename:
        filePath = "./XC2/_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if item["$id"] in InvalidTargetIDs:
                    continue
                for key in item:  
                    if ([item["$id"], key] in IgnoreID_AND_Key):
                        continue       
                    if key in keyWords:
                        if (rangeofValuesToReplace == []) or (item[key] in rangeofValuesToReplace):
                            item[key] = random.choice(rangeValidReplacements)
                    elif key == "Flag":
                        for flag, flagVal in item[key].items():
                            if flag in keyWords:
                                if (flagVal in rangeofValuesToReplace):
                                    item[key][flag] = random.choice(rangeValidReplacements)                                
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)


def ChangeJSONLine(filenames: list[str], ids: list[int], keys: list[str], replacement, replaceAll = False, Game = "XC2"):
    for name in filenames:
        filePath = f"./{Game}/_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if replaceAll:
                    for key in keys:
                        item[key] = replacement
                elif item["$id"] in ids:
                    for key in keys:
                        item[key] = replacement
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def ChangeJSONLineInMultipleSpots(filenames: list[str], ids: list[int], keys: list[str], replacements: list, replaceAll = False, Game = "XC2"): # sometimes we want to change a json line at multiple locations, so you want to input a list of replacements that tie to the key they're going into
    for name in filenames:
        filePath = f"./{Game}/_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if replaceAll:
                    for key in range(len(keys)):
                        row[keys[key]] = replacements[key]
                elif row["$id"] in ids:
                    for key in range(len(keys)):
                        row[keys[key]] = replacements[key]
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def ChangeJSONLineWithCallback(filenames, ids, callback, replaceAll = False):
    for name in filenames:
        filePath = "./XC2/_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if replaceAll or item["$id"] in ids:
                    callback(item)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def QueryJSONLine(filename, searchField, searchVal):
        filePath = "./XC2/_internal/JsonOutputs/" + filename
        if not os.path.exists(filePath):
            return
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if item[searchField] == searchVal:
                    return item
        return None

def CopyJSONFile(filename):
    filePath = "./XC2/_internal/JsonOutputs/" + filename
    if not os.path.exists(filePath):
      return dict()
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        out = dict()
        for item in data['rows']:
            out[item['$id']] = dict()
            for key, value in item.items():
                if key == '$id':
                    continue
                out[item['$id']][key] = copy.deepcopy(value)
        return out

def PrintTable(filename):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(filename)
    filePath = "./XC2/_internal/JsonOutputs/" + filename
    if not os.path.exists(filePath):
        return
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for item in data['rows']:
            print(item)
    print()

def ExtendJSONFile(filePath, additionsList = []):
    with open("./XC2/_internal/JsonOutputs/" + filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for item in additionsList:
            data["rows"].extend(item)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
        
        
def ReplaceJSONFile(filePath, replacement = []):
    with open("./XC2/_internal/JsonOutputs/" + filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"] = replacement
        file.seek(0)
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.truncate()