class solution:

    def dfs(self, arr1, arr2, m):
        self.ans
        if m==0:
            return self.ans
        arr3 = arr1
        arr4 = arr2
        for i in range(len(arr1),0):
            res = arr3[i]
            arr3 = arr3 - arr4[i]
            self.ans = max(self.ans + res, self.ans)
            ans = self.dfs(arr3.pop(1),arr4.pop(1),m-1)
            self.ans = max(self.ans,ans)
        return self.ans

n = int(input().strip())

m = int(input().strip())

arr1 = list(map(int,input().split()))

arr2 = list(map(int, input().split()))

print(solution().dfs(arr1,arr2,m))
