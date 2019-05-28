from urllib.request import urlopen
import re

url = 'https://shogiwars.heroz.jp/users/michael_sun'
kakoi_url = 'https://shogiwars.heroz.jp/users/michael_sun/trophy/1?locale=ja'
f = urlopen(kakoi_url)
encoding = 'utf-8'
text = f.read().decode(encoding)

print(text)

