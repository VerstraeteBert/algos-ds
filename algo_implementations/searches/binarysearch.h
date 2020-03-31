#ifndef BINARYSEARCH_H
#define BINARYSEARCH_H

template <class T>
int binary_search(const vector<T>& v, const T& needle) {
    return search_partition(v, 0, v.size() - 1, needle);
}

template <class T>
int search_partition(const vector<T>& v, int l, int r, const T& needle) {
    while (l <= r) {
        int m = (l + r) / 2 + l;
        if (needle == v[m]) {
            return m;
        }

        // needle in first half of array?
        if (needle < v[m]) {
            r = m - 1;
        } else {
            // must be in second half
            l = m + 1;
        }
    }
    return v.size();
}

#endif //BINARYSEARCH_H
