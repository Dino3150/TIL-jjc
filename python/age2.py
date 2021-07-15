# requests
import requests


'''
tak, tony, eric, musk
4명의 나이를 확인하는 코드
'''

# 1. url 만들어서 요청 보냄
url = 'https://api.agify.io/?name=david'
response = requests.get(url)

# 2. 결과 json을 변환
result = response.json()

# response = requests.get(url).json()
print(result)

# 3. 딕셔너리 구조에서 원하는 값만 출력


## 추가 코드
# tak, tony, eric, musk


