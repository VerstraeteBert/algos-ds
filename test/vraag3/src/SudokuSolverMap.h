#ifndef SUDOKUSOLVER_H
#define SUDOKUSOLVER_H

#include <stdexcept>

/**
 * Given a number, it check every the adjacent rows, columns and 3x3 subgrids of the candidate position
 * if number is already present, it cannot be a valid solution
 */
bool is_valid_map(int row, int col, int num, const bool row_map[9][10], const bool col_map[9][10], const bool subgrid_map[9][10]) {
    // check if numbers already present
    if (row_map[row][num]) return false;
    if (col_map[col][num]) return false;
    int subgrid = (row / 3) * 3 + (col / 3);
    return subgrid_map[subgrid][num] == 0;
}

bool solve_sudoku_map_btr(int grid [9][9], int row, int col, bool row_map[9][10], bool col_map[9][10], bool subgrid_map[9][10]) {
    // iterate over every field
    // note the third loop statement -> only reset col to start if going to next row
    for (; row < 9; row++, col = 0) {
        for (; col < 9; col++) {
            // if current field is already filled go to the next position
            if (grid[row][col] != 0) continue;

            // try every number from ( 1 .. 9 ) in the current field
            for (int num = 1; num <= 9; num++) {
                // if number fits in the field
                if (is_valid_map(row, col, num, row_map, col_map, subgrid_map)) {
                    int subgrid = (row / 3) * 3 + (col / 3);
                    // assign the number to the field
                    grid[row][col] = num;
                    // update presence table
                    row_map[row][num] = true;
                    col_map[col][num] = true;
                    subgrid_map[subgrid][num] = true;

                    // recurse with pointer to next position
                    if (solve_sudoku_map_btr(grid, row, col + 1, row_map, col_map, subgrid_map)) {
                        // if all next positions can be filled; the sudoku is solved
                        return true;
                    } else {
                        // if either one of the next positions cannot possibly be filled
                        // reset the assigned field and try the next number
                        grid[row][col] = 0;
                        // update presence table
                        row_map[row][num] = false;
                        col_map[col][num] = false;
                        subgrid_map[subgrid][num] = false;
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
bool solve_sudoku_map(int grid[9][9]) {
    if (grid == nullptr) throw std::invalid_argument("Grid is a nullptr");

    bool row_map[9][10] = {};
    bool col_map[9][10] = {};
    bool subgrid_map[9][10] = {};

    // builds initial presence table from input
    // if a number in input presence table is out of range (not in 1 .. 9) -> return early
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            int num = grid[row][col];

            if (num == 0) continue;
            // return if input invalid
            if (num > 9 || num < 0) return false;

            int subgrid = (row / 3) * 3 + (col / 3);
            // check dimension presence table for duplicated
            if (row_map[row][num]) return false;
            // update presence table
            row_map[row][num] = true;

            if (col_map[col][num]) return false;
            col_map[col][num] = true;

            if (subgrid_map[subgrid][num]) return false;
            subgrid_map[subgrid][num] = true;
        }
    }

    return solve_sudoku_map_btr(grid, 0, 0, row_map, col_map, subgrid_map);
}

#endif //SUDOKUSOLVER_H

