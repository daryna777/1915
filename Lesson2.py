class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        self.name = 11
        self.old = 12
        self.num = 14
        self.num2 = 16
        print("I am alive!")
    def printer(self):
        print(self.height)
        print(self.name)
        print(self.old)
        print(self.num)
        print(self.num2)
Yaroslav = Student()
Aleksandra = Student()
#print(Yaroslav.height)
#print(Aleksandra.height)
Yaroslav.height = 159
Aleksandra.height = 157
#print(Yaroslav.height)
#print(Aleksandra.height)
Mark = Student()
Daryna = Student()
#print(Mark.name)
#print(Daryna.old)
Yan = Student()
Tanya = Student()
#Student.__init__(self="Tanya")
#print(Yan.num)
#print(Tanya.num2)
Yaroslav.printer()
Aleksandra.printer()
Mark.printer()
Daryna.printer()
Yan.printer()
Tanya.priner()