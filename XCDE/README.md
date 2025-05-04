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
https://xenobladedata.github.io/ \

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


### Process:
If you have any issues come to the [discord](https://discord.gg/h93yqZHG8z) where we can help!

1. CONSOLE ONLY: Use NXDumpTool to perform a full dump of XCDE's RomFS to your microSD card, and put it into your computer.
2. EMULATOR ONLY: Use your emulator's built-in tool to perform a full dump of XCDE's RomFS.
3. Locate "bf2.ard" and "bf2.arh"; those are the only two important files.
> **IMPORTANT:** if your sdcard is formatted as fat32, bf2.ard might be split into a folder with multiple files inside. In this case you will have to combine them.\
> Open a command prompt and navigate to your bf2.ard folder\
> Depending on your OS run the following command:\
> **Windows: `copy /b` file1name `+` file2name `+` file3name `bf2.ard`\
> **Mac/Linux: `cat` file1name file2name file3name `> bf2.ard`\
> You should have the combined file now!
4. Download the latest release of [XenoLib](https://github.com/PredatorCZ/XenoLib), and extract its contents.
5. Drag and drop bf2.arh onto extract_arh.cmd.
6. It should automatically start extracting. Many empty filename id warnings are normal, wait until it finishes extracting.
7. It should output a zip folder and inside there should now be a folder named "bdat"; This is the folder that the randomizer program targets as the input folder. The output folder should be\
FOR YUZU: C:/Users/yourName/AppData/Roaming/yuzu/load/0100E95004039001/Randomizer/romfs/bdat\
FOR RYUJINX: C:/Users/yourName/AppData/Roaming/Ryujinx/sdcard/atmosphere/contents/0100e95004039001/romfs/bdat\
FOR CONSOLE: This PC/Nintendo Switch/SD Card/atmosphere/contents/0100E95004039001/romfs/bdat (This is on your microsd card)\
NOTE: You will have to create the 0100E95004039001 folder.
8. Choose your preferred settings, then use the randomizer program to randomize the contents of the game.
9. CONSOLE ONLY: Put your microSD card back into your Switch and Launch the game. Pressing L bypasses the active patches, so if you wish to play the vanilla game again, you can do so in this way.
10. You should be ready to start playing!