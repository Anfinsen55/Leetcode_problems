class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Arr1=sorted(nums1)
        Arr2=sorted(nums2)

        i=0
        j=0

        result=[]
        while i<len(Arr1) and j<len(Arr2):
            if Arr1[i] < Arr2[j]:
                i += 1
            elif Arr2[j] < Arr1[i]:
                j += 1
            else:
                result.append(Arr1[i])
                i += 1
                j += 1
        return result
