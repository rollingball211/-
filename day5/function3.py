#입력 인수에 초깃값 미리 설정하기

def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다"%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("박응용",27)
