import random
import time

Person = ["Rex", "Jin", "Nia", "Malos", "Pyra", "Mythra", "Pneuma", "Padraig", "Morag", "Zeke", "Ozychlyrus", "Turters", "Tora", "Poppi", "Dromarch", "Sever", "Amalthus", "Aion", "Klaus", "Galea", "Wulfric", "Akhos", "Patroka", "Mikhail", "Lora", "Haze", "Addam", "Minoth", "Milton", "Dahlia", "Roc", "Azurda", "Corvin"]
Action = ["Eats", "Destroys", "Disrupts", "Rolls", "Breaks", "Topples", "Launches", "Crushes", "Strikes", "Corrupts", "Befriends", "Spikes", "Hates"]


def RandomSeedName():
    one = random.randrange(0,len(Person))
    two = random.randrange(0,len(Action))
    three = random.randrange(0,len(Person))
    seedName = Person[one] + Action[two] + Person[three]
    return seedName