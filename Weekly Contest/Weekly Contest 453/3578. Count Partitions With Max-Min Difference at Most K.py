"""
3578. Count Partitions With Max-Min Difference at Most K - Medium


You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]


Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 


Constraints:

2 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^9
0 <= k <= 10^9
"""

from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        min_q = deque()
        max_q = deque()
        j = 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i, x in enumerate(nums):
            while min_q and nums[min_q[-1]]> x:
                min_q.pop()
            min_q.append(i)

            while max_q and nums[max_q[-1]] < x:
                max_q.pop()
            max_q.append(i)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                if min_q[0] == j:
                    min_q.popleft()
                if max_q[0] == j:
                    max_q.popleft()
                j += 1

            dp[i + 1] = (dp[i] * 2 - dp[j - 1]) % mod

        return (dp[n] - dp[n - 1]) % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countPartitions([9, 4, 1, 3, 7], 4))  # 6

    # Example 2
    print(sol.countPartitions([3, 3, 4], 0))  # 2
