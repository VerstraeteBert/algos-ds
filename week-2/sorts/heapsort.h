#ifndef HEAPSORT_H
#define HEAPSORT_H

#include "./sorteermethode.h"

template<class T>
void build_max_heap(vector<T>&);
template<class T>
void max_heapify (vector<T>&, int, int);
/**
 * \class HeapSort
 * Average/wordt: O(nlogn)
 * Ω(nlogn) (distinct keys)
 * Ω(n) (equal keys)
 * unstable
 *
 * 1. create an initial stable max_heap
 * 2. swap root (max-element) with last leaf node, the very last part of array is now considered sorted
 *    -> decreased size of considered array by 1
 * 3. sift new first element down to its correct position; which will ensure the max element is at the root again
 * 4. goto 2 unless only one element remains
 */
template <class T>
class HeapSort : public Sorteermethode<T> {
        void operator()(vector<T> & v) const {
            build_max_heap(v);

            for (int i = v.size() - 1; i > 0; i--) {
                swap(v[i], v[0]);
                max_heapify(v, 0, i);
            }
        }
};

/**
 * max_heapify ensures a correct substree, starting from the root element of the subtree
 *  1. compare values of parent with children
 *      if any of children larger than parent -> pick max child as new parent -> goto 2.
 *      else done
 *  2. swap largest child with parent
 *  3. recurse down affected subtree, goto 1 with parent node set to new idx of previous parent
 *       e.g. recurse down affected subtree
 *                10                        10
 *             2                        5
 *          1    5           =>      1    2
 *             1   3                    1   3
 *      1. 2 and 5 will be swapped, however 3 is still greater than 2;
 *      so we must recursively go deeper into the subtree to ensure its also in a correct max-heapy state.
 */
template <class T>
void max_heapify(vector<T>& v, int parent_idx, int size) {
    int idx_largest = parent_idx;
    int l_child_idx = parent_idx * 2 + 1;
    int r_child_idx = parent_idx * 2 + 2;

    // always boundscheck; to ensure we don't try on a non-existing child
    if (l_child_idx < size && v[l_child_idx] > v[idx_largest]) {
        idx_largest = l_child_idx;
    }

    if (r_child_idx < size && v[r_child_idx] > v[idx_largest]) {
        idx_largest = r_child_idx;
    }

    if (idx_largest != parent_idx) {
        swap(v[parent_idx], v[idx_largest]);

        max_heapify(v, idx_largest, size);
    }
}

/**
 * Builds max heap by appropriately swapping parents with children that might be larger
 * -> thus we start from the last parent node; which is always (v.size() - 2) / 2
 * Consider 0   L1: 1 2  l2: 3 4 5 6
 * Index of 2 is indeed (7 - 2) / 2
 */
template <class T>
void build_max_heap(vector<T>& v) {
    for (int parent_idx = (v.size() - 2)  / 2; parent_idx >= 0; parent_idx--) {
        max_heapify(v, parent_idx, v.size());
    }
}


#endif
