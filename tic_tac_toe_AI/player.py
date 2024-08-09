import math
import random
from typing import Dict


class FilledSqaureError(Exception):
    pass

class Player:
    def __init__(self, player_symbol) -> None:
        self.player_symbol = player_symbol

    # we want all players to get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, player_symbol) -> None:
        super().__init__(player_symbol)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, player_symbol) -> None:
        super().__init__(player_symbol)

    def get_move(self, game):
        valid_square = False
        val = None
        # ensures that the right input is received
        while not valid_square:
            square = input(f"{self.player_symbol}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val in game.filled_squares():
                    raise FilledSqaureError
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again ')
            except FilledSqaureError:
                print("Square already filled. Try another square")
        return val
    

class GeniusComputerPlayer(Player):
    def __init__(self, player_symbol) -> None:
        super().__init__(player_symbol)

    def get_move(self, game):
        # for starters let's just randomly choose an available movee.
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) 
        else:
            # use the minmax algorithm to get the next best move
            square = self.minimax(game, self.player_symbol)['position']
        return square
    
    def minimax(self, game_state, player):
        # this is going to be a recursive function.
        
        # this max player wants to win everytime..
        # so the score has to be the highest everytime
        max_player = self.player_symbol # referring to the genius player
        other_player = 'o'  if player == 'x' else 'x'

        # BASE CASE: We want to check if the previous move is a winner
        if game_state.current_winner == other_player:
            # let's return the position(the square the other player is on) and the score(heuristic)
            # for minimax to work.
            return {'position': None,
                    'score': 1 * (game_state.num_empty_squares() + 1) \
                            if other_player == max_player \
                                else -1 * (game_state.num_empty_squares() + 1)
                    }
        elif not game_state.empty_squares():
            return {'position': None, 'score': 0}
        
        # ok so here we're making some comparision of the scores
        # between the max player and the other player
        # at any point in time
        if player == max_player:
            # initialise his score to the lowest possible score so at least one iteration will beat it
            best = {'position': None, 'score': -math.inf}  
        else: # make the other guy's score the highest ever so that it seems like he's winning and we have to beat him
            best = {'position': None, 'score': math.inf}

        
        for possible_move in game_state.available_moves():
            # 1: make the move
            game_state.make_move(possible_move, player)
            # 2: simulate game after making the move
            sim_score = self.minimax(game_state, other_player)

            # 3: reset the board after simulation
            game_state.board[possible_move] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_move

            # 4: update the dictionary that is used for tracking
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else: # minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score 

        # print("##################")
        # game_state.print_board()
        # print(best, game_state.current_winner)
        # print(' ')

        
            
        return best


