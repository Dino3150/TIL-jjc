import requests

location = 'https://www.metaweather.com/api/location/1132599/'
ii = [0,1,2,3,4]

resp = requests.get(location).json()
print(type(resp))

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


for i in ii:
    day = resp["consolidated_weather"][i]
    print(f'{day["applicable_date"]} {resp["title"]}의 날씨는 {trans[day["weather_state_name"]]}입니다. 최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}입니다.')


