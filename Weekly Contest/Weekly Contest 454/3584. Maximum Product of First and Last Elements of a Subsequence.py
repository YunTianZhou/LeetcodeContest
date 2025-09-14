"""
3584. Maximum Product of First and Last Elements of a Subsequence - Medium


You are given an integer array nums and an integer m.

Return the maximum product of the first and last elements of any subsequence of nums of size m.

 

Example 1:

Input: nums = [-1,-9,2,3,-2,-3,1], m = 1

Output: 81

Explanation:

The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.


Example 2:

Input: nums = [1,3,-5,5,6,-4], m = 3

Output: 20

Explanation:

The subsequence [-5, 6, -4] has the largest product of the first and last elements.


Example 3:

Input: nums = [2,-1,2,-6,5,2,-5,7], m = 2

Output: 35

Explanation:

The subsequence [5, 7] has the largest product of the first and last elements.

 

Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= m <= nums.length
"""

from typing import List
from math import inf


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)

        mini = nums[0]
        maxi = nums[0]
        res = -inf
        for i in range(m - 1, n):
            maxi = max(maxi, nums[i - m + 1])
            mini = min(mini, nums[i - m + 1])
            res = max(res, maxi * nums[i], mini * nums[i])

        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumProduct([-1, -9, 2, 3, -2, -3, 1], 1))  # 81

    # Example 2
    print(sol.maximumProduct([1, 3, -5, 5, 6, -4], 3))  # 20

    # Example 3
    print(sol.maximumProduct([2, -1, 2, -6, 5, 2, -5, 7], 2))  # 35
