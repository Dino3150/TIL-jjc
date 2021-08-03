# 반복문
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(fact(4))


# 재귀함수
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(4))


# 피보나치 수열
def fib(n):
    # base case
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))


## 반복문
def fibo_for(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a+b
    return b

print(fibo_for(5))
