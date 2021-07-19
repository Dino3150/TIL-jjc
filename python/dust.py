import requests
from bs4 import BeautifulSoup

url = 'https://weather.naver.com/air/05140120'
resp = requests.get(url).text
resp2 = BeautifulSoup(resp, 'html.parser')
dust = resp2.select_one('#content > div > em > span.value _cnPm10Value')

print(dust)

