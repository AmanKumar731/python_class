class Solution:
    def removeElement(self, nums, val):

        while val in nums:
            nums.remove(val)

        return len(nums)
    
re = Solution()
nums = [3,2,2,3]
val = 3

k =re.removeElement(nums,val)
print(k)
print(nums)
print(val)

'''
# Kaise kaam karta hai?
nums = [3,2,2,3]
value check in the num and if 3 in num, then remove after that loop stop. 
'''


