prompt="""
1.Add
2.Del
3.List
4.Quit

Enter number :"""

number =0;
while number!=4:
    print(prompt)
    number = int(input())
#While문을 탈출하는 문장 break

coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee=coffee-1
    print("남은 커피의 양은 %d입니다" %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
