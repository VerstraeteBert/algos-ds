//testprogramma voor het social distance algoritme

#include "lijst.h"
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

Lijst<int> maakLijst(const vector<int>& v){
    Lijst<int> l;
    for(auto sleutel: v){
        l.voegToe(sleutel);
    }
    return l;
}

/**
 * Notes on the implementation can be found at function declaration of applySocialDistancing
 *      and other helper functions
 */
int main()
{
    {
        //We testen met lijsten van int sleutelwaarden
        vector<pair<vector<int>, vector<int>>> testvectoren;
        //bemerk dat volgorden in omgekeerde volgorde zijn gespecifeerd, omdat voegToe steeds aan het begin van de lijst toevoegt
        vector<int> v1 = {1,5,6,3,8,5,6,9,6,7,4,5,1,2};
        vector<int> v1_sol = {1,0,5,6,3,0,0,8,5,0,0,0,6,9,0,0,6,7,4,5,0,1,2};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v1, v1_sol));
        vector<int> v2 = {7,5,3,2,7,4,5,1,5,6,7,9,1};
        vector<int> v2_sol = {7,0,5,3,2,0,0,7,4,5,0,1,0,5,0,6,7,9,0,1};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v2, v2_sol));
		vector<int> v3 = {20,1,1,1,1,1,1,6,6,6,6,6,6,6,10};
        vector<int> v3_sol = {20,0,1,1,1,1,1,1,0,6,6,6,6,6,6,6,0,10};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v3, v3_sol));
		vector<int> v4 = {1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,5,1,2,3};
        vector<int> v4_sol = {1,2,3,0,4,5,6,7,0,1,2,0,3,4,5,6,0,1,0,2,3,4,5,0,0,1,2,3};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v4, v4_sol));
		vector<int> v5 = {3,2,1,4,3,2,1,5,4,3,2,1,6,5,4,3,2,1};
        vector<int> v5_sol = {3,2,1,4,3,2,1,0,5,0,4,3,2,1,0,6,5,0,4,3,2,1};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v5, v5_sol));
        vector<int> v6 = {1,5,9,13,13,12,8,5,1};
        vector<int> v6_sol = {1,0,5,0,9,0,13,13,12,0,8,5,0,1};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v6, v6_sol));
        // empty vector
        vector<int> v7 = {};
        vector<int> v7_sol = {};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v7, v7_sol));
        // all same elements
        vector<int> v8 = {1,1,1,1,1};
        vector<int> v8_sol = {1,1,1,1,1};
        testvectoren.emplace_back(pair<vector<int>, vector<int>>(v8, v8_sol));
        
        
        int socialDistance = 3;
        int isolationKey = 0;

        for(auto& v: testvectoren){
            //eerste element in vector wordt laatste element van gelinkte lijst
            auto l = maakLijst(v.first);
            auto l_sol = maakLijst(v.second);
            cerr << "Testen van de vector: " << endl;
            l.schrijf(cerr);
            cerr << endl;
            l.applySocialDistancing(socialDistance, isolationKey);
            cerr << "Na toepassen van social distancing: " << endl;
            l.schrijf(cerr);
            if (l != l_sol) {
                cout << "-------- FOUT! --------" << endl;
            }
            cerr << endl;
        }	
		
    }

    cout << "OK\n";

    return 0;
}
