from crawling_kifu import crawl_kifu_url_test
from wars2csa import warskifu2csa, writecsa
import re

#url = 'https://shogiwars.heroz.jp/users/history/michael_sun?locale=ja'
url = 'https://shogiwars.heroz.jp/users/history/michael_sun?gtype=sb&locale=ja'
dpt = 1

crawl_kifu_url_test(url, dpt)
