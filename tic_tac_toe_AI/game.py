from time import sleep
from player import HumanPlayer,RandomComputerPlayer,GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # using a list to represent a 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i,space in enumerate(self.board) if space == ' ']
    
    def filled_squares(self):
        return [i for i,space in enumerate(self.board) if space != ' ']
        
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def winner(self, square, player_symbol):
        # checking the row
        row_ind = square // 3
        # this is really genius...
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([space == player_symbol for space in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([space == player_symbol for space in column]):
            return True
        
        # check diagonals

        # gets the indexes of all squares in the left to right diagonal ie (0,4,8)
        left_right_diagonal = [self.board[i] for i in [0,4,8]] 
        # gets the indexes of all squares in the left to right diagonal ie (0,4,8)
        right_left_diagonal = [self.board[i] for i in [2,4,6]]
      
        # prefiltering as this condition only works for spaces with even indexes
        if square % 2 == 0:
            # if one play symbol occupies all 3 spaces then win!!
            if all([space == player_symbol for space in left_right_diagonal]):
                return True
            if all([space == player_symbol for space in right_left_diagonal]):
                return True
            
        # if all of these fail game not over yet!!
        return False


    def make_move(self, square, player_symbol):
        if self.board[square] == ' ':
            self.board[square] = player_symbol
            if self.winner(square, player_symbol):
                self.current_winner = player_symbol
            return True
        return False

def play(game,x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    player_symbol = 'x'

    while game.empty_squares():
        if player_symbol == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # make a move
        if game.make_move(square, player_symbol):
            if print_game:
                print(f"{player_symbol} makes a move to square: {square}")
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(f"{player_symbol} wins!")
                return player_symbol

            # let the next player move
            player_symbol = 'o' if player_symbol == 'x' else 'x'
        
        # tiny break
        sleep(0.8)

    if print_game:
        print('It\'s a tie!!')


if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = GeniusComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

