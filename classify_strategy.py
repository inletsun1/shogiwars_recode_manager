import re

DEPTH_SEARCH = 40 #序盤戦法の分類に使用する手数

def kifu2string(filepath):
    #解析する棋譜ファイルの読み込み
    with open(filepath) as f:
        kifu = f.read()
        #開始局面を1次元のリストに変換
        tmp_ban = re.findall(r'P1.*\nP2.*\nP3.*\nP4.*\nP5.*\nP6.*\nP7.*\nP8.*\nP9.*\n', kifu)[0]
        tmp_ban_str = re.sub(r'[P1,P2,P3,P4,P5,P6,P7,P8,P9,\n]', '', tmp_ban)
        tmp_ban = [tmp_ban_str[i:i+3] for i in range(0, len(tmp_ban_str), 3)]
        sashite = re.findall(r'\'sashite\n.*', kifu, flags=(re.MULTILINE|re.DOTALL))[0]
        #指し手を抽出
        sashite = re.sub(r'\'sashite\n', '', sashite)
        sashite = re.split('\n', sashite)
        return tmp_ban, sashite

def kakoi2string(filepath):
    #分類する囲いや戦法ファイルの読み取り
    with open(filepath) as f:
        kakoi = f.read()
        kakoi = re.findall(r'P1.*\nP2.*\nP3.*\nP4.*\nP5.*\nP6.*\nP7.*\nP8.*\nP9.*\n', kakoi)[0]
        kakoi_str = re.sub(r'[P1,P2,P3,P4,P5,P6,P7,P8,P9,\n]', '', kakoi)
        kakoi = [[i, kakoi_str[3*i:3*(i+1)]] for i in range(0, len(kakoi_str)//3) if kakoi_str[3*i:3*(i+1)] != ' * ']
        return kakoi

def reverseSenteGote(kakoi):
    #引数の棋譜の先手と後手を入れ替える
    for i in range(len(kakoi)):
        kakoi[i][0] = 80 - kakoi[i][0]
        if kakoi[i][1][0] == '+':
            kakoi[i][1] = '-' + kakoi[i][1][1:]
        elif kakoi[i][1][0] == '-':
            kakoi[i][1] = '+' + kakoi[i][1][1:]
    return kakoi


def movePiece(tmp_ban, sashite, te):
    #現在の手番の指し手を指し、盤面を動かす
    tmp_sashite = sashite[te-1]
    if tmp_sashite=='%TORYO':
        return False
    #将棋盤の並びに合わせてリストのインデックスを指定
    before_pos = 9*int(tmp_sashite[2])-int(tmp_sashite[1])+1
    after_pos = 9*int(tmp_sashite[4])-int(tmp_sashite[3])+1

    tmp_ban[before_pos-1] = ' * '
    tmp_ban[after_pos-1] = tmp_sashite[0]+tmp_sashite[5:7]
    return tmp_ban

def isMatchKakoi(tmp_ban, sashite, kakoi):
    for te in range(1, DEPTH_SEARCH+1):
        flag = True
        tmp_ban = movePiece(tmp_ban, sashite, te)
        if tmp_ban==False:
            return False

        for te_kakoi in kakoi:
            if tmp_ban[te_kakoi[0]] == te_kakoi[1]:
                continue
            else:
                flag = False
                break
        if flag:
            break
    return flag

