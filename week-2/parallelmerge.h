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
void merge_sort(vector<T>& vec, int start, int end, int thread_pool);
template <class T>
void merge(vector<T>& vec, int start, int mid, int end);

/** \class ParallelMerge
*/
template <class T>
class ParallelMerge : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        merge_sort(v, 0, v.size() - 1, thread::hardware_concurrency());
    }
};

template <class T>
void merge_sort(vector<T>& vec, int start, int end, int thread_pool)  {
    if (start < end) {
        int middle = (start + end) / 2;

        if (thread_pool >= 2) {
            auto fn = async(launch::async, [&] { merge_sort(vec, start, middle, thread_pool - 2); });
            merge_sort(vec, middle + 1, end, thread_pool - 2);
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

    for (int i = 0; i < curr; i++) {
        vec[start++] = move(temp[i]);
    }
}

#endif
