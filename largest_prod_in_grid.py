
# Daylan Stoica
# @DaylanDStoica

# 22 August 2022

'''
Largest product in a grid


Project Eueler  
Problem 11

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

def make_the_grid():
    '''split the grid into 2D array'''
    base_grid = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
    base_grid_rows = base_grid.split('\n')
    cols = []
    returned_grid = []
    for row in base_grid_rows:
        cols = row.split()
        returned_grid.append(cols)
    # returned_grid = base_grid_rows
    # returned_grid = cols
    return returned_grid


# def is_pos_too_close_to_left(grid, col_x):

def is_pos_too_close_to_top_left ( grid, col_x, row_y, line_len = 4):
    '''return different values for their proximity to a border'''
    x_ret = 0
    y_ret = 0
    # 0 is not too close, 1 is one from too close, 2 is two from too close,
    # 3 is 3 from too close, 
    # there is 4 too close
    row_count = len(grid) #the number of rows,
    col_count = len(grid[0]) # the number of columns
    x_ret = col_x - (line_len-1)
    # getting negatives will indicate too close
    y_ret = row_y - (line_len-1)
    if x_ret >= 0:
        x_ret = 0
    if y_ret >= 0:
        y_ret = 0
    
    print(f"({col_x}, {row_y}), close to upper_left corner: ({x_ret}, {y_ret})")

    return x_ret , y_ret

def is_pos_too_close_to_bott_right (grid, col_x, row_y, line_len = 4):
    '''return different values for closeness to lower-right corner'''
    row_count = len(grid)
    col_count = len(grid[0])

    x_ret = col_count - col_x - line_len
    y_ret = row_count - row_y - line_len

    if x_ret >= 0:
        x_ret = 0
    if y_ret >= 0:
        y_ret = 0    
    print(f"({col_x}, {row_y}), close to lower_right corner: ({x_ret}, {y_ret})")
    return x_ret, y_ret

def test_the_too_close_functions():
    grid = make_the_grid()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            is_pos_too_close_to_top_left(grid, x, y)
            is_pos_too_close_to_bott_right(grid, x, y)

test_the_too_close_functions()
# check the 4 long of each position, return 4-long arrays for each possible extent
def check_prod_diagonally( grid, col_x, row_y, border_prox_x = 0, border_prox_y = 0):
    '''return the highest product of diagonals, check for both right and left
    likely the most complicated'''
    # border proximity for changing the products to be considered, remaining within index boundary
    left_x, top_y = is_pos_too_close_top_left( grid, col_x, row_y)
    right_x, bott_y = is_pos_too_close_bott_right( grid, col_x, row_y)

    for i in range(-3,4):
        for j in range(-3,4):
            pass
def check_prod_vertically( grid, col_x, row_y, border_prox_x = 0, border_prox_y = 0):
    '''return the highest product of columns'''

    for y in range(-3,3+1): # from 3 in either direction from the position
        #provide if-else cases if too close to a border
        pass
def check_prod_horiz( grid, col_x, row_y, border_prox_x = 0, border_prox_y = 0):
    '''return the highest product of rows'''
    for x in range( -3, 3+1): # from 3 in either direction from the position
        #provide if-else cases if too close to a border
        pass

def check_prod_all ( grid):
    '''use the other check_prod functions, 
    going in increments of 4
    check the next 4 in the direction'''
    for row in range(0, len(grid) ):
        for col in range(0, len(row) ):
            diag = check_prod_diagonally( grid, row, col)
            vert = check_prod_vertically( gird, row, col)
            horz = check_prod_vertically( grid, row, col)
def main():
    the_grid = make_the_grid()
    for row in the_grid:
        print(row)
        print("row_length   ", len(row))
    print("row count: ", len( the_grid) )

# main()