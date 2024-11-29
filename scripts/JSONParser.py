import json, random, os, IDs


def ChangeJSON(Filename, keyWords, rangeofValuesToReplace, rangeValidReplacements = [], InvalidTargetIDs = [], SliderOdds = IDs.CurrentSliderOdds): # make this a function to reuse, check the settings ot see if we even do this

    # print(f"Valid Replacements: {Replacements}")
    rangeValidReplacements.extend(IDs.ValidReplacements)
    rangeValidReplacements = list(set(rangeValidReplacements) - set(IDs.InvalidReplacements))

    for name in Filename:
        filePath = "./_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if not item["$id"] in InvalidTargetIDs:
                    for key in item:
                        if any((key == keyWord) for keyWord in keyWords):
                            if ((item[key] in rangeofValuesToReplace) and (SliderOdds >= random.randint(1,100))):
                                item[key] = random.choice(rangeValidReplacements)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    IDs.ValidReplacements.clear()
    IDs.CurrentSliderOdds = 100