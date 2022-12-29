class Mom:
    def __init__(self):
        super().__init__()
        self.iq = 220
class Dad:
    def __init__(self):
        super().__init__()
        self.beauty = 130
class Daughter(Mom, Dad):
    def print_info(self):
        print(self.iq)
        print(self.beauty)

anna = Daughter()
anna.print_info()