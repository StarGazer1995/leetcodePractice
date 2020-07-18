#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution{
    public:
    void backtrack(vector<vector<int>> &res, vector<int> &temp,vector<int> &nums, int pos){
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }else{
            for(int i = pos;i<nums.size();i++){
                temp.push_back(nums[i]);
                backtrack(res,temp,nums,i+1);
                temp.pop_back();
            }
            return;
        }
    }
    vector<vector<int>> permuteUnique(vector<int> &nums){
        vector<vector<int>> res;
        vector<int> temp;
        int pos = 0;
        backtrack(res,temp,nums,pos);
        return res;
    }
};
