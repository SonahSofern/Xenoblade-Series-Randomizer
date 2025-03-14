import json
import random
from IDs import Arts, AutoAttacks
import Options
import scripts.PopupDescriptions
from _Arts import *

EnhancementSets = [[2760, 2761, 2762, 2763, 2764, 2764], [2745, 2746, 2747, 2748, 2749, 2749], [2815, 2816, 2817, 2818, 2819, 2819], [2830, 2831, 2832, 2833, 2834, 2834], [2815, 2816, 2817, 2818, 2819, 2819], [2861, 2862, 2863, 2864, 2865, 2865], [2745, 2746, 2747, 2748, 2749, 2749], [2815, 2816, 2817, 2818, 2819, 2819], [2680, 2681, 2682, 2683, 2684, 2684], [2815, 2816, 2817, 2818, 2819, 2819], [2746, 2746, 2746, 2746, 2746, 2746], [2815, 2816, 2817, 2818, 2819, 2819], [2680, 2681, 2682, 2683, 2684, 2684], [2680, 2681, 2682, 2683, 2684, 2684], [2815, 2816, 2817, 2818, 2819, 2819], [2700, 2701, 2702, 2703, 2704, 2704], [2755, 2756, 2757, 2758, 2759, 2759], [2780, 2781, 2782, 2783, 2784, 2784], [2790, 2791, 2792, 2793, 2794, 2794], [2855, 2856, 2857, 2858, 2859, 2859], [2795, 2796, 2797, 2798, 2799, 2799], [2866, 2866, 2866, 2866, 2866, 2866], [2770, 2771, 2772, 2773, 2774, 2774], [2735, 2736, 2737, 2738, 2739, 2739], [2765, 2766, 2767, 2768, 2769, 2769], [2790, 2791, 2792, 2793, 2794, 2794], [2850, 2851, 2852, 2853, 2854, 2854], [2866, 2866, 2866, 2866, 2866, 2866], [2765, 2766, 2767, 2768, 2769, 2769], [2850, 2851, 2852, 2853, 2854, 2854], [2866, 2866, 2866, 2866, 2866, 2866], [2770, 2771, 2772, 2773, 2774, 2774], [2725, 2726, 2727, 2728, 2729, 2729], [2740, 2741, 2742, 2743, 2744, 2744], [2725, 2726, 2727, 2728, 2729, 2729], [2770, 2771, 2772, 2773, 2774, 2774], [2790, 2791, 2792, 2793, 2794, 2794], [2825, 2826, 2827, 2828, 2829, 2829], [2700, 2701, 2702, 2703, 2704, 2704], [2790, 2791, 2792, 2793, 2794, 2794], [2825, 2826, 2827, 2828, 2829, 2829], [2700, 2701, 2702, 2703, 2704, 2704], [2770, 2771, 2772, 2773, 2774, 2774], [2705, 2706, 2707, 2708, 2709, 2709], [2840, 2841, 2842, 2843, 2844, 2844], [2840, 2841, 2842, 2843, 2844, 2844], [2765, 2766, 2767, 2768, 2769, 2769], [2705, 2706, 2707, 2708, 2709, 2709], [2705, 2706, 2707, 2708, 2709, 2709], [2840, 2841, 2842, 2843, 2844, 2844], [2775, 2776, 2777, 2778, 2779, 2779], [2765, 2766, 2767, 2768, 2769, 2769], [2840, 2841, 2842, 2843, 2844, 2844], [2800, 2801, 2802, 2803, 2804, 2804], [2745, 2746, 2747, 2748, 2749, 2749], [2830, 2831, 2832, 2833, 2834, 2834], [2685, 2686, 2687, 2688, 2689, 2689], [2800, 2801, 2802, 2803, 2804, 2804], [2685, 2686, 2687, 2688, 2689, 2689], [2760, 2761, 2762, 2763, 2764, 2764], [2830, 2831, 2832, 2833, 2834, 2834], [2760, 2761, 2762, 2763, 2764, 2764], [2800, 2801, 2802, 2803, 2804, 2804], [2830, 2831, 2832, 2833, 2834, 2834], [2750, 2751, 2752, 2753, 2754, 2754], [2760, 2761, 2762, 2763, 2764, 2764], [2830, 2831, 2832, 2833, 2834, 2834], [2805, 2806, 2807, 2808, 2809, 2809], [2861, 2862, 2863, 2864, 2865, 2865], [2810, 2811, 2812, 2813, 2814, 2814], [2810, 2811, 2812, 2813, 2814, 2814], [2861, 2862, 2863, 2864, 2865, 2865], [2780, 2781, 2782, 2783, 2784, 2784], [2805, 2806, 2807, 2808, 2809, 2809], [2861, 2862, 2863, 2864, 2865, 2865], [2805, 2806, 2807, 2808, 2809, 2809], [2780, 2781, 2782, 2783, 2784, 2784], [2861, 2862, 2863, 2864, 2865, 2865], [2810, 2811, 2812, 2813, 2814, 2814], [2780, 2781, 2782, 2783, 2784, 2784], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2770, 2771, 2772, 2773, 2774, 2774], [2740, 2741, 2742, 2743, 2744, 2744], [2850, 2851, 2852, 2853, 2854, 2854], [2770, 2771, 2772, 2773, 2774, 2774], [2850, 2851, 2852, 2853, 2854, 2854], [2770, 2771, 2772, 2773, 2774, 2774], [2780, 2781, 2782, 2783, 2784, 2784], [2785, 2786, 2787, 2788, 2789, 2789], [2850, 2851, 2852, 2853, 2854, 2854], [2795, 2796, 2797, 2798, 2799, 2799], [2866, 2866, 2866, 2866, 2866, 2866], [2715, 2716, 2717, 2718, 2719, 2719], [2866, 2866, 2866, 2866, 2866, 2866], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2866, 2866, 2866, 2866, 2866, 2866], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2866, 2866, 2866, 2866, 2866, 2866], [2740, 2741, 2742, 2743, 2744, 2744], [2850, 2851, 2852, 2853, 2854, 2854], [2795, 2796, 2797, 2798, 2799, 2799], [2815, 2816, 2817, 2818, 2819, 2819], [2765, 2766, 2767, 2768, 2769, 2769], [2845, 2846, 2847, 2848, 2849, 2849], [2775, 2776, 2777, 2778, 2779, 2779], [2815, 2816, 2817, 2818, 2819, 2819], [2765, 2766, 2767, 2768, 2769, 2769], [2815, 2816, 2817, 2818, 2819, 2819], [2775, 2776, 2777, 2778, 2779, 2779], [2800, 2801, 2802, 2803, 2804, 2804], [2755, 2756, 2757, 2758, 2759, 2759], [2765, 2766, 2767, 2768, 2769, 2769], [2845, 2846, 2847, 2848, 2849, 2849], [2815, 2816, 2817, 2818, 2819, 2819], [2810, 2811, 2812, 2813, 2814, 2814], [2815, 2816, 2817, 2818, 2819, 2819], [2755, 2756, 2757, 2758, 2759, 2759], [2810, 2811, 2812, 2813, 2814, 2814], [2815, 2816, 2817, 2818, 2819, 2819], [2745, 2746, 2747, 2748, 2749, 2749], [2810, 2811, 2812, 2813, 2814, 2814], [2815, 2816, 2817, 2818, 2819, 2819], [2745, 2746, 2747, 2748, 2749, 2749], [2755, 2756, 2757, 2758, 2759, 2759], [2815, 2816, 2817, 2818, 2819, 2819], [2830, 2831, 2832, 2833, 2834, 2834], [2760, 2761, 2762, 2763, 2764, 2764], [2745, 2746, 2747, 2748, 2749, 2749], [2830, 2831, 2832, 2833, 2834, 2834], [2860, 2860, 2860, 2860, 2860, 2860], [2760, 2761, 2762, 2763, 2764, 2764], [2861, 2862, 2863, 2864, 2865, 2865], [2740, 2741, 2742, 2743, 2744, 2744], [2805, 2806, 2807, 2808, 2809, 2809], [2760, 2761, 2762, 2763, 2764, 2764], [2845, 2846, 2847, 2848, 2849, 2849], [2830, 2831, 2832, 2833, 2834, 2834], [2815, 2816, 2817, 2818, 2819, 2819], [2815, 2816, 2817, 2818, 2819, 2819], [2845, 2846, 2847, 2848, 2849, 2849], [2830, 2831, 2832, 2833, 2834, 2834], [2845, 2846, 2847, 2848, 2849, 2849], [2815, 2816, 2817, 2818, 2819, 2819], [2830, 2831, 2832, 2833, 2834, 2834], [2830, 2831, 2832, 2833, 2834, 2834], [2845, 2846, 2847, 2848, 2849, 2849], [2815, 2816, 2817, 2818, 2819, 2819], [2790, 2791, 2792, 2793, 2794, 2794], [2745, 2746, 2747, 2748, 2749, 2749], [2825, 2826, 2827, 2828, 2829, 2829], [2685, 2686, 2687, 2688, 2689, 2689], [2790, 2791, 2792, 2793, 2794, 2794], [2685, 2686, 2687, 2688, 2689, 2689], [2760, 2761, 2762, 2763, 2764, 2764], [2825, 2826, 2827, 2828, 2829, 2829], [2760, 2761, 2762, 2763, 2764, 2764], [2790, 2791, 2792, 2793, 2794, 2794], [2825, 2826, 2827, 2828, 2829, 2829], [2750, 2751, 2752, 2753, 2754, 2754], [2760, 2761, 2762, 2763, 2764, 2764], [2825, 2826, 2827, 2828, 2829, 2829], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2680, 2681, 2682, 2683, 2684, 2684], [2850, 2851, 2852, 2853, 2854, 2854], [2795, 2796, 2797, 2798, 2799, 2799], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2680, 2681, 2682, 2683, 2684, 2684], [2740, 2741, 2742, 2743, 2744, 2744], [2680, 2681, 2682, 2683, 2684, 2684], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2745, 2746, 2747, 2748, 2749, 2749], [2810, 2811, 2812, 2813, 2814, 2814], [2840, 2841, 2842, 2843, 2844, 2844], [2840, 2841, 2842, 2843, 2844, 2844], [2810, 2811, 2812, 2813, 2814, 2814], [2746, 2746, 2746, 2746, 2746, 2746], [2810, 2811, 2812, 2813, 2814, 2814], [2840, 2841, 2842, 2843, 2844, 2844], [2840, 2841, 2842, 2843, 2844, 2844], [2810, 2811, 2812, 2813, 2814, 2814], [2700, 2701, 2702, 2703, 2704, 2704], [2755, 2756, 2757, 2758, 2759, 2759], [2805, 2806, 2807, 2808, 2809, 2809], [2861, 2862, 2863, 2864, 2865, 2865], [2740, 2741, 2742, 2743, 2744, 2744], [2740, 2741, 2742, 2743, 2744, 2744], [2861, 2862, 2863, 2864, 2865, 2865], [2780, 2781, 2782, 2783, 2784, 2784], [2805, 2806, 2807, 2808, 2809, 2809], [2861, 2862, 2863, 2864, 2865, 2865], [2805, 2806, 2807, 2808, 2809, 2809], [2780, 2781, 2782, 2783, 2784, 2784], [2861, 2862, 2863, 2864, 2865, 2865], [2740, 2741, 2742, 2743, 2744, 2744], [2780, 2781, 2782, 2783, 2784, 2784], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2785, 2786, 2787, 2788, 2789, 2789], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2785, 2786, 2787, 2788, 2789, 2789], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2785, 2786, 2787, 2788, 2789, 2789], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2785, 2786, 2787, 2788, 2789, 2789], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2830, 2831, 2832, 2833, 2834, 2834], [2760, 2761, 2762, 2763, 2764, 2764], [2770, 2771, 2772, 2773, 2774, 2774], [2730, 2731, 2732, 2733, 2734, 2734], [2830, 2831, 2832, 2833, 2834, 2834], [2770, 2771, 2772, 2773, 2774, 2774], [2760, 2761, 2762, 2763, 2764, 2764], [2830, 2831, 2832, 2833, 2834, 2834], [2770, 2771, 2772, 2773, 2774, 2774], [2730, 2731, 2732, 2733, 2734, 2734], [2830, 2831, 2832, 2833, 2834, 2834], [2730, 2731, 2732, 2733, 2734, 2734], [2800, 2801, 2802, 2803, 2804, 2804], [2815, 2816, 2817, 2818, 2819, 2819], [2810, 2811, 2812, 2813, 2814, 2814], [2840, 2841, 2842, 2843, 2844, 2844], [2800, 2801, 2802, 2803, 2804, 2804], [2815, 2816, 2817, 2818, 2819, 2819], [2840, 2841, 2842, 2843, 2844, 2844], [2815, 2816, 2817, 2818, 2819, 2819], [2810, 2811, 2812, 2813, 2814, 2814], [2840, 2841, 2842, 2843, 2844, 2844], [2810, 2811, 2812, 2813, 2814, 2814], [2815, 2816, 2817, 2818, 2819, 2819], [2840, 2841, 2842, 2843, 2844, 2844], [2800, 2801, 2802, 2803, 2804, 2804], [2810, 2811, 2812, 2813, 2814, 2814], [2835, 2836, 2837, 2838, 2839, 2839], [2860, 2860, 2860, 2860, 2860, 2860], [2760, 2761, 2762, 2763, 2764, 2764], [2745, 2746, 2747, 2748, 2749, 2749], [2861, 2862, 2863, 2864, 2865, 2865], [2765, 2766, 2767, 2768, 2769, 2769], [2878, 2879, 2880, 2881, 2882, 2882], [3015, 3016, 3017, 3018, 3019, 3019], [2740, 2741, 2742, 2743, 2744, 2744], [2770, 2771, 2772, 2773, 2774, 2774], [2975, 2976, 2977, 2978, 2979, 2979], [2810, 2811, 2812, 2813, 2814, 2814], [2825, 2826, 2827, 2828, 2829, 2829], [2800, 2801, 2802, 2803, 2804, 2804], [2830, 2831, 2832, 2833, 2834, 2834], [2872, 2872, 2872, 2872, 2872, 2872], [2873, 2874, 2875, 2876, 2877, 2877], [2795, 2796, 2797, 2798, 2799, 2799], [2873, 2874, 2875, 2876, 2877, 2877], [2780, 2781, 2782, 2783, 2784, 2784], [2790, 2791, 2792, 2793, 2794, 2794], [2873, 2874, 2875, 2876, 2877, 2877], [2873, 2874, 2875, 2876, 2877, 2877], [2872, 2872, 2872, 2872, 2872, 2872], [2795, 2796, 2797, 2798, 2799, 2799], [2805, 2806, 2807, 2808, 2809, 2809], [2872, 2872, 2872, 2872, 2872, 2872], [2755, 2756, 2757, 2758, 2759, 2759], [2810, 2811, 2812, 2813, 2814, 2814], [2745, 2746, 2747, 2748, 2749, 2749], [2866, 2866, 2866, 2866, 2866, 2866], [2866, 2866, 2866, 2866, 2866, 2866], [2810, 2811, 2812, 2813, 2814, 2814], [2755, 2756, 2757, 2758, 2759, 2759], [2810, 2811, 2812, 2813, 2814, 2814], [2866, 2866, 2866, 2866, 2866, 2866], [2755, 2756, 2757, 2758, 2759, 2759], [2755, 2756, 2757, 2758, 2759, 2759], [2810, 2811, 2812, 2813, 2814, 2814], [2745, 2746, 2747, 2748, 2749, 2749], [2866, 2866, 2866, 2866, 2866, 2866], [2740, 2741, 2742, 2743, 2744, 2744], [2850, 2851, 2852, 2853, 2854, 2854], [2795, 2796, 2797, 2798, 2799, 2799], [2866, 2866, 2866, 2866, 2866, 2866], [2740, 2741, 2742, 2743, 2744, 2744], [2866, 2866, 2866, 2866, 2866, 2866], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2740, 2741, 2742, 2743, 2744, 2744], [2866, 2866, 2866, 2866, 2866, 2866], [2795, 2796, 2797, 2798, 2799, 2799], [2850, 2851, 2852, 2853, 2854, 2854], [2866, 2866, 2866, 2866, 2866, 2866], [2740, 2741, 2742, 2743, 2744, 2744], [2850, 2851, 2852, 2853, 2854, 2854], [2795, 2796, 2797, 2798, 2799, 2799]]


