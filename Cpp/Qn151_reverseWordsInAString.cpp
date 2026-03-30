#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        string temp = "", final = "";
        vector<string> result;

        for(int i = 0; i < n; ++i){
            char c = s[i];
            
            if(c != ' '){ // '' is for char and "" is for string
                temp.push_back(c); // or use temp += c;
            }else{
                if(temp != ""){ //ensure not pushing in empty word
                    result.push_back(temp);
                    temp.clear();
                }
            }
        }

        if(temp != ""){result.push_back(temp);}

        int m = result.size();
        for(int j = m-1; j >= 0; --j){
            final += result[j];
            
            if(j != 0){
                final += " ";
            }
        }
        return final;

    }
};


int main(){
    string s;
    cout << "Please input the string: \n";
    getline(cin, s);

    Solution solver;
    cout << solver.reverseWords(s) << endl;

    return 0;

}