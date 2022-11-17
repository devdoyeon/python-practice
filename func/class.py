class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def set_data(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def div(self):
        return self.first / self.second
    def min(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second

a = FourCal(4, 2)
# a.set_data(4, 2)

class ExtendClass(FourCal): # 클래스 상속 (FourCal의 기능을 모두 가져오면서 추가하거나 수정해야 할 기능이 생길 경우 상속 받아 수정할 수 있다.)
    def pow(self):
        return self.first ** self.second

'''
  __init__ 생성자가 있을 경우 a = FourCal(4, 2)로 간추려 적을 수 있다.
  a = FourCal()
  a.setData(4, 2) 와

  a = FourCal(4, 2) 가 같다는 의미이다. 그러므로 생성자가 있을 경우 setData 함수는 없어도 된다.
'''

print(a.add(), a.min(), a.mul(), a.div())