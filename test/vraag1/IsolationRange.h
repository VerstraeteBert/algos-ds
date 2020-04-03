#ifndef ISOLATIONRANGE_H
#define ISOLATIONRANGE_H
using namespace std;

template <class T>
class IsolationRange {
    public:
        const T* min;
        const T* max;
        const T& N;

        explicit IsolationRange(const T& range) : N(range) {};

        ~IsolationRange() {
            min = nullptr;
            max = nullptr;
        }

        IsolationRange& operator=(IsolationRange<T>&& other) noexcept {
            if (&other != this) {
                this->min = other.min;
                this->max = other.max;
            }
            return *this;
        }

        /**
         * Ensure both that a key is within the bounds of a range
         *      - the key needs to be <= (min + N)
         * If the key fits within the range the range is updated to reflect this
         *      - if the key is smaller than the current min
         *          - min is replaced with the key
         *      - if the key is larger than the current max
         *          - max is replaced with the key
         */
        bool ensureValidBoundsAndUpdate(const T& new_key) {
            // error handling -> what if new_key is nullptr
            if (new_key < *this->min) {
                if (validateRange(new_key, *this->max)) {
                    this->min = &new_key;
                } else {
                    return false;
                }
            } else if (new_key > *this->max) {
                if (validateRange(*this->min, new_key)) {
                    this->max = &new_key;
                } else {
                    return false;
                }
            }
            // key must be equal to current min or max; still valid
            return true;
        };

        /**
         * Compares two ranges:
         * if there's an overlap, the number of overlapping elements is returned
         * if there's no overlap, 0 is returned.
         *
         * Determining overlap:
         *  Imagine two ranges
         *  a [----]
         *  b    [---]
         *  The b's minimum must be <= to the a's maximum to have an overlap
         *  Since the ranges could also be compared the other way around,
         *  a    [---]
         *  b [----]
         *  the a's minimum must also be <= to b's maximum
         *  Notice that in both the order, the conditions still must hold true
         *
         *  This logic can be easily inverted (look at the example below)
         *      b.min > a.max || a.min > b.max
         *     a [---]
         *     b         [---]
         *
         *  If there's an overlap we need to figure out the minimum and maximum bound of intersection
         *  a    [---]
         *  b [----]
         *  From the example we can easily see that a's minimum is the minimum bound of the intersection;
         *  conversely b's maxmimum is the maximum bound of the intersection
         *
         *  To generalize this, since the ranges can be in any order
         *  we need to figure out the max(a.min, b.min) and use this as the mimimum bound of the intersection
         *  While min(a.max, b.max) is the maximum bound of the intersection;
         *
         *  e.g.
         *  a [6 10]
         *  b [8 12]
         *
         *  max(a.min, b.min) == 8
         *  min(a.max, b.max) == 10
         *
         *  number of elements in intersection (8, 9, 10)
         *      == (10 - 8) + 1
         */
        int calculateNumberOverlaps(const IsolationRange<T>& other) {
                if (*other.min > *this->max || *this->min > *other.max) {
                    // no intersection
                    return 0;
                } else {
                    // intersection found: return number of overlapping elements
                    return (std::min(*this->max, *other.max) - std::max(*this->min, *other.min)) + 1;
                }
        }

    private:
        bool validateRange(const T& key_min, const T& key_max) {
            return (key_max - key_min) <= this->N;
        }
};

#endif // ISOLATIONRANGE_H