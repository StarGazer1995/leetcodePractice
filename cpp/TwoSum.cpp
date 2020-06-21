#include<iostream>
#include<map>
#include<vector>
using namespace std;

class Solution{
    public:
    vector<int> twoSum(vector<int> &nums,int target){
        map<int,int> sum;
        for(int i=0;i<nums.size();i++){
            int res = target - nums[i];
            if(!sum.count(res)){
                sum[nums[i]] = i;
            }else{
                return vector<int>(sum[res],i);
            }
        }
        return vector<int>(0,0);

    }
};

int main(){
    std::vector<int> nums = {2,7,11,8};
    int target = 9;
    std::vector<int> res = Solution().twoSum(nums,target);
    for(int i=0;i<res.size();i++){
        cout<<res[i]<<endl;
    }
    return 0;
}