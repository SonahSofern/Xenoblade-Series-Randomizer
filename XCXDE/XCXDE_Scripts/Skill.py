from XCXDE.XCXDE_Scripts import IDs
from scripts import JSONParser, StatRand, Helper, PopupDescriptions

maxMult = 3

def SkillEnhancements(intensity):
    '''Art enhancement currently paired with stats, they are unique to arts so can be adjusted without messing with other things'''
    statRando = StatRand.Stat(2, intensity)
    enhFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_Enhance.json")
    skillFile = JSONParser.File("XCXDE/JsonOutputs/common/BTL_SkillClass.json")
    
    # Ids from BTL_SkillClass
    param1MultSkillIDs = [2, 4, 5, 7, 8, 9, 15, 17, 47, 20, 25, 26, 29, 30, 33, 41, 44, 46, 49, 59, 83, 87, 89, 91, 94] # Don't change param1 of this skill
    param2MultSkillIDs = [26, 46, 52] # Don't change param2 of this skill
    ratioMultSkillIDs = [6, 26, 34, 46, 75, 81] # Change ratio of this skill
    
    for skill in skillFile.rows:                
        # Get the 5 level of enhancements that the skill has
        targetEnhancementIDs = []
        for i in range(0,5):
            targetEnhancementIDs.append(skill[f"Enhance[{i}]"])
            
        # Roll one mult for all 5 levels of this skill for each category
        if skill["$id"] not in param1MultSkillIDs: param1Mult = statRando.RollBalancedMult() 
        if skill["$id"] not in param2MultSkillIDs: param2Mult = statRando.RollBalancedMult()
        if skill["$id"] in ratioMultSkillIDs: ratioMult = statRando.RollBalancedMult()
    
        for enh in enhFile.rows:
            if enh["$id"] not in targetEnhancementIDs: continue
            
            if skill["$id"] not in param1MultSkillIDs: statRando.ApplyMult(enh, "param1", param1Mult)
            if skill["$id"] not in param2MultSkillIDs: statRando.ApplyMult(enh, "param2", param2Mult)
            if skill["$id"] in ratioMultSkillIDs: statRando.ApplyMult(enh, "ratio", ratioMult)
    
    enhFile.Close()
    skillFile.Close()
    

def SkillOrder():
    skillIDs = Helper.RandomGroup(Helper.InclRange(1,94))
    
    for i in range(1,39):
        growFile = JSONParser.File(f"XCXDE/JsonOutputs/common/CHR_Class{i:02}Growth.json")

        newSkillList = [] # Keeps track of what skills this class already has
        
        for rank in growFile.rows:
            for skillSlot in ["LearnSkill01", "LearnSkill02"]:
                # You dont learn skill here
                if rank[skillSlot] == 0: continue
            
                # Roll until we get a skill this class doesn't have yet            
                newSkill = skillIDs.SelectRandomMember()
                while newSkill in newSkillList:
                    newSkill = skillIDs.SelectRandomMember()
                
                # Assign
                rank[skillSlot] = newSkill
                                    
                # Add to keep track of what we learned so far
                newSkillList.append(newSkill)
        
        growFile.Close()
        
def SkillDesc(name):
    artRandoDesc = PopupDescriptions.Description()
    artRandoDesc.Header(name)
    artRandoDesc.Text(f"Randomizes the strength of skills within {1/maxMult}-{maxMult} times the original amount.")
    artRandoDesc.Tag("Intensity")
    artRandoDesc.Text(StatRand.IntensityDescription)
    return artRandoDesc