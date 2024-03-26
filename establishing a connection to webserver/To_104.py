import requests
import pandas as pd
from IPython.display import clear_output

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',      #browser
       	'Referer': 'https://www.104.com.tw/'}                                                                   #last browse url(page)
url = 'https://www.104.com.tw/jobs/search/list?ro=0&area=6001001000&order=12&asc=0&page=2&mode=l'
#get the data
resp = requests.get(url, headers=headers)
# DataFrame, JSON, first 3 rows
df = pd.DataFrame(resp.json()['data']['list']).head(3)
print(df)
