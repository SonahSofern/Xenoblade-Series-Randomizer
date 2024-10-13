import json
import random

BladeSpecialsJson = "./_internal/JsonOutputs/common/BTL_Arts_Bl.json"


def TotalBladeRandomize(): # runs all the functions that need to run
    BladeSpecialReactions()

def BladeSpecialReactions():
    print("Randomizing Blade Reactions")   
    with open(BladeSpecialsJson, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']: # key, value is tuple 
            for key, value in row.items():
                if key.startswith('ReAct'):
                    value = random.randint(0,14)
