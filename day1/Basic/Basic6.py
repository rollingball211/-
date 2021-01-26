#문자열 관련 함수들.

#1.문자 개수 세기 (count)
a="hobby"
print(a.count('b'))
#2.위치 알려주기(find)
b="Python is best choice"
print(a.find('b'))
#없다면 -1을 반환
print(a.find('k'))
c ="Life is too short"
print(c.index('t'))

#문자열 삽입 join
d= ","
print(d.join('abcd'))
#소문자 대문자로 바꾸기 upper 대문자 소문자 바꾸기 lower
e= "hi"
print(e.upper())
print(e.lower())
#공백 지우기 strip ,lstrip , rstrip 한칸 이상의 연속된 공백들을 모두 지움
f=" hi "
print(f.strip())
print(f.lstrip())
print(f.rstrip())
#문자열 바꾸기 replace 
g="Life is too short"
print(g.replace("Life","Your leg"))
#문자열 공백을 기준으로 문자열 나눔 split
print(g.split()) #공백을 기준으로 문자열 나눔
h="a:b:c:d"
print(h.split(':')) #기호를 기준으로 문자열을 나눔