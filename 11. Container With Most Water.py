class Solution(object):
    def maxArea(self, height):
        # Concept (Left & Right pointer)
        # take two indices, left will point to start & right to end of the array
        # height will be minmum of height[l], height[r] i.e 1,3 height = 1
        # width will be right - left: width = r -l
        # if height[l] is less then height[r], then l will be moved else right
        
        res = 0  
        l, r = 0, len(height) - 1
        
        while l < r:
            h = min(height[l], height[r])
            area = (r - l) * h
            res = max(area, res)
            
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        
        return res

height = [1,8,6,2,5,4,8,3,7]

print("Input: ", height)
solution = Solution()
print("Output: ", solution.maxArea(height))