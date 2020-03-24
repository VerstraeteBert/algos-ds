#ifndef PARALLELMERGE_H
#define PARALLELMERGE_H

#include "sorteermethode.h"
#include <iostream>
#include <thread>
#include <future>
#include <iterator>
#include <vector>

using namespace std;

const int THRESHOLD = 32;

template <class T>
void merge_sort(vector<T>& vec, int start, int end, int thread_pool);
template <class T>
void merge(vector<T>& vec, int start, int mid, int end);
template <class T>
void insertion_sort(vector<T>& v, int start, int end);

/** \class ParallelMerge
*/
template <class T>
class ParallelMerge : public Sorteermethode<T> {
    void operator()(vector<T> & v) const {
        merge_sort(v, 0, v.size() - 1, thread::hardware_concurrency());
    }
};

template <class T>
void insertion_sort(vector<T>& v, int start, int end) {
    for (int i = start + 1; i <= end; i++) {
        auto el = move(v[i]);
        int j = i - 1;
        while (j >= start && v[j] > el) {
            v[j + 1] = move(v[j]);
            j--;
        }
        v[j + 1] = move(el);
    }
}

template <class T>
void merge_sort(vector<T>& vec, int start, int end, int thread_pool)  {
    if (end - start > THRESHOLD) {
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
    } else {
        insertion_sort(vec, start, end);
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
