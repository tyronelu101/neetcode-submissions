class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (r/3) * 3 + (c/3)
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r, board_row in enumerate(board):
            for c, cell in enumerate(board_row):
                if cell != '.':
                    box_index = (r//3) * 3 + (c//3)
                    if cell in row[r] or cell in column[c] or cell in box[box_index]:
                        return False
                    row[r].add(cell)
                    column[c].add(cell)
                    box[box_index].add(cell)
                    
        return True