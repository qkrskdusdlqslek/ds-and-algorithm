# file : ds24_forFactorial.py
# desc : 반복문으로 팩토리얼 구하기 

n = 10
factValue = 1 # 곱셈이기 때문에 1부터 시작

for i in range(n, 0, -1): # 10부터 1까지 역순으로
    factValue *= i

print(f'{n}! = {factValue}')

# 재귀호출 factorial
def facotrial(num):
    if num <= 1: return 1
    
    return num * facotrial(num-1)

print(f'{n}! = {facotrial(n)}')
# 10 = 3628800, 20 = 2432902008176640000, 30 = 265252859812191058636308480000000
# 재귀호출 1000을 하면 RecursionError: maximum recursion depth exceeded 재귀호출 최고 깊이를 초과

