import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

print(soup.select('#logo'))    # 搜尋 id 為 logo 的 tag 內容
print('\n--------------------\n')

print(soup.find_all('div', id="header"))
print('\n--------------------\n')

divs = soup.find_all('div')
print(divs[1])
print('\n--------------------\n')

print(divs[1].find_parent().find_all('li')) # 從搜尋到的項目裡，尋找父節點裡所有的 li
print('\n-------------------------\n')

print(soup.find(id="nav_dom_int_sub"))

print(soup('a'))

print(soup('a', limit=2))

print(soup.find_all('a', string='Domains'))
