from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        Do not return anything, modify nums1 in-place instead

        You are given two integer arrays nums1 and nums2, 
        sorted in non-decreasing order, and two integers m and n, 
        representing the number of elements in nums1 and nums2 respectively
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        '''
        # Start from the end of nums1 and nums2
        i = m - 1
        j = n - 1
        k = m + n -1
        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1 

# example usage
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]