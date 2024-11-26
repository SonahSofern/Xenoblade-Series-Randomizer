import json, random, os

ValidReplacements = []

def ChangeJSON(Filename, keyWords, rangeofValuesToReplace, rangeValidReplacements = [], InvalidTargetIDs = []): # make this a function to reuse, check the settings ot see if we even do this

    # Setup replacement exclusions
    global ValidReplacements
    # print(f"Valid Replacements: {Replacements}")
    rangeValidReplacements.extend(ValidReplacements)

    for name in Filename:
        filePath = "./_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if not item["$id"] in InvalidTargetIDs:
                    for key in item.items():
                        if any((key == keyWord) for keyWord in keyWords):
                            if (item[key] in rangeofValuesToReplace):
                                item[key] = random.choice(rangeValidReplacements)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    ValidReplacements.clear()
