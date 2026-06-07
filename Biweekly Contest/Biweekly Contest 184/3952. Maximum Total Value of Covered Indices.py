"""
3952. Maximum Total Value of Covered Indices - Medium


You are given an integer array nums of length n and a binary string s of length n, where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.

You may perform the following operation any number of times:

 - Choose a token currently located at index i, where i > 0, such that this token has not been moved before.

 - Move this token from index i to index i - 1.

An index is considered covered if it contains a token after all moves.

Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.



Example 1:

Input: nums = [9,2,6,1], s = "0101"

Output: 15

Explanation:

 - Initially, indices 1 and 3 contain tokens.

 - Move the token from index 3 to index 2.

 - Move the token from index 1 to index 0.

 - The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.


Example 2:

Input: nums = [5,1,4], s = "001"

Output: 4

Explanation:

 - Initially, only index 2 contains a token.

 - It is optimal to leave the token at index 2.

 - The covered index is [2], so the total value is nums[2] = 4.


Example 3:

Input: nums = [9,3,5], s = "011"

Output: 14

Explanation:

 - Initially, indices 1 and 2 contain tokens.

 - Move the token from index 1 to index 0.

 - The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 5 = 14.



Constraints:

1 <= n == nums.length == s.length <= 10^5
1 <= nums[i] <= 10^5
s[i] is either '0' or '1'
"""

from math import inf


class Solution:
    def maxTotal(self, nums: list[int], s: str) -> int:
        dp0, dp1 = -inf, 0
        for i, (x, c) in enumerate(zip(nums, s)):
            dp0, dp1 = (
                max(dp0, dp1) if c == "0" else (-inf if i == 0 else dp0 + nums[i - 1]),
                -inf if c == "0" else max(dp0, dp1) + nums[i]
            )
        return max(dp0, dp1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxTotal([9, 2, 6, 1], "0101"))  # 15

    # Example 2
    print(sol.maxTotal([5, 1, 4], "001"))  # 4

    # Example 3
    print(sol.maxTotal([9, 3, 5], "011"))  # 14
