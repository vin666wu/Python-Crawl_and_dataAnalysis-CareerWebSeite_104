import requests
import pandas as pd
from IPython.display import clear_output

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',      #browser
       	'Referer': 'https://www.104.com.tw/'}                                                                   #last browse url(page)

df = []

for page in range(1,10):
	url = f'https://www.104.com.tw/jobs/search/list?ro=0&area=6001001000&order=12&asc=0&page={page}&mode=l'
	print(url)
	resp = requests.get(url, headers=headers)
	ndf = pd.DataFrame(resp.json()['data']['list'])
	df.append(ndf)
	if ndf.shape[0]<=30:
		break
df = pd.concat(df, ignore_index=True)
print(df)
