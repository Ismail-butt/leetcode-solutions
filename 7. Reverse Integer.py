import math
class Solution(object):
    def reverse(self, x):
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 - 1

        # Concept (mod & divide)
        # take the mod of no to get the last digit like 123 % 10, digit 3
        # then divide the no by 10 to cut the last digit like 123 / 10 = 12
        # res > MAX // 10 is cheking if result is greater than max
        # res == MAX // 10 and digit >= MAX % 10, this is checking if result is equal to
        # max and the current digit we get is bigget then the last digit of max, if
        # it happens, we return 0

        # if no is negative then we will convert into positive and imply our solution bcz
        # python is dumb, like -1 // 10 = -1
        flag = False
        if x < 0:
            flag = True
            x = x * -1
            MAX += 1 # bcz the diffrence b/w min and max is 1, and it's a neg value, so max + 1
        
        res = 0

        while x:
            digit = int(math.fmod(x, 10)) # python dumb -1 % 10 = 9
            x = int(x/10) # python dumb -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MAX % 10):
                return 0

            res = (res*10) + digit

        # to make it negative, bcz no was negative before
        if flag:
            res = res * -1
            
        return res

x = 123

print("Input: ", x)
solution = Solution()
print("Output: ", solution.reverse(x))
