#ifndef STLSORT_H
#define STLSORT_H

#include "../sorts/sorteermethode.h"
#include <algorithm>

/** \class STLSort
*/
template <class T>
class STLSort : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        std::sort(v.begin(), v.end());
    }
};

#endif

