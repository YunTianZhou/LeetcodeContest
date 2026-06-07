"""
3956. Maximum Sum of M Non-Overlapping Subarrays I - Hard


You are given an integer array nums of length n, and three integers m, l, and r.

Your task is to select at least one and at most m non-overlapping subarrays from nums such that:

 - Each selected subarray has a length between [l, r] (inclusive).

 - The total sum of all selected subarrays is maximized.

Return the maximum total sum you can achieve.



Example 1:

Input: nums = [4,1,-5,2], m = 2, l = 1, r = 3

Output: 7

Explanation:

One optimal strategy is to:

 - Select the subarray [4, 1] with sum 4 + 1 = 5 and the subarray [2] with sum 2. Both subarrays have length between [l, r].

 - The total sum of these subarrays is 5 + 2 = 7, which is the maximum achievable sum with at most m = 2 subarrays.


Example 2:

Input: nums = [1,0,3,4], m = 2, l = 1, r = 2

Output: 8

Explanation:

One optimal strategy is to:

 - Select the subarray [1] with sum 1 and the subarray [3, 4] with sum 3 + 4 = 7. Both subarrays have length between [l, r].

 - The total sum of these subarrays is 1 + 7 = 8, which is the maximum achievable sum with at most m = 2 subarrays.


Example 3:

Input: nums = [-1,7,-4], m = 1, l = 2, r = 3

Output: 6

Explanation:

 - Select the subarray [-1, 7] from nums which has length between [l, r].

 - The total sum of this subarray is -1 + 7 = 6, which is the maximum achievable sum with at most m = 1 subarray.


Example 4:

Input: nums = [-3,-4,-1], m = 2, l = 1, r = 2

Output: -1

Explanation:

 - All subarrays of nums have negative sums. The optimal strategy is to select the subarray [-1], which has length between [l, r].

 - The total sum of this subarray is -1, which is the maximum achievable sum with at most m = 2 subarrays.



Constraints:

1 <= n == nums.length <= 1000
-10^9 <= nums[i] <= 10^9
1 <= m <= n
1 <= l <= r <= n
"""

from collections import deque
from itertools import accumulate
from math import inf


class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        ps = list(accumulate(nums, initial=0))
        
        prev = [0] * (n + 1)
        ans = -inf

        for _ in range(m):
            cur = [0] * (n + 1)
            dq = deque()
            
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    x = prev[j] - ps[j]
                    while dq and dq[-1][0] <= x:
                        dq.pop()
                    dq.append((x, j))
                
                while dq and dq[0][1] < i - r:
                    dq.popleft()
                
                cur[i] = cur[i - 1]
                if dq:
                    cost = ps[i] + dq[0][0]
                    ans = max(ans, cost)
                    cur[i] = max(cur[i], cost)
            
            prev = cur

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumSum([4, 1, -5, 2], 2, 1, 3))  # 7

    # Example 2
    print(sol.maximumSum([1, 0, 3, 4], 2, 1, 2))  # 8

    # Example 3
    print(sol.maximumSum([-1, 7, -4], 1, 2, 3))  # 6

    # Example 4
    print(sol.maximumSum([-3, -4, -1], 2, 1, 2))  # -1
