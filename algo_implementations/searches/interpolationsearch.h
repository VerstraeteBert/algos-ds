//
// Created by Bert Verstraete on 31/03/2020.
//
#ifndef INTERPOLATIONSEARCH_H
#define INTERPOLATIONSEARCH_H

/**
 * Can we do better than binary search on uniformly distributed datasets? Hell yeah!
 * Interpolation search works like we would search a phonebook;
 *      -> if the person we're searching is lower alphabetically search left side
 *      -> BUT if it's much lower, search more towards the left, otherwise search more towards left of middle
 *
 * O(lg(lg(N))) time complexity if uniformly distributed
 *  OR O(N) in the worst case
 *
 * Only valuable for large arrays because of the complicated repeated calculations
 */
template <class T>
int interpolation_search(const vector<T>& v, const T& key) {
    int l = 0;
    int r = v.size() - 1;

    while ((v[r] != v[l]) && (key >= v[l]) && (key <= v[r])) {
        int m = l + ((key - v[l]) * (r - l) / (v[r] - v[l]));

        if (v[m] < key)
            l = m + 1;
        else if (key < v[m])
            r = m - 1;
        else
            return m;
    }

    if (key == v[l])
        return l ;
    else
        return -1;
}
#endif // INTERPOLATIONSEARCH_H
