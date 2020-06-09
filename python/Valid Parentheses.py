class solution:
    def validParentheses(self,s):
        if(len(s)==1):
            return False
        dic = {']':'[', '}':'{', ')':'('}
        stk = []
        for i in s:
            if( i=='['or i=='{' or i=='('):
                stk.append(i)
            else:
                if(dic[i]==stk[-1]):
                    stk.pop()
                else:
                    return False
        return True


s = "["
print(solution().validParentheses(s))