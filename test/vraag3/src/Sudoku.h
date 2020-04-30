#pragma clang diagnostic push
#pragma ide diagnostic ignored "hicpp-signed-bitwise"
#ifndef SUDOKU_H
#define SUDOKU_H

#include <fstream>
#include <iostream>
#include "./SudokuSolverNaive.h"
#include "./SudokuSolverMap.h"
#include "./SudokuSolverBitMap.h"

using namespace std;

class Sudoku{
public:
    explicit Sudoku(const string& filename);
    bool isSolved();
    bool solveNaive();
    bool solveMap();
    bool solveBitmap();
    int left3();
    friend ostream& operator<< (ostream &out, const Sudoku &s);
private:
    int grid[9][9];
};

ostream& operator<< (ostream &out, const Sudoku &s){
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            out << s.grid[i][j] << " " ;

            if ((j+1) % 3 == 0 && j < 8)
                out << "| ";
        }
        out << endl;
        if ((i+1) % 3 == 0 && i < 8){
            out << "------+-------+------" << endl;
        }
    }
    return out;
}

Sudoku::Sudoku(const string& filename){
    ifstream infile(filename);
    if (infile){
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                infile >> grid[i][j];
            }
        }
    }
}

// uses presence tables to check if sudoku is solved
// A solved (9x9 sudoku has two requirements
// -> no invalid numbers (only 1..9)
//      -> validated through simple comparison
// -> no duplicate numbers in each dimensions (row, column, subgrid)
//      -> validated with the presence table
bool Sudoku::isSolved() {
    int row_map[3] = {};
    int col_map[9] = {};
    int subgrid_map[9] = {};

    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            int num = grid[row][col];
            // invalid values ? -> not solved
            if (num <= 0 || num > 9) return false;

            // duplicated number present in dimension? -> not solved
            int row_num_offset = num + 10 * (row % 3);
            if ((row_map[row / 3] >> row_num_offset) & 1) return false;
            // update dimension presence table -> set num'th bit
            row_map[row / 3] |= (1 << row_num_offset);

            if ((col_map[col] >> num) & 1) return false;
            col_map[col] |= (1 << num);

            int subgrid = (row / 3) * 3 + (col / 3);
            if ((subgrid_map[subgrid] >> num) & 1) return false;
            subgrid_map[subgrid] |= (1 << num);
        }
    }

    // no duplicated numbers or invalid numbers -> solved!
    return true;
}

bool Sudoku::solveNaive(){
    return solve_sudoku_naive(grid);
}

bool Sudoku::solveMap() {
    return solve_sudoku_map(grid);
}

bool Sudoku::solveBitmap() {
    return solve_sudoku_bitmap(grid);
}

// helper function to check correct solution
int Sudoku::left3() {
    return grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2];
}

#endif
#pragma clang diagnostic pop