import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
resp = requests.get(url)

data = BeautifulSoup(resp.text, 'html.parser')

kospi = data.select_one('#KOSPI_now').text

print(kospi)

