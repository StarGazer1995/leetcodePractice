#include<iostream>

using namespace std;
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode *pHead = head;
        while(pHead!=nullptr){
            count++;
            pHead=pHead->next;
        }
        if(count<n) return nullptr;
        if(count==n) return head->next;
        pHead = head;
        int pos = count-n;
        count = 0;
        while(count<pos-1){
            pHead = pHead->next;
            count++;
        }
        pHead->next = pHead->next->next;
        return head;
    }
};