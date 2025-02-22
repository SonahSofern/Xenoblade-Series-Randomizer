from scripts import JSONParser, Helper


def UnlockNGPlusBlades():
    # Make T-elos and Torna blades available in base playthrough
    JSONParser.ChangeJSONLineWithCallback(["common/BLD_RareList.json"], [], ModifyGachaAvailability, replaceAll=True)

    # Adds Mikhail to the Gacha table
    MikhailGachaRow = {
        "$id": 38,
        "Blade": 1045,
        "Condition": 0,
    }
    for i in Helper.InclRange(1, 5):
        MikhailGachaRow["Prob" + str(i)] = 0.25  # Same as Akhos and Patroka
        MikhailGachaRow["Assure" + str(i)] = 0
    JSONParser.ExtendJSONFile("common/BLD_RareList.json", [[MikhailGachaRow]])


def ModifyGachaAvailability(gacha):
    if gacha['Condition'] == 1789:  # NG+ (Torna blades)
        gacha['Condition'] = 0
    elif gacha['Condition'] == 3219:  # Completed save file (T-elos)
        gacha['Condition'] = 0
