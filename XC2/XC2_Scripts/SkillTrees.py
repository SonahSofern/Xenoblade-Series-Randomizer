import json, random
from XC2.XC2_Scripts.Enhancements import *
from XC2.XC2_Scripts import Options
from scripts import PopupDescriptions

def RandomizeSkillEnhancements():
    DefaultArtsCancelSlots, DefaultXSlots, DefaultYSlots, DefaultBSlots  = [12,55,82,102,131,161,192,221,251], [1,51,61,91,121,162,181,222,241], [11,31,71,101,141,171,191,231,261], [21,52,62,92,122,151,201,211,242]
    ArtsCancelSlots, X_Slots, Y_Slots, B_Slots = [], [], [], []
    Rex, Nia, Tora, Vandham, Morag, Zeke, Lora, Addam, Hugo = Helper.InclRange(1, 30), Helper.InclRange(31, 60), Helper.InclRange(61, 90), Helper.InclRange(91, 120), Helper.InclRange (121, 150), Helper.InclRange(151, 180), Helper.InclRange(181, 210), Helper.InclRange(211, 240), Helper.InclRange(241, 270)
    DriverList = [Rex, Nia, Tora, Vandham, Morag, Zeke, Lora, Addam, Hugo]
    isVanilla = not Options.DriverSkillTreesOption_NonstandardSkills.GetState()
    isEarlyArtsCancel = Options.DriverSkillTreesOption_EarlyArtsCancel.GetState()
    isEarlyXYB = Options.DriverSkillTreesOption_EarlyXYBAttack.GetState()
    for Driver in DriverList:
        RemainingUnusedDriverIDs = Driver.copy()
        if isEarlyArtsCancel: # remove defaults first
            ArtsCancelSlots.append(DefaultArtsCancelSlots[DriverList.index(Driver)])
            RemainingUnusedDriverIDs.remove(DefaultArtsCancelSlots[DriverList.index(Driver)])
            SlotCostZero([1])
        if isEarlyXYB:
            X_Slots.append(DefaultXSlots[DriverList.index(Driver)])
            RemainingUnusedDriverIDs.remove(DefaultXSlots[DriverList.index(Driver)])
            Y_Slots.append(DefaultYSlots[DriverList.index(Driver)])
            RemainingUnusedDriverIDs.remove(DefaultYSlots[DriverList.index(Driver)])
            B_Slots.append(DefaultBSlots[DriverList.index(Driver)])
            RemainingUnusedDriverIDs.remove(DefaultBSlots[DriverList.index(Driver)])
            SlotCostZero([4,7,10])
        if Driver == Zeke:
            ChosenID = random.choice(RemainingUnusedDriverIDs)
            ZekeEyeSlot = [ChosenID]
            RemainingUnusedDriverIDs.remove(ChosenID)
        if not isEarlyArtsCancel: # have to separate out the if nots to avoid overwriting an arts cancel slot
            ChosenID = random.choice(RemainingUnusedDriverIDs)
            ArtsCancelSlots.append(ChosenID)
            RemainingUnusedDriverIDs.remove(ChosenID)
        if not isEarlyXYB:
            ChosenIDs = random.sample(RemainingUnusedDriverIDs, 3)
            X_Slots.append(ChosenIDs[0])
            RemainingUnusedDriverIDs.remove(ChosenIDs[0])
            Y_Slots.append(ChosenIDs[1])
            RemainingUnusedDriverIDs.remove(ChosenIDs[1])
            B_Slots.append(ChosenIDs[2])
            RemainingUnusedDriverIDs.remove(ChosenIDs[2])

    with open("./XC2/JsonOutputs/common/BTL_Skill_Dr.json", 'r+', encoding='utf-8') as enhancementFile:
        with open("./XC2/JsonOutputs/common_ms/btl_skill_dr_name.json", 'r+', encoding='utf-8') as nameFile:
            enhanceFile = json.load(enhancementFile)
            skillNameFile = json.load(nameFile)

            if isVanilla:
                def FindSkill(skillList, targetEnhancementIDs):
                    for skill in skillList:
                        if skill[1] in targetEnhancementIDs:
                            targetEnhancementIDs.remove(skill[1])
                            skillList.remove(skill)
                            return skill
                ArtCancelEnhanceIDs = [1280,187,1309,1340,1368,1397,1431,1450,1464,1494,1523,2246]
                X_StartIDs = [1277,1327,1321,1369,1389,1427,1447,1461,1491,1513]
                Y_StartIDs = [1290,1308,1349,1360,1398,1419,1448,1474,1483,1521]
                B_StartIDs = [110,1268,1299,1338,1378,1411,1440,1449,1452,1504,1534]
                ZekeEyeID = [1444]
                AllSpecialEnhances = ArtCancelEnhanceIDs + X_StartIDs + Y_StartIDs + B_StartIDs + ZekeEyeID
                skillList = []
                specialSkillList = []
                
                for skillSlot in enhanceFile['rows']: # Make a list of ids
                    if skillSlot["Enhance"] in AllSpecialEnhances:
                        specialSkillList.append([skillSlot["Name"],skillSlot["Enhance"]])
                    else:
                        skillList.append([skillSlot["Name"],skillSlot["Enhance"]])
                        
                random.shuffle(skillList)
                random.shuffle(specialSkillList)
                    
                for skillSlot in enhanceFile["rows"]:  # Set special Cases
                    id = skillSlot["$id"]
                    if id in ArtsCancelSlots:
                        newOne = FindSkill(specialSkillList,ArtCancelEnhanceIDs)
                    elif id in X_Slots:
                        newOne = FindSkill(specialSkillList,X_StartIDs)
                    elif id in Y_Slots:
                        newOne = FindSkill(specialSkillList,Y_StartIDs)
                    elif id in B_Slots:
                        newOne = FindSkill(specialSkillList,B_StartIDs)
                    elif id in ZekeEyeSlot:
                        newOne = FindSkill(specialSkillList,ZekeEyeID)
                    else:
                        try:
                            newOne = random.choice(skillList)
                            skillList.remove(newOne)
                        except:
                            pass # Ignore since the last skill chosen wont be able to swap
                        
                    skillSlot["Name"] = newOne[0]
                    skillSlot["Enhance"] = newOne[1]
            else:
                InvalidSkillEnhancements = [CritBoost,PhyAndEthDefenseUp, EtherCannonRange,BladeSwapDamage, FlatCritBoost, BlockBoost, FlatBlockBoost, PartyCritMaxAffinity, DamageAndCritUpMaxAffinity, ForcedHPPotionOnHit, HpPotChanceFor2, ArtCancel, EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, AegisPowerUp, BigBangPowerUp, CatScimPowerUp, VarSaberPowerUp, MechArmsPowerUp, WhipswordPowerUp, DrillShieldPowerUp, DualScythesPowerUp, EvadeDrainHp, EvadeDriverArt, KnuckleClawsPowerUp, BitballPowerUp, GreataxePowerUp, TwinRingPowerUp, MegalancePowerUp,ShieldHammerPowerUp, ChromaKatanaPowerUp, EtherCannonPowerUp, ArtDamageHeal, AegisParty, AegisDriver, EthDefBoost, FlatEthDefBoost, PhysDefBoost, FlatDefBoost]
                ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
                ForcedSkills = []
                for skillSlot in enhanceFile['rows']:
                    if ForcedSkills != []:
                        skill = random.choice(ForcedSkills)
                    elif skillSlot["$id"] in ArtsCancelSlots:
                        skill = ArtCancel
                    elif skillSlot["$id"] in ZekeEyeSlot:
                        skill = EyeOfJustice
                    elif skillSlot["$id"] in X_Slots:
                        skill = XStartBattle
                    elif skillSlot["$id"] in Y_Slots:
                        skill = YStartBattle
                    elif skillSlot["$id"] in B_Slots:
                        skill = BStartBattle
                    else:
                        skill = random.choice(ValidSkills)
                        # ValidSkills.remove(skill)
                    skill.RollEnhancement()
                    skillNameFile["rows"][skillSlot["$id"]-1]["name"] = skill.name
                    enhanceFile["rows"][skillSlot["$id"]-1]["Enhance"] = skill.id
            nameFile.seek(0)
            nameFile.truncate()
            json.dump(skillNameFile, nameFile, indent=2, ensure_ascii=False)
        enhancementFile.seek(0)
        enhancementFile.truncate()
        json.dump(enhanceFile, enhancementFile, indent=2, ensure_ascii=False)
        
