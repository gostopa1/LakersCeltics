# Download the ZIP file of the game
wget https://archive.org/download/msdos_Lakers_versus_Celtics_and_the_NBA_Playoffs_1989/Lakers_versus_Celtics_and_the_NBA_Playoffs_1989.zip
# Unzip
unzip Lakers_versus_Celtics_and_the_NBA_Playoffs_1989.zip
# Unzip and overwrite 
unzip -o Lakers_versus_Celtics_and_the_NBA_Playoffs_1989.zip 


# Extract all images from teams
python scripts/extract_all_team_images.py

# SUBDAT
python ./scripts/visualize_4bit.py Lakersve/SUBDAT --offset 0  --length 60 --rows 7 --cols 96 --image ./images/players-stats.png
python ./scripts/visualize_4bit.py Lakersve/SUBDAT --offset 336  --length 60 --rows 7 --cols 96 --image ./images/year_stats-offense.png
python ./scripts/visualize_4bit.py Lakersve/SUBDAT --offset 672  --length 60 --rows 7 --cols 96 --image ./images/year_stats-defense.png
# python ./scripts/visualize_4bit.py Lakersve/SUBDAT --offset 1008  --length 100 --rows 40 --cols 256 --image ./block.png --overlay


python ./scripts/visualize_4bit.py Lakersve/TP5 --offset 5212  --length 60 --rows 5 --cols 24 --image ./block.png --overlay
#python ./scripts/set_values.py Lakersve/TP5 --offset 5212  --length 6 --values "1"
unzip -o Lakers_versus_Celtics_and_the_NBA_Playoffs_1989.zip 
python ./scripts/set_values.py Lakersve/TP1 --offset 5224  --length 72 --values "01"
python ./scripts/set_values.py Lakersve/TP5 --offset 5260  --length 24 --values "FF"
python ./scripts/set_values.py Lakersve/TP1 --offset 5260  --length 24 --values "00"
python ./scripts/visualize_4bit.py Lakersve/TP5 --offset 5224  --length 12 --rows 4 --cols 24 --image ./block.png --overlay

open /Users/tan/DosStuff/dosbox-x-macosx-arm64-20251007154914/dosbox-x/dosbox-x.app --args /Users/tan/DosStuff/LakersCeltics/Lakersve/BBALL.EXE

# github-personal
# git remote set-url origin git@github-personal:gostopa1/LakersCeltics.git

# Test scenario: Add last row of attributes all FF for Lakers and all 00 for Celtics. Let em play
python ./scripts/set_values.py Lakersve/TP5 --offset 5260  --length 24 --values "FF"
python ./scripts/set_values.py Lakersve/TP1 --offset 5260  --length 24 --values "00"
python ./scripts/visualize_4bit.py Lakersve/TP5 --offset 5224  --length 12 --rows 4 --cols 24 --image ./block.png --overlay
