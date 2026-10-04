"""
4072. Maximum Alternating Subarray Sum With One Deletion - Medium


You are given an integer array nums.

You may delete at most one element from nums, then choose a subarray of the resulting array.

Return the maximum possible alternating sum of the chosen subarray.

The alternating sum of an array is the sum of its elements at even indices minus the sum of its elements at odd indices. The chosen subarray is reindexed starting from 0 before calculating its alternating sum.



Example 1:

Input: nums = [5,-5,1]

Output: 11

Explanation:

Choose not to delete an element and select the entire array. Its alternating sum is 5 - (-5) + 1 = 11, which is the maximum possible.


Example 2:

Input: nums = [10,-5,-100]

Output: 110

Explanation:

Delete nums[1] = -5 to obtain [10,-100], then select the entire resulting array. Its alternating sum is 10 - (-100) = 110, which is the maximum possible.


Example 3:

Input: nums = [4,7]

Output: 7

Explanation:

Choose not to delete an element and select the subarray [7]. Its alternating sum is 7, which is the maximum possible.



Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""

from math import inf


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        dp = [0] * 4

        ans = -inf
        for x in reversed(nums):
            ans = max(ans, x + dp[3])

            dp = [
                max(0, x + dp[1]), max(0, -x + dp[0]),
                max(x + dp[3], dp[0]), max(-x + dp[2], dp[1])
            ]

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxAlternatingSum([5, -5, 1]))  # 11

    # Example 2
    print(sol.maxAlternatingSum([10, -5, -100]))  # 110

    # Example 3
    print(sol.maxAlternatingSum([4, 7]))  # 7
