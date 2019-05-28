from classify_strategy import *
import glob 
import os
import shutil


kifu_dir = './kifu/*.csa'
files = glob.glob(kifu_dir)
kakoi_files = glob.glob('./kakoi/*.csa')

def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

print("start")
for filename in files:
    for kakoi_name in kakoi_files:
        kakoi = kakoi2string(kakoi_name)
        tmp_ban, sashite = kifu2string(filename)
        if isMatchKakoi(tmp_ban, sashite, kakoi):
            dirname = kakoi_name.split("/")
            dirname = dirname[2]
            dirname = './' + dirname[0:-4] + "/"
            mkdir(dirname)
            fn = filename.split("/")
            shutil.copy(filename, dirname + fn[-1])
print("finished")

rev_kakoi = reverseSenteGote(kakoi)
