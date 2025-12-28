"""
3791. Number of Balanced Integers in a Range - Hard


You are given two integers low and high.

An integer is called balanced if it satisfies both of the following conditions:

 - It contains at least two digits.

 - The sum of digits at even positions is equal to the sum of digits at odd positions (the leftmost digit has position 1).

Return an integer representing the number of balanced integers in the range [low, high] (both inclusive).



Example 1:

Input: low = 1, high = 100

Output: 9

Explanation:

The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.


Example 2:

Input: low = 120, high = 129

Output: 1

Explanation:

Only 121 is balanced because the sum of digits at even and odd positions are both 2.


Example 3:

Input: low = 1234, high = 1234

Output: 0

Explanation:

1234 is not balanced because the sum of digits at odd positions (1 + 3 = 4) does not equal the sum at even positions (2 + 4 = 6).



Constraints:

1 <= low <= high <= 10^15
"""

from functools import cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def solve(limit):
            s = list(map(int, str(limit)))
            n = len(s)

            @cache
            def dfs(i, diff, parity, tight):
                if i == n:
                    return 1 if diff == 0 else 0

                ans = 0
                for x in range((s[i] + 1 if tight else 10)):
                    d = diff + (x if parity else -x)
                    p = not parity
                    t = tight and x == s[i]
                    ans += dfs(i + 1, d, p, t)

                return ans

            return dfs(0, 0, True, True)

        return solve(high) - solve(low - 1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countBalanced(1, 100))  # 9

    # Example 2
    print(sol.countBalanced(120, 129))  # 1

    # Example 3
    print(sol.countBalanced(1234, 1234))  # 0

