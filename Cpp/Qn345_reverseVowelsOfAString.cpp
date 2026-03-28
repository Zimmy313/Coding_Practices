#include <string>
#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    bool isVal(char c){
        c = tolower(c);
        string v = "aeiou";
        return v.find(c) != string::npos;
    }

    string reverseVowels(string s){
        vector<int> v;
        for(int i = 0; i < s.size(); ++i){
            char c = s[i];

            if(isVal(c)){
                v.push_back(i);
            }
        }

        string result = s;
        for(int i = 0; i < s.size(); ++i){
            char c = s[i];

            if(isVal(c)){
                int index_swap = v.back();
                v.pop_back();

                result[i] = s[index_swap];
            }
        }
        return result;
    }
};


int main(){
    string s;

    cout << "input s: \n";
    cin >> s;

    Solution solver;

    cout << solver.reverseVowels(s) << "\n";

    return 0;
}