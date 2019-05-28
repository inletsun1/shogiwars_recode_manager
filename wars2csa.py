#coding:utf-8
import re

def warskifu2csa(wars_kifu):
    kifu = re.split(r'\t|,', wars_kifu)
    kifu = kifu[0::2]
    if kifu[-1]=='SENTE_WIN_TORYO':
        kifu[-1] = '%TORYO'
    return kifu

def scrape_strategy(strategy):
    strategy = strategy.group()
    tmp_strategy = re.finditer(r'#(.*)</a>', strategy)
    for m in tmp_strategy:
        tmp = m.group()
        tmp = re.sub(r'</a>', '', tmp)
        tmp = re.sub(r'#', '', tmp)

def writecsa(wars_kifu, strategy, filename):
    with open(filename+'.csa', 'w') as f:
        #csaファイル形式のバージョン
        version = 'V2.2\n'
        #開始局面の設定
        HIRATE = 'P1-KY-KE-GI-KI-OU-KI-GI-KE-KY\nP2 * -HI *  *  *  *  * -KA * \nP3-FU-FU-FU-FU-FU-FU-FU-FU-FU\nP4 *  *  *  *  *  *  *  *  * \nP5 *  *  *  *  *  *  *  *  * \nP6 *  *  *  *  *  *  *  *  * \nP7+FU+FU+FU+FU+FU+FU+FU+FU+FU\nP8 * +KA *  *  *  *  * +HI * \nP9+KY+KE+GI+KI+OU+KI+GI+KE+KY\n'
        kifu = warskifu2csa(wars_kifu)
        f.write(version)
        f.write(HIRATE)
        f.write('\'sashite\n')
        for i in range(len(kifu)):
            f.write(kifu[i]+'\n')
