import math
import random #assuming these will be needed

class player:
    def __init__(self, letter): #_init_ allows us to INITIALIZE the attributes of the object
        self.letter = letter

    def get_move(self, game):
        pass 


class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves()) #random spot which is valid 
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8): ')
            #we are checking that a correct value is being inputted (has to be a integer or it is invalid, or if spot is taken it is also invalid)
            try: 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqaure = True
            except ValueError:
                print('Invalid Square. Please Try Again.')
        
        return val