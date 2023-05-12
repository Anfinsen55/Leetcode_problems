class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		res=0
		presum=0
		dict1={0:1}

		for i in  nums:
			presum = presum + i

			if (presum-k) in dict1:
				res = res + dict1[presum-k]

			if presum not in dict1:
				dict1[presum] = 1
			else:
				dict1[presum] = dict1[presum]+1

		return res
