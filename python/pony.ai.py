class solution:
    def sticky(self,data,H,W):
        sticker1 = data.copy()
        sticker1[0] = [0] + [1] * (W-2) + [0]
        for i in range(1,H):
            for j in range(W):
                if(sticker1[i][j]==1):
                    sticker1[i-1][j] = 1

        sticker2 = []
        for i in range(H):
            sticker2.append([])
            for j in range(W):
                if(data[i][j]==sticker1[i][j]):
                    sticker2[i].append(1)
                else:
                    sticker2[i].append(0)
        return [sticker1,sticker2]

import sys
data = sys.stdin.readline().strip()
data = list(map(int,data.split(" ")))
H,W = data[0],data[1]
data = []
for i in range(H,0,-1):
    temp = sys.stdin.readline().strip()
    data.append(list(map(int,temp.split(" "))))
ans = solution().sticky(data,H,W)
print(ans[0])
print(ans[1])