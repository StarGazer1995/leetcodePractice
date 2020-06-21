#include<string>
#include<iostream>
#include<map>
using namespace std;
class Solution{
    public:
    int lengthOfLongestSubstring(string s) {
        int size_temp=0;
        std::map<char,int> temp;
        int j=0;
        for(int i=0;i<s.length();i++){
            if(temp.count(s[i]) || 0){
                j=std::max(temp[s[i]],j);
            }
            size_temp=std::max(size_temp,i-j+1);
            temp[s[i]]=i+1;
        }
        return size_temp;
    }
};

int main(){
    string s = "abcabcbb";
    cout<<Solution().lengthOfLongestSubstring(s)<<endl;
    return 0;
}