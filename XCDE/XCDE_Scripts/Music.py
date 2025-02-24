import json, IDs, random

def MusicRando():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/bgmlist.json", 'r+', encoding='utf-8') as bgmFile:
        bgmData = json.load(bgmFile)
        for bgm in bgmData["rows"]:
            bgm["file_name"] = random.choice(Music)
        bgmFile.seek(0)
        bgmFile.truncate()
        json.dump(bgmData, bgmFile, indent=2, ensure_ascii=False)
        

Music = [
"f01_loop", # - Hometown
"f02_loop", # - Colony 9
"f03_loop", # - Tephra Cave
"f04_loop", # - Gaur Plain
"f05_loop", # - Colony 6 - Ether Mine
"f06_loop", # - Satorl Marsh
"f07_loop", # - Forest of the Nopon
"f08_loop", # - Frontier Village
"f10_loop", # - Where the Ancestors Sleep
"f11_loop", # - Eryth Sea
"f12_loop", # - Alcamoth, Imperial Capital
"f13_loop", # - Prison Island
"f14_loop", # - Valak Mountain
"f15_loop", # - Sword Valley
"f16_loop", # - Galahad Fortress
"f17_loop", # - The Fallen Land
"f18_loop", # - Hidden Machina Village
"f19_loop", # - Mechonis Field
"f20_loop", # - Agniratha, Mechonis Capital
"f21_loop", # - Central Factory
"f22_loop", # - Bionis Interior (Carcass)
"f23_loop", # - Colony 6 - Rebuilding / Restoration
"f24_loop", # - Memory's End (Spacey Ambience Song)
"f25_loop", # - In The Refugee Camp (Escape Boat Camping)
"f26_loop", # - The End Lies Ahead (To The Final Battle, Prison Island)
"f51_loop", # - Gran Dell FC
"f52_loop", # - Bionis' Shoulder FC

# Non-Default Environmental Songs

"a01_loop", # - Hometown
"a02_loop", # - Colony 9
"a03_loop", # - Gaur Plain
"a04_loop", # - Satorl Marsh
"a05_loop", # - Forest of the Nopon (Makna Forest)
"a06_loop", # - Frontier Village
"a08_loop", # - Eryth Sea
"a09_loop", # - Alcamoth, Imperial Capital
"a10_loop", # - Valak Mountain
"a11_loop", # - Sword Valley
"a12_loop", # - The Fallen Land
"a14_loop", # - Agniratha, Mechonis Capital
"a15_loop", # - Bionis Interior (Pulse)
"a16_loop", # - Colony 6 - Silence
"a17_loop", # - Colony 6 - Hope
"a18_loop", # - Colony 6 - Future 
"a51_loop", # - Gran Dell FC
"a52_loop", # - Bionis' Shoulder FC

# Combat Music

"b01_loop", # - Time to Fight!
"b02_loop", # - You Will Know Our Names
"b03_loop", # - Mechanical Rhythm
"b05_loop", # - An Obstacle in Our Path
"b06_loop", # - Zanza the Divine
"b07_loop", # - The God Slaying Sword
"b08_loop", # - Enemies Closing In
"b09_loop", # - Visions of the Future
"b10_loop", # - Searching Glance
"b11_loop", # - Irregular Bound
"b12_loop", # - Zanza's World
"b15_loop", # - A Tragic Decision
"b51_loop", # - Time to Fight! (Bionis Shoulder) FC
"b52_loop", # - Fogbeasts
"b53_loop", # - Roar from Beyond


# Cutscene Music

"e01_a" # - Prologue A
"e01_b" # - Prologue B
"e02" # - Main Theme (3:40)
"e02_loop" # - Main Theme Loop (7:30)
"e03" # - Unfinished Business
"e04" # - Engage the Enemy
"e05" # - Bionis' Awakening
"e06" # - Ancient Mysteries
"e07" # - A Spiritual Place
"e07_loop" # - A Spiritual Place Loop (5:29)
"e08" # - Epilogue
"e09" # - Memories
"e09_loop" # - Memories Loop (6:11)
"e10" # - Everyday Life (2:12)
"e10_loop" # - Everyday Life Loop (4:12)
"e11" # - Riki the Legendary Heropon
"e11_loop" # - Riki the Legendary Heropon Loop (5:03)
"e12_v1" # - Reminiscence 
"e12_v1_loop" # - Reminiscence Loop (6:13)
"e12_v2" # - Reminiscence (Music Box) 
"e12_v2_loop" # - Reminiscence (Music Box) Loop (6:06)
"e13" # - A Friend On My Mind
"e13_loop" # - A Friend On My Mind Loop (5:17)
"e14" # - Shulk and Fiora
"e14_loop" # - Shulk and Fiora Loop (6:14)
"e15" # - Apprehension
"e15_loop" # - Apprehension Loop (5:30)
"e16" # - Tension
"e16_loop" # - Tension Loop (5:48)
"e17" # - Face
"e17_loop" # - Face Loop
"e18" # - Disquiet -- The song that sounds like something banging in the wind
"e18_loop" # - Disquiet Loop
"e19" # - Apprehension
"e19_loop" # - Apprehension Looped
"e20" # - Crisis
"e20_loop" # - Crisis Looped (3:42)
"e21" # - Egil's Theme (Anger, Darkness of the Heart)
"e21_loop" # - Egil's Theme Looped (6:24)
"e22" # - Shadows Creeping
"e22_loop" # - Shadows Creeping Looped (6:10)
"e23_v1" # - Intrigue (2:32)
"e23_v1_loop" # - Intrigue Looped (5:14)
"e23_v2" # - Intrigue (v2) (2:48) -- Has more strings melody, more to it.
"e23_v2_loop" # - Intrigue (v2) Looped (5:46)
"e23_v3" # - Intrigue (v3) (2:48) -- Has even more strings melody!
"e23_v3_loop" # - Intriuge (v3) Looped (5:46)
"e24" # - Towering Shadow (Gigantic Silhouette)
"e24_loop" # - Towering Shadow Looped (5:49)
"e25" # - Sorrow
"e25_loop" # - Sorrow Looped (5:06)
"e26_v1" # - Once We Part Ways
"e26_v1_loop" # - Once We Part Ways Loop (6:56)
"e26_v2" # - Thoughts Enshrined (While I Think)
"e26_v2_loop" # - Thoughts Enshrined (6:52)
"e27" # - Regret
"e27_loop" # - Regret Looped (5:15)
"e28" # - The Battle Is Upon Us (The Night Before the Decisive Battle)
"e28_loop" # - The Battle Is Upon Us Looped (6:57)
"e29" # - Futures That Lie Ahead (To One's Own Future)
"e29_loop" # - Futures That Lie Ahead Looped (6:50)
"e30_v1" # - Majesty (Grandeur) 
"e30_v1_loop" # - Majesty Looped (7:22)
"e30_v2" # - Majesty (End-Game, Providence)
"e31_v1" # - Hope v1 (Unused Song) (3:18)
"e31_v1_loop" # - Hope v2 Looped (6:46)
"e31_v2" # - Hope v2 (1:35)
"e31_v2_loop" # - Hope v2 Looped (3:20)
"e32" # - Riki's Kindness (Riki's Tenderness)
"e32_loop" # - Riki's Kindness Looped (4:50)
"e33" # - The Monado Awakens (0:35)
"e34" # - Urgency (1:11)
"e34_loop" # - Urgency Loop (2:24)

# Achievement Jingles

"j01" # - Collectopaedia Line Completed
"j02" # - Collectopaedia Page Completed
"j03" # - New Objective Received
"j04" # - New Area Found
"j05" # - Secret Area Found
]