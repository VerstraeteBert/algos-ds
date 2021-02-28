//#include "binarytree.h"
//#include "optimization1.h"
#include "optimization2.h"

#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>

void readQuestions(const char *filename, std::vector<std::string> &questions, std::list<std::string> &animals, std::vector<std::map<std::string, bool>> &answers)
{
    int nAnimals, nQuestions;

    std::ifstream in(filename);
    if (in)
    {
        in >> nAnimals;
        in >> nQuestions;

        std::string temp;
        std::getline(in, temp);

        questions.resize(nQuestions);
        for (int i = 0; i < nQuestions; i++)
        {
            std::getline(in, questions[i]);
        }

        answers.resize(nQuestions);

        std::string animal;
        for (int i = 0; i < nAnimals; i++)
        {
            in >> animal;

            animals.push_front(animal);

            for (int j = 0; j < nQuestions; j++)
            {
                in >> temp;
                answers[j][animal] = temp == "y";
            }
        }
    }
    else
    {
        std::cout << "Could not open file" << std::endl;
    }
}

int main()
{
    std::vector<std::string> questions;
    std::list<std::string> animals;
    std::vector<std::map<std::string, bool>> answers;
    readQuestions("../fixtures/animals_large.txt", questions, animals, answers);

    // Questions is a vector of strings
    std::cout << "Loaded " << questions.size() << " questions" << std::endl;
    for (auto& question : questions){
        std::cout << question <<std::endl;
    }

    // Animals is a list of strings
    std::cout << "Loaded " << animals.size() << " animals" << std::endl;
    for (auto& animal : animals){
        std::cout << animal <<std::endl;
    }

    // answers is a vector with for each question a map, mapping animal (string) to answer (bool).
    BinaryTree tree;
    bool success = tree.build(questions, animals, answers);

    std::cout << (success ? "Successfully built tree" : "Not enough information to build a tree") << std::endl;

    if (success) {
        std::cout << std::endl << tree << std::endl;
        std::cout << "The height of the tree is: " << tree.height() << std::endl;
        std::cout << "The tree has " << tree.numberOfLeaves() << " leaves" << std::endl;
        std::cout << "The average depth of a leaf is " << tree.averageDepth() << std::endl;
        std::cout << "The tree has " << tree.numberOfSplits() << " splits" << std::endl;
    }

    return 0;
}
