from scripts import Helper

class StatR():
    def __init__(self, maxMult, bitMax, intensity, neutralMult = 1, min = 1, reverseChance = 50):
        self.maxPercentMult = maxMult*100
        self.max = pow(2, bitMax) - 1
        self.min = min
        self.intensity = intensity
        self.neutralMultPercent = neutralMult*100
        self.reverseChance = reverseChance # % chance of getting the negative effect from your mult (a decrease in stat)
        
    def Balanced(self, target, stat, allowFloat = False):
        '''On average gets multipliers according to intensity, eg. intensity 90 with max at 300% gets you 90% towards the max so up to 270% variance'''
        percVariance = self.intensity * .01
        maxWithIntensity = percVariance * self.maxPercentMult

        chosenMult = Helper.random.randrange(self.neutralMultPercent, int(maxWithIntensity)) # Choose a mult between neutral and max*intensity
        
        if Helper.OddsCheck(self.reverseChance):
            chosenMult = 100/chosenMult
                
        clampedMult = Helper.Clamp(target[stat]*chosenMult, self.min, self.max) # Clamp the result to the bounds
        
        if not allowFloat:
            clampedMult = int(clampedMult)
        
        target[stat] = clampedMult