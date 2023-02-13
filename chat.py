import os
import requests
from bs4 import BeautifulSoup

dir_name='张学友歌曲'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# 请求网站，获取Response对象
url='https://wapbaike.baidu.com/item/%E5%BC%A0%E5%AD%A6%E5%8F%8B/77479?&fr=aladdin#2'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
response = requests.get(url, headers=headers)

# 解析HTML网页
html = response.text  # 获取页面文本
soup = BeautifulSoup(html, 'lxml')  # 使用BeautifulSoup解析页面
table = soup.find('table')  # 定位列表所在的table
tr_list = table.find_all('tr')  # 找出所有的tr

# 获取歌曲名与下载路径
for tr in tr_list[1:]:
    song_name = tr.find_all('td')[0].text.strip()  # 歌曲名
    download_link = tr.find_all('td')[2].a['href']  # 下载路径

# 下载歌曲
song_data = requests.get(download_link).content
with open (dir_name+'/'+song_name+'.mp3', mode='wb') as fp:
    fp.write(song_data)
