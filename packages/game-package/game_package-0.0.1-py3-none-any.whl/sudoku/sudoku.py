import random
import copy

solved_sudoku = []

def print_board(sudoku):
    for row_i in range(len(sudoku)):
        for num_i in range(len(sudoku[0])):
            if(num_i != 0 and num_i%3 == 0):
                print("|", end=" ")
            print(sudoku[row_i][num_i], end=" ")
        print()
        if(row_i != 0 and row_i+1 != len(sudoku[0]) and (row_i+1)%3 == 0 ):
            print("-" * 21)

def current_value_set(sudoku, row, col, number):

    for x in range(9):
        if(sudoku[row][x] == number):
            return False
        
    for y in range(9):
        if(sudoku[y][col] == number):
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if(sudoku[corner_row + x][corner_col + y] == number):
                return False
    
    return True

def create_sudoku(sudoku, row, col):
    if(col == 9):
        if(row == 8):
            return True
        row += 1
        col = 0

    if sudoku[row][col] > 0:
        return create_sudoku(sudoku, row, col + 1)

    passed_num = set()
    while(len(passed_num) < 9):
        random_num = random.randint(1, 9)
        if(random_num not in passed_num):
            passed_num.add(random_num)
            if current_value_set(sudoku, row, col, random_num):
                sudoku[row][col] = random_num
                if create_sudoku(sudoku, row, col + 1):
                    return True
                sudoku[row][col] = 0
    return False

def sudoku_spacing(sudoku):
    suduko_difficulty = input("press [h]for hard [m]for medium [e]for easy: ")

    gap_range = 0
    if(suduko_difficulty == "h"):
        gap_range = 7
    elif(suduko_difficulty == "m"):
        gap_range = 4
    elif(suduko_difficulty == "e"):
        gap_range = 3
    else:
        print("Invalid input")
        return False

    for x in range(len(sudoku)):
        spaced_index = set()
        while(len(spaced_index) < gap_range):
            random_index = random.randint(0,8)
            if(random_index not in spaced_index):
                spaced_index.add(random_index)
                sudoku[x][random_index] = " "
    return True

def give_solution(solution):
    solution_input = input("Also want the solution. y/n?: ")

    if(solution_input == "Y" or solution_input == "y"):
        print_board(solution)
    else:
        print("Thank you!😁")
        return



def sudoku():
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    if create_sudoku(sudoku, 0, 0):
        solved_sudoku = copy.deepcopy(sudoku)

    if(solved_sudoku == []):
        solved_sudoku = sudoku

    valid_input = sudoku_spacing(sudoku)
    if(valid_input):
        print_board(sudoku)

    give_solution(solved_sudoku)

sudoku()


