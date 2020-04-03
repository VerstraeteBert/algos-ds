#ifndef INFINITESEARCH_H
#define INFINITESEARCH_H

#include "./binarysearch.h"
#include <vector>

using namespace std;

template <class T>
/**
 * Searching in an ordered infinite array
 *      -> binary search won't work; since we don't know the right bound
 *
 * First we must find a value in the array that is larger than the key, defining an upper bound
 * -> we check a row of indices 0 1 2 4 8 16 ...
 *      -> whenever a value at that index is larger -> r,
 *          we know that the key must be between that index (r) and the previous index (l)
 * -> normal binary search from found l -> r
 *
 * Complexity
 *  O(log(n)) steps needed to find the right bound
 *  ; size of partition from l -> r will be ~N, binary searching this is O(log(N)) complexity
 *    -> 2 * (log(n)) ~= log(n)
 */

int infinite_search(const vector<T>& v, const T& key) {
    int l = 0;
    int r = 1;

    // is first element the key?
    if (v[l] == key) return l;

    while (v[r] < key) {
        l = r;
        r *= 2;
    }

    return search_partition(v, l, r, key);
}

#endif // INFINITESEARCH_H
