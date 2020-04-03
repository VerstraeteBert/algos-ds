#include "Deksel.cpp"
#include "Pot.cpp"
#include "matcher.cpp"
#include <vector>
#include <iomanip>
#include <random>
#include <iostream>

void vulVectoren(const std::vector<int>& diameters, std::vector<Deksel>& deksels, std::vector<Pot>& potjes){
    for(const int& x : diameters){
        deksels.emplace_back(x);
        potjes.emplace_back(x);
    }
    
    std::mt19937 eng{std::random_device{}()};    
    std::shuffle(deksels.begin(),deksels.end(),eng);

    //reseed
    std::mt19937 eng2{std::random_device{}()};    
    std::shuffle(potjes.begin(),potjes.end(),eng2);
}

void fill_random(vector<int>& vec, int max) {
    std::random_device rd;
    std::mt19937 eng{rd()};
    assert(max < std::numeric_limits<int>::max());
    std::uniform_int_distribution<int> dist{0, static_cast<int>(max)};

    std::generate(vec.begin(), vec.end(), [&dist, &rd]() { return dist(rd); });
}

bool assert_correct_pairing(const vector<pair<Deksel,Pot>>& v_pairs) {
    for (auto& pair : v_pairs) {
        if (pair.first.getDiameter() != pair.second.getDiameter()) {
            cout << "FOUT:" << pair.first.getDiameter() << " : " << pair.second.getDiameter() << endl;
            return false;
        }
    }
    return true;
}

/**
 * Notes about implementation in matcher.cpp
 */
int main(){
    std::vector<int> diameters {1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 10};
    std::vector<Deksel> deksels;
    std::vector<Pot> potjes;
    vulVectoren(diameters, deksels, potjes);
    vector<pair<Deksel, Pot>> v_pairs = Matcher::match(deksels, potjes);

    cout << "---- Initial State ----" << endl;
    for (int i = 0; i < deksels.size(); i++) {
        cout << "Deksel " << deksels[i].getUUID() << " with value: " << deksels[i].getDiameter()
             << " ; Pot" << potjes[i].getUUID() << " with value: " <<  potjes[i].getDiameter()
             << endl;
    }

    assert_correct_pairing(v_pairs);

    cout << endl << "----Matched pairs----" << endl;
    for (auto& pair : v_pairs) {
        cout << "Deksel " << pair.first.getUUID() << " with value: " << pair.first.getDiameter()
             << " matched with Pot " << pair.second.getUUID() << " with value: " <<  pair.second.getDiameter()
             << endl;
    }

    // test large vector with high variance
    diameters.clear();
    diameters.resize(1'000'000);
    fill_random(diameters, 1'000'000);
    deksels.clear();
    potjes.clear();
    vulVectoren(diameters, deksels, potjes);
    assert(assert_correct_pairing(v_pairs));

    // test vector with 3 elements
    diameters.clear();
    diameters.resize(3);
    fill_random(diameters, 3);
    deksels.clear();
    potjes.clear();
    vulVectoren(diameters, deksels, potjes);
    v_pairs = Matcher::match(deksels, potjes);
    assert(assert_correct_pairing(v_pairs));

    // test empty vector
    diameters.clear();
    diameters.resize(0);
    fill_random(diameters, 0);
    deksels.clear();
    potjes.clear();
    vulVectoren(diameters, deksels, potjes);
    v_pairs = Matcher::match(deksels, potjes);
    assert(assert_correct_pairing(v_pairs));

    // test vector with all elements of same key
    diameters.clear();
    diameters.resize(10);
    fill(diameters.begin(), diameters.end(), 1);
    deksels.clear();
    potjes.clear();
    vulVectoren(diameters, deksels, potjes);
    v_pairs = Matcher::match(deksels, potjes);
    assert(assert_correct_pairing(v_pairs));

    std::cout << endl << "OK" << std::endl;
    return 0;
}
