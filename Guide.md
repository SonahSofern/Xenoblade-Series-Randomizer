./bdat-toolset-win64.exe extract ./common.bdat -o ./OutputBDAT -f json --pretty (load original bdat)
./_internal/Toolset/bdat-toolset-win64.exe pack ./_internal/JsonOutputs -o C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat -f json
python -m PyInstaller XC2_Randomizer.spec     (Compile to a single exe file, not sure if rust tool will work this way) (spits it out to dist)

Click Randomize
turns your common.bdat into json
changes/randomizes values of the json based on sliders values
change back to bdat
automatically downloads it when done

C:/Users/benja/Desktop/XC2_Randomizer/bdat
C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat

