"""
3704. Count No-Zero Pairs That Sum to N - Hard


A no-zero integer is a positive integer that does not contain the digit 0 in its decimal representation.

Given an integer n, count the number of pairs (a, b) where:

 - a and b are no-zero integers.
 - a + b = n

Return an integer denoting the number of such pairs.



Example 1:

Input: n = 2

Output: 1

Explanation:

The only pair is (1, 1).


Example 2:

Input: n = 3

Output: 2

Explanation:

The pairs are (1, 2) and (2, 1).


Example 3:

Input: n = 11

Output: 8

Explanation:

The pairs are (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3), and (9, 2). Note that (1, 10) and (10, 1) do not satisfy the conditions because 10 contains 0 in its decimal representation.



Constraints:

2 <= n <= 10^15
"""

from functools import cache


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)

        def count_sum(x):
            if x < 2:
                return 0
            return min(x - 1, 19 - x)

        @cache
        def dfs(i, carry, zero):
            if i < 0:
                return 0 if carry else 1
            
            d = s[i] - carry

            if zero:
                if i > 0 and d == 0:
                    return 0
                return dfs(i - 1, d < 0, True)
            
            res = 0
            
            if i < m - 1:
                if d != 0:
                    res += 2 * dfs(i - 1, d < 0, True)
                elif i == 0:
                    res += 1

            res += count_sum(d) * dfs(i - 1, False, False)
            res += count_sum(10 + d) * dfs(i - 1, True, False)

            return res
        
        return dfs(m - 1, False, False)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countNoZeroPairs(2))  # 1

    # Example 2
    print(sol.countNoZeroPairs(3))  # 2

    # Example 3
    print(sol.countNoZeroPairs(11))  # 8
    