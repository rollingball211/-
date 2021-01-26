#딕셔너리 자료형
#key를 통해 value를 얻음.
#{Key1:Value1,Key2:Value2....}
dic = {'name':'pey','phone':'01040735281','birth':'1013'}

a={1:'hi'}
b={'a':[1,2,3]} #value에 리스트 넣기 가능
#딕셔너리 쌍 추가
c ={1:'a'}
c[2] ='b' #{2:'b'} 쌍 추가
print(c)
c['name']='pey'
print(c)
c[3] =[1,2,3]
print(c)
#삭제하기
del c[1] #key가 1인 value 삭제
print(c)

d = {1:'a',2:'b'}
print(d[1]) #key가 1인 요소의 value를 반환
print(d[2])

#key 리스트 만들기(keys) key만 반환.
print(dic.keys())
print(list(dic.keys())) #key값 리스트로 만들기.

#value 리스트 만들기 (values)
print(dic.values())

print(list(dic.values()))
#key, value 쌍 얻기(items)
print(dic.items())

#key로 value 얻기 (get)
print(dic.get('name'))

#해당 key가 딕셔너리 안에 있나 조사하기
print('name'in dic)
print('email' in dic)

#key value 쌍 모두 지우기 clear
dic.clear()
print(dic)