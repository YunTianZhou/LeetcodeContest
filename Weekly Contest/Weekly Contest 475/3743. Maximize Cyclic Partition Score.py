"""
3743. Maximize Cyclic Partition Score - Hard


You are given a cyclic array nums and an integer k.

Partition nums into at most k subarrays. As nums is cyclic, these subarrays may wrap around from the end of the array back to the beginning.

The range of a subarray is the difference between its maximum and minimum values. The score of a partition is the sum of subarray ranges.

Return the maximum possible score among all cyclic partitions.



Example 1:

Input: nums = [1,2,3,3], k = 2

Output: 3

Explanation:

 - Partition nums into [2, 3] and [3, 1] (wrapped around).

 - The range of [2, 3] is max(2, 3) - min(2, 3) = 3 - 2 = 1.

 - The range of [3, 1] is max(3, 1) - min(3, 1) = 3 - 1 = 2.

 - The score is 1 + 2 = 3.


Example 2:

Input: nums = [1,2,3,3], k = 1

Output: 2

Explanation:

 - Partition nums into [1, 2, 3, 3].

 - The range of [1, 2, 3, 3] is max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2.

 - The score is 2.


Example 3:

Input: nums = [1,2,3,3], k = 4

Output: 3

Explanation:

Identical to Example 1, we partition nums into [2, 3] and [3, 1]. Note that nums may be partitioned into fewer than k subarrays.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""

from typing import List
from math import inf


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def solve(nums):
            dp = [[-inf] * 3 for _ in range(k + 1)]
            for j in range(k + 1):
                dp[j][0] = 0
            for x in nums:
                for j in range(k, 0, -1):
                    dp[j][0] = max(dp[j][0], x + dp[j][1], -x + dp[j][2])
                    dp[j][1] = max(dp[j][1], -x + dp[j - 1][0])
                    dp[j][2] = max(dp[j][2], x + dp[j - 1][0])
            return dp[k][0]

        i = nums.index(max(nums))
        ans1 = solve(nums[i:] + nums[:i])
        ans2 = solve(nums[i + 1:] + nums[:i + 1])
        return max(ans1, ans2)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumScore([1, 2, 3, 3], 2))  # 3

    # Example 2
    print(sol.maximumScore([1, 2, 3, 3], 1))  # 2

    # Example 3
    print(sol.maximumScore([1, 2, 3, 3], 4))  # 3
    