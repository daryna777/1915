class Student:
    def __init__(self):
        self.money = 100
    def holiday(self):
        self.money -=5
    def work(self):
        self.money +=5
Daryna = Student()
print(Daryna.money)