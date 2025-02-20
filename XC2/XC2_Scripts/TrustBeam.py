import json
from scripts import JSONParser, Helper
def BeamRandomizer():
    JSONParser.ChangeJSONFile(["common/EFF_KizunaLink.json"], ["Red1","Red2", "Green1", "Green2", "Blue1", "Blue2"], Helper.InclRange(0,255), Helper.InclRange(0,255))
    JSONParser.ChangeJSONFile(["common/EFF_KizunaLink.json"], ["WavePower"],[100,120,140,200,300,400], Helper.InclRange(0,1000))