import random

Noun = ["Rex", "Jin", "Nia", "Malos", "Pyra", "Mythra", "Pneuma", "Padraig", "Morag", "Zeke", "Ozychlyrus", "Turters", "Tora", "Poppi", "Dromarch", "Sever", "Amalthus", "Aion", "Klaus", "Galea", "Wulfric", "Akhos", "Patroka", "Mikhail", "Lora", "Haze", "Addam", "Minoth", "Milton", "Dahlia", "Roc", "Azurda", "Corvin","Eulogimenos", "Bana", "Pupunin", "MuiMui", "FanLaNorne", "Niall", "Raqura", "Lila", "Dughall", "Iona", "Umon", "Vandham"]
Verb = ["Eats", "Destroys", "Disrupts", "Rolls", "Breaks", "Topples", "Launches", "Crushes", "Strikes", "Corrupts", "Befriends", "Spikes", "Hates", "Trusts", "Enrages", "Fears"]

def RandomSeedName():
    seedName = Noun[random.randrange(0,len(Noun))] + Verb[random.randrange(0,len(Verb))] + Noun[random.randrange(0,len(Noun))]
    return seedName