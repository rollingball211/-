"""
for 변수 in list(tuple or 문자열)
수행할 문장1
수행할 문장2
"""

#1.for 기본형

test_list =['one','two','three']
for i in test_list:
    print(i)

#2.다양한 FOR 문의 사용
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
#3.for문의 응용
marks = [90,25,67,45,80]
number=0
for mark in marks:
    number = number+1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number) 

#4.for문과 continue
number=0
for mark in marks:
    number = number+1
    if mark<60: continue
    print("%d번 학생 축하합니다! 합격입니다" %number)

