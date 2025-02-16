import JSONParser, Helper

def BladeComboRandomization():
    ModifyCombo() # Seems to work
    #CustomCombo() # Doesn't seem to work. The "combo" never goes off. No zoom-in animation and no final hit damage

def ModifyCombo():
    def modifySteamExplosion(combo):
        combo['Name'] = 66
        combo['Atr'] = 4

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_ElementalCombo.json"], [6], modifySteamExplosion)

    newComboText = dict()
    newComboText['$id'] = 66
    newComboText['style'] = 36 # Always 36, whatever that means
    newComboText['name'] = 'Custom Combo'

    JSONParser.ExtendJSONFile("common_ms/btl_elementalcombo_ms.json", [[newComboText]])

def CustomCombo():
    newCombo = dict() # after 1,000,000 volt. electric, electric, earth
    newCombo['$id'] = 66
    newCombo['Name'] = 66
    newCombo['DebugName'] = 'Custom Combo'
    newCombo['Caption'] = 0
    newCombo['Atr'] = 3 # This is 1 less than the ID in the MNU_Msg_Attr table, for some reason. So the valid ranges are [1,8] instead of [2,9] (1 is attribute of NONE)
    newCombo['ComboStage'] = 3
    newCombo['Route'] = 1
    newCombo['RouteIra'] = 1
    newCombo['PreCombo'] = 33 # 1,000,000 Volt
    newCombo['Range'] = 0 # I believe this is used for AOE
    newCombo['BaseTime'] = 0 # 900 for stage 1-2. 0 for stage 3
    newCombo['Reaction'] = 0# Only blowdown or knockback. Usually only on tier 3s, but there's 1 exception (Wind-->Wind does knockback lvl 5 for some reason)
    newCombo['ReactionLv'] = 0
    newCombo['DD'] = 250 # 38 for level 1 unless there's no dot. No dots (Stone, Wind) have 150. For level 2s it's usually around 50-60 for dots and like 150-225 for non-dots. Level 3s are around 230-300 depending on difficulty of combos
    newCombo['Dot'] = 0 # 6 for all level 1s unless there's no dot. 8-10 for levels 2s. Always 0 for level 3
    newCombo['Interval'] = 0 # 45 if dot. 0 otherwise
    newCombo['DDEn'] = 40 # 7-10x smaller than the player equivalent
    newCombo['DotEn'] = 0 # level 3s are always 0, some others are sometimes 0. 0.6 for level 1s, 1 or 1.4 for level 2s.
    for i in Helper.InclRange(1,16):
        if i == 1:
            newCombo['DDf' + str(i)] = 40 # Unknown what this is, only 1 is used
        else:
            newCombo['DDf' + str(i)] = 0  # Unknown what this is, only 1 is used
    for i in Helper.InclRange(1, 16):
        newCombo['DmgRt' + str(i)] = 0 # Unused?
    for i in Helper.InclRange(1, 16):
        newCombo['ReAct' + str(i)] = 0 # Unknown what this is. Only 1 is used, and the value is always 1 when it is (Break)
    newCombo['Effect'] = 'cmn_005_029' # Mega Eruption's effect
    newCombo['SE'] = 107 # Mega Eruption's SE
    newCombo['NaID'] = 3 # What is this used for?
    newCombo['DamageRate'] = 15 # always equals 5 x ComboStage
    newCombo['FusionName1'] = 1 # Unknown, always 1
    newCombo['FusionName2'] = 1 # Unknown, always 1
    newCombo['FusionName3'] = 0 # Unknown, always 0
    newCombo['FusionName4'] = 0 # Unknown, always 0
    newCombo['Icon'] = 0 # Unknown, always 0
    newCombo['NeedAtrNum'] = 4 # Unknown, always 4
    JSONParser.ExtendJSONFile("common/BTL_ElementalCombo.json", [[newCombo]])
    JSONParser.PrintTable("common/BTL_ElementalCombo.json")

    newComboText = dict()
    newComboText['$id'] = 66
    newComboText['style'] = 36 # Always 36, whatever that means
    newComboText['name'] = 'Custom Combo'

    JSONParser.ExtendJSONFile("common_ms/btl_elementalcombo_ms.json", [[newComboText]])
    JSONParser.PrintTable("common_ms/btl_elementalcombo_ms.json")
