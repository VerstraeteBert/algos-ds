#ifndef INSERTIONSORT_H
#define INSERTIONSORT_H

#include "sorteermethode.h"

/** \class InsertionSort
*/
template <class T>
class InsertionSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        for (int i = 1; i < v.size(); i++) {
            int j = i - 1;
            auto el = move(v[i]);
            while (j >= 0 && v[j] > el) {
                v[j + 1] = move(v[j]);
                j--;
            }
            v[j + 1] = move(el);
        }
    }
};

#endif

