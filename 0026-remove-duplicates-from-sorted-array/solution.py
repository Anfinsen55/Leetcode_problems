class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for m in range(1,len(nums)):
            if nums[m]!= nums[m-1]:
                nums[l]=nums[m]
                l+=1
        return l
