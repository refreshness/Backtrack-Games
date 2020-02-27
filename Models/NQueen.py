class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class NQueen:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for i in range(size)]

    def place_remove_queen(self, queen, remove=False):
        if self.board[queen.y][queen.x] < 0 and remove is False:
            return None
        inc = 1
        if remove is True:
            inc = -inc
            self.board[queen.y][queen.x] = -self.board[queen.y][queen.x] + inc
        else:
            self.board[queen.y][queen.x] = -self.board[queen.y][queen.x] - inc

        self.__do_rows_columns(queen.x, queen.y, inc)
        self.__do_first_diagonal(queen.x, queen.y, inc)
        self.__do_second_diagonal(queen.x, queen.y, inc)

    def __do_rows_columns(self, x, y, inc):
        for i in range(1, self.size):
            if self.board[y][(x + i) % self.size] >= 0:
                self.board[y][(x + i) % self.size] += inc
            else:
                self.board[y][(x + i) % self.size] -= inc
            if self.board[(y + i) % self.size][x] >= 0:
                self.board[(y + i) % self.size][x] += inc
            else:
                self.board[(y + i) % self.size][x] -= inc

    def __do_first_diagonal(self, x, y, inc):
        i = 1
        while (x + i < self.size and y + i < self.size) or \
                (x - i >= 0 and y - i >= 0):
            if x + i < self.size and y + i < self.size:
                if self.board[y + i][x + i] >= 0:
                    self.board[y + i][x + i] += inc
                else:
                    self.board[y + i][x + i] -= inc
            if x - i >= 0 and y - i >= 0:
                if self.board[y - i][x - i] >= 0:
                    self.board[y - i][x - i] += inc
                else:
                    self.board[y - i][x - i] -= inc
            i += 1

    def __do_second_diagonal(self, x, y, inc):
        i = 1
        while (x + i < self.size and y - i >= 0) or \
                (x - i >= 0 and y + i < self.size):
            if x + i < self.size and y - i >= 0:
                if self.board[y - i][x + i] >= 0:
                    self.board[y - i][x + i] += inc
                else:
                    self.board[y - i][x + i] -= inc
            if x - i >= 0 and y + i < self.size:
                if self.board[y + i][x - i] >= 0:
                    self.board[y + i][x - i] += inc
                else:
                    self.board[y + i][x - i] -= inc
            i += 1

    def check_board(self):
        queens = 0
        for row in self.board:
            for cell in row:
                if cell < -1:
                    return False
                if cell == -1:
                    queens += 1

        if queens == self.size:
            return True
        return False
