"""
4041. Minimum Operations to Form Subset Sum II - Hard


You are given an integer array nums and an integer sum.

In one operation, choose an element with current value x and replace it with either 2 * x or floor(x / 2).

For each element, multiplication and division operations may be performed in any order.

Return the minimum number of operations needed so that some subset of the resulting array has a sum exactly equal to sum. If it is impossible, return -1.

The floor() function returns the integer part of the division.



Example 1:

Input: nums = [10,2], sum = 13

Output: 3

Explanation:

 - Divide nums[0] = 10 once: 10 -> 5, costing 1 operation.

 - Multiply nums[1] = 2 twice: 2 -> 4 -> 8, costing 2 operations.

 - After these operations, nums = [5, 8]. The subset {5, 8} sums to 13 using 3 operations in total.


Example 2:

Input: nums = [6,3], sum = 8

Output: 2

Explanation:

 - Turn nums[1] = 3 into 2 using 2 operations:

   - Divide nums[1] to get 1.

   - Multiply nums[1] = 1 to get 2.

 - After these operations, nums = [6, 2]. The subset {6, 2} sums to 8 using 2 operations in total.


Example 3:

Input: nums = [2,2], sum = 7

Output: -1

Explanation:

 - No sequence of operations lets a subset of nums sum to 7, so the answer is -1.



Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 500
1 <= sum <= 5000
"""

from math import inf


class Solution:
    def minOperations(self, nums: list[int], s: int) -> int:
        dp = [0] + [inf] * s
        
        for x in nums:
            costs = {}
            a = 0
            while (x >> a) > 0 and a < dp[s]:
                b = 0
                while (v := x >> a << b) <= s and a + b < dp[s]:
                    if v not in costs:
                        costs[v] = a + b
                    b += 1
                a += 1

            ndp = dp.copy()
            for i, c in costs.items():
                if ndp[s] <= c:
                    continue
                for j in range(i, s + 1):
                    if dp[j - i] + c < ndp[j]:
                        ndp[j] = dp[j - i] + c
            dp = ndp

        return -1 if dp[s] == inf else dp[s]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([10, 2], 13))  # 3

    # Example 2
    print(sol.minOperations([6, 3], 8))  # 2

    # Example 3
    print(sol.minOperations([2, 2], 7))  # -1
