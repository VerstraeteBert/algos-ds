#ifndef CYCLICSEARCH_H
#define CYCLICSEARCH_H

#include <vector>

using namespace std;

/**
 * An element in a sorted array can be found in O(log n) time via binary search.
 * But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand.
 * We can still find the location in O(log N) time using an adaptation
 *
 *  1) Find middle point mid = (l + h)/2
 *  2) If key is present at middle point, return mid.
 *  3) Else If arr[l..mid] is sorted
 £      a) If key to be searched lies in range from arr[l]
 *          to arr[mid], recur for arr[l..mid].
 *      b) Else recur for arr[mid+1..h]
 *  4) Else (arr[mid+1..h] must be sorted)
 *      a) If key to be searched lies in range from arr[mid+1]
 *         to arr[h], recur for arr[mid+1..h].
 *      b) Else recur for arr[l..mid]
 */
template <class T>
int interpolating_search(vector<T>& v, T& key) {
    return search_part(v, 0, v.size() - 1, key);
}

template <class T>
int search_part(const vector<T>& v, int l, int r, const T& key) {
    // key not present
    if (l > r) return -1

    int m = l + (r - l) / 2;
    // found key?
    if (v[m] == key) return m;

    // left partition is sorted
    if (v[l] <= v[m]) {
        // if key in this partition, binary search it
        if (key >= v[l] && key <= v[m]) {
            return search_part(v, l, m - 1, key);
        }

        // key must be in other partition
        return search_part(v, m + 1, r, key);
    }

    // right half must be sorted
    // if key in right partition, binary search it
    if (key >= v[m] && key <= v[r]) {
        return search(v, m + 1, r, key);
    }
    // key must be in other partition
    return search(v, l, m - 1, key);
}

#endif //CYCLICSEARCH_H
