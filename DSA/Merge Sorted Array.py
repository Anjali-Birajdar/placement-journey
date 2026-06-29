# Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()


num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]

solution = Solution()
solution.merge(num1, 3, num2, 3)
print(num1)
