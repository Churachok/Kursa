from random import choice


class GameLogic:
    def __init__(self):
        self.is_win = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.board = []
        self.empty_index = 8

    def is_win_cp(self):
        return self.is_win.copy()

    def rules(self):
        self.board = self.is_win_cp()
        self.empty_index = 8

    def possible_moves(self):
        moves = []
        row, col = divmod(self.empty_index, 3)
        if row > 0:
            moves.append(self.empty_index - 3)
        if row < 2:
            moves.append(self.empty_index + 3)
        if col > 0:
            moves.append(self.empty_index - 1)
        if col < 2:
            moves.append(self.empty_index + 1)
        return moves

    def swap(self, index):
        self.board[self.empty_index], self.board[index] = self.board[index], self.board[self.empty_index]
        self.empty_index = index

    def start_game(self):
        self.board = self.is_win_cp()
        self.empty_index = 8
        for i in range(100):
            possible = self.possible_moves()
            if possible:
                random_move = choice(possible)
                self.swap(random_move)

    def is_moving(self, value):
        if value not in range(1, 9):
            return False
        index = self.board.index(value)
        if index in self.possible_moves():
            self.swap(index)
            return True
        return False

    def win(self):
        return self.board == self.is_win
