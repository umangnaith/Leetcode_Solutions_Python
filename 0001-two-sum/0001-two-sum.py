class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if (nums[i]+nums[j])==target:
                        return i,j"""
        i,j=0,len(nums)-1
        for i in range(len(nums)):
            for j in range(len(nums)-1,0,-1):
                if j > i and nums[i]+nums[j] == target:
                    return ([i,j])
