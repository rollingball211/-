#1.리스트에 요소 추가 append
a=[1,2,3]
a.append(4)
print(a)
#리스트 안에는 어떤 자료형도 추가 가능
a.append([5,6])
print(a)

#2.리스트 정렬 sort
b=[1,4,3,2]
b.sort()
print(b)
#문자 알파벳 순서로 정렬가능
c=['a','c','b']
c.sort()
print(c)

#리스트 뒤집기 reverse
c.reverse()
print(c)

#위치 반환 index index함수는 리스트에 x라는 값이 있으면 x의 위치값 리턴
d=[1,2,3]
print(d.index(3))
print(d.index(1))

#리스트에 요소 삽입 inserrt

e=[1,2,3]
e.insert(0,4) #a[0] 위치에 4 삽입
print(e)

#remove(x) 리스트에서 첫번째로 나오는 x 삭제
f= [1,2,3,1,2,3]
f.remove(3)
print(f)

#리스트에 포함된 요소 x의 개수 세기
g= [1,2,3,1]
print(g.count(1))

#리스트 확장 extend(x) x에는 리스트만 올수 있으며 , 원래의 리스트에 x리스트를 더하게 됨
a.extend([4,5])
print(a)
h=[6,7]
a.extend(h)
print(a)
