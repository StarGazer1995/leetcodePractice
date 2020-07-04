#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution{
    protected:
    bool check(vector<vector<int>> &res,vector<int> temp){
        std::sort(temp.begin(),temp.end());
        bool flag = false;
        if(res.size()==0){
            return false;
        }
        for(int i=0;i<res.size();i++){
            if(res[i]==temp) flag = true;
        }
        return flag;
    }
    void backtrack(vector<vector<int>> &res, vector<int> &temp, vector<int> &candidates, int target){
        if(std::accumulate(temp.begin(),temp.end(),0)>target) return;
        if(std::accumulate(temp.begin(),temp.end(),0)==target){
            if(check(res,temp)) return;
            res.push_back(temp);
        }else{
            for(int i=0;i<candidates.size();i++){
                temp.push_back(candidates[i]);
                backtrack(res,temp,candidates,target);
                temp.pop_back();
            }
        }
    }
    public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target){
        vector<vector<int>> res;
        vector<int> temp;
        backtrack(res,temp,candidates,target);
        return res;
    }
};