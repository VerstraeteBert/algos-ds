#ifndef MERGESORT_H
#define MERGESORT_H

#include "sorteermethode.h"

/** \class MergeSort
*/
template <class T>
class MergeSort : public Sorteermethode<T>  {
    void operator()(vector<T> & v) const {
        merge_sort(v, 0, v.size() - 1);
    }

    void merge_sort(vector<T>& vec, int start, int end) const {
        if (start < end) {
            int middle = (start + end) / 2;
            merge_sort(vec, start, middle);
            merge_sort(vec, middle + 1, end);
            merge(vec, start, middle, end);
        }
    }

    void merge(vector<T>& vec, int start, int mid, int end) const {
        int l = start; int r = mid + 1; int curr = 0;
        auto temp = vector<T>(end - start + 1);
        while (l <= mid && r <= end) {
            if (vec[l] <= vec[r]) {
                temp[curr] = move(vec[l]);
                l++;
            } else {
                temp[curr] = move(vec[r]);
                r++;
            }
            curr++;
        }

        while (l <= mid) {
            temp[curr] = move(vec[l]);
            curr++;
            l++;
        }

        while (r <= end) {
            temp[curr] = move(vec[r]);
            curr++;
            r++;
        }

        for (int i = 0; i <= temp.size(); i++) {
            vec[i + start] = move(temp[i]);
        }
    }
};

#endif

