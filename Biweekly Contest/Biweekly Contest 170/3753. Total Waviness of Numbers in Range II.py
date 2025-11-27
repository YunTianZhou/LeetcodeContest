"""
3753. Total Waviness of Numbers in Range II - Hard


You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

 - A digit is a peak if it is strictly greater than both of its immediate neighbors.

 - A digit is a valley if it is strictly less than both of its immediate neighbors.

 - The first and last digits of a number cannot be peaks or valleys.

 - Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range [num1, num2].



Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:

 - 120: middle digit 2 is a peak, waviness = 1.
 - 121: middle digit 2 is a peak, waviness = 1.
 - 130: middle digit 3 is a peak, waviness = 1.
 - All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.


Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:

 - 198: middle digit 9 is a peak, waviness = 1.
 - 201: middle digit 0 is a valley, waviness = 1.
 - 202: middle digit 0 is a valley, waviness = 1.
 - All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.


Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.



Constraints:

1 <= num1 <= num2 <= 10^15
"""

from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num):
            s = list(map(int, str(num)))
            n = len(s)

            @cache
            def dfs(i, tight, wave, p, t):
                if i == n:
                    return wave

                res = 0
                for x in range(s[i] + 1 if tight else 10):
                    ntight = tight and x == s[i]
                    np = -1 if p == -1 and x == 0 else x
                    nt = 0 if p == -1 or x == p else 1 if x > p else 2
                    nw = wave
                    if p >= 0 and (t == 1 and p > x) or (t == 2 and p < x):
                        nw += 1
                    res += dfs(i + 1, ntight, nw, np, nt)
                    
                return res

            return dfs(0, True, 0, -1, 0)

        return solve(num2) - solve(num1 - 1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.totalWaviness(120, 130))  # 3

    # Example 2
    print(sol.totalWaviness(198, 202))  # 3

    # Example 3
    print(sol.totalWaviness(4848, 4848))  # 2
