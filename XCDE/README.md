# XCDE_Randomizer
A randomizer project for Xenoblade Chronicles 1 DE capable of randomizing: Enemies, Armors, Music, Loot and much more!


# General Description
This program randomizes the BDAT files in Xenoblade Chronicles 1 DE. Tested on the main story of the English Version 1.1.2. The project is still a work in progress, please report bugs or suggestions to our discord so we can make this better!

# Contact Us
Discord: https://discord.gg/h93yqZHG8z

# Known Issues
Future connected has not been tested at all, it may or may not work.


# Credits
https://github.com/roccodev/bdat-rs \
https://www.xenoserieswiki.org/wiki/Main_Page \
https://xenobladedata.github.io/

# Setup

### Requirements:
[Python v3.11.0](https://www.python.org/downloads/release/python-3110/)\
Legal Dump of Xenoblade 1 DE Switch v1.1.2\
Homebrewed Switch or Emulator\
[NXDumpTool](https://github.com/DarkMatterCore/nxdumptool)\
[XenoLib](https://github.com/PredatorCZ/XenoLib/)

### Console Also Requires:
microSD card (A 32GB minimum exFAT-formatted microSD card is recommended; FAT32 will split up your files and youll have to take an extra step to combine them.)\
Modded Nintendo Switch with Atmosphere


## Process:
If you have any issues come to the [discord](https://discord.gg/h93yqZHG8z) where we can help!

### Console
1. Use [NXDumpTool](https://github.com/DarkMatterCore/nxdumptool) to perform a full dump of XCDE's RomFS to your microSD card, and put it into your computer.
2. Inside the dump there should now be a folder named "bdat"; This is the folder that the randomizer program targets as the input folder. The output folder should be: This PC/Nintendo Switch/SD Card/atmosphere/contents/0100FF500E34A000/romfs/bdat (This is on your microsd card)
3. Choose your preferred settings, then use the randomizer program to randomize the contents of the game.
4. Put your microSD card back into your Switch and Launch the game. Pressing L bypasses the active patches, so if you wish to play the vanilla game again, you can do so in this way.
5. You should be ready to start playing!


### Emulator
1. Use your emulator's built-in tool to perform a full dump of XCDE's RomFS.
2. Inside the dump there should now be a folder named "bdat"; This is the folder that the randomizer program targets as the input folder. The output folder should be\
FOR YUZU: C:/Users/yourName/AppData/Roaming/yuzu/load/0100FF500E34A000/Randomizer/romfs/bdat\
> You will have to make the "Randomizer/romfs/bdat" folder path>
FOR RYUJINX: C:/Users/yourName/AppData/Roaming/Ryujinx/sdcard/atmosphere/contents/0100FF500E34A000/romfs/bdat\
> You will have to make the "romfs/bdat" folder path>
3. Choose your preferred settings, then use the randomizer program (.exe) to randomize the contents of the game.
4. You should be ready to start playing!



