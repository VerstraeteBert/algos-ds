#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <set>
#include <queue>
#include <chrono>
#include <random>
#include <algorithm>
#include <string>

#include "hashfunctions.h"
#include "containers.h"

/*
Reads all the files in "folder". Assumes that they are named 0.py, 1.py, ...
Returns a vector with for each file a set of of tokens in that file. 
Tokens are unique words or bigrams (two sequential words).
*/
std::vector<std::set<std::string>> readDatafiles(const char *folder)
{
    auto start = std::chrono::high_resolution_clock::now();

    std::vector<std::set<std::string>> contents;

    int i = 0;
    std::ifstream in(folder + std::to_string(i) + ".py");

    while (in)
    {
        std::string word;
        std::string previous = "";
        contents.push_back(std::set<std::string>());

        while (in)
        {
            in >> word;
            contents[i].insert(word);

            previous = previous + " " + word;
            contents[i].insert(previous);

            previous = word;
        }

        i++;
        in = std::ifstream(folder + std::to_string(i) + ".py");
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "Reading the data files took " << duration.count() << " ms" << std::endl;

    return contents;
}

// Replaces each unique word with a unique id (0, 1, 2, ...)
// uses a map to keep track of words previously mapped to an unique id, so duplicates receive the same number
std::vector<std::set<int>> replaceWithUniqueId(const std::vector<std::set<std::string>> &input)
{
    auto start = std::chrono::high_resolution_clock::now();

    // using an unordered map for O(1) amortized lookups, normal map would be O(LogN)
    std::unordered_map<std::string, int> memo;
    int UID = 0;
    std::vector<std::set<int>> contents(input.size());

    for (int i = 0; i < input.size(); i++) {
        for (const auto& str : input[i]) {
            auto memo_itr = memo.find(str);
            if (memo_itr == memo.end()) {
                memo.emplace(str, UID);
                contents[i].emplace(UID);
                UID++;
            } else {
                contents[i].emplace(memo_itr->second);
            }
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "Replacing words with IDs took " << duration.count() << " ms" << std::endl;
    return contents;
}

// Replaces each word with its hash code
template <unsigned int (*hashfunction)(const std::string &)>
std::vector<std::set<int>> replaceWithHash(const std::vector<std::set<std::string>> &input)
{
    auto start = std::chrono::high_resolution_clock::now();

    std::vector<std::set<int>> contents(input.size());

    for (int i = 0; i < input.size(); i++) {
        for (const auto& str : input[i]) {
            contents[i].emplace(hashfunction(str));
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "Replacing words with hash values took " << duration.count() << " ms" << std::endl;
    return contents;
}

// prints a ordered list of hashcodes and their number of collisions, and corresponding elements that caused the collisions.
// since we want it to be ordered, map is the ideal choice vs unordered_map. While it also offers guaranteed performance of O(logN) for finds.
template <unsigned int (*hashfunction)(const std::string &)>
void findCollisions(const std::vector<std::set<std::string>> &input)
{
    auto start = std::chrono::high_resolution_clock::now();
    std::map<int, std::set<std::string>> collision_map;

    std::cout << "----------- COLLISIONS -----------" << std::endl;
    int num_collisions = 0;

    for (const auto& vec : input) {
        for (const auto& str : vec) {
            collision_map[hashfunction(str)].emplace(str);
        }
    }

    for (const auto& pair :  collision_map) {
        if (pair.second.size() == 1) continue;
        num_collisions += (pair.second.size());

        std::cout << pair.second.size() << " Collisions found with hashcode " << pair.first << ":" << pair.second << std::endl;
    }
    std::cout << "Total number of collisions found: " << num_collisions << std::endl;
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "Printing colissions took " << duration.count() << " ms" << std::endl;
}

// Calculates numbers of equal elements present in two given sets
// This is pretty much a copy of the logic in the std::set_intersection implementation, however,
// instead of copying the elements into a new set, only the amount of overlapping elements are counted.
// to both save memory and time copying.
template <class T>
int get_count_intersect(const std::set<T>& set_a, const std::set<T>& set_b) {
    auto iter_a = set_a.cbegin();
    auto iter_b = set_b.cbegin();

    int count = 0;

    while (iter_a != set_a.cend() && iter_b != set_b.cend()) {
        if (*iter_a < *iter_b) {
            iter_a++;
        } else {
            if (*iter_a == *iter_b) {
                count++;
                iter_a++;
            }
            iter_b++;
        }
    }
    return count;
}

// calculates the Jaccard index for all supplied sets which represent the source code in a document
// since Jaccard(setA,setB)==Jaccard(setB,setA) the calculation for a pair of documents only needs to be made once.
template <typename T>
std::vector<std::priority_queue<std::pair<double, int>>> jaccard(const std::vector<std::set<T>> &contents)
{
    auto start = std::chrono::high_resolution_clock::now();

    std::vector<std::priority_queue<std::pair<double, int>>> similarities(contents.size());

    // calculate the jaccard idx for each pair of document
    // note the loop indices: comparing only unique pairs
    for (int i = 0; i < contents.size() - 1; i++) {
        for (int j = i + 1; j < contents.size(); j++) {
            double inters_size = get_count_intersect(contents[i], contents[j]);

            // jaccard_idx: intersection / total
            //              -> total can be described as (A + B - intersection)
            // given we have A and B, which are the sizes of the respective sets, only the intersection needs to be calculated
            double jaccard_idx = inters_size / ( contents[i].size() + contents[j].size() - inters_size );

            // jaccard(setA, setB) == jaccard(setB,setA)
            similarities[i].emplace(jaccard_idx, j);
            similarities[j].emplace(jaccard_idx, i);
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "Calculating the Jaccard index took " << duration.count() << " ms" << std::endl;
    return similarities;
}

// Shows the most similar documents for each document
// Each document only needs to occur once in the list
// Ignore the document if the similarity score is lower than "threshold"
void showSummary(std::vector<std::priority_queue<std::pair<double, int>>>& similarities, double threshold)
{
    // holds bool values for each document to prevent doubly printed documents
    std::vector<bool> seen(similarities.size(), false);

    // keeps track of document number
    int i = 0;

    // using an output buffer to prevent printing empty lines
    // where either no similar docs were above the threshold or the document has been printed already
    std::string output_buffer;

    std::cout << std::left << std::setw(6)
        << "doc" << "Similar documents" << std::endl
        << "-----------------------" << std::endl;

    int total_reported = 0;

    for (auto& prio_q : similarities) {
        // print pairs as long as there are documents left and similarity higher than threshold
        int counter_print_newline = 1;
        while (!prio_q.empty() && prio_q.top().first >= threshold) {
            auto &pair = prio_q.top();
            if (!seen[pair.second]) {
                seen[pair.second] = true;
                output_buffer += (std::to_string(pair.second) + " (" + std::to_string(pair.first) + ") ");
                // print 6 similar docs before going to newline to keep it neatly viewable
                if (counter_print_newline % 6 == 0) {
                    output_buffer += "\n      ";
                }
                total_reported++;
                counter_print_newline++;
            }
            prio_q.pop();
        }

        // filtering empty output lines (no similar docs / similar docs already reported)
        if (!output_buffer.empty()) {
            std::cout << std::left << std::setw(6)
                << i << output_buffer << std::endl;

            output_buffer.clear();
        }

        i++;
    }
    std::cout << std::endl << "Reported similarities above threshold: " << total_reported << std::endl
    << "-----------------------" << std::endl << std::endl;
}

// finds the max value in a vector of sets
// since the sets are ordered (smaller to bigger) only the last element in each set needs to be considered
int findMax(const std::vector<std::set<int>> &sets) {
    if (sets.empty()) return -1;

    int max = *(sets[0].rbegin());

    for (int i = 1 ; i < sets.size(); i++) {
        max = std::max(max, *(sets[i].rbegin()));
    }

    return max;
}

// Currently just returns a hardcoded next prime number (hashed with goodhash on quiz dataset)
// obviously this wouldn't work well if documents were dynamic and / or different hash functions were used
// Two approaches come to mind for finding the next prime number dynamically
//      a) keep a sorted vector in memory (which has a high memory requirement) and run a modified binary sort to find the next prime number after a supplied val
//      b) try next numbers until a prime number is found; this approach has a high time complexity compared to approach a. However it is constant in memory.
int findNextPrime(int val) {
    return 2146939727;
}

// populates given vector with n unique number from [floor;ceil]
// keeping track of previously assigned number in a set. (which offers O(log(n)) searches compared to the O(N) needed in the vector
void generateCoeffs(std::vector<int>& coeffs, int n, int floor, int ceil) {
    std::set<int> seen;
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(floor,ceil);

    int found = 0;

    while (found < n) {
        int candidate = dist(rng);

        while (seen.find(candidate) != seen.cend()) {
            candidate = dist(rng);
        }

        seen.emplace(candidate);
        coeffs[found++] = candidate;
    }
}

// Minhashing algo; which calculates an approximated Jaccard for a given set of documents.
// Arguments:
//      A vector with each index representing a document of sets of unique integers representing the contents of the docs.
//      A number k, which denotes how many hash functions need to be generated and ran
//                  higher k will results in longer processing time, but more accurate results.
//
// 1. find maximum value in the supplied sets:
//      Since each set is sorted, only the last elements of each set need to be viewed to select the max element
// 2. select next prime number:
//       Currently hardcoded, as it was out of scope for this exercise.
//       Possible implementation ideas discussed above the findNextprime method.
// 3. Select coefficients for k hash functions
//       K unique integers are picked for A and K unique integers are picked for B (see generateCoeffs)
// 4. Run the K hash functions on each set, saving the lowest resulting hash value for each hash function / document pair
// 5. compare saved lowest hash functions of each document pair, the approximated jaccard is then calculated as the amount of equal lowest hash functions over the total hash functions
std::vector<std::priority_queue<std::pair<double, int>>> minhashing(const std::vector<std::set<int>> &contents, int k)
{
    auto start = std::chrono::high_resolution_clock::now();

    int maxVal = findMax(contents);

    int prime = findNextPrime(maxVal);

    auto coeffsA = std::vector<int>(k);
    auto coeffsB = std::vector<int>(k);

    generateCoeffs(coeffsA, k, 1, maxVal - 1);
    generateCoeffs(coeffsB, k, 0, maxVal - 1);

    std::vector<std::vector<int>> minhash_sigs(contents.size(), std::vector<int>(k));

    for (int docNum = 0; docNum < contents.size(); docNum++) {
        for (int funcNum = 0; funcNum < k; funcNum++) {
            int minCode = prime;

            for (const auto curr_entry : contents[docNum]) {
                int curr_code = ((coeffsA[funcNum]) * curr_entry + (coeffsB[funcNum])) % prime;
                minCode = std::min(curr_code, minCode);
            }

            minhash_sigs[docNum][funcNum] = minCode;
        }
    }

    // calculate approximated jaccard index
    std::vector<std::priority_queue<std::pair<double, int>>> similarities(contents.size());

    for (int docNum = 0; docNum < contents.size(); docNum++) {
        for (int otherDocNum = docNum + 1; otherDocNum < contents.size(); otherDocNum++) {
            double count_eq = 0;
            for (int funcNum = 0; funcNum < k; funcNum++) {
                if (minhash_sigs[docNum][funcNum] == minhash_sigs[otherDocNum][funcNum]) {
                    count_eq++;
                }
            }
            double approx_jaccard = count_eq / k;
            similarities[docNum].emplace(approx_jaccard, otherDocNum);
            similarities[otherDocNum].emplace(approx_jaccard, docNum);
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "minhashing took " << duration.count() << " ms" << std::endl;
    return similarities;
}

/**
 * Hashing & jaccard
 *
 * Implementation notes haven been written above the respective functions
 *
 * Step 1: naive jaccard on strings
 *  - Jaccard calculation takes about 900ms on my machine. String comparisons are slow.
 *
 * Optimization 1: Unique ID replacement
 *  - Replacing the strings with Unique IDS takes about 20ms
 *  - However calculating the Jaccard, with int comparisons is much faster at around 250ms
 *  - Total approximately 270ms, 3x faster than the Jaccard on strings! However a large memory overhead is needed  to keep track of ID string mapping.
 *
 * Optimization 2: Hash replacement
 *  - A hash function should result in little to no colission to ensure representative Jaccard calculations
 *  - A hash function should be fast and should generate data that can be cheaply compared
 *
 *  Results from testing:
 *      The supplied bad hashes and horner hash, while fast, generate a lot of colissions. Rendering them unusable for accurate Jaccard calculations.
 *
 *  The supplied good hash, SDBM, DJB2, and Jenkins One At A Time generate no (or very little) collisions with this dataset.
 *  This ensures an accurate Jaccard calculation, which is the same for each of these hash algos.
 *
 *  In terms of performance, each of them are very close having the same asymptotic time complexity, only differing in constants.
 *  While the Hash calculations are fast, the jaccard calculations are significantly slower than with the Unique IDs approach.
 *  On average each of them take 350ms for both hashing and calculating the Jaccard indexes. Rendering each of them a valid choice.
 *  This 350 ms is slower (1.2x) than the 270 ms needed for the Unique ID approach. However requires less memory overhead in the hashing step.
 *
 *
 *  Optimization 3 (LSH - Minhash):
 *  Performance and accuracy is highly dependant on the choice of the number of hashing functions used (k).
 *
 *  Higher k -> less variance from accurate Jaccard, slower.
 *  Lower k -> higher variance, faster.
 *
 *
 *  Choices of K performance
 *   k     time
 *  140    205ms
 *  120    170ms
 *  100    150ms
 *  80     120ms
 *  60     100ms
 *
 * K's around 60 seem to show a variance that is unacceptable for this use case (~8%).
 * Picking k=80, seems to show an average variance of (~6%), which is alright. While still being  at least twice as fast as the previous methods.
 * Picking k's above 120 seems to deliver diminishing returns, where the variance only slight lowers.
 *
 * In scenarios where a higher variance is acceptable, k should be lower, to improve performance.
 * Whenever variance is not acceptable, experimentation with higher k should be done,
 *  or previous optimizations should be evaluated instead if the performance gains become negligible.
 */
int main()
{
    // Read the source code as sets of strings
    std::vector<std::set<std::string>> contents = readDatafiles("src/quiz/");

//    // testing different methods
    std::cout << std::endl << "------ Strings ------" << std::endl;
    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesStrings = jaccard<std::string>(contents);
//
//
//    std::cout << std::endl << "------ Unique ID ------" << std::endl;
//    std::vector<std::set<int>> contentsId = replaceWithUniqueId(contents);
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesUniqueID = jaccard<int>(contentsId);
//
//
//    std::cout << std::endl <<"---- Bad hash -----" <<  std::endl;
//    std::vector<std::set<int>> contentsIdBadHash = replaceWithHash<other_bad_hash>(contents);
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesBadHash = jaccard<int>(contentsIdBadHash);
//    findCollisions<bad_hash>(contents);
//
//    std::cout << std::endl << "------ Good hash algo ------" << std::endl;
    std::vector<std::set<int>> contentsIdGoodHash = replaceWithHash<good_hash>(contents);
    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesGoodHash = jaccard<int>(contentsIdGoodHash);
//    findCollisions<good_hash>(contents);
    std::cout << std::endl << "------ SDBM hash ------" << std::endl;
//    std::vector<std::set<int>> contentsIdSDBM = replaceWithHash<sdbm>(contents);
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesSDBM = jaccard<int>(contentsIdSDBM);
//    findCollisions<sdbm>(contents);
    std::cout << std::endl << "------ DJB2 hash ------" << std::endl;
    std::vector<std::set<int>> contentsIdDJB2 = replaceWithHash<djb2>(contents);
    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesDJB2 = jaccard<int>(contentsIdDJB2);
//    findCollisions<djb2>(contents);
    std::cout << std::endl << "------ Jenkins One At A Time hash ------" << std::endl;
    std::vector<std::set<int>> contentsIdJenkins = replaceWithHash<jenkins_one_bit_at_a_time>(contents);
    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesJenkins = jaccard<int>(contentsIdJenkins);
    findCollisions<jenkins_one_bit_at_a_time>(contents);

    // minhash
//    std::cout << std::endl << "------ Minhash k140 ------" << std::endl;
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesMinHash140 = minhashing(contentsIdGoodHash, 140);
    std::cout << std::endl << "------ Minhash k120 ------" << std::endl;
    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesMinHash120 = minhashing(contentsIdGoodHash, 120);
//    std::cout << std::endl << "------ Minhash 100k ------" << std::endl;
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesMinHash100 = minhashing(contentsIdGoodHash, 100);
//    std::cout << std::endl << "------ Minhash k80 ------" << std::endl;
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesMinHash80 = minhashing(contentsIdGoodHash, 80);
//    std::cout << std::endl << "------ Minhash k60 ------" << std::endl;
//    std::vector<std::priority_queue<std::pair<double, int>>> similaritiesMinHash60 = minhashing(contentsIdGoodHash, 60);
//
//    // Show the results
//    std::cout << std::endl << "Showing Jaccard results (good hash)" << std::endl;
//    showSummary(similaritiesGoodHash, 0.75);
//    std::cout << std::endl << "Showing approx Jaccard (with minhash) results (good hash) k = 100" << std::endl;
//    showSummary(similaritiesMinHash100, 0.75);
//    std::cout << std::endl << "Showing approx Jaccard (with minhash) results (good hash) k = 80" << std::endl;
//    showSummary(similaritiesMinHash80, 0.75);

    return 0;
}
