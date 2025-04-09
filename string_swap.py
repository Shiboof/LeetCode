class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))
        if len(diff) != 2:
            return False
        return diff[0] == diff[1][::-1]
    
# Example usage
s1 = "bank"
s2 = "kanb"
solution = Solution()
result = solution.areAlmostEqual(s1, s2)
print(result)  # Output: True