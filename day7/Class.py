"""

"""


class service:
    secret="영구는 배꼽이 두개다"
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        result= a+b
        print("%s님 %s+%s =%s입니다" %(self.name,a,b,result))

class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        result= self.first+self.second
        return result
    def subtraction(self):
        result = self.first-self.second
        return result
    def multiply(self):
        result = self.first*self.second
        return result
    def divide(self):
        result = self.first/self.second
        return result


pey=service()
pey.setname("홍길동")
pey.sum(1,1)
print(pey.secret)

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(3,7)
print(a.sum())
print(a.subtraction())
print(a.multiply())
print(a.divide())
