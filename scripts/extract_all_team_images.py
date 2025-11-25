import glob 
import os
dirname = "Lakersve/"
filelist = sorted(glob.glob(f"{dirname}/TP*"))

print(filelist)

for team in filelist:
    os.makedirs(f'./images/{team}',exist_ok=True)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 0 --length 828 --rows 18 --cols 92 --image ./images/{team}/team_name.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 828 --length 780 --rows 30 --cols 52 --image ./images/{team}/logo.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 1608 --length 1584 --rows 72 --cols 44 --image ./images/{team}/names.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 4012 --length 100 --rows 25 --cols 8 --image ./images/{team}/one_head_all_versions.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 4012 --length 1200 --rows 300 --cols 8 --image ./images/{team}/all_heads.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 5272 --length 110 --rows 5 --cols 44 --image ./images/{team}/score_name.png'
    os.system(cmd)
    cmd = f'python ./scripts/visualize_4bit.py {team} --offset 4000 --length 6 --rows 12 --cols 1 --image ./images/{team}/heights.png --overlay'
    os.system(cmd)









