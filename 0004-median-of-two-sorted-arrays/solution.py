class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()

        if len(nums1)%2==0:
            ave=(nums1[int(len(nums1)/2-1)]+nums1[(int(len(nums1)/2))])/2
            return(ave)

        else:
            ave=(nums1[int(len(nums1)/2-0.5)])
            return(ave)
        
