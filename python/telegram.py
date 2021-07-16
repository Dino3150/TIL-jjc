import requests

#정보
TOKEN = '1828002930:AAEiH1EYxkSUgCixN9DpfK2ltT_eb1j7wa8'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

# 1. url 요청하고, 결과를 python 자료구조로 저장
url = f'{BASE_URL}/getUpdates'
resp = requests.get(url).json()

# chat_id
chat_id = resp['result'][0]['message']['chat']['id']

# 날씨
weather = 'https://www.metaweather.com/api/location/1132599/'

resp2 = requests.get(weather).json()

trans = {
    'Snow' : '눈',
    'Sleet' : '진눈깨비',
    'Hail' : '우박',
    'Thunderstorm' : '뇌우',
    'Heavy Rain' : '비',
    'Light Rain' : '이슬비',
    'Showers' : '소나기',
    'Heavy Cloud' : '구름 많음',
    'Light Cloud' : '적은 구름 ',
    'Clear' : '맑음'
}

day = resp2['consolidated_weather'][0]
text = f'{day["applicable_date"]} {resp2["title"]}의 날씨는 {trans[day["weather_state_name"]]}입니다. 최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}입니다.'
send_msg = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_msg)
    
# 메시지 준비