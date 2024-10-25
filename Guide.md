./bdat-toolset-win64.exe extract ./common.bdat -o ./OutputBDAT -f json --pretty (load original bdat)
./_internal/Toolset/bdat-toolset-win64.exe pack ./_internal/JsonOutputs -o C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat -f json
python -m PyInstaller XC2_Randomizer.spec (Compiles to distributable)


MY PATHS
C:/Users/benja/Desktop/XC2_Randomizer/bdat
C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat

