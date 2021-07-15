# 요청 보내주는 requests 를 가져온다.
import requests

url = 'https://api.agify.io?name=michael'

# 저장하는데, 이거 json이라서 리스트-딕셔너리 구조로 바꿔줘!
response = requests.get(url).json()
response_text = requests.get(url).text

print(response)
print(type(response))
print(response['age'])
print('===================')
# 저장하는데, 이거 text로 바꿔줘 -> BeautiSoup으로 구조화를 (HTML) -> 선택자