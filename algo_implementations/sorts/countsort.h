//
// Created by Bert Verstraete on 31/03/2020.
//

#ifndef COUNTSORT_H
#define COUNTSORT_H

#include <vector>
#include <iostream>

using namespace std;

/**
 * Counting sort is an algorithm for sorting object based on small integer key values
 * 1) find range of min element -> max element
 * 2) build freq table with the count of each unique key
 * 3) modify freq_table to be the cumulative count of each key up to then
 *  -> this modified freq_table indicates the position of each object in the output sequence
 * 4) output each object from the input arr into an output arr; using the positions in the freq_table;
 *      -> decrease the count in the freq_table on each insertion
 */

template <class T>
class CountSort : public Sorteermethode<T>  {
    void operator()(vector<T> & v) const {
        // already sorted
        if (v.size() <= 1) return;

        // find range of elements
        // at most max - min + 1 distinct elements
        // e.g: max = 6; min = 2
        // 2 3 4 5 6 -> 5 distinct elements
        // identify min and max
        T max = v[0];
        T min = v[0];
        for (int i = 1; i < v.size(); i++) {
            if (max < v[i]) {
                max = v[i];
            }
            else if (min > v[i]) {
                min = v[i];
            }
        }

        vector<int> freq_table = vector<int>(max - min + 1);
        // find frequency of each element, save in freq table
        for (int i = 0; i < v.size(); i++) {
            freq_table[v[i] - min]++;
        }

        // find cumulative frequency of each element
        for (int i = 1; i < freq_table.size(); i++) {
            freq_table[i] += freq_table[i - 1];
        }

        // output vec
        vector<T> output = vector<T>(v.size());
        // put elements in correct position
        // from back to front to ensure stability
        for (int i = v.size() - 1; i >= 0; i--) {
            output[ freq_table[v[i] - min] - 1 ] = move(v[i]);
            freq_table[v[i] - min]--;
        }

        v = move(output);
    }
};

#endif //COUNTSORT_H
