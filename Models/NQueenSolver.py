from Models.Backtrack import Backtrack
from Models.NQueen import Queen


class NQueenSolver(Backtrack):

    def __init__(self, nqueen):
        super().__init__()
        self.nqueen = nqueen

    def is_finished(self):
        if len(self.stack) == self.nqueen.size:
            return True
        return False

    def accept(self, queen):
        self.nqueen.place_remove_queen(queen)

    def reject(self, queen):
        self.nqueen.place_remove_queen(queen, True)

    def next_node(self, queen):
        if queen.y + 1 < self.nqueen.size:
            return Queen(0, queen.y + 1)
        return None

    def next_alt(self, queen):
        if queen.x + 1 < self.nqueen.size:
            return Queen(queen.x + 1, queen.y)
        return None

    def is_valid(self, queen):
        if self.nqueen.board[queen.y][queen.x] == 0:
            return True
        return False

    def act(self):
        pass
