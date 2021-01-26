#리스트 자료형
#리스트명 = [요소1,요소2...요소n]

a=[1,2,3]
print(a)
print(a[0])

print(a[0]+a[2])

b=[1,2,3,['a','b','c']] #(a,b,c)는 b리스트의 4번째 element.
print(b[0])
print(b[-1])
print(b[3])

print(b[-1][0]) #b리스트 안의 abc리스트중 첫번째 element 꺼내옴.

#list slicing 
c =[1,2,3,4,5]
print(c[0:2])

#list adding
d = [1,2,3]
e = [4,5,6]
print(d+e)
#list Repetition
print(d*3)

#list modify & delete
f= [1,2,3]
f[2]=4
print(f)
f[1:2]=['a','b','c']
print(f)
f[1:3]= []
print(f)
#del 함수 이용해 삭제
del f[1]
print(f)


