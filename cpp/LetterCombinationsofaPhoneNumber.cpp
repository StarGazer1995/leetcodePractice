#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

class solution{
    public:
    vector<string> combination(vector<string> vecIn,vector<string> mapIn){
        if(vecIn.size()!=0){
            vector<string> res;
            for(string i:vecIn){
                for(string j:mapIn){
                    res.push_back(i+j);
                }
            }
            return res;
        }else{
            for(string i:mapIn)
                vecIn.push_back(i);
        }
        return vecIn;
    }
    vector<string> LetterCombinationsofaPhoneNumber(string s){
        map<char, vector<string> > dic = {
                    {'2', {"a", "b", "c"}},
                    {'3', {"d", "e", "f"}},
                    {'4', {"g", "h", "i"}},
                    {'5', {"j", "k", "l"}},
                    {'6', {"m", "n", "o"}},
                    {'7', {"p", "q", "r", "s"}},
                    {'8', {"t", "u", "v"}},
                    {'9', {"w", "x", "y", "z"}}
                    };
        vector<string> res;
        for(char i:s){
            res = combination(res,dic[i]);
        }
        return res;
    }
};
int main(){
    string s = "23";
    vector<string> res=solution().LetterCombinationsofaPhoneNumber(s);
    for(auto i:res){
        cout<<i<<endl;
    }
}