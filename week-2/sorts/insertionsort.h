#ifndef INSERTIONSORT_H
#define INSERTIONSORT_H

#include "sorteermethode.h"

/** \class InsertionSort
*/
template <class T>
class InsertionSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        int i;
        for (i = 1; i < v.size(); i++) {
            auto el = move(v[i]);
            int j = i - 1;
            while (j >= 0 && v[j] > el) {
                v[j + 1] = move(v[j]);
                j--;
            }
            v[j + 1] = move(el);
        }
    }
};

#endif
