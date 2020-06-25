//TODO: unsolved
#include<vector>
#include<iostream>
#include<numeric>
#include<algorithm>

using namespace std;
class solution{
    public:
    bool check(vector<vector<int> > &res,vector<int> temp){
        bool flag=false;
        for(int i = 0;i<res.size(); i++){
            if(res[i]==temp) flag=true;
        }
        return false;
    }
    void helper(vector<int> &nums,vector<int> temp,vector<vector<int> > &res,int pos){
        if(temp.size()==3){ 
            if(accumulate(temp.begin(),temp.end(),0)==0){
                if(!check(res,temp))
                    res.push_back(temp);
                return;
            }else{
                return;
            }
        }
        if(pos>temp.size()-1) return; 
        temp.push_back(nums[pos]);  
        helper(nums,temp,res,pos+1);
    }
    vector<vector<int> > Threesum(vector<int> &nums){
        std::sort(nums.begin(),nums.end());
        vector<vector<int> > res;
        vector<int> temp;
        int pos = 0;
        for(;pos<nums.size();pos++){
            helper(nums,temp,res,pos);
        }
        return res;
    }
};

int main(){
    std::vector<int> nums {-1, 0, 1, 2, -1, -4};
    vector<vector<int> > res = solution().Threesum(nums);
    for(int i = 0; i<res.size();i++){
        for(int j = 0;j<res[i].size();j++){
            cout<<res[i][j]<< " ";
        }
        cout<<" "<<endl;
    }
    return 0;
}