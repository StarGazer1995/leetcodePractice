#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution{
    protected:
    void backtrack(vector<vector<int>> &res,vector<int> &temp, vector<int> &nums){
        if(temp.size()==nums.size()){
            res.push_back(temp);
        }else{
            for(int i = 0;i<nums.size();i++){
                if(std::find(temp.begin(),temp.end(),nums[i])!=temp.end())
                    continue;
                else{
                    temp.push_back(nums[i]);
                    backtrack(res,temp,nums);
                    temp.pop_back();
                }
            }
        }
    }
    public:
    vector<vector<int>> permute(vector<int>& nums){
        vector<vector<int>> res;
        vector<int> temp;
        backtrack(res,temp,nums);
        return res;
    }
};