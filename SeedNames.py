import random
import time

FirstWord = ["Rex", "Jin", "Nia", "Malos", "Pyra", "Mythra", "Pneuma", "Padraig", "Morag", "Zeke", "Ozychlyrus", "Turters", "Tora", "Poppi", "Dromarch", "Sever", "Amalthus", "Aion", "Klaus", "Galea", "Wulfric", "Akhos", "Patroka", "Mikhail", "Lora", "Haze", "Addam", "Minoth"]
SecondWord = ["Eats", "Destroys", "Disrupts", "Rolls", "Breaks", "Topples", "Launches", "Smashes", "Crushes", "Strikes", "Corrupts", "Befriends", "Spikes"]


def RandomSeedName():
    one = random.randrange(0,len(FirstWord))
    two = random.randrange(0,len(SecondWord))
    three = random.randrange(0,len(FirstWord))
    seedName = FirstWord[one] + SecondWord[two] + FirstWord[three]
    return seedName