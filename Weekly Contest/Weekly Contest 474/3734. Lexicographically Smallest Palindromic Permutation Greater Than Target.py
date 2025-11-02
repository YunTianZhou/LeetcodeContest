"""
3734. Lexicographically Smallest Palindromic Permutation Greater Than Target - Hard


You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.



Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

The lexicographically smallest permutation that is strictly greater than target is "baab".


Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

None of them is lexicographically strictly greater than target. Therefore, the answer is "".


Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".


Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

The only palindromic permutation of s is "aca".

"aca" is strictly greater than target. Therefore, the answer is "aca".



Constraints:

1 <= n == s.length == target.length <= 300
s and target consist of only lowercase English letters.
"""

from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2
        cnt = Counter(s)

        def valid():
            return all(x >= 0 for x in cnt.values())

        center = ""
        for ch, c in cnt.items():
            if c % 2:
                if center:
                    return ""
                center = ch
                cnt[ch] -= 1

        ans = list(target)
        for i in range(half):
            cnt[target[i]] -= 2
            ans[n - i - 1] = target[i]
        if n % 2:
            ans[half] = center

        if valid() and (t := "".join(ans)) > target:
            return t

        for i in range(half - 1, -1, -1):
            c = target[i]
            cnt[c] += 2

            if not valid():
                continue

            for j in range(ord(c) - ord("a") + 1, 26):
                d = chr(j + ord("a"))

                if cnt[d] < 2:
                    continue

                cnt[d] -= 2
                ans[i] = ans[n - i - 1] = d

                curr = "a"
                for k in range(i + 1, half):
                    while cnt[curr] < 2:
                        curr = chr(ord(curr) + 1)
                    ans[k] = ans[n - k - 1] = curr
                    cnt[curr] -= 2

                return "".join(ans)

        return ""


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.lexPalindromicPermutation("baba", "abba"))  # "baab"

    # Example 2
    print(sol.lexPalindromicPermutation("baba", "bbaa"))  # ""

    # Example 3
    print(sol.lexPalindromicPermutation("abc", "abb"))  # ""

    # Example 4
    print(sol.lexPalindromicPermutation("aac", "abb"))  # "aca"
