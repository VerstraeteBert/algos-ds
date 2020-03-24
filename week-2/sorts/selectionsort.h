#ifndef SELECTIONSORT_H
#define SELECTIONSORT_H

#include "sorteermethode.h"

/** \class SelectionSort
*/
template <class T>
class SelectionSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
       int minIdx;
       for (int i = 0; i < v.size() - 1; i++) {
           minIdx = i;
           for (int j = i + 1; j < v.size(); j++) {
               if (v[j] < v[minIdx]) {
                   minIdx = j;
               }
           }
           swap(v[minIdx], v[i]);
       }
    }
};

#endif
