from random import choice


class GameLogic:
    def __init__(self, size=3):
        if size not in [3, 4, 5]:
            raise ValueError("Размер должен быть 3, 4 или 5")
        self.size = size
        self.total_cells = size * size
        self.is_win = list(range(1, self.total_cells)) + [0] 
        self.board = []
        self.empty_index = self.total_cells - 1

    def is_win_cp(self):
        return self.is_win.copy()

    def rules(self):
        self.board = self.is_win_cp()
        self.empty_index = self.total_cells - 1

    def possible_moves(self):
        moves = []
        row, col = divmod(self.empty_index, self.size)
        if row > 0:
            moves.append(self.empty_index - self.size)
        if row < self.size - 1:
            moves.append(self.empty_index + self.size)
        if col > 0:
            moves.append(self.empty_index - 1)
        if col < self.size - 1:
            moves.append(self.empty_index + 1)
        return moves

    def swap(self, index):
        self.board[self.empty_index], self.board[index] = self.board[index], self.board[self.empty_index]
        self.empty_index = index

    def start_game(self):
        self.board = self.is_win_cp()
        self.empty_index = self.total_cells - 1
        shuffle_count = {
            3: 100,
            4: 200,
            5: 300
        }
        
        for i in range(shuffle_count.get(self.size, 100)):
            possible = self.possible_moves()
            if possible:
                random_move = choice(possible)
                self.swap(random_move)

    def is_moving(self, value):
        if value not in range(1, self.total_cells):
            return False
        
        try:
            index = self.board.index(value)
        except ValueError:
            return False
            
        if index in self.possible_moves():
            self.swap(index)
            return True
        return False

    def win(self):
        return self.board == self.is_win
    
    def get_size(self):
        return self.size
    
    def get_board_2d(self):
        return [self.board[i:i + self.size] for i in range(0, self.total_cells, self.size)]
