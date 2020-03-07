#ifndef PARALLELMERGE_H
#define PARALLELMERGE_H

#include "sorteermethode.h"
#include <iostream>
#include <thread>
#include <future>
#include <iterator>
#include <vector>

using namespace std;

template <class T>
void merge_sort(vector<T>& vec, int start, int end, int hw_threads);
template <class T>
void merge(vector<T>& vec, int start, int mid, int end);

/** \class ParallelMerge
 * Nog niet 100% werkend :-(
*/
template <class T>
class ParallelMerge : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        merge_sort(v, 0, v.size() - 1, thread::hardware_concurrency());
    }
};

template <class T>
void merge_sort(vector<T>& vec, int start, int end, int hw_threads)  {
    if (start < end) {
        int middle = (start + end) / 2;

        if (hw_threads >= 2) {
            auto fn = std::async(launch::async, [&] { merge_sort(vec, start, middle, hw_threads - 2); });
            merge_sort(vec, middle + 1, end, hw_threads - 2);
            fn.wait();
        } else {
            merge_sort(vec, start, middle, 0);
            merge_sort(vec, middle + 1, end, 0);
        }

        merge(vec, start, middle, end);
    }
}

template <class T>
void merge(vector<T>& vec, int start, int mid, int end) {
    int l = start; int r = mid + 1; int curr = 0;
    // al gesorteerd
    if (vec[mid] <= vec[r]) {
        return;
    }
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

#endif
