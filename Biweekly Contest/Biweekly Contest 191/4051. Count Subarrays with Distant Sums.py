"""
4051. Count Subarrays with Distant Sums - Hard


You are given an integer array nums and two integers goal and k.

A subarray nums[i..j] is considered distant if the absolute difference between its sum and goal is at least k.

Return the number of distant subarrays.



Example 1:

Input: nums = [1,2,1], goal = 4, k = 1

Output: 5

Explanation:

The distant subarrays for k = 1 are:

i  j  nums[i..j]  Sum  abs(sum - goal)
0  0  [1]         1    3
1  1  [2]         2    2
2  2  [1]         1    3
0  1  [1, 2]      3    1
1  2  [2, 1]      3    1

Thus, the answer is 5.


Example 2:

Input: nums = [2,-1,3], goal = 2, k = 2

Output: 2

Explanation:

The distant subarrays for k = 2 are:

i  j  nums[i..j]  Sum  abs(sum - goal)
1  1  [-1]        -1   3
0  2  [2, -1, 3]  4    2

Thus, the answer is 2.


Example 3:

Input: nums = [-3,1,2], goal = 0, k = 3

Output: 2

Explanation:

The distant subarrays for k = 3 are:

i  j  nums[i..j]  Sum  abs(sum - goal)
0  0  [-3]        -3   3
1  2  [1, 2]      3    3

Thus, the answer is 2.



Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
-10^9 <= goal <= 10^9
0 <= k <= 10^9
"""

from bisect import bisect_left, bisect_right
from itertools import accumulate


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        pref = list(accumulate(nums, initial=0))
        xs = sorted(set(pref))

        bit = BinaryIndexedTree(len(xs) + 1)
        ans = 0
        for i, x in enumerate(pref):
            l = bisect_right(xs, x - goal - k)
            r = bisect_left(xs, x - goal + k) - 1

            sub = bit.range_query(l + 1, r + 1) if l <= r else 0
            ans += i - sub

            bit.update(bisect_left(xs, x) + 1, 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.distantSubarrays([1, 2, 1], 4, 1))  # 5

    # Example 2
    print(sol.distantSubarrays([2, -1, 3], 2, 2))  # 2

    # Example 3
    print(sol.distantSubarrays([-3, 1, 2], 0, 3))  # 2
