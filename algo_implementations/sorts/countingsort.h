#ifndef COUNTING_SORT_H
#define COUNTING_SORT_H

#include <vector>

using namespace std;

template <class T>
class CountingSort : public Sorteermethode<T> {
    void operator()(vector <T> &v) const {
        if (v.size() == 0) return;

        int min = v[0];
        int max = v[0];
        for (int i = 1; i < v.size(); i++) {
            if (v[i] < min) {
                min = v[i];
            } else if (v[i] > max) {
                max = v[i];
            }
        }

        vector<int> cum_sum = vector<int>(max - min + 1);

        for (int el : v) {
            cum_sum[el - min]++;
        }

        for (int i = 1; i < cum_sum.size(); i++) {
            cum_sum[i] += cum_sum[i - 1];
        }

        vector<int> res = vector<int>(v.size());

        for (int i = v.size() - 1; i >= 0; i--) {
            int idx = cum_sum[res[i] - min];
            cum_sum[res[i] - min]--;
            res[idx] = res[i];
        }

        v = move(res);
    }
};

#endif //COUNTING_SORT_H
