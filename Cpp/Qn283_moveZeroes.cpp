#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0, right = 0, n = nums.size();

        while(left != n){
            right = left; 

            if(nums[left] == 0){

                while(++right < n && nums[right] == 0);
                
                if(right < n){
                    int temp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = temp;
                }
            }
            left++;
        }
    }
    void moveZeroes_fast(vector<int>& nums){
        int left = 0;

        for(int right=0; right<nums.size(); right++){
            if(nums[right] != 0){
                swap(nums[left], nums[right]);
                left++;
            }
        }
    }
};

int main(){
    std::vector<int> nums;
    int n, x;
    cout << "How many numbers?: \n";
    cin >> n;

    cout << "Please input the numbers one by one: \n";
    for(int i = 0; i < n; ++i){
        cin >> x;
        nums.push_back(x);
    }

    Solution solver;
    solver.moveZeroes(nums);

    cout << "Result:";
    for(int num : nums){
        cout << num << " ";
    }
    cout << endl;

    return 0;

}