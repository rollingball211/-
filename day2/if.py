#if문 조건문 뒤에는 반드시 콜론이 붙음.

money=2000
if money >= 3000:
     print("택시타")
else:
     print("걸어가라")

card = 1
if money>=3000 or card:
    print("택시를 타고 가")
else:
    print("걸어 가")

#만약 주머니에 돈이 있으면 택시를 타고 , 없으면 걸어 가라

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타구 가라!")
else: 
    print("걸어 가라")


#주머니에 돈이 있으면 가만히 있고 돈이 없으면 카드를 꺼내라
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
#다양한 조건을 판단하는 elif
#주머니에 돈이 있으면 택시를 타고 , 주머니에 돈은 없지만 카드가 있으면 택시를 타고 ,돈도 없고 카드도 없으면 걸어가라

if 'money'in pocket:
     print("택시를 타라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
