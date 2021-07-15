# requests
import requests

'''
tak, tony, eric, musk
4명의 나이를 확인하는 코드
'''

# 1. url 만들어서 요청 보냄
persons = ['tom', 'tony', 'eirc', 'musk']
for person in persons:
    url = f'https://api.agify.io?name={person}'
    response = requests.get(url).json()
    print(f'{response["name"]}은(는) {response["age"]}세 입니다.')

# 3. 딕셔너리 구조에서 원하는 값만 출력

