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
AOE = ArtEffect([1,2,5], "AOE", "Makes this art an Area of Effect, there are 3 types:\nAround User\nAround Target\nCone\n", [AOEGroup])

DebuffGroup:list[ArtEffect] = []
Taunt = ArtEffect([11], "Taunt", "Inflicts Taunt", [DebuffGroup])
Stench = ArtEffect([12], "Stench", "Inflicts Stench", [DebuffGroup])
ShackleDriver = ArtEffect([13], "Shackle Dr", "Inflicts Shackle Driver")
ShackleBlade = ArtEffect([14], "Shackle Bl", "Inflicts Shackle Blade", [DebuffGroup])
NullHeal = ArtEffect([15], "Null Heal", "Inflicts Null Heal for 15 seconds", [DebuffGroup])
Doom = ArtEffect([21], "Doom", "Inflicts Doom")
PDefDown = ArtEffect([23], "P Def↓", "Reduces Physical Defense", [DebuffGroup])
EDefDown = ArtEffect([24], "E Def↓", "Reduces Ether Defense", [DebuffGroup])
ResistanceDown = ArtEffect([25], "Res↓", "Inflicts Resistance Down", [DebuffGroup])
WindsOfTime = ArtEffect([30], "Freeze", "Stops enemy from acting for a time")
Inexaustible = ArtEffect([29], "Omnibuff", "Trades red health (torna) for all stat increases")
Enrage = ArtEffect([35], "Enrage", "Enrages the target if possible")

BuffGroup:list[ArtEffect] = []
NullReact = ArtEffect([1], "NlReact", "Nullifies all incoming reactions while casting this art.", [BuffGroup])
Evade = ArtEffect([2], "Evade", "Evade all incoming attacks while casting this art.", [BuffGroup])
Block = ArtEffect([3], "Block", "Block all incoming attacks while casting this art.", [BuffGroup])
Invincible = ArtEffect([4], "Inv", "Negate all incoming attacks while casting this art.", [BuffGroup])
Reflect = ArtEffect([5], "Rflct", "Reflect all incoming damage while casting this art.", [BuffGroup])
Counter = ArtEffect([6], "Counter", "Negate incoming attacks and inflict blowdown on attackers while casting this art.", [BuffGroup])
LaunchCounter = ArtEffect([7], "↑Counter", "Negative incoming attacks and inflict launch on attackers while casting this art.", [BuffGroup])
Absorb = ArtEffect([17], "Absorb", "Absorb all incoming attacks while casting this art, this heals you the amount absorbed.", [BuffGroup])
# Eventually might add logic for damage absorb and release

EnhancementGroup:list[ArtEffect] = []
BackUp = ArtEffect([[2760, 2761, 2762, 2763, 2764, 2764],[2755, 2756, 2757, 2758, 2759, 2759]], "Back↑", "Increases damage from the back.", [EnhancementGroup])
SideUp = ArtEffect([[2745, 2746, 2747, 2748, 2749, 2749],[2750, 2751, 2752, 2753, 2754, 2754]], "Side↑", "Increases damage from the side.", [EnhancementGroup])
AggroDown = ArtEffect([[2830, 2831, 2832, 2833, 2834, 2834],[2835, 2836, 2837, 2838, 2839, 2839]], "Aggro↓", "Reduces Aggro towards self by a %.", [EnhancementGroup])
AggroUp = ArtEffect([[2850, 2851, 2852, 2853, 2854, 2854],[2873, 2874, 2875, 2876, 2877, 2877]], "Aggro↑", "Increases aggro towards self.", [EnhancementGroup])
AggroedUp = ArtEffect([[2975, 2976, 2977, 2978, 2979, 2979]], "Aggroed↑", "Increases damage to enemy targeting yourself.", [EnhancementGroup])
AquaticUp = ArtEffect([[2705, 2706, 2707, 2708, 2709, 2709]], "Aquatic↑", "Increased damage to aquatic enemies.", [EnhancementGroup])
CancelUp = ArtEffect([[2810, 2811, 2812, 2813, 2814, 2814]], "Cancel↑", "Increased damage on cancelled attacks.", [EnhancementGroup])
CritUp = ArtEffect([[2975, 2976, 2977, 2978, 2979, 2979]], "Crit↑", "Increased crit damage.", [EnhancementGroup])
CritCDDown = ArtEffect([[2840, 2841, 2842, 2843, 2844, 2844]], "Crit CD↓", "Reduces cooldown for this art on a crit.", [EnhancementGroup])
FlyingUp = ArtEffect([[2700, 2701, 2702, 2703, 2704, 2704]], "Flying↑", "Increased damage to flying enemies.", [EnhancementGroup])
FrontUp = ArtEffect([[2740, 2741, 2742, 2743, 2744, 2744]], "Front↑", "Increased damage from the front.", [EnhancementGroup])
Vamp = ArtEffect([[2735, 2736, 2737, 2738, 2739, 2739],[2878, 2879, 2880, 2881, 2882, 2882]], "Vamp", "Heals a % of the damage dealt.", [EnhancementGroup])
PartyVamp = ArtEffect([[2845, 2846, 2847, 2848, 2849, 2849]], "Party Vamp", "Heals your party a % of the damage dealt.", [EnhancementGroup])
HighHPUp = ArtEffect([[2800, 2801, 2802, 2803, 2804, 2804]], "High HP↑", "Increased damage when user is on high health.", [EnhancementGroup])
HpPotion = ArtEffect([[2805, 2806, 2807, 2808, 2809, 2809]], "HP Potion", "Drops HP potions when this art hits.", [EnhancementGroup])
InsectUp = ArtEffect([[2685, 2686, 2687, 2688, 2689, 2689]], "Insect↑", "Increased damage to insects.", [EnhancementGroup])
LaunchUp = ArtEffect([[2780, 2781, 2782, 2783, 2784, 2784],[2775, 2776, 2777, 2778, 2779, 2779]], "Launch↑", "Increased damage to launched targets.", [EnhancementGroup])
LowHPUp = ArtEffect([[2790, 2791, 2792, 2793, 2794, 2794],[2785, 2786, 2787, 2788, 2789, 2789]], "Low HP↑", "Increased damage when user is on low health.", [EnhancementGroup])
MachineUp = ArtEffect([[2730, 2731, 2732, 2733, 2734, 2734],[2725, 2726, 2727, 2728, 2729, 2729]], "Machine↑", "Increased damage to machines.", [EnhancementGroup])
Pierce = ArtEffect([[2861, 2862, 2863, 2864, 2865, 2865]], "Pierce", "Pierces target's defenses.", [EnhancementGroup])
ToppleUp = ArtEffect([[2770, 2771, 2772, 2773, 2774, 2774],[2765, 2766, 2767, 2768, 2769, 2769]], "Topple↑", "Increased damage to toppled targets.", [EnhancementGroup])
BeastUp = ArtEffect([[2680, 2681, 2682, 2683, 2684, 2684]], "Beast↑", "Increased damage to beasts.", [EnhancementGroup])
HumanoidUp = ArtEffect([[2715, 2716, 2717, 2718, 2719, 2719]], "Humanoid↑", "Increased damage to humanoids.", [EnhancementGroup])
