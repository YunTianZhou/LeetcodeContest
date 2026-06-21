"""
3966. Count Good Integers in a Range - Hard


You are given three integers l, r and k.

A number is considered good if the absolute difference between every pair of adjacent digits is at most k.

Return the number of good integers in the range [l, r] (inclusive).

The absolute difference between values x and y is defined as abs(x - y).



Example 1:

Input: l = 10, r = 15, k = 1

Output: 3

Explanation:

 - The good integers in the range are 10, 11, and 12.

 - For 10, abs(1 - 0) = 1.

 - For 11, abs(1 - 1) = 0.

 - For 12, abs(1 - 2) = 1.

 - All these differences are at most k = 1. Thus, the answer is 3.


Example 2:

Input: l = 201, r = 204, k = 2

Output: 2

Explanation:

 - The good integers in the range are 201 and 202.

 - For 201, abs(2 - 0) = 2 and abs(0 - 1) = 1.

 - For 202, abs(2 - 0) = 2 and abs(0 - 2) = 2.

 - Thus, the answer is 2.



Constraints:

10 <= l <= r <= 10^15
0 <= k <= 9
"""

from functools import cache


class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        s_high = list(map(int, str(r)))

        n = len(s_high)
        s_low = list(map(int, str(l).zfill(n)))

        @cache
        def dfs(i, zero, tight_l, tight_r, p):
            if i == n:
                return 1
            
            low = max(s_low[i] if tight_l else 0, p - k)
            high = min(s_high[i] if tight_r else 9, p + k if not zero else 9)

            ans = 0
            for x in range(low, high + 1):
                ntl = tight_l and x == s_low[i]
                ntr = tight_r and x == s_high[i]
                nzero = zero and x == 0
                ans += dfs(i + 1, nzero, ntl, ntr, x)
            
            return ans

        return dfs(0, True, True, True, 0)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.goodIntegers(10, 15, 1))  # 3

    # Example 2
    print(sol.goodIntegers(201, 204, 2))  # 2
