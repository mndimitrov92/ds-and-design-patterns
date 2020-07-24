"""
Write a function that will take 3 args:
bombs = list of bomb locations
rows , columns
mine_sweeper([0,0],[1,2],3, 4)
bomb at row 0 column 0
bomb at row0 column 1
3 rows, 4 columns

We should return an 3 x 4 array (-1) = bomb
"""


def mine_sweeper(bombs, rows, columns):
    field = [[0 for i in range(columns)] for x in range(rows)]

    # add the bombs to the field
    for bomb_location in bombs:
        bomb_row, bomb_col = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if (0 <= i < rows) and (0 <= j < columns) and field[i][j] != -1:
                    field[i][j] += 1
    return field


print(mine_sweeper([[0, 0], [1, 2]], 3, 4))
