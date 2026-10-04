"""
4071. Minimum Rotations to Dial a Number II - Medium


You are given an integer n and a string s of length n consisting of digits.

The dial contains the digits 0 through 9 in order and is circular, so 0 and 9 are adjacent. The pointer initially points to 0.

To dial each digit of s in order, rotate the pointer until it points to that digit. Each rotation moves the pointer to an adjacent digit, and you may rotate in either direction. Dialing a digit that the pointer already points to requires no rotations.

Before dialing, you may perform the following operation at most once:

Choose an index k such that 0 <= k < n and reverse the suffix s[k..n - 1].

Return the minimum total number of rotations needed to dial the string after optimally choosing whether to perform the operation and which suffix to reverse.



Example 1:

Input: n = 4, s = "1502"

Output: 9

Explanation:

Reverse the suffix starting at k = 1 to obtain "1205", then dial it.

Step   From   To     Rotations
1      0      1      1
2      1      2      1
3      2      0      2
4      0      5      5

The total is 1 + 1 + 2 + 5 = 9, which is the minimum total number of rotations.


Example 2:

Input: n = 4, s = "2916"

Output: 12

Explanation:

Choose not to reverse a suffix and dial "2916".

Step   From   To     Rotations
1      0      2      2
2      2      9      3
3      9      1      2
4      1      6      5

The total is 2 + 3 + 2 + 5 = 12, which is the minimum total number of rotations.


Example 3:

Input: n = 4, s = "4219"

Output: 6

Explanation:

Reverse the suffix starting at k = 0, which reverses the entire string, to obtain "9124", then dial it.

Step   From   To     Rotations
1      0      9      1
2      9      1      2
3      1      2      1
4      2      4      2

The total is 1 + 2 + 1 + 2 = 6, which is the minimum total number of rotations.



Constraints:

1 <= n == s.length <= 10^5
s consists only of digits '0' to '9'
"""


class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dst(x: int, y: int) -> int:
            d = abs(x - y)
            return min(d, 10 - d)

        total = prev = sub = 0
        last = int(s[-1])
        for x in map(int, s):
            d = dst(x, prev)
            total += d
            sub = max(sub, d - dst(last, prev))
            prev = x

        return total - sub


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minRotations(4, "1502"))  # 9

    # Example 2
    print(sol.minRotations(4, "2916"))  # 12

    # Example 3
    print(sol.minRotations(4, "4219"))  # 6
