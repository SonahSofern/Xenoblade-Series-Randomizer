# XC2_Randomizer
A randomizer project for Xenoblade 2



# General Description
This program randomizes the BDAT files in Xenoblade Chronicles 2. Tested on the main story of the English Version 2.1.0 + DLC only. The project is still a work in progress, please report bugs or suggestions to our discord so we can make this better!

# Contact Us
Discord: https://discord.gg/h93yqZHG8z

# Known Issues
Race Mode will overwrite some settings. (for example Treasure Chest Contents will be overwritten if race mode is on)\
Torna has not been tested at all, it may or may not work.\

# Credits
https://github.com/roccodev/bdat-rs
https://frontiernav.net/wiki/xenoblade-chronicles-2
https://xenobladedata.github.io/
https://gitlab.com/damysteryman/XC2SaveNETThingy/-/tags/r6.1

# Setup

### Requirements:
[Python v3.11.0](https://www.python.org/downloads/release/python-3110/)\
Legal Dump of Xenoblade 2 Switch v2.1.0 + All DLC\
Homebrewed Switch or Emulator\
[NXDumpTool](https://github.com/DarkMatterCore/nxdumptool)\
[Xenoblade 2 Set](https://gbatemp.net/threads/xenoblade-chronicles-2-graphics-settings.529436/)

### Console Also Requires:
microSD card (A 16GB minimum exFAT-formatted microSD card is recommended; FAT32 seems to mess stuff up.)\
Modded Nintendo Switch with Atmosphere


### Process:
Guide adapted from: https://gamebanana.com/tuts/13815\

1. Use NXDumpTool to dump XC2's RomFS.
2. Put your microSD card into your computer, and locate "bf2.ard" and "bf2.arh"; those are the only two important files. Everything else in the dump can be safely deleted.
3. Download Xenoblade2Set from (https://gbatemp.net/threads/xenoblade-chronicles-2-graphics-settings.529436/), and extract its contents.
4. Copy bf2.ard and bf2.arh to the Xenoblade2Set folder, and run "quickbms_4gb_files.exe".
5. It will ask for a "bms script"; select Xenoblade2ard.bms. It will then ask for "archives/files"; select bf2.arh. For "output folder", go into the empty "modified" folder and press "Save". The files should extract, it may take a bit.
6. CONSOLE ONLY: There should now be a new "bdat" folder inside "modified"; This is the folder that the randomizer program targets as the input folder. The output folder should be /atmosphere/contents/0100E95004039001/romfs/bdat on your microSD card.
7. EMULATOR ONLY: There should now be a new "bdat" folder inside "modified"; This is the folder that the randomizer program targets as the input folder. The output folder should be the emulator's name then /load/0100E95004039001/Randomizer/romfs/bdat .
8. Choose your preferred settings, then use the randomizer program to randomize the contents of the game.
9. CONSOLE ONLY: Put your microSD card back into your Switch, use Atmosphere and Homebrew to launch the game. Pressing L bypasses the active patches, so if you wish to play the vanilla game again, you can do so in this way.