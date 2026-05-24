"""
3937. Minimum Operations to Make Array Modulo Alternating I - Medium


You are given an integer array nums and an integer k.

In one operation, you can increase or decrease any element of nums by 1.

An array is called modulo alternating if there exist two distinct integers x and y (0 <= x, y < k) such that:

 - For every even index i, nums[i] % k == x

 - For every odd index i, nums[i] % k == y

Return the minimum number of operations required to make nums modulo alternating.



Example 1:

Input: nums = [1,4,2,8], k = 3

Output: 2

Explanation:


 - Let's choose x = 1 for even indices and y = 2 for odd indices.

 - Perform the following operations:

    - Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8].
    - Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8].

 - Now, for even indices, nums[i] % k = 1, and for odd indices, nums[i] % k = 2.

 - Thus, the total number of operations required is 2.


Example 2:

Input: nums = [1,1,1], k = 3

Output: 1

Explanation:

 - Incrementing nums[1] by 1 gives nums = [1, 2, 1], which satisfies the condition with x = 1 and y = 2.

 - Thus, the total number of operations required is 1.



Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 10^9
2 <= k <= 100
"""

from bisect import bisect_left, bisect_right
from itertools import accumulate
from math import inf


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        def solve(nums):
            n = len(nums)
            nums = sorted(x % k for x in nums)
            
            a = [nums[i % n] + k * (i // n) for i in range(n * 3)]
            ps = list(accumulate(a, initial=0))

            cand = set()
            for x in nums:
                cand.add(x)
                cand.add((x - 1) % k)
                cand.add((x + 1) % k)
            
            dl = k // 2
            dr = (k - 1) // 2

            top1 = top2 = inf
            best = -1
            for x in cand:
                x += k
                mid = bisect_left(a, x)
                l = bisect_left(a, x - dl)
                r = bisect_right(a, x + dr)

                cost = (x * (mid - l) - (ps[mid] - ps[l]) +
                       (ps[r] - ps[mid]) - x * (r - mid))
                
                if cost < top1:
                    top2 = top1
                    top1 = cost
                    best = x
                elif cost < top2:
                    top2 = cost
            
            return best, top1, top2

        x, x_top1, x_top2 = solve(nums[::2])
        y, y_top1, y_top2 = solve(nums[1::2])

        if x == y:
            return min(x_top1 + y_top2, x_top2 + y_top1)
        else:
            return x_top1 + y_top1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([1, 4, 2, 8], 3))  # 2

    # Example 2
    print(sol.minOperations([1, 1, 1], 3))  # 1
