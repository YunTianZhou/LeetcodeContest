"""
3702. Longest Subsequence With Non-Zero Bitwise XOR - Medium


You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.



Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.


Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

from typing import List
from functools import reduce
from operator import xor


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        if all(x == 0 for x in nums):
            return 0
        elif reduce(xor, nums) == 0:
            return n - 1
        else:
            return n
            

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestSubsequence([1, 2, 3]))  # 2

    # Example 2
    print(sol.longestSubsequence([2, 3, 4]))  # 3
