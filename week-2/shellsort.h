#ifndef SHELLSORT_H
#define SHELLSORT_H

#include "sorteermethode.h"
#include <iostream>

/** \class Shellsort
*/
template <class T>
class ShellSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        int size = v.size();
        for (int gap = size / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < size; i++) {
                auto temp = move(v[i]);

                int j = i;
                while (j >= gap && v[j - gap] > temp) {
                    v[j] = move(v[j - gap]);
                    j -= gap;
                }
                v[j] = move(temp);
            }
        }
    }
};

#endif
