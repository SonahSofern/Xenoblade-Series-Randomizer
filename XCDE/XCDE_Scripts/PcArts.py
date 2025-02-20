import json, random

def RandomizePcArts():
    with open("./XCDE/_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            art["pc"] = random.randrange(1,9)
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
        
# Setting that just shuffles arts
# Setting that randomizes effects of arts
# Setting to keep shulk with monado