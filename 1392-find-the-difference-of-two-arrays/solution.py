class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1,list2,list3=[],[],[]
        for i in nums1:
            if i in nums2:
                continue
            else:
                list2.append(i)
        for j in nums2:
            if j in nums1:
                continue
            else:
                list3.append(j)
        list1.append(list(set(list2)))
        list1.append(list(set(list3)))
        return list1
