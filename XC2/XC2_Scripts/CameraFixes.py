import json

def BladeArtCameraFixes():
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_Bl_Cam.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                for i in range(1, 8):
                    row[f"Camera{i}"] = 1
                row["Flag"]["EnTarget"] = 1                 
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

    with open("./XC2/_internal/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data["rows"]:
                row["Scale"] = 250
                row["WpnScale"] = 250                
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

