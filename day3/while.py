#while문 기본구조
#while 조건문:
#수행할 문장1...
#수행할 문장n
#while문 => 조건문이 참을 동안에 while문 아래에 속하는 문장들이계속해서 수행됨

TreeHit= 0
while TreeHit<10:
    TreeHit=TreeHit+1
    print("나무를 %d번 찍었습니다" %TreeHit)
    if TreeHit==10:
        print("나무가 넘어갑니다")