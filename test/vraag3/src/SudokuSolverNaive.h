#ifndef SUDOKUSOLVERNAIVE_H
#define SUDOKUSOLVERNAIVE_H

#include <stdexcept>

using namespace std;

/**
 * Given a canditate number, it check every the adjacent rows, columns and 3x3 subgrids of the candidate position
 * if candidate number is already present, it cannot be a valid solution
 */
bool is_valid_naive(const int grid[9][9], int row, int col, int num) {
    int subgrid_row_offset = 3 * (row / 3);
    int subgrid_col_offset = 3 * (col / 3);
    for (int offset = 0; offset < 9; offset++) {
        if (grid[row][offset] == num) return false;
        if (grid[offset][col] == num) return false;
        if (grid[subgrid_row_offset + offset / 3][subgrid_col_offset + offset % 3] == num) return false;
    }

    return true;
}

bool solve_sudoku_btr_naive(int grid [9][9], int row, int col) {
    // iterate over every field
    // note the third loop statement -> only reset col to start if going to next row
    for (; row < 9; row++, col = 0) {
        for (; col < 9; col++) {
            // if current field is already filled go to the next position
            if (grid[row][col] != 0) continue;

            // try every number from ( 1 .. 9 ) in the current field
            for (int num = 1; num <= 9; num++) {
                // if number fits in the field
                if (is_valid_naive(grid, row, col, num)) {
                    // assign the number to the field
                    grid[row][col] = num;
                    // recurse with pointer to next position
                    if (solve_sudoku_btr_naive(grid, row, col + 1)) {
                        // if all next positions can be filled; the sudoku is solved
                        return true;
                    } else {
                        // if either one of the next positions cannot possibly be filled
                        // reset the assigned field and try the next number
                        grid[row][col] = 0;
                    }
                }
            }
            // if none of the numbers match -> backtrack
            return false;
        }
    }
    // all rows and col fields are filled in -> solved
    return true;
}

// Assuming a fixed grid of 9x9
bool solve_sudoku_naive(int grid [9][9]) {
    if (grid == nullptr) throw std::invalid_argument("Grid is a nullptr");
    return solve_sudoku_btr_naive(grid, 0, 0);
}

#endif //SUDOKUSOLVERNAIVE_H
