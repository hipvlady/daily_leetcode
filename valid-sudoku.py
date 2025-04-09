def isValidSudoku(board):
    for row in board:
        if not is_valid(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid(column):
            return False

    for box_row in range(3):
        for box_col in range(3):
            box = []
            for r in range(3):
                for c in range(3):
                    row = box_row * 3 + r
                    col = box_col * 3 + c
                    box.append(board[row][col])

            if not is_valid(box):
                return False

    return True


def is_valid(block):
    seen = set()
    for cell in block:
        if cell == ".":
            continue

        if cell in seen:
            return False

        if cell < "1" or cell > "9":
            return False

        seen.add(cell)
    return True


# Test with your board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

result = isValidSudoku(board)
print(f"Is the Sudoku board valid? {result}")