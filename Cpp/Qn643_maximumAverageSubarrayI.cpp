#include <vector>
#include <iostream>
using namespace std;

class Solution{
public:
    double findMaxAverage(vector<int>& nums, int k){
        int n = nums.size(), acc=0;
        double result = -1e18, temp; // make it small

        for(int left = 0; left <= n-k; ++left){
            if(left == 0){
                for(int i = 0; i < k; ++i){
                    acc += nums[i];
                }
                temp = (double)acc/k;
            }
            else{
                acc += nums[left + k - 1];
                temp = (double)acc/k;
            }

            acc -= nums[left];
            if(temp > result){
                result = temp;
            }
        }
        return result;
    }

    double findMaxAverage_slow(vector<int>& nums, int k){
        int n = nums.size();
        double result = -1e18; // make it small

        for(int left = 0; left <= n-k; ++left){
            double temp = 0;

            for(int i = 0; i < k;++i){
                temp+=nums[left+i];
            }
            temp/=k;
            
            if(result < temp){
                result = temp;
            }
        }
        return result;
    }
};

int main(){
    std::vector<int> nums;
    int n,k,x;
    double result;

    cout << "How many numbers\n";
    cin >> n;

    // cout << "Please input the nums one by one: \n";
    // for(int i = 0; i < n; ++i){
    //     cin >> x;
    //     nums.push_back(x);
    // }

    cout << "Input numbers: \n";
    for (int i = 0; i < n; ++i){
        cin >> x;
        nums.push_back(x);
    }

    cout << "what's k? \n";
    cin >> k;

    Solution solver;
    result = solver.findMaxAverage(nums, k);

    cout << result << "\n";

    return 0;

}
