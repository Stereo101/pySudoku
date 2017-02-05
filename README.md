Small python script, give or take 100 lines, that solves sudoku puzzles.

Simplified solution process:
__1.__Fill in all spots where only 1 number can exist
__2.__Repeat until no such spots exist
__3.__If the board is complete, complete the process. Return the board
__4.__If the board is not complete, find the spot where the smallest numbers of guesses fit
__5.__Call this process on each guess board, one of the guesses must be right.

The 10,000 puzzles included here are from websudoku.com
