#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
public:
    void backtrack(vector<vector<int>> &res, vector<int> &temp,vector<int> nums,int k,int pos){
        if(temp.size()==k){
            res.push_back(temp);
            return;
        }else{
            for(int i = pos;i<nums.size();i++){
                temp.push_back(nums[i]);
                backtrack(res,temp,nums,k,i+1);
                temp.pop_back();
            }
            return;
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        if(k>n) return res;
        vector<int> nums;
        for(int i=1;i<=n;i++){
            nums.push_back(i);
        }
        vector<int> temp;
    }
};