class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class solution:
    def dfs(self,root:TreeNode,count):
        if not root:
            return count
        temp = count + 1
        count_r = self.dfs(root.right,temp)
        count_l = self.dfs(root.left,temp)
        return max(count_l,count_r)
    def maximumDepthofBinaryTree(self,root:TreeNode):
        ans = self.dfs(root,0)
        return ans

node_1 = TreeNode
node_1.val = 20
node_1.left = TreeNode(15)
node_1.right = TreeNode(7)
node_2 = TreeNode(3)
node_2.left = TreeNode(9)
node_2.right = node_1

print(solution().maximumDepthofBinaryTree(node_2))