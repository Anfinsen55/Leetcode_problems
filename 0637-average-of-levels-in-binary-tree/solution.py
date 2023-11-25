# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if root: res = [root.val] 
        else: return res
        queue = collections.deque()
        if root.right:
            queue.append((root.right, 1))
        if root.left:
            queue.append((root.left, 1))
        if len(queue) == 0: return res
        prevLevel = 1
        currSum = 0
        currCount = 0
        while queue:

            node = queue.popleft()
            val, level = node[0].val, node[1]
            if level != prevLevel:
                res.append(currSum / currCount)
                currSum = val
                currCount = 1
                prevLevel = level

            else:
                currSum += val
                currCount += 1

            if node[0].left:
                queue.append((node[0].left, level + 1))
            if node[0].right:
                queue.append((node[0].right, level + 1))

        res.append(currSum / currCount)
        return res
        
