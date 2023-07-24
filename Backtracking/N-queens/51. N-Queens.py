# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.





from ast import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.' for c in range(n)] for r in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if board[r][c] =='.' and c not in col and (r+c) not in posDiag and (r-c) not in negDiag:
                    col.add(c)
                    posDiag.add((r+c))
                    negDiag.add((r-c))
                    board[r][c] = 'Q'

                    backtrack(r+1)

                    col.remove(c)
                    posDiag.remove((r+c))
                    negDiag.remove((r-c))
                    board[r][c] = '.'


        backtrack(0)
        return res