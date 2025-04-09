from typing import List

# This code defines a class Solution with a method twoSum that finds two indices of numbers in a list that add up to a target value.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            subtracted = target - num
            if subtracted in num_map:
                return[num_map[subtracted], i]
            num_map[num] = i
        return []
            
nums = [2,7,11,15] 
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]