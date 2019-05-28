from crawling_kifu import crawl_kifu_url
from wars2csa import warskifu2csa, writecsa
import re

url = 'https://shogiwars.heroz.jp/users/history/ponainfinity?locale=ja'
dpt = 10

crawl_kifu_url(url, dpt)
