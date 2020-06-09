class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class solution:
    def Symmetric(self,root1,root2):
        ans = True
        if (root1==None and root2==None):
            return True
        elif((root1==None) or (root2==None) or (root1.val != root2.val)):
            return False

        ans1 = self.Symmetric(root1.left,root2.right)
        ans2 = self.Symmetric(root1.right,root2.left)
        return ans1 and ans2

    def isSymmetric(self,root):
        if not root:
            return False
        return self.Symmetric(root.left,root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.left = TreeNode(3)
print(solution().isSymmetric(root))
