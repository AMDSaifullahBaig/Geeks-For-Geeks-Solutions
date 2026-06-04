class Solution:
	def twoSum(self, arr, target):
		hash=set()
		for i in range(len(arr)):
		    complement=target-arr[i]
		    if complement in hash:
		        return True
		    hash.add(arr[i])
		return False