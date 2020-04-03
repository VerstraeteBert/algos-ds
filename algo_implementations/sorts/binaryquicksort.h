#ifndef BINARYQUICKSORT_H
#define BINARYQUICKSORT_H

// bit size of int, minus sign bit
const int INT_SIZE = sizeof(int) * 8 - 1;

template <class T>
class BinaryQuicksort : public Sorteermethode<T>  {
    void operator()(vector<T> & v) const {
        binary_quicksort(v, 0, v.size() - 1, 0);
    }

    int get_i_bit(int num, int n) const {
        return (num >> (INT_SIZE - n)) & 1;
    }

    // implementatie voor ints
    // zelfde als quicksort, maar we nemen als pivot een bit
    // 1) partitioneer in twee helften
    //      - links: n'de bit is 0
    //      - rechts: n'de bit is 1
    // ga terug naar 1 met volgende bit
    // complexiteit:
    //  -> random bits: O(n*log(n)) (echter met betere partitionering dan qsort)
    //  -> niet random bits -> quicksort beter
    // er zit nog een foutje in de implementatie, kan deze niet vinden
    void binary_quicksort(vector<T>& vec, int l, int r, int n_bit) const {
        if (r <= l || n_bit > INT_SIZE) return;

        int i = l;
        int j = r;

        while (j != i) {
            while (get_i_bit(vec[i], n_bit) == 0 && i < j) {
                i++;
            }
            while (get_i_bit(vec[i], n_bit) == 1 && j > i) {
                j--;
            }
            swap(vec[i], vec[j]);
        }

        if (get_i_bit(vec[r], n_bit) == 0) {
            j++;
        }

        binary_quicksort(vec, l, j - 1, n_bit + 1);
        binary_quicksort(vec, j, r, n_bit + 1);
    }

};

#endif //BINARYQUICKSORT_H
