import Options, json, random
from scripts import JSONParser, Helper


def WeaponRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/ITM_wpnlist.json", 'r+', encoding='utf-8') as wpnFile:
        
        isAppearance = Options.WeaponOption_Appearance.GetState()
        isDam = Options.WeaponOption_Damage.GetState()
        isRange = Options.WeaponOption_Range.GetState()
        isBlock = Options.WeaponOption_Block.GetState()
        isCrit = Options.WeaponOption_Crit.GetState()
        isSpeed = Options.WeaponOption_Speed.GetState()
        isGems = Options.WeaponOption_Gems.GetState()
        
        
        wpnData = json.load(wpnFile)
        for wep in wpnData["rows"]:
            
            if isAppearance:
                Appearance(wep)
                
            if isDam:
                Damage(wep)
            
            if isRange:
                Range(wep)
                
            if isBlock:
                Range(wep)
                
            if isCrit:
                Range(wep)
                
            if isSpeed:
                Range(wep)
                
            if isGems:
                Range(wep)


        JSONParser.CloseFile(wpnData, wpnFile)

def Appearance(wep):
    pass

def Damage(wep):
    pass

def Range(wep):
    pass

def Block(wep):
    pass

def Crit(wep):
    pass

def Speed(wep):
    pass

def Gems(wep):
    pass