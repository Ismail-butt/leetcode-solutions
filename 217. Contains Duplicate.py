class Solution(object):
    def containsDuplicate(self, nums):
        # Concept (Check if Element is present in list or not)
        # we can use list/hashset/dict
        # take a list, and check if current element is found in list or not
        # if it not found in the list, add it else if it founds return True
        
        li = []
        
        for i in range(len(nums)):
            if nums[i] in li:
                return True
            li.append(nums[i])
        return False

nums = [1,2,3,1]

print("Input: ", nums)
solution = Solution()
print("Output: ", solution.containsDuplicate(nums))