import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

response = requests.get(url).text
print(response)


data = BeautifulSoup(response)

kospi = data.select_one('#KOSDAQ_now')

print(kospi.text)