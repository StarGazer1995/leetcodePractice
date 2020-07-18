#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;
class solution{
    protected:
    bool check(vector<vector<int>> res,vector<int> temp){
        if(res.empty()) return false;
        for(int i = 0; i<res.size();i++){
            if(res[i]==temp) return true;
        }
        return false;
    }
    void backtrack(vector<vector<int>> &res,vector<int> &temp,vector<int> &candidates,int &target,int pos){
        if(std::accumulate(temp.begin(),temp.end(),0)>target) return;
        if(std::accumulate(temp.begin(),temp.end(),0)==target){
            if(check(res,temp)) return;
            res.push_back(temp);
        }else{
            for(int i = pos;i<candidates.size();i++){
                temp.push_back(candidates[i]);
                backtrack(res,temp,candidates,target,i+1);
                temp.pop_back();
            }
        }
    }
    public:
    vector<vector<int>> combinationSum2(vector<int> candidates,int target){
        vector<vector<int>> res;
        vector<int> temp;
        std::sort(candidates.begin(),candidates.end());
        backtrack(res,temp,candidates,target,0);
        return res;
    }
};