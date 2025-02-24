import Options, json

def MusicRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/bgmlist.json", 'r+', encoding='utf-8') as bgmFile:
        bgmData = json.load(bgmFile)
        for bgm in bgmData["rows"]:
            bgm["file_name"] = "b05_loop"
        bgmFile.seek(0)
        bgmFile.truncate()
        json.dump(bgmData, bgmFile, indent=2, ensure_ascii=False)
        
Music = {
    "No Sound": ["b04_loop"],
    "You Will Know Our Names": ["b02_loop"],
    "Mechanical Rythym": ["b03_loop"]
}
RemasteredBattleMusic = [
    "b01_loop", # Time To Fight
    "b02_loop", # You Will Know Our Names
    "b03_loop", # Mechanical Rythym
    
    
    
]

OriginalBattleMusic = [
    
    
    
    
]

RemasteredEnvironmentMusic = [
    
    
    
    
]

OriginalEnvironmentMusic = [
    
    
    
    
]