class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue; # more efficient when expecting many "."
                squRow = r//3
                squCol = c//3
                if (board[r][c] in row[r] 
                    or board[r][c] in col[c]
                    or board[r][c] in squ[(squRow, squCol)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                squ[(squRow, squCol)].add(board[r][c])
        return True
