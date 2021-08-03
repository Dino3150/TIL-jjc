try:
    num = input('숫자입력 : ')
    print(int(num))
except ValueError:
    print('숫자가 아닙니다.')

######################################

my_dict = {'key' : 'value'}

# EAFP
# 예외처리를 활용하여 검사를 수행하지 않고 일단 실행하고 예외처리를 진행하는 스타일
# 파이썬 코드가 문제 없이 '실행될 것'을 전제로 코드를 실행
try :
    x = my_dict['key']
except KeyError:
    pass


# LBYL
# 도약하기 전에 봐라
# 어떤 것이 실행하기 전에 에러가 날만한 요소들을 조건문으로 검사를 하고 실행
if 'key' in my_dict:
    x = my_dict['key']
else:
    pass