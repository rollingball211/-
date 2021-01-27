a=1
def vartest(a):
    a= a+1
    return a

a =vartest(a)
print(a)

def vartest1():
    global a
    a=a+1
vartest1()
print(a)