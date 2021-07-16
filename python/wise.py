'''
1. 랜덤 명언을 가져와서 변수에 저장
https://favqs.com/api/qotd
'''

import requests

# 0. URL
url = 'https://favqs.com/api/qotd'
# 1. 요청을 보내서 응답 받은 JSON을 파이썬 자료구조로
response = requests.get(url).json()
# 2. 해당 내용에서 필요한 부분 꺼내기
print(response['quote']['author'])
print(response['quote']['body'])
#