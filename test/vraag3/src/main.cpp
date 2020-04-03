#include <iostream>
#include "Sudoku.h"
#include "../lib/chrono.h"

using namespace std;

/**
 * Sudoku Backtracking Solver
 *
 * I've made three implementations;
 *  All three of them are similar as they're all backtracking algorithms.
 *
 *  The recursive general implementation, which is the same for all three:
 *
 *  ----- Summary -------
 *      Each recursive call handles a field that needs yet to be filled
 *          -> pick a valid number ( 1 .. 9 )
 *          -> if no valid number exists, backtrack
 *          -> else go to the next field and try to fill it in
 *
 *
 *  --------    More in detail general implementation      ---------
 *  Start at the left-top most field
 *
 *  1. Continue until a field is not yet filled in (signified by 0 value)
 *      -> going from left to right in each row, going to the next row if column out of bounds
 *      -> if past the last position; all numbers are filled in correctly
 *              -> RETURN TRUE
 *
 *  2. Try next candidate number from 1 .. 9
 *      -> validate for every candidate if the same number is not yet present in
 *          -> same row
 *          -> same column
 *          -> same subgrid (3x3)
 *
 *  3. If candidate number is valid
 *      -> save the candidate number into the field
 *      -> recurse to 1 -> supplying the next field that needs to be checked
 *      -> wait for return value of recursive call (goto 5)
 *
 *     If not valid
 *          -> goto 2 as long as there is a number left to try
 *          -> if no number is left to try goto 4
 *
 *  4. No number left to try for a given position
 *      -> this signifies that a previous field was filled in incorrectly
 *      -> BACKTRACK!
 *              -> RETURN FALSE
 *
 *  5. Handle recursive return value
 *      -> if false returned from 4 (backtracking was necessary)
 *          -> removed candidate number in current field
 *          -> goto 2 - >try next number in current field
 *      -> if true returned from 1 (all numbers filled in)
 *          -> SOLUTION FOUND
 *          -> bubble up the true return value up the stack and done!
 *
 *  -------       Differences between implementations        ------------
 *
 *  The differences between the implementations lies in the way candidate numbers are checked for validity.
 *
 *  In my first, naive implementation: for every candidate number of a field,
 *      every field in the same row, column and subgrid was compared to the candidate.
 *      If a any of these already contain the candidate, the candidate number in the field cannot yield a valid solution.
 *
 *  The problem with this implementation is that 27 comparisons need to be made on every validation check;
 *  Since this validation step can be potentially be ran up to 9 times for every field, it is a huge performance bottleneck.
 *
 *  The two other, more optimized implementations were inspired by my solution of the is_solve() method:
 *      where I took the approach of building a presence table while iterating over every field.
 *      Only having to check for every field if the number is in the correct range 1 .. 9
 *      AND that the number was not yet present in the presence table for its corresponding row, column and subgrid.
 *
 *  This general idea can also be used in the backtracking algorithm, and highly optimizes the validity checking step
 *      Where 3 tables are kept each containing the presence of every number from 1..9 in a given dimension
 *          1) in every row
 *          2) in every column
 *          3) in every subgrid
 *     In each validation step only 3 checks need to be made compared to the 27 of the naive implementation
 *          -> check if candidate is already present in its row, column and subgrid
 *
 *     Algorithm adaptations:
 *      - Build an initial presence table for each column, row and subgrid, from the input grid
 *      - On every candidate validity check, check if number already present in corresponding row, column and subgrid
 *      - when copying a number into a field
 *          -> update presence tables for corresponding row, column and subgrid
 *      - when removing number from a field (setting it to empty again)
 *          -> update presence tables for corresponding row, column and subgrid
 *
 *     NOTE: due to the building of an initial presence table: input can easily be validated aswell
 *                  -> if a duplicate number already exists for instance, or a number is not within the range 1..9
 *                        -> we can return early or throw an exception!
 *
 *     In these more optimized an at least 4x performance gain is seen (on my machine) compared to the naive validation
 *                  ---- BENCHMARKING ----
 *           Completed naive solving in: 0.449862
 *           Completed solving with map in: 0.102412
 *           Completed solving with bitmap in: 0.102184
 *
 *     1) The boolean map approach, which for every row, column and subgrid keeps a 2 dimensional presence table of 9x10
 *              -> each row corresponds to a dimension of the grid (row, column or subgrid respectively)
 *              -> each column corresponds to a number being present in the dimension
 *                  -> true -> already present
 *                  -> false -> not yet present
 *
 *     NOTE: 9x9 would suffice, as the numbers range from 1..9, however that makes the code harder just a little bit harder to read
 *      -> accessing the presence table would have to written as
 *              e.g. row_table[candidate - 1]
 *                  instead of row_table[candidate]
 *              This costs 27 bytes more (9 (length of dimension) * 3 (every dimension) * 1 (bool byte size)) which is trivial
 *              And as in most things in CS, it is a tradeoff for sanity
 *
 *
 *     2) The bitmap approach is marginally more memory optimized
 *           since the dimension is 9x9, the numbers in each dimensions easily fit into a 4 byte integer
 *           As we only need 9 bits (using 10 bits however, same idea as with the bool map, in this case it doesn't influence the memory taken)
 *
 *           Where tables are kept for each dimension of 9 ints (length of the dimension)
 *              The same technique is used as in the bool map, where bit N keeps track of the presence of number N in a given dimension
 *                  -> 1 -> present
 *                  -> 0 -> not present
 *
 *           The extra memory taken is less than with the bool map
 *                  bool map: 9 * 10 * 1 (bool byte size) * 3 == 270 bytes
 *                  bit map: 9 * 4 (int byte size) * 3 == 108
 *
 *           Does this marginal amount of memory optimization and tiny performance gain make up for worse readability?
 *              -> Probably not. Still fun to play with!
 */
