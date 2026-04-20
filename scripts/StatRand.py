from scripts import Helper


b8 = 256
b16 = 65535

class Stat():
    def __init__(self, maxMult, intensity):
        '''intensity - a value from 1-100 that determines how far away from the original value you can get, 100 means you can get full length away , eg. intensity 90 with max at 300% gets you 90% towards the max so up to 270% variance'''
        self.maxPercentMult = maxMult*100
        self.intensity = intensity
        
    def Balanced(self, target, stat, max, min = 1, allowFloat = False, neutralMultPercent = 100, reverseChance = 50):
        '''On average gets multipliers according to intensity'''
        percVariance = self.intensity * .01
        maxWithIntensity = percVariance * self.maxPercentMult

        chosenMult = Helper.random.randrange(neutralMultPercent, int(maxWithIntensity)) # Choose a mult between neutral and max*intensity
        
        if Helper.OddsCheck(reverseChance):
            chosenMult = 100/chosenMult
                
        clampedMult = Helper.Clamp(target[stat]*chosenMult, min, max) # Clamp the result to the bounds
        
        if not allowFloat:
            clampedMult = int(clampedMult)
        
        target[stat] = clampedMult