# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        else:
            q = [root]
            d = {root: None}#key:child node, value:parent node
            while len(q):
                t_node = q.pop(0)
                if t_node.left is not None:
                    q.append(t_node.left)
                    d[t_node.left] = t_node
                if t_node.right is not None:
                    q.append(t_node.right)
                    d[t_node.right] = t_node
                if t_node.left is None and t_node.right is None:
                    check_sum = t_node.val
                    while d[t_node]:
                        check_sum += d[t_node].val
                        t_node = d[t_node]
                    if check_sum == sum:
                        return True
            return False

# {1,-2,-3,1,3,-2,#,-1}, 2
# if __name__ == '__main__':
#    solution = Solution()
#    root = TreeNode(1)
#    n2 = TreeNode(-2)
#    n3 = TreeNode(-3)
#    n4 = TreeNode(1)
#    n5 = TreeNode(3)
#    n6 = TreeNode(-2)
#    n7 = TreeNode(-1)
#    root.left = n2
#    root.right = n3
#    n2.left = n4
#    n2.right = n5
#    n3.left = n6
#    n4.left = n7
#    print solution.hasPathSum(root,2)