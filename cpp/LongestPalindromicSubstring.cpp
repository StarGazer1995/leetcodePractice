// TODO: needs to be debuged 

#include<iostream>
#include<string>
using namespace std;
class Solution{
    public:

    string PalindromicCheck(string &s, int i, int j){
        while(i>0&&j<s.length()&&s[i]==s[j]){
            i--;
            j++;
        }
        return s.substr(i+1,j-i-2);
    }
    string LongestPalindromicSubstring(string s){
        string res = "";
        int len = s.length();
        for(int i =0;i<len;i++){
            string tmp = PalindromicCheck(s,i,i);
            if(tmp.length()>res.length()) res = tmp;
            tmp = PalindromicCheck(s,i,i+1);
            if(tmp.length()>res.length()) res = tmp;
        }
        return res;
    }
};

int main(){
    string s = "cbbd";
    cout<<Solution().LongestPalindromicSubstring(s)<<endl;
    return 0;
}