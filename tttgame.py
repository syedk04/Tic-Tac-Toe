import time
from tttplayer import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self,):
        self.board = [' ' for _ in range(9)] #We will use a single list to represent a 3x3 board
        self.current_winner = None #To keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #getting the rows 
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] #short version of code below
       # moves = []
       # for (i, spot) in enumerate(self.board):
       #   if spot == ' ':
       #      moves.append(i)
       # return moves
    
    def empty_sqaures(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
        # another way: return len(self.available_moves())
        
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row for winner
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind +1) *3]
        if all([spot == letter for spot in row]):
            return True 
        
        #check column for winner
        column_ind = square % 3
        column = [self.board[column_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 
        
        #check for diagonal winner (Only numers 0, 2, 4, 6, 8) as they are the only diagonal spaces
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True 
        
        # if no winner then it is a tie so we return false for winner method
        return False


def play(game, x_player, o_player, print_game=True): #print_game can be toggled to false
    # returns winner of the game, or NONE if the game ends in a tie (letter that won)
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    while game.empty_sqaures():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switch players depending on what was played

            
        #break so computer doesn't go right away
        time.sleep(0.8)

    if print_game:
        print('Tie game!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
