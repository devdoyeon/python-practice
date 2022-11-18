class Calculator:
    def __init__(self, list):
        self.list = list
    def sum(self):
        num = 0
        for i in self.list:
            num += int(i)
        return num
    def avg(self):
        num = 0
        for i in self.list:
            num += int(i)
        return num / len(self.list)

cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()
cal2.avg()