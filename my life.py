import random
class Human:
    def __init__(self, name="Daryna", rating=None):
        self.rating = rating
        self.name = name
        self.money = 20
        self.gladness = 70
        self.satiety = 40
        self.health = 100
    def medicine(self):
        self.health+=50
    def health(self):
        if self.health<100:
            print("Потрібні ліки щоб не стало ще гірше")
            self.medicine()
    def disease(self):
        self.gladness-=30
    def games(self):
        self.gladness+=2
    def walk(self):
        self.gladness+=6
        self.satiety-=3
    def eat(self):
        self.satiety+=5
    def sleep(self):
        self.gladness+=1
    def homework(self):
        self.gladness-=1
    def chill(self):
        self.gladness+=3
    def TV(self):
        self.gladness+=2
    def school(self):
        if self.workday:
            print("Час до школи")
            self.school()
        self.satiety-=4
        self.rating+=1
        self.gladness-=1
    def shopping(self):
        self.gladness+=15
        self.money-=40
    def STEP(self):
        if self.friday:
            print("час вчитися в академії ШАГ")
            self.STEP()
        self.gladness=+2
        self.rating=+2
        self.satiety=-1
    def English(self):
        if self.tuesday_thursday:
            print("час займатися англійською мовою")
        self.gladness=+2
        self.satiety=-1
        self.rating=+1
    def is_alive(self):
        if self.gladness<0:
            print("Дуже сумно")
            return False
        if self.satiety<0:
            print("Голод")
            return False
        if self.health<0:
            print("Дуже хвора")
            return False
class School:
    def __init__(self, rates_list):
        self.rating=random.choice((list(rates_list)))
    rates_list={
        12:{"money":50,"gladness":20},
        11: {"money": 45,"gladness": 18},
        10: {"money": 40,"gladness": 15},
        9: {"money": 30,"gladness": 12},
        8: {"money": 20, "gladness": 9},
        7: {"money": 10, "gladness": 6},
        6: {"gladness": 3},
        5: {"gladness": -1},
        4: {"gladness": -5},
        3: {"gladness": -10},
        2: {"gladness": -20},
        1: {"gladness": -50}
    }
class Food:
    def __init__(self, food_list):
        self.satiety=random.choice((list(food_list)))
    food_list={
        "Soup":{"satiety":40},
        "fried potatoes": {"satiety":30},
        "potatoes with cutlet": {"satiety":50},
        "chocolate": {"satiety": 10,"gladness":17},
        "pizza": {"satiety": 35,"gladness":15},
        "sandwich": {"satiety":15},
        "sweets": {"satiety": 5,"gladness":15}
    }
class Disease:
    def __init__(self, virus_list):
        self.disease=random.choice((list(virus_list)))
    virus_list={
        "COVID-19":{"health": -50,"gladness":-70},
        "cold": {"health": -5, "gladness": -15},
        "flu": {"health": -30, "gladness": -50},
        "cough": {"health": -15, "gladness": -30},
        "toothache": {"health": -10, "gladness": -55}
    }