#include <vector>
#include <iostream>
#include "DiameterComparison.cpp"

using namespace std;
class Matcher {
    public:
        static vector<pair<Deksel, Pot>> match(const vector<Deksel>&,  const vector<Pot>&);
    private:
        static void quick_match(vector<Deksel>&, vector<Pot>&, int, int);
        template <class T, class G>
        static pair<int, int> partition(vector<T>& v, const G& pivot, int start, int end);
};

/**
 * Matches deksels with a certain diameter with potten of the same diameter
 * Preconditions -> vectors of same size, and a match exists for each element
 * O(2N) -> O(N) memory since it is a pure function
 *
 * Deksels and potten cannot be directly be compared with themselves;
 * preventing initial sorting of the arrays and a linear selection afterwards.
 *
 * The algorithm comprises of two steps
 *      1. lining up elements in both vectors using an adaptation of quicksort
 *      2. linear pairing of lined up elements of the two vectors
 */
vector<pair<Deksel, Pot>> Matcher::match(const vector<Deksel>& v_deksel_orig, const vector<Pot>& v_pot_orig) {
    // copy both vectors; ensure a pure function
    auto v_deksel = vector<Deksel>(v_deksel_orig);
    auto v_pot = vector<Pot>(v_pot_orig);

    // line up elements
    quick_match(v_deksel, v_pot, 0, (int) v_deksel.size() - 1);

    // match pairs after lining up
    auto res = vector<pair<Deksel, Pot>>();
    // immediately reservere correct size to avoid unnecessary copying when resizes need to happen
    res.reserve(v_deksel.size());

    // move vector elements; to avoid possibly costly copying.
    // it must be noted however, since Deksel and Potten are still trivially copyable
    // that this has no effect on performance, to emulate a more realistic scenario with larger data container;
    // I left the move here.
    for (int i = 0; i < v_deksel.size(); i++) {
        res.emplace_back(move(v_deksel[i]), move(v_pot[i]));
    }

    return res;
}

/**
 * Quick_match is an adaptation of the divide and conquer algorithm quicksort, as proposed in the assignment.
 *      Partitioning using the Dutch National Flag problem algorithm, which partitions in-place in Θ(N) time
 *      Just like the standard quicksort, it is not stable.
 *              O(N*LOG(N) TIME
 *              O(LOG(N)) SPACE (only recursion; in-place swapping)
 *
 *      Preconditions -> vectors of same size, and a match exists for each element
 *
 *          1. Partition one of the vectors using a arbitrary pivot from the other vector (first element picked):
 *                  The first partition containing elements smaller than the pivot
 *                  The second containing all elements equal to the pivot
 *                  The third containing all elements larger than the pivot
 *                                       [lt ; eq ; gt]
 *              This first partitioning step returns the bounds of the equal partition for use in the next steps
 *
 *          2. The same thing is done with the other vector:
 *              Since we cannot compare the original pivot (which is of the same type as this vector)
 *              one of the elements described by the returned eq bounds can be used and passed in as pivot element.
 *
 *              Given the precondition that the vectors are of them same size, and a match exists for each element,
 *              this will line up the pairs that have the same diameter values as the pivot in both arrays.
 *              In both vectors, this section of the array is in the correct position and is fully processed.
 *
 *          3. Recursion
 *              Now only the elements in the lt and gt partitions are possible not lined up.
 *              With the bounds of the eq partition returned from step 1, which is the idx of the first eq and last eq element.
 *              Goto 1 with new bounds, as long as there at least 2 elements to process (start < end).
 *                                                start                       end
 *                  Quick_match lt partition: [start                    eq_left_bound - 1]
 *                  Quick_match gt partition: [eq_right_bound + 1             end        ]
 *
 *              These bounds are safe; imagine two notable edge cases:
 *                      1. eq_left_bound = 0  OR eq_right_bound = v.size()-1
 *                          [1 1 2 3] (with pivot 1)
 *                          No smaller elements -> left recursion will immeditaly hit the exit condition
 *                      2. No smaller or larger elements
 *                          [1 1 1 1] (pivot 1, of course)
 *                          Immediately hit the exit condition on both sides
 *
 *          This implementation sorts both vectors as a side effect;
 *              by having the left partition be the smaller elements
 *              and the right partition being the larger elements
 *
 */