def SlotCostZero(ids): # Used since art cancel gets put here
    for i in range(1, 10):
        with open(f"./XC2/JsonOutputs/common/BTL_Skill_Dr_Table{i:02}.json", 'r+', encoding='utf-8') as driverFiles:
            dFile = json.load(driverFiles)
            for item in dFile["rows"]:
                if item["$id"] in ids: 
                    item["NeedSp"] = 0
            driverFiles.seek(0)
            driverFiles.truncate()
            json.dump(dFile, driverFiles, indent=2, ensure_ascii=False)


def BladeSkillTreeShortening(): #how do you do, fellow skill tree randomization functions
    JSONParser.ChangeJSONLine(["common/CHR_Bl.json"],[0],Helper.StartsWith("ArtsAchievement",1,3) + Helper.StartsWith("SkillAchievement",1,3) + Helper.StartsWith("FskillAchivement",1,3) + ["KeyAchievement"], 15, replaceAll=True) # 15 is a trust condition and sets everything to that, so its all on trust with this

def Descriptions():
    SkillTreeDesc = PopupDescriptions.Description()
    SkillTreeDesc.Header(Options.DriverSkillTreesOption.name)
    SkillTreeDesc.Text("If no suboptions are also enabled, skills will be randomly pulled from the vanilla list of driver skills.")
    SkillTreeDesc.Image("DriverSkillTreeRandoBasic.png", "XC2", 700)
    SkillTreeDesc.Header(Options.DriverSkillTreesOption_NonstandardSkills.name)
    SkillTreeDesc.Text("If this suboption is enabled, skills will instead be pulled from a randomly generated list of effects.")
    SkillTreeDesc.Image("DriverSkillTreeRandoNonVanillaSkills.png", "XC2", 700)
    SkillTreeDesc.Header(Options.DriverSkillTreesOption_EarlyArtsCancel.name)
    SkillTreeDesc.Text("If this suboption is enabled, the inner-left skill on each Driver's Skill Tree will always be:\n'Lets you use an Art after canceling an Art.'\nIt will also cost 0 SP.")
    SkillTreeDesc.Image("DriverSkillTreeRandoEarlyArtsCancel.png", "XC2", 700)
    SkillTreeDesc.Header(Options.DriverSkillTreesOption_EarlyXYBAttack.name)
    SkillTreeDesc.Text("If this suboption is enabled, the inner-middle 3 skills on each Driver's Skill Tree will always be:\n'Allows use of the Driver Art assigned to [button] at the start of battle.'\nThey will also cost 0 SP.")
    SkillTreeDesc.Image("DriverSkillTreeRandoEarlyStartWithArt.png", "XC2", 700)
    return SkillTreeDesc
