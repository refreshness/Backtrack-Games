from Models.NQueen import NQueen, Queen
from Models.NQueenSolver import NQueenSolver


def pprint(matrix):
    for row in matrix:
        print(row)


nq1 = NQueen(4)
solver = NQueenSolver(nq1)
solver.backtrack(Queen(0, 0))
pprint(solver.nqueen.board)
