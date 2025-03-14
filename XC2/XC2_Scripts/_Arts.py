class ArtEffect():
    def __init__(self, ids, name, description, group:list[list] = [],  abvName = None):
        self.ids = ids
        self.name = name
        self.abvName = abvName
        self.group = group
        self.desc = description
        for g in group:
            g.append(self)

ReactionGroup:list[ArtEffect] = []
Break = ArtEffect([1], "Break", "Inflicts Break", [ReactionGroup], abvName="B")
Topple = ArtEffect([2], "Topple", "Inflicts Topple", [ReactionGroup], abvName="T")
Launch = ArtEffect([3], "Launch", "Inflicts Launch", [ReactionGroup], abvName="L")
Smash = ArtEffect([4], "Smash", "Inflicts Smash", [ReactionGroup], abvName="S")
Knockback = ArtEffect([5,6,7,8,9], "Knockback", "Inflicts Knockback", [ReactionGroup], abvName="Kb")
Blowdown = ArtEffect([10,11,12,13,14], "Blowdown", "Inflicts Blowdown", [ReactionGroup], abvName="Bd")

AOEGroup:list[ArtEffect] = []
AOE = ArtEffect([1,2,5], "Area of Effect", "AOE", "Makes this art an Area of Effect, there are 3 types:\nAround User\nAround Target\nCone\n", [AOEGroup])

DebuffGroup:list[ArtEffect] = []
Taunt = ArtEffect([11], "Taunt", "Inflicts Taunt", [DebuffGroup])
Stench = ArtEffect([12], "Stench", "Inflicts Stench", [DebuffGroup])
ShackleDriver = ArtEffect([13], "Shackle Dr", "Inflicts Shackle Driver")
ShackleBlade = ArtEffect([14], "Shackle Bl", "Inflicts Shackle Blade", [DebuffGroup])
NullHeal = ArtEffect([15], "Null Heal", "Stops healing for 15 seconds", [DebuffGroup])
Doom = ArtEffect([21], "Doom", "Inflicts Doom", [DebuffGroup])
PDefDown = ArtEffect([23], "P Def↓", "Reduces Target's Physical Defense")
EDefDown = ArtEffect([24], "E Def↓", "Reduces Target's Ether Defense", [DebuffGroup])
ResistanceDown = ArtEffect([25], "Res↓", "Inflicts Resistance Down (Resistance to Reactions)", [DebuffGroup])
WindsOfTime = ArtEffect([30], "Freeze", "Stops enemy from acting for a time")
Enrage = ArtEffect([35], "Enrage", "Enrages the target if possible")

BuffGroup:list[ArtEffect] = []
NullReact = ArtEffect([1], "NlReact", "Nullifies all incoming reactions while casting this art", [BuffGroup])

BuffsDict = {
    "NlReact": 1,
    "Evade": 2,
    "Block": 3,
    "Counter": 6,
    "↑Counter": 7,
    "Rflct": 5,
    "Inv": 4,
    "Absorb":  17
    # Eventually might add logic for damage absorb and release
}