class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        values = dict()
        
        for i, elem in enumerate(nums):
            comp = target - elem
            
            if comp in values:
                return [values[comp], i]
            else:
                values[elem] = i
        
        return []

nums = [3,2,4]
target = 6

print("Input: ", nums)
solution = Solution()
print("Output: ", solution.twoSum(nums, target))