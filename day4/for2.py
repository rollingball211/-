#리스트 안에 for문 포함하기. 리스트 내포
a=[1,2,3,4]
result =[]
for num in a:
    result.append(num*3)
    
print(result)

result = [num *3 for num in a]
print(result)
#리스트 내포 
"""
표현식 for 항목 in 반복가능객체 if 조건
"""