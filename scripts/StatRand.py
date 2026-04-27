from scripts import Helper


b8 = 255
b16 = 65535

class Stat():
    '''A class that randomizes stats by multiplying them, based on intensity and various modes'''
    def __init__(self, maxMult, intensity, neutralMultPercent = 100):
        '''intensity - a value from 1-100 that determines how far away from the original value you can get, 100 means you can get full length away , eg. intensity 90 with max at 300% gets you 90% towards the max so up to 270% variance'''
        self.maxPercentMult = maxMult*100
        self.intensity = intensity
        self.neutralMultPercent = neutralMultPercent
        
        # Calculate max with intensity
        percVariance = self.intensity * .01
        self.maxWithIntensity = percVariance * (self.maxPercentMult - neutralMultPercent) + neutralMultPercent
    
    def RollBalancedMult(self, reverseChance = 50):
        '''On average gets multipliers according to intensity (returns results like 1.5 meaning 1.5x mult)'''
        
        if (self.neutralMultPercent >= int(self.maxWithIntensity)):
            chosenMult = self.neutralMultPercent
        else:
            chosenMult = Helper.random.randrange(self.neutralMultPercent, int(self.maxWithIntensity)) # Choose a mult between neutral and max*intensity
        
        if Helper.OddsCheck(reverseChance):
            chosenMult = 100/chosenMult # Reverse the value over 100
        else:
            chosenMult /= 100 # Divide the value by 100
            
        # print(f"Mult: {chosenMult}")
        return chosenMult
            
    def ApplyMult(self, target, stat, chosenMult = 1, max = b16, min = 1, allowFloat = False):
        '''Applies the mult to the stat, allowing for max and min values, as well as handling floats'''      
        clampedMult = Helper.Clamp(target[stat]*chosenMult, min, max) # Clamp the result to the bounds
        
        if not allowFloat:
            clampedMult = int(clampedMult)
        
        target[stat] = clampedMult