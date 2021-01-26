#집합(set)

s1 = set([1,2,3])
#set 키워드를 만들어 사용
print(s1)

s2= set("Hello")
print(s2)
#중복 허용 x , 순서가 없음=> 리스트와 튜플과는 다르게 인덱싱 불가능.

#교집합 합집합 차집합
s3= set([1,2,3,4,5,6])
s4= set([4,5,6,7,8,9])

print(s3&s4)
print(s3.intersection(s4))
#교

print(s3|s4)
print(s3.union(s4))
#합

print(s3-s4)
print(s3.difference(s4))
#차

#값 1개 추가하기(add)
s1.add(4)
print(s1)
#값 여러개 추가 (update)
s1.update([5,6,7])
print(s1)
#특정값 제거하기 (Remove)
s1.remove(2)
print(s1)

