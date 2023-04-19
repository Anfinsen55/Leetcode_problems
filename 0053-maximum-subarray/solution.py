class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_len= float('-inf')
        max_value=0

        for num in nums:
            max_value += num
            max_len = max(max_len, max_value)
            max_value = max(max_value, 0)
        return max_len
