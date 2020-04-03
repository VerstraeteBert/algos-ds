#pragma clang diagnostic push
#pragma ide diagnostic ignored "hicpp-signed-bitwise"
#ifndef SUDOKUSOLVERBITMAP_H
#define SUDOKUSOLVERBITMAP_H

#include <stdexcept>

typedef unsigned int uint;

/**
 * Given a number, it check every the adjacent rows, columns and 3x3 subgrids of the candidate position
 * if number is already present, it cannot be a valid solution
 */
bool is_valid_bitmap(int row, int col, int num, const uint row_map[9], const uint col_map[9], const uint subgrid_map[9]) {
    // check if num'th bit is set -> already present
    if ((row_map[row] >> num) & 1) return false;
    if ((col_map[col] >> num) & 1) return false;
    int subgrid = (row / 3) * 3 + (col / 3);
    return ((subgrid_map[subgrid] >> num) & 1) == 0;
}

bool solve_sudoku_bitmap_btr(int grid [9][9], int row, int col, uint row_map[9], uint col_map[9], uint subgrid_map[9]) {
    // iterate over every field
    // note the third loop statement -> only reset col to start if going to next row
    for (; row < 9; row++, col = 0) {
        for (; col < 9; col++) {
            // if current field is already filled go to the next position
            if (grid[row][col] != 0) continue;

            // try every number from ( 1 .. 9 ) in the current field
            for (int num = 1; num <= 9; num++) {
                // if number fits in the field
                if (is_valid_bitmap(row, col, num, row_map, col_map, subgrid_map)) {
                    int subgrid = (row / 3) * 3 + (col / 3);
                    // assign the number to the field
                    // set corresponding reservation bits
                    grid[row][col] = num;
                    row_map[row] |= (1 << num);
                    col_map[col] |= (1 << num);
                    subgrid_map[subgrid] |= (1 << num);

                    // recurse with pointer to next position
                    if (solve_sudoku_bitmap_btr(grid, row, col + 1, row_map, col_map, subgrid_map)) {
                        // if all next positions can be filled; the sudoku is solved
                        return true;
                    } else {
                        // if either one of the next positions cannot possibly be filled
                        // reset the assigned field and try the next number
                        // also clear the corresponding bits in the reservation maps
                        grid[row][col] = 0;
                        row_map[row] &= ~(1 << num);
                        col_map[col] &= ~(1 << num);
                        subgrid_map[subgrid] &= ~(1 << num);
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
bool solve_sudoku_bitmap(int grid[9][9]) {
    if (grid == nullptr) throw std::invalid_argument("Grid is a nullptr");

    uint row_map[9] = {};
    uint col_map[9] = {};
    uint subgrid_map[9] = {};

    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            int num = grid[row][col];
            if (num == 0) continue;
            if (num > 9 || num < 0) return false;

            int subgrid = (row / 3) * 3 + (col / 3);

            // get num'th bit of row bitmap; if it's 1 -> already present
            if ((row_map[row] >> num) & 1) return false;
            // set num'th bit of row bitmap
            row_map[row] |= (1 << num);

            if ((col_map[col] >> num) & 1) return false;
            col_map[col] |= (1 << num);

            if ((subgrid_map[subgrid] >> num) & 1) return false;
            subgrid_map[subgrid] |= (1 << num);
        }
    }

    return solve_sudoku_bitmap_btr(grid, 0, 0, row_map, col_map, subgrid_map);
}

#endif //SUDOKUSOLVERBITMAP_H
