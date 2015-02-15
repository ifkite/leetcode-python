# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        else:
            if root.left.val == root.right.val:
                return self.isSymmetricAss(root.left.left, root.right.right) and \
                    self.isSymmetricAss(root.left.right, root.right.left)
            else:
                return False

    def isSymmetricAss(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            if left.val == right.val:
                return self.isSymmetricAss(left.left, right.right) and \
                    self.isSymmetricAss(left.right, right.left)
            else:
                return False