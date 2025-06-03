from scripts import Helper, JSONParser, PopupDescriptions
import json
import copy
import Options

def ReassignAlphabeticalSort(): # we add some custom named items if any of the following settings are on:
    if Options.AccessoriesOption.GetState() or Options.AuxCoresOption.GetState() or Options.BladeWeaponChipsOption.GetState() or Options.CosmeticsOption.GetState() or Options.StartwithIncreasedMovespeedOption.GetState() or Options.RaceModeOption.GetState() or Options.UMHuntOption.GetState() or Options.TornaMainOption.GetState():
        ItemFileList = ['ITM_BoosterList', 'ITM_CollectionList', 'ITM_CrystalList', 'ITM_EventList', 'ITM_FavoriteList', 'ITM_HanaArtsEnh', 'ITM_HanaAssist', 'ITM_HanaAtr', 'ITM_HanaNArtsSet', 'ITM_HanaRole', 'ITM_InfoList', 'ITM_Orb', 'ITM_OrbEquip', 'ITM_PcEquip', 'ITM_PcWpnChip', 'ITM_PreciousList', 'ITM_PreciousListIra', 'ITM_SalvageList', 'ITM_TresureList']
        TextFileList = ['itm_booster', 'itm_collection', 'itm_crystal', 'itm_evt', 'itm_favorite', 'itm_orb', 'itm_orb', 'itm_hana_atr_ms', 'itm_hana_narts_set_ms', 'itm_hana_role_ms', 'itm_info', 'itm_orb', 'itm_orb', 'itm_pcequip', 'itm_pcwpnchip_ms', 'itm_precious', 'itm_precious', 'itm_salvage', 'itm_tresure']
        DictList = []
        for fileindex in range(len(ItemFileList)):
            with open(f"./XC2/_internal/JsonOutputs/common/{ItemFileList[fileindex]}.json", 'r+', encoding='utf-8') as file:
                data = json.load(file)

                with open(f"./XC2/_internal/JsonOutputs/common_ms/{TextFileList[fileindex]}.json", 'r+', encoding='utf-8') as textfile:
                    textdata = json.load(textfile)

                    for row in data["rows"]:
                        NewDict = {}
                        NewDict["$id"] = row["$id"]
                        NewDict["name"] = ""
                        for textrow in textdata["rows"]:
                            if textrow["$id"] == row["Name"]:
                                NewDict["name"] = textrow["name"]
                                break
                        DictList.append(NewDict)

                    textfile.seek(0)
                    textfile.truncate()
                    json.dump(textdata, textfile, indent=2, ensure_ascii=False)

                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)

        SortedDictList = sorted(DictList, key=lambda dictionary: dictionary["name"])
        IDtoSortPos = {}

        for item in range(len(SortedDictList)):
            if SortedDictList[item]["name"] != "":
                IDtoSortPos[SortedDictList[item]["$id"]] = item
            else:
                IDtoSortPos[SortedDictList[item]["$id"]] = 0

        for fileindex in range(len(ItemFileList)):
            with open(f"./XC2/_internal/JsonOutputs/common/{ItemFileList[fileindex]}.json", 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    row["sortGB"] = IDtoSortPos[row["$id"]]
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)

    pass
