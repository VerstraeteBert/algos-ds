#ifndef BINARYSEARCH_H
#define BINARYSEARCH_H

template <class T>
int binary_search(vector<T>& v, T& needle) {
    int l = 0; r = v.size() - 1;

    while (l <= r) {
        int m = (l + r) / 2 + l;
        if (needle == v[m]) {
            return m;
        }

        if (needle < v[m]) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    return v.size();
}

#endif //BINARYSEARCH_H
