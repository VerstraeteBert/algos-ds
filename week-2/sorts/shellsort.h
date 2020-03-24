#ifndef SHELLSORT_H
#define SHELLSORT_H

#include "sorteermethode.h"
#include <iostream>

/** \class Shellsort
*/
template <class T>
class ShellSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        // naïve reeks creatie (n/2^i)
        for (int gap = v.size() / 2; gap >= 1; gap /= 2) {
            // per gap insertion sort
            for (int i = gap; i < v.size(); i++) {
                auto el = move(v[i]);
                int j = i - gap;
                while (j >= 0 && el < v[j]) {
                    v[j + gap] = move(v[j]);
                    j -= gap;
                }
                v[j + gap] = move(el);
            }
        }
    }
};

#endif