def DriverArtRandomizer():
    with open("./XC2/_internal/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        
        isAutoAttacks = Options.DriverArtsOption_AutoAttacks.GetState()
        isMultiReact = Options.DriverArtsOption_MultipleReactions.GetState()
        isReactions = Options.DriverArtsOption_SingleReaction.GetState()
        isCooldowns = Options.DriverArtsOption_Cooldown.GetState()
        isDamage = Options.DriverArtsOption_Damage.GetState()
        isEnhancements = Options.DriverArtsOption_Enhancements.GetState()
        isBuffs = Options.DriverArtsOption_Buffs.GetState()
        isDebuffs = Options.DriverArtsOption_Debuffs.GetState()
        isAOE = Options.DriverArtsOption_AOE.GetState()
        isSpeed = Options.DriverArtsOption_AnimationSpeed.GetState()
        odds = Options.DriverArtsOption.GetOdds()
        
        for art in artData["rows"]:
            if art["$id"] in [4,5,6,7]: # Dont change aegis since they get copied to later
                continue
            
            if (not isAutoAttacks) and (isAutoAttacks or (art["$id"] in AutoAttacks)): # Ignore auto attacks unless the option is clicked
                continue
            isEnemyTarget = (art["Target"] in [0,4]) # Ensures Targeting Enemy
    
            if (isReactions or isMultiReact) and isEnemyTarget:
                for j in range(1,17):
                    art[f"ReAct{j}"] = 0 # Clearing Defaults these are needed bc torna arts are weird so i cant clear them blindly before hand gotta follow these conditions so this is the easiest way
                if OddCheck(odds):
                    Reaction(art, isMultiReact)
                    
            if isCooldowns and OddCheck(odds):
                Cooldowns(art)
                
            if isDamage and OddCheck(odds):
                Damage(art)
                
            if isEnhancements and isEnemyTarget:
                for i in range(1,7):
                    art[f"Enhance{i}"] = 0
                if OddCheck(odds):
                    Enhancements(art, EnhancementSets)
                    
            if isBuffs:
                art["ArtsBuff"] = 0 
                if OddCheck(odds//2): # These are really strong so im lowering the odds
                    Buffs(art)
                    
            if isDebuffs and isEnemyTarget:
                art["ArtsDeBuff"] = 0
                if OddCheck(odds):
                    Debuffs(art)
                    
            if isAOE and isEnemyTarget:
                art["RangeType"] = 0
                if OddCheck(odds):
                    AOE(art)
                    
            if isSpeed and OddCheck(odds):
                AnimationSpeed(art)

        # Since Aegis and Broadsword Share Captions they need the same effects
        CopyArt(artData,305,4)
        CopyArt(artData,306,5)
        CopyArt(artData,308,6)
        CopyArt(artData,307,7)
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
 
def CopyArt(artData, copyID, artID): # Copies all relavent effects of the art for shared captions
    for art in artData["rows"]:
        if art["$id"] == copyID:
            copy = art
            break
    for art in artData["rows"]:
        if art["$id"] == artID:
            art["RangeType"] = copy["RangeType"]
            art["Radius"] =  copy["Radius"]
            art["Length"] = copy["Length"]
            for i in range(1,17):
                art[f"ReAct{i}"] = copy[f"ReAct{i}"]
            for i in range(1,7):
                art[f"Enhance{i}"] = copy[f"Enhance{i}"]
            art["ArtsDeBuff"] = copy["ArtsDeBuff"]
            art["ArtsBuff"] = copy["ArtsBuff"]
            break


def OddCheck(odds):
    return (odds > random.randrange(0,100))

def Reaction(art, multReact):
    for i in range(1,17):
        if art[f"ReAct{i}"] > 14: # Dont replace weird ones that just move blades
            continue
        choice = random.choice(ReactionGroup)
        if art[f"HitFrm{i}"] == 0 and (i != 16 and art[f"HitFrm{i+1}"] == 0): # Need the second condition because zenobias Ascension Blade 129 has no hit on frame 1 but afterwards has hits # Make sure there is a hit
            art[f"ReAct{i-1}"] = random.choice(choice.ids) # Adds something to the last hit
            break
        if multReact:
            art[f"ReAct{i}"] =  random.choice(choice.ids) # Adds each hit

def Cooldowns(art): 
    CD = random.randrange(5,14)
    for i in range(1,7):
        step = random.choice([0,0,1,1,1,2])
        if CD > step:
            CD -= step
        art[f"Recast{i}"] = CD

def Damage(art): 
    DMG = random.randrange(100,325,5)
    initDMG = DMG
    # different damage scalings for different arts, chosen at random, added to make arts feel more unique. Arts with lower base damages should scale lower, while arts with higher base damages should scale higher
    scales = { 
        "low": [10, 15, 20],
        "med": [25, 30, 35],
        "high": [35, 40, 45]
    }
    for i in range(1,7):
        match initDMG:
            case initDMG if initDMG <= 175:
                chosenscale = "low"
            case initDMG if 175 < initDMG <= 250:
                chosenscale = "med"
            case initDMG if initDMG > 250:
                chosenscale = "high"
        step = random.choice(scales[chosenscale])
        DMG += step
        art[f"DmgMgn{i}"] = DMG
        
def Enhancements(art, EnhancementSet):  # Go through and fix these to be variables of the function so i can reference all values in the name for genart description so i can make level 4 specials have the highest level effect and it still reads those effects
    Enhancement = random.choice(EnhancementSet)
    for i in range(1,7):
        art[f"Enhance{i}"] = Enhancement[i-1]



def Buffs(art):
    name, buff = random.choice(list(BuffsDict.items()))
    art["ArtsBuff"] = buff

DebuffsDict = {
    "Taunt" : 11,
    # "Stench": 12, # It applies but im not sure enemy drivers even lose affinity with their blades like that
    "NlHeal": 15,
    "Shackle": 14,
    "Def↓": 23,
    "EDef↓": 24,
    "Res↓": 25,
    # "Monado Armor": 16, # These work just dont want player to apply them lol
    # "Doom": 21,
    # "Superstrength": 17
}

def Debuffs(art):
    name, debuff = random.choice(list(DebuffsDict.items()))
    art["ArtsDeBuff"] = debuff

def AnimationSpeed(art):
    art["ActSpeed"] = random.randrange(50,200,10)

def AOE(art):
    RangeType = random.choice(AOEGroup)
    RandomRadius = random.randint(10,15)
    RandomLength = random.randrange(2,17,4)
    art["RangeType"] = random.choice(RangeType.ids)
    art["Radius"] =  RandomRadius
    art["Length"] = RandomLength



def GenCustomArtDescriptions(artsFile, descFile, isSpecial = False):
    EnhancementsDict = {
        "Aggro↓" : [2830,2835],
        "Aggro↑" : [2850,2873],
        "Aggroed↑": [2795],
        "Aquatic↑": [2705],
        "Back↑": [2760,2755],
        "Cancel↑": [2810],
        "Crit↑": [2975],
        "Crit CD↓": [2840],
        # "Evade": [2825,2866,2872], Evade is not an enhancement and wont work for it
        "Flying↑": [2700],
        "Front↑": [2740],
        "Vamp": [2735,2878],
        "Party Vamp": [2845],
        "High HP↑": [2800,2805],
        "HP Potion": [2815,2860],
        "Insect↑": [2685],
        "Launch↑": [2780,2775],
        "Low HP↑": [2790,2785],
        "Machine↑": [2730,2725],
        "Pierce": [2861],
        "Side↑": [2746,2745,2750],
        "Topple↑": [2770,2765],
        "Beast↑": [2680],
        "Humanoid↑": [2715]
    }

    BuffsDict = {
        "NlReact": [1],
        "Evade": [2],
        "Block": [3],
        "Counter": [6],
        "↑Counter": [7],
        "Reflect": [5],
        "Invincible": [4],
        "Absorb":  [17]
        # Eventually might add logic for damage absorb and release
    }
    
    with open(artsFile, "r+", encoding='utf-8') as ArtsFile:     
        with open(descFile, "r+", encoding='utf-8') as DescFile:     
            artsData = json.load(ArtsFile)
            descData = json.load(DescFile)
            AnchorShotDesc = 0
            
            for art in artsData["rows"]:
                CurrDesc = art["Caption"]
                CombinedCaption = ["","","","",""]
                FirstDescriptionMod = 0
                LastDescriptionMod = 0
                # AOE
                for aoe in AOEGroup:    
                    if art["RangeType"] in aoe.ids:
                        CombinedCaption[0] += f"[System:Color name=blue]{aoe.abvName}[/System:Color]"
                        break

                # Type of Art Not changing this currently 
                # for key,values in MoveType.items():
                #     if art["ArtsType"] in values:
                #         CombinedCaption[1] += f"{key}"
                #         break
                
                for key,values in BuffsDict.items():
                    if art["ArtsBuff"] in values:
                        CombinedCaption[1] += f"{key}"
                        break

                # Reactions 
                ReactCaption = ""
                TypeReactions = []
                for i in range(1,17):              
                    if art[f"HitDirID{i}"] != 0:
                        for react in ReactionGroup:
                            if art[f"ReAct{i}"] in react.ids:
                                ReactCaption += f"[System:Color name=tutorial]{react.abvName}[/System:Color]->"
                                TypeReactions.append(art[f"ReAct{i}"])
                                break
                ReactCaption = ReactCaption[:-2]
                # if len(ReactCaption) > 15: # If the length is too long, shorten it to "Driver Combo"
                #     ReactCaption = "[System:Color name=tutorial]Driver Combo[/System:Color]"
                if len(TypeReactions) == 1: # If the length is 1, spell out the reaction
                    for react in ReactionGroup:
                        if TypeReactions[0] in react.ids:
                            ReactCaption = f"[System:Color name=tutorial]{react.name}[/System:Color]"
                            break
                CombinedCaption[2] = ReactCaption
                    
                # Enhancements
                for key,values in EnhancementsDict.items():
                    if art["Enhance1"] in values:
                        CombinedCaption[3] += f"[System:Color name=green]{key}[/System:Color]"
                        break
                    
                # Debuffs   
                if (art.get("ArtsDeBuff") != None):                    
                    for key,values in DebuffsDict.items():
                        if art["ArtsDeBuff"] in values:
                            CombinedCaption[4] = f"[System:Color name=red]{key}[/System:Color]"
                            break

                # Putting it all together
                TotalArtDescription = ""    
                for i in range(0, len(CombinedCaption)):
                    if CombinedCaption[i] != "":
                        FirstDescriptionMod = i
                        break
                for i in range(len(CombinedCaption) - 1, 0, -1):
                    if CombinedCaption[i] != "":
                        LastDescriptionMod = i
                        break
                TotalArtDescription += CombinedCaption[FirstDescriptionMod]
                if FirstDescriptionMod != LastDescriptionMod:
                    for i in range(FirstDescriptionMod + 1, LastDescriptionMod + 1):
                        if CombinedCaption[i] != "":
                            TotalArtDescription += " / "
                            TotalArtDescription += CombinedCaption[i]


                if TotalArtDescription == "":
                    TotalArtDescription = "No Effects"

                # Update Descriptions
                for desc in descData["rows"]:
                    if desc["$id"] == CurrDesc:
                        if not isSpecial: 
                            if desc["$id"] == 4:   # Sets anchor shot 5 to anchor shot 4's description since they are the same art
                                TotalArtDescription = TotalArtDescription.replace(ReactCaption + " / ", "")   # Removes the reaction text from 4 because it is disabled until you get to uraya. 4 Corresponds to before uraya description and 5 is after uraya.
                                AnchorShotDesc = desc["name"]
                                desc["name"]
                            if desc["$id"] == 5:
                                desc["name"] = AnchorShotDesc
                                break
                        desc["name"] = TotalArtDescription
                        break

                    
            DescFile.seek(0)
            DescFile.truncate()
            json.dump(descData, DescFile, indent=2, ensure_ascii=False)             
        ArtsFile.seek(0)
        ArtsFile.truncate()
        json.dump(artsData, ArtsFile, indent=2, ensure_ascii=False)
        
        
def DriverArtDescriptions():
    desc= scripts.PopupDescriptions.Description()
    desc.Header(Options.DriverArtsOption.name)
    desc.Text("This option randomizes various effects of driver arts, even to effects that could not be obtained in the normal game.")
    desc.Image("artsimage.png", "XC2", 600)
    desc.Text("Any changes made will update the art's description in combat. These are color coded by type.")
    desc.Header(Options.DriverArtsOption_AutoAttacks.name)
    
    desc.Text("Applies your chosen options to each driver's autoattacks as well as arts.")
    desc.Header(f"{Options.DriverArtsOption_SingleReaction.name}/{Options.DriverArtsOption_MultipleReactions.name}")
    
    desc.Text("Allows single/multiple reaction(s) to be placed on arts. These effects are shown in yellow text. These will be abbreviated if the description gets too long.\nIf both options are enabled multiple reactions will take priority.")
    reactions = []
    for react in ReactionGroup:
        reactions.append(f"{react.name} ({react.abvName}) - {react.desc}")
    desc.Text("\n".join(reactions))

    
    # desc.Text("Break - B\nTopple - T\nLaunch - L\nSmash - S\nBlowdown - Bd\nKnockback - Kb")
    
    desc.Header(Options.DriverArtsOption_Debuffs.name)
    desc.Text("Allows Debuffs to be placed on arts")
    for key,value in DebuffsDict.items():
        myDebuffs = "\n".join(DebuffsDict.keys())
    desc.Text(myDebuffs)
    
    desc.Header(Options.DriverArtsOption_Buffs.name)
    desc.Text("Allows Buffs to be placed on arts.")
    for key,value in BuffsDict.items():
        myBuffs = "\n".join(BuffsDict.keys())
    desc.Text(myBuffs)
    
    return desc