# Copied TP5 to TP1 so that both teams are identical. 
#Then changed the stats of TP5 to be as high as the best players
# And TP1 as low as the best players
# The only noticable difference was the fatigue. 
# TP1 was getting more tired, not like crazy, but clearly more fatigue

# By default when copying one team to another, Los Angeles (the original) win

# Try in Arcade and Regular Season
unzip -o Lakers_versus_Celtics_and_the_NBA_Playoffs_1989.zip 
rm ./Lakersve/TP1
cp ./Lakersve/TP5 ./Lakersve/TP1
# Multiples of 2?
#python ./scripts/set_values.py Lakersve/TP5 --offset 5224  --length 24 --values "18"
#python ./scripts/set_values.py Lakersve/TP1 --offset 5224  --length 24 --values "02"

# This seems to have opposite effect. Low values, better result !?
#python ./scripts/set_values.py Lakersve/TP5 --offset 5236  --length 24 --values "12"
#python ./scripts/set_values.py Lakersve/TP5 --offset 5236  --length 24 --values "00"
#python ./scripts/set_values.py Lakersve/TP1 --offset 5236  --length 24 --values "FF"

#3rd stat category
#python ./scripts/set_values.py Lakersve/TP5 --offset 5248  --length 24 --values "28"
# When all are FF it seems to affect the choice of players and the computer is doing continuous changes
# This seems to be the most important
python ./scripts/set_values.py Lakersve/TP5 --offset 5248  --length 24 --values "08"
python ./scripts/set_values.py Lakersve/TP1 --offset 5248  --length 24 --values "FF"

# Free throws?
#python ./scripts/set_values.py Lakersve/TP5 --offset 5260  --length 24 --values "FF"
#python ./scripts/set_values.py Lakersve/TP1 --offset 5260  --length 24 --values "00"
python ./scripts/visualize_4bit.py Lakersve/TP5 --offset 5224  --length 12 --rows 4 --cols 24 --image ./block.png --overlay
python ./scripts/visualize_4bit.py Lakersve/TP5 --offset 5224  --length 12 --rows 4 --cols 24 --image ./tests/Lakers_5224-5272.png --overlay
python ./scripts/visualize_4bit.py Lakersve/TP1 --offset 5224  --length 12 --rows 4 --cols 24 --image ./tests/Celtics_5224-5272.png --overlay
open /Users/tan/DosStuff/dosbox-x-macosx-arm64-20251007154914/dosbox-x/dosbox-x.app --args /Users/tan/DosStuff/LakersCeltics/Lakersve/BBALL.EXE
open /Users/tan/DosStuff/dosbox-x-macosx-arm64-20251007154914/dosbox-x/dosbox-x.app --args "/Users/tan/DosStuff/LakersCeltics/Lakersve/BBALL.EXE TANDY"



# Takeaways: 
# 1. The first row takes only multiples of 2
# The second stats category seems to be inverse, when high, it has negative effect
# The 3rd row can take FFs, but not zeros (?). If everything is FF, the computer goes crazy with subs during breaks
# The last row allows FF, probably related to fatigue
# With seemingly identical statistics, even when copying two identical teams, the original Lakers win. Is it indexing from somewhere else some stats?
# Simulation mode, make players to get tired. 