#include<iostream>
  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

  class Solution{
      public:
      ListNode* addTwoNumbers(ListNode* l1,ListNode* l2){

        ListNode* tmpRoot = new ListNode(0); 
        ListNode* ansRoot = tmpRoot;
        
        bool first = true;
        int carry = 0;
        while(l1 != nullptr || l2 != nullptr)
        {
            if(l1 == nullptr) l1 = new ListNode(0);
            if(l2 == nullptr) l2 = new ListNode(0);
            int value = l1->val + l2->val + carry;

            carry = 0;
            if(value > 9)
            {
                value -= 10;
                carry = 1;
            }

            if(first)
            {
                tmpRoot->val = value;
                first = false;
            }
                
            else
            {
                tmpRoot -> next = new ListNode(value);
                tmpRoot = tmpRoot -> next;
            }
            l1 = l1->next;
            l2 = l2 -> next;
        }
            
        if(carry != 0)
        {
            tmpRoot -> next = new ListNode(1);
            tmpRoot = tmpRoot -> next;
        }
        return ansRoot;
        }
  };

  int main(){
      ListNode p1(0);
      ListNode p2(9);
      ListNode *p = Solution().addTwoNumbers(&p1,&p2);
      while(p!=nullptr){
          std::cout<<p->val;
      }
      return 0;
  }