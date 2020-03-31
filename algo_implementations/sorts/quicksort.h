#ifndef QUICKSORT_H
#define QUICKSORT_H

#include <unistd.h>

#include "sorteermethode.h"

/** \class QuickSort
 * Ω(n log(n))
 * Θ(n log(n))
 * O(n^2) -> gelijke elemnten / omgekeerd volgorde
 *  -> deze case kan met grote kans vermenden worden door pivot slimmer te kiezen
 *  -> random / mediaan van drie; waarbij mediaan van drie te prefereren is
*/
template <class T>
class QuickSort : public Sorteermethode<T>  {
    void operator()(vector<T> & v) const {
//        srand(getpid());
        quick_sort(v, 0, v.size() - 1);
    }

    void median_of_three(vector<T>& v, int m1, int m0, int m2) const {
        // mediaan berekenen van 3 elementen;
        // mediaan komt in m1
        // start        3 2 1 : 1 2 3 : 1 3 2
        // m1 < m0?     2 3 1 : 1 2 3 : 1 3 2
        // m2 < m1?     3 1 2 : 1 2 3 : 1 2 3
        //    m1 < m2?  3 2 1 : 1 2 3 : 1 2 3
        if (v[m1] < v[m0]) {
            swap(v[m1], v[m0]);
        }

        if (v[m2] < v[m1]) {
            swap(v[m2], v[m1]);
            if (v[m1] < v[m0]) {
                swap(v[m1], v[m0]);
            }
        }
    }

    /**
     * Partitie gedeelte:
     * Opslitsen in twee partities
     *  Linkse partitie -> alle elementen <= pivot
     *  Rechtse partitie -> alle elementen >= pivot
     */
    void quick_sort(vector<T>& v, int start, int end) const {
        // stopconditie recursie (minder dan 2 elementen)
        if (start < end) {
            // partitie gedeelte
            int pivot = partition(v, start, end);
            quick_sort(v, start, pivot);
            quick_sort(v, pivot + 1, end);
        }
    }

    int partition(vector<T>& v, int start, int end) const {
        // worst case zoveel mogelijk vermijden
        // random pivot
//        int pvt_idx = rand() % (start - end) + start;
//      // mediaan van 3
        median_of_three(v, start, start + (end - start) / 2,  end);

        T pivot = v[start];
        int l = start;
        int r = end;

        while (v[r] > pivot) {
            r--;
        }

        while (l < r) {
            swap(v[l], v[r]);
            l++; r--;

            while (v[l] < pivot) {
                l++;
            }

            while (v[r] > pivot) {
                r--;
            }
        }
        // r used as divider between two partitions (r now last element of <= pivot partition)
        return r;
    }
};

#endif

