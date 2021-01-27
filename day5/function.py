#파이썬 함수 
"""
def 함수명(입력 인수):
    수행할 문장1
    수행할 문장2
"""

def sum(a,b):
    return a+b

a=3
b=4
c=sum(a,b)
print(c)

"""
일반적인 함수
def 함수명(입력 인수):
    수행할 문장1
    return 결과값
"""

def sum1(a,b):
    result = a+b
    return result

d= sum1(3,4)
print(d)

def say():
    return "Hi"
e= say()
print(e)

def sum2(a,b):
    print("%d와 %d의 합은 %d입니다" %(a,b,a+b))

f= sum2(3,4)

def say1():
    print('hi')

say1()

#여러개의 입력값을 받는 함수 만들기.
def sum_many(*args):
    sum =0
    for i in args:
         sum = sum + i
    return sum

result1 = sum_many(1,2,3)
result2 = sum_many(1,2,3,4,5,6,7,8,9,10)

print(result1)
print(result2)
