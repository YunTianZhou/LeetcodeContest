"""
3671. Sum of Beautiful Subsequences - Hard


You are given an integer array nums of length n.

For every positive integer g, we define the beauty of g as the product of g and the number of strictly increasing subsequences of nums whose greatest common divisor (GCD) is exactly g.

Return the sum of beauty values for all positive integers g.

Since the answer could be very large, return it modulo 10^9 + 7.



Example 1:

Input: nums = [1,2,3]

Output: 10

Explanation:

All strictly increasing subsequences and their GCDs are:

Subsequence  GCD
[1]          1
[2]          2
[3]          3
[1,2]        1
[1,3]        1
[2,3]        1
[1,2,3]      1

Calculating beauty for each GCD:

GCD  Count of subsequences  Beauty (GCD x Count)
1    5                      1 x 5 = 5
2    1                      2 x 1 = 2
3    1                      3 x 1 = 3

Total beauty is 5 + 2 + 3 = 10.


Example 2:

Input: nums = [4,6]

Output: 12

Explanation:

All strictly increasing subsequences and their GCDs are:

Subsequence  GCD
[4]          4
[6]          6
[4,6]        2

Calculating beauty for each GCD:

GCD  Count of subsequences  Beauty (GCD x Count)
2    1                      2 x 1 = 2
4    1                      4 x 1 = 4
6    1                      6 x 1 = 6

Total beauty is 2 + 4 + 6 = 12.



Constraints:

1 <= n == nums.length <= 10^4
1 <= nums[i] <= 7 * 10^4
"""

from typing import List


MOD = 10 ** 9 + 7
MAX = 7 * 10 ** 4
divisors = [[] for _ in range(MAX + 1)]
for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisors[j].append(i)


class TimeZoneBinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.now = 0
        self.tree = [0] * (n + 1)
        self.time = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            if self.time[idx] < self.now:
                self.time[idx] = self.now
                self.tree[idx] = 0
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            if self.time[idx] == self.now:
                total += self.tree[idx]
            idx -= idx & -idx
        return total % MOD

    def range_query(self, left: int, right: int) -> int:
        return (self.query(right) - self.query(left - 1)) % MOD

    def reset(self):
        self.now += 1


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        m = max(nums)
        bit = TimeZoneBinaryIndexedTree(m + 1)

        def count(nums):
            bit.reset()
            ans = 0
            for x in nums:
                curr = 1 + bit.query(x - 1)
                ans += curr
                bit.update(x, curr)
            return ans % MOD

        groups = [[] for _ in range(m + 1)]
        for x in nums:
            for d in divisors[x]:
                groups[d].append(x)

        f = [0] * (m + 1)
        ans = 0
        for i in range(m, 0, -1):
            f[i] = count(groups[i])
            for j in range(i + i, m + 1, i):
                f[i] -= f[j]
            ans += i * f[i]
        
        return ans % MOD


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.totalBeauty([1, 2, 3]))  # 10

    # Example 2
    print(sol.totalBeauty([4, 6]))  # 12
