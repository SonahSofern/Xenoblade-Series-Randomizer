./bdat-toolset-win64.exe extract ./common.bdat -o ./OutputBDAT -f json --pretty (load original bdat)
./bdat-toolset-win64.exe pack ./BDAT_JSON -o C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat -f json (write to files)
python -m PyInstaller --onefile --windowed  page.spec     (Compile to a single exe file, not sure if rust tool will work this way)