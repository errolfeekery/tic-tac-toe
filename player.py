import math
import random


class Player:
    '''

    creating player class with letter for each player, either x or o
    '''
    def __init__(self, letter):
        ''' letter is x or o '''
        self.letter = letter

    def get_move(self, game):
        ''' we want players to get their next move '''
        pass


class RandomComputerPlayer(Player):
    ''' computer player which inherits class from Player '''
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    ''' human player inherits class from Player class '''
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
