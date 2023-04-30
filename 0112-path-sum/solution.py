# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs_sum(curr=None, sumTill=0):

            if curr:
                sumTill += curr.val
                left = dfs_sum(curr.left, sumTill)
                right = False
                if not left:
                    right = dfs_sum(curr.right, sumTill)


                if curr.left == None and curr.right == None:
                    return sumTill == targetSum
                return left or right
            return False
        return dfs_sum(root)

