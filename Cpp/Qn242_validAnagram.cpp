#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution{
public:
    // note that this can be solved using sorting but it is slower.
    // time complexity O(n), space complexity O(1) since there are at most 26 characters.
    bool isAnagram(string s, string t){
        unordered_map<char,int> map_s, map_t;
        int n = s.size(), m = t.size();
        char s1, t1;

        if(n != m){return false;}

        for(int i = 0 ; i <  n; ++i){
            s1 = s[i]; t1 = t[i];
            map_s[s1]++; map_t[t1]++;
        }

        if(map_s == map_t){
            return true;
        }

        return false;
    }
};

int main(){
    string s, t;
    Solution solver;
    bool result;
    
    cout << "Please input string s:\n";
    cin >> s;

    cout << "Please input string t:\n";
    cin >> t;

    result = solver.isAnagram(s,t);

    cout << boolalpha;
    cout << result << "\n";

    return 0;

}