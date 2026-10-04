"""
4073. Count Good Strings - Hard


You are given an integer n.

A string is considered good if it consists only of the characters 'a' and 'b', and one of the following holds:

 - It contains exactly one distinct character, and its length is odd.

 - It can be written as s = s1 + s2, where s1 and s2 are non-empty good strings, and the last character of s1 is different from the first character of s2.

Return the number of good strings of length n, modulo 10^9 + 7.

Here, + denotes string concatenation.



Example 1:

Input: n = 4

Output: 6

Explanation:

 - The good strings are "aaab", "abbb", "baaa", "bbba", "abab", and "baba".

 - For example, "aaab" = "aaa" + "b". Both parts are good because each contains one distinct character and has odd length, and their characters at the boundary are different.

 - Also, "ab" = "a" + "b" is good, so "abab" = "ab" + "ab" is good because the boundary characters are different.

 - Thus, the answer is 6.


Example 2:

Input: n = 3

Output: 4

Explanation:

The good strings are "aaa", "bbb", "aba", and "bab". Thus, the answer is 4.


Example 3:

Input: n = 2

Output: 2

Explanation:

The good strings are "ab" and "ba". Thus, the answer is 2.



Constraints:

1 <= n <= 10^15
"""


class Solution:
    def countGoodStrings(self, n: int) -> int:
        mod = 10 ** 9 + 7

        f0, f1 = 0, 1
        for i in range(n.bit_length() - 1, -1, -1):
            f0, f1 = f0 * (2 * f1 - f0) % mod, (f0 * f0 + f1 * f1) % mod
            if n >> i & 1:
                f0, f1 = f1, (f0 + f1) % mod
        
        return f0 * 2 % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countGoodStrings(4))  # 6

    # Example 2
    print(sol.countGoodStrings(3))  # 4

    # Example 3
    print(sol.countGoodStrings(2))  # 2
