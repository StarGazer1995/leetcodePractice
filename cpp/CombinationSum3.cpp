#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
class Solution{
    public:
    void backtrack(vector<vector<int>> &res,vector<int> &temp,vector<int> &nums, int n, int k,int pos){
        if(n==0){
            if(temp.size()==k) res.push_back(temp);
            return;
        }else if(n<0) return;
        else{
            for(int i= pos;i<nums.size();i++){
                temp.push_back(nums[i]);
                backtrack(res,temp,nums,n-nums[i],k,i+1);
                temp.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {  
        vector<int> nums {1,2,3,4,5,6,7,8,9};
        vector<vector<int>> res;
        if(n>45) return res;
        vector<int> temp;
        backtrack(res,temp,nums,n,k,0);
        return res;
    }
};