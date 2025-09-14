"""
3621. Number of Integers With Popcount-Depth Equal to K I - Hard


You are given two integers n and k.

For any positive integer x, define the following sequence:

p0 = x
pi+1 = popcount(pi) for all i >= 0, where popcount(y) is the number of set bits (1's) in the binary representation of y.

This sequence will eventually reach the value 1.

The popcount-depth of x is defined as the smallest integer d >= 0 such that pd = 1.

For example, if x = 7 (binary representation "111"). Then, the sequence is: 7 → 3 → 2 → 1, so the popcount-depth of 7 is 3.

Your task is to determine the number of integers in the range [1, n] whose popcount-depth is exactly equal to k.

Return the number of such integers.



Example 1:

Input: n = 4, k = 1

Output: 2

Explanation:

The following integers in the range [1, 4] have popcount-depth exactly equal to 1:

x  Binary  Sequence
2  "10"    2 → 1
4  "100"   4 → 1
Thus, the answer is 2.


Example 2:

Input: n = 7, k = 2

Output: 3

Explanation:

The following integers in the range [1, 7] have popcount-depth exactly equal to 2:

x  Binary  Sequence
3  "11"    3 → 2 → 1
5  "101"   5 → 2 → 1
6  "110"   6 → 2 → 1
Thus, the answer is 3.



Constraints:

1 <= n <= 10^15
0 <= k <= 5
"""

from functools import cache


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        m = n.bit_length()
        dep = [0] * (m + 1)
        dep[0] = 64
        for i in range(2, m + 1):
            dep[i] = 1 + dep[i.bit_count()]
        
        @cache
        def dfs(i, free, cnt):
            if i == -1:
                return 1 if dep[cnt] + 1 == k else 0
            can_one = free or (n >> i & 1)
            res = dfs(i - 1, can_one, cnt)
            if can_one:
                res += dfs(i - 1, free, cnt + 1)
            return res

        return dfs(m - 1, False, 0) - (1 if k == 1 else 0)



if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.popcountDepth(4, 1))  # 2

    # Example 2
    print(sol.popcountDepth(7, 2))  # 3
