"""
4000. Largest Integer With Given Digit Sum - Easy


You are given two non-negative integers n and s.

Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer exists, return -1.



Example 1:

Input: n = 2, s = 9

Output: 90

Explanation:

The largest integer with at most 2 digits that has a sum of digits of 9 is 90.


Example 2:

Input: n = 2, s = 19

Output: -1

Explanation:

There is no integer with at most 2 digits that has a sum of digits of 19, so the answer is -1.


Example 3:

Input: n = 5, s = 0

Output: 0

Explanation:

The only non-negative integer whose digits sum to 0 is 0.



Constraints:

1 <= n <= 5
0 <= s <= 100
"""


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1

        d, r = divmod(s, 9)

        ans = 10 ** d - 1
        if r > 0:
            ans = ans * 10 + r
            n -= 1

        return ans * 10 ** (n - d)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.largestInteger(2, 9))  # 90

    # Example 2
    print(sol.largestInteger(2, 19))  # -1

    # Example 3
    print(sol.largestInteger(5, 0))  # 0
