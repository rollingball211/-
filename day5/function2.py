def sum_mul(choice,*args):
    if choice =="sum":
        result = 0
        for i in args:
            result= result+i #args에 입력받은 모든 값을 더함.

    elif choice == "mul":
        result=1
        for i in args:
            result=result*i
    #return result


result1 =sum_mul('sum',1,2,3,4,5)
print(result1)
result2=sum_mul('mul',1,2,3,4,5)
print(result2)

def sum_and_mul(a,b):
    return a+b,a*b

result3=sum_and_mul(3,4)
print(result3)