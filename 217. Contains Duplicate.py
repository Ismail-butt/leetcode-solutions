class Solution(object):
    def containsDuplicate(self, nums):
        # Concept (Check if Element is present in hashset or not)
        # take a hashset, and check if current element is found in hashset or not
        # if it not found in the hashset, add it else if it founds return True
        
        hashset = set()
        
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False

nums = [1,2,3,1]

print("Input: ", nums)
solution = Solution()
print("Output: ", solution.containsDuplicate(nums))