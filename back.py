from random import randint
from random import choice

class GameLogic():
    def rules():
        self.is_win=[1,2,3,4,5,6,7,8]
        self.board = self.is_win_cp()
        self.empty_index = 8

    def possible_moves():
        move=[]
        row,col = divmod(self.empty_index,3)
        if row>0:
            move.append(self.empty_index -3)
        elif row<2:
            move.append(self.empty_index +3)
        elif col>0:
            move.append(self.empty_index -1)
        elif col<2:
            move.append(self.empty_index +1)
        return move

    def swap(index):
        self.board[self.empty_index], self.board = self.board[index], self.board[self.empty_index]
        self.empty_index = index

    def start_game():
        self.board = self.is_win_cp()
        self.wmpty_index = 8
        for i in range(100):
            move = self.possible_moves()
            if move:
                random_move = choice(move)
                self.swap(random_move)
        
