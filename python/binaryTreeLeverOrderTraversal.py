class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def binaryTreeLeverOrderTraversal(self,root:TreeNode):
        queue,order = [],[]
        stk = []
        queue.append(root)
        count =1
        while queue:
            temp = []
            while count>0:
                v = queue.pop(0)
                stk.append(v)
                temp.append(v.val)
                count-=1
            order.append(temp)
            while(len(stk)):
                v=stk.pop()
                if v.right is not None:
                    queue.append(v.right)
                    count+=1
                if v.left is not None:
                    queue.append(v.left)
                    count+=1

        return order

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
print(solution().binaryTreeLeverOrderTraversal(root))