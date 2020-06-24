#include<vector>
#include<iostream>

using namespace std;
class Solution{
    public:
    int maxArea(vector<int>& height){
        int Maxarea = 0;
        int start = 0, end = height.size()-1;
        while(start<end){
            Maxarea = std::max(Maxarea,std::min(height[start],height[end])*(end-start));
            if(height[start]<height[end]) start++;
            else end--;
        }
        return Maxarea;
    }
};

int main(){
    vector<int> height={1,8,6,2,5,4,8,3,7};
    int max = Solution().maxArea(height);
    cout<<max<<endl;
    return 0;
}