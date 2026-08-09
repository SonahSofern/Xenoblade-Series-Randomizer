import random
def RandomSeedName(Nouns, Verbs):
    if len(Nouns) < 2 or len(Verbs) < 1: return "No seed options"
    firstNoun = random.choice(Nouns)
    firstVerb = random.choice(Verbs)
    secondNoun = random.choice(Nouns)
    
    # Prevent Repeat Nouns
    while (firstNoun == secondNoun):
        secondNoun = random.choice(Nouns)
        
    seedName = firstNoun + firstVerb + secondNoun
    return seedName