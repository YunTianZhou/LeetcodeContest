"""
3915. Maximum Sum of Alternating Subsequence With Distance at Least K - Hard


You are given an integer array nums of length n and an integer k.

Pick a subsequence with indices 0 <= i1 < i2 < ... < im < n such that:

 - For every 1 <= t < m, i[t+1] - i[t] >= k.

 - The selected values form a strictly alternating sequence. In other words, either:

    - nums[i1] < nums[i2] > nums[i3] < ..., or

    - nums[i1] > nums[i2] < nums[i3] > ...

A subsequence of length 1 is also considered strictly alternating. The score of a valid subsequence is the sum of its selected values.

Return an integer denoting the maximum possible score of a valid subsequence.



Example 1:

Input: nums = [5,4,2], k = 2

Output: 7

Explanation:

An optimal choice is indices [0, 2], which gives values [5, 2].

 - The distance condition holds because 2 - 0 = 2 >= k.

 - The values are strictly alternating because 5 > 2.

The score is 5 + 2 = 7.


Example 2:

Input: nums = [3,5,4,2,4], k = 1

Output: 14

Explanation:

An optimal choice is indices [0, 1, 3, 4], which gives values [3, 5, 2, 4].

 - The distance condition holds because each pair of consecutive chosen indices differs by at least k = 1.

 - The values are strictly alternating since 3 < 5 > 2 < 4.

The score is 3 + 5 + 2 + 4 = 14.


Example 3:

Input: nums = [5], k = 1

Output: 5

Explanation:

The only valid subsequence is [5]. A subsequence with 1 element is always strictly alternating, so the score is 5.



Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= n
"""


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, x: int):
        while idx <= self.n:
            self.tree[idx] = max(self.tree[idx], x)
            idx += idx & -idx

    def query(self, idx: int) -> int:
        mx = 0
        while idx > 0:
            mx = max(mx, self.tree[idx])
            idx -= idx & -idx
        return mx


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        xs = sorted(set(nums))
        rank = {x: i for i, x in enumerate(xs, start=1)}
        m = len(xs)

        dp_inc = [0] * n
        dp_dec = [0] * n
        bit_inc = BinaryIndexedTree(m)
        bit_dec = BinaryIndexedTree(m)
        for i in range(n):
            x = rank[nums[i]]
            if i >= k:
                j = i - k
                y = rank[nums[j]]
                bit_inc.update(m - y + 1, dp_inc[j])
                bit_dec.update(y, dp_dec[j])
            
            dp_inc[i] = bit_dec.query(x - 1) + nums[i]
            dp_dec[i] = bit_inc.query(m - x) + nums[i]

        return max(max(dp_inc), max(dp_dec))


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxAlternatingSum([5, 4, 2], 2))  # 7

    # Example 2
    print(sol.maxAlternatingSum([3, 5, 4, 2, 4], 1))  # 14

    # Example 3
    print(sol.maxAlternatingSum([5], 1))  # 5
