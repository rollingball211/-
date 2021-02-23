class HousePark:
    lastname="박" 
    def setname(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print("%s,%s 여행을 가다" %(self.fullname,where))
    def love(self,other):
        print("%s,%s와 사랑에 빠졌네" %(self.fullname,other.fullname))
    def fight(self,other):
        print("%s,%s와 싸우네"%(self.fullname,other.fullname))
    def __add__(self,other):
        print("%s, %s와 결혼했네"%(self.fullname,other.fullname))
    def __sub__(self,other):
        print("%s,%s와 이혼했네"%(self.fullname,other.fullname))
    """
    lastname: housepark클래스에 의해 생성되는 인스턴스 모두에 "박" 이라는 값을 갖게 만듬.
    """
class HouseKim(HousePark):
    lastname="김"
    def travel(self,where,day):
        print("%s, %s 여행을 %d일 가다"%(self.fullname,where,day))

pey=HousePark()
pey.setname("응용")
pey.travel("부산")

ming=HouseKim()
ming.setname("줄리엣")
ming.travel("헬리오시티",3)
"""
연산자 오버로딩: 연산자를 객체끼리 사용가능하게 할 수 있는 기법.
"""
pey.love(ming)
pey + ming
pey.fight(ming)
pey - ming