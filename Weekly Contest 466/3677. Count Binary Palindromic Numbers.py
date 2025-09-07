"""
3677. Count Binary Palindromic Numbers - Hard


You are given a non-negative integer n.

A non-negative integer is called binary-palindromic if its binary representation (written without leading zeros) reads the same forward and backward.

Return the number of integers k such that 0 <= k <= n and the binary representation of k is a palindrome.

Note: The number 0 is considered binary-palindromic, and its representation is "0".



Example 1:

Input: n = 9

Output: 6

Explanation:

The integers k in the range [0, 9] whose binary representations are palindromes are:

0 → "0"
1 → "1"
3 → "11"
5 → "101"
7 → "111"
9 → "1001"

All other values in [0, 9] have non-palindromic binary forms. Therefore, the count is 6.


Example 2:

Input: n = 0

Output: 1

Explanation:

Since "0" is a palindrome, the count is 1.



Constraints:

0 <= n <= 10^15
"""


class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        m = n.bit_length()

        def solve(m, k):
            upper = 0
            for i in range(k):
                nxt = upper | (1 << i) | (1 << (m - i - 1))
                if nxt <= n:
                    upper = nxt
            return upper >> (m - k)
        
        return solve(m, (m + 1) // 2) + (1 << (m // 2))


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countBinaryPalindromes(9))  # 6

    # Example 2
    print(sol.countBinaryPalindromes(0))  # 1
    