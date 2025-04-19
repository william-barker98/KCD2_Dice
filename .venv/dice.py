import random

class Dice():
    def __init__(self, id):
        self.id = id
        self.faces = 6
        self.result = None

    def roll(self):
        result = random.randint(1, self.faces)
        self.result = result
