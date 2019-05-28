from urllib.request import urlopen
import re
import time
from wars2csa import writecsa, warskifu2csa

def crawl_kifu_url(url, dpt):
    if dpt<1:
        f = urlopen(url)
        encoding = 'utf-8'
        text = f.read().decode(encoding)
        for m in re.finditer(r'<a href=\"//(.*)\">', text):
            tmp_url = m.group(0)
            tmp_url = re.sub(r'<a href=\"', '', tmp_url)
            tmp_url = re.sub(r'\">', '', tmp_url)
            filename = re.sub(r'//kif-pona.heroz.jp/games/', '', tmp_url)
            filename = re.sub(r'\?locale=ja', '', filename)
            tmp_kifu = crawl_raw_kifu('https:'+tmp_url)
            writecsa(tmp_kifu, filename)
    else:
        for i in range(dpt):
            crawl_kifu_url(url+'&start='+str((i+1)*10), 0)
            time.sleep(5)
            

def crawl_raw_kifu(url):
    f = urlopen(url)
    encoding = 'utf-8'
    text = f.read().decode(encoding)
    kifu = re.search(r'receiveMove.*', text).group(0)
    kifu = re.sub(r'receiveMove\("', '', kifu)
    kifu = re.sub(r'"\);', '', kifu)
    return kifu

def crawl_raw_kifu_test(url, filename):
    print(url)
    f = urlopen(url)
    encoding = 'utf-8'
    text = f.read().decode(encoding)
    with open(filename+".txt", "w") as f:
        f.write(text)
    kifu = re.search(r'receiveMove.*', text).group(0)
    kifu = re.sub(r'receiveMove\("', '', kifu)
    kifu = re.sub(r'"\);', '', kifu)
    return kifu

def crawl_kifu_url_test(url, dpt):
    if dpt<1:
        f = urlopen(url)
        encoding = 'utf-8'
        text = f.read().decode(encoding)
        with open("lists"+".txt", "w") as f:
            f.write(text)
        print(text)
        print('')
        strategies = re.finditer(r'<div class=\"game_params\">\n((.*)<span>(.*)</span>\n)*', text)
        for m, strategy in zip(re.finditer(r'<a href=\"//(.*)\">', text), strategies):
            tmp_url = m.group(0)
            tmp_url = re.sub(r'<a href=\"', '', tmp_url)
            tmp_url = re.sub(r'\">', '', tmp_url)
            filename = re.sub(r'//kif-pona.heroz.jp/games/', '', tmp_url)
            filename = re.sub(r'\?locale=ja', '', filename)
            tmp_kifu = crawl_raw_kifu_test('https:'+tmp_url, filename)
            writecsa(tmp_kifu, filename)
    else:
        for i in range(dpt):
            print("tmp_url: " + url+'&start='+str((i+1)*10))
            crawl_kifu_url_test(url+'&start='+str((i+1)*10), 0)
            time.sleep(5)
            
def scrape_strategy(tmp_game):
    tmp_strategy = re.finditer(r'#(.*)</a>', tmp_game)
    for m in tmp_strategy:
        tmp = m.group()
        tmp = re.sub(r'</a>', '', tmp)
        tmp = re.sub(r'#', '', tmp)
