from random import randint
from random import choice

class GameLogic:
    def rules(self):
        self.is_win=[1,2,3,4,5,6,7,8,0]
        self.board = self.is_win_cp()
        self.empty_index = 8

    def possible_moves(self):
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

    def swap(self, index):
        self.board[self.empty_index], self.board = self.board[index], self.board[self.empty_index]
        self.empty_index = index

    def start_game(self):
        self.board = self.is_win_cp()
        self.empty_index = 8
        for i in range(100):
            move = self.possible_moves()
            if move:
                random_move = choice(move)
                self.swap(random_move)
    
    def is_moving(self, value):
        if value not in range(1,9):
            return False
        index = self.board.index(value)
        if index in self.possible_moves():
            self.swap(index)
            return True
        return False

    def win(self):
        return self.board == self.is_win
        
