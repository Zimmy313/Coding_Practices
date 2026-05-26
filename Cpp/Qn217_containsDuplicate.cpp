#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution{
public:
    bool hasDuplicate(vector<int>& nums){
        unordered_set<int> map;

        for(int x : nums){

            if(map.find(x) != map.end()){ // if not end, then it is duplicate, return true
                return true;
            }
            map.insert(x);
        }
        // no duplicate found
        return false;

    }
};

int main(){
    vector<int> nums;
    int n, x;
    Solution solver;
    bool result;

    cout << "How many numbers?\n";
    cin >> n;

    cout << "Input numbers:\n";
    for(int i = 0; i < n; ++i){
        cin >> x;
        nums.push_back(x);
    }

    result = solver.hasDuplicate(nums);

    cout << boolalpha;
    cout << "The result is: "<<result << "\n";

    return 0;
}