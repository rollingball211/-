#while문을 빠져나가지 않고 while문의 맨 처음으로 돌아가고 싶을떄

a=0
while a<10:
    a=a+1
    if a%2 ==0: continue#a를 2로 나누었을때 0이면 맨 처음으로 돌아감
    print(a)

#무한 루프 
#while True: 사용
while True:

    print("Ctrl+C를 눌러야 빠져나갈수 있습니다")