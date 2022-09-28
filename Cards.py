import random

class Cards():
    '''class Cards draws cards for the game
    
    attributes:
        self.card1 (int): value of card 1 between 1 and 13
        self.card2 (int): value of card 2 between 1 and 13, different than card 1
    '''
    def __init__(self):
        self.card1 = 0
        self.card2 = 0
        self.points = 0



    def draw(self):

        self.card1 = random.randint(1, 13)
        while self.card2 == 0 or self.card2 == self.card1:
            self.card2 = random.randint(1, 13)
            

    def compare(self, guess):

        if guess == 'h':
            if self.card2 > self.card1:
                self.points += 100
            if self.card2 < self.card1:
                self.points += -75

        if guess == 'l':
            if self.card2 < self.card1:
                self.points += 100
            if self.card2 > self.card1:
                self.points += -75

        

