int main() {
    Chrono timer = Chrono();

    cout << "---- BENCHMARKING ----" << endl;

    // test every sudoku with naive implementation
    timer.start();
    int check = 0;
    for (int i = 1; i <= 50; i++) {
        auto filename = "sudokus/" + to_string(i) + ".txt";
        auto s = Sudoku(filename);
        s.solveNaive();
        check += s.left3();
        assert(s.isSolved());
    }
    assert(check == 24702);
    timer.stop();
    cout << "Completed naive solving in: " << timer.tijd() << endl;

    // test every sudoku with map implementation
    timer.start();
    check = 0;
    for (int i = 1; i <= 50; i++) {
        auto filename = "sudokus/" + to_string(i) + ".txt";
        auto s = Sudoku(filename);
        s.solveMap();
        check += s.left3();
        if (!s.isSolved()) {
            cout << s << endl;
        }
    }
    assert(check == 24702);
    timer.stop();
    cout << "Completed solving with map in: " << timer.tijd() << endl;

    // test every sudoku with bitmap implementation
    timer.start();
    check = 0;
    for (int i = 1; i <= 50; i++) {
        auto filename = "sudokus/" + to_string(i) + ".txt";
        auto s = Sudoku(filename);
        s.solveBitmap();
        check += s.left3();
        if (!s.isSolved()) {
            cout << s << endl;
        }
    }
    assert(check == 24702);
    timer.stop();
    cout << "Completed solving with bitmap in: " << timer.tijd() << endl;

    // test invalid case with map -> return early?
    auto filename = "invalid.txt";
    auto s = Sudoku(filename);
    bool res = s.solveMap();
    assert(res == 0);
    assert(s.isSolved() == 0);

    // test invalid case with bitmap -> return early?
    s = Sudoku(filename);
    res = s.solveBitmap();
    assert(res == 0);
    assert(s.isSolved() == 0);
}
