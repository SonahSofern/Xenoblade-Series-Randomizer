import random

Person = ["Rex", "Jin", "Nia", "Malos", "Pyra", "Mythra", "Pneuma", "Padraig", "Morag", "Zeke", "Ozychlyrus", "Turters", "Tora", "Poppi", "Dromarch", "Sever", "Amalthus", "Aion", "Klaus", "Galea", "Wulfric", "Akhos", "Patroka", "Mikhail", "Lora", "Haze", "Addam", "Minoth", "Milton", "Dahlia", "Roc", "Azurda", "Corvin","Eulogimenos", "Bana", "Pupunin", "MuiMui", "FanLaNorne", "Niall", "Raqura", "Lila", "Dughall", "Iona", "Umon", "Vandham"]
Action = ["Eats", "Destroys", "Disrupts", "Rolls", "Breaks", "Topples", "Launches", "Crushes", "Strikes", "Corrupts", "Befriends", "Spikes", "Hates", "Trusts", "Enrages", "Fears"]

def RandomSeedName():
    seedName = Person[random.randrange(0,len(Person))] + Action[random.randrange(0,len(Action))] + Person[random.randrange(0,len(Person))]
    return seedName