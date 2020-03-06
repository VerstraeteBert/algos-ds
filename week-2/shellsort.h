#ifndef SHELLSORT_H
#define SHELLSORT_H

#include "sorteermethode.h"
#include <iostream>

/** \class Shellsort
*/
template <class T>
class ShellSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        for (int gap = v.size() / 2; gap > 0; gap--) {
            for (int curr = gap; curr < v.size(); curr++) {
                if (v[curr] < v[curr - gap]) {
                    auto el = move(v[curr]);
                    v[curr] = move(v[curr - gap]);
                    v[curr - gap] = move(el);
                }
            }
        }
    }
};

#endif

