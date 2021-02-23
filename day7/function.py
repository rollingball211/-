#1.abs(x) 그 숫자의 절댓값을 돌려주는 함수
print(abs(-3))
#2.all(x) 반복 가능한 자료형x를 입력 인수를 받으며, x가 모두 참이면 True,하나라도 거짓이면 False 리턴
print(all([1,2,3,0]))
#3.any(x) x중 하나라도 참이 있을 경우 True를 리턴, x가 모두 거짓일 경우에만 False 리턴
print(any([1,0,0]))
#4.chr(i) 아스키 코드 값을 입력으로 받아 코드에 해당하는 문자를 출력하는 함수.
print(chr(97))
#5.dir 객체가 자체적으로 가지고있는 변수나 함수를 보여줌.
#6 divmod(a,b) 두개의 숫자를 입력으로 받고 a를 b로 나눈 몫과 나머지를 튜플형태로 리턴.
print(divmod(1.3,0.2))
#7 enumerate (열거) 순서가 있는 자료형을 입력으로 ㅂ다아 인덱스 값을 포함하는 enumerate 객체로 리턴
for i,name in enumerate(['body','far','bar']):
    print(i,name)
#8 eval(Expression) 실행 가능한 문자열 을 입력으로 받아 문자열을 싱행한 결과값 리턴
print(eval("'hi'+'a'"))
#9 lambada def와 동일한 역할을 함.
sum = lambda a,b: a+b
print(sum(3,4))