import numpy

fruits = ["orange","cherry","pineapple", "watermelon", "golden_apple"]
fruits_probas = [0.40, 0.25, 0.20, 0.10, 0.05]
fruits_earnings = {
    "orange" : 3, 
    "cherry" : 12, 
    "pineapple" : 25, 
    "watermelon" : 150, 
    "golden_apple" : 2000
    }

class Game():

    def __init__(self, balance):

        self.balance = balance
        self.is_bonus = False
        self.bonus_fruit = ""

    def play(self):

        self.balance -= 1

        random_fruits = numpy.random.choice(fruits, 3, p=fruits_probas)

        if random_fruits[0] == random_fruits[1] == random_fruits[2]:
            earning = fruits_earnings[random_fruits[0]]
            self.is_bonus = True
            self.bonus_fruit = random_fruits[0]
        else:
            earning = 0
            self.is_bonus=False

        self.balance += earning

        return random_fruits