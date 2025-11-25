import glob 
import os
dirname = "Lakersve/"
filelist = sorted(glob.glob(f"{dirname}/TP*"))

print(filelist)

for team in filelist:
    os.makedirs(f'./images/{team}',exist_ok=True)
    
    # 0 - 828: The name of the team as bitmap
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 0 --length 828 --rows 18 --cols 92 --image ./images/{team}/team_name.png'
    os.system(cmd)
    
    # 828 - 1608: The logo of the team 30x52
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 828 --length 780 --rows 30 --cols 52 --image ./images/{team}/logo.png'
    os.system(cmd)
    
    # 1608 - 3192: Roster name sprites, alphabetically (based on surname)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 1608 --length 1584 --rows 72 --cols 44 --image ./images/{team}/names.png'
    os.system(cmd)

    # 3192 - 3204: Indices of the players, how the alphabetically ordered names are mappes to the roster
    # Values multiples of two, e.g. 00, 02, 04, ... 16
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 3192 --length 12 --rows 12 --cols 2 --image ./images/{team}/player_indices.png --overlay --pixel-size 40'
    os.system(cmd)
    
    # 3204 - 4000
    
    # 4000 - 4012: Heights, one byte each, values only 0, 1, or 2 (shortest to highest), mapped to the alphabetical sorting
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 4000 --length 12 --rows 12 --cols 2 --image ./images/{team}/heights.png --overlay'
    os.system(cmd)
    
    # 4012 - 5212: Sprites of the heads in 5 directions for each player
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 4012 --length 1200 --rows 300 --cols 8 --image ./images/{team}/all_heads.png'
    os.system(cmd)
    
    # 5212 - 5224: Skin color, full byte! Why? 0 black, 1, white
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 5212  --length 12 --rows 1 --cols 24 --image ./images/{team}/skin_color.png --overlay'
    os.system(cmd)
    
    # 5224 - 5272: 48 bytes unkown 12x10 nibbles. Stats? Setting all to 00 crashes, same for 01
    # First 12 bytes take only multiples of 2
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 5224  --length 60 --rows 4 --cols 24 --image ./tests/{team.split("/")[-1]}_5212-5271.png --overlay'
    os.system(cmd)
    
    # 5272 - 5382 (end of file): Score board name 5 x 44 array
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 5272 --length 110 --rows 5 --cols 44 --image ./images/{team}/score_name.png'
    os.system(cmd)









