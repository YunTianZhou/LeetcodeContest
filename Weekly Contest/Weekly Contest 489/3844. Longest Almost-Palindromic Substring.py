"""
3844. Longest Almost-Palindromic Substring - Medium


You are given a string s consisting of lowercase English letters.

A substring is almost-palindromic if it becomes a palindrome after removing exactly one character from it.

Return an integer denoting the length of the longest almost-palindromic substring in s.



Example 1:

Input: s = "abca"

Output: 4

Explanation:

Choose the substring "abca".

 - Remove "abca".

 - The string becomes "aba", which is a palindrome.

 - Therefore, "abca" is almost-palindromic.


Example 2:

Input: s = "abba"

Output: 4

Explanation:

Choose the substring "abba".

 - Remove "abba".

 - The string becomes "aba", which is a palindrome.

 - Therefore, "abba" is almost-palindromic.


Example 3:

Input: s = "zzabba"

Output: 5

Explanation:

Choose the substring "zzabba".

 - Remove "zabba".

 - The string becomes "abba", which is a palindrome.

 - Therefore, "zabba" is almost-palindromic.



Constraints:

2 <= s.length <= 2500
s consists of only lowercase English letters.
"""


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        def extend(i, j, k):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if k == 0:
                return j - i - 1
            else:
                return max(extend(i - 1, j, k - 1), extend(i, j + 1, k - 1))

        return min(n, max(extend(i // 2, (i + 1) // 2, 1) for i in range(2 * n - 1)))


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.almostPalindromic("abca"))  # 4

    # Example 2
    print(sol.almostPalindromic("abba"))  # 4

    # Example 3
    print(sol.almostPalindromic("zzabba"))  # 5
    