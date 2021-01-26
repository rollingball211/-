#5 range.
a= range(10) #0부터 10미만의 숫자를 포함하는 range 객체 생성. 끝숫자 포함x
print(a)

sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60: continue
    print("%d번 학생 축하합니다.합격입니다." %(number+1))
#len 함수는 리스트 내 요소으 ㅣ개수를 돌려주는 함수.

#99단
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ") #i*j를 다음줄로 넘기지 않기 위해
    print('') #2단 ..n단 구분하기위해.