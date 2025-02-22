import random
def RandomSeedName(Nouns, Verbs):
    firstNoun = random.choice(Nouns)
    firstVerb = random.choice(Verbs)
    secondNoun = random.choice(Nouns)
    
    # Prevent Repeat Nouns
    while (firstNoun == secondNoun):
        secondNoun = random.choice(Nouns)
        
    seedName = firstNoun + firstVerb + secondNoun
    return seedName