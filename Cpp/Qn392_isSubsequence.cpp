#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.size();
        int m = t.size();
        int i = 0, j = 0;

        while(i < n && j < m){
            if(s[i] == t[j]){
                i++;
            }
            j++;
        }
        return i == n;
    }
};

int main(){
    string s, t;
    cout << "Please input string s: \n";
    cin >> s;

    cout << "Please input string t: \n";
    cin >> t;

    Solution sol; // same as Solution sol = Solution();

    bool result = sol.isSubsequence(s,t);

    cout << boolalpha << result << "\n";

    return 0; 
}