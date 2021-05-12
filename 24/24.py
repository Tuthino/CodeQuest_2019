import sys
def read_puzzle():
    l = []
    for line in sys.stdin:
        line = line.rstrip()
        line = list(line)
        for i in range(0,len(line)):
            if line[i] == "_":
                line[i] = '-1'
            line[i] = int(line[i])
        l.append(line)
    return l

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row,col tuple (or (None, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # return True if is valid, False otherwise

    # check rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #check columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    #check square
    # get where the 3x3 square starts
    # and iterate over the 3 values in the row/col
    row_start = (row // 3) * 3 # 1//3 = 0; 5//3 = 1; ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False
    # if we get here, there is no collision :D
    return True

def solve_sudoku(puzzle):
    # solving sudoku with backtracking
    # each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row,col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1,10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the puzzle,
        # then we need to backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE
    return False

def prepare_out(puzzle):
    for l in puzzle:
        strings = [str(integer) for integer in l]
        a_string = "".join(strings)
        an_integer = int(a_string)
        print(an_integer)


if __name__ == '__main__':
    puzzle = read_puzzle()
    for x in range(1, ((len(puzzle)) - 1), 9):
        board = puzzle[x:x + 9]
        solve_sudoku(board)
    puzzle = puzzle[1:]
    prepare_out(puzzle)