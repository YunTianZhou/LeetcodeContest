"""
3780. Maximum Sum of Three Numbers Divisible by Three - Medium


You are given an integer array nums.

Your task is to choose exactly three integers from nums such that their sum is divisible by three.

Return the maximum possible sum of such a triplet. If no such triplet exists, return 0.



Example 1:

Input: nums = [4,2,3,1]

Output: 9

Explanation:

The valid triplets whose sum is divisible by 3 are:

 - (4, 2, 3) with a sum of 4 + 2 + 3 = 9.
 - (2, 3, 1) with a sum of 2 + 3 + 1 = 6.

Thus, the answer is 9.


Example 2:

Input: nums = [2,1,5]

Output: 0

Explanation:

No triplet forms a sum divisible by 3, so the answer is 0.



Constraints:

3 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List
from math import inf


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dp = [[-inf] * 3 for _ in range(4)]
        dp[0][0] = 0
        
        for x in nums:
            for i in range(3, 0, -1):
                for j in range(3):
                    k = (x + j) % 3
                    dp[i][k] = max(dp[i][k], dp[i - 1][j] + x)

        return 0 if dp[3][0] == -inf else dp[3][0]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumSum([4, 2, 3, 1]))  # 9

    # Example 2
    print(sol.maximumSum([2, 1, 5]))  # 0
