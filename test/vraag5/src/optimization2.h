#ifndef BINTREE_H
#define BINTREE_H

#include <memory>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include "./containers.h"

class Node;

class BinaryTree : public std::unique_ptr<Node>
{
public:
    using std::unique_ptr<Node>::unique_ptr;
    using std::unique_ptr<Node>::operator=;

    friend std::ostream &operator<<(std::ostream &os, const BinaryTree &tree);

    bool build(std::vector<std::string>& questions, std::list<std::string> &animals, std::vector<std::map<std::string, bool>>& answers, int level = 0);
    [[nodiscard]] int height() const;
    [[nodiscard]] double averageDepth() const;
    [[nodiscard]] int numberOfLeaves() const;
    [[nodiscard]] int numberOfSplits() const;
private:
    void print_preorder(int level = 0, bool is_pos = false) const;
    void GetTotalLeafNodesAndDepth(int& totalLeafHeight, int& totalLeafNodes, int level) const;
    [[nodiscard]] bool isLeafNode() const;
    [[nodiscard]] int calculateQuestionSubsSizeDiff(const std::list<std::string>& animals, const std::vector<std::map<std::string, bool>> &answers, int i) const;
};

class Node {
public:
    std::string value;
    BinaryTree left, right;

    explicit Node(std::string& val) : value(val) {};
};

// simplified info gain calculation
int BinaryTree::calculateQuestionSubsSizeDiff(const std::list<std::string>& animals, const std::vector<std::map<std::string, bool>> &answers, int i) const {
    int num_pos = 0;
    int num_neg = 0;

    for (auto& animal : animals) {
        answers[i].at(animal) ? num_pos++ : num_neg++;
    }

    return std::max(num_pos, num_neg) - std::min(num_pos, num_neg);
}

bool BinaryTree::build(std::vector<std::string>& questions, std::list<std::string> &animals, std::vector<std::map<std::string, bool>> &answers, int level)
{
    if (animals.empty()) {
        return true;
    }

    if (animals.size() == 1) {
        *this = std::make_unique<Node>(animals.front());
        return true;
    }

    // conflicts!
    if (level == questions.size()) {
        std::cout << "Can not distinguish between " << animals << std::endl;
        return false;
    }

    // Optimization 2
    // greedy information gain calculation
    //      -> information gain can be seen as the difference in size of the binary subsets
    //      -> if the difference is 0, e.g. (4 yes 4 no) it is optimal
    //      ->  larger differences are less optimal e.g. (6y, 2n) -> 4 vs (5y, 3n) -> 2
    //
    // If question is the last possible questions, it is optimal.
    if (level != questions.size() - 1) {
        int optimal_idx = level;
        int optimal_subset_diff = calculateQuestionSubsSizeDiff(animals, answers, level);

        for (int i = level + 1; i < questions.size(); i++) {
            // if subset diff is 0 e.g (4 yes, 4 no) no further processing is needed
            if (optimal_subset_diff == 0) {
                break;
            }

            int curr_q_subset_diff = calculateQuestionSubsSizeDiff(animals, answers, i);
            if (curr_q_subset_diff < optimal_subset_diff) {
                optimal_idx = i;
                optimal_subset_diff = curr_q_subset_diff;
            }
        }

        // Optimization 1 has now become redundant, the situation alleviated with that optimization will now only occur
        // if all remaining questions do no splitting, thus, when this occurs we can return early as there will be conflicts.
        if (optimal_subset_diff == animals.size()) {
            std::cout << "Can not distinguish between " << animals << std::endl;
            return false;
        }

        // swap questions and their respective answers, if optimal q is not the original q
        if (optimal_idx != level) {
            std::swap(questions[optimal_idx], questions[level]);
            std::swap(answers[optimal_idx], answers[level]);
        }
    }
    // End of optimization 2

    *this = std::make_unique<Node>(questions[level]);

    std::list<std::string> animalsPos;
    auto animals_itr = animals.begin();
    while (animals_itr != animals.end()) {
        if (answers[level][*animals_itr]) {
            animalsPos.emplace_back(std::move(*animals_itr));
            // erase returns iterator on position AFTER removed item in list (could be end)
            animals_itr = animals.erase(animals_itr);
        } else {
            animals_itr++;
        }
    }
    // animalsPos contains all animals that tested positive for the current question
    // animals now contains all animals that tested negative for the current question


    // This version shows all collisions
    // The return commented underneath shows short circuits on the first collisions
    if (!(*this)->left.build(questions, animalsPos, answers, level + 1)) {
        (*this)->right.build(questions, animals, answers, level + 1);
        return false;
    } else {
        return (*this)->right.build(questions, animals, answers, level + 1);
    }

    // short circuit if left subtree contains collisions
    // return (*this)->left.build(questions, animalsPos, answers, level + 1) && (*this)->right.build(questions, animals, answers, level + 1);
}

bool BinaryTree::isLeafNode()  const {
    return (*this)->left == nullptr && (*this)->right == nullptr;
}

// Cfr. UFora, example was wrong, it counted the number of nodes, not edges to the leaf.
//  Simple adaptation -> base case -1 instead of 0 to count number of edges.
int BinaryTree::height() const {
    if (*this == nullptr) return -1;
    return std::max((*this)->left.height(), (*this)->right.height()) + 1;
}

void BinaryTree::GetTotalLeafNodesAndDepth(int& totalLeafHeight, int& totalLeafNodes, int level) const {
    if (*this == nullptr) return;

    if (isLeafNode()) {
        totalLeafNodes++;
        totalLeafHeight += level;
        return;
    }

    (*this)->left.GetTotalLeafNodesAndDepth(totalLeafHeight, totalLeafNodes, level + 1);
    (*this)->right.GetTotalLeafNodesAndDepth(totalLeafHeight, totalLeafNodes, level + 1);
}

// Both a function to get depth of leaf nodes and height of leaf nodes exist
// However running them both would be O(2N), while combining requires only O(N)
double BinaryTree::averageDepth() const {
    int totalLeafHeight = 0;
    int totalLeafNodes = 0;

    GetTotalLeafNodesAndDepth(totalLeafHeight, totalLeafNodes, 0);

    return (double) totalLeafHeight / totalLeafNodes;
}

// leaf -> node without children
int BinaryTree::numberOfLeaves() const {
    if (*this == nullptr) return 0;

    if (this->isLeafNode()) {
        // leaf node
        return 1;
    } else {
        // internal node
        return (*this)->left.numberOfLeaves() + (*this)->right.numberOfLeaves();
    }
}

// numbers of splits == number of internal nodes
// internal node -> not a leaf node
int BinaryTree::numberOfSplits() const {
    if (*this == nullptr) return 0;

    if (this->isLeafNode()) {
        // leaf node
        return 0;
    } else {
        // internal node
        return (*this)->left.numberOfSplits() + (*this)->right.numberOfSplits() + 1;
    }
}

void BinaryTree::print_preorder(int level, bool is_pos) const {
    if (*this == nullptr) return;

    // level - 1 to ensure root level answers have no indentation
    for (int i = 0; i < level - 1; i++) {
        std::cout << "\t";
    }

    if (level == 0) {
        std::cout << (*this)->value << std::endl;
    } else {
        std::cout << (is_pos ? "--Y-->" : "--N-->") << " " << (*this)->value << std::endl;
    }

    (*this)->left.print_preorder(level + 1,true);
    (*this)->right.print_preorder(level + 1, false);
}

std::ostream &operator<<(std::ostream &os, const BinaryTree &tree) {
    tree.print_preorder();
    return os;
}

#endif
