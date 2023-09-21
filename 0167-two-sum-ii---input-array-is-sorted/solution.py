class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=1
        while not numbers[left]+numbers[right]==target:
            if numbers[left]+numbers[right]<target:
                left+=1
                right+=1
            else:
                left-=1
        return(left+1,right+1)

        
