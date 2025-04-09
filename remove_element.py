from typing import List

'''
    Remove all occurences of val in nums.
    Then return the number of elements in nums,
    not equal to val
'''

class Solution:
    def removeElement(self, num: List[int], val: int) -> int:
        k = 0
        for i in range(len(num) -1, -1, -1):
            if num[i] == val:
                num.pop(i)
                k += 1
                print("num after pop:", num)
        return len(num)
    
# example usage
nums = [3,2,2,3]
val = 3
solution = Solution()
result = solution.removeElement(nums, val)
print(result)  # Output: 2