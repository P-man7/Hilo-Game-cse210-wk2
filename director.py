from game.Cards import Cards

class Director():
    '''Director controls the flow of the game

    attributes: 
        cards (list[cards]): a list of cards.
        is_playing (boolean): if the gam eis being played and can continue.
        score (int): score for one round
        total_score (int): score for entire game.
    
    '''

    def __init__(self):
        '''initiates a new director
            
        Args:
            self (Director): and instance of Director.
        '''


        self.is_playing = True
        self.card2 = 0
        self.score = 0
        self.total_score = 300


    def start_game(self):
        '''starts game and keeps it running while in loop.
        
        Args:
            self (Director)'''
        while self.is_playing:
            
            self.do_updates()

            self.do_outputs()

            #Ask the player to play again, if 'n',  then end game loop
            if self.is_playing:
                replay = input('Play again? [y/n]')
                self.is_playing = (replay == 'y')


    def get_guess(self):
        guess = input('Higher or Lower? [h/l] ')
        return guess
        

    def do_updates(self):
        Cards.draw(self)
        print(f'The card is: {Cards.card1}')
        guess = self.get_guess()
        print(f'The next card is: {Cards.card2}')
        Cards.compare(self, guess)
        self.total_score += Cards.points
        

    def do_outputs(self):
        print(f'total score is: {self.total_score}')
        if self.total_score <= 0:
            self.is_playing = False
        






















