from classify_strategy import *
import glob 


kifu_dir = './kifu/*.csa'
files = glob.glob(kifu_dir)
for filename in files:
    kakoi = kakoi2string('./kakoi/yokofu.csa')
    print(filename)
    tmp_ban, sashite = kifu2string(filename)
    if isMatchKakoi(tmp_ban, sashite, kakoi):
        print('横歩取り')
    else:
        print('力戦')

rev_kakoi = reverseSenteGote(kakoi)
