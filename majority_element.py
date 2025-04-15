'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max_value = None
        count = 0
        for num in nums:
            if count == 0:
                max_value = num
            if max_value == num:
                count += 1
            else:
                count -= 1
        return max_value

solution = Solution()
nums = [2,2,1,1,1,2,2]
output = solution.majorityElement(nums)
print(output)