void Matcher::quick_match(vector<Deksel>& v_deksel,vector<Pot>& v_pot, int start, int end) {
    if (start < end) {
        pair<int, int> pivot_indices = partition(v_deksel, v_pot[start], start, end);
        partition(v_pot, v_deksel[pivot_indices.first], start, end);
        quick_match(v_deksel, v_pot, start, pivot_indices.first - 1);
        quick_match(v_deksel, v_pot, pivot_indices.second + 1, end);
    }
}

/**
 * Partitions vector based on a given pivot of another type
 *  - Θ(N) time complexity, in-place -> O(1) memory
 *  Forming three partitions
 *     [ lt ; eq ; gt ]
 *
 *  Uses three pointers
 *      runner -> linearly scans vector and compares elements with pivot
 *      lt_place -> pointing to end of known lt partition (initially leftmost idx)
 *      gt_place -> pointing to start of known gt partition (initially rightmost idx)
 *
 *  In each iteration the element at the index of runner is compared with the pivot
 *     putting elements gt or lt the pivot in their respective partitions
 *     while pushing elements eq to the pivot towards the middle
 *
 *      - if (v[runner] < pivot)
 *          -> the element belongs in the lt partition
 *          -> v[runner] swapped with v[lt_place]
 *          -> increment both pointers
 *      - if (v[runner] == pivot)
 *          -> no swaps, advance runner
 *      - if (v[runner] > pivot)
 *          -> swap v[runner] with v[gt_place]
 *          -> decrement only gt_place, since swapped element could belong in the lt partition
 *
 * Returns bounds of eq partition -> since this partition is in the correct spot
 *                                      and can be used to divide problems for quick_match
 *
 *  pivot: 2
 *    ↓           ↓
 *  [ 1 2 3 1 3 2 2 ] (v[runner] < pivot) -> swap(v[runner], v[lt_place]) -> increment both
 *    ↑
 *
 *      ↓         ↓
 *  [ 0 1 2 0 2 1 1 ] (v[runner] == pivot) -> advance runner
 *      ↑
 *
 *      ↓         ↓
 *  [ 0 1 2 0 2 1 1 ] (v[runner] > pivot) -> swap(v[runner],v[gt_place]) -> decrement gt_place
 *        ↑
 *
 *      ↓       ↓
 *  [ 0 1 1 0 2 1 2 ] (v[runner] == pivot) -> advance runner
 *        ↑
 *
 *      ↓       ↓
 *  [ 0 1 1 0 2 1 2 ] (v[runner] < pivot) -> swap(v[runner], v[lt_place]) -> increment both
 *          ↑
 *
 *        ↓     ↓
 *  [ 0 0 1 1 2 1 2 ] (v[runner] > pivot) -> swap(v[runner],v[gt_place]) -> decrement gt_place
 *            ↑
 *
 *        ↓   ↓
 *  [ 0 0 1 1 1 2 2 ] (v[runner] == pivot) -> all elements are already correcty partitioned
 *            ↑                               However, we cannot be sure if runner currently
 *                                            contains an element which should be on the lt partition
 *                                            thus, another iteration (runner <= gt_place)!!
 *
 *        ↓   ↓
 *  [ 0 0 1 1 1 2 2 ] (runner > gt_place) -> Done
 *              ↑
 *
 *  lt_place -> left bound of eq
 *  gt_place -> right bound of eq
 *
 *  As a side note; a comparator could be passed into this method; to make it more templateable.
 *  This comparator could then get passed down from the non-generic match_sort implementation.
 *  However, that seems like an unnecessary abstraction at this point.
 */
template<class T, class G>
pair<int, int> Matcher::partition(vector<T>& v, const G& pivot, int start, int end) {
    int lt_place = start;
    int gt_place = end;
    int runner = start;

   while (runner <= gt_place) {
       if (dia_lt(v[runner], pivot)) {
           swap(v[runner], v[lt_place]);
           lt_place++;
           runner++;
       } else if (dia_gt(v[runner], pivot)) {
           swap(v[runner], v[gt_place]);
           gt_place--;
       } else {
           runner++;
       }
   }

   return pair<int, int>(lt_place, gt_place);
}
