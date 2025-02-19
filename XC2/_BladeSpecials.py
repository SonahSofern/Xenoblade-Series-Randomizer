# BladeSpecialReactionsOption = Option("Blade Special Reactions", Blade, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [lambda: JSONParser.ChangeJSONFile(["common/BTL_Arts_Bl.json"], Helper.StartsWith("ReAct", 1, 16), HitReactions, HitReactions)], _hasSpinBox = True)
def BladeSpecials():
    pass