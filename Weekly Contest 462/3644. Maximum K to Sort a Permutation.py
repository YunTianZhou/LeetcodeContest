"""
3644. Maximum K to Sort a Permutation - Medium


You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

A permutation is a rearrangement of all the elements of an array.



Example 1:

Input: nums = [0,3,2,1]

Output: 1

Explanation:

Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].


Example 2:

Input: nums = [0,1,3,2]

Output: 2

Explanation:

Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2, resulting in a sorted permutation: [0, 1, 2, 3].


Example 3:

Input: nums = [3,2,1,0]

Output: 0

Explanation:

Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k.



Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.
"""

from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        
        value = -1
        for i, x in enumerate(sorted(nums)):
            if nums[i] != x:
                value &= x
                
        return 0 if value == -1 else value


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sortPermutation([0, 3, 2, 1]))  # 1

    # Example 2
    print(sol.sortPermutation([0, 1, 3, 2]))  # 2

    # Example 3
    print(sol.sortPermutation([3, 2, 1, 0]))  # 0
    