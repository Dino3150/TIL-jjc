# A very simple Flask Hello World app for you to get started with...
import random
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    pick = random.sample(range(1, 46), 6)
    return f'{pick}'

# 1. /lotto
@app.route('/lotto')
def lotto():
    # 파이썬 코드
    pick = random.sample(range(1, 46), 6)
    # 보여줄 것을 문자열로
    return f'{pick}'

# 응답
# 사용자가 요청 보낼 URL 패턴 만들고
@app.route('/dinner')
# 함수를 만들어서
def dinner():
    # 반환하는 것!
    dinner_box = ['카레', '피자', '동원참치삼각김밥', '마라탕', '핫도그', '제육', '돈까스', '피자', '치킨',  '족발', '라면', '초밥', '삼겹살', '샐러드', '꽃등심은 친구에게']
    menu = random.sample(dinner_box, 2)
    return f'{menu[0]} 먹을래? {menu[1]} 먹을래?'

# 이거 하려면 추가 설정이 필요합니다!
# 주소를 크롬창에 요청한번 보내주세요!

@app.route('/telegram', methods=['POST'])
def telegram():
    TOKEN = '1828002930:AAEiH1EYxkSUgCixN9DpfK2ltT_eb1j7wa8'
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
    response = request.get_json()
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == '/로또':
        text = random.sample(range(1, 46), 6)
    send_message_url = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}'
    response = requests.get(send_message_url).json()
    return 'hi'