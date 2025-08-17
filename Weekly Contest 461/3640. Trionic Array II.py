"""
3640. Trionic Array II - Hard


You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.

Return the maximum sum of any trionic subarray in nums.



Example 1:

Input: nums = [0,-2,-1,-3,0,2,-1]

Output: -4

Explanation:

Pick l = 1, p = 2, q = 3, r = 5:

nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.


Example 2:

Input: nums = [1,4,2,7]

Output: 14

Explanation:

Pick l = 0, p = 1, q = 2, r = 3:

nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
Sum = 1 + 4 + 2 + 7 = 14.
 


Constraints:

4 <= n = nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
It is guaranteed that at least one trionic subarray exists.
"""

from typing import List
from math import inf


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        dec_len = [1] * n
        dec = nums.copy()
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dec_len[i] = dec_len[i - 1] + 1
                dec[i] += dec[i - 1]

        inc = nums.copy()
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] += max(0, inc[i - 1])

        rev_inc = nums.copy()
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                rev_inc[i] += max(0, rev_inc[i + 1])

        ans = -inf
        for q in range(1, n - 1):
            if nums[q] >= nums[q + 1] or dec_len[q] <= 1:
                continue
            p = q - dec_len[q] + 1
            if p == 0 or nums[p - 1] >= nums[p]:
                continue
            curr = inc[p - 1] + dec[q] + rev_inc[q + 1]
            ans = max(ans, curr)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSumTrionic([0, -2, -1, -3, 0, 2, -1]))  # -4

    # Example 2
    print(sol.maxSumTrionic([1, 4, 2, 7]))  # 14
