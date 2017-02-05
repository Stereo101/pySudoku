Small python script, give or take 100 lines, that solves sudoku puzzles.

Simplified solution process:

1.Fill in all spots where only 1 number can exist

2.Repeat until no such spots exist

3.If the board is complete, complete the process. Return the board

4.If the board is not complete, find the spot where the smallest numbers of guesses fit

5.Call this process on each guess board, one of the guesses must be right.


The 10,000 puzzles included here are from websudoku.